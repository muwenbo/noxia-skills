---
name: noxia-fast-forward
description: End-to-end automated analysis + reporting for a Noxia case that is already ready — chains variant analysis, ACMG classification, and report drafting in one pass, skipping the routine human-confirmation gates. Classifying causative variants and drafting reports are pre-authorized and automated. Use when the user asks to "fast-forward", "auto-analyze", "run end-to-end", or wants an unattended analysis+report on one or more ready cases (referred to by case id, case name, or proband sample name).
---

# Noxia Fast-Forward Analysis

One automated pass: **resolve case → variant analysis → outcome → (classify + mark for positives) → always draft report.**
This mode is the explicit authorization to write: `classify_variant`, `mark_variant_for_report`,
`draft_report_text`, and `update_report_fields` run **without pausing for per-step approval**.

## What this mode overrides (and what it does NOT)

- **Overrides** the "never classify/draft without explicit permission" gates in
  [noxia-variant-analysis](../noxia-variant-analysis/SKILL.md) and
  [noxia-reporting](../noxia-reporting/SKILL.md). Auto-proceed through their steps.
- **Does NOT override** clinical safety floors:
  - Only runs on cases with `status = ready`. **Never call `run_case_bioinformatics_process` / re-run `/analyze`.**
    If a case is not ready, skip it and report why — do not start a pipeline.
  - **Never force a non-ideal variant into a formal finding.** Auto-classify + mark only a
    *confidently causative* variant. Honor the over-calling and VUS-inflation guards in
    [noxia-variant-analysis/REFERENCE.md](../noxia-variant-analysis/REFERENCE.md).
  - QC failure, "no convincing variant", and any speculative interpretation go into the report's
    **AI Analysis Draft** (`draft_report_text`) — never into a forced classification or Primary Finding.

## Step 0 — Resolve the case

Input may be a case id, a case name, or a proband/sample name.
- Numeric → treat as `case_id`.
- Otherwise `mcp__noxia__list_cases` and match on case name or proband sample name.
- Multiple matches → this is the **only** point you may ask the user (identity, not clinical judgment).
- Confirm `status = ready` before proceeding (`get_case`). Not ready → skip + report; do not annotate.

## Step 1 — Variant analysis (automated)

Run [noxia-variant-analysis](../noxia-variant-analysis/SKILL.md) Steps 1–5, auto-proceeding:
QC review → `summarize_case_variants` → **exhaust all pages of `preset=recommended`** (cursor loop, not page 1 only)
→ **mandatory LoF sweep** (`consequence=[frameshift, stop_gained, splice_donor, splice_acceptor, start_lost]` + `max_gnomad_af=0.001`, Step 3b — bypasses engine blind spot for novel truncating variants)
→ **VUS-with-PVS1 check** (Step 3c — flag VUS truncating variants where `pvs1=true`; PVS1 + PM2 = LP regardless of engine rank)
→ `get_variant` detail on all shortlisted candidates → **VAF quality check** (`genotypes[].vaf`/`.depth`; apply mosaicism gene list from [REFERENCE.md](../noxia-variant-analysis/REFERENCE.md); remove implausible-VAF non-mosaic variants from primary shortlist) → cross-check `ranking`/`disease_matches` as corroboration only.
Capture: QC status, the evidence chain, and where the engine's `candidate=true` agrees or disagrees.

## Step 2 — Decide the outcome

| Outcome | Trigger |
|---|---|
| **Positive** | A variant with a complete, confident evidence chain (specific HPO match, inheritance fit, rarity, ClinVar/REVEL/CADD/SpliceAI agreement, biallelic phase if AR). |
| **VUS** | Best candidate fits the gene-disease association but evidence is insufficient (e.g. PM2+PP3 only). |
| **Negative** | No convincing variant. Includes QC-failed cases analyzed under caveat. |

## Step 3 — Classify + mark

Run [noxia-reporting](../noxia-reporting/SKILL.md) Steps 1–2:
- `classify_variant` — full 28-criterion dict, reasoning text for every active criterion.
- `mark_variant_for_report(include=true, notes=…)`; mark **both** variants for compound-het.
- VUS / Negative: do **not** mark a Primary Finding. (You may honestly `classify_variant` a true VUS as
  `VUS`, but never as Pathogenic/Likely_Pathogenic, and never mark it as the causative answer.)

### Compelling VUS candidates — always mark for report

A VUS should also be `classify_variant` + `mark_variant_for_report` as a **reported candidate** (not
Primary Finding) when **all three** of the following hold:

1. **Phenotype specificity** — ≥1 HPO term matches the disease at `EXACT` or
   `DISEASE_TERM_SUBCLASS_OF_QUERY` level (not just `NON_ROOT_COMMON_ANCESTOR`).
2. **Population rarity** — absent from gnomAD or AF below the gene's disease threshold.
3. **Mechanistic plausibility** — variant type is consistent with the gene's MOI (LoF in a
   haploinsufficiency gene; missense in a dominant-negative or GoF context; biallelic for AR if a
   second hit is present or plausible from coverage).

This applies across all outcomes:

| Scenario | Action |
|---|---|
| **Positive + phenotype-mismatched primary** (primary Pathogenic has only `NON_ROOT` HPO matches) | Mark the co-occurring VUS with specific HPO matches as a reported candidate alongside the primary finding. Note it as the preferred explanation for the clinical phenotype. |
| **Pure VUS outcome** (best candidate is a VUS) | Mark it for report and write the VUS narrative in the AI Analysis Draft. |
| **Two independent findings** (Pathogenic + compelling VUS in a different gene) | Report both; describe them as independent findings in the draft. |

The `mark_variant_for_report` notes must state: ACMG classification, HPO match rationale, and the
specific evidence (de novo confirmation, functional study, segregation) that would upgrade the variant.

## Step 4 — Always draft the report (route by outcome)

Run [noxia-reporting](../noxia-reporting/SKILL.md) Step 3 for **every** outcome. `get_report` → write fields
in one pass → `get_report` to verify. Follow that skill's clinical-prose conventions ("this proband",
no named databases, full ACMG spelling, one paragraph per variant).

| Outcome | `draft_report_text` (AI Analysis Draft) | Other fields |
|---|---|---|
| **Positive** | Phenotype → gene → variant → interpretation narrative. | All 5 fields incl. `variant_descriptions`. |
| **VUS** | VUS narrative: candidate gene, why evidence is uncertain, what would upgrade it. | `clinical_summary`, `gene_descriptions`, VUS `variant_descriptions`, `diagnostic_recommendations` (functional/segregation follow-up). |
| **Negative** | State no convincing variant. Put **QC concerns** and any **speculative interpretation** here, explicitly labeled non-diagnostic. For a distinctive phenotype, derive the speculative interpretation with [noxia-phenotype-inference](../noxia-phenotype-inference/SKILL.md) (assay-blind mechanism → confirmatory test). | `clinical_summary`, `diagnostic_recommendations` (reanalysis triggers, broader testing). |

## Output & batch handling

- Emit the case-call block (Positive/VUS/Negative + evidence chain + confidence) per case, using the
  format in [noxia-variant-analysis/REFERENCE.md](../noxia-variant-analysis/REFERENCE.md).
- Multiple cases (list, or "all ready in project"): process each independently, then write the
  **synthesis** paragraph (same REFERENCE) — which calls were unambiguous, which needed judgment, where
  engine `candidate=true` agreed/disagreed with the independent read.
- After all writes: remind the user that MCP-submitted classifications still require manual approval
  in the Noxia web UI before they are finalized.

## Checklist (per case)

- [ ] Case resolved (id / name / proband sample) and confirmed `status = ready` — no annotation triggered
- [ ] Variant analysis run automated: `preset=recommended` all pages exhausted + explicit LoF sweep (Step 3b) + VUS-with-PVS1 check (Step 3c)
- [ ] VAF quality check done — `genotypes[].vaf` and `.depth` checked for all shortlisted candidates; implausible-VAF non-mosaicism-gene variants removed from primary shortlist
- [ ] Outcome decided (Positive / VUS / Negative) without over-calling
- [ ] Positive only: `classify_variant` (full criteria + reasoning) and `mark_variant_for_report`
- [ ] Compelling VUS candidates assessed: any VUS with ≥1 EXACT/SUBCLASS HPO match + gnomAD-rare + mechanistically plausible → `classify_variant` + `mark_variant_for_report` as reported candidate
- [ ] Report drafted for every outcome; QC/no-candidate/speculation routed to AI Analysis Draft
- [ ] `get_report` confirms fields saved
- [ ] Case-call block emitted; synthesis written for batches; web-UI approval reminder given
