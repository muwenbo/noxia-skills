# ClinGen ABCA4 Expert Panel Variant Interpretation Guidelines

**Version:** 1.0.0
**Released:** November 14, 2025
**Affiliation:** ABCA4 Variant Curation Expert Panel (VCEP)
**Reference Transcript:** NM_000350.3

---

## Table of Contents

1. [Overview](#overview)
2. [Gene and Disease Information](#gene-and-disease-information)
3. [Point-Based Classification System](#point-based-classification-system)
4. [Pathogenic Evidence Criteria](#pathogenic-evidence-criteria)
   - [PVS1 - Null Variant](#pvs1---null-variant)
   - [PS1 - Same Amino Acid Change](#ps1---same-amino-acid-change)
   - [PS2 - De Novo Evidence](#ps2---de-novo-evidence)
   - [PS3 - Functional Studies](#ps3---functional-studies)
   - [PS4 - Case-Control Studies](#ps4---case-control-studies)
   - [PM2 - Population Frequency](#pm2---population-frequency)
   - [PM3 - In Trans with Pathogenic Variant](#pm3---in-trans-with-pathogenic-variant)
   - [PM4 - Protein Length Changes](#pm4---protein-length-changes)
   - [PM5 - Novel Missense at Known Position](#pm5---novel-missense-at-known-position)
   - [PP1 - Co-segregation](#pp1---co-segregation)
   - [PP3 - Computational Evidence](#pp3---computational-evidence)
   - [PP4 - Phenotype Specificity](#pp4---phenotype-specificity)
5. [Benign Evidence Criteria](#benign-evidence-criteria)
   - [BA1 - Stand-Alone Benign](#ba1---stand-alone-benign)
   - [BS1 - Allele Frequency Greater Than Expected](#bs1---allele-frequency-greater-than-expected)
   - [BS3 - Functional Studies (Benign)](#bs3---functional-studies-benign)
   - [BS4 - Lack of Segregation](#bs4---lack-of-segregation)
   - [BP4 - Computational Evidence (Benign)](#bp4---computational-evidence-benign)
   - [BP7 - Synonymous/Intronic Variants](#bp7---synonymousintronic-variants)
6. [Not Applicable Criteria](#not-applicable-criteria)
7. [Approved Functional Assays](#approved-functional-assays)
8. [BS1 Exclusion Variant List](#bs1-exclusion-variant-list)
9. [PVS1 Decision Flowchart](#pvs1-decision-flowchart)
10. [References](#references)

---

## Overview

This document provides the ClinGen ABCA4 Expert Panel specifications to the ACMG/AMP variant interpretation guidelines for ABCA4. The VCEP curates only the ABCA4 gene with a single autosomal recessive phenotype: ABCA4-related retinopathies.

**Classification Framework:** This rule set uses the point counting classification system introduced by Tavtigian et al. (PMID: 32720330) in lieu of the rule combining recommendations in Richards et al. (PMID: 25741868).

---

## Gene and Disease Information

| Attribute | Value |
|-----------|-------|
| **Gene** | ABCA4 (HGNC:34) |
| **HGNC Name** | ATP binding cassette subfamily A member 4 |
| **Reference Transcript** | NM_000350.3 |
| **Disease** | ABCA4-related retinopathy (MONDO:0800406) |
| **Mode of Inheritance** | Autosomal recessive |

### Associated Phenotypes

- **Stargardt disease** (most common)
- Retinitis pigmentosa
- Cone-rod dystrophy
- Other ABCA4-related retinopathies

---

## Point-Based Classification System

Variant classification is determined by summing evidence points from applicable criteria:

| Classification | Point Range |
|----------------|-------------|
| **Pathogenic** | ≥10 points |
| **Likely Pathogenic** | 6 to 9 points |
| **Uncertain Significance (VUS)** | 0 to 5 points |
| **Likely Benign** | -6 to -1 points |
| **Benign** | ≤-7 points |

### Evidence Strength Point Values

| Strength Level | Pathogenic Points | Benign Points |
|----------------|-------------------|---------------|
| Very Strong | 8 | N/A |
| Strong | 4 | -4 |
| Moderate | 2 | -2 |
| Supporting | 1 | -1 |

---

## Pathogenic Evidence Criteria

### PVS1 - Null Variant

**Original ACMG Summary:** Null variant (nonsense, frameshift, canonical ±1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.

**VCEP Specification:** Use the ABCA4-modified ClinGen SVI PVS1 flowchart (see [PVS1 Decision Flowchart](#pvs1-decision-flowchart) section).

| Strength | Points | Criteria |
|----------|--------|----------|
| Very Strong | 8 | Per SVI WG decision tree modified for ABCA4 |
| Strong | 4 | Per SVI WG decision tree modified for ABCA4 |
| Moderate | 2 | Per SVI WG decision tree modified for ABCA4 |

**Key Considerations:**
- Beware of genes where LOF is not a known disease mechanism
- Use caution interpreting LOF variants at the extreme 3' end of the gene
- Use caution with splice variants predicted to lead to exon skipping but leave the remainder of the protein intact
- Use caution in the presence of multiple transcripts

---

### PS1 - Same Amino Acid Change

**Original ACMG Summary:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.

| Strength | Points | Criteria |
|----------|--------|----------|
| Strong | 4 | Comparison missense variant must reach **pathogenic** classification using ABCA4 VCEP specifications. Do not apply if the comparison variant is suspected to cause a splicing defect via SpliceAI or other splice predictor. **OR** Comparison splicing variant must reach pathogenic classification and both variants must share the same predicted splicing effect. **OR** See Walker et al. 2023 (PMID: 37352859) Figure 5 for variants with RNA sequencing data. |
| Moderate | 2 | Comparison variant must reach **likely pathogenic** classification using ABCA4 VCEP specifications. Same caveats apply. |
| Supporting | 1 | See Walker et al. 2023 (PMID: 37352859) Figure 5 for variants with RNA sequencing data. |

---

### PS2 - De Novo Evidence

**Original ACMG Summary:** De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.

**VCEP Specification:** Probands must have a second ABCA4 variant classified using ABCA4 VCEP specifications. If the second variant is classified as VUS, the proband's points should be downgraded by half. This code's strength should be capped at **moderate** if phase is unknown for all probands.

#### Phenotype Categories for PS2:

1. **Stargardt disease:** Use SVI recommendations for "Phenotype consistent with gene but not highly specific"
2. **Other ABCA4-related retinopathies** (retinitis pigmentosa, cone-rod dystrophy, etc.): Use SVI recommendations for "Phenotype consistent with gene but not highly specific and high genetic heterogeneity"

| Strength | Points |
|----------|--------|
| Very Strong | 8 |
| Strong | 4 |
| Moderate | 2 |
| Supporting | 1 |

---

### PS3 - Functional Studies

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.

| Strength | Points | Criteria |
|----------|--------|----------|
| Strong | 4 | Loss of function of ABCA4 protein in **transgenic mice** measured by autofluorescence and/or A2E production |
| Supporting | 1 | Measurement of ABCA4 expression or ATPase activity in HEK293 or HeLa cells (see [Approved Functional Assays](#approved-functional-assays)) |

---

### PS4 - Case-Control Studies

**Original ACMG Summary:** The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.

**VCEP Specification:** Based on enrichment analysis from Cornelis et al., 2022 (PMID: 35120629) comparing bi-allelic ABCA4 variants published up to December 31, 2020 against population-matched gnomAD data.

| Strength | Points | Criteria |
|----------|--------|----------|
| Strong | 4 | OR ≥5 where CI does not contain 1 |
| Moderate | 2 | OR ≥3 and <5 where CI does not contain 1 |

---

### PM2 - Population Frequency

**Original ACMG Summary:** Absent from controls (or at extremely low frequency if recessive) in population databases.

| Strength | Points | Criteria |
|----------|--------|----------|
| Supporting | 1 | Total MAF <0.0001 in gnomAD |

---

### PM3 - In Trans with Pathogenic Variant

**Original ACMG Summary:** For recessive disorders, detected in trans with a pathogenic variant.

**VCEP Specification:** Neither variant can meet BS1 or BA1 criteria to apply this code. Both variants must be classified using ABCA4 Rule Specifications.

#### Points Awarded per In Trans Proband

| Classification/Zygosity of Other Variant | Confirmed In Trans | Phase Unknown |
|------------------------------------------|-------------------|---------------|
| Pathogenic or Likely Pathogenic variant | 1.0 | 0.5 (P) / 0.25 (LP) |
| Homozygous occurrence (max 1.0 point) | 0.5 | N/A |
| Uncertain Significance variant (max 0.5 point) | 0.25 | 0.0 |

*Note: All variants should be sufficiently rare (meet PM2 specification). P = Pathogenic; LP = Likely Pathogenic*

#### PM3 Strength Determination

| Evidence Level | Total Points Required |
|----------------|----------------------|
| PM3_Supporting | 0.5 |
| PM3 (Moderate) | 1.0 |
| PM3_Strong | 2.0 |
| PM3_VeryStrong | 4.0 |

| Strength | Points |
|----------|--------|
| Very Strong | 8 |
| Strong | 4 |
| Moderate | 2 |
| Supporting | 1 |

---

### PM4 - Protein Length Changes

**Original ACMG Summary:** Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

| Strength | Points | Criteria |
|----------|--------|----------|
| Moderate | 2 | >1 amino acid deletion/insertion or stop loss variant, **OR** >1 nucleotide with PhyloP ≥7.367 |
| Supporting | 1 | 1 amino acid deletion/insertion or stop loss variant, **OR** 1 nucleotide with PhyloP ≥7.367 |

---

### PM5 - Novel Missense at Known Position

**Original ACMG Summary:** Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.

| Strength | Points | Criteria |
|----------|--------|----------|
| Moderate | 2 | Comparison variant must reach **pathogenic** classification using ABCA4 VCEP specifications. Do not apply if the comparison variant is suspected to cause a splicing defect. |
| Supporting | 1 | Comparison variant must reach **likely pathogenic** classification using ABCA4 VCEP specifications. Do not apply if the comparison variant is suspected to cause a splicing defect. |

---

### PP1 - Co-segregation

**Original ACMG Summary:** Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.

**VCEP Specification:** Non-truncating in trans variants must be curated using ClinGen ABCA4 VCEP specifications and reach pathogenic or likely pathogenic classification. Truncating in trans variants need no further curation. Affected relatives must have both variants identified in proband.

| Strength | Points | Criteria |
|----------|--------|----------|
| Strong | 4 | Segregation in proband plus >2 affected relatives |
| Moderate | 2 | Segregation in proband plus 2 affected relatives |
| Supporting | 1 | Segregation in proband plus 1 affected relative |

---

### PP3 - Computational Evidence

**Original ACMG Summary:** Multiple lines of computational evidence support a deleterious effect on the gene or gene product.

| Strength | Points | Criteria |
|----------|--------|----------|
| Moderate | 2 | Missense variants with REVEL score >0.772 **OR** Synonymous/indel variants with CADD score ≥28.1 **OR** SpliceAI score ≥0.8 |
| Supporting | 1 | Missense variants with REVEL score 0.644-0.772 **OR** Synonymous/indel variants with CADD score 25.3-28.0 **OR** SpliceAI score ≥0.2 |

---

### PP4 - Phenotype Specificity

**Original ACMG Summary:** Patient's phenotype or family history is highly specific for a disease with a single genetic etiology.

**VCEP Specification:** Use the ABCA4 PP4 Specification Table for scoring. This rule is **not applicable** for variants meeting BS1 or BA1 criteria.

| Strength | Points | Criteria |
|----------|--------|----------|
| Moderate | 2 | Single proband with ≥8 phenotype points |
| Supporting | 1 | Single proband with 3-7.5 phenotype points |

#### PP4 Phenotype Scoring Table

**Required for PP4 Use (0.5 points each):**
- Macular flecks on imaging and/or fundus autofluorescence
- Onset under 18 years of age
- Presence of at least two ABCA4 variants

**Specific ABCA4 Phenotype Findings (2 points each):**
- Peripapillary sparing
- Previous exome, genome, or 100+ retinal dystrophy gene panel testing that did not provide an alternative explanation

**Consistent with ABCA4 Phenotype Findings:**

| Finding | Points |
|---------|--------|
| Absent or decreased rod and/or cone ERG responses | 0.5 |
| Optic nerve pallor | 0.5 |
| Bull's eye maculopathy | 1.0 |
| Choriocapillaris dystrophy | 1.0 |
| Pigmentary retinopathy with attenuated vessels | 0.5 |
| White/yellow dots (fundus albipunctatus type) | 1.0 |
| Posterior subcapsular cataract | 0.5 |
| RPE mottling | 0.5 |
| Macular atrophy | 0.5 |
| Cystoid macular edema | 0.5 |
| Decreased peripheral vision | 1.0 |
| Night blindness/nyctalopia | 0.5 |
| Decreased central visual acuity | 1.0 |
| Chorioretinopathy | 1.0 |
| Scotoma | 0.5 |

---

## Benign Evidence Criteria

### BA1 - Stand-Alone Benign

**Original ACMG Summary:** Allele frequency is above 5% in population databases.

| Strength | Criteria |
|----------|----------|
| Stand-Alone | Grpmax allele frequency >0.163 in gnomAD |

---

### BS1 - Allele Frequency Greater Than Expected

**Original ACMG Summary:** Allele frequency is greater than expected for the disorder.

**VCEP Specification:** Based on Whiffin-Ware calculator using:
- Prevalence: 1 in 7,500
- Allelic heterogeneity: 1
- Gene heterogeneity: 1
- Penetrance: 0.5

**Important:** Certain variants are **excluded** from this rule code (see [BS1 Exclusion Variant List](#bs1-exclusion-variant-list)).

| Strength | Points | Criteria |
|----------|--------|----------|
| Strong | -4 | Grpmax allele frequency >0.0163 in gnomAD |
| Supporting | -1 | Grpmax allele frequency >0.00163 in gnomAD |

---

### BS3 - Functional Studies (Benign)

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

**VCEP Specification:** Transgenic mouse models or conflicting minigene assay results should **not** be used as benign evidence.

| Strength | Points | Criteria |
|----------|--------|----------|
| Supporting | -1 | See approved functional assays list |

---

### BS4 - Lack of Segregation

**Original ACMG Summary:** Lack of segregation in affected members of a family.

| Strength | Points | Criteria |
|----------|--------|----------|
| Strong | -4 | Two affected family members without the variant of interest |

---

### BP4 - Computational Evidence (Benign)

**Original ACMG Summary:** Multiple lines of computational evidence suggest no impact on gene or gene product.

| Strength | Points | Criteria |
|----------|--------|----------|
| Moderate | -2 | Missense variants with REVEL score <0.184 **OR** Synonymous/indel variants with CADD score ≤17.3 (PMID: 40225145) |
| Supporting | -1 | Missense variants with REVEL score 0.184-0.290 **OR** Synonymous/indel variants with CADD score 17.4-20 **OR** Intronic variants (where BP7 not applicable) with SpliceAI ≤0.1 |

---

### BP7 - Synonymous/Intronic Variants

**Original ACMG Summary:** A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.

**VCEP Specification:** BP4 is **not** used in combination with this rule code.

| Strength | Points | Criteria |
|----------|--------|----------|
| Moderate | -2 | Intronic (outside canonical -21 to +7) or synonymous variant with SpliceAI prediction <0.1 (PMID: 40225145). Does not apply when conflicting minigene or other functional data is available. |

---

## Not Applicable Criteria

The following ACMG criteria are **not applicable** for ABCA4 variant interpretation:

| Criterion | Reason |
|-----------|--------|
| **PM1** | There is benign variation throughout the ABCA4 gene (no mutational hotspots without benign variation) |
| **PM6** | Use PS2 code for all de novo variants (including non-confirmed paternity) |
| **PP2** | This gene is not constrained for missense variation |
| **PP5** | Not recommended by ClinGen SVI VCEP Review Committee (PMID: 29543229) |
| **BS2** | Age of onset is variable and penetrance is known to be incomplete for some variants |
| **BP1** | Truncating variants do not predominate and missense variants are a known cause of disease |
| **BP2** | Some modifier gene variants are in cis with known pathogenic variants |
| **BP3** | There are no known repetitive regions without known function |
| **BP5** | An individual can be a carrier of a pathogenic ABCA4 variant while having another molecular etiology for their retinopathy |
| **BP6** | Not recommended by ClinGen SVI VCEP Review Committee (PMID: 29543229) |

---

## Approved Functional Assays

### PS3/BS3 Functional Assay Guidance

The following assays have been validated for use in ABCA4 variant interpretation:

#### 1. ABCA4 Expression Assay (PS3_Supporting only)

| Parameter | Description |
|-----------|-------------|
| **PMID** | 34954332; 33375396; 32845050; 29847635 |
| **Author** | Molday et al. |
| **Method** | Expression of ABCA4 variants in HEK293 cells; measure ABCA4 variant level relative to WT by western blotting |
| **Interpretation** | Low expression (<75% WT) indicates protein misfolding; Values <50% WT indicate severe misfolding |
| **Controls** | WT ABCA4 cDNA (positive); Empty cDNA (negative) |
| **Replicates** | Triplicates |
| **Threshold** | ≥20% reduction = PS3_Supporting |
| **Approved Strength** | PS3_Supporting only |

#### 2. ATPase Activity Assay (PS3_Supporting or BS3_Supporting)

| Parameter | Description |
|-----------|-------------|
| **PMID** | Same as expression assay |
| **Author** | Molday et al. |
| **Method** | Expression in HEK293 cells; purification by immunoaffinity chromatography; measure ATPase activity ± substrate |
| **Interpretation** | Absence of substrate-stimulated ATPase activity indicates loss of function |
| **Controls** | WT ABCA4 cDNA (positive); Empty cDNA (negative) |
| **Replicates** | Triplicates (3 measurements) |
| **Threshold** | ≥80% WT = Normal; ≥20% reduction = Abnormal |
| **Approved Strength** | PS3_Supporting or BS3_Supporting |

#### 3. F-Factor Combined Analysis (PS3_Supporting or BS3_Supporting)

| Parameter | Description |
|-----------|-------------|
| **Method** | Combining expression level with ATPase activity measurements |
| **Interpretation** | F-factor provides indication of disease severity |
| **Threshold** | ≥80% WT = Normal; ≥20% reduction = Abnormal |
| **Approved Strength** | PS3_Supporting or BS3_Supporting |

#### 4. Immunofluorescence Localization Assay (PS3_Supporting or BS3_Supporting)

| Parameter | Description |
|-----------|-------------|
| **PMID** | 29145636; 25712131 |
| **Author** | Molday et al.; Palczewski et al. |
| **Method** | Expression in HEK293 or HeLa cells; cellular localization by immunofluorescence microscopy |
| **Interpretation** | WT localizes as vesicle-like structures; Misfolded variants retained in ER (reticular pattern) |
| **Controls** | WT cDNA (positive); Empty cDNA (negative) |
| **Replicates** | Analysis of 20 cells manually |
| **Threshold** | ≥80% WT = Normal; ≥20% reduction = Abnormal |
| **Approved Strength** | PS3_Supporting or BS3_Supporting |

#### 5. Transgenic Mouse Model (PS3_Strong only)

| Parameter | Description |
|-----------|-------------|
| **Method** | Generation and characterization of transgenic mice harboring disease mutation |
| **Readout** | In vivo autofluorescence relative to age-matched WT mice; A2E levels by HPLC |
| **Controls** | KO mice (positive); WT mice (negative) |
| **Replicates** | Triplicate measurements |
| **Threshold** | ≥20% reduction |
| **Approved Strength** | PS3_Strong only |

**Important Note:** Transgenic mouse models or conflicting minigene assay results should **NOT** be used as benign evidence.

---

## BS1 Exclusion Variant List

The following variants are **excluded** from the BS1/BS1_Supporting rule code due to their association with milder phenotypes and higher-than-expected minor allele frequencies:

| ABCA4 Variant | Grpmax Total MAF |
|---------------|------------------|
| c.2588G>C, p.Gly863Ala | 0.008753 |
| c.5603A>T, p.Asn1868Ile | 0.06693 |
| c.5882G>A, p.Gly1961Glu | 0.01768 |
| c.3113C>T, p.Ala1038Val | 0.001985 |
| c.6320G>A, p.Arg2107His | 0.01986 |
| c.4685T>C, p.Ile1562Thr | 0.001878 |
| c.4253+43G>A | 0.005726 |

**Rationale:** These variants are well known to harbor variants associated with milder phenotypes when in trans with more severe pathogenic variants and may have no phenotype in homozygosity. Instead of lowering the BS1_Supporting cutoff to accommodate these variants, they are excluded from the rule code to better characterize other variants with similar MAF that are not known or suspected to cause disease.

**Reference:** Cornelis et al. (PMID: 35120629)

---

## PVS1 Decision Flowchart

The following flowchart guides the application of PVS1 criteria for ABCA4 variants (NM_000350.3 transcript):

### Nonsense or Frameshift Variants

**Predicted to undergo NMD (c.≤6766; p.≤2255):**
- Exon present in biologically relevant transcript(s) → **PVS1**

**Not predicted to undergo NMD (downstream of c.6766/p.2255):**
- Truncated/altered region critical to protein function → **PVS1_Strong**
- Role of region unknown:
  - LoF variants frequent in general population AND/OR exon absent from biologically relevant transcript(s) → **N/A**
  - LoF variants NOT frequent AND exon present in biologically relevant transcript(s):
    - Variant removes >10% of protein → **PVS1_Strong**
    - Variant removes <10% of protein → **PVS1_Moderate**

### GT→AG ±1,2 Splice Site Variants

**Exon skipping or cryptic splice site disrupts reading frame AND predicted to undergo NMD:**
- Exon present in biologically relevant transcript(s) → **PVS1**

**Exon skipping or cryptic splice site preserves reading frame:**
- Role of region unknown:
  - LoF variants frequent in general population AND/OR exon absent from biologically relevant transcript(s) → **N/A**
  - LoF variants NOT frequent AND exon present in biologically relevant transcript(s):
    - Variant removes >10% of protein → **PVS1_Strong**
    - Variant removes <10% of protein → **PVS1_Moderate**
- Truncated/altered region critical to protein function → **PVS1_Strong**

### GC→AG ±1,2 Splice Sites (Introns 45 & 48)

- Variant improves the donor site (i.e., creates a GT donor site) → **N/A**

### Deletions

**Full gene deletion:** → **PVS1** (see note below)

**Single to multi-exon deletion or inversion:**
- Disrupts reading frame AND predicted to undergo NMD:
  - Exon present in biologically relevant transcript(s) → **PVS1**
- Preserves reading frame:
  - Variant removes >10% of protein → **PVS1_Strong**
  - Variant removes <10% of protein → **PVS1_Moderate**

*Note: Exon 1 is an exception; intronic variants in this exon are not LoF (PMID: 36174334)*

### Duplications

*(≥1 exon in size and must be completely contained within gene)*

**Proven in tandem** (WGS, junctional PCR, sequencing of entire gene, orientation notwithstanding):
- Reading frame disrupted AND NMD predicted → **PVS1**
- No or unknown impact on reading frame and NMD → **N/A**

**Presumed in tandem** (MLPA, qPCR, exome depth, CNV analysis, WES):
- Reading frame presumed disrupted AND NMD predicted → **PVS1_Strong**
- Duplication extends beyond ABCA4 → **N/A**

### Initiation Codon Variants

- No known alternative start codon in other transcripts:
  - ≥1 pathogenic variant(s) upstream of closest potential in-frame start codon → **PVS1**

*Note: Next in-frame start codon at 61. At least 44 P/LP variants in ClinVar upstream of p.61*

### RNA Splicing Data

**No variant-specific observed impact for silent/intronic alterations:**
- SpliceAI delta score ≤0.1 → **BP7_Strong**

**Variant-specific impact shown by assay compared to control (for all coding and non-coding variants):**
- Complete loss of protein (no evidence of normal spliced mRNA) → **PVS1***
- Near complete loss of protein (some evidence of normal spliced mRNA) → **PVS1_Strong***

*\* Additional specifications may apply based on Walker et al. 2023 (PMID: 37352859)*

---

## References

### Primary Guidelines

1. Richards S, Aziz N, Bale S, et al. (2015). Standards and guidelines for the interpretation of sequence variants: a joint consensus recommendation of the American College of Medical Genetics and Genomics and the Association for Molecular Pathology. *Genet Med.* 17(5):405-424. **PMID: 25741868**

2. Tavtigian SV, Harrison SM, Boucher KM, Biesecker LG. (2020). Fitting a naturally scaled point system to the ACMG/AMP variant classification guidelines. *Hum Mutat.* 41(10):1734-1737. **PMID: 32720330**

### ABCA4-Specific References

3. Cornelis SS, Runhart EH, et al. (2022). Personalized genetic counseling for Stargardt disease: Offspring risk estimates based on variant severity. *Am J Hum Genet.* 109(3):498-507. **PMID: 35120629**

4. Walker CE, et al. (2023). Using RNA sequencing to evaluate ABCA4 variants of uncertain significance. *Genet Med.* 25(8):100890. **PMID: 37352859**

### ClinGen Resources

5. Brnich SE, et al. (2018). Recommendations for application of the functional evidence PS3/BS3 criterion using the ACMG/AMP sequence variant interpretation framework. *Genome Med.* 10(1):17. **PMID: 29543229**

6. Abou Tayoun AN, et al. (2018). Recommendations for interpreting the loss of function PVS1 ACMG/AMP variant criterion. *Hum Mutat.* 39(11):1517-1524. **PMID: 30192042**

### Computational Prediction Thresholds

7. Pejaver V, et al. (2022). Calibration of computational tools for missense variant pathogenicity classification and ClinGen recommendations for PP3/BP4 criteria. *Am J Hum Genet.* 109(12):2163-2177. **PMID: 36413997**

8. CADD and REVEL threshold specifications: https://www.medrxiv.org/content/10.1101/2023.04.24.23288782v1

9. SpliceAI validation: **PMID: 40225145**

---

## Document Information

**Prepared by:** ClinGen ABCA4 Variant Curation Expert Panel
**Version:** 1.0.0
**Release Date:** November 14, 2025
**Last Updated:** January 2026

**Disclaimer:** These guidelines represent the expert consensus of the ClinGen ABCA4 VCEP and should be used in conjunction with clinical judgment. Variant interpretation should consider the totality of evidence and the specific clinical context.

---

*For questions or updates regarding these guidelines, please contact the ClinGen ABCA4 VCEP through the ClinGen website.*
