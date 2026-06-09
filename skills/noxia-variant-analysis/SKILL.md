---
name: noxia-variant-analysis
description: Variant analysis workflow for rare disease cases in Noxia — covers QC review, full variant list retrieval and phenotype-driven scan (not rank-driven), candidate shortlisting by clinical criteria, variant detail retrieval, ranking cross-reference, and opportunistic classification. Use when a case is ready and HPO terms are set, and the goal is to identify the causative variant before reporting.
---

# Noxia Variant Analysis

## Scope

QC check → case overview → shortlist candidates → assess top genes.  
Starts after intake is complete (`status = ready`, HPO set).  
ACMG classification and reporting are handled separately.  
**Important:** never call `classify_variant` without the user's explicit permission. Present the proposed ACMG criteria, classification, and reasoning first — wait for the user to approve before submitting to Noxia. After submission, remind the user to also approve the classification in the Noxia web UI (MCP-submitted classifications require manual review and confirmation before they are finalized).

---

## Step 1 — QC check

**Primary path — dedicated MCP tool:**

```
mcp__noxia__get_case_qc(case_id=<id>)
```

Returns the full QC report including all per-sample metrics and a top-level `qc_passed` boolean.

**Quick check — `get_case` flag:**  
`mcp__noxia__get_case(case_id=<id>)` also returns a `qc_passed` field. Use it as a fast pre-flight signal before fetching the full report. If `qc_passed=false`, always call `get_case_qc` for the detail before deciding how to proceed.

**REST fallback (if MCP unavailable):**

```bash
curl -sS -b /tmp/jar http://127.0.0.1:8000/api/cases/<id>/qc/report | python3 -m json.tool
```

| Metric | Threshold | Risk if failed |
|---|---|---|
| Mean coverage | ≥30× WES, ≥20× WGS | Variants missed in low-coverage regions |
| % bases ≥20× | ≥95% | High false-negative rate |
| Ti/Tv ratio | 2.0–2.2 WES, 2.0–2.1 WGS | Contamination or pipeline error |
| Heterozygosity rate | Within expected range | Excess → contamination; deficit → inbreeding |

**If QC fails — STOP and inform the user.** Do not proceed until they explicitly confirm. Document the concern in `clinical_summary` if proceeding.

---

## Step 2 — Case overview

```
mcp__noxia__summarize_case_variants(case_id=<id>)
```

Returns total counts, consequence-class breakdown, and engine-flagged signals. Use to gauge scale and spot obvious hits before drilling in.

---

## Step 3 — Retrieve and scan the full candidate list

**Retrieve first, rank later.** Pull the complete recommended list before forming any shortlist.

**Default query:** use the `"recommended"` preset and **exhaust all pages — this is mandatory, not optional.** The preset is already a conservative filter; do not stop at page 1:

```
mcp__noxia__query_variants(case_id=<id>, filter={"preset": "recommended"})
# → repeat with next_cursor until cursor is null
```

If the case has no project (`project_id: null`), the preset errors — fall back to consequence/impact filters:

```
mcp__noxia__query_variants(case_id=<id>, filter={"impact": "HIGH"})
```

### 3a — Phenotype-driven scan across the whole list

Once you have the full list, **do not evaluate it top-to-bottom by rank.** Instead apply a clinical lens across all returned variants simultaneously:

1. **Consequence sweep** — flag every LoF variant (stop_gained, frameshift, splice_donor, splice_acceptor, start_lost) regardless of rank or `in_report` status. LoF in a haploinsufficiency gene is clinically significant even at rank 50+.
2. **HPO-gene overlap** — for each gene in the list, ask whether its known disease association matches the proband's HPO terms. Flag any gene whose disease phenotype matches ≥2 HPO terms, regardless of ranking.
3. **Inheritance-mode fit** — XLR hemizygous hits in males are fully penetrant (check chrX variants); AD LoF variants are candidates even as singletons; AR requires biallelic evidence (check for compound-het pairs in the same gene).
4. **Rarity confirmation** — deprioritise variants with gnomAD AF >0.1% (>0.01% for AD dominant-negative or severe phenotypes).

**Critical:** A variant at rank 29 that is a frameshift in a known ID gene with an exact HPO match is a stronger candidate than a rank-3 VUS missense with a non-matching phenotype. Rank is a tiebreaker within a tier, not a clinical verdict.

### 3b — Mandatory explicit LoF sweep (engine blind-spot guard)

**Always run this query, regardless of what the recommended preset returned:**

```
mcp__noxia__query_variants(case_id=<id>, filter={
  "consequence": ["frameshift_variant", "stop_gained",
                  "splice_donor_variant", "splice_acceptor_variant", "start_lost"],
  "max_gnomad_af": 0.001
})
# → paginate until cursor is null
```

**Why this is required — engine structural blind spot:** the prioritization engine scores variants using variant-level pathogenicity predictors (REVEL, SpliceAI, ClinVar). Novel frameshifts and stop-gained variants have no REVEL score and often no ClinVar entry, so the engine returns `log10LR ≈ −4` (floor) and `pathogenicity_reason: "No variant-level evidence"`. A de novo frameshift in a well-established haploinsufficiency gene will land at rank 30+ and be stored as VUS despite satisfying PVS1 + PM2 = Likely Pathogenic. This query bypasses the engine's scoring entirely and surfaces every truncating variant below the population frequency threshold. Cross-reference hits against the recommended-preset results and add any new LoF variants to the shortlist for `get_variant` review.

### 3c — VUS-with-PVS1 misclassification check

> **Note:** This step requires `acmg_criteria` to be returned by `query_variants` (being added by the Noxia team). Once available, run:

```
mcp__noxia__query_variants(case_id=<id>, filter={
  "acmg_classification": ["VUS"],
  "consequence": ["frameshift_variant", "stop_gained",
                  "splice_donor_variant", "splice_acceptor_variant"]
})
```

Flag any variant where `acmg_criteria.pvs1 = true`. Under ACMG/AMP combining rules, PVS1 + PM2 = Likely Pathogenic — a stored VUS with PVS1 active is almost always a misclassification. These variants must be promoted to the shortlist and reviewed via `get_variant` for full criteria assessment, independent of their engine rank.

Until `acmg_criteria` are available in `query_variants`, catch these via the 3b LoF sweep and check `acmg_criteria` in `get_variant` detail for each hit.

### 3d — Drill into shortlisted candidates

For each flagged candidate, retrieve full detail:

```
mcp__noxia__get_variant(variant_id=<id>)
```

Fields to check: `consequence`, `gnomad_af`, `revel_score`, `cadd_phred`, `acmg_classification`, `acmg_criteria`, `clinvar_significance`, and the `ranking.disease_matches[].hpo_matches[]` block for HPO overlap detail.

### 3e — Genotype quality / VAF check

For every shortlisted candidate, inspect the `genotypes[]` block from `get_variant`. Full thresholds and the mosaicism gene list are in [REFERENCE.md](REFERENCE.md).

| Zygosity | Expected VAF | Action if outside range |
|---|---|---|
| Hemizygous (chrX/Y, male) | ≥ 0.80 | Flag artifact; cross-check sex_check QC; do not use as primary finding |
| Heterozygous | 0.40–0.60 | Flag if < 0.30; check mosaicism gene list before dismissing |
| Homozygous | ≥ 0.85 | Flag if < 0.80 |
| Any | depth < 20× | Low-confidence — do not advance to primary shortlist |

Mosaicism-permissive genes (VAF 0.10–0.40 acceptable — document as mosaic candidate, not artifact):
`CDKL5 · GNAS · NF1 · NIPBL · PCDH19 · PIK3CA · PKD1 · PKD2 · SAMD9 · SCN1A · SCN2A · TSC1 · TSC2`

Variants failing the VAF gate and not on the mosaicism list must be **removed from the primary shortlist** and routed to the QC / AI Analysis Draft with a recommendation for orthogonal validation.

---

## Step 4 — Cross-reference rankings (supporting evidence only)

> **Rankings are supporting evidence, never the driver.** Gene/variant rankings (the `gene-rankings` /
> `variant-rankings` REST endpoints, and the `ranking` block) come from a traditional bioinformatics
> prioritization algorithm. Consult them *after* independent clinical reasoning — not to drive
> candidate shortlisting.
> **Why:** Rankings reflect a scoring model's priors, not clinical judgment. Using them as the primary
> filter risks anchoring on the engine's biases rather than the actual clinical picture.
> **How to apply:** shortlist with clinical first principles (consequence class, gnomAD frequency, HPO
> phenotype overlap, inheritance fit), then cross-check rankings as a sanity check. Never promote or
> demote a candidate solely because of `candidate=true` or a high `composed_score`.

Rankings are embedded in `get_variant` — no separate REST call needed. The `ranking` block contains:
- `rank`, `gene_rank`, `tier` (Strong / Moderate / Weak) — engine confidence
- `in_report`, `confirmed_pathogenic` — engine pre-selection flags
- `compound_het`, `phase_group_role` — biallelic evidence
- `pathogenicity_reason` — brief engine rationale
- `inheritance_match` — AD/AR/XL fit per engine
- `disease_matches[].hpo_matches[]` — per-disease HPO overlap with `match_type` (EXACT_MATCH / NON_ROOT_COMMON_ANCESTOR / etc.)

Rankings are **corroboration, not verdicts**. Use `disease_matches[].hpo_matches[]` to sanity-check phenotype overlap, and `tier` / `in_report` to flag engine-prioritised variants — then verify independently against variant fields.

**HPO timing artefact:** if HPO was set after annotation, `disease_matches` may be empty or show no matches. Apply independent clinical HPO-overlap regardless.

---

## Step 5 — Assess top candidates

For each shortlisted candidate:
- Variant evidence: consequence, gnomAD AF vs threshold, REVEL/CADD/SpliceAI, ClinVar
- Phenotype overlap: specific HPO term matches to gene-disease associations
- Inheritance fit: family structure vs AD/AR/XL; compound-het requires phase evidence
- Adjacent variant check: flag clusters ≤20 bp apart in same gene as potential MNVs. Report to user for confirmation, warn if >2 variants, then use `merge_variants_in_cis` to merge and reclassify (see [REFERENCE.md](REFERENCE.md))
- Briefly rule out lower-ranked competing genes

Apply the clinical judgment rules and counter the known LLM biases in [REFERENCE.md](REFERENCE.md),
and output using the case-call format defined there.

---

## Step 6 — Opportunistic classification of top candidates

After identifying the lead candidate(s), check whether classification should be attempted or revised:

**Trigger classification (or re-classification) when:**
- The variant is VUS or unclassified (no approved curation workspace classification), **and** the available evidence is sufficient to reach Likely Pathogenic or Pathogenic.
- The variant already has a classification **but** case-specific phenotype information could activate additional criteria that upgrade or downgrade it — e.g.:
  - A distinctive, gene-specific HPO match activates **PP4** (phenotype highly specific for the gene).
  - Confirmed de novo (from trio data or family history) activates **PS2**.
  - Phenotype mismatch or alternative diagnosis makes **BP5** applicable (downgrade).

**Classification criteria to consider from case data alone (no lab required):**
| Criterion | What to look for in the case |
|---|---|
| PP4 | HPO terms that are EXACT_MATCH or DISEASE_TERM_SUBCLASS_OF_QUERY for the gene's specific disease; phenotype gestalt is highly discriminating |
| PM2 | AF absent from gnomAD (already captured by auto-classifier, but verify) |
| PS2 / PM6 | De novo status confirmed / assumed — check family history; no affected parent, de novo reported in the phenotype description |
| BP5 | An alternative Pathogenic variant already explains the phenotype — makes this variant less likely causative |

**Do not classify without user approval** (unless operating in fast-forward mode, which pre-authorises classification). Present proposed criteria and reasoning first; wait for the user to confirm before calling `classify_variant`.

**After classification:** remind the user that MCP-submitted classifications require manual approval in the Noxia web UI before they are finalized.

---

## Checklist

- [ ] QC reviewed — `get_case` `qc_passed` flag checked; if false, full `get_case_qc` report fetched; no flags, or user confirmed to proceed (concern documented)
- [ ] Case overview fetched (`summarize_case_variants`)
- [ ] Full `preset=recommended` list retrieved — **all pages paginated, cursor exhausted** (not just page 1)
- [ ] Phenotype-driven scan applied across the full list: LoF sweep, HPO-gene overlap check, inheritance-mode fit, rarity filter — **not top-to-bottom by rank**
- [ ] **Explicit LoF sweep query run** (Step 3b) — `consequence=[frameshift, stop_gained, splice_donor, splice_acceptor, start_lost]` + `max_gnomad_af=0.001`, independent of preset and ACMG filter
- [ ] **VUS-with-PVS1 check run** (Step 3c) — VUS truncating variants reviewed for `pvs1=true` misclassification; promoted to shortlist if PVS1 + PM2 active
- [ ] Shortlisted candidates identified through clinical criteria; rankings used as corroboration only
- [ ] Variant detail fetched for each shortlisted candidate (`get_variant`)
- [ ] **VAF/genotype quality checked** (Step 3e) — `genotypes[].vaf` and `.depth` reviewed for each candidate; implausible-VAF non-mosaicism-gene variants removed from primary shortlist
- [ ] Rankings cross-checked via `ranking` block (tier, in_report, disease_matches) — as supporting evidence
- [ ] HPO timing artefact considered — verify `disease_matches` is populated; apply manual HPO-overlap if empty
- [ ] Adjacent/MNV check done on co-located variants (≤20bp) — user confirmed, merged via `merge_variants_in_cis`, reviewed if >2 sources
- [ ] Opportunistic classification assessed: VUS candidates evaluated for PP4/PS2/PM6/BP5 upgrades from case phenotype; classification proposed to user (or submitted in fast-forward mode)
- [ ] User reminded to approve all MCP-submitted classifications in the Noxia web UI
- [ ] Top candidates assessed with explicit evidence chain

---

See [REFERENCE.md](REFERENCE.md) for MNV/adjacent variant rules and known engine limitations.
