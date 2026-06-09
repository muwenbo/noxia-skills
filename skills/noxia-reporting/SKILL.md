---
name: noxia-reporting
description: ACMG variant classification, variant marking, and clinical report drafting in Noxia. Use after variant analysis is complete and a causative variant has been identified — covers classify_variant, mark_variant_for_report, draft_report_text, and update_report_fields.
---

# Noxia Reporting

## Scope

Classify causative variant(s) → mark for report → draft all report fields.  
Starts after variant analysis has identified the causative gene/variant.

**Before classifying, confirm the evidence actually supports a causative call.** If it does not,
**conclude that no convincing causative variant was found** and report that outcome — do not classify
or mark a forced finding to satisfy the task. A VUS or negative result is a valid, complete report.

---

## Step 1 — Resolve the disease for classification

Before classifying, identify the best-fit OMIM disease using `kb_get_disease`. This confirms the disease name, inheritance, and phenotype overlap to anchor the classification context.

```
mcp__noxia__kb_get_disease(disease_id="<OMIM_ID>")
# OMIM ID from the variant's ranking.disease_matches[].disease_id (get_variant output)
```

**Disease selection rules:**
- Pick the OMIM disease whose **inheritance pattern and molecular mechanism** best match the variant (e.g., frameshift LoF → Duchenne MD not Becker MD; AR compound het → recessive entry not dominant).
- When multiple diseases are plausible, pick the strongest HPO + mechanism fit; note others in `classification_notes`.
- Fall back to free-text `disease_name` when no single OMIM entry fits (novel association, atypical presentation spanning entries, disease absent from KB).

Use `disease_ref` to bind the classification to the resolved Disease row — no internal PK required:
- OMIM: `"OMIM:310200"` or bare `"310200"`
- MONDO: `"MONDO:0010679"`

The response echoes back the resolved `disease_id`. If the ref matches multiple diseases (ambiguous OMIM), the call raises an error with candidate MONDO IDs — re-call with the specific MONDO ref.

### Pre-classification genotype quality check

Before classifying, verify genotype quality from `get_variant.genotypes[]`:
- `vaf` must be consistent with the expected zygosity (het ~0.40–0.60, homozygous ≥ 0.85, hemizygous in males ≥ 0.80)
- `depth` must be ≥ 20×
- If VAF is outside the expected range: **do not classify** until the variant is validated orthogonally, unless the gene is mosaicism-permissive (see noxia-variant-analysis/REFERENCE.md). A low-VAF variant on a non-mosaicism gene is an artifact flag, not a finding.

---

## Step 2 — Classify the variant

```
mcp__noxia__classify_variant(
  variant_id   = <id>,
  acmg_class   = "Pathogenic",   # Pathogenic | Likely_Pathogenic | VUS | Likely_Benign | Benign
  disease_ref  = "OMIM:310200",  # preferred — resolves to internal Disease row; use MONDO if OMIM is ambiguous
  disease_name = "<name>",       # fallback only when no OMIM/MONDO entry fits the classification
  criteria   = {
    "pvs1": true, "ps1": false, "ps2": false, "ps3": false, "ps4": false,
    "pm1": false, "pm2": true,  "pm3": false, "pm4": false, "pm5": false, "pm6": false,
    "pp1": false, "pp2": false, "pp3": false, "pp4": false, "pp5": false,
    "ba1": false,
    "bs1": false, "bs2": false, "bs3": false, "bs4": false,
    "bp1": false, "bp2": false, "bp3": false, "bp4": false, "bp5": false, "bp6": false, "bp7": false
  },
  reasoning = {
    "pvs1": "<why this criterion applies>",
    "pm2":  "<why this criterion applies>"
    # only active criteria need text
  }
)
```

**Rules:**
- Provide the full 28-criterion dict; unused criteria `false`
- Write explicit reasoning text for every criterion set to `true`
- Don't promote VUS to diagnosis — PM2 + PP3 alone in a constrained gene is not actionable without functional or segregation data
- If no variant clears the bar, stop here and conclude **no convincing causative variant was found** rather than classifying the least-weak candidate

---

## Step 2 — Mark variant for report

```
mcp__noxia__mark_variant_for_report(
  variant_id = <id>,
  include    = true,
  notes      = "<clinical summary of why this variant is causative>"
)
```

For compound-het: mark both variants.

---

## Step 3 — Draft the report

First check current report state:
```
mcp__noxia__get_report(case_id=<id>)
```

Then write all fields in one pass:

```
mcp__noxia__draft_report_text(case_id=<id>, draft_text="<interpretation narrative>")

mcp__noxia__update_report_fields(
  case_id                  = <id>,
  clinical_summary         = "<demographics + presenting features + family history>",
  diagnostic_recommendations = "<numbered action items>",
  gene_descriptions        = {"GENE": "<gene function + associated disease>"},
  variant_descriptions     = {"GENE:c.X>Y": "<variant detail + ACMG evidence summary>"}
)
```

Verify all fields saved:
```
mcp__noxia__get_report(case_id=<id>)
```

---

## Report field guidance

| Field | What to include |
|---|---|
| `clinical_summary` | Age, sex, presenting features, family history, referring clinician |
| `diagnostic_recommendations` | Numbered: confirmatory testing, segregation, cascade screening, management implications |
| `gene_descriptions` | Gene function, inheritance mode, associated OMIM disease(s), prevalence context |
| `variant_descriptions` | HGVS notation, consequence, gnomAD AF, ClinVar status, ACMG class + active criteria |
| `draft_report_text` | Narrative linking phenotype → gene → variant → clinical interpretation |

---

## Clinical prose style for `gene_descriptions` and `variant_descriptions`

### Gene description paragraph — template

> Pathogenic variants in the **[GENE]** gene can cause **[Full Disease Name] ([Abbreviation]) [MIM:XXXXXX]**, which is an autosomal [dominant/recessive] disorder. [1–2 sentences: what the disease involves at a pathophysiological level, typical onset period.] [Clinical features organized by onset subtype — e.g., "In neonatal-onset patients, the major clinical features include…; In childhood-onset patients, the main clinical manifestations are…" — or as a numbered list for multi-system diseases.] [If applicable: inter-individual variability or incomplete penetrance, with PMID citation.]

**Example:**
> Pathogenic variants in the CHAT gene can cause Congenital Myasthenic Syndrome Type 6, Presynaptic (CMS6) [MIM:254210], which is an autosomal recessive disorder. This disease involves skeletal muscle weakness caused by impairment at the neuromuscular junction, and typically presents in the neonatal or early childhood period. In neonatal-onset patients, the major clinical features include respiratory insufficiency, respiratory distress, apnea, cyanosis, poor sucking, feeding difficulties, weak cry, ptosis, and multiple joint contractures. In childhood-onset patients, the main clinical manifestations are motor developmental delays due to muscle weakness, and difficulties in activities such as running or climbing stairs.

### Variant description paragraph — template (one paragraph per variant)

> The variant **c.[HGVS_c]([HGVS_p])** identified in this proband is a [frameshift/missense/nonsense/splice] variant [caused by a deletion/insertion/substitution] in the [exonic/intronic] region of the **[GENE]** gene. This [variant type] variant theoretically leads to [premature termination of protein translation / amino acid substitution at position X / …]. [If frameshift/nonsense: "Multiple loss-of-function pathogenic variants have been reported downstream of this variant, suggesting that the deleted portion of the protein has an important impact on protein function."] [Literature: "This variant has not been reported in the literature." OR "It has been detected in [N] documented case(s) of [disease] in the literature (PMID:XXXXXXXX)."] [Population: "This variant has not been reported in large-scale population frequency databases." OR "This variant has not been reported in large-scale population frequency databases."] Based on current evidence, this variant is classified as a **[Pathogenic / Likely Pathogenic / Variant of Uncertain Significance (VUS)]** variant.

**Example (frameshift, Likely Pathogenic):**
> The variant c.1381_1382del(p.Met461Aspfs*49) identified in this proband is a frameshift variant caused by a deletion in the exonic region of the CHAT gene. This frameshift variant theoretically leads to premature termination of protein translation. Multiple loss-of-function pathogenic variants have been reported downstream of this variant, suggesting that the deleted portion of the protein has an important impact on protein function. This variant has not been reported in the literature or in large-scale population frequency databases. Based on current evidence, this variant is classified as a Likely Pathogenic variant.

**Example (missense, VUS):**
> The variant c.736A>G(p.Lys246Glu) identified in this proband is a missense variant in the exonic region of the CHAT gene. This variant has not been reported in the literature or in large-scale population frequency databases. Based on current evidence, this variant is classified as a Variant of Uncertain Significance (VUS).

### Key conventions

- Say **"this proband"** — not "the patient" or "the index case"
- **Never name specific databases** (gnomAD, ExAC, etc.) — use "large-scale population frequency databases"
- **ACMG classification spelled out in full:** Pathogenic, Likely Pathogenic, Variant of Uncertain Significance (VUS) — abbreviate only in parentheses after first use
- **MIM numbers** in brackets: `[MIM:XXXXXX]`
- **PMIDs** in parentheses: `(PMID:XXXXXXXX)`
- **Inheritance** always stated in gene paragraph opening: "autosomal dominant" / "autosomal recessive"
- **One paragraph per variant** — never combine two variants into one paragraph
- **No bullet points** inside variant paragraphs — prose only
- **No first-person** ("I", "we") anywhere in report text
- Mechanistic claims are hedged: **"theoretically leads to"** — database/literature facts and the final classification are stated definitively

---

## Checklist

- [ ] Causative variant identified (from variant analysis)
- [ ] **VAF/genotype quality confirmed** — `genotypes[].vaf` consistent with zygosity expectation; `depth` ≥ 20×; low-VAF non-mosaicism-gene variants not classified
- [ ] `kb_get_disease` called to confirm disease name, inheritance, and phenotype fit before classifying
- [ ] `classify_variant` — `disease_name` includes OMIM number; all 28 criteria provided; reasoning text for every active criterion
- [ ] `mark_variant_for_report` — both variants marked for compound-het
- [ ] `get_report` reviewed before writing
- [ ] All 5 report fields written in one pass
- [ ] `get_report` confirms all fields saved

---

## Known limitation

`gene_descriptions` and `variant_descriptions` are stored correctly but render only in the **AI Analysis Draft** section of the UI — they do **not** populate the Primary Finding table columns. This is a known Noxia UI mismatch awaiting a fix.
