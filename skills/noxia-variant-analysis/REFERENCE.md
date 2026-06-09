# Variant Analysis — Reference

## Adjacent variant / MNV check

When variants in the same gene are **≤20 bp apart**, flag them as potential MNVs
(multi-nucleotide variants) that may need to be merged and evaluated as a single
complex allele.

**Flags:**
- Same gene, genomic positions within ≤20 bp of each other
- Any number of variants — pairs, triplets, or larger clusters
- One or more appear pathogenic (e.g. stop_gained, frameshift), adjacent ones may be benign (low REVEL/CADD)
- Called at similar allele fractions / zygosity patterns consistent with cis

**What to do:**

1. **Report the cluster to the user.** List all variants, their HGVS, positions,
   and pairwise distances. Ask the user to confirm they should be treated as a
   cis complex allele before proceeding.

2. **Warn if >2 variants are involved.** Merging three or more variants carries
   higher uncertainty — the caller may have mis-phased one component, the
   combined consequence may be harder to predict, and the merged HGVS may not
   reflect the true haplotype. After merging, **ask the user to carefully review**
   the resulting merged variant before classification.

3. **Use `merge_variants_in_cis` to merge.** Once the user confirms, call the
   merge tool with all source variant IDs and a clear `phase_evidence` string.
   The tool computes the correct combined genomic sequence, derives the canonical
   HGVS (e.g. `c.572_579delinsTCCTCAAATGGA`), and creates a new merged variant
   row. **Do not merge without user confirmation.**

4. **Recalculate combined consequence.** The merged delins codon change may
   differ from any individual component — always verify the tool-computed HGVS
   against your expectation. The net frameshift may start at a different codon
   than any single variant.

5. **Classify the merged variant** — present the proposed ACMG criteria,
   classification, and reasoning to the user first. **Do not call
   `classify_variant` without the user's explicit permission.** Once approved,
   submit the classification with the canonical HGVS. Note the caller-split
   origin in the classification notes.

6. **Update the report** — mark the merged variant for report, unmark the source
   variants, and use the canonical HGVS in gene/variant descriptions and draft
   interpretation.

7. **Remind the user to approve** — all classifications submitted via
   `classify_variant` (MCP) must be manually reviewed and confirmed in the
   Noxia web UI. After classifying, remind the user to approve the
   classification before considering the case complete.

Example: Three CD40LG variants at chrX:136659200/204/208 (8bp cluster) merged
into `c.572_579delinsTCCTCAAATGGA` (p.Ala191ValfsTer11) — a single frameshift
that would have been missed if each component were evaluated independently.

---

## Known engine limitations

| Issue | Workaround |
|---|---|
| `query_variants` has no preset/priority filter | Use REST `gene-rankings` + `variant-rankings` |
| `phenotype_lr=0` when HPO set post-annotation | Apply manual clinical HPO-overlap |
| `run_case_bioinformatics_process` fails from `ready` state ("cannot transition") | Annotation already ran; gene-ranking data is present — proceed directly |
| Engine `explanation` may oversimplify | Always verify against raw variant fields before quoting |

---

## Genotype quality / VAF check

Always check the `genotypes[]` block returned by `get_variant` for every shortlisted candidate.

**Fields returned:**
- `relation` — proband / mother / father / sibling
- `genotype` — `hom` / `het` / `hemizygous`
- `depth` — total read depth at the variant site
- `allele_depth` — alt allele read count
- `ref_depth` — ref allele read count
- `vaf` — variant allele fraction (`allele_depth / depth`)

### VAF thresholds

| Zygosity | Expected VAF | Flag if |
|---|---|---|
| Hemizygous (chrX/Y in male) | ≥ 0.80 | < 0.60 — likely artifact or sex assignment error |
| Heterozygous constitutional | 0.40–0.60 | < 0.30 — artifact, allele bias, or low mosaicism |
| Homozygous | ≥ 0.85 | < 0.80 — contamination or mis-call |
| Any zygosity | — | depth < 20× — low-confidence regardless of VAF |

### Mosaicism-permissive genes

For these genes, VAF 0.10–0.40 can represent genuine somatic mosaicism — document as "mosaic likely pathogenic" with VAF explicitly noted; do **not** dismiss as artifact:

`CDKL5 · GNAS · NF1 · NIPBL · PCDH19 · PIK3CA · PKD1 · PKD2 · SAMD9 · SCN1A · SCN2A · TSC1 · TSC2`

For all other genes: VAF outside the expected range for the called zygosity is a **pre-classification artifact flag**. Remove from primary shortlist and route to the QC / AI Analysis Draft section.

### Artifact flag procedure

1. Note the VAF, expected range for the zygosity, and the discrepancy.
2. Check the mosaicism gene list — if listed, document as mosaic candidate and proceed with caution.
3. For X-linked variants: cross-check `sex_check_status` from QC. A hemizygous call in a declared male with VAF < 0.60 is likely artifact or sex assignment error — do not use as primary finding.
4. Remove the variant from the primary shortlist; document in the QC section or AI Analysis Draft.
5. Recommend IGV inspection or orthogonal validation before clinical reporting.

---

## Key REST endpoints

| Purpose | Endpoint |
|---|---|
| Gene rankings | `GET /api/cases/<id>/gene-rankings` |
| Variant rankings | `GET /api/cases/<id>/variant-rankings` |
| Skipped variants | `GET /api/cases/<id>/skipped-variants` |
| Prioritization metadata | `GET /api/cases/<id>/prioritization-metadata` |
| QC report | `GET /api/cases/<id>/qc/report` |

---

## Clinical judgment rules

The canonical reasoning rules for every Noxia case call. The other Noxia skills
(reporting, fast-forward, phenotype-inference) defer to this section.

- **Frequency.** gnomAD AF < 1e-4 for AR, < 1e-5 for penetrant AD. Use `gnomad_af_popmax` when available.
- **Inheritance fit.** AD → de novo or single het with phenotype; AR → hom or compound het (verify phase / second hit); X-linked per sex.
- **Pathogenicity evidence.** ClinVar P/LP, HIGH-impact LoF (frameshift, stop_gain, splice ±1/2), REVEL > 0.5 or CADD > 20 for missense, SpliceAI ≥ 0.5 for splice.
- **Phenotype overlap.** Require explicit HPO match to a known gene-disease association. "Immune-related"-style loose matches are not enough.
- **Engine fields are anchors, not verdicts.** Verify `composed_lr`, `candidate=true`, and `explanation` against the underlying variant before quoting them.
- **Decisiveness signal.** A large `composed_score` gap between rank 1 and rank 2 = decisive; small gap = competing hypotheses, lower confidence.
- **Beware genotype-only LRs.** If `composed_lr` is high but `phenotype_lr ≪ 1`, the call is weak.
- **Genotype quality.** Before advancing any variant to a primary finding, verify `genotypes[].vaf` is consistent with the expected zygosity (het ~0.40–0.60, hemizygous ≥ 0.80, hom ≥ 0.85) and `depth` ≥ 20×. Implausible VAF = artifact flag; remove from shortlist unless the gene is mosaicism-permissive (see Genotype quality / VAF check section above).

---

## Known LLM biases — actively counter

1. **Over-calling.** Default to "no convincing variant" when evidence is thin. Don't promote a VUS to a diagnosis to satisfy the task.
2. **Ignoring age of onset / epidemiology.** Adult-onset common diseases (UC, T2D, common epilepsy) are almost never monogenic. Weight this before naming a candidate.
3. **VUS inflation.** PM2 + PP3 alone in a constrained gene is not actionable without functional or segregation data.
4. **Loose phenotype matching.** Require specific HPO overlap, not vibe-level relevance.

---

## Case-call output format

Emit this block for every case call:

```
Case <id> — <Positive | VUS | Negative>
Top gene: <SYMBOL> (<inheritance>, composed_score=<n>, top disease OMIM <id> <name>, composed_LR=<n>)
Top variant(s):
  - <transcript>:c.<...> (p.<...>) — chr:pos REF>ALT — ClinVar <...> — gnomAD AF <...> — ACMG <...>
  - (second variant if compound het)
Reasoning: 1–3 sentences citing the evidence chain (HPO match strength, biallelic status, inheritance fit, gnomAD rarity, ClinVar/REVEL agreement).
Open questions / caveats: <segregation unknown? VUS upgrade pending functional? etc.>
Confidence: HIGH | MODERATE | LOW
```

After a batch, write a one-paragraph **synthesis**: which calls were unambiguous, which needed
judgment, where the engine's `candidate=true` agreed or disagreed with your independent read.
