---
name: noxia-variant-classifier
description: "Deep ACMG/VCEP variant classification using noxia KB + ClinGen VCEP guidelines. Use ONLY when the user explicitly requests VCEP-level or detailed ACMG criteria breakdown for a specific variant. Do NOT auto-trigger — this is intentionally token-intensive. Accepts a noxia variant_id, HGVS notation, rsID, or genomic coordinates. Produces a full 28-criterion ACMG analysis with VCEP modifications and a classification proposal for user review. Does NOT submit the classification — that is the user's decision."
---

# Noxia Variant Classifier

Full ACMG/AMP + ClinGen VCEP variant classification. Applies gene-specific VCEP criteria modifications
where available. Ends with a classification **proposal** — the agent does not auto-submit; the user
decides whether to accept and call `classify_variant` (MCP) or approve via the noxia web UI.

**Use only when the user explicitly asks for VCEP classification or a detailed ACMG breakdown.**
Routine noxia case analysis does not require this skill.

---

## Path Resolution

```
SKILL_DIR = this SKILL.md's directory (.claude/skills/noxia-variant-classifier/)
VCEP_GUIDELINES = $SKILL_DIR/../variant-classifier/data/vcep-guidelines/
CLINVAR_SCRIPT  = $SKILL_DIR/../variant-classifier/scripts/clinvar_region_query.py
PAPER_SCRIPT    = $SKILL_DIR/../paper-finder/scripts/paper_fetcher.py
```

---

## Step 1 — KB Annotation

Call both tools in parallel:

```
mcp__noxia__kb_lookup_variant(hgvs="<variant>")
  OR
mcp__noxia__kb_lookup_variant(chrom="<chr>", pos=<pos>, ref="<ref>", alt="<alt>")
```

```
mcp__noxia__kb_get_gene(symbol="<GENE>")
```

**From `kb_lookup_variant`, extract:**
- `consequence`, `impact`, `hgvs_c`, `hgvs_p`, `transcript_id`
- `gnomad_af`, `gnomad_popmax` (per-ancestry breakdown for PM2/BS1)
- `cadd_phred`, `revel_score` (PP3/BP4)
- `spliceai` — individual delta scores: `ds_ag`, `ds_al`, `ds_dg`, `ds_dl` and matching `dp_*` positions (PVS1-splice, PP3, BP7)
- `clinvar_significance`, `clinvar_review_status` (PS1 anchor, PP5, BP6)
- `domains` — UniProt feature annotations at this residue (PM1)
- `pmids` — associated literature PMIDs (seed for paper-finder)

**From `kb_get_gene`, extract:**
- `loeuf`, `pli` (PP2, gene constraint context)
- `clingen_dosage_sensitivity`
- `associated_diseases[]` — inheritance patterns
- `vcep_acmg_specifications` — **check this field**: if non-null, a VCEP spec exists for this gene

---

## Step 2 — VCEP Guideline

If `kb_get_gene.vcep_acmg_specifications` is non-null:

1. Note the spec name and version from the response
2. Search `$VCEP_GUIDELINES/` for a file matching the gene symbol:
   ```bash
   ls $SKILL_DIR/../variant-classifier/data/vcep-guidelines/ | grep -i "<GENE>"
   ```
3. If a guideline file exists, **read it in full** before evaluating any criteria
4. Note which criteria are modified, strengthened, or restricted by the VCEP spec

If no VCEP spec exists: apply standard ACMG/AMP 2015 rules.

Some genes have multiple specs by inheritance pattern (e.g., `ACTA1_AD` vs `ACTA1-AR`, `RYR1_AD` vs
`RYR1_AR`). If multiple files match, ask the user which context applies before proceeding.

---

## Step 3 — ClinVar Region Lookup (PS1 / PM5)

For **missense, in-frame indel, or splice variants**, run a ClinVar region search to find other
classified variants at or near the same codon/position:

```bash
# Use a ±5 bp window around the variant position
python $SKILL_DIR/../variant-classifier/scripts/clinvar_region_query.py \
  <CHROM>:<POS-5>-<POS+5> --format json -o /tmp/clinvar_region.json
```

From the results, identify:
- **PS1 candidates**: same amino acid change as a known P/LP variant (identical AA substitution)
- **PM5 candidates**: different pathogenic AA change at the same residue (novel missense, same hotspot)
- **BP6 candidates**: variant itself listed as Benign/Likely Benign in ClinVar with ≥2 star review

Only run this step for missense, in-frame indel, or splice-altering variants. Skip for LoF (frameshift,
stop_gain) where PS1/PM5 are not applicable.

---

## Step 4 — Literature (if PMIDs available)

If `kb_lookup_variant` returned PMIDs:

```bash
# Metadata preview first (fast)
python $SKILL_DIR/../paper-finder/scripts/paper_fetcher.py <PMID1> <PMID2> ... --metadata-only
```

Present the metadata table to the user and ask:
1. **Skip literature** — proceed with computational evidence only
2. **Fetch full text for selected PMIDs** — for case-level evidence extraction
3. **Add additional PMIDs** — user provides extra references

If full text requested, run without `--metadata-only` and save to `./papers/`. Then read the papers
and extract evidence for:
- **PS2/PM6**: de novo observations (confirmed / assumed parentage)
- **PS3/BS3**: functional studies (validated assay outcomes)
- **PS4**: case counts, case-control data
- **PP1/BS4**: segregation / non-segregation in family members
- **PM3**: compound heterozygosity in trans with another pathogenic variant
- **PP4**: phenotype descriptions matching the gene-disease association
- **BP5**: alternate molecular cause identified

---

## Step 5 — User Verification Checkpoint

Present a summary before classification:

| Item | Value |
|------|-------|
| Variant | `<hgvs_c>` (`<hgvs_p>`) |
| Gene | `<GENE>` / transcript `<transcript_id>` |
| Consequence | `<consequence>` / impact `<impact>` |
| gnomAD AF | `<gnomad_af>` (popmax: `<highest_population>` = `<af>`) |
| CADD phred | `<cadd_phred>` |
| REVEL | `<revel_score>` |
| SpliceAI max | `<max_delta>` (DS_AG=`<>` DS_AL=`<>` DS_DG=`<>` DS_DL=`<>`) |
| ClinVar | `<clinvar_significance>` (`<review_status>`) |
| Domain | `<domain info or "no annotated domain">` |
| VCEP spec | `<spec name + version or "none">` |
| PMIDs | `<count>` found |
| ClinVar region | `<N>` P/LP variants found nearby |

Confirm with user before proceeding. If `--notes` or additional context was provided by the user,
display it here and note how it will be applied.

---

## Step 6 — ACMG Criteria Evaluation

Evaluate all 28 criteria systematically. For each, state: **Applied / Not applied** and the
reasoning. Apply VCEP modifications found in Step 2 — these override the standard rules below.

### Pathogenic criteria

**PVS1** — Null variant in a gene where LoF is a known mechanism  
Apply if: frameshift, stop_gain, splice ±1/2, start_loss, exon deletion. Check `loeuf` and ClinGen
dosage sensitivity. Use the VCEP PVS1 decision tree if one exists in the guideline file.

**PS1** — Same AA change as established pathogenic variant  
Apply if ClinVar region query found a P/LP variant with identical protein change and ≥2 star review.

**PS2** — De novo (confirmed parentage)  
Apply from literature or user-provided family data.

**PS3** — Functional studies support pathogenicity  
Apply from literature. Require validated assay result; cell-based reporter alone is insufficient.

**PS4** — Variant significantly more prevalent in affected individuals  
Apply from case-control data. Note case counts.

**PM1** — In mutational hotspot or well-established functional domain  
Apply if `kb_lookup_variant.domains` shows the residue falls inside a documented UniProt feature
(active site, binding site, disulfide bond, transmembrane region). Do NOT apply for generic
"region of unknown function."

**PM2** — Absent from (or extremely low frequency in) population databases  
Apply if `gnomad_af` is absent or < 1e-4 (AR) / < 1e-5 (penetrant AD). Use `gnomad_popmax` — if
any ancestry exceeds the threshold, do not apply. Downgrade to supporting (PM2_Supporting) per
ClinGen recommendations if variant is present but very rare (1–5 allele observations).

**PM3** — In trans with a pathogenic variant (recessive context)  
Apply from literature or case data. Requires phase evidence.

**PM4** — Protein length change in non-repeat region  
Apply for in-frame indels outside of repetitive sequence regions.

**PM5** — Novel missense at residue where different pathogenic AA change is known  
Apply if ClinVar region query found a P/LP variant at the same residue with a different substitution.

**PM6** — De novo (parentage not confirmed)  
Apply from literature when de novo is assumed but not confirmed.

**PP1** — Cosegregation in multiple affected family members  
Apply from literature or user data.

**PP2** — Missense variant in gene with low rate of benign missense variation  
Apply if consequence is missense AND `loeuf` < 0.35 or gene is in a constrained missense intolerance
list. Check VCEP guidelines — some specs restrict or eliminate PP2.

**PP3** — Multiple computational tools support pathogenicity  
Apply if REVEL ≥ 0.75 OR CADD phred ≥ 25, and no opposing computational tools. For splice variants:
apply if max SpliceAI delta score ≥ 0.5. VCEP specs often raise or lower these thresholds.

**PP4** — Specific phenotype highly specific for gene  
Apply from case HPO data. Require EXACT_MATCH or strong DISEASE_TERM_SUBCLASS_OF_QUERY HPO overlap,
not loose similarity.

**PP5** — Reputable source classifies as pathogenic  
Apply if ClinVar shows P/LP with ≥2 star review status AND no conflicting interpretations.

### Benign criteria

**BA1** — Allele frequency > 5% in population databases  
Apply if `gnomad_af` or any `gnomad_popmax` entry ≥ 0.05. Immediately resolves to Benign.

**BS1** — Allele frequency greater than expected for disorder  
Apply if `gnomad_popmax` exceeds disease prevalence threshold. Use VCEP-specified threshold when
available; otherwise use 0.01 for AD, 0.03 for AR as defaults.

**BS2** — Observed in healthy adults in homozygous state  
Apply from gnomAD homozygote count when disorder has early complete penetrance.

**BS3** — Functional studies show no damaging effect  
Apply from literature. Same rigor standard as PS3.

**BS4** — Lack of segregation in affected family members  
Apply from family/case data.

**BP1** — Missense in gene where only LoF causes disease  
Apply if the gene's disease mechanism is exclusively LoF AND variant is missense.

**BP2** — Observed in trans with dominant pathogenic variant, OR in cis with pathogenic variant  
Apply from phase/family data.

**BP3** — In-frame deletion/insertion in repetitive region  
Apply for indels confirmed to be within tandem repeat sequence.

**BP4** — Multiple computational tools support benign effect  
Apply if REVEL < 0.15 AND CADD phred < 15, and no opposing tools. For splice: SpliceAI max delta
< 0.1. VCEP specs often modify these thresholds.

**BP5** — Variant found in case with an alternate molecular basis for disease  
Apply from case data.

**BP6** — Reputable source classifies as benign  
Apply if ClinVar shows B/LB with ≥2 star review and no conflicting interpretations.

**BP7** — Silent variant with no predicted splice impact  
Apply if consequence is synonymous AND all SpliceAI delta scores < 0.1.

---

## Step 7 — Point Tally and Classification

Sum the points using standard ACMG weights, applying any VCEP strength overrides:

| Strength | Points |
|----------|--------|
| PVS (Very Strong) | +8 |
| PS (Strong Pathogenic) | +4 |
| PM (Moderate) | +2 |
| PP (Supporting Pathogenic) | +1 |
| BS (Strong Benign) | -4 |
| BP (Supporting Benign) | -1 |
| BA1 (Standalone) | Benign immediately |

Thresholds: Pathogenic ≥ 10 · Likely Pathogenic 6–9 · VUS −5 to +5 · Likely Benign −6 to −9 · Benign ≤ −10

---

## Step 8 — Present Classification Proposal

Output the proposal in this format:

```
## ACMG Classification Proposal

Variant:    <GENE>:<hgvs_c> (<hgvs_p>)
Transcript: <transcript_id>
VCEP spec:  <spec name + version | "Standard ACMG/AMP 2015">

### Active criteria
| Criterion | Strength | Evidence |
|-----------|----------|----------|
| PVS1      | Very Strong | <1-line reason> |
| PM2       | Moderate    | <1-line reason> |
...

### Inactive criteria with notes (optional — only include if borderline or VCEP-modified)
| Criterion | Decision | Reason |
|-----------|----------|--------|
| PP3       | Not applied | REVEL 0.48 — below VCEP threshold of 0.75 |

### Point tally
Pathogenic: +<N>  Benign: <N>  Net: <N>

### Proposed classification: <Pathogenic | Likely Pathogenic | VUS | Likely Benign | Benign>

### Open questions / caveats
- <segregation unknown>
- <functional data missing>
- <second hit not confirmed>
```

Then prompt the user:

> This is a classification proposal. If you agree, you can submit it to the noxia case via
> `mcp__noxia__classify_variant` (providing `variant_id`, the criteria dict, and per-criterion
> reasoning) or approve it directly in the noxia web UI Curation Workspace. Do you want to proceed
> with submission, revise any criteria, or save this as a draft?

---

## Quick Mode (--quick)

If the user requests `--quick` or computational-only mode:
- Skip literature (Steps 3–4)
- Skip ClinVar region query
- Use only computational criteria: PVS1, BA1, BS1, PM2, PP2, PP3, BP4, BP7
- State explicitly that case-level evidence (PS2/PS3/PS4/PP1/PM3) was not evaluated
