# ClinGen Glaucoma Expert Panel Variant Interpretation Guidelines for MYOC

**Version:** 2.1.0
**Released:** 11/6/2025
**Affiliation:** Glaucoma VCEP
**Based on:** Tavtigian et al., 2020 - Bayesian adaptation of Richards et al., 2015 ACMG/AMP Guidelines

---

## Gene Information

| Attribute | Value |
|-----------|-------|
| **Gene** | MYOC (HGNC:7610) |
| **HGNC Name** | myocilin |
| **Transcript** | NM_000261.1 |
| **Disease** | open-angle glaucoma (MONDO:0005338) |
| **Inheritance** | Autosomal dominant inheritance |

---

## Release Notes

**Version 2.1.0 - Minor changes:**
1. Added additional combinations to reach PM5_Strong
2. Updated the Rules combining criteria to reflect the point system approved
3. Clarified that stability assays also included part of PS3/BS3 and uploaded functional data previously assessed

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

**Original ACMG Summary:** Null variant (nonsense, frameshift, canonical ±1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.

**VCEP Specifications:**

**Status:** ❌ **NOT APPLICABLE**

**Comment:** MYOC variants cause JOAG/POAG through a **gain of function (GoF)** disease mechanism and **not loss of function (LoF)**. Truncating variants in exon 3 are expected to be pathogenic because they escape nonsense-mediated decay.

**Modification Type:** N/A

---

### PS1 - Same Amino Acid Change

**Original ACMG Summary:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.

**Example:** Val→Leu caused by either G>C or G>T in the same codon.

**Caveat:** Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:**
- The novel change must **not affect splicing** (SpliceAI ≤ 0.2)
- The combination of PP3 and PS1 should not be higher than **6 points**

#### Strength Levels

| Strength | Criteria | Point Value |
|----------|----------|-------------|
| **Strong** | Same amino acid change as previously established pathogenic variant | 4 |
| **Moderate** | Same amino acid change as a previously established likely pathogenic variant | 2 |

**Modification Type:** Clarification (Moderate also includes Strength modification)

---

### PS2 - De Novo (Confirmed)

**Original ACMG Summary:** De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.

**Note:** Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.

**VCEP Specifications:**

PS2 and PM6 have been combined under PS2. See Table 3 for point system. The proposed SVI point recommendations for:
- **"Phenotype consistent with gene but not highly specific"** applies to **JOAG**
- **"Phenotype consistent with the gene but not highly specific and with high genetic heterogeneity"** applies to **POAG**

**Requirements:**
- Both maternity and paternity need to be proven for confirmed de novo variants
- Parents need to be clinically assessed and not have a diagnosis of glaucoma (If a parent has suspicious signs of glaucoma, the age and the severity of the symptoms should be taken into account before applying criteria)

#### PS2/PM6 Point System (Table 3)

**Points per Proband:**

| Phenotype | Confirmed de novo | Assumed de novo |
|-----------|-------------------|-----------------|
| **JOAG** | 1 | 0.5 |
| **POAG** | 0.5 | 0.25 |

**Evidence Strength Thresholds:**

| Points | Strength Level | Color Code |
|--------|----------------|------------|
| 0.5 | PS2_Supporting | Green |
| 1 | PS2_Moderate | Orange |
| 2 | PS2 (Strong) | Red |
| 4 | PS2_VeryStrong | Dark Red |

#### Strength Levels

| Strength | Criteria | Point Value |
|----------|----------|-------------|
| **Strong** | ≥2 confirmed de novo in JOAG | 4 |
| **Moderate** | ≥2 confirmed de novo in POAG<br>OR 1 confirmed de novo in JOAG<br>OR ≥2 assumed de novo in JOAG | 2 |
| **Supporting** | 1 confirmed de novo in POAG<br>OR ≥2 assumed de novo in POAG<br>OR 1 assumed de novo in JOAG | 1 |

**Modification Type:** Disease-specific (Moderate and Supporting also include Strength modification)

---

### PS3 - Functional Studies

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.

**Note:** Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.

**VCEP Specifications:**

The mechanism by which the variants cause POAG is a **GoF mechanism with accumulation of insoluble aggregates inside the endoplasmic reticulum of the trabecular meshwork cells**. Follow the SVI recommendations from Brnich et al. when assessing functional assays to apply PS3 toward functional evidence.

**Applicable Functional Studies:**
- Stability, solubility or secretion assays
- Animal models that replicate the glaucoma phenotype

**Requirements:**
- PS3 should only be applied if the assay includes both **negative and positive controls** and includes **technical and/or biological replicates**
- If multiple results from functional assays are available for a single variant, then the evidence from the assay that is **best validated** should apply
- Controls from the same general class of assay can be **combined to calculate the odds of pathogenicity (OddsPath)** as per the published SVI recommendations
- If results from different assays are conflicting for a single variant, then the level of validation of each assay should be considered to decide whether the results from one assay can override the results from another

**Note:** The characteristics of each study reviewed, the summary of the assays combined, validation controls, OddsPath and recommendations and classification of variants with functional data are detailed in Tables 1 & 2.

#### Strength Levels

| Strength | Criteria | Point Value |
|----------|----------|-------------|
| **Strong** | Assays with OddsPath >18.7 as per the SVI recommendations | 4 |
| **Moderate** | Assays with OddsPath >4.3 as per the SVI recommendations | 2 |
| **Supporting** | Assays with OddsPath >2.1 as per the SVI recommendations | 1 |

**Modification Type:** Disease-specific, Gene-specific (Moderate and Supporting also include Strength modification)

---

### PS4 - Prevalence in Affected

**Original ACMG Summary:** The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.

**Note 1:** Relative risk (RR) or odds ratio (OR), as obtained from case-control studies, is >5.0 and the confidence interval around the estimate of RR or OR does not include 1.0.

**Note 2:** In instances of very rare variants where case-control studies may not reach statistical significance, the prior observation of the variant in multiple unrelated patients with the same phenotype, and its absence in controls, may be used as moderate level of evidence.

**VCEP Specifications:**

Case-control data for MYOC variants is limited due to control cohorts often being too small to reflect the true prevalence of variants in a true control population. Instead, the Glaucoma VCEP recommends using PS4 for **counting probands from multiple independent studies** using a "quasi case-control study" approach.

**Requirements:**
- Probands need to be clinically assessed and have **JOAG or POAG**
- **PM2 needs to be met** (due to incomplete penetrance, late age of onset of glaucoma and the rate of undiagnosed glaucoma in the general population, pathogenic variants may be present in population databases)
- Individuals with multiple MYOC VUS/LP/P variants cannot be considered as evidence of either variant

#### Strength Levels

| Strength | Criteria | Point Value |
|----------|----------|-------------|
| **Strong** | ≥ 15 probands from multiple independent studies | 4 |
| **Moderate** | ≥ 6 probands from multiple independent studies | 2 |
| **Supporting** | ≥ 2 probands from multiple independent studies | 1 |

**Modification Type:** Gene-specific (Moderate and Supporting also include Strength modification)

---

### PM1 - Mutational Hot Spot

**Original ACMG Summary:** Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.

**Status:** ❌ **NOT APPLICABLE**

**Comment:** MYOC has no mutational hot spot and benign variants are present though the well-characterised olfactomedin domain in exon 3.

---

### PM2 - Absent from Controls

**Original ACMG Summary:** Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

**Caveat:** Population data for indels may be poorly called by next generation sequencing.

**VCEP Specifications:**

- The **highest allele frequency in population databases** should be used
- Only applies to populations of **≥ 10,000 alleles**
- PM2 should be used at a **Supporting level** as per the SVI recommendations
- The filtering allele frequency for PM2 was set **one order of magnitude lower than BS1**. This is a conservative approach: some pathogenic variants are expected to be present in population databases due to POAG being a complex disease with late onset and age-related penetrance. Moreover, most MYOC pathogenic variants are absent from large population databases.

#### Strength Levels

| Strength | Criteria | Point Value |
|----------|----------|-------------|
| **Supporting** | Allele frequency ≤ 0.0001 in population databases | 1 |

**Modification Type:** Disease-specific, Gene-specific

---

### PM3 - In Trans with Pathogenic

**Original ACMG Summary:** For recessive disorders, detected in trans with a pathogenic variant.

**Note:** This requires testing of parents (or offspring) to determine phase.

**Status:** ❌ **NOT APPLICABLE**

**Comment:** MYOC variants have an autosomal dominant mode of inheritance.

---

### PM4 - Protein Length Changes

**Original ACMG Summary:** Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

**VCEP Specifications:**

The disease mechanism for MYOC variants is **GoF, not LoF**. Therefore, PM4 is used **instead of PVS1** for truncating variants in the olfactomedin domain. One stop-loss variant has been reported in MYOC.

There are only four in-frame variants reported in the MYOC database. There is a lack of current data to support a benign/pathogenic classification of in-frame del/ins.

#### Strength Levels

| Strength | Criteria | Point Value |
|----------|----------|-------------|
| **Moderate** | In-frame del/ins, stop-loss variants and truncating variants involving **>10% of the protein** and located within the conserved olfactomedin domain (AA 246-502) | 2 |
| **Supporting** | In-frame del/ins, stop-loss variants and truncating variants involving **≤10% of the protein** and located within the conserved olfactomedin domain (AA 246-502) | 1 |

**Modification Type:** Gene-specific (Supporting also includes Strength modification)

---

### PM5 - Novel Missense at Same Residue

**Original ACMG Summary:** Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.

**Example:** Arg156His is pathogenic; now you observe Arg156Cys.

**Caveat:** Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:**

- The novel change must **not affect splicing** (SpliceAI ≤ 0.2) and must **meet PP3**
- The novel change must have a **Grantham score equal or greater than** the previously established pathogenic or likely pathogenic variant
- The combination of PP3 and PM5 should not be higher than **5 points**

#### Strength Levels

| Strength | Criteria | Point Value |
|----------|----------|-------------|
| **Strong** | Same residue as 2 previously established pathogenic variants<br>OR 1 previously established pathogenic and 2 likely pathogenic variants<br>OR 4 previously established likely pathogenic variants<br>(all assessed independently of PM5) | 4 |
| **Moderate** | Same residue as a previously established pathogenic variant (assessed independently of PM5)<br>OR 2 previously established likely pathogenic variants (both assessed independently of PM5) | 2 |
| **Supporting** | Same residue as a previously established likely pathogenic variant (assessed independently of PM5) | 1 |

**Modification Type:** Clarification (Strong and Supporting also include Strength modification)

---

### PM6 - De Novo (Assumed)

**Original ACMG Summary:** Assumed de novo, but without confirmation of paternity and maternity.

**Status:** ❌ **NOT APPLICABLE**

**Comment:** Refer to PS2. PS2 and PM6 have been combined under PS2 using the point-based system.

---

### PP1 - Co-segregation

**Original ACMG Summary:** Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.

**Note:** May be used as stronger evidence with increasing segregation data.

**VCEP Specifications:**

- **BA1 and BS1 must not be met**
- Multiple families are jointly considered by **adding the informative meioses across families** according to Kelly et al.
- Only **genotype positive/phenotype positive** and **obligate carriers/phenotype positive** individuals should be counted as segregations
- Individuals who are genotype positive/phenotype negative and individuals who are genotype negative/phenotype negative should **not be counted**
- Phenotype positive need to be clinically assessed and either have a **diagnosis of glaucoma or suspicious signs of glaucoma**
- **Do not apply Strong level of evidence** if the variant is present in a single family due to risk of other variant in linkage disequilibrium

#### Strength Levels

| Strength | Criteria | Point Value |
|----------|----------|-------------|
| **Strong** | ≥7 meioses in >1 family | 4 |
| **Moderate** | ≥ 5 meioses regardless of the number of families | 2 |
| **Supporting** | ≥ 3 meioses regardless of the number of families | 1 |

**Modification Type:** Clarification, Strength

---

### PP2 - Missense in Constrained Gene

**Original ACMG Summary:** Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.

**Status:** ❌ **NOT APPLICABLE**

**Comment:** Although pathogenic missense variants are common in MYOC, the gene also has a significant amount of benign missense variants as shown by the **missense constraint z score in gnomAD (z = 0.52)** supporting tolerance to variation.

---

### PP3 - Computational Evidence

**Original ACMG Summary:** Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).

**Caveat:** As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.

**VCEP Specifications:**

- The combination of PP3 and PM5 should not be higher than **5 points**
- The combination of PP3 and PS1 should not be higher than **6 points**

Pejaver et al. estimated thresholds for different strength of evidence for computational predictors and recommended using one that reaches a strong level of evidence for pathogenicity and moderate for benignity. The Glaucoma VCEP recommended using **only one in silico predictor**, in line with a recent study showing a lower rate of concordance when multiple software are used.

The Glaucoma VCEP piloted the 4 predictors recommended by Pejaver et al. (REVEL, VEST4, BayesDel2 and MutPred2) on previously established LB/B and LP/P variants by the Glaucoma VCEP. Of the 4 tools, **REVEL had the highest sensitivity** (PP3 was applied to 95.2% (20/21) of LP/P variants) and the lowest specificity (BP4 was applied to 45.0% (9/20) of LB/B variants). Therefore the VCEP recommends using **REVEL** based on its ease of access, high level of accuracy toward variant pathogenicity and more conservative predictions toward benign impact in the context of MYOC variants.

Based on the disease mechanism (GoF), the fact that all pathogenic variants are located in the last exon of the gene and the absence of current evidence supporting splicing as having a deleterious impact, the Glaucoma VCEP **does not recommend using SpliceAI for PP3**.

#### Strength Levels

| Strength | Criteria | Point Value |
|----------|----------|-------------|
| **Strong** | REVEL score of **≥ 0.932** | 4 |
| **Moderate** | REVEL score of **0.773-0.931** | 2 |
| **Supporting** | REVEL score of **0.644-0.772** | 1 |

**Modification Type:** Clarification, Strength

---

### PP4 - Phenotype Specificity

**Original ACMG Summary:** Patient's phenotype or family history is highly specific for a disease with a single genetic etiology.

**Status:** ❌ **NOT APPLICABLE**

**Comment:** The phenotype associated with MYOC variants is not highly specific and there is genetic heterogeneity.

---

### PP5 - Reputable Source

**Original ACMG Summary:** Reputable source recently reports variant as pathogenic, but the evidence is not available to the laboratory to perform an independent evaluation.

**Status:** ❌ **NOT APPLICABLE**

**Comment:** This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PubMed: 29543229).

---

## Benign Criteria

### BA1 - Allele Frequency >5%

**Original ACMG Summary:** Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

**VCEP Specifications:**

- The **highest allele frequency in population databases** should be used
- Variant must be present in **≥ 5 alleles** in any validated general continental population dataset of at least 2,000 observed alleles

The Whiffin/Ware calculator was used to obtain a population allele frequency threshold for BA1 using conservative figures:
- The prevalence of POAG in the African population, which is the highest among all populations, was used **(1/24)**
- The maximum allelic contribution for the most common MYOC variant (p.Gln368Ter) was set at **2.6%** using data from large disease registries (the Australian and New Zealand of Advanced Glaucoma and the Glaucoma Inheritance Study in Tasmania with data on over 3,236 individuals)
- A conservative estimate for the penetrance at **7.6%** was used based on the penetrance of p.Gln368Ter in a population-based study using data from the UK biobank
- The maximum credible allele frequency calculated was **0.007**, which was rounded up to **0.01**

#### Strength Level

| Strength | Criteria | Point Value |
|----------|----------|-------------|
| **Stand Alone** | Allele frequency **≥ 0.01** in population databases | N/A |

**Modification Type:** Disease-specific, Gene-specific

---

### BS1 - Frequency Greater Than Expected

**Original ACMG Summary:** Allele frequency is greater than expected for disorder.

**VCEP Specifications:**

- The **highest allele frequency in population databases** should be used
- Variant must be present in **≥ 5 alleles** in any validated general continental population dataset of at least 2,000 observed alleles
- **Does not apply to p.Gln368Ter**

The Whiffin/Ware calculator was used to obtain a population allele frequency threshold for BS1 using a more realistic estimate of the penetrance:
- The prevalence of POAG and the maximum allelic contribution used were the same as for BA1
- A penetrance at **56%** was used based on the penetrance of p.Gln368Ter in family-based studies using data from the Australian and New Zealand of Advanced Glaucoma and the Glaucoma Inheritance Study in Tasmania
- The maximum credible allele frequency calculated was **0.001**

**Exemption:** An exemption was applied to **p.Gln368Ter**. MYOC p.Gln368Ter is a well-established pathogenic variant but displays incomplete penetrance. Its allele frequency in gnomAD is 0.001588 in European Non-Finnish, 0.003344 in European Finnish, and is 0.0025 in the UKBB. Evidence supports a European founder effect.

#### Strength Level

| Strength | Criteria | Point Value |
|----------|----------|-------------|
| **Strong** | Allele frequency **≥ 0.001** in population databases | -4 |

**Modification Type:** Disease-specific, Gene-specific

---

### BS2 - Observed in Healthy Adult

**Original ACMG Summary:** Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

**Status:** ❌ **NOT APPLICABLE**

**Comment:** MYOC variants have an incomplete penetrance and late age of onset.

---

### BS3 - Functional Studies (No Effect)

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

**VCEP Specifications:**

BS3 at a Moderate or Supporting level applies to variants showing solubility or secretion in functional assays for studies with OddsPath as per the published SVI recommendations.

**Requirements:**
- Only apply if the assay includes both **negative and positive controls** and includes **technical and/or biological replicates**
- If multiple results from functional assays are available for a single variant, then the evidence from the assay that is **best validated** should apply
- Controls from the same general class of assay can be **combined to calculate the odds of pathogenicity (OddsPath)** as per the published SVI recommendations
- If results from different assays are conflicting for a single variant, then the level of validation of each assay should be considered to decide whether the results from one assay can override the results from another

#### Strength Levels

| Strength | Criteria | Point Value |
|----------|----------|-------------|
| **Moderate** | Applies to variants showing solubility or secretion in functional assays for studies with OddsPath **<0.23** as per the SVI recommendations | -2 |
| **Supporting** | Applies to variants showing solubility or secretion in functional assays for studies with OddsPath **<0.48** as per the SVI recommendations | -1 |

**Modification Type:** Gene-specific, Strength

---

### BS4 - Lack of Segregation

**Original ACMG Summary:** Lack of segregation in affected members of a family.

**Caveat:** The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.

**Status:** ❌ **NOT APPLICABLE**

**Comment:** The presence of phenocopies, the reduced age-related penetrance and the possibility that more than one pathogenic variant can contribute to the phenotype observed in families make non-segregation difficult to assess in the context of MYOC and POAG.

---

### BP1-BP7 - Benign Supporting

| Criterion | Status | Comment |
|-----------|--------|---------|
| **BP1** | ❌ Not Applicable | Both truncating and missense MYOC variants are causative |
| **BP2** | ❌ Not Applicable | Biallelic variants (either compound heterozygotes or homozygotes) have been reported (with variable phenotype) and are not incompatible with life. Two missense variants in cis could act synergistically or the effect of a variant occurring after a truncating variant may not be predicted |
| **BP3** | ❌ Not Applicable | MYOC does not have a repetitive region without a known function |
| **BP4** | ✅ Applicable | Multiple lines of computational evidence suggest no impact on gene or gene product |
| **BP5** | ❌ Not Applicable | Multiple molecular diagnoses are possible and variants in different genes could have an additive effect |
| **BP6** | ❌ Not Applicable | This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PubMed: 29543229) |
| **BP7** | ✅ Applicable | A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved |

#### BP4 - Computational Evidence (No Impact)

**VCEP Specifications:**

Similar to PP3, The Glaucoma VCEP decided to follow the SVI recommendations to apply the REVEL thresholds calculated for the different levels of evidence.

MYOC which only has 3 exons, one transcript and for which splicing is not known to vary. Based on the disease mechanism and the absence of current evidence supporting pathogenicity of intronic/noncoding variants, the Glaucoma VCEP agreed to apply BP4 to noncoding variants using SpliceAI.

| Strength | Criteria | Point Value |
|----------|----------|-------------|
| **Strong** | REVEL score of **≤ 0.016** | -4 |
| **Moderate** | REVEL score of **0.017-0.183** | -2 |
| **Supporting** | For missense variants: REVEL score of **0.184-0.290**<br>For all other variants located outside of donor/acceptor ±1,2 dinucleotide positions, when splicing assay is not available: SpliceAI **≤ 0.1** | -1 |

**Modification Type:** Clarification, Strength

#### BP7 - Synonymous (No Splice Impact)

| Strength | Criteria | Point Value |
|----------|----------|-------------|
| **Supporting** | Apply to intronic/noncoding and synonymous (silent) exonic variants if BP4 is met | -1 |

**Modification Type:** Clarification

---

## Rules for Combining Criteria

### Point-Based Classification System

This VCEP uses a **point-based variant classification system** following the Tavtigian et al., 2020 Bayesian adaptation of the ACMG/AMP guidelines.

#### Classification Categories

| Category | Point Ranges |
|----------|--------------|
| **Pathogenic** | ≥10 |
| **Likely Pathogenic** | 6 - 9 |
| **Uncertain Significance** | -1 to 5 |
| **Likely Benign** | -6 to -2 |
| **Benign** | ≤-7 |

### Pathogenic Classification (≥10 points)

Variants are classified as **Pathogenic** when the total points from applicable criteria reach **≥10**.

**Example combinations:**
- PS1 (4) + PS3_Strong (4) + PP3_Moderate (2) = 10 points
- PS4_Strong (4) + PS2_Strong (4) + PP3_Moderate (2) = 10 points
- PM5_Strong (4) + PS3_Moderate (2) + PS4_Moderate (2) + PP3_Moderate (2) = 10 points

### Likely Pathogenic Classification (6-9 points)

Variants are classified as **Likely Pathogenic** when the total points from applicable criteria reach **6-9**.

**Example combinations:**
- PS1_Strong (4) + PP3_Moderate (2) = 6 points
- PS3_Moderate (2) + PM4_Moderate (2) + PP3_Moderate (2) = 6 points
- PS4_Moderate (2) + PM5_Moderate (2) + PP1_Moderate (2) = 6 points

### Uncertain Significance Classification (-1 to 5 points)

Variants are classified as **Uncertain Significance (VUS)** when the total points from applicable criteria fall in the range **-1 to 5**.

### Likely Benign Classification (-6 to -2 points)

Variants are classified as **Likely Benign** when the total points from applicable criteria reach **-6 to -2**.

**Example combinations:**
- BP4_Strong (-4) + BP7_Supporting (-1) + PM2 not met = -5 points
- BS3_Moderate (-2) + BP4_Moderate (-2) = -4 points

### Benign Classification (≤-7 points or BA1)

Variants are classified as **Benign** when:
- Total points from applicable criteria reach **≤-7**, OR
- **BA1 is met** (stand-alone criterion)

**Example combinations:**
- BS1_Strong (-4) + BP4_Strong (-4) = -8 points
- BA1 (stand-alone) = Benign

---

## Appendices

### Appendix A: Key Considerations for MYOC Variant Interpretation

#### Disease Mechanism
- MYOC variants cause JOAG/POAG through a **gain of function (GoF)** mechanism
- Pathogenic variants lead to **accumulation of insoluble aggregates inside the endoplasmic reticulum** of trabecular meshwork cells
- **Not a loss of function (LoF)** mechanism - therefore PVS1 is not applicable
- Truncating variants in **exon 3** are expected to be pathogenic because they **escape nonsense-mediated decay**

#### Protein Structure
- **Olfactomedin domain:** AA 246-502 (conserved functional domain in exon 3)
- Most pathogenic variants are located in the olfactomedin domain
- No mutational hot spot identified
- Benign variants are present throughout the olfactomedin domain

#### Penetrance and Prevalence
- **Incomplete penetrance** - not all individuals with pathogenic variants develop glaucoma
- **Late age of onset** - disease typically manifests in adulthood
- **Age-related penetrance** - risk increases with age
- Most common pathogenic variant: **p.Gln368Ter**
  - Penetrance: ~56% in family studies, ~7.6% in population studies
  - European founder effect identified
  - Exempted from BS1 criterion

#### Population Frequency Considerations
- Pathogenic variants may be present in population databases due to:
  - Incomplete penetrance
  - Late age of onset
  - Undiagnosed glaucoma in the general population
- Conservative thresholds have been established using Whiffin/Ware calculator

#### Phenotype Considerations
- **JOAG (Juvenile-Onset Open-Angle Glaucoma):** Earlier onset, more consistent with gene
- **POAG (Primary Open-Angle Glaucoma):** Later onset, high genetic heterogeneity
- Different point values for PS2 based on phenotype (see Table 3)

### Appendix B: Population Frequency Thresholds Summary

| Criterion | Threshold | Strength | Calculation Basis |
|-----------|-----------|----------|-------------------|
| **BA1** | ≥ 0.01 (1%) | Stand Alone | Conservative penetrance (7.6%), prevalence 1/24, max allelic contribution 2.6% |
| **BS1** | ≥ 0.001 (0.1%) | Strong | Realistic penetrance (56%), prevalence 1/24, max allelic contribution 2.6% |
| **PM2** | ≤ 0.0001 (0.01%) | Supporting | One order of magnitude lower than BS1 |

**Requirements for all frequency criteria:**
- Use **highest allele frequency** (popmax) in population databases
- Only apply to populations of **≥ 10,000 alleles**
- Variant must be present in **≥ 5 alleles** (for BA1/BS1)

**Exception:** BS1 does not apply to p.Gln368Ter

### Appendix C: Computational Predictor - REVEL

**Why REVEL was selected:**
- Highest sensitivity (95.2% for LP/P variants)
- Ease of access
- High accuracy for pathogenicity prediction
- More conservative for benign predictions in MYOC context
- Outperformed VEST4, BayesDel2, and MutPred2 in VCEP pilot study

**REVEL Thresholds:**

| Score Range | PP3 Classification | BP4 Classification |
|-------------|-------------------|-------------------|
| ≥ 0.932 | PP3_Strong (4 pts) | - |
| 0.773-0.931 | PP3_Moderate (2 pts) | - |
| 0.644-0.772 | PP3_Supporting (1 pt) | - |
| 0.291-0.643 | Neither PP3 nor BP4 | Neither PP3 nor BP4 |
| 0.184-0.290 | - | BP4_Supporting (-1 pt) |
| 0.017-0.183 | - | BP4_Moderate (-2 pts) |
| ≤ 0.016 | - | BP4_Strong (-4 pts) |

**SpliceAI:**
- **Not recommended for PP3** (all pathogenic variants in last exon; no splicing impact expected)
- **Can be used for BP4:** SpliceAI ≤ 0.1 for noncoding variants (BP4_Supporting, -1 pt)
- **Used for PS1/PM5:** Novel change must not affect splicing (SpliceAI ≤ 0.2)

### Appendix D: Functional Evidence Guidelines

**Acceptable Assay Types:**
1. **Stability assays**
2. **Solubility assays**
3. **Secretion assays**
4. **Animal models** that replicate the glaucoma phenotype

**Minimum Requirements:**
- Both **positive and negative controls**
- **Technical and/or biological replicates**
- Validation data demonstrating reproducibility

**Calculating Evidence Strength:**

Use **OddsPath** (Odds of Pathogenicity) as per SVI recommendations:

| OddsPath | PS3/BS3 Strength |
|----------|------------------|
| >18.7 | PS3_Strong (4 pts) |
| >4.3 to ≤18.7 | PS3_Moderate (2 pts) |
| >2.1 to ≤4.3 | PS3_Supporting (1 pt) |
| 0.48 to 2.1 | Not applicable |
| <0.48 to ≥0.23 | BS3_Supporting (-1 pt) |
| <0.23 | BS3_Moderate (-2 pts) |

**Handling Multiple Assays:**
- If multiple assays available for a variant, use the **best validated** assay
- Controls from the **same general class** can be combined to calculate OddsPath
- If assays conflict, consider **level of validation** to determine which result to use

**Note:** Detailed functional data with OddsPath calculations are available in Tables 1 & 2 of the full VCEP specification.

### Appendix E: Segregation Analysis (PP1)

**Counting Meioses:**
- Multiple families can be jointly considered by **adding informative meioses across families**
- Count only:
  - **Genotype positive/phenotype positive** individuals
  - **Obligate carriers/phenotype positive** individuals
- **Do not count:**
  - Genotype positive/phenotype negative individuals
  - Genotype negative/phenotype negative individuals

**Phenotype Requirements:**
- Individuals must be **clinically assessed**
- Must have either:
  - **Diagnosis of glaucoma**, OR
  - **Suspicious signs of glaucoma**

**Restrictions:**
- **BA1 and BS1 must not be met** before applying PP1
- **Do not apply Strong level** (≥7 meioses) if variant present in only **one family** (risk of linkage disequilibrium)

**Strength Thresholds:**

| Meioses | Families | Strength | Points |
|---------|----------|----------|--------|
| ≥7 | >1 | Strong | 4 |
| ≥5 | Any | Moderate | 2 |
| ≥3 | Any | Supporting | 1 |

### Appendix F: Point Combination Constraints

**Maximum Point Caps:**

1. **PP3 + PS1 ≤ 6 points**
   - Example: PP3_Strong (4) + PS1_Strong (4) = 8 points → **Capped at 6 points**
   - If both criteria met at max strength, reduce PP3 to PP3_Moderate

2. **PP3 + PM5 ≤ 5 points**
   - Example: PP3_Strong (4) + PM5_Moderate (2) = 6 points → **Capped at 5 points**
   - If both criteria met at max strength, reduce PP3 to PP3_Supporting

**Rationale:** These caps prevent over-counting evidence when criteria are based on related evidence types.

### Appendix E: References

1. Brnich SE, Abou Tayoun AN, et al. Recommendations for application of the functional evidence PS3/BS3 criterion using the ACMG/AMP sequence variant interpretation framework. Genome Med. 2019;12(1):3. PMID: 31892348

2. Caballero M, Borrás T. Inefficient processing of an olfactomedin-deficient myocilin mutant: potential physiological relevance to glaucoma. Biochem Biophys Res Commun. 2001;282(3):662-70. PMID: 11401512

3. Liu Y, Vollrath D. Reversal of mutant myocilin non-secretion and cell killing: implications for glaucoma. Hum Mol Genet. 2004;13(11):1193-204. PMID: 15069026

4. Collantes ERA, Delfin MS, et al. EFEMP1 rare variants cause familial juvenile-onset open-angle glaucoma. Hum Mutat. 2022;43(2):240-252. PMID: 34923728

5. Alward WL, Kwon YH, et al. Variations in the myocilin gene in patients with open-angle glaucoma. Arch Ophthalmol. 2002;120(9):1189-97. PMID: 12215093

6. Kelly MA, Caleshu C, et al. Adaptation and validation of the ACMG/AMP variant classification framework for MYH7-associated inherited cardiomyopathies: recommendations by ClinGen's Inherited Cardiomyopathy Expert Panel. Genet Med. 2018;20(3):351-359. PMID: 29300372

7. Pejaver V, Byrne AB, et al. Calibration of computational tools for missense variant pathogenicity classification and ClinGen recommendations for PP3/BP4 criteria. Am J Hum Genet. 2022;109(12):2163-2177. PMID: 36413997

8. Ghosh R, Oak N, et al. Evaluation of in silico algorithms for use with ACMG/AMP clinical variant interpretation guidelines. Genome Biol. 2017;18(1):225. PMID: 29179779

9. Tian Y, Pesaran T, et al. REVEL and BayesDel outperform other in silico meta-predictors for clinical variant classification. Sci Rep. 2019;9(1):12752. PMID: 31484976

10. Whiffin N, Minikel E, et al. Using high-resolution variant frequencies to empower clinical genome interpretation. Genet Med. 2017;19(10):1151-1158. PMID: 28518168

11. Tham YC, Li X, et al. Global prevalence of glaucoma and projections of glaucoma burden through 2040: a systematic review and meta-analysis. Ophthalmology. 2014;121(11):2081-90. PMID: 24974815

12. Quigley HA, Broman AT. The number of people with glaucoma worldwide in 2010 and 2020. Br J Ophthalmol. 2006;90(3):262-7. PMID: 16488940

13. Souzeau E, Burdon KP, et al. Higher prevalence of myocilin mutations in advanced glaucoma in comparison with less advanced disease in an Australasian disease registry. Ophthalmology. 2013;120(6):1135-43. PMID: 23453510

14. Han X, Souzeau E, et al. Myocilin Gene Gln368Ter Variant Penetrance and Association With Glaucoma in Population-Based and Registry-Based Studies. JAMA Ophthalmol. 2019;137(1):28-35. PMID: 30267046

15. Baird PN, Craig JE, et al. Analysis of 15 primary open-angle glaucoma families from Australia identifies a founder effect for the Q368STOP mutation of myocilin. Hum Genet. 2003;112(2):110-6. PMID: 12522550

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| **2.1.0** | 11/6/2025 | 1. Added additional combinations to reach PM5_Strong<br>2. Updated the Rules combining criteria to reflect the point system approved<br>3. Clarified that stability assays also included part of PS3/BS3 and uploaded functional data previously assessed |

---

*This document was compiled from ClinGen VCEP specifications. For the most current version and additional resources, please refer to the [ClinGen website](https://clinicalgenome.org/).*

**Document generated:** February 6, 2026
**Based on:** ClinGen_ACMG_Specifications_MYOC_v2.1.0.pdf
