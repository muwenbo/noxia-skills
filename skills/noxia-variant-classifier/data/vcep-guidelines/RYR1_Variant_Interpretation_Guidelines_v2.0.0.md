# ClinGen Malignant Hyperthermia Susceptibility VCEP Variant Interpretation Guidelines for RYR1

**Version:** 2.0.0
**Released:** 3/1/2022
**Affiliation:** Malignant Hyperthermia Susceptibility VCEP
**Based on:** Richards et al., 2015 ACMG/AMP Guidelines

**Release Notes (v2.0.0):**
1. Revised PS4 such that at all strength levels an individual with two VUS/LP/P variants in RYR1 cannot be considered as supporting pathogenicity of either variant.
2. PS1 can be used at level moderate for previously classified likely pathogenic variant at the same codon with the same amino acid change.
3. PM5 can be used at level supporting for previously classified likely pathogenic variant at the same codon, different amino acid change.
4. PM1 should be downgraded to supporting when either PS1 or PM5 are used.

---

## Gene Information

| Attribute | Value |
|-----------|-------|
| **Gene** | RYR1 (HGNC:10483) |
| **HGNC Name** | ryanodine receptor 1 |
| **Transcript** | NM_000540.3 |
| **Disease** | Malignant hyperthermia of anesthesia (MONDO:0018493) |
| **Inheritance** | Autosomal dominant with reduced penetrance |

---

## Table of Contents

1. [Pathogenic Criteria](#pathogenic-criteria)
   - [PVS1 - Null Variant](#pvs1---null-variant)
   - [PS1 - Same Amino Acid Change](#ps1---same-amino-acid-change)
   - [PS2 - De Novo (Confirmed)](#ps2---de-novo-confirmed)
   - [PS3 - Functional Studies](#ps3---functional-studies)
   - [PS4 - Prevalence in Affected](#ps4---prevalence-in-affected)
   - [PM1 - Mutational Hot Spot](#pm1---mutational-hot-spot)
   - [PM2 - Absent from Controls](#pm2---absent-from-controls)
   - [PM3 - In Trans with Pathogenic](#pm3---in-trans-with-pathogenic)
   - [PM4 - Protein Length Changes](#pm4---protein-length-changes)
   - [PM5 - Novel Missense at Same Residue](#pm5---novel-missense-at-same-residue)
   - [PM6 - De Novo (Assumed)](#pm6---de-novo-assumed)
   - [PP1 - Co-segregation](#pp1---co-segregation)
   - [PP2 - Missense in Constrained Gene](#pp2---missense-in-constrained-gene)
   - [PP3 - Computational Evidence](#pp3---computational-evidence)
   - [PP4 - Phenotype Specificity](#pp4---phenotype-specificity)
   - [PP5 - Reputable Source](#pp5---reputable-source)
2. [Benign Criteria](#benign-criteria)
   - [BA1 - Allele Frequency >0.38%](#ba1---allele-frequency-038)
   - [BS1 - Frequency Greater Than Expected](#bs1---frequency-greater-than-expected)
   - [BS2 - Observed in Healthy Adult](#bs2---observed-in-healthy-adult)
   - [BS3 - Functional Studies (No Effect)](#bs3---functional-studies-no-effect)
   - [BS4 - Lack of Segregation](#bs4---lack-of-segregation)
   - [BP1-BP7 - Benign Supporting](#bp1-bp7---benign-supporting)
3. [Rules for Combining Criteria](#rules-for-combining-criteria)
4. [Appendices](#appendices)

---

## Pathogenic Criteria

### PVS1 - Null Variant

**Original ACMG Summary:** Null variant (nonsense, frameshift, canonical +/-1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.

**VCEP Specification:** **Not Applicable**

PVS1 is not applicable. MHS is due to gain-of-function variants in RYR1.

---

### PS1 - Same Amino Acid Change

**Original ACMG Summary:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change. Example: Val->Leu caused by either G>C or G>T in the same codon. Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:**

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Strong** | Same amino acid change as a previously established **pathogenic** variant regardless of nucleotide change. Previously established pathogenic variant must reach a classification of pathogenic **without** PS1. | None |
| **Moderate** | Same amino acid change as a previously established **likely pathogenic** variant regardless of nucleotide change. Previously established likely pathogenic variant must reach a classification of likely pathogenic **without** PS1. | Strength |

> **Note:** When PS1 is applied, PM1 should be downgraded to PM1_Supporting.

---

### PS2 - De Novo (Confirmed)

**Original ACMG Summary:** De novo (both maternity and paternity confirmed) in a patient with the disease and no family history. Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.

**VCEP Specifications:** Uses a point-based system shared with PM6. Each **proven** de novo case = 2 points; each **assumed** de novo case = 1 point.

#### PS2/PM6 Point System

| Total Points | Strength Level |
|--------------|----------------|
| ≥8 | Very Strong |
| 4-7 | Strong |
| 2-3 | Moderate |
| 1 | Supporting |

> **Modification Type:** Strength (all levels)

---

### PS3 - Functional Studies

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product. Note: Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.

**VCEP Specifications:**

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Strong** | Knock-in mouse showing MH reaction in response to RYR1 agonist **AND** increased sensitivity to RYR1 agonists in ex vivo tissue/cells | Strength, Disease-specific |
| **Moderate** | Increased sensitivity to RYR1 agonist in HEK293 in vitro assay, Ca²⁺ release significantly increased compared to WT, controls to include known pathogenic and benign variants, n≥3. **OR** Three or more independent ex vivo studies all showing release of Ca²⁺ in response to RYR1 agonist. **OR** Knock-in mouse showing MH reaction in response to RYR1 agonist **OR** increased sensitivity to RYR1 agonists in ex vivo tissue/cells (but not both, which would be PS3_Strong). | Strength, Disease-specific |
| **Supporting** | Two independent ex vivo studies all showing release of Ca²⁺ in response to RYR1 agonist | Strength, Disease-specific |

#### Approved Functional Assay Summary

| Assay Type | Description | PS3 Level |
|------------|-------------|-----------|
| Knock-in mouse (full) | MH reaction to RYR1 agonist AND increased ex vivo sensitivity | Strong |
| HEK293 in vitro | Ca²⁺ release increased vs WT, with P/B controls, n≥3 | Moderate |
| Ex vivo (≥3 studies) | Three or more independent studies showing Ca²⁺ release to agonist | Moderate |
| Knock-in mouse (partial) | MH reaction to agonist OR increased ex vivo sensitivity (not both) | Moderate |
| Ex vivo (2 studies) | Two independent studies showing Ca²⁺ release to agonist | Supporting |

---

### PS4 - Prevalence in Affected

**Original ACMG Summary:** The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.

**VCEP Specifications:**

PS4 uses a disease-specific **MH case point system**:
- Probands with a personal or family history of an **MH event** are awarded **0.5 points**
- Probands with a personal or family history of a **positive (MHS) IVCT/CHCT** are awarded an additional **0.5 points**
- **Exclusion:** Probands with multiple variants in RYR1 classified as VUS, likely pathogenic, or pathogenic are **not** considered

#### PS4 Strength Levels (Low-frequency variants: popmax ≤0.00006)

| Strength | MH Case Points Required | Popmax Threshold |
|----------|------------------------|------------------|
| **Strong** | ≥7 MH case points | gnomAD popmax ≤0.00006 |
| **Moderate** | 2-6 MH case points | gnomAD popmax ≤0.00006 |
| **Supporting** | 1 MH case point | gnomAD popmax ≤0.00006 |

#### PS4 Strength Levels (Higher-frequency variants: popmax >0.00006 and <0.0038)

| Strength | Odds Ratio Threshold | Popmax Requirement |
|----------|---------------------|-------------------|
| **Strong** | OR ≥18.7 (MH case points vs gnomAD allele count) | gnomAD popmax <0.0038 |
| **Moderate** | OR ≥4.33 (MH case points vs gnomAD allele count) | gnomAD popmax <0.0038 |
| **Supporting** | OR ≥2.08 (MH case points vs gnomAD allele count) | gnomAD popmax <0.0038 |

> **Modification Type:** Strength, Disease-specific (all levels)

---

### PM1 - Mutational Hot Spot

**Original ACMG Summary:** Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.

**VCEP Specifications:**

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Moderate** | Residues **1-552** (N-terminal region) and **2,101-2,458** (central region). PM1 should **not** be applied at moderate weight with PS1/PM5 — see PM1_Supporting. | Disease-specific |
| **Supporting** | Residues **1-552** (N-terminal region) and **2,101-2,458** (central region), **if PS1/PM5 applicable** then PM1 should be used at supporting. **OR** Residues **4,631-4,991** (C-terminal region). | Strength, Disease-specific |

#### PM1 Domain Summary

| Region | Residues | Default Strength | With PS1/PM5 |
|--------|----------|-----------------|--------------|
| N-terminal | 1-552 | Moderate | Supporting |
| Central | 2,101-2,458 | Moderate | Supporting |
| C-terminal | 4,631-4,991 | Supporting | Supporting |

---

### PM2 - Absent from Controls

**Original ACMG Summary:** Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium. Caveat: Population data for indels may be poorly called by next generation sequencing.

**VCEP Specification:** **Not Applicable**

PM2 is not used alone for RYR1/MHS classification.

---

### PM3 - In Trans with Pathogenic

**Original ACMG Summary:** For recessive disorders, detected in trans with a pathogenic variant. Note: This requires testing of parents (or offspring) to determine phase.

**VCEP Specification:** **Not Applicable**

PM3 is not applicable. MHS is inherited as an autosomal dominant trait with reduced penetrance.

---

### PM4 - Protein Length Changes

**Original ACMG Summary:** Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

**VCEP Specification:** **Not Applicable**

PM4 is not applicable. The majority of RYR1 variants that are causative for MHS are missense variants.

---

### PM5 - Novel Missense at Same Residue

**Original ACMG Summary:** Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before. Example: Arg156His is pathogenic; now you observe Arg156Cys. Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:**

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Moderate** | Missense change at an amino acid residue where a different missense variant previously determined to be **pathogenic**. Previously established pathogenic variant must reach a classification of pathogenicity **without** PM5. **Grantham score** for the alternate pathogenic variant must be **less than** for the variant being assessed. | None |
| **Supporting** | Missense change at an amino acid residue where a different missense variant previously determined to be **pathogenic or likely pathogenic**. Previously established likely pathogenic variant must reach a classification of likely pathogenic **without** PM5. **Grantham score** for the alternate likely pathogenic variant must be **less than** for the variant being assessed. | Strength, Disease-specific |

> **Note:** When PM5 is applied, PM1 should be downgraded to PM1_Supporting.

---

### PM6 - De Novo (Assumed)

**Original ACMG Summary:** Assumed de novo, but without confirmation of paternity and maternity.

**VCEP Specifications:** Same point-based system as PS2. Each **proven** de novo case = 2 points; each **assumed** de novo case = 1 point.

#### PM6 Point System (shared with PS2)

| Total Points | Strength Level |
|--------------|----------------|
| ≥8 | Very Strong |
| 4-7 | Strong |
| 2-3 | Moderate |
| 1 | Supporting |

> **Modification Type:** Strength (all levels)

---

### PP1 - Co-segregation

**Original ACMG Summary:** Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease. Note: May be used as stronger evidence with increasing segregation data.

**VCEP Specifications:**

| Strength | Meioses Required | Modification Type |
|----------|-----------------|-------------------|
| **Strong** | ≥7 reported meioses | Strength |
| **Moderate** | 5-6 reported meioses | Strength |
| **Supporting** | 3-4 reported meioses | Strength |

---

### PP2 - Missense in Constrained Gene

**Original ACMG Summary:** Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.

**VCEP Specification:** **Not Applicable**

PP2 is not applicable. RYR1 does not appear to be constrained for missense variation with a z-score of 1.92 in gnomAD.

---

### PP3 - Computational Evidence

**Original ACMG Summary:** Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.). Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.

**VCEP Specifications:**

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Moderate** | REVEL score **>0.85** | Strength |

---

### PP4 - Phenotype Specificity

**Original ACMG Summary:** Patient's phenotype or family history is highly specific for a disease with a single genetic etiology.

**VCEP Specification:** **Not Applicable**

PP4 is not applicable. Variants in CACNA1S also result in MHS.

---

### PP5 - Reputable Source

**Original ACMG Summary:** Reputable source recently reports variant as pathogenic, but the evidence is not available to the laboratory to perform an independent evaluation.

**VCEP Specification:** **Not Applicable**

This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PMID: 29543229).

---

## Benign Criteria

### BA1 - Allele Frequency >0.38%

**Original ACMG Summary:** Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

**VCEP Specification (Stand Alone):**
- gnomAD popmax allele frequency **>0.0038 (0.38%)**

> **Modification Type:** Disease-specific

---

### BS1 - Frequency Greater Than Expected

**Original ACMG Summary:** Allele frequency is greater than expected for disorder.

**VCEP Specification (Strong):**
- gnomAD popmax allele frequency **>0.0008 (0.08%)**

> **Modification Type:** Disease-specific

---

### BS2 - Observed in Healthy Adult

**Original ACMG Summary:** Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

**VCEP Specifications:**

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Strong** | Two or more variant-positive individuals with a **negative** IVCT/CHCT test | Disease-specific |
| **Moderate** | One variant-positive individual with a **negative** IVCT/CHCT test | Strength, Disease-specific |

---

### BS3 - Functional Studies (No Effect)

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

**VCEP Specifications:**

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Moderate** | Three or more independent ex vivo studies, **NO** significant release of Ca²⁺ in response to agonist | Strength, Disease-specific |
| **Supporting** | No significant increased sensitivity to RYR1 agonist in an approved in vitro assay, Ca²⁺ release measured, n≥3. **OR** One or two independent ex vivo studies, NO significant release of Ca²⁺ in response to agonist. **OR** Knock-in mouse showing no MH reaction in response to RYR1 agonist AND no increased sensitivity to RYR1 agonists in ex vivo tissue/cells. | Strength, Disease-specific |

#### BS3 Functional Evidence Summary

| Assay Type | Description | BS3 Level |
|------------|-------------|-----------|
| Ex vivo (≥3 studies) | Three or more independent studies, no Ca²⁺ release to agonist | Moderate |
| In vitro assay | No increased sensitivity in approved assay, n≥3 | Supporting |
| Ex vivo (1-2 studies) | One or two studies, no Ca²⁺ release to agonist | Supporting |
| Knock-in mouse | No MH reaction AND no increased ex vivo sensitivity | Supporting |

---

### BS4 - Lack of Segregation

**Original ACMG Summary:** Lack of segregation in affected members of a family.

**VCEP Specification:** **Not Applicable**

BS4 is not applicable. Phenotype for MHS is routinely determined based on the in vitro contracture test (IVCT) that has a false positive rate of approximately 6% (PP1) or the caffeine-halothane contracture test (CHCT). As the phenotype in individuals who have not experienced an MH crisis cannot be reliably determined, BS4 is not utilized.

---

### BP1-BP7 - Benign Supporting

| Criterion | Status | Specification |
|-----------|--------|---------------|
| **BP1** | Not Applicable | BP1 is not applicable. MH is caused primarily by missense variants in RYR1. |
| **BP2** | Supporting | Observed in **cis** with a pathogenic variant in any inheritance pattern. |
| **BP3** | Not Applicable | BP3 is not applicable. RYR1 does not have repetitive regions without known function. |
| **BP4** | Supporting | Computational evidence suggests no impact on gene or gene product; **REVEL score <0.5**. (Modification: Disease-specific) |
| **BP5** | Not Applicable | BP5 is not applicable as individuals have been described with MHS and two pathogenic variants in RYR1. |
| **BP6** | Not Applicable | This criterion is not for use as recommended by the ClinGen SVI VCEP Review Committee (PMID: 29543229). |
| **BP7** | Supporting | A synonymous (silent) variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved. |

---

## Rules for Combining Criteria

### Pathogenic Classification

| Criteria Combination |
|---------------------|
| 1 Very Strong **AND** ≥1 Strong |
| 1 Very Strong **AND** ≥2 Moderate |
| 1 Very Strong **AND** 1 Moderate **AND** 1 Supporting |
| 1 Very Strong **AND** ≥2 Supporting |
| ≥2 Strong |
| 1 Strong **AND** ≥3 Moderate |
| 1 Strong **AND** 2 Moderate **AND** ≥2 Supporting |
| 1 Strong **AND** 1 Moderate **AND** ≥4 Supporting |

### Likely Pathogenic Classification

| Criteria Combination |
|---------------------|
| 1 Very Strong **AND** 1 Moderate |
| 1 Strong **AND** 1 Moderate |
| 1 Strong **AND** ≥2 Supporting |
| ≥3 Moderate |
| 2 Moderate **AND** ≥2 Supporting |
| 1 Moderate **AND** ≥4 Supporting |

### Benign Classification

| Criteria Combination |
|---------------------|
| 1 Stand Alone (BA1) |
| ≥2 Strong |

### Likely Benign Classification

| Criteria Combination |
|---------------------|
| 1 Strong **AND** 1 Supporting |
| ≥2 Supporting |

---

## Appendices

### Appendix A: Applicable Criteria Summary

| Criterion | Applicable | Available Strengths | Key Notes |
|-----------|-----------|-------------------|-----------|
| PVS1 | No | — | MHS is gain-of-function |
| PS1 | Yes | Strong, Moderate | Moderate for LP variants |
| PS2 | Yes | Very Strong, Strong, Moderate, Supporting | Point-based (shared with PM6) |
| PS3 | Yes | Strong, Moderate, Supporting | Disease-specific functional assays |
| PS4 | Yes | Strong, Moderate, Supporting | MH case point system |
| PM1 | Yes | Moderate, Supporting | Domain-specific; downgrade with PS1/PM5 |
| PM2 | No | — | Not used alone |
| PM3 | No | — | MHS is autosomal dominant |
| PM4 | No | — | MHS caused by missense variants |
| PM5 | Yes | Moderate, Supporting | Grantham score requirement |
| PM6 | Yes | Very Strong, Strong, Moderate, Supporting | Point-based (shared with PS2) |
| PP1 | Yes | Strong, Moderate, Supporting | Meiosis count-based |
| PP2 | No | — | RYR1 z-score = 1.92 |
| PP3 | Yes | Moderate | REVEL >0.85 |
| PP4 | No | — | CACNA1S also causes MHS |
| PP5 | No | — | Not recommended by ClinGen SVI |
| BA1 | Yes | Stand Alone | Popmax >0.0038 |
| BS1 | Yes | Strong | Popmax >0.0008 |
| BS2 | Yes | Strong, Moderate | Negative IVCT/CHCT |
| BS3 | Yes | Moderate, Supporting | Disease-specific functional assays |
| BS4 | No | — | Phenotype unreliable without MH event |
| BP1 | No | — | MH is missense-driven |
| BP2 | Yes | Supporting | In cis with pathogenic only |
| BP3 | No | — | No repetitive regions |
| BP4 | Yes | Supporting | REVEL <0.5 |
| BP5 | No | — | Multiple P variants possible |
| BP6 | No | — | Not recommended by ClinGen SVI |
| BP7 | Yes | Supporting | Standard synonymous criteria |

### Appendix B: Population Frequency Thresholds Summary

| Criterion | Threshold | Strength |
|-----------|-----------|----------|
| BA1 | >0.0038 (0.38%) | Stand Alone |
| BS1 | >0.0008 (0.08%) | Strong |
| PS4 (low freq) | ≤0.00006 popmax | Required for case-count method |
| PS4 (higher freq) | <0.0038 popmax | Required for OR method |

### Appendix C: Computational Predictor Thresholds

| Predictor | Pathogenic Threshold (PP3) | Benign Threshold (BP4) |
|-----------|--------------------------|----------------------|
| REVEL | >0.85 (Moderate) | <0.5 (Supporting) |

### Appendix D: PM1 Functional Domain Map

```
RYR1 Protein (5,038 amino acids)
├── N-terminal region: residues 1-552       → PM1_Moderate (or Supporting with PS1/PM5)
├── Central region: residues 2,101-2,458    → PM1_Moderate (or Supporting with PS1/PM5)
├── [residues 553-2,100; 2,459-4,630]      → PM1 not applicable
└── C-terminal region: residues 4,631-4,991 → PM1_Supporting
```

### Appendix E: Key Disease-Specific Considerations

- **Mechanism:** MHS is caused by **gain-of-function** missense variants in RYR1 (not loss-of-function)
- **Inheritance:** Autosomal dominant with **reduced penetrance**
- **Phenotyping:** In vitro contracture test (IVCT) and caffeine-halothane contracture test (CHCT) are the primary phenotyping tools; IVCT has ~6% false positive rate
- **Genetic heterogeneity:** CACNA1S variants also cause MHS
- **Multi-variant considerations:** Individuals with two P/LP/VUS variants in RYR1 require special handling (excluded from PS4 case counts)

### Appendix F: Reference PMIDs

| PMID | Context |
|------|---------|
| 29543229 | ClinGen SVI recommendation — PP5/BP6 not for use |

---

## Version History

| Version | Date | Summary |
|---------|------|---------|
| 2.0.0 | 3/1/2022 | Revised PS4 multi-variant exclusion; PS1 moderate for LP; PM5 supporting for LP; PM1 downgrade rule with PS1/PM5 |

---

*This document was compiled from ClinGen Malignant Hyperthermia Susceptibility VCEP specifications. For the most current version, please refer to the [ClinGen website](https://clinicalgenome.org).*
