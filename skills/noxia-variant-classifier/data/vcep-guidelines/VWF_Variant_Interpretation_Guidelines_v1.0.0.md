# ClinGen von Willebrand Disease Expert Panel Variant Interpretation Guidelines for VWF (Type 2)

**Version:** 1.0.0
**Released:** 7/9/2024
**Affiliation:** von Willebrand Disease VCEP
**Based on:** Richards et al., 2015 ACMG/AMP Guidelines

---

## Gene Information

| Attribute | Value |
|-----------|-------|
| **Gene** | VWF (HGNC:12726) |
| **HGNC Name** | von Willebrand factor |
| **Transcript** | NM_000552.5 |
| **Diseases** | von Willebrand disease type 2A (MONDO:0015628) — AD |
| | von Willebrand disease type 2B (MONDO:0015629) — AD |
| | von Willebrand disease type 2M (MONDO:0015630) — AD |
| | von Willebrand disease 2 (MONDO:0013304) — Undetermined |
| | von Willebrand disease (hereditary or acquired) (MONDO:0024574) — Other |
| **Inheritance** | Autosomal dominant (2A, 2B, 2M); Autosomal recessive (2N) |

> **General Comments:** Applying VWD type 2 variant curation guidance is complex. If you are unsure how to apply these rule specifications after reading guidance materials provided below, it may be best not to use these guidelines. Alternatively, you are welcome to submit variants for the ClinGen VWD VCEP to curate for you.

---

## Important: Rule Set Applicability

This rule set applies **only** to VWF variants associated with a **type 2 clinical diagnosis of VWD** and/or variants with no known association with disease. Key considerations:

- If the variant has **not** been previously associated with VWD type 2, or the proband does not clearly have a VWD type 2 phenotype, **do not use this rule set**
- VWD type 2 phenotyping is complex — if the specific type 2 diagnosis (2A, 2B, 2M, or 2N) is unclear, this rule set is **not recommended**
- Types 2A, 2B, and 2M are generally **autosomal dominant** and share a rule set; Type 2N is **autosomal recessive** with a separate rule set
- Some variants associate with more than one VWD type — curate separately for each phenotype with its respective probands
- A general VWD rule set (agnostic of type) is planned for future development
- Rule specifications for VWD types 1 and 3 are also under development

### Rule Set Selection Flow

1. Has the variant been previously associated with a specific VWD type 2 subtype (2A, 2B, 2M, or 2N)?
   - **Yes** → Use the appropriate type-specific rules
   - **No** → Does the proband have sufficient laboratory results for PP4?
     - **Yes** → Determine the subtype from laboratory data, then use appropriate rules
     - **No** → Do not use these rule specifications

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
   - [BA1 - Allele Frequency >5%](#ba1---allele-frequency-5)
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

**VCEP Specification: Not Applicable**

> **Comments:** VWD type 2 is defined by qualitative defects in the VWF protein and not caused by null variants.

---

### PS1 - Same Amino Acid Change

**Original ACMG Summary:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change. Example: Val->Leu caused by either G>C or G>T in the same codon. Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:**

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Strong** | Use with no specification except comparison variant must be classified as pathogenic using rules from the VWD VCEP. | Gene-specific |
| **Moderate** | Use with no specification except comparison variant must be classified as likely pathogenic using rules from the VWD VCEP. | Gene-specific |

---

### PS2 - De Novo (Confirmed)

**Original ACMG Summary:** De novo (both maternity and paternity confirmed) in a patient with the disease and no family history. Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.

**VCEP Specifications:** Use the ClinGen SVI point-based recommendations for de novo evidence. Phenotype consistency is determined by PP4 criteria:

- Use **"Phenotype consistent with gene but not highly specific"** if the proband meets **PP4 criteria**
- Use **"Phenotype highly specific for gene"** if the proband meets **PP4_Moderate criteria**

See Table 1 attached (PS2/PM6 guidance document).

| Strength | Points Required | Modification Type |
|----------|-----------------|-------------------|
| **Very Strong** | 4 points | Disease-specific |
| **Strong** | 2 points | Disease-specific |
| **Moderate** | 1 point | Disease-specific |
| **Supporting** | 0.5 points | Disease-specific |

#### PS2/PM6 Point System

| Phenotypic Consistency | Confirmed De Novo (PS2) | Assumed De Novo (PM6) |
|------------------------|------------------------|-----------------------|
| **Phenotype highly specific for gene** (meets PP4_Moderate) | 2 points | 1 point |
| **Phenotype consistent with gene but not highly specific** (meets PP4) | 1 point | 0.5 points |
| Phenotype consistent but with high genetic heterogeneity | 0.5 points | 0.25 points |
| Phenotype not consistent | 0 points | 0 points |

#### Evidence Strength Thresholds

| Total Points | Strength Level |
|--------------|----------------|
| 0.5 | Supporting |
| 1.0 | Moderate |
| 2.0 | Strong |
| 4.0 | Very Strong |

---

### PS3 - Functional Studies

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product. Note: Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.

**VCEP Specifications:**

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Strong** | Either: (1) In a transgenic animal model, must demonstrate minimal to no function. **OR** (2) The following types of assays using recombinant VWF are approved for each subtype (see details below). | Disease-specific |
| **Supporting** | Subtype-specific assays as described below. | Disease-specific |

#### PS3_Strong — Subtype-Specific Assay Requirements

**Subtype 2A:**
A multimerization assay in which the variant is expressed in a recombinant system (either independently or coexpressed with WT) resulting in abnormal multimers, with a reported loss of HMWM, **AND** to confirm this is consistent with the variant's mechanism of disease, there must be a patient harboring the variant with a clinical assay also showing loss of HMWMs. This evidence must be published in a peer reviewed journal and a picture of the gel must be visible for evaluation.

**Subtype 2B:**
A GP1b or platelet binding assay indicating gain of function by increased binding at low doses of ristocetin.

**Subtype 2M:**
Either (1) a GP1b or platelet binding assay **OR** (2) a collagen binding assay, indicating loss of function by decreased binding.

> **Note:** See attached spreadsheet for examples of approved assay instances. There are no universal thresholds for these assays; however, the relevant results should be described as clinically significant if assays were performed in a clinical laboratory or statistically significant if pertaining to research findings.

#### PS3_Supporting — Subtype-Specific Assay Requirements

**Subtype 2A:**
Either (1) a multimerization assay in which the variant is expressed in a recombinant system (either independently or coexpressed with WT) resulting in abnormal multimers, with a reported loss of HMWM (must be published in a peer reviewed journal and a picture of the gel must be visible for evaluation), **OR** (2) an ADAMTS susceptibility assay indicating increased susceptibility relative to WT.

#### Approved Assay Instances

##### 2A Multimerization Assays (PS3_Supporting or PS3_Strong)

| PMID | Author | Year | Approved | Strength |
|------|--------|------|----------|----------|
| 11264172 | Schneppenheim | 2001 | Yes | Supporting/Strong |
| 11264172 | Schneppenheim | 2001 | Yes | Supporting/Strong |
| 16322474 | Hassenpflug | 2006 | Yes | Supporting/Strong |
| 19422453 | Baronciani | 2009 | Yes | Supporting/Strong |
| 22431572 | Jacobi | 2012 | Yes | Supporting/Strong |
| 22905953 | Wang | 2012 | Yes | Supporting/Strong |
| 23539537 | Yadegari | 2013 | Yes | Supporting/Strong |

##### 2A ADAMTS13 Susceptibility Assays (PS3_Supporting)

| PMID | Author | Year | Approved | Strength |
|------|--------|------|----------|----------|
| 16322474 | Hassenpflug | 2006 | Yes | Supporting |
| 22781599 | Zhang | 2012 | Yes | Supporting |
| 22431572 | Jacobi | 2012 | Yes | Supporting |
| 23110044 | Interlandi | 2012 | Yes | Supporting |
| 28076816 | Aponte-Santamaria | 2017 | Yes | Supporting |
| 29186156 | Lynch | 2017 | Yes | Supporting |

##### 2B Binding Gain-of-Function Assays (PS3_Strong)

| PMID | Author | Year | Approved | Strength |
|------|--------|------|----------|----------|
| 2011604 | Ware | 1991 | Yes | Strong |
| 1557393 | Cooney | 1992 | Yes | Strong |
| 1373334 | Kroner | 1992 | Yes | Strong |
| 1400429, 8165601, 8376405 | Randi | 1992 | Yes | Strong |
| 1429668, 8298143, 8204881 | Ribba | 1992 | Yes | Strong |
| 8123843, 9858249, 8547152 | Hilbert | 1994 | Yes | Strong |
| 8630394, 1557393 | Cooney | 1996 | Yes | Strong |
| 10845912 | Ajzenberg | 2000 | Yes | Strong |
| 16246252, 17155947 | Baronciani | 2005 | Yes | Strong |
| 26345337 | Ma | 2015 | Yes | Strong |
| 30488424, 23179108 | Ahmad | 2019 | Yes | Strong |

##### 2M Binding Loss-of-Function Assays (PS3_Strong)

| PMID | Author | Year | Approved | Strength |
|------|--------|------|----------|----------|
| 10845912 | Ajzenberg | 2000 | Yes | Strong |
| 26345337 | Ma | 2015 | Yes | Strong |
| 29341351 | Bowman | 2018 | Yes | Strong |

---

### PS4 - Prevalence in Affected

**Original ACMG Summary:** The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls. Note 1: Relative risk (RR) or odds ratio (OR), as obtained from case-control studies, is >5.0 and the confidence interval around the estimate of RR or OR does not include 1.0. Note 2: In instances of very rare variants where case-control studies may not reach statistical significance, the prior observation of the variant in multiple unrelated patients with the same phenotype, and its absence in controls, may be used as moderate level of evidence.

**VCEP Specifications:** Do not apply this code for variants that meet BS1 or BA1 criteria. Do not count proband used for PP4 in this code's proband count.

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Very Strong** | Appropriate to use code when there are 8 or more probands that meet the laboratory phenotype of the PP4 definition for a specific VWD type 2 phenotype (i.e. all probands must qualify for a clinical diagnosis of the same VWD type 2 phenotype based on laboratory criteria stated under PP4). | Disease-specific |
| **Strong** | Appropriate to use code when there are 4-7 probands that meet the laboratory phenotype of the PP4 definition for a specific VWD type 2 phenotype (i.e. all probands must qualify for a clinical diagnosis of the same VWD type 2 phenotype based on laboratory criteria stated under PP4). | Disease-specific |
| **Moderate** | Appropriate to use code when there are 2-3 probands that meet the laboratory phenotype of the PP4 definition for a specific VWD type 2 phenotype (i.e. all probands must qualify for a clinical diagnosis of the same VWD type 2 phenotype based on laboratory criteria stated under PP4). | Disease-specific |
| **Supporting** | Appropriate to use code when there is 1 proband that meets the laboratory phenotype of the PP4 definition for a specific VWD type 2 phenotype. | Disease-specific |

#### PS4 Proband Count Summary

| Proband Count | Strength Level |
|---------------|----------------|
| 1 | Supporting |
| 2-3 | Moderate |
| 4-7 | Strong |
| ≥8 | Very Strong |

---

### PM1 - Mutational Hot Spot

**Original ACMG Summary:** Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.

**VCEP Specification: Not Applicable**

> **Comments:** Rule does not apply due to benign variation being present throughout the gene.

---

### PM2 - Absent from Controls

**Original ACMG Summary:** Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium. Caveat: Population data for indels may be poorly called by next generation sequencing.

**VCEP Specification (Supporting only):**
- gnomAD popmax MAF **<0.0001**

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Supporting** | Use code for variants with a popmax MAF of <0.0001 in gnomAD. | Disease-specific, Gene-specific |

---

### PM3 - In Trans with Pathogenic

**Original ACMG Summary:** For recessive disorders, detected in trans with a pathogenic variant. Note: This requires testing of parents (or offspring) to determine phase.

**VCEP Specification: Not Applicable**

> **Comments:** These are dominant conditions, so this rule code does not apply.

---

### PM4 - Protein Length Changes

**Original ACMG Summary:** Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

**VCEP Specifications:**

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Moderate** | Use with no specification for type 2A and 2M. This rule code is not applicable to variants associated with type 2B disease, since type 2B is only associated with gain of function variants. | Gene-specific |

---

### PM5 - Novel Missense at Same Residue

**Original ACMG Summary:** Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before. Example: Arg156His is pathogenic; now you observe Arg156Cys. Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:**

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Moderate** | Use code when previously reported variant reaches a pathogenic classification using the VWD Type 2 rule specifications. Previously reported variant can be associated with a different type of VWD. | General recommendation |
| **Supporting** | Use code when previously reported variant reaches a likely pathogenic classification using the VWD Type 2 rule specifications. Previously reported variant can be associated with a different type of VWD. | General recommendation |

> **Note:** Code may also be applied when two previously reported variants reach a likely pathogenic classification using the VWD Type 2 rule specifications. Previously reported variants can be associated with a different type of VWD.

---

### PM6 - De Novo (Assumed)

**Original ACMG Summary:** Assumed de novo, but without confirmation of paternity and maternity.

**VCEP Specification: Not Applicable**

> **Comments:** Use the PS2 code in lieu of using this code for de novo variants. The PS2 point-based system incorporates both confirmed and assumed de novo evidence (see [PS2 section](#ps2---de-novo-confirmed)).

---

### PP1 - Co-segregation

**Original ACMG Summary:** Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease. Note: May be used as stronger evidence with increasing segregation data.

**VCEP Specifications:**

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Moderate** | Appropriate to use when there are multiple families each reported to have two or more meioses. | Disease-specific |
| **Supporting** | Appropriate to use when there are 2 or more meioses within a single family. | Disease-specific |

---

### PP2 - Missense in Constrained Gene

**Original ACMG Summary:** Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.

**VCEP Specification: Not Applicable**

> **Comments:** Not applicable due to presence of benign variation throughout the VWF gene.

---

### PP3 - Computational Evidence

**Original ACMG Summary:** Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.). Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.

**VCEP Specifications:**

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Supporting** | Appropriate to use for missense variants that have a REVEL score of greater or equal to 0.644 **OR** a SpliceAI score suggestive of a splicing defect (greater or equal to 0.5). | Gene-specific |

---

### PP4 - Phenotype Specificity

**Original ACMG Summary:** Patient's phenotype or family history is highly specific for a disease with a single genetic etiology.

**VCEP Specifications:** The PP4 code cannot be applied for variants that meet BA1 criteria.

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Moderate** | The patient must have a clinical phenotype of excessive mucocutaneous bleeding and required laboratory values to use the PP4 rule code at the moderate strength. See Table 2A for required and consistent laboratory values. | Disease-specific |
| **Supporting** | The patient must have a clinical phenotype of excessive mucocutaneous bleeding and required laboratory values to use the PP4 rule code at the supporting strength. See Table 2B for required and consistent laboratory values. | Disease-specific |

#### Table 2A: PP4_Moderate — Required and Consistent Laboratory Values

| | Type 2A | Type 2B | Type 2M |
|---|---------|---------|---------|
| **Required** | Proband must have VWF activity < antigen **AND** loss of high molecular weight multimers **AND** decreased VWF:GP1b binding, **OR** decreased VWF:RCo assay, **OR** decreased collagen binding assay | Proband must have an assay showing VWF GOF in a GP1b assay, such as a RIPA, VWF platelet binding assay, an ELISA or another equivalent test. Loss of high molecular weight multimers and/or decreased platelet count (may occur only under physiologic stress or with pregnancy) | Proband must have a VWF activity < antigen **AND** no loss of high molecular weight multimers **AND** decreased platelet/GPIb binding assay, **OR** decreased collagen binding assay |
| **Consistent** | Factor VIII activity level should be in line with VWF antigen or higher (>0.7). Normal RIPA study | Proband has VWF activity < antigen. Evidence against platelet-type VWD | Factor VIII activity should be in line with VWF antigen or higher (>0.7). If the activity assay uses ristocetin, negative for the VWF p.D1472H variant |

#### Table 2B: PP4_Supporting — Required and Consistent Laboratory Values

| | Type 2A | Type 2B | Type 2M |
|---|---------|---------|---------|
| **Required** | Proband must have VWF activity < antigen, **OR** loss of high molecular weight multimers, **OR** decreased VWF:GPIb1BA binding, **OR** abnormal VWF:RCo assay, **OR** decreased collagen binding assay | Proband must have an assay showing VWF GOF in a GP1B assay, such as a RIPA, VWF platelet binding assay, an ELISA or another equivalent test. | Proband must have a VWF activity < antigen (ratio 0.7) **AND** no loss of high molecular weight multimers, **OR** decreased platelet/GPIb binding assay, **OR** decreased collagen binding assay |

---

### PP5 - Reputable Source

**Original ACMG Summary:** Reputable source recently reports variant as pathogenic, but the evidence is not available to the laboratory to perform an independent evaluation.

**VCEP Specification: Not Applicable**

> This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PMID: 29543229).

---

## Benign Criteria

### BA1 - Allele Frequency >5%

**Original ACMG Summary:** Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

**VCEP Specification (Stand Alone):**
- gnomAD popmax MAF **>0.1 (10%)**

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Stand Alone** | Appropriate to use for variants with a Popmax MAF of >0.1 in gnomAD. | Disease-specific, Gene-specific |

---

### BS1 - Frequency Greater Than Expected

**Original ACMG Summary:** Allele frequency is greater than expected for disorder.

**VCEP Specification (Strong):**
- gnomAD popmax MAF **>0.01 (1%)**

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Strong** | Appropriate to use for variants with a Popmax MAF of >0.01 in gnomAD. | Disease-specific, Gene-specific |

---

### BS2 - Observed in Healthy Adult

**Original ACMG Summary:** Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

**VCEP Specification: Not Applicable**

> **Comments:** Not applicable due to the incomplete penetrance seen in VWD.

---

### BS3 - Functional Studies (No Effect)

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

**VCEP Specification: Not Applicable**

> **Comments:** There are no available assays that can clearly and dependably show no damaging protein effects.

---

### BS4 - Lack of Segregation

**Original ACMG Summary:** Lack of segregation in affected members of a family. Caveat: The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.

**VCEP Specifications:**

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Strong** | Appropriate to use when two or more relatives have the phenotype consistent with VWD type 2 without harboring the variant identified in other affected family members. Additionally, there is not another established cause of type 2 VWD (e.g. there are not multiple type 2 VWD diagnoses) segregating in the family. | Disease-specific |
| **Supporting** | Appropriate to use when only one relative has the phenotype consistent with VWD type 2 without harboring the variant identified in other affected family members. Additionally, there is not another established cause of type 2 VWD (e.g. there are not multiple type 2 VWD diagnoses) segregating in the family. | Disease-specific |

---

### BP1-BP7 - Benign Supporting

| Criterion | Status | Comment |
|-----------|--------|---------|
| **BP1** | Not Applicable | The VWF gene is not constrained for missense variation (gnomAD). |
| **BP2** | Not Applicable | Do not use due to potential of variant being associated with VWD 2N (recessive disease). |
| **BP3** | Not Applicable | There are no known repetitive regions in the VWF gene without a known function. |
| **BP4** | Supporting | Use for missense variants that have a REVEL score of less than or equal to 0.290 AND SpliceAI cutoff of <0.1. Use SpliceAI cutoff of <0.1 for other variant types. **Modification:** Gene-specific |
| **BP5** | Supporting | A second variant in VWF may be considered an alternate molecular basis for disease when that variant is LP/P (as evaluated by the VWD VCEP) and fully explains the phenotype of the patient's reported VWD subtype. **Modification:** None |
| **BP6** | Not Applicable | This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PMID: 29543229). |
| **BP7** | Supporting | Use SpliceAI for splicing predictor with a cutoff score of <0.1. **Modification:** General recommendation |

---

## Rules for Combining Criteria

### Pathogenic Classification

| Criteria Combination | Applicable Criteria |
|---------------------|---------------------|
| 1 Very Strong **AND** ≥1 Strong | (PS2_Very Strong, PS4_Very Strong) AND (PS1, PS2, PS3, PS4) |
| 1 Very Strong **AND** ≥2 Moderate | (PS2_Very Strong, PS4_Very Strong) AND (PS1_Moderate, PS2_Moderate, PS4_Moderate, PM4, PM5, PP1_Moderate, PP4_Moderate) |
| 1 Very Strong **AND** 1 Moderate **AND** 1 Supporting | (PS2_Very Strong, PS4_Very Strong) AND (PS1_Moderate, PS2_Moderate, PS4_Moderate, PM4, PM5, PP1_Moderate, PP4_Moderate) AND (PS2_Supporting, PS3_Supporting, PS4_Supporting, PM2_Supporting, PM5_Supporting, PP1, PP3, PP4) |
| 1 Very Strong **AND** ≥2 Supporting | (PS2_Very Strong, PS4_Very Strong) AND (PS2_Supporting, PS3_Supporting, PS4_Supporting, PM2_Supporting, PM5_Supporting, PP1, PP3, PP4) |
| ≥2 Strong | (PS1, PS2, PS3, PS4) |
| 1 Strong **AND** ≥3 Moderate | (PS1, PS2, PS3, PS4) AND (PS1_Moderate, PS2_Moderate, PS4_Moderate, PM4, PM5, PP1_Moderate, PP4_Moderate) |
| 1 Strong **AND** 2 Moderate **AND** ≥2 Supporting | (PS1, PS2, PS3, PS4) AND (PS1_Moderate, PS2_Moderate, PS4_Moderate, PM4, PM5, PP1_Moderate, PP4_Moderate) AND (PS2_Supporting, PS3_Supporting, PS4_Supporting, PM2_Supporting, PM5_Supporting, PP1, PP3, PP4) |
| 1 Strong **AND** 1 Moderate **AND** ≥4 Supporting | (PS1, PS2, PS3, PS4) AND (PS1_Moderate, PS2_Moderate, PS4_Moderate, PM4, PM5, PP1_Moderate, PP4_Moderate) AND (PS2_Supporting, PS3_Supporting, PS4_Supporting, PM2_Supporting, PM5_Supporting, PP1, PP3, PP4) |

### Likely Pathogenic Classification

| Criteria Combination | Applicable Criteria |
|---------------------|---------------------|
| 1 Very Strong **AND** 1 Moderate | (PS2_Very Strong, PS4_Very Strong) AND (PS1_Moderate, PS2_Moderate, PS4_Moderate, PM4, PM5, PP1_Moderate, PP4_Moderate) |
| 1 Strong **AND** 1 Moderate | (PS1, PS2, PS3, PS4) AND (PS1_Moderate, PS2_Moderate, PS4_Moderate, PM4, PM5, PP1_Moderate, PP4_Moderate) |
| 1 Strong **AND** ≥2 Supporting | (PS1, PS2, PS3, PS4) AND (PS2_Supporting, PS3_Supporting, PS4_Supporting, PM2_Supporting, PM5_Supporting, PP1, PP3, PP4) |
| ≥3 Moderate | (PS1_Moderate, PS2_Moderate, PS4_Moderate, PM4, PM5, PP1_Moderate, PP4_Moderate) |
| 2 Moderate **AND** ≥2 Supporting | (PS1_Moderate, PS2_Moderate, PS4_Moderate, PM4, PM5, PP1_Moderate, PP4_Moderate) AND (PS2_Supporting, PS3_Supporting, PS4_Supporting, PM2_Supporting, PM5_Supporting, PP1, PP3, PP4) |
| 1 Moderate **AND** ≥4 Supporting | (PS1_Moderate, PS2_Moderate, PS4_Moderate, PM4, PM5, PP1_Moderate, PP4_Moderate) AND (PS2_Supporting, PS3_Supporting, PS4_Supporting, PM2_Supporting, PM5_Supporting, PP1, PP3, PP4) |
| 1 Strong **AND** 2 Moderate | (PS1, PS2, PS3, PS4) AND (PS1_Moderate, PS2_Moderate, PS4_Moderate, PM4, PM5, PP1_Moderate, PP4_Moderate) |

### Benign Classification

| Criteria Combination | Applicable Criteria |
|---------------------|---------------------|
| ≥2 Strong | (BS1, BS4) |
| 1 Stand Alone | (BA1) |

### Likely Benign Classification

| Criteria Combination | Applicable Criteria |
|---------------------|---------------------|
| 1 Strong **AND** 1 Supporting | (BS1, BS4) AND (BS4_Supporting, BP4, BP5, BP7) |
| ≥2 Supporting | (BS4_Supporting, BP4, BP5, BP7) |

---

## Appendices

### Appendix A: VWD Type 2 Background

Von Willebrand disease (VWD) is an inherited bleeding disorder characterized by a lack of effective plasma von Willebrand factor (VWF) protein, related to quantitative or qualitative defects. Type 2 VWD results from qualitative defects and accounts for ~30% of VWD caused by pathogenic variants in the VWF gene (PMID: 30306084). Symptoms are typically mild to moderate mucocutaneous bleeding with near complete penetrance of laboratory findings.

**Subtypes:**
- **Type 2A:** Variants result in loss of high molecular weight VWF multimers, which are required for effective clot formation. Typically autosomal dominant.
- **Type 2B:** Gain of function variants that increase VWF binding to platelet GPIb-alpha, which can result in loss of HMWM, removal of the platelet-VWF complex from circulation, and can lead to thrombocytopenia. Abnormal multimers and/or thrombocytopenia may or may not be present at baseline and can be provoked or exacerbated by stressful events. Autosomal dominant. Phenotype mimics platelet-type von Willebrand disease.
- **Type 2M:** Variants decrease VWF binding to GPIb-alpha or collagen without loss of high molecular weight VWF multimers. Typically autosomal dominant.
- **Type 2N:** Variants decrease binding efficiency of VWF to factor VIII protein, decreasing circulating factor VIII levels. Phenotype mimics mild hemophilia A. Autosomal recessive.

**Molecular Defects:** Type 2 variants are predominantly missense variation. Type 2B pathogenic variants are almost always in exon 28. Most Type 2A and 2M variants are also in exon 28. Type 2N pathogenic variants are typically in exons 18-20 but have been reported in exons 17 and 24-25 (PMID: 20301765).

**Prevalence:** Type 2 VWD is estimated at ~1 in 100,000 (PMID: 33780098).

**Gene:** VWF gene is 178 kb with 52 exons, encoding a 2813 amino acid protein.

### Appendix B: PS3 Functional Assay Details

#### Assay Categories by Subtype

**Type 2A — Multimerization Assays:**
Recombinant VWF expression systems with SDS-agarose gel electrophoresis or equivalent to assess multimer pattern. Evidence of abnormal multimers with loss of HMWM. Approved for PS3_Supporting (recombinant data alone) or PS3_Strong (when combined with clinical assay confirmation from a patient).

**Type 2A — ADAMTS13 Susceptibility Assays:**
Assays measuring increased susceptibility of mutant VWF to ADAMTS13 cleavage relative to wild-type. Approved for PS3_Supporting.

**Type 2B — Binding Gain-of-Function Assays:**
GP1b or platelet binding assays demonstrating increased binding at low doses of ristocetin. Includes RIPA-based assays, ELISA with rGPIb-alpha, and platelet binding assays. Approved for PS3_Strong.

**Type 2M — Binding Loss-of-Function Assays:**
GP1b or platelet binding assays, or collagen binding assays demonstrating decreased binding. Approved for PS3_Strong.

### Appendix C: Population Frequency Thresholds Summary

| Criterion | Threshold | Database | Strength |
|-----------|-----------|----------|----------|
| BA1 | Popmax MAF >0.1 | gnomAD | Stand Alone |
| BS1 | Popmax MAF >0.01 | gnomAD | Strong |
| PM2 | Popmax MAF <0.0001 | gnomAD | Supporting |

### Appendix D: Computational Predictor Thresholds

| Predictor | Pathogenic Threshold (PP3) | Benign Threshold (BP4) |
|-----------|---------------------------|------------------------|
| REVEL | ≥0.644 | ≤0.290 |
| SpliceAI | ≥0.5 (PP3) | <0.1 (BP4) |

### Appendix E: Not Applicable Criteria Summary

The following ACMG/AMP criteria are **not applicable** for VWD Type 2 variant curation:

| Criterion | Reason |
|-----------|--------|
| PVS1 | VWD type 2 is defined by qualitative defects, not caused by null variants |
| PM1 | Benign variation present throughout the gene |
| PM3 | Types 2A/2B/2M are dominant conditions |
| PM6 | Incorporated into PS2 point-based system |
| PP2 | Benign variation present throughout the VWF gene |
| PP5 | Not recommended by ClinGen SVI (PMID: 29543229) |
| BS2 | Incomplete penetrance in VWD |
| BS3 | No assays available that can clearly show no damaging effects |
| BP1 | VWF gene not constrained for missense variation |
| BP2 | Potential for VWD 2N (recessive) association |
| BP3 | No known repetitive regions without known function in VWF |
| BP6 | Not recommended by ClinGen SVI (PMID: 29543229) |

### Appendix F: Reference PMIDs

| PMID | Description |
|------|-------------|
| 20301765 | VWD molecular defects and subtypes reference |
| 29543229 | ClinGen SVI recommendation (PP5/BP6 not for use) |
| 30306084 | VWD epidemiology and genetic testing |
| 33780098 | VWD prevalence estimates |
| 10959685 | Overall VWD prevalence |

---

## Version History

| Version | Date | Description |
|---------|------|-------------|
| 1.0.0 | 7/9/2024 | Initial release of VWD Type 2 (2A, 2B, 2M) rule specifications |

---

*This document was compiled from ClinGen VCEP specifications and ClinGen SVI recommendations. For the most current version, please refer to the ClinGen website.*
