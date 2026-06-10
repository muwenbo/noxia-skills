# ClinGen Coagulation Factor Deficiency Expert Panel Variant Interpretation Guidelines for F9

**Version:** 2.0.0
**Released:** January 20, 2026
**Affiliation:** Coagulation Factor Deficiency VCEP
**Based on:** Tavtigian et al., 2020 - Bayesian adaptation of Richards et al., 2015 ACMG/AMP Guidelines

---

## Gene Information

| Attribute | Value |
|-----------|-------|
| **Gene** | F9 (HGNC:3551) |
| **HGNC Name** | coagulation factor IX |
| **Transcript** | NM_000133.4 |
| **Disease** | Hemophilia B (MONDO:0010604) |
| **Inheritance** | X-linked inheritance |

---

## General Comments

When pathogenic and benign rule codes are applied, see guidance below for the point counting variant classification system rather than defer to classification of variant of uncertain significance.

---

## Release Notes (v2.0.0)

Edits post SVI review:
- **PVS1** - Updated to include RNA recommendations based on Walker, et al paper
- **PP3/BP4/BP7** - Updated SpliceAI cut off based on Walker, et al paper
- **PS4** - Changed requirement that only 3 hemizygotes could be present in gnomAD in order to apply code. This was changed as a result of the increased number of individuals in gnomAD v4.1. Now using a ratio to avoid needing to update regularly in the future
- **BS2** - Fixed typo
- **PS1** - Added splicing option from Walker, et al
- **PS3** - Downgraded all assays to supporting weight

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

Apply the ClinGen Coagulation Factor Deficiency VCEP/SVI decision tree to determine use and strength of the PVS1 rule. PVS1 (RNA): assays demonstrating a variant leads to aberrant splicing profile that can be used in the PVS1 decision tree as described in Walker et al. (PMID: 36865205) that was added to the v1 CFD-VCEP PVS1 flowchart. **If using PVS1(RNA), do not apply PP3.**

#### Strength Levels

| Strength | Criteria | Default Points |
|----------|----------|----------------|
| **Very Strong** | Per Coagulation Factor Deficiency VCEP/SVI PVS1 decision tree | 8 |
| **Strong** | Per Coagulation Factor Deficiency VCEP/SVI PVS1 decision tree | 4 |
| **Moderate** | Per Coagulation Factor Deficiency VCEP/SVI PVS1 decision tree | 2 |
| **Supporting** | Per Coagulation Factor Deficiency VCEP/SVI PVS1 decision tree | 1 |

**Modification Type:** Gene-specific

---

### PS1 - Same Amino Acid Change

**Original ACMG Summary:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change. Example: Val->Leu caused by either G>C or G>T in the same codon. Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:**

| Strength | Criteria | Default Points |
|----------|----------|----------------|
| **Strong** | This evidence code can be applied when there is 1 pathogenic variant OR 2 likely pathogenic variants at the same residue based on F9 gene rule specifications from the Coagulation Factor Deficiency VCEP and where *in silico* predictors do not suggest a splicing defect. **OR** When two or more variants share the same predicted splicing effect and one comparison splicing variant reaches a pathogenic classification or 2 comparison variants reach a likely pathogenic classification using the Coagulation Factor Deficiency VCEP specifications modified from Walker, et al 2023 (PMID: 37352859). | 4 |
| **Moderate** | This evidence code can be applied when there is 1 likely pathogenic variant at the same residue based on F9 gene rule specifications from the Coagulation Factor Deficiency VCEP and where *in silico* predictors do not suggest a splicing defect. **OR** When the comparison variant shares the same predicted splicing effect and the comparison splicing variant reaches a likely pathogenic classification using the Coagulation Factor Deficiency VCEP specifications based on Walker, et al 2023 (PMID: 37352859). | 2 |

**Modification Type:** General recommendation

---

### PS2 - De Novo

**Original ACMG Summary:** De novo (both maternity and paternity confirmed) in a patient with the disease and no family history. Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.

**VCEP Specifications:**

Use ClinGen's de novo modified point system for a **highly specific phenotype** (see guidance below). Combine all assumed and confirmed de novo cases for this code and use at the appropriate strength based on amount of points for all probands. **Probands must meet the PS4 phenotype criteria to apply this code.**

#### PS2/PM6 Point System

| Phenotypic Consistency | Confirmed Parental Relationships | Unconfirmed |
|------------------------|----------------------------------|-------------|
| **Phenotype highly specific for gene** (use for hemophilia A and B) | 2 points | 1 point |
| Phenotype consistent but not highly specific | 1 point | 0.5 points |
| Phenotype consistent + high genetic heterogeneity | 0.5 points | 0.25 points |
| Phenotype not consistent | 0 points | 0 points |

#### Evidence Strength Thresholds

| Points | Strength Level | Default Points |
|--------|----------------|----------------|
| ≥4 | PS2_Very Strong | 8 |
| 2-3.5 | PS2_Strong | 4 |
| 1-1.5 | PS2_Moderate | 2 |
| 0.5 | PS2_Supporting | 1 |

**Modification Type:** Disease-specific

---

### PS3 - Functional Studies

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product. Note: Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.

**VCEP Specifications:** See functional study spreadsheet.

| Strength | Criteria | Default Points |
|----------|----------|----------------|
| **Supporting** | Abnormal factor IX activity level (<40 IU/dL or 40%) in a cell line and/or mouse model. **--OR--** Abnormal factor IX activity level (<40 IU/dL or 40%) studied in an animal model setting other than mouse (i.e. – bovine factor IX activity levels compared to factor X levels). **--OR--** Absent or significantly reduced factor IX antigen level compared to wildtype using conformation-specific reporter assay in cell lines. | 1 |

**Note:** All assays have been downgraded to supporting weight in v2.0.0.

**Modification Type:** Disease-specific

#### Approved Functional Assays

##### ELISA Assay (Gao et al., 2020)
| Attribute | Details |
|-----------|---------|
| **PMID** | 32766856 |
| **DOI** | 10.1182/bloodadvances.2020002520 |
| **Assay Description** | Cell-based reporter assay that measures secreted conformation-specific reporter levels and secreted total reporter levels, which corresponds to the FIX protein levels in patients. Protein levels evaluated by ELISA. |
| **Material Used** | HEK293T cells |
| **Readout Type** | Quantitative (0-100%) |
| **Readout Description** | FIX-PC quantified by ELISA |
| **Biological Replicates** | Met; triplicates |
| **Technical Replicates** | Not met |
| **Positive Control** | Met; WT |
| **Negative Control** | Not met |
| **Validation Controls (P/LP)** | 28 variants - to evaluate pathogenicity |
| **Threshold for Normal** | Similar to WT (results presented as % of WT) |
| **Threshold for Abnormal** | Lesser than WT |
| **Approved Assay** | Yes |
| **Proposed Strength** | Supporting |

---

### PS4 - Prevalence in Affected

**Original ACMG Summary:** The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls. Note 1: Relative risk (RR) or odds ratio (OR), as obtained from case-control studies, is >5.0 and the confidence interval around the estimate of RR or OR does not include 1.0. Note 2: In instances of very rare variants where case-control studies may not reach statistical significance, the prior observation of the variant in multiple unrelated patients with the same phenotype, and its absence in controls, may be used as moderate level of evidence.

**VCEP Specifications:**

**Hemophilia B phenotype requirements:**
- Abnormal factor IX activity levels in the severe, moderate or mild range (< 40% factor IX activity level) are sufficient to confer a diagnosis
- It is reasonable to expect that genomic data from individuals with hemophilia B could be used in population databases. Therefore, we decided to implement use of a ratio of hemizygotes found to harbor a variant of interest by the total number of alleles in XY individuals in that population database (# of hemizygotes with variant of interest/total # of alleles from XY individuals sequenced in the database) as a criteria for using the PS4 code
- **The PS4 code is only applicable to variants with a ratio lower than or equal to 1.26 x 10^-5**. This ratio was set by using the most frequently seen pathogenic variant, F9 c.316G>A, p.Gly106Ser, in gnomAD that was studied in the Coagulation Factor Deficiency VCEP pilot F9 study.

| Strength | Criteria | Default Points |
|----------|----------|----------------|
| **Very Strong** | ≥8 probands meet criteria described above | 8 |
| **Strong** | 4-7 probands meet criteria described above | 4 |
| **Moderate** | 2-3 probands meet criteria described above | 2 |
| **Supporting** | 1 proband meets criteria described above | 1 |

**Modification Type:** Disease-specific

---

### PM1 - Mutational Hot Spot

**Original ACMG Summary:** Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.

**VCEP Specifications:**

**The combined weight of codes PM1 and PM5 applied for a single variant can only equal strong.**

| Strength | Criteria | Default Points |
|----------|----------|----------------|
| **Strong** | This code can be used for variants affecting any of the **3 catalytic residues (H267, D315 or S411)** and **2 activation residues (R191-A192 and R226-V227)** in the F9 gene (PMID: 12554099). | 4 |
| **Moderate** | This code should be applied when the variant is within **exons 3, 4 or 5**. | 2 |

**Modification Type:** Gene-specific

---

### PM2 - Absent from Controls

**Original ACMG Summary:** Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium. Caveat: Population data for indels may be poorly called by next generation sequencing.

**VCEP Specifications:** None

| Strength | Criteria | Default Points |
|----------|----------|----------------|
| **Supporting** | Variant must be absent in males in population databases, such as gnomAD. | 1 |

**Modification Type:** Disease-specific

---

### PM3 - In Trans with Pathogenic

**Original ACMG Summary:** For recessive disorders, detected in trans with a pathogenic variant. Note: This requires testing of parents (or offspring) to determine phase.

**VCEP Specifications:** *Not Applicable*

**Comments:** Not applicable for the F9 gene (X-linked inheritance).

---

### PM4 - Protein Length Changes

**Original ACMG Summary:** Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

**VCEP Specifications:** Use code with no specification.

| Strength | Criteria | Default Points |
|----------|----------|----------------|
| **Moderate** | Use code with no specification. | 2 |

**Modification Type:** None

---

### PM5 - Novel Missense at Same Residue

**Original ACMG Summary:** Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before. Example: Arg156His is pathogenic; now you observe Arg156Cys. Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:**

**The combined weight of codes PM1 and PM5 applied for a single variant can only equal strong.**

| Strength | Criteria | Default Points |
|----------|----------|----------------|
| **Moderate** | This evidence code can be applied when there is 1 pathogenic variant or 2 likely pathogenic variants at the same residue based on F9 rule specification from the Coagulation Factor Deficiency VCEP and where *in silico* predictors do not suggest a splicing defect. | 2 |
| **Supporting** | This evidence code can be applied when there is 1 likely pathogenic variant at the same residue based on F9 rule specifications Coagulation Factor Deficiency VCEP and where *in silico* predictors do not suggest a splicing defect. A "highly suspicious" VUS is defined as a variant that is 1 supporting code away from reaching a likely pathogenic classification. | 1 |

**Modification Type:** Gene-specific

---

### PM6 - De Novo (Assumed)

**Original ACMG Summary:** Assumed de novo, but without confirmation of paternity and maternity.

**VCEP Specifications:** *Not Applicable*

**Comments:** This rule code is combined with PS2. Please combine assumed de novo cases with confirmed de novo cases and apply PS2 at the appropriate weight.

---

### PP1 - Co-segregation

**Original ACMG Summary:** Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease. Note: May be used as stronger evidence with increasing segregation data.

**VCEP Specifications:**

Base strength of rule code on number of meioses across one or more families.

| Strength | Criteria | Default Points |
|----------|----------|----------------|
| **Strong** | This code is applicable when there are ≥4 meioses across ≥2 families. | 4 |
| **Moderate** | This code is applicable when there are at least 3 meioses across one or more families. | 2 |
| **Supporting** | This code is applicable when there are 2 meioses in one family **OR** 1 meiosis between 2 affected siblings. | 1 |

**Modification Type:** Disease-specific

---

### PP2 - Missense in Constrained Gene

**Original ACMG Summary:** Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.

**VCEP Specifications:** *Not Applicable*

**Comments:** Not applicable for F9.

---

### PP3 - Computational Evidence

**Original ACMG Summary:** Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.). Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.

**VCEP Specifications:**

**Do not apply PP3 for variants that meet criteria for a PVS1_RNA rule code.**

| Strength | Criteria | Default Points |
|----------|----------|----------------|
| **Supporting** | Code can be applied for variants where the **REVEL score is ≥0.6** OR a **SpliceAI score ≥0.2**. | 1 |

**Modification Type:** Gene-specific

---

### PP4 - Phenotype Specificity

**Original ACMG Summary:** Patient's phenotype or family history is highly specific for a disease with a single genetic etiology.

**VCEP Specifications:**

**Hemophilia B phenotype requirements:**
- Abnormal factor IX activity levels in the severe, moderate or mild range (< 40% factor IX activity level) are sufficient to confer a diagnosis
- A proband must have had full gene sequencing and deletion/duplication analysis to apply this code
- **A proband used for this code cannot be applied towards the PS4 count**

| Strength | Criteria | Default Points |
|----------|----------|----------------|
| **Moderate** | Proband must meet hemophilia B phenotype criteria AND have full gene sequencing and deletion/duplication analysis. | 2 |

**Modification Type:** Disease-specific

---

### PP5 - Reputable Source

**Original ACMG Summary:** Reputable source recently reports variant as pathogenic, but the evidence is not available to the laboratory to perform an independent evaluation.

**VCEP Specifications:** *Not Applicable*

This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PMID: 29543229).

---

## Benign Criteria

### BA1 - Allele Frequency Stand Alone

**Original ACMG Summary:** Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

**VCEP Specifications:**

99.99% CI; subpopulation must have a minimum of five variant alleles present. Males and females are included for this code.

| Strength | Criteria | Default Points |
|----------|----------|----------------|
| **Stand Alone** | MAF cutoff of ≥0.0000556 (or 0.00556%). | Not Applicable |

**Modification Type:** Gene-specific

---

### BS1 - Frequency Greater Than Expected

**Original ACMG Summary:** Allele frequency is greater than expected for disorder.

**VCEP Specifications:**

99.99% CI; subpopulation must have a minimum of five variant alleles present. Males and females are included for this code.

| Strength | Criteria | Default Points |
|----------|----------|----------------|
| **Strong** | MAF cutoff of ≥0.00000556 (or 0.000556%). | -4 |

**Modification Type:** Gene-specific

---

### BS2 - Observed in Healthy Adult

**Original ACMG Summary:** Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

**VCEP Specifications:** None

| Strength | Criteria | Default Points |
|----------|----------|----------------|
| **Strong** | This evidence code can be used when a F9 variant is observed in a male with a normal factor IX activity level (at least >40% IU or as defined by laboratory cut off). | -4 |

**Modification Type:** Disease-specific

---

### BS3 - Functional Studies (No Effect)

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

**VCEP Specifications:** None

| Strength | Criteria | Default Points |
|----------|----------|----------------|
| **Strong** | This code can be used for F9 gene variants studied in a cell line or mouse model setting that confer a normal factor IX activity **AND** normal factor IX antigen levels **OR** normal Western Blot. | -4 |

**Modification Type:** Disease-specific

---

### BS4 - Lack of Segregation

**Original ACMG Summary:** Lack of segregation in affected members of a family. Caveat: The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.

**VCEP Specifications:** None

| Strength | Criteria | Default Points |
|----------|----------|----------------|
| **Strong** | This evidence code can be used when a F9 variant is observed in a male with a family history of hemophilia B and has a normal factor IX activity level. | -4 |

**Modification Type:** Disease-specific

---

### BP1-BP7 - Benign Supporting

| Criterion | Status | Strength | Comment | Default Points |
|-----------|--------|----------|---------|----------------|
| **BP1** | Not Applicable | - | Not applicable for F9 gene. | - |
| **BP2** | Not Applicable | - | Not being used at this time. There are reports of males with hemophilia having two suspicious pathogenic variants. | - |
| **BP3** | Not Applicable | - | Not applicable for F9 gene. | - |
| **BP4** | Applicable | Supporting | This code can be applied for variants reaching a **REVEL score ≤0.3 AND a SpliceAI score ≤0.1**. | -1 |
| **BP5** | Not Applicable | - | This rule code is not recommended for use at this time. There is no known alternate cause of isolated factor IX deficiency. | - |
| **BP6** | Not Applicable | - | This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PMID: 29543229). | - |
| **BP7** | Applicable | Strong/Supporting | See below | -4/-1 |

#### BP7 Specifications

| Strength | Criteria | Default Points |
|----------|----------|----------------|
| **Strong** | Applicable for variants that have no observable splicing impact with RNA sequencing and/or minigene assay AND a SpliceAI score ≤0.1. | -4 |
| **Supporting** | Splicing prediction score ≤0.1 is required. Conservation should be assessed using PhyloP (cutoff <0.1) and PhastCons (cutoff <0.5). | -1 |

**Note:** This code can also be used for non-canonical intronic variants. The use of BP7 with BP4 is allowed, as appropriate, to classify variants meeting both criteria as likely benign.

**Modification Type:** Gene-specific / General recommendation

---

## Point-Based Classification System

### Evidence Point Values

| Evidence Category | Point Value |
|-------------------|-------------|
| Very Strong Pathogenic | 8 |
| Strong Pathogenic | 4 |
| Moderate Pathogenic | 2 |
| Supporting Pathogenic | 1 |
| Supporting Benign | -1 |
| Strong Benign | -4 |
| Stand Alone Benign | N/A (automatic Benign) |

### Classification Thresholds

| Category | Point Range |
|----------|-------------|
| **Pathogenic** | ≥10 |
| **Likely Pathogenic** | 6 - 9 |
| **Uncertain Significance** | 0 - 5 |
| **Likely Benign** | -6 to -1 |
| **Benign** | ≤-7 |

---

## Rules for Combining Criteria

### Combining Pathogenic and Benign Codes

For F9 variants where criteria codes for benign and pathogenic evidence apply, these variants are **not** subjected to an automatic variant of uncertain significance (VUS) classification. Instead, the VCEP recommends application of the rule combination point system described by Tavtigian, et al. 2020 (PMID: 32720330).

1. Use the point values table above to determine how many points each evidence code is worth
2. Sum those point values (pathogenic codes add positive points, benign codes add negative points)
3. Use the classification thresholds to determine the final variant classification

### Standard ACMG/AMP Pathogenic Classification

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

### Standard ACMG/AMP Likely Pathogenic Classification

| Criteria Combination |
|---------------------|
| 1 Very Strong **AND** 1 Moderate |
| 1 Strong **AND** 1 Moderate |
| 1 Strong **AND** ≥2 Supporting |
| ≥3 Moderate |
| 2 Moderate **AND** ≥2 Supporting |
| 1 Moderate **AND** ≥4 Supporting |
| 1 Strong **AND** 2 Moderate |

### Standard ACMG/AMP Benign Classification

| Criteria Combination |
|---------------------|
| ≥2 Strong |
| 1 Stand Alone (BA1) |

### Standard ACMG/AMP Likely Benign Classification

| Criteria Combination |
|---------------------|
| 1 Strong **AND** 1 Supporting |
| ≥2 Supporting |

---

## Appendices

### Appendix A: PVS1 Decision Tree for F9

#### Nonsense or Frameshift Variants

| Variant Type | NMD Predicted | Strength |
|--------------|---------------|----------|
| Nonsense up to c.788 | Yes | PVS1 |
| Frameshift -1/+2 up to c.730 | Yes | PVS1 |
| Frameshift +1/-2 up to c.773 | Yes | PVS1 |
| Nonsense from c.789 | No | PVS1_Moderate (if truncated region <10% of protein) |
| Frameshift -1/+2 from c.731 | No | PVS1_Moderate (if truncated region <10% of protein) |
| Frameshift +1/-2 from c.774 | No | PVS1_Moderate (if truncated region <10% of protein) |

#### Canonical Splice Site Variants (GT-AG, +/-1,2)

| Scenario | Strength |
|----------|----------|
| Exon skipping or cryptic splice disrupts reading frame AND predicted NMD (Exons 2, 3, 6) | PVS1 |
| Exon skipping or cryptic splice preserves reading frame (Exons 1, 4, 5) | PVS1_Moderate (if truncated region <10% of protein) |
| Exon skipping or cryptic splice disrupts reading frame AND NOT predicted NMD (Exon 7) | PVS1_Moderate |

#### Deletions (Single Exon to Full Gene)

| Scenario | Strength |
|----------|----------|
| Single to multi exon deletion - Disrupts reading frame AND NMD predicted | PVS1 |
| Single to multi exon deletion - Disrupts reading frame AND NOT NMD predicted, variant removes >10% of protein | PVS1_Moderate |
| Single to multi exon deletion - Disrupts reading frame AND NOT NMD predicted, variant removes <10% of protein, region critical to function (exons 4, 5) | PVS1_Strong |
| Single to multi exon deletion - Preserves reading frame, truncated region critical to protein function (exons 3, 4, 5) | PVS1 |
| Single to multi exon deletion - Preserves reading frame, role of region unknown | PVS1_Strong |
| Full gene deletion | PVS1 |

#### Duplications (≥1 exon, completely contained within gene)

| Scenario | Strength |
|----------|----------|
| Proven in tandem - Reading frame disrupted and NMD predicted | PVS1 |
| Proven in tandem - No or unknown impact on reading frame and NMD | N/A |
| Presumed in tandem - Reading frame presumed disrupted and NMD predicted | PVS1_Strong |
| Proven not in tandem | N/A |

#### Initiation Codon Variants

| Scenario | Strength |
|----------|----------|
| No known alternative start codon in other transcripts AND no pathogenic variant(s) upstream of closest potential in-frame start codon | PVS1_Supporting |

**Note:** When PVS1 is applied using RNA splicing data, PP3 cannot be applied.

---

### Appendix B: Reference PMIDs

| PMID | Description |
|------|-------------|
| 29543229 | ClinGen SVI recommendations for PP5/BP6 |
| 32720330 | Tavtigian et al. 2020 - Point-based classification system |
| 36865205 | Walker et al. - RNA recommendations for PVS1 |
| 37352859 | Walker et al. 2023 - Splicing variant classification |
| 32766856 | Gao et al. 2020 - ELISA functional assay |
| 12554099 | F9 catalytic and activation residues reference |

---

### Appendix C: Population Frequency Thresholds Summary

| Criterion | Threshold | Strength |
|-----------|-----------|----------|
| **BA1** | ≥0.0000556 (0.00556%) | Stand Alone |
| **BS1** | ≥0.00000556 (0.000556%) | Strong |
| **PM2** | Absent in males | Supporting |
| **PS4** | Ratio ≤1.26 x 10^-5 (hemizygotes/total XY alleles) | Variable |

**Note:** 99.99% CI; subpopulation must have a minimum of five variant alleles present. Males and females are included for BA1 and BS1.

---

### Appendix D: Computational Prediction Thresholds

| Criterion | Tool | Pathogenic Threshold | Benign Threshold |
|-----------|------|---------------------|------------------|
| **PP3** | REVEL | ≥0.6 | - |
| **PP3** | SpliceAI | ≥0.2 | - |
| **BP4** | REVEL | - | ≤0.3 |
| **BP4** | SpliceAI | - | ≤0.1 |
| **BP7** | SpliceAI | - | ≤0.1 |
| **BP7** | PhyloP | - | <0.1 |
| **BP7** | PhastCons | - | <0.5 |

**Note:** For BP4, BOTH REVEL ≤0.3 AND SpliceAI ≤0.1 are required.

---

### Appendix E: Critical Functional Residues in F9

| Residue Type | Residues | PM1 Strength |
|--------------|----------|--------------|
| **Catalytic Residues** | H267, D315, S411 | Strong |
| **Activation Residues** | R191-A192, R226-V227 | Strong |
| **Exon Location** | Exons 3, 4, 5 | Moderate |

---

### Appendix F: Criteria Not Applicable for F9

| Criterion | Reason |
|-----------|--------|
| **PM3** | Not applicable for X-linked inheritance |
| **PM6** | Combined with PS2 - use combined de novo counting |
| **PP2** | Not applicable for F9 |
| **PP5** | Not recommended by ClinGen SVI |
| **BP1** | Not applicable for F9 |
| **BP2** | Reports of males with hemophilia having two suspicious pathogenic variants |
| **BP3** | Not applicable for F9 |
| **BP5** | No known alternate cause of isolated factor IX deficiency |
| **BP6** | Not recommended by ClinGen SVI |

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 2.0.0 | January 20, 2026 | Post SVI review edits: Updated PVS1 RNA recommendations, PP3/BP4/BP7 SpliceAI cutoffs, PS4 gnomAD criteria, BS2 typo fix, PS1 splicing option, PS3 assays downgraded to supporting |
| 1.0.0 | Initial release | Initial VCEP specifications |

---

*This document was compiled from ClinGen Coagulation Factor Deficiency VCEP specifications and ClinGen SVI recommendations. For the most current version, please refer to the ClinGen website.*
