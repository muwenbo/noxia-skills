# ClinGen von Willebrand Disease Expert Panel Variant Interpretation Guidelines for VWF (Type 2N)

**Version:** 1.0.0
**Released:** 7/9/2024
**Affiliation:** von Willebrand Disease VCEP
**Based on:** Richards et al., 2015 ACMG/AMP Guidelines
**Description:** VWD type 2N rule specifications

---

## General Comments

Applying VWD type 2 variant curation guidance is complex. If you are unsure how to apply these rule specifications after reading guidance materials provided below, it may be best not to use these guidelines. Alternatively, you are welcome to submit variants for the ClinGen VWD VCEP to curate for you.

**Important:** This rule set only applies to VWF variants associated with a type 2 VWD diagnosis or no bleeding phenotype at all. VWD type 2 is complex to diagnose. If the variant has not been previously associated with a specific type 2 diagnosis (e.g., 2A, 2B, 2M, or 2N) and the proband's type 2 diagnosis is unclear, do not use this rule set. These rule specifications are not recommended for variants that have only been associated with a clinical diagnosis of Types 1 and/or 3 VWD or no clinical diagnosis/proband.

---

## Gene Information

| Attribute | Value |
|-----------|-------|
| **Gene** | VWF (HGNC:12726) |
| **HGNC Name** | von Willebrand factor |
| **Transcript** | NM_000552.5 |
| **Disease** | von Willebrand disease type 2N (MONDO:0015631) |
| **Inheritance** | Autosomal recessive inheritance |

---

## Disease Background

Von Willebrand disease (VWD) is an inherited bleeding disorder characterized by a lack of effective plasma von Willebrand factor (VWF) protein, related to quantitative or qualitative defects. **Type 2N** variants decrease the binding efficiency of VWF to factor VIII protein, which decreases the circulating level of the factor VIII protein. As a result, the phenotype mimics that of mild hemophilia A, but is a defect of VWF inherited in an autosomal recessive fashion. Type 2N pathogenic variants are typically located in exons 18–20 but have been reported in exons 17 and 24–25 (PMID: 20301765).

The prevalence of Type 2 VWD is estimated to be ~1 in 100,000 (PMID: 33780098). The VWF gene is 178 kb with 52 exons and encodes a 2813 amino acid protein. Type 2 variants are predominantly due to missense variation.

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
   - [BP1–BP7 - Benign Supporting](#bp1bp7---benign-supporting)
3. [Rules for Combining Criteria](#rules-for-combining-criteria)
4. [Appendices](#appendices)

---

## Pathogenic Criteria

### PVS1 - Null Variant

**Original ACMG Summary:** Null variant (nonsense, frameshift, canonical ±1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.

**VCEP Specification:** *Not Applicable*

**Comments:** VWD type 2N is caused by qualitative protein defects and not null variants.

---

### PS1 - Same Amino Acid Change

**Original ACMG Summary:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | Use with no specification except comparison variant must be classified as pathogenic using rules from the VWD VCEP. |
| **Moderate** | Use with no specification except comparison variant must be classified as likely pathogenic using rules from the VWD VCEP. |

**Modification Type:** Gene-specific

---

### PS2 - De Novo (Confirmed)

**Original ACMG Summary:** De novo (both maternity and paternity confirmed) in a patient with the disease and no family history. Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.

**VCEP Specifications:** Please note that presence of a second *VWF* variant is required to use this rule code.

Use proposed SVI point recommendations with the following phenotype consistency mapping for VWD type 2N:

- Use **"Phenotype consistent with gene but not highly specific"** if the proband meets **PP4 criteria**
- Use **"Phenotype highly specific for gene"** if the proband meets **PP4_Moderate criteria**

See Table 1 (PS2/PM6 Point System) below.

**Modification Type:** Disease-specific

#### PS2/PM6 Point System (Table 1)

| Phenotypic Consistency | Confirmed De Novo (PS2 points) | Assumed De Novo (PM6 points) |
|------------------------|-------------------------------|------------------------------|
| Phenotype highly specific for gene (meets PP4_Moderate) | 2 points | 1 point |
| Phenotype consistent with gene but not highly specific (meets PP4) | 1 point | 0.5 points |
| Phenotype consistent but with high genetic heterogeneity | 0.5 points | 0.25 points |
| Phenotype not consistent | 0 points | 0 points |

#### PS2/PM6 Evidence Strength Thresholds

| Total Points | Strength Level |
|--------------|----------------|
| ≥0.5 | Supporting |
| ≥1.0 | Moderate |
| ≥2.0 | Strong |
| ≥4.0 | Very Strong |

#### PS2 Strength Levels

| Strength | Criteria |
|----------|----------|
| **Very Strong** | Use proposed SVI point recommendations for "Phenotype consistent with gene but not highly specific" if the proband meets PP4 criteria. Use "Phenotype highly specific for gene" phenotype consistency if the proband meets PP4_Moderate criteria. See Table 1. Required 4 points. |
| **Strong** | Same as above. Required 2 points. |
| **Moderate** | Same as above. Required 1 point. |
| **Supporting** | Same as above. If the proband meets PP4_Moderate criteria, use a moderate or higher evidence weight. Required 0.5 point. |

---

### PS3 - Functional Studies

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product. Note: Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | Either (1) in a transgenic animal model, must demonstrate minimal to no function, OR (2) a Factor VIII binding assay using recombinant vWF resulting in decreased binding compared to WT. See attached spreadsheet for examples of approved assay instances to use for this rule code. There are no universal thresholds for these assays; however, the relevant results should be described as clinically significant if assays were performed in a clinical laboratory or statistically significant if pertaining to research findings. |

**Modification Type:** Disease-specific

#### Approved Assay Instances

##### 1. FVIII Binding Assay (In Vitro)

**General description:** Increasing amounts of VWF are immobilized by binding to anti-VWF polyclonal antibody-coated microplates. Recombinant FVIII is incubated with the captured VWF, and the bound FVIII is then measured by adding the reagents for a chromogenic assay of FVIII-dependent Factor X activation.

| Property | Details |
|----------|---------|
| **Material** | Variant generated by site-directed mutagenesis and transiently expressed in COS-7, HEK293-EBNA, 293T, or HEK293T cells |
| **Readout** | Quantitative (ELISA) |
| **Threshold (normal)** | Equivalent to WT |
| **Threshold (abnormal)** | Significantly decreased from WT |
| **Approved** | Yes |
| **Proposed Strength** | Strong |

**Published instances (8 studies):**

| PMID | First Author | Year | Cell System |
|------|-------------|------|-------------|
| 9129031 | Gu | 1997 | COS-7 |
| 9845532 | Jorieux | 1998 | COS-7 |
| 10706867 | Allen | 2000 | COS-7 |
| 15213842 | Schneppenheim | 2004 | 293-EBNA |
| 20586924 | Castaman | 2010 | HEK293-EBNA |
| 23636243 | Skipwith | 2013 | 293T |
| 28581694 | Swystun | 2017 | VWF/FVIII DKO mice (murine plasma-derived) |
| ASH Abstract | Montgomery | 2018 | HEK293T (mutated murine VWF) |

##### 2. Hydrodynamic Injection / In Vivo Animal Model

**General description:** The influence of VWF–FVIII binding on hemostatic thrombus formation assessed in a murine tail vein transection (TVT) model. VWF KO mice received tail vein injections of wild type or severe type 2N VWF, with in vivo expression induced via hydrodynamic tail vein injections of the murine VWF cDNA containing the type 2N VWD variants.

| Property | Details |
|----------|---------|
| **PMID** | 28581694 |
| **First Author** | Swystun (2017) |
| **Material** | VWF/FVIII double knockout (DKO) C57BL/6 mice |
| **Readout** | Quantitative (ELISA) |
| **Positive Control** | WT |
| **Negative Control** | FVIII KO |
| **Approved** | Yes |
| **Proposed Strength** | Strong |

##### 3. Knock-In Mouse Model

**General description:** CRISPR/Cas9 gene editing to generate VWF2N mice with type 2N causative mutations on the C57BL6 background.

| Property | Details |
|----------|---------|
| **Reference** | ASH Abstract (Montgomery & Shi, 2018) |
| **Material** | Two lines of VWF2N mice (VWF2N1/2N1 and VWF2N2/2N2) each with 2354G>A (G785E) mutation generated via CRISPR/Cas9 |
| **Positive Control** | WT |
| **Approved** | Yes |
| **Proposed Strength** | Strong |

##### 4. Mufti et al. Study

| Property | Details |
|----------|---------|
| **PMID** | 29980574 |
| **First Author** | Mufti (2018) |
| **Last Author** | Hampshire |
| **Note** | This study investigated 2 common SNVs in VWF: rs1063856 (c.2365A>G) and rs1063857 (c.2385T>C). Neither SNV had a significant effect on VWF:FVIIIB when investigated in healthy controls or in vitro. However, the combined variant haplotype p.[T789A;Y795=] VWF had a slightly decreased binding affinity to FVIII compared with WT VWF, likely due to a faster dissociation rate. |

---

### PS4 - Prevalence in Affected

**Original ACMG Summary:** The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.

**VCEP Specification:** *Not Applicable*

**Comments:** Use PM3 for proband counting.

---

### PM1 - Mutational Hot Spot

**Original ACMG Summary:** Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.

**VCEP Specification:** *Not Applicable*

**Comments:** Rule does not apply due to benign variation being present throughout the gene.

---

### PM2 - Absent from Controls

**Original ACMG Summary:** Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium. Caveat: Population data for indels may be poorly called by next generation sequencing.

**VCEP Specification (Supporting only):**
- Use code for variants with a **popmax MAF of <0.005** in gnomAD

**Modification Type:** Disease-specific, Gene-specific

---

### PM3 - In Trans with Pathogenic

**Original ACMG Summary:** For recessive disorders, detected in trans with a pathogenic variant. Note: This requires testing of parents (or offspring) to determine phase.

**VCEP Specifications:** May be applied when the variants on both alleles have MAFs below the BS1 threshold.

Use SVI recommended point system for probands with a VWD type 2N diagnosis.

#### PM3 Point System (Per Proband)

| Classification/Zygosity of Other Variant | Confirmed in Trans | Phase Unknown |
|------------------------------------------|-------------------|---------------|
| Pathogenic or Likely pathogenic variant | 1.0 | 0.5 (P) / 0.25 (LP) |
| Homozygous (non-consanguineous) | 1.0 | 1.0 |
| Homozygous (consanguineous, max 0.5/family) | 0.5 | 0.5 |
| VUS (max 0.5 total) | 0.25 | 0.0 |

#### PM3 Evidence Strength Thresholds

| Total Points | Strength Level |
|--------------|----------------|
| 0.5 | PM3_Supporting |
| 1.0 | PM3 (Moderate) |
| 2.0 | PM3_Strong |
| 4.0 | PM3_VeryStrong |

**Modification Type:** Disease-specific

---

### PM4 - Protein Length Changes

**Original ACMG Summary:** Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Moderate** | Use with no specification. |

**Modification Type:** None

---

### PM5 - Novel Missense at Same Residue

**Original ACMG Summary:** Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before. Example: Arg156His is pathogenic; now you observe Arg156Cys. Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Moderate** | Use code when previously reported variant reaches a pathogenic classification using the VWD Type 2 rule specifications. Previously reported variant can be associated with a different type of VWD. Code may also be applied when two previously reported variants reach a likely pathogenic classification using the VWD Type 2 rule specifications. Previously reported variants can be associated with a different type of VWD. |
| **Supporting** | Use code when previously reported variant reaches a likely pathogenic classification using the VWD Type 2 rule specifications. Previously reported variant can be associated with a different type of VWD. |

**Modification Type:** Disease-specific, General recommendation

---

### PM6 - De Novo (Assumed)

**Original ACMG Summary:** Assumed de novo, but without confirmation of paternity and maternity.

**VCEP Specification:** *Not Applicable*

**Comments:** Use the PS2 code in lieu of using this code for de novo variants. See [PS2/PM6 Point System](#ps2pm6-point-system-table-1) above.

---

### PP1 - Co-segregation

**Original ACMG Summary:** Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease. Note: May be used as stronger evidence with increasing segregation data.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | Appropriate to use when a proband has three affected family members. |
| **Moderate** | Appropriate to use when a proband has two affected family members. |
| **Supporting** | Appropriate to use when a proband has one affected family member. |

**Modification Type:** Disease-specific

---

### PP2 - Missense in Constrained Gene

**Original ACMG Summary:** Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.

**VCEP Specification:** *Not Applicable*

**Comments:** Not applicable due to presence of benign variation throughout the VWF gene.

---

### PP3 - Computational Evidence

**Original ACMG Summary:** Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.). Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.

**VCEP Specification (Supporting):**
- Appropriate to use for missense variants that have a **REVEL score ≥0.644** OR a **SpliceAI score suggestive of a splicing defect (≥0.5)**

**Modification Type:** Gene-specific

---

### PP4 - Phenotype Specificity

**Original ACMG Summary:** Patient's phenotype or family history is highly specific for a disease with a single genetic etiology.

**VCEP Specification (Moderate):**

The patient must have a clinical phenotype of excessive mucocutaneous bleeding and required laboratory values to use the PP4 rule code, including:
- A **low factor VIII activity level**, AND
- Evidence of **decreased VWF:FVIII binding**

Additional consistent information should be noted but is not required, including:
- Either normal or low VWF:Ag
- Normal high molecular weight multimers
- Sequencing with duplication/deletion analysis of the F8 gene

**Modification Type:** Disease-specific

---

### PP5 - Reputable Source

**Original ACMG Summary:** Reputable source recently reports variant as pathogenic, but the evidence is not available to the laboratory to perform an independent evaluation.

**VCEP Specification:** *Not Applicable*

**Comments:** This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PMID: 29543229).

---

## Benign Criteria

### BA1 - Allele Frequency >5%

**Original ACMG Summary:** Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

**VCEP Specification (Stand Alone):**
- Appropriate to use for variants with a **Popmax MAF of >0.1** in gnomAD

**Modification Type:** Disease-specific, Gene-specific

---

### BS1 - Frequency Greater Than Expected

**Original ACMG Summary:** Allele frequency is greater than expected for disorder.

**VCEP Specification (Strong):**
- Appropriate to use for variants with a **Popmax MAF of >0.01** in gnomAD

**Modification Type:** Disease-specific, Gene-specific

---

### BS2 - Observed in Healthy Adult

**Original ACMG Summary:** Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

**VCEP Specification:** *Not Applicable*

**Comments:** Not applicable due to the incomplete penetrance seen in VWD.

---

### BS3 - Functional Studies (No Effect)

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

**VCEP Specification:** *Not Applicable*

**Comments:** There are no available assays that can clearly and dependably show no damaging protein effects.

---

### BS4 - Lack of Segregation

**Original ACMG Summary:** Lack of segregation in affected members of a family. Caveat: The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | Appropriate to use when two or more relatives have the phenotype consistent with VWD type 2 without harboring the variant identified in other affected family members. Additionally, there is not another established cause of type 2 VWD (e.g. - there are not multiple type 2 VWD diagnoses) segregating in the family. |
| **Supporting** | Appropriate to use when only one relative has the phenotype consistent with VWD type 2 without harboring the variant identified in other affected family members. Additionally, there is not another established cause of type 2 VWD (e.g. - there are not multiple type 2 VWD diagnoses) segregating in the family. |

**Modification Type:** Disease-specific

---

### BP1–BP7 - Benign Supporting

| Criterion | Status | Comment |
|-----------|--------|---------|
| **BP1** | *Not Applicable* | The VWF gene is not constrained for missense variation (gnomAD). |
| **BP2** | *Not Applicable* | Do not use due to potential of variant being associated with VWD 2N (recessive disease). |
| **BP3** | *Not Applicable* | There are no known repetitive regions in the VWF gene without a known function. |
| **BP4** | Supporting | Use for missense variants that have a REVEL score of **less than or equal to 0.290** AND SpliceAI cutoff of **<0.1**. Use SpliceAI cutoff of <0.1 for other variant types. |
| **BP5** | Supporting | A second variant in VWF may be considered an alternate molecular basis for disease when that variant is LP/P (as evaluated by the VWD VCEP) and fully explains the phenotype of the patient's reported VWD subtype. |
| **BP6** | *Not Applicable* | This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PMID: 29543229). |
| **BP7** | Supporting | Use SpliceAI for splicing predictor with a cutoff score of 0. |

---

## Rules for Combining Criteria

### Pathogenic Classification

| Criteria Combination | Applicable Codes |
|---------------------|------------------|
| 1 Very Strong **AND** ≥1 Strong | (PS2_Very Strong, PM3_Very Strong) AND (PS1, PS2, PS3, PM3_Strong, PP1_Strong) |
| 1 Very Strong **AND** ≥2 Moderate | (PS2_Very Strong, PM3_Very Strong) AND (PS1_Moderate, PS2_Moderate, PM3, PM4, PM5, PP1_Moderate, PP4_Moderate) |
| 1 Very Strong **AND** 1 Moderate **AND** 1 Supporting | (PS2_Very Strong, PM3_Very Strong) AND (PS1_Moderate, PS2_Moderate, PM3, PM4, PM5, PP1_Moderate, PP4_Moderate) AND (PS2_Supporting, PM2_Supporting, PM3_Supporting, PM5_Supporting, PP1, PP3) |
| 1 Very Strong **AND** ≥2 Supporting | (PS2_Very Strong, PM3_Very Strong) AND (PS2_Supporting, PM2_Supporting, PM3_Supporting, PM5_Supporting, PP1, PP3) |
| ≥2 Strong | (PS1, PS2, PS3, PM3_Strong, PP1_Strong) |
| 1 Strong **AND** ≥3 Moderate | (PS1, PS2, PS3, PM3_Strong, PP1_Strong) AND (PS1_Moderate, PS2_Moderate, PM3, PM4, PM5, PP1_Moderate, PP4_Moderate) |
| 1 Strong **AND** 2 Moderate **AND** ≥2 Supporting | (PS1, PS2, PS3, PM3_Strong, PP1_Strong) AND (PS1_Moderate, PS2_Moderate, PM3, PM4, PM5, PP1_Moderate, PP4_Moderate) AND (PS2_Supporting, PM2_Supporting, PM3_Supporting, PM5_Supporting, PP1, PP3) |
| 1 Strong **AND** 1 Moderate **AND** ≥4 Supporting | (PS1, PS2, PS3, PM3_Strong, PP1_Strong) AND (PS1_Moderate, PS2_Moderate, PM3, PM4, PM5, PP1_Moderate, PP4_Moderate) AND (PS2_Supporting, PM2_Supporting, PM3_Supporting, PM5_Supporting, PP1, PP3) |

### Likely Pathogenic Classification

| Criteria Combination | Applicable Codes |
|---------------------|------------------|
| 1 Very Strong **AND** 1 Moderate | (PS2_Very Strong, PM3_Very Strong) AND (PS1_Moderate, PS2_Moderate, PM3, PM4, PM5, PP1_Moderate, PP4_Moderate) |
| 1 Strong **AND** 1 Moderate | (PS1, PS2, PS3, PM3_Strong, PP1_Strong) AND (PS1_Moderate, PS2_Moderate, PM3, PM4, PM5, PP1_Moderate, PP4_Moderate) |
| 1 Strong **AND** ≥2 Supporting | (PS1, PS2, PS3, PM3_Strong, PP1_Strong) AND (PS2_Supporting, PM2_Supporting, PM3_Supporting, PM5_Supporting, PP1, PP3) |
| ≥3 Moderate | (PS1_Moderate, PS2_Moderate, PM3, PM4, PM5, PP1_Moderate, PP4_Moderate) |
| 2 Moderate **AND** ≥2 Supporting | (PS1_Moderate, PS2_Moderate, PM3, PM4, PM5, PP1_Moderate, PP4_Moderate) AND (PS2_Supporting, PM2_Supporting, PM3_Supporting, PM5_Supporting, PP1, PP3) |
| 1 Moderate **AND** ≥4 Supporting | (PS1_Moderate, PS2_Moderate, PM3, PM4, PM5, PP1_Moderate, PP4_Moderate) AND (PS2_Supporting, PM2_Supporting, PM3_Supporting, PM5_Supporting, PP1, PP3) |
| 1 Strong **AND** 2 Moderate | (PS1, PS2, PS3, PM3_Strong, PP1_Strong) AND (PS1_Moderate, PS2_Moderate, PM3, PM4, PM5, PP1_Moderate, PP4_Moderate) |

### Benign Classification

| Criteria Combination | Applicable Codes |
|---------------------|------------------|
| ≥2 Strong | (BS1, BS4) |
| 1 Stand Alone | (BA1) |

### Likely Benign Classification

| Criteria Combination | Applicable Codes |
|---------------------|------------------|
| 1 Strong **AND** 1 Supporting | (BS1, BS4) AND (BS4_Supporting, BP4, BP5, BP7) |
| ≥2 Supporting | (BS4_Supporting, BP4, BP5, BP7) |

---

## Appendices

### Appendix A: Criteria Summary Table

| Criterion | VCEP Status | Max Strength | Modification Type |
|-----------|-------------|--------------|-------------------|
| PVS1 | Not Applicable | — | — |
| PS1 | Specified | Strong / Moderate | Gene-specific |
| PS2 | Specified (point-based) | Very Strong | Disease-specific |
| PS3 | Specified | Strong | Disease-specific |
| PS4 | Not Applicable | — | — |
| PM1 | Not Applicable | — | — |
| PM2 | Specified | Supporting | Disease-specific, Gene-specific |
| PM3 | Specified (point-based) | Very Strong | Disease-specific |
| PM4 | Default | Moderate | None |
| PM5 | Specified | Moderate / Supporting | Disease-specific, General recommendation |
| PM6 | Not Applicable (use PS2) | — | — |
| PP1 | Specified | Strong | Disease-specific |
| PP2 | Not Applicable | — | — |
| PP3 | Specified | Supporting | Gene-specific |
| PP4 | Specified | Moderate | Disease-specific |
| PP5 | Not Applicable | — | — |
| BA1 | Specified | Stand Alone | Disease-specific, Gene-specific |
| BS1 | Specified | Strong | Disease-specific, Gene-specific |
| BS2 | Not Applicable | — | — |
| BS3 | Not Applicable | — | — |
| BS4 | Specified | Strong / Supporting | Disease-specific |
| BP1 | Not Applicable | — | — |
| BP2 | Not Applicable | — | — |
| BP3 | Not Applicable | — | — |
| BP4 | Specified | Supporting | Gene-specific |
| BP5 | Specified | Supporting | None |
| BP6 | Not Applicable | — | — |
| BP7 | Specified | Supporting | Disease-specific |

### Appendix B: Population Frequency Thresholds Summary

| Criterion | Threshold | Strength |
|-----------|-----------|----------|
| BA1 | >0.1 (Popmax MAF in gnomAD) | Stand Alone |
| BS1 | >0.01 (Popmax MAF in gnomAD) | Strong |
| PM2 | <0.005 (Popmax MAF in gnomAD) | Supporting |

### Appendix C: VWD Type 2 Subtype Selection Guidance

Before using this rule set, establish the VWD type 2 subtype:

- **Type 2N indicators:** Low factor VIII activity level, decreased VWF:FVIII binding, autosomal recessive inheritance
- **Key laboratory values:** VWF:Act, VWF:Ag, FVIII:C, VWF:FVIIIB, high molecular weight multimer analysis
- **Type 2N pathogenic variants:** Typically located in exons 17–20 and 24–25

If the variant has not been previously associated with a specific type 2 diagnosis and the proband's type 2 diagnosis is unclear, do not use this rule set.

### Appendix D: Reference PMIDs

| PMID | Description |
|------|-------------|
| 10959685 | VWD prevalence estimates |
| 20301765 | VWD molecular defects and classification |
| 29543229 | ClinGen SVI recommendation against PP5/BP6 |
| 30306084 | VWD type distribution |
| 33780098 | VWD prevalence and genetic testing |
| 9129031 | Gu et al. 1997 - FVIII binding assay |
| 9845532 | Jorieux et al. 1998 - FVIII binding assay |
| 10706867 | Allen et al. 2000 - FVIII binding assay |
| 15213842 | Schneppenheim et al. 2004 - FVIII binding assay |
| 20586924 | Castaman et al. 2010 - FVIII binding assay |
| 23636243 | Skipwith et al. 2013 - FVIII binding assay |
| 28581694 | Swystun et al. 2017 - FVIII binding / Hydrodynamic model |
| 29980574 | Mufti et al. 2018 - VWF SNV analysis |

---

## Version History

| Version | Date | Notes |
|---------|------|-------|
| 1.0.0 | 7/9/2024 | Initial release of VWD type 2N rule specifications |

---

*This document was compiled from ClinGen VCEP specifications and ClinGen SVI recommendations. For the most current version, please refer to the ClinGen website.*
