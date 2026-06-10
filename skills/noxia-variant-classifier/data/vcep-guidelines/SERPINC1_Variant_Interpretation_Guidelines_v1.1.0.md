# ClinGen Thrombosis Expert Panel Variant Interpretation Guidelines for SERPINC1

**Version:** 1.1.0
**Released:** 2/7/2025
**Affiliation:** Thrombosis VCEP
**Based on:** Richards et al., 2015 ACMG/AMP Guidelines

**Release Notes:** All requested edits were made in this document and in the VCI, with exception of one. The p.Cys29= variant remains a VUS since there is only one benign code assigned. The point counting system is currently only being applied when conflicting rule codes are applied.

---

## Gene Information

| Attribute | Value |
|-----------|-------|
| **Gene** | SERPINC1 (HGNC:775) |
| **HGNC Name** | serpin family C member 1 |
| **Transcript** | NM_000488.4 |
| **Disease** | Antithrombin III deficiency (MONDO:0013144) |
| **Inheritance** | Autosomal dominant inheritance |

---

## Table of Contents

1. [Pathogenic Criteria](#pathogenic-criteria)
   - [PVS1 - Null Variant](#pvs1---null-variant)
   - [PS1 - Same Amino Acid Change](#ps1---same-amino-acid-change)
   - [PS2 - De Novo](#ps2---de-novo)
   - [PS3 - Functional Studies](#ps3---functional-studies)
   - [PS4 - Prevalence in Affected](#ps4---prevalence-in-affected)
   - [PM1 - Mutational Hot Spot / Critical Domain](#pm1---mutational-hot-spot--critical-domain)
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
4. [Rules for Conflicting Criteria](#rules-for-conflicting-criteria)
5. [Appendices](#appendices)

---

## Pathogenic Criteria

### PVS1 - Null Variant

**Original ACMG Summary:** Null variant (nonsense, frameshift, canonical ±1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.

**Caveats:**
- Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7).
- Use caution interpreting LOF variants at the extreme 3' end of a gene.
- Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact.
- Use caution in the presence of multiple transcripts.

**VCEP Specifications:** Use the SVI WG PVS1 decision tree with specified "regions critical to protein function" for SERPINC1. Applicable at all strength levels.

#### Strength Levels

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Very Strong** | Use decision tree as per SVI WG with specified "regions critical to protein function" | Gene-specific |
| **Strong** | Use decision tree as per SVI WG with specified "regions critical to protein function" | Gene-specific |
| **Moderate** | Use decision tree as per SVI WG with specified "regions critical to protein function" | Gene-specific |
| **Supporting** | Use decision tree as per SVI WG with specified "regions critical to protein function" | Gene-specific |

---

### PS1 - Same Amino Acid Change

**Original ACMG Summary:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change. Example: Val->Leu caused by either G>C or G>T in the same codon. Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:** Use caution not to compare variants being curated to variants that are potential cryptic splice sites.

#### Strength Levels

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Strong** | Use with no additional specification except comparison variant must be classified as **pathogenic** using SERPINC1 rule specifications from the Thrombosis VCEP | Gene-specific |
| **Moderate** | Use with no additional specification except comparison variant must be classified as **likely pathogenic** using SERPINC1 rule specifications from the Thrombosis VCEP | Gene-specific |

---

### PS2 - De Novo

**Original ACMG Summary:** De novo (both maternity and paternity confirmed) in a patient with the disease and no family history. Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.

**VCEP Specifications:** Any proband must meet the PP4-defined antithrombin deficiency laboratory phenotype (see PP4/PS4 description below). Use the "Phenotype highly specific for gene" category from the ClinGen SVI de novo point system.

> **Note:** PM6 (assumed de novo) is **Not Applicable** for SERPINC1. Use the PS2 code in lieu of PM6 for all de novo variants. Both confirmed and unconfirmed parental relationships are scored through the PS2 point system.

#### PS2/PM6 Point System

| Phenotypic Consistency | Confirmed Parental Relationships | Unconfirmed Parental Relationships |
|------------------------|----------------------------------|------------------------------------|
| **Phenotype highly specific for gene** *(use this row for antithrombin deficiency)* | 2 points | 1 point |
| Phenotype consistent but not highly specific | 1 point | 0.5 points |
| Phenotype consistent + high genetic heterogeneity | 0.5 points | 0.25 points |
| Phenotype not consistent | 0 points | 0 points |

#### Evidence Strength Thresholds

| Total Points | Strength Level |
|--------------|----------------|
| ≥0.5 | PS2_Supporting |
| ≥1.0 | PS2_Moderate |
| ≥2.0 | PS2 (Strong) |
| ≥4.0 | PS2_VeryStrong |

---

### PS3 - Functional Studies

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product. Note: Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.

**VCEP Specifications:** Model organisms do not tend to recapitulate the phenotype of interest and are not used for curation. Only PS3_Supporting strength is available for SERPINC1.

#### Strength Levels

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Supporting** | See approved assay list below. General description of assays that can be used: *In vitro* functional studies in COS-1, HEK293T, or HEK-EBNA cells demonstrating abnormal activity or antigen levels (details below) | Disease-specific |

#### Approved Assay Categories

**Antithrombin Activity Assays:**
- Antithrombin activity levels measured by FXa inhibition activity assay
- Antithrombin activity levels measured by thrombin inhibition activity assay

**Antithrombin Antigen Assays:**
- Antithrombin antigen levels measured by ELISA

**In vivo Studies:**
- Studies demonstrating rescue of antithrombin levels would be considered, but no studies are known to be available at this time

#### Approved Assay Instances

##### Antithrombin Activity

| Attribute | PMID: 23809926 (Maruyama 2013) | PMID: 27098529 (Navarro-Fernandez 2016) | PMID: 30237862 (Navarro-Fernandez 2018) |
|-----------|-------------------------------|----------------------------------------|----------------------------------------|
| **Assay** | AT activity by FXa & thrombin inhibition assay | AT activity by FXa inhibition (chromogenic) | Antithrombin activity |
| **Cell Line** | COS-1 cells | HEK-EBNA cells | HEK-EBNA cells |
| **Readout** | Quantitative: AT activity levels in cell lysate and conditioned medium | Quantitative: anti-FXa activity in conditioned medium | Quantitative: Size of thrombin-AT complexes formed |
| **Technical Replicates** | Met (triplicates) | ? | Met (triplicates) |
| **Positive Control** | Met (WT) | ? | Met (WT) |
| **Negative Control** | Not met | ? | Met (mock) |
| **Threshold (Normal)** | Similar to WT | Similar to WT | Similar to WT |
| **Threshold (Abnormal)** | Different than WT | Different than WT | Lesser than WT |
| **Test Variant** | c.2534C>T (Arg56Cys) | c.89T>A (Val30Glu) | c.3G>T (Met1?) |
| **Approved** | Yes | Yes | Yes |
| **Proposed Strength** | PS3_Supporting | PS3_Supporting | PS3_Supporting |

##### Antithrombin Antigen

| Attribute | PMID: 23809926 (Maruyama 2013) | PMID: 23117546 (Deng 2013) |
|-----------|-------------------------------|---------------------------|
| **Assay** | AT antigen by ELISA | AT antigen by ELISA |
| **Cell Line** | COS-1 cells | HEK293T cells |
| **Readout** | Quantitative: AT antigen levels in cell lysate and conditioned medium | Quantitative: AT antigen levels in cell lysate and conditioned medium |
| **Technical Replicates** | Met (triplicates) | Met (triplicates) |
| **Positive Control** | Met (WT) | Met (WT) |
| **Negative Control** | Not met | Not met |
| **Threshold (Normal)** | Similar to WT | Similar to WT (%WT) |
| **Threshold (Abnormal)** | Different than WT | Lesser than WT |
| **Test Variant** | c.2534C>T (Arg56Cys); c.13398C>A (Ala459Asp); c.2703C>G (Pro112Arg) | c.134G>A (Arg45Gln); c.342T>G (Ser114Arg) |
| **Approved** | Yes | Yes |
| **Proposed Strength** | PS3_Supporting | PS3_Supporting |

##### Non-Approved Assays (Not for Clinical Use)

| Assay | Reference | Reason |
|-------|-----------|--------|
| Immunofluorescence assay (HEK-EBNA) | PMID: 30237862 (Navarro-Fernandez 2018) | Not approved |
| Intracellular retention assay (HEK-EBNA) | DOI: 10.1160/TH12-09-0707 (Aguila 2013) | Not approved |

---

### PS4 - Prevalence in Affected

**Original ACMG Summary:** The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.

**VCEP Specifications:** This code requires the use of proband points. Do not apply this code for variants that meet BS1 or BA1 criteria. Do not count the proband used for PP4 in this code's proband count.

#### Proband Eligibility Requirements

The proband must have a laboratory phenotype consistent with antithrombin deficiency. A personal history of thrombosis is **neither required nor considered** when applying this rule code. Additionally:
- Individuals must **not** be on an anticoagulant
- Acquired antithrombin deficiency must be ruled out
- Females must **not** be pregnant or taking oral contraceptives

#### PS4 Proband Point System

**1 point each:**
- A proband with antithrombin activity level <0.8 IU/mL (or below the lower limit of a laboratory's assay reference range) on **repeated independent samples**
- A proband with antithrombin activity level <0.8 IU/mL (or below the lower limit of a laboratory's assay reference range) **without confirmation** of repeated independent samples but **with a family history** of antithrombin activity levels <0.8 IU/mL (a family history of thrombosis but no antithrombin activity levels provided does not qualify)
- A proband with an **abnormal crossed immunoelectrophoresis assay** demonstrating decreased antithrombin function

**0.5 point each:**
- A proband with antithrombin activity level <0.8 IU/mL (or below the lower limit of a laboratory's assay reference range) **without confirmation** of repeated independent samples tested

#### PS4 Evidence Strength Thresholds

| Total Points | Strength Level |
|--------------|----------------|
| 1 | PS4_Supporting |
| 2–3 | PS4_Moderate |
| 4–7 | PS4 (Strong) |
| ≥8 | PS4_VeryStrong |

---

### PM1 - Mutational Hot Spot / Critical Domain

**Original ACMG Summary:** Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.

**VCEP Specifications (Moderate):**

This code is applicable for variants affecting the following residues:

| Functional Domain | Residues |
|-------------------|----------|
| **Disulfide bridge cysteine residues**¹ | Cys40, Cys53, Cys127, Cys160, Cys279, Cys462 |
| **Heparin binding site residues** | Ile39, Arg56, Pro73, Arg79 |
| **Reactive site residues**² | Ala414, Ala416 |
| **N-glycosylation site**³ | Asn224 |

> **References:**
> 1. Kottke-Marchant K, Duncan A. *Antithrombin deficiency: issues in laboratory diagnosis.* Arch Pathol Lab Med (2002) 126(11):1326-36. PMID: 12421140
> 2. Perry DJ, Carrell RW. *CpG dinucleotides are "hotspots" for mutation in the antithrombin III gene.* Mol Biol Med (1989) 6(3):239-43. PMID: 2615648
> 3. Navarro-Fernandez et al. *Antithrombin Dublin (p.Val30Glu).* Thromb Haemost (2016) 116(1):146-54.

**Modification Type:** Gene-specific

---

### PM2 - Absent from Controls

**Original ACMG Summary:** Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium. Caveat: Population data for indels may be poorly called by next generation sequencing.

**VCEP Specification (Supporting only):**
- gnomAD popmax filtering allele frequency **<0.00002**

**Modification Type:** Disease-specific, Gene-specific

---

### PM3 - In Trans with Pathogenic

**Original ACMG Summary:** For recessive disorders, detected in trans with a pathogenic variant. Note: This requires testing of parents (or offspring) to determine phase.

***Not Applicable***

**Comments:** Variants in this gene are being curated as a dominant condition, so this rule code does not apply.

---

### PM4 - Protein Length Changes

**Original ACMG Summary:** Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

**VCEP Specifications:**

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Moderate** | No specification (use as per original ACMG guidelines) | None |

---

### PM5 - Novel Missense at Same Residue

**Original ACMG Summary:** Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before. Example: Arg156His is pathogenic; now you observe Arg156Cys. Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:** Use caution not to compare variants being curated to variants that are potential cryptic splice sites.

#### Strength Levels

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Moderate** | Use when previously reported variant reaches a **pathogenic** classification using SERPINC1 rule specifications from the Thrombosis VCEP | General recommendation |
| **Supporting** | Use when previously reported variant reaches a **likely pathogenic** classification using SERPINC1 rule specifications from the Thrombosis VCEP | General recommendation |

---

### PM6 - De Novo (Assumed)

**Original ACMG Summary:** Assumed de novo, but without confirmation of paternity and maternity.

***Not Applicable***

**Comments:** Use the PS2 code in lieu of using this code for de novo variants. See [PS2 - De Novo](#ps2---de-novo) above for the unified point-based system that handles both confirmed and assumed de novo scenarios.

---

### PP1 - Co-segregation

**Original ACMG Summary:** Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease. Note: May be used as stronger evidence with increasing segregation data.

**VCEP Specifications:**

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Strong** | ≥7 meioses across **more than one family** | Disease-specific |
| **Moderate** | 4–6 meioses across one or more families | Disease-specific |
| **Supporting** | 2–3 meioses across one or more families | Disease-specific |

---

### PP2 - Missense in Constrained Gene

**Original ACMG Summary:** Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.

***Not Applicable***

**Comments:** Not applicable due to presence of benign variation throughout the SERPINC1 gene.

---

### PP3 - Computational Evidence

**Original ACMG Summary:** Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.). Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.

**VCEP Specifications (Supporting):**

| Variant Type | Tool | Threshold |
|-------------|------|-----------|
| **Missense variants** | REVEL | Score ≥0.6 |
| **Potential splicing variants** | SpliceAI | Score ≥0.5 |

**Modification Type:** Gene-specific

---

### PP4 - Phenotype Specificity

**Original ACMG Summary:** Patient's phenotype or family history is highly specific for a disease with a single genetic etiology.

**VCEP Specifications:** Please see attached guidance regarding the use of PP4/PS4 rule codes to properly assess eligibility. Do not apply this code for variants that meet BS1 or BA1 criteria. Do not count the proband used for the PP4 code for the PS4 code's proband count.

**PP4 (Supporting):**

A single proband used for this phenotype rule code must have:
- Antithrombin activity level **<0.8 IU/mL** (or below the lower limit of a laboratory's assay reference range)
- Abnormal levels confirmed on **repeated independent samples**
- **OR** an abnormal crossed immunoelectrophoresis assay demonstrating decreased antithrombin function (typically caused by type II variants)

**Additional Eligibility Requirements (shared with PS4):**
- A personal history of thrombosis is **neither required nor considered**
- Individual must **not** be on an anticoagulant
- Acquired antithrombin deficiency must be ruled out
- Females must **not** be pregnant or taking oral contraceptives

**Modification Type:** Disease-specific

---

### PP5 - Reputable Source

**Original ACMG Summary:** Reputable source recently reports variant as pathogenic, but the evidence is not available to the laboratory to perform an independent evaluation.

***Not Applicable***

This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PMID: 29543229).

---

## Benign Criteria

### BA1 - Allele Frequency >5%

**Original ACMG Summary:** Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

**VCEP Specification (Stand Alone):**
- gnomAD popmax filtering allele frequency **≥0.002**

**Modification Type:** Disease-specific, Gene-specific

---

### BS1 - Frequency Greater Than Expected

**Original ACMG Summary:** Allele frequency is greater than expected for disorder.

**VCEP Specifications:** Common founder SERPINC1 variants are **excluded** from eligibility of the BS1 code.

#### Excluded Founder Variants

| Variant (cDNA) | Variant (Protein) | Common Name / Reference |
|----------------|-------------------|------------------------|
| c.218C>T | p.Pro73Leu | PMID: 23910795 |
| c.236G>A | p.Arg79His | AT Padua |
| c.439A>G | p.Thr147Ala | PMID: 32920809 |
| c.1246G>T | p.Ala416Ser | AT Cambridge II |
| — | p.Leu131Phe | PMID: 26748602 |
| c.89T>A | p.Val30Glu | AT Dublin (PMID: 27098529) |

> **Note:** This list of excluded founder variants will likely grow over time.

**BS1 (Strong):**
- gnomAD popmax filtering allele frequency **>0.0002**

**Modification Type:** Disease-specific, Gene-specific

---

### BS2 - Observed in Healthy Adult

**Original ACMG Summary:** Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

**VCEP Specifications:**

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Strong** | Variant identified in **≥2 heterozygotes** OR **≥1 homozygote** with normal antithrombin levels [>0.8 IU/mL (or above the lower limit of a laboratory's assay reference range)] | Disease-specific |
| **Supporting** | Variant identified in **1 heterozygote** with normal antithrombin levels [>0.8 IU/mL (or above the lower limit of a laboratory's assay reference range)] | Disease-specific |

---

### BS3 - Functional Studies (No Effect)

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

***Not Applicable***

**Comments:** There are no available assays or model organisms that can recapitulate disease, and in vitro studies cannot dependably rule out pathogenicity.

---

### BS4 - Lack of Segregation

**Original ACMG Summary:** Lack of segregation in affected members of a family. Caveat: The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.

**VCEP Specifications:**

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Strong** | Variant does not segregate in a minimum of **4 relatives** with abnormal antithrombin activity levels [<0.8 IU/mL] within the same family, **OR** the variant does not segregate in **≥2 families**. Non-segregation defined by having abnormal antithrombin activity levels without the SERPINC1 variant of interest. | Disease-specific |
| **Supporting** | Variant does not segregate in a minimum of **2 relatives** with abnormal antithrombin activity levels [<0.8 IU/mL] within the same family. | Disease-specific |

---

### BP1–BP7 - Benign Supporting

| Criterion | Status | Specification | Modification Type |
|-----------|--------|---------------|-------------------|
| **BP1** | **Not Applicable** | This rule code does not apply to the SERPINC1 gene, as missense and truncating variants account for disease. | — |
| **BP2** | **Applicable (Supporting)** | Can be applied when a SERPINC1 variant is **in cis** with another pathogenic SERPINC1 variant. The pathogenic variant must be evaluated using ClinGen SERPINC1 specified rules. **Cannot** be applied to a variant *in trans* with a pathogenic variant, as this scenario could reasonably occur and increase the risk of venous thrombosis. | Disease-specific |
| **BP3** | **Not Applicable** | There are no known repetitive regions in the SERPINC1 gene without a known function. | — |
| **BP4** | **Applicable (Supporting)** | Use for missense variants with REVEL score **≤0.30** AND no evidence of splicing effect via SpliceAI (score **≤0.1**), OR for non-canonical intronic variants with no evidence of splicing effect via SpliceAI (score ≤0.1). | Gene-specific |
| **BP5** | **Not Applicable** | Not recommended for use at this time. There are other genes that can be associated with decreased antithrombin activity levels, such as genes associated with congenital disorders of glycosylation. | — |
| **BP6** | **Not Applicable** | Not for use as recommended by the ClinGen SVI VCEP Review Committee (PMID: 29543229). | — |
| **BP7** | **Applicable (Supporting)** | Use SpliceAI to rule out a predicted splicing effect (score **≤0.1**). Evolutionary conservation is defined as PhyloP >0.1 **OR** the reference nucleotide is present in ≥3 mammals or ≥1 primate. | General recommendation |

---

## Rules for Combining Criteria

### Pathogenic Classification

| Criteria Combination |
|---------------------|
| 1 Very Strong *(PVS1, PS2_VeryStrong, PS4_VeryStrong)* **AND** ≥1 Strong *(PVS1_Strong, PS1, PS2, PS4, PP1_Strong)* |
| 1 Very Strong *(PVS1, PS2_VeryStrong, PS4_VeryStrong)* **AND** ≥2 Moderate *(PVS1_Moderate, PS1_Moderate, PS2_Moderate, PS4_Moderate, PM1, PM4, PM5, PP1_Moderate)* |
| 1 Very Strong *(PVS1, PS2_VeryStrong, PS4_VeryStrong)* **AND** 1 Moderate *(PVS1_Moderate, PS1_Moderate, PS2_Moderate, PS4_Moderate, PM1, PM4, PM5, PP1_Moderate)* **AND** 1 Supporting *(PVS1_Supporting, PS2_Supporting, PS3_Supporting, PS4_Supporting, PM2_Supporting, PM5_Supporting, PP1, PP3, PP4)* |
| 1 Very Strong *(PVS1, PS2_VeryStrong, PS4_VeryStrong)* **AND** ≥2 Supporting *(PVS1_Supporting, PS2_Supporting, PS3_Supporting, PS4_Supporting, PM2_Supporting, PM5_Supporting, PP1, PP3, PP4)* |
| ≥2 Strong *(PVS1_Strong, PS1, PS2, PS4, PP1_Strong)* |
| 1 Strong *(PVS1_Strong, PS1, PS2, PS4, PP1_Strong)* **AND** ≥3 Moderate *(PVS1_Moderate, PS1_Moderate, PS2_Moderate, PS4_Moderate, PM1, PM4, PM5, PP1_Moderate)* |
| 1 Strong *(PVS1_Strong, PS1, PS2, PS4, PP1_Strong)* **AND** 2 Moderate *(PVS1_Moderate, PS1_Moderate, PS2_Moderate, PS4_Moderate, PM1, PM4, PM5, PP1_Moderate)* **AND** ≥2 Supporting *(PVS1_Supporting, PS2_Supporting, PS3_Supporting, PS4_Supporting, PM2_Supporting, PM5_Supporting, PP1, PP3, PP4)* |
| 1 Strong *(PVS1_Strong, PS1, PS2, PS4, PP1_Strong)* **AND** 1 Moderate *(PVS1_Moderate, PS1_Moderate, PS2_Moderate, PS4_Moderate, PM1, PM4, PM5, PP1_Moderate)* **AND** ≥4 Supporting *(PVS1_Supporting, PS2_Supporting, PS3_Supporting, PS4_Supporting, PM2_Supporting, PM5_Supporting, PP1, PP3, PP4)* |

### Likely Pathogenic Classification

| Criteria Combination |
|---------------------|
| 1 Very Strong *(PVS1, PS2_VeryStrong, PS4_VeryStrong)* **AND** 1 Moderate *(PVS1_Moderate, PS1_Moderate, PS2_Moderate, PS4_Moderate, PM1, PM4, PM5, PP1_Moderate)* |
| 1 Very Strong *(PVS1, PS2_VeryStrong, PS4_VeryStrong)* **AND** 1 Supporting *(PVS1_Supporting, PS2_Supporting, PS3_Supporting, PS4_Supporting, PM2_Supporting, PM5_Supporting, PP1, PP3, PP4)* |
| 1 Strong *(PVS1_Strong, PS1, PS2, PS4, PP1_Strong)* **AND** 1 Moderate *(PVS1_Moderate, PS1_Moderate, PS2_Moderate, PS4_Moderate, PM1, PM4, PM5, PP1_Moderate)* |
| 1 Strong *(PVS1_Strong, PS1, PS2, PS4, PP1_Strong)* **AND** ≥2 Supporting *(PVS1_Supporting, PS2_Supporting, PS3_Supporting, PS4_Supporting, PM2_Supporting, PM5_Supporting, PP1, PP3, PP4)* |
| ≥3 Moderate *(PVS1_Moderate, PS1_Moderate, PS2_Moderate, PS4_Moderate, PM1, PM4, PM5, PP1_Moderate)* |
| 2 Moderate *(PVS1_Moderate, PS1_Moderate, PS2_Moderate, PS4_Moderate, PM1, PM4, PM5, PP1_Moderate)* **AND** ≥2 Supporting *(PVS1_Supporting, PS2_Supporting, PS3_Supporting, PS4_Supporting, PM2_Supporting, PM5_Supporting, PP1, PP3, PP4)* |
| 1 Moderate *(PVS1_Moderate, PS1_Moderate, PS2_Moderate, PS4_Moderate, PM1, PM4, PM5, PP1_Moderate)* **AND** ≥4 Supporting *(PVS1_Supporting, PS2_Supporting, PS3_Supporting, PS4_Supporting, PM2_Supporting, PM5_Supporting, PP1, PP3, PP4)* |
| 1 Strong *(PVS1_Strong, PS1, PS2, PS4, PP1_Strong)* **AND** 2 Moderate *(PVS1_Moderate, PS1_Moderate, PS2_Moderate, PS4_Moderate, PM1, PM4, PM5, PP1_Moderate)* |

### Benign Classification

| Criteria Combination |
|---------------------|
| ≥2 Strong *(BS1, BS2, BS4)* |
| 1 Stand Alone *(BA1)* |

### Likely Benign Classification

| Criteria Combination |
|---------------------|
| 1 Strong *(BS1, BS2, BS4)* **AND** 1 Supporting *(BS2_Supporting, BS4_Supporting, BP2, BP4, BP7)* |
| ≥2 Supporting *(BS2_Supporting, BS4_Supporting, BP2, BP4, BP7)* |

---

## Rules for Conflicting Criteria

For SERPINC1 variants where criteria codes for both benign and pathogenic evidence apply, these variants are **not** subjected to a Variant of Uncertain Significance (VUS) classification. Instead, apply the rule combination point system described by **Tavtigian et al. 2020** (PMID: 32720330).

**Process:**
1. Use Tavtigian et al. Table 2 to determine the point value for each evidence code
2. Sum the point values (benign evidence codes contribute negative points)
3. Use Tavtigian et al. Table 3 to determine the final classification based on the summed point value

| Evidence Strength | Points (Pathogenic) | Points (Benign) |
|-------------------|--------------------:|----------------:|
| Supporting | +1 | −1 |
| Moderate | +2 | −2 |
| Strong | +4 | −4 |
| Very Strong | +8 | — |
| Stand Alone | — | −8 |

| Point Total | Classification |
|-------------|----------------|
| ≥10 | Pathogenic |
| 6–9 | Likely Pathogenic |
| 0–5 | VUS |
| −1 to −6 | Likely Benign |
| ≤−7 | Benign |

---

## Appendices

### Appendix A: Criteria Applicability Summary

| Criterion | Available Strengths | Status |
|-----------|-------------------|--------|
| PVS1 | VeryStrong, Strong, Moderate, Supporting | Applicable (SVI decision tree) |
| PS1 | Strong, Moderate | Applicable |
| PS2 | VeryStrong, Strong, Moderate, Supporting | Applicable (point system; also replaces PM6) |
| PS3 | Supporting only | Applicable (approved assays only) |
| PS4 | VeryStrong, Strong, Moderate, Supporting | Applicable (proband point system) |
| PM1 | Moderate | Applicable (specific residues) |
| PM2 | Supporting | Applicable (popmax MAF <0.00002) |
| PM3 | — | **Not Applicable** (dominant condition) |
| PM4 | Moderate | Applicable (no specification) |
| PM5 | Moderate, Supporting | Applicable |
| PM6 | — | **Not Applicable** (use PS2 instead) |
| PP1 | Strong, Moderate, Supporting | Applicable (meiosis count) |
| PP2 | — | **Not Applicable** (benign variation present) |
| PP3 | Supporting | Applicable (REVEL ≥0.6 / SpliceAI ≥0.5) |
| PP4 | Supporting | Applicable (AT activity phenotype) |
| PP5 | — | **Not Applicable** (per ClinGen SVI) |
| BA1 | Stand Alone | Applicable (popmax MAF ≥0.002) |
| BS1 | Strong | Applicable (popmax MAF >0.0002; excludes founder variants) |
| BS2 | Strong, Supporting | Applicable (normal AT levels) |
| BS3 | — | **Not Applicable** (no reliable benign assay) |
| BS4 | Strong, Supporting | Applicable (non-segregation) |
| BP1 | — | **Not Applicable** (missense causes disease) |
| BP2 | Supporting | Applicable (in cis only) |
| BP3 | — | **Not Applicable** (no repetitive regions) |
| BP4 | Supporting | Applicable (REVEL ≤0.30 + SpliceAI ≤0.1) |
| BP5 | — | **Not Applicable** (other genes affect AT levels) |
| BP6 | — | **Not Applicable** (per ClinGen SVI) |
| BP7 | Supporting | Applicable (SpliceAI ≤0.1 + conservation) |

### Appendix B: Population Frequency Thresholds Summary

| Criterion | Threshold | Strength |
|-----------|-----------|----------|
| BA1 | ≥0.002 popmax MAF | Stand Alone |
| BS1 | >0.0002 popmax MAF | Strong |
| PM2 | <0.00002 popmax MAF | Supporting |

### Appendix C: Computational Prediction Thresholds Summary

| Criterion | Tool | Pathogenic Threshold | Benign Threshold |
|-----------|------|---------------------|-----------------|
| PP3 (Missense) | REVEL | ≥0.6 | — |
| PP3 (Splicing) | SpliceAI | ≥0.5 | — |
| BP4 (Missense) | REVEL + SpliceAI | — | REVEL ≤0.30 AND SpliceAI ≤0.1 |
| BP4 (Intronic) | SpliceAI | — | ≤0.1 |
| BP7 (Synonymous) | SpliceAI + PhyloP | — | SpliceAI ≤0.1; PhyloP >0.1 OR ref nt in ≥3 mammals/≥1 primate |

### Appendix D: Reference PMIDs

| PMID | Reference |
|------|-----------|
| 12421140 | Kottke-Marchant K, Duncan A. *Antithrombin deficiency: issues in laboratory diagnosis.* Arch Pathol Lab Med (2002) 126(11):1326-36. |
| 2615648 | Perry DJ, Carrell RW. *CpG dinucleotides are "hotspots" for mutation in the antithrombin III gene.* Mol Biol Med (1989) 6(3):239-43. |
| 27098529 | Navarro-Fernandez et al. *Antithrombin Dublin (p.Val30Glu): a relatively common variant with moderate thrombosis risk of causing transient antithrombin deficiency.* Thromb Haemost (2016) 116(1):146-54. |
| 29543229 | ClinGen SVI VCEP Review Committee recommendation (PP5/BP6 not for use). |
| 32720330 | Tavtigian et al. 2020. Point-based system for combining criteria with conflicting evidence. |
| 23809926 | Maruyama (2013). AT activity/antigen functional assay (COS-1 cells). |
| 23117546 | Deng (2013). AT antigen functional assay (HEK293T cells). |
| 30237862 | Navarro-Fernandez (2018). AT activity and immunofluorescence assays (HEK-EBNA cells). |
| 23910795 | Founder variant reference: p.Pro73Leu. |
| 32920809 | Founder variant reference: p.Thr147Ala. |
| 26748602 | Founder variant reference: p.Leu131Phe. |

---

## Version History

| Version | Date | Notes |
|---------|------|-------|
| 1.1.0 | 2/7/2025 | Current version. All requested edits applied; p.Cys29= retained as VUS (single benign code). Point counting system applied only for conflicting rule codes. |

---

*This document was compiled from ClinGen Thrombosis VCEP specifications for SERPINC1. For the most current version, please refer to the ClinGen website.*
