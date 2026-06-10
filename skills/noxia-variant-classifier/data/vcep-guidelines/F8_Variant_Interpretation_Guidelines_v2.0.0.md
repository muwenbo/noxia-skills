# ClinGen Coagulation Factor Deficiency VCEP Variant Interpretation Guidelines for F8

**Version:** 2.0.0
**Released:** 1/20/2026
**Affiliation:** Coagulation Factor Deficiency VCEP
**Based on:** Tavtigian et al., 2020 - Bayesian adaptation of Richards et al., 2015 ACMG/AMP Guidelines

---

## Gene Information

| Attribute | Value |
|-----------|-------|
| **Gene** | F8 (HGNC:3546) |
| **HGNC Name** | coagulation factor VIII |
| **Transcript** | NM_000132.4 |
| **Disease** | Hemophilia A (MONDO:0010602) |
| **Inheritance** | X-linked inheritance |

---

## Release Notes (v2.0.0)

**Edits post SVI Review:**
- PVS1 - Updated to include RNA recommendations based on Walker, et al paper
- PP3/BP4/BP7 - Updated SpliceAI cut off based on Walker, et al paper
- PS4 - Changed requirement that only 3 hemizygotes could be present in gnomAD in order to apply code. Now using a ratio to avoid needing to update regularly in the future
- BS2 - Fixed typo
- PS1 - Updated to include Walker, et al splicing recommendations
- PS3 - Decreased weight to supporting for all assays

---

## Table of Contents

1. [Pathogenic Criteria](#pathogenic-criteria)
   - [PVS1 - Null Variant](#pvs1---null-variant)
   - [PS1 - Same Amino Acid Change](#ps1---same-amino-acid-change)
   - [PS2 - De Novo](#ps2---de-novo)
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
   - [BA1 - Allele Frequency Stand Alone](#ba1---allele-frequency-stand-alone)
   - [BS1 - Frequency Greater Than Expected](#bs1---frequency-greater-than-expected)
   - [BS2 - Observed in Healthy Adult](#bs2---observed-in-healthy-adult)
   - [BS3 - Functional Studies (No Effect)](#bs3---functional-studies-no-effect)
   - [BS4 - Lack of Segregation](#bs4---lack-of-segregation)
   - [BP1-BP7 - Benign Supporting](#bp1-bp7---benign-supporting)
3. [Point-Based Classification System](#point-based-classification-system)
4. [Rules for Combining Criteria](#rules-for-combining-criteria)
5. [Appendices](#appendices)
   - [Appendix A: PVS1 Decision Tree](#appendix-a-pvs1-decision-tree)
   - [Appendix B: PS2/PM6 De Novo Guidance](#appendix-b-ps2pm6-de-novo-guidance)
   - [Appendix C: Approved Functional Assays](#appendix-c-approved-functional-assays)
   - [Appendix D: Guidance for Combining Conflicting Criteria](#appendix-d-guidance-for-combining-conflicting-criteria)

---

## Pathogenic Criteria

### PVS1 - Null Variant

**Original ACMG Summary:** Null variant (nonsense, frameshift, canonical +/-1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.

**Caveats:**
- Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7)
- Use caution interpreting LOF variants at the extreme 3' end of a gene
- Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact
- Use caution in the presence of multiple transcripts

**VCEP Specifications:**

Apply the ClinGen Coagulation Factor Deficiency VCEP/SVI decision tree to determine use and strength of the PVS1 rule.

**PVS1 (RNA):** Assays demonstrating a variant leads to aberrant splicing profile can be used in the PVS1 decision tree as described in Walker et al. (PMID: 36865205) that was added to the v1 CFD-VCEP PVS1 flowchart. **If using PVS1(RNA), do not apply PP3.**

#### Strength Levels

| Strength | Criteria | Point Value |
|----------|----------|-------------|
| **Very Strong** | Per Coagulation Factor Deficiency VCEP/SVI PVS1 decision tree | 8 |
| **Strong** | Per Coagulation Factor Deficiency VCEP/SVI PVS1 decision tree | 4 |
| **Moderate** | Per Coagulation Factor Deficiency VCEP/SVI PVS1 decision tree | 2 |

#### PVS1 Decision Tree Summary

**Nonsense or Frameshift:**

| Variant Type | NMD Prediction | Strength |
|--------------|----------------|----------|
| Nonsense up to c.6851 | Predicted to undergo NMD | PVS1 |
| Nonsense from c.6852 | NOT predicted to undergo NMD | PVS1_Strong |
| Frameshift -1/+2 up to c.6826 | Predicted to undergo NMD | PVS1 |
| Frameshift -1/+2 from c.6827 | NOT predicted to undergo NMD | PVS1_Strong |
| Frameshift +1/-2 up to c.6728 | Predicted to undergo NMD | PVS1 |
| Frameshift +1/-2 from c.6729 | NOT predicted to undergo NMD | PVS1_Strong |

**Canonical Splice Sites (GT-AG at +/-1,2):**

| Scenario | Exons | Strength |
|----------|-------|----------|
| Exon skipping/cryptic splice disrupts reading frame AND predicted to undergo NMD | Exons 1, 2, 7-12, 14, 15, 17, 21, 23, 24 | PVS1 |
| Exon skipping/cryptic splice preserves reading frame, truncated region critical | Exons 3-6, 13, 16, 18-20, 22, 26 | PVS1_Strong |
| Exon skipping/cryptic splice disrupts reading frame AND NOT predicted to undergo NMD | Exon 25 | PVS1_Strong |

**Deletions (Single exon to full gene):**

| Deletion Type | Impact | Strength |
|---------------|--------|----------|
| Single to multi exon deletion | Disrupts reading frame AND predicted to undergo NMD | PVS1 |
| Single to multi exon deletion | Disrupts reading frame AND NOT predicted to undergo NMD, removes >10% of protein | PVS1_Strong |
| Single to multi exon deletion | Disrupts reading frame AND NOT predicted to undergo NMD, removes <10% of protein | PVS1_Moderate |
| Single to multi exon deletion | Preserves reading frame, truncated region critical (e.g., exon 26) | PVS1_Strong |
| Single to multi exon deletion | Preserves reading frame, role of region unknown | PVS1_Moderate |
| Full gene deletion | N/A | PVS1 |

**Duplications (>=1 exon, completely contained within gene):**

| Duplication Type | Impact | Strength |
|------------------|--------|----------|
| Proven in tandem | Reading frame disrupted AND NMD predicted | PVS1 |
| Presumed in tandem | Reading frame presumed disrupted AND NMD predicted | PVS1_Moderate |
| Proven not in tandem | No or unknown impact on reading frame and NMD | N/A |

**Initiation Codon:**

| Scenario | Strength |
|----------|----------|
| No known alternative start codon in other transcripts AND >=1 pathogenic variant(s) upstream of closest potential in-frame start codon | PVS1_Moderate |

> **Note:** Next in-frame start codon at position 32 (c.96; kozak: -3G; +4G); at least 4 P/LP variants in ClinVar upstream of c.96

---

### PS1 - Same Amino Acid Change

**Original ACMG Summary:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.

**Example:** Val->Leu caused by either G>C or G>T in the same codon.

**Caveat:** Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:**

| Strength | Criteria | Point Value |
|----------|----------|-------------|
| **Strong** | This evidence code can be applied when there is 1 pathogenic variant or 2 likely pathogenic variants at the same residue based on F8 gene rule specifications from the Coagulation Factor Deficiency VCEP and where *in silico* predictors do not suggest a splicing defect. **OR** When two or more variants share the same predicted splicing effect and one comparison splicing variant reaches a pathogenic classification or 2 comparison variants reach a likely pathogenic classification using the Coagulation Factor Deficiency VCEP specifications modified from Walker, et al 2023 (PMID: 37352859). | 4 |
| **Moderate** | This evidence code can be applied when there is 1 likely pathogenic variant at the same residue based on F8 gene rule specifications from the Coagulation Factor Deficiency VCEP and where *in silico* predictors do not suggest a splicing defect. **OR** When the comparison variant shares the same predicted splicing effect and the comparison splicing variant reaches a likely pathogenic classification using the Coagulation Factor Deficiency VCEP specifications based on Walker, et al 2023 (PMID: 37352859). | 2 |

---

### PS2 - De Novo

**Original ACMG Summary:** De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.

**Note:** Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.

**VCEP Specifications:**

Use ClinGen's de novo modified point system for a **highly specific phenotype** (see guidance below). Probands must meet the PS4 phenotype criteria to apply this code. Combine all assumed and confirmed de novo cases for this code and use at the appropriate strength based on amount of points for all probands.

#### PS2/PM6 Combined Point System

Use the phenotype consistency "**Phenotype highly specific for gene**" (1st option) for hemophilia A.

| Points | De Novo Status | Strength Level | Point Value |
|--------|----------------|----------------|-------------|
| 4 points | Confirmed de novo | Very Strong | 8 |
| 2 points | Confirmed de novo | Strong | 4 |
| 1 point | Assumed de novo | Moderate | 2 |
| 0.5 point | Assumed de novo | Supporting | 1 |

#### ClinGen SVI De Novo Point Values

| Phenotypic Consistency | Confirmed Parental Relationships | Unconfirmed |
|------------------------|----------------------------------|-------------|
| Phenotype highly specific for gene | 2 points | 1 point |
| Phenotype consistent but not highly specific | 1 point | 0.5 points |
| Phenotype consistent + high genetic heterogeneity | 0.5 points | 0.25 points |
| Phenotype not consistent | 0 points | 0 points |

---

### PS3 - Functional Studies

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.

**Note:** Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.

**VCEP Specifications:**

| Strength | Criteria | Point Value |
|----------|----------|-------------|
| **Supporting** | Abnormal factor VIII activity (<40 IU/dL or 40%) via one-stage or two-stage chromogenic assay in a cell line and/or mouse model. **--OR--** Absent or significantly reduced factor VIII antigen levels compared to wildtype in a cell line by quantitative assay. | 1 |

> **Note:** PS3 has been decreased to supporting strength for all assays in v2.0.0.

---

### PS4 - Prevalence in Affected

**Original ACMG Summary:** The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.

**VCEP Specifications:**

#### Hemophilia A Phenotype Requirements:

1. **Severe hemophilia A:** Abnormal factor VIII activity levels in the severe range (**< 1% factor VIII activity level**) are sufficient to confer a diagnosis of hemophilia A.

2. **Mild/Moderate hemophilia A (1-40% factor VIII activity level):**
   - There must be a clear pattern of X-linked inheritance (i.e., more than a sibling pair)
   - If the proband is a simplex case, there are only affected siblings, or no family history information is available, documentation that **von Willebrand disease (VWD) type 2N was ruled out** as a diagnosis is required

   **Exceptions when VWD 2N documentation is not available:**
   1. If VWD 2N is ruled out in at least one proband, all other probands can be counted, OR
   2. If there are 4 or more unrelated probands reported with mild or moderate hemophilia A, all probands can be counted

#### gnomAD Ratio Requirement:

The PS4 code is only applicable to variants with a ratio **lower than or equal to 1.26 x 10^-5**.

**Ratio calculation:** # of hemizygotes with variant of interest / total # of alleles from XY individuals sequenced in the database

> **Note:** This ratio was set by using the most frequently seen pathogenic variant, F8 c.1834C>T, p.Arg612Cys, in gnomAD that was studied in the Coagulation Factor Deficiency VCEP pilot F8 study.

#### Strength Levels

| Strength | Number of Probands | Point Value |
|----------|-------------------|-------------|
| **Very Strong** | >=8 probands meet criteria | 8 |
| **Strong** | 4-7 probands meet criteria | 4 |
| **Moderate** | 2-3 probands meet criteria | 2 |
| **Supporting** | 1 proband meets criteria | 1 |

---

### PM1 - Mutational Hot Spot

**Original ACMG Summary:** Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.

**VCEP Specifications:**

This rule is applicable to the variant residues noted below based on activity that is critical to the function of the factor VIII protein (PMID: 33592631, 35722946). **Combined weight of codes PM1 and PM5 applied for a single variant can only equal strong.**

#### Strength Levels

| Strength | Residues | Point Value |
|----------|----------|-------------|
| **Strong** | R391-S392, R759-S760, E1701-Q1705, R1708-S1709, Y1683, Y1689, Y737, Y742 | 4 |
| **Moderate** | **Residues affecting secretion:** Arg1667, Arg1332; **FXa-binding residues:** Gly2267-Gly2304 (with the exception of Ser2283) | 2 |

---

### PM2 - Absent from Controls

**Original ACMG Summary:** Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

**Caveat:** Population data for indels may be poorly called by next generation sequencing.

**VCEP Specifications:**

| Strength | Criteria | Point Value |
|----------|----------|-------------|
| **Supporting** | Variant must be absent in males in population databases, such as gnomAD | 1 |

---

### PM3 - In Trans with Pathogenic

**Original ACMG Summary:** For recessive disorders, detected in trans with a pathogenic variant.

**Note:** This requires testing of parents (or offspring) to determine phase.

**VCEP Specifications:** **Not Applicable** for the F8 gene.

---

### PM4 - Protein Length Changes

**Original ACMG Summary:** Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

**VCEP Specifications:**

| Strength | Criteria | Point Value |
|----------|----------|-------------|
| **Moderate** | Use code with no specification | 2 |

---

### PM5 - Novel Missense at Same Residue

**Original ACMG Summary:** Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.

**Example:** Arg156His is pathogenic; now you observe Arg156Cys.

**Caveat:** Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:**

**Combined weight of codes PM1 and PM5 applied for a single variant can only equal strong.**

| Strength | Criteria | Point Value |
|----------|----------|-------------|
| **Moderate** | This evidence code can be applied when there is 1 pathogenic variant or 2 likely pathogenic variants at the same residue based on the F8 rule specifications from the Coagulation Factor Deficiency VCEP and where *in silico* predictors do not suggest a splicing defect. | 2 |
| **Supporting** | This evidence code can be applied when there is 1 likely pathogenic variant at the same residue based on the F8 rule specifications from the Coagulation Factor Deficiency VCEP and where *in silico* predictors do not suggest a splicing defect. | 1 |

---

### PM6 - De Novo (Assumed)

**Original ACMG Summary:** Assumed de novo, but without confirmation of paternity and maternity.

**VCEP Specifications:** **Not Applicable**

This rule code is combined with PS2. Please combine assumed de novo cases with confirmed de novo cases and apply PS2 at the appropriate weight.

---

### PP1 - Co-segregation

**Original ACMG Summary:** Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.

**Note:** May be used as stronger evidence with increasing segregation data.

**VCEP Specifications:**

Base strength of rule code on number of meioses across one or more families.

| Strength | Criteria | Point Value |
|----------|----------|-------------|
| **Strong** | The code is applicable when there are >=4 meioses across >=2 families | 4 |
| **Moderate** | The code is applicable when there are at least 3 meioses across one or more families | 2 |
| **Supporting** | The code is applicable when there are 2 meioses in one family **OR** 1 meiosis between 2 affected siblings | 1 |

---

### PP2 - Missense in Constrained Gene

**Original ACMG Summary:** Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.

**VCEP Specifications:** **Not Applicable** for F8.

---

### PP3 - Computational Evidence

**Original ACMG Summary:** Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).

**Caveat:** As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.

**VCEP Specifications:**

**Do not apply PP3 for variants that meet criteria for a PVS1_RNA rule code.**

| Strength | Criteria | Point Value |
|----------|----------|-------------|
| **Supporting** | Code can be applied for variants where the **REVEL score is >= 0.6** or a **SpliceAI score of >= 0.2** | 1 |

---

### PP4 - Phenotype Specificity

**Original ACMG Summary:** Patient's phenotype or family history is highly specific for a disease with a single genetic etiology.

**VCEP Specifications:**

#### Hemophilia A Phenotype Requirements:

1. **Severe hemophilia A:** Abnormal factor VIII activity levels in the severe range (**< 1% factor VIII activity level**) are sufficient to confer a diagnosis of hemophilia A.

2. **Mild/Moderate hemophilia A (1-40% factor VIII activity level):**
   - There must be a clear pattern of X-linked inheritance (i.e., more than a sibling pair)
   - If the proband is a simplex case, there are only affected siblings, or no family history information is available, documentation that **von Willebrand disease (VWD) type 2N was ruled out** as a diagnosis is required

   **Exceptions when VWD 2N documentation is not available:**
   1. If VWD 2N is ruled out in at least one proband, all other probands can be counted, OR
   2. If there are 4 or more unrelated probands reported with mild or moderate hemophilia A, all probands can be counted

3. **Full gene sequencing and deletion/duplication analysis** of the F8 gene is required to use this rule code

4. This rule code is **not eligible for any variants meeting BA1 criteria**

5. A proband used for PP4 **cannot be used for PS4**

| Strength | Criteria | Point Value |
|----------|----------|-------------|
| **Moderate** | Proband must meet hemophilia A phenotype criteria AND have full gene sequencing and deletion/duplication analysis | 2 |

---

### PP5 - Reputable Source

**Original ACMG Summary:** Reputable source recently reports variant as pathogenic, but the evidence is not available to the laboratory to perform an independent evaluation.

**VCEP Specifications:** **Not Applicable**

This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee. (PMID: 29543229)

---

## Benign Criteria

### BA1 - Allele Frequency Stand Alone

**Original ACMG Summary:** Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

**VCEP Specifications:**

99.99% CI; subpopulation must have a minimum of five variant alleles present. Males and females are included for this code.

| Strength | Criteria |
|----------|----------|
| **Stand Alone** | MAF cutoff of **>= 0.0333%** (or 0.000333) |

---

### BS1 - Frequency Greater Than Expected

**Original ACMG Summary:** Allele frequency is greater than expected for disorder.

**VCEP Specifications:**

99.99% CI; subpopulation must have a minimum of five variant alleles present. Males and females are included for this code.

| Strength | Criteria | Point Value |
|----------|----------|-------------|
| **Strong** | MAF cutoff of **>= 0.00333%** (or 0.0000333) | -4 |

---

### BS2 - Observed in Healthy Adult

**Original ACMG Summary:** Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

**VCEP Specifications:**

This code is **not applicable if there is a normal one stage factor VIII level and an abnormal factor VIII using a chromogenic assay or vice versa.**

| Strength | Criteria | Point Value |
|----------|----------|-------------|
| **Strong** | This evidence code can be used when a F8 variant is observed in a male with a normal factor VIII activity level (at least >40% IU or as defined by laboratory cut off) using a one stage and/or a chromogenic assay | -4 |

---

### BS3 - Functional Studies (No Effect)

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

**VCEP Specifications:**

| Strength | Criteria | Point Value |
|----------|----------|-------------|
| **Strong** | This code can be used for F8 gene variants studied in a cell line or mouse model setting that confer a **normal factor VIII activity level AND normal factor VIII antigen level OR normal Western Blot** | -4 |
| **Supporting** | This code can be used for F8 gene variants studied in a cell line or mouse model setting that confer: **Normal factor VIII activity level**, OR **Abnormal factor VIII activity level with abnormal 2N binding assay suggesting a diagnosis of VWD Normandy (VWD 2N) instead of hemophilia A** | -1 |

---

### BS4 - Lack of Segregation

**Original ACMG Summary:** Lack of segregation in affected members of a family.

**Caveat:** The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.

**VCEP Specifications:**

| Strength | Criteria | Point Value |
|----------|----------|-------------|
| **Strong** | This evidence code can be used when a F8 variant is observed in a male with a family history of hemophilia A and has a normal factor VIII activity level | -4 |

---

### BP1-BP7 - Benign Supporting

| Criterion | Status | Comment | Point Value |
|-----------|--------|---------|-------------|
| **BP1** | Not Applicable | Not applicable for F8 gene | N/A |
| **BP2** | Not Applicable | Not being used at this time. There are reports of males with hemophilia having two suspicious pathogenic variants | N/A |
| **BP3** | Not Applicable | Not applicable for F8 gene | N/A |
| **BP4** | Applicable | Code can be applied for variants reaching a **REVEL score of 0.3 or below AND a SpliceAI score of <= 0.1** | -1 |
| **BP5** | Not Applicable | While unlikely, it is possible for males with hemophilia to also have a diagnosis of von Willebrand Normandy (or VWD 2N) | N/A |
| **BP6** | Not Applicable | This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PMID: 29543229) | N/A |
| **BP7** | Applicable | Also applicable to non-canonical intronic variants. The use of BP7 with BP4 is allowed, as appropriate, to classify variants meeting both criteria as likely benign | See below |

#### BP7 Strength Levels

| Strength | Criteria | Point Value |
|----------|----------|-------------|
| **Strong** | Applicable for variants that have no observable splicing impact with RNA sequencing and/or minigene assay and a **SpliceAI score of <= 0.1** | -4 |
| **Supporting** | SpliceAI should be used to suggest no splicing impact. Splicing prediction score of **<= 0.1** is required. Conservation should be assessed using **PhyloP (cutoff < 0.1)** and **PhastCons (cutoff < 0.5)** | -1 |

---

## Point-Based Classification System

The Coagulation Factor Deficiency VCEP uses the point-based classification system from Tavtigian et al., 2020 (PMID: 32720330).

### Evidence Point Values

| Evidence Level | Pathogenic Points | Benign Points |
|----------------|-------------------|---------------|
| Very Strong | 8 | N/A |
| Strong | 4 | -4 |
| Moderate | 2 | -2 |
| Supporting | 1 | -1 |
| Stand Alone | N/A | N/A (BA1) |

### Classification Thresholds

| Category | Point Range |
|----------|-------------|
| **Pathogenic** | >= 10 |
| **Likely Pathogenic** | 6 - 9 |
| **Uncertain Significance** | 0 - 5 |
| **Likely Benign** | -6 to -1 |
| **Benign** | <= -7 |

---

## Rules for Combining Criteria

### Standard ACMG/AMP Combining Rules

#### Pathogenic Classification

| Criteria Combination |
|---------------------|
| 1 Very Strong **AND** >=1 Strong |
| 1 Very Strong **AND** >=2 Moderate |
| 1 Very Strong **AND** 1 Moderate **AND** 1 Supporting |
| 1 Very Strong **AND** >=2 Supporting |
| >=2 Strong |
| 1 Strong **AND** >=3 Moderate |
| 1 Strong **AND** 2 Moderate **AND** >=2 Supporting |
| 1 Strong **AND** 1 Moderate **AND** >=4 Supporting |

#### Likely Pathogenic Classification

| Criteria Combination |
|---------------------|
| 1 Very Strong **AND** 1 Moderate |
| 1 Strong **AND** 1 Moderate |
| 1 Strong **AND** >=2 Supporting |
| >=3 Moderate |
| 2 Moderate **AND** >=2 Supporting |
| 1 Moderate **AND** >=4 Supporting |
| 1 Strong **AND** 2 Moderate |

#### Benign Classification

| Criteria Combination |
|---------------------|
| >=2 Strong |
| 1 Stand Alone (BA1) |

#### Likely Benign Classification

| Criteria Combination |
|---------------------|
| 1 Strong **AND** 1 Supporting |
| >=2 Supporting |

### Combining Conflicting Criteria

For F8 variants where criteria codes for **both benign and pathogenic evidence apply**, these variants are **not subjected to an automatic variant of uncertain significance (VUS) classification**. Instead, application of the rule combination point system described by Tavtigian, et al. 2020 (PMID: 32720330) is recommended.

**Process:**
1. Use the point values table to determine how many points each evidence code is worth
2. Sum all point values (positive and negative)
3. Use the classification thresholds to determine the final classification

---

## Appendices

### Appendix A: PVS1 Decision Tree

#### Nonsense or Frameshift Variants

```
Nonsense or Frameshift
    |
    +-- Predicted to undergo NMD
    |       |-- Nonsense up to c.6851 --> PVS1
    |       |-- Frameshift -1/+2 up to c.6826 --> PVS1
    |       |-- Frameshift +1/-2 up to c.6728 --> PVS1
    |
    +-- NOT predicted to undergo NMD
            |-- Nonsense from c.6852 --> PVS1_Strong*
            |-- Frameshift -1/+2 from c.6827 --> PVS1_Strong*
            |-- Frameshift +1/-2 from c.6729 --> PVS1_Strong*

*Downstream of c.6852: 3 variants get to LP or P without PVS1 based on VCEP rules
and 2 ClinVar missense variants are classified P and therefore warrant use of
PVS1 at the strong level.
```

#### Canonical Splice Sites (GT-AG +/-1,2)

```
Splice Site Variant
    |
    +-- Exon skipping/cryptic splice DISRUPTS reading frame
    |       |-- Predicted to undergo NMD (Exons 1,2,7-12,14,15,17,21,23,24) --> PVS1
    |       |-- NOT predicted to undergo NMD (Exon 25) --> PVS1_Strong
    |
    +-- Exon skipping/cryptic splice PRESERVES reading frame
            |-- Truncated region critical (Exons 3-6,13,16,18-20,22,26) --> PVS1_Strong
            |-- Role of region unknown --> PVS1_Moderate
```

#### Deletions

```
Deletion (Single exon to full gene)
    |
    +-- Full gene deletion --> PVS1
    |
    +-- Single to multi-exon deletion
            |
            +-- Disrupts reading frame
            |       |-- Predicted to undergo NMD --> PVS1
            |       |-- NOT predicted to undergo NMD
            |               |-- Removes >10% of protein --> PVS1_Strong
            |               |-- Removes <10% of protein --> PVS1_Moderate
            |
            +-- Preserves reading frame
                    |-- Truncated region critical --> PVS1_Strong
                    |-- Role of region unknown --> PVS1_Moderate
```

> **Note:** Exons 8 and 14 contain all the PM1_Strong residues

#### Duplications

```
Duplication (>=1 exon, completely contained within gene)
    |
    +-- Proven in tandem
    |       |-- Reading frame disrupted AND NMD predicted --> PVS1
    |       |-- No/unknown impact on reading frame and NMD --> N/A
    |
    +-- Presumed in tandem
    |       |-- Reading frame presumed disrupted AND NMD predicted --> PVS1_Moderate
    |
    +-- Proven not in tandem --> N/A
```

#### Initiation Codon

```
Initiation Codon Variant
    |
    +-- No known alternative start codon
            |-- >=1 P/LP variant upstream of closest in-frame start codon --> PVS1_Moderate

Note: Next in-frame start codon at position 32 (c.96; kozak: -3G; +4G)
At least 4 P/LP variants in ClinVar upstream of c.96
```

> **Important:** When PVS1 is applied using RNA splicing data, PP3 cannot be applied.

---

### Appendix B: PS2/PM6 De Novo Guidance

Use the **ClinGen SVI Recommendations for Applying de novo Evidence**.

For hemophilia A and B, use the phenotype consistency **"Phenotype highly specific for gene"** (1st option).

#### Point Assignment

| Phenotypic Consistency | Confirmed Parental Relationships | Unconfirmed |
|------------------------|----------------------------------|-------------|
| Phenotype highly specific for gene | 2 points | 1 point |
| Phenotype consistent but not highly specific | 1 point | 0.5 points |
| Phenotype consistent + high genetic heterogeneity | 0.5 points | 0.25 points |
| Phenotype not consistent | 0 points | 0 points |

#### Strength Determination

| Total Points | Strength Level |
|--------------|----------------|
| 0.5 points | Supporting |
| 1.0 point | Moderate |
| 2.0 points | Strong |
| 4.0 points | Very Strong |

---

### Appendix C: Approved Functional Assays

#### One-Stage Clotting Assay (OSA)

| Reference | Description | Cell Line | Approved | Strength |
|-----------|-------------|-----------|----------|----------|
| Pipe 1999 (PMID: 9864159) | One-stage clotting assay using MLA Electra 750 fibrinometer by reconstitution of human FVIII-deficient plasma | COS-1 cells | Yes | PS3_Supporting |
| Pezeshkpoor 2019 (PMID: 30997536) | One-stage clotting assay - aPTT-based commercial assay | COS-1 cells | Yes | PS3_Supporting |
| Roualdes 2015 (PMID: 25708597) | One-stage clotting assay based on aPTT with APTT-HS reagent (Stago) | COS-1 cells | Yes | PS3_Supporting |

#### Two-Stage Chromogenic Assay (CSA)

| Reference | Description | Cell Line | Approved | Strength |
|-----------|-------------|-----------|----------|----------|
| Pipe 1999 (PMID: 9864159) | Modified two-stage assay using COAMATIC chromogenic assay | COS-1 cells | Yes | PS3_Supporting |
| Pezeshkpoor 2019 (PMID: 30997536) | Two-stage chromogenic assay - commercial chromogenic assay | COS-1 cells | Yes | PS3_Supporting |

#### ELISA Assay

| Reference | Description | Cell Line | Approved | Strength |
|-----------|-------------|-----------|----------|----------|
| Roualdes 2015 (PMID: 25708597) | ELISA assay using Asserachrom FVIII kit (Stago) | COS-1 cells | Yes | PS3_Supporting |
| Jourdy 2016 (PMID: 26915717) | ELISA - FVIII:Ag quantified with Asserchrom FVIII:Ag kit (Diagnostica Stago) | COS-1 cells | Yes | PS3_Supporting |

#### Assay Thresholds

| Assay Type | Normal Readout | Abnormal Readout |
|------------|----------------|------------------|
| One-stage clotting | Similar to wildtype | Different from wildtype |
| Chromogenic | Similar to wildtype | Different from wildtype |
| ELISA | No statistical difference from wildtype | Statistically different from wildtype |

---

### Appendix D: Guidance for Combining Conflicting Criteria

For F8 variants where criteria codes for benign and pathogenic evidence apply, these variants are not subjected to an automatic variant of uncertain significance (VUS) classification. Instead, the rule combination point system described by Tavtigian, et al. 2020 (PMID: 32720330) is recommended.

#### Point Values (Tavtigian et al., Table 2)

| Evidence Strength | Pathogenic Points | Benign Points |
|-------------------|-------------------|---------------|
| Very Strong | 8 | N/A |
| Strong | 4 | -4 |
| Moderate | 2 | -2 |
| Supporting | 1 | -1 |

#### Classification from Point Sum (Tavtigian et al., Table 3)

| Total Points | Classification |
|--------------|----------------|
| >= 10 | Pathogenic |
| 6 to 9 | Likely Pathogenic |
| 0 to 5 | Uncertain Significance |
| -1 to -6 | Likely Benign |
| <= -7 | Benign |

---

### Appendix E: Population Frequency Thresholds Summary

| Criterion | Threshold | Strength | Notes |
|-----------|-----------|----------|-------|
| BA1 | >= 0.0333% | Stand Alone | 99.99% CI; min 5 variant alleles; males and females included |
| BS1 | >= 0.00333% | Strong | 99.99% CI; min 5 variant alleles; males and females included |
| PM2 | Absent in males | Supporting | Population databases such as gnomAD |
| PS4 ratio | <= 1.26 x 10^-5 | Required for PS4 | # hemizygotes / total # alleles from XY individuals |

---

### Appendix F: In Silico Predictor Thresholds

| Criterion | Predictor | Threshold | Direction |
|-----------|-----------|-----------|-----------|
| PP3 | REVEL | >= 0.6 | Pathogenic |
| PP3 | SpliceAI | >= 0.2 | Pathogenic |
| BP4 | REVEL | <= 0.3 | Benign |
| BP4 | SpliceAI | <= 0.1 | Benign |
| BP7 | SpliceAI | <= 0.1 | Benign |
| BP7 | PhyloP | < 0.1 | Not conserved |
| BP7 | PhastCons | < 0.5 | Not conserved |

---

### Appendix G: Key References

| PMID | Citation | Topic |
|------|----------|-------|
| 36865205 | Walker et al. | RNA recommendations for PVS1 |
| 37352859 | Walker et al. 2023 | Splicing predictions for PS1 |
| 33592631 | - | PM1 critical residues |
| 35722946 | - | PM1 critical residues |
| 32720330 | Tavtigian et al. 2020 | Point-based classification system |
| 29543229 | - | PP5/BP6 not recommended |

---

## Criteria Summary Table

| Criterion | Applicable | Strength(s) Available | Notes |
|-----------|------------|----------------------|-------|
| PVS1 | Yes | Very Strong, Strong, Moderate | Use decision tree; RNA option available |
| PS1 | Yes | Strong, Moderate | Check splicing predictions |
| PS2 | Yes | Very Strong, Strong, Moderate, Supporting | Combined with PM6; use point system |
| PS3 | Yes | Supporting only | All assays decreased to supporting in v2.0.0 |
| PS4 | Yes | Very Strong, Strong, Moderate, Supporting | Proband count based; ratio requirement |
| PM1 | Yes | Strong, Moderate | Specific residues; combined with PM5 max = Strong |
| PM2 | Yes | Supporting only | Absent in males |
| PM3 | No | N/A | Not applicable for X-linked |
| PM4 | Yes | Moderate | No modification |
| PM5 | Yes | Moderate, Supporting | Combined with PM1 max = Strong |
| PM6 | No | N/A | Combined with PS2 |
| PP1 | Yes | Strong, Moderate, Supporting | Meiosis-based |
| PP2 | No | N/A | Not applicable for F8 |
| PP3 | Yes | Supporting | REVEL >= 0.6 or SpliceAI >= 0.2 |
| PP4 | Yes | Moderate | Full sequencing required |
| PP5 | No | N/A | Not recommended |
| BA1 | Yes | Stand Alone | MAF >= 0.0333% |
| BS1 | Yes | Strong | MAF >= 0.00333% |
| BS2 | Yes | Strong | Male with normal FVIII activity |
| BS3 | Yes | Strong, Supporting | Activity + antigen for strong |
| BS4 | Yes | Strong | Male with family history + normal FVIII |
| BP1 | No | N/A | Not applicable for F8 |
| BP2 | No | N/A | Not used |
| BP3 | No | N/A | Not applicable for F8 |
| BP4 | Yes | Supporting | REVEL <= 0.3 AND SpliceAI <= 0.1 |
| BP5 | No | N/A | Not applicable |
| BP6 | No | N/A | Not recommended |
| BP7 | Yes | Strong, Supporting | RNA evidence or conservation |

---

*This document was compiled from ClinGen Coagulation Factor Deficiency VCEP specifications v2.0.0. For the most current version, please refer to the ClinGen website.*
