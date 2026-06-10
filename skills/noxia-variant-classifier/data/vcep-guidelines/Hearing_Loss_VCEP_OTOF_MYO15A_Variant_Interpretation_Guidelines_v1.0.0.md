# ClinGen Hearing Loss VCEP Variant Interpretation Guidelines for OTOF and MYO15A

**Version:** 1.0.0
**Released:** March 30, 2022
**Affiliation:** Hearing Loss VCEP (ClinGen Hearing Loss Variant Curation Expert Panel)
**Expert Panel Page:** https://www.clinicalgenome.org/affiliation/50007
**Based on:** Richards et al., 2015 ACMG/AMP Guidelines
**Related Publication:** PMID 30311386

---

## Gene Information

| Attribute | OTOF | MYO15A |
|-----------|------|--------|
| **Gene** | OTOF (HGNC:8515) | MYO15A (HGNC:7594) |
| **HGNC Name** | otoferlin | myosin XVA |
| **Transcript** | NM_194248.2 | NM_016239.3 |
| **Disease** | Nonsyndromic genetic hearing loss (MONDO:0019497) | Nonsyndromic genetic deafness (MONDO:0019497) |
| **Inheritance** | Autosomal Recessive | Autosomal Recessive |

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
   - [BA1 - Allele Frequency >0.5%](#ba1---allele-frequency-05)
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

**Original ACMG Summary:** Null variant (nonsense, frameshift, canonical +/−1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.

**VCEP Specifications:**

Null variant in a gene with established LOF as a disease mechanism. See PVS1_Strong, PVS1_Moderate, PVS1_Supporting for reduced evidence applications.

PVS1 should also be considered for both OTOF and MYO15A with variants falling in two exons being exceptions to this rule:
- **OTOF:** NM_194248.2 Exon 46 (c.5841 to c.5994; PMID: 19250381)
- **MYO15A:** NM_016239.3 Exon 8 (c.4033 to c.4038; PMID: 10552926) and Exon 26 (c.5911 to c.5964; PMID: 30096381 and high frequency LOF variant in gnomAD)

#### Strength Levels

| Strength | Criteria |
|----------|----------|
| **Very Strong (PVS1)** | See PVS1 flowchart below. Null variant in gene where LOF is established mechanism of disease. |
| **Strong (PVS1_Strong)** | See PVS1 flowchart for PVS1_Strong variants in gene where LOF is a known mechanism of disease. |
| **Moderate (PVS1_Moderate)** | See PVS1 flowchart for PVS1_Moderate variants in gene where LOF is a known mechanism of disease. |
| **Supporting (PVS1_Supporting)** | See PVS1 flowchart for PVS1_Supporting variants in gene where LOF is a known mechanism of disease. |

#### PVS1 Flowchart Decision Tree

**Nonsense or Frameshift:**
| Scenario | NMD? | Exon in Biologically-Relevant Transcript? | Additional Criteria | Strength |
|----------|------|------------------------------------------|---------------------|----------|
| Predicted to undergo NMD | Yes | Exon present in biologically-relevant transcript(s) | — | PVS1 |
| Predicted to undergo NMD | Yes | Exon absent from biologically-relevant transcript(s) | — | N/A |
| Not predicted to undergo NMD | No | Truncated/altered region critical to protein function | — | PVS1_Strong |
| Not predicted to undergo NMD | No | LoF variants in exon frequent in general population AND/OR exon absent from biologically-relevant transcripts | — | N/A |
| Not predicted to undergo NMD | No | LoF variants NOT frequent; exon present in biologically-relevant transcript(s) | Removes >10% of protein | PVS1_Strong |
| Not predicted to undergo NMD | No | LoF variants NOT frequent; exon present in biologically-relevant transcript(s) | Removes <10% of protein | PVS1_Moderate |

**GT-AG Splice Sites (canonical +/−1,2):**
| Scenario | Reading Frame | Additional Criteria | Strength |
|----------|---------------|---------------------|----------|
| Exon skipping disrupts reading frame, predicted to undergo NMD | Disrupted | Exon present in biologically-relevant transcript(s) | PVS1 |
| Exon skipping disrupts reading frame, predicted to undergo NMD | Disrupted | Exon absent from biologically-relevant transcript(s) | N/A |
| Exon skipping disrupts reading frame, NOT predicted to undergo NMD | Disrupted | Truncated/altered region critical to protein function | PVS1_Strong |
| Exon skipping disrupts reading frame, NOT predicted to undergo NMD | Disrupted | LoF variants frequent in general population AND/OR exon absent | N/A |
| Exon skipping disrupts reading frame, NOT predicted to undergo NMD | Disrupted | LoF variants NOT frequent; exon present | Removes >10% of protein → PVS1_Strong |
| Exon skipping disrupts reading frame, NOT predicted to undergo NMD | Disrupted | LoF variants NOT frequent; exon present | Removes <10% of protein → PVS1_Moderate |
| Exon skipping or cryptic splice site preserves reading frame | Preserved | Truncated/altered region critical to protein function | PVS1_Strong |
| Exon skipping or cryptic splice site preserves reading frame | Preserved | Role of region in protein function unknown; LoF frequent AND/OR exon absent | N/A |
| Exon skipping or cryptic splice site preserves reading frame | Preserved | Role unknown; LoF NOT frequent; exon present | Removes >10% of protein → PVS1_Strong |
| Exon skipping or cryptic splice site preserves reading frame | Preserved | Role unknown; LoF NOT frequent; exon present | Removes <10% of protein → PVS1_Moderate |

**Deletion (Single exon to full gene):**
| Scenario | Additional Criteria | Strength |
|----------|---------------------|----------|
| Full gene deletion | — | PVS1 |
| Single to multi exon deletion – disrupts reading frame, predicted to undergo NMD | Exon present in biologically-relevant transcript(s) | PVS1 |
| Single to multi exon deletion – disrupts reading frame, predicted to undergo NMD | Exon absent from biologically-relevant transcript(s) | N/A |
| Single to multi exon deletion – disrupts reading frame, NOT predicted to undergo NMD | Truncated/altered region critical to protein function | PVS1_Strong |
| Single to multi exon deletion – disrupts reading frame, NOT predicted to undergo NMD | LoF variants frequent AND/OR exon absent from biologically-relevant transcripts | N/A |
| Single to multi exon deletion – disrupts reading frame, NOT predicted to undergo NMD | LoF NOT frequent; exon present; removes >10% of protein | PVS1_Strong |
| Single to multi exon deletion – disrupts reading frame, NOT predicted to undergo NMD | LoF NOT frequent; exon present; removes <10% of protein | PVS1_Moderate |
| Single to multi exon deletion – preserves reading frame | Truncated/altered region critical to protein function | PVS1_Strong |

**Duplication (≥1 exon in size, completely contained within gene):**
| Scenario | Additional Criteria | Strength |
|----------|---------------------|----------|
| Proven in tandem | Reading frame disrupted and NMD predicted | PVS1 |
| Proven in tandem | No or unknown impact on reading frame and NMD | N/A |
| Presumed in tandem | Reading frame presumed disrupted and NMD predicted | PVS1_Strong |
| Proven not in tandem | — | N/A |

**Initiation Codon:**
| Scenario | Additional Criteria | Strength |
|----------|---------------------|----------|
| No known alternative start codon in other transcripts | ≥1 pathogenic variant(s) upstream of closest potential in-frame start codon | PVS1_Moderate |
| No known alternative start codon in other transcripts | No pathogenic variant(s) upstream of closest potential in-frame start codon | PVS1_Supporting |
| Different functional transcript uses alternative start codon | — | N/A |

---

### PS1 - Same Amino Acid Change

**Original ACMG Summary:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | Same amino acid change as an established pathogenic variant; OR splice variants at same nucleotide and with similar impact prediction as previously reported pathogenic variant. |

**Notes:**
- Established variant must meet criteria for pathogenicity by the HL specifications
- Can also use PS1 for splice variants located in the splice consensus sequence, at the same nucleotide position as a previously reported pathogenic variant
  - Example: c.105+1G>C is known to be pathogenic, can use PS1 for c.105+1G>T
- No additional hearing loss specifications for missense variants. Follow recommendations as outlined in Richards 2015 and/or the Sequence Variant Interpretation working group within ClinGen
- **Caveat** (from ACMG/AMP guidelines): Assess the possibility that the variant may act directly through the DNA change (e.g. through splicing disruption as assessed by at least computational analysis) instead of through the amino acid change

---

### PS2 - De Novo (Confirmed)

**Original ACMG Summary:** De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.

**VCEP Specifications:**

- OTOF and MYO15A are associated with autosomal recessive conditions. Therefore, de novo variants are expected to be an unlikely occurrence
- It is recommended that de novo evidence is only awarded when phase with another variant (VUS, Likely Pathogenic, or Pathogenic) can be confirmed in trans. This is to avoid inappropriately awarding de novo evidence, which would lead to potentially incorrect classification
- Follow recommendations as specified by the Sequence Variant Interpretation working group within ClinGen
  - Determine number of points per proband using Table 1 below
  - Sum the total number of points for all probands, and determine the strength of the evidence by using Table 2
  - **Please note: the phenotype for de novo occurrences for MYO15A and OTOF are not considered "highly specific"**

#### Table 1: Points Awarded Per De Novo Occurrence

| Phenotypic Consistency | Confirmed De Novo | Assumed De Novo |
|------------------------|-------------------|-----------------|
| Phenotype highly specific for gene | 2 | 1 |
| Phenotype consistent with gene but not highly specific | 1 | 0.5 |
| Phenotype consistent with gene but not highly specific and high genetic heterogeneity† | 0.5 | 0.25 |
| Phenotype not consistent with gene | 0 | 0 |

†Maximum allowable value of 1 may contribute to overall score.

#### Table 2: PS2/PM6 Evidence Strength Thresholds

| Supporting (PS2_Supporting or PM6_Supporting) | Moderate (PS2_Moderate or PM6) | Strong (PS2 or PM6_Strong) | Very Strong (PS2_VeryStrong or PM6_VeryStrong) |
|-----------------------------------------------|-------------------------------|---------------------------|-----------------------------------------------|
| 0.5 points | 1.0 points | 2.0 points | 4.0 points |

---

### PS3 - Functional Studies

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | Knock-in mouse model demonstrates the phenotype. |
| **Moderate** | Validated functional studies show a deleterious effect (none are defined for OTOF and MYO15A). |
| **Supporting** | Functional studies with limited validation show a deleterious effect. |

**Notes:**
- Recommend that functional evidence, except for a variant-specific mouse model, is **not** used as strong evidence, due to the absence of well-established functional studies for hearing loss genes
- There are no specific assays for OTOF or MYO15A. However, PS3_Supporting can be applied for other functional analyses if:
  - The assay has been validated by a known pathogenic and benign variant **AND**
  - There is plausible reason that the function the assay is testing relates to the phenotype **AND**
  - The assay conditions are likely to mimic the physiological environment

---

### PS4 - Prevalence in Affected

**Original ACMG Summary:** The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong (PS4)** | Fisher Exact or Chi-Squared analysis shows statistical increase in cases over controls. |
| ~~**Moderate (PS4_Moderate)**~~ | ~~Genes not associated with autosomal dominant conditions; proband count not in use.~~ |
| ~~**Supporting (PS4_Supporting)**~~ | ~~Genes not associated with autosomal dominant conditions; proband count not in use.~~ |

**Notes for autosomal recessive:**
- If a published case-control study does not exist, and the variant is reported at high frequency in both cases and controls, a Chi-squared or Fisher's Exact test can be performed to determine if the variant is statistically higher in cases than the general population
- To use this, the gene must be definitively associated with hearing loss
- Fisher's exact test is preferred if sample size allows
- This should be done with caution, since general population databases are not a true control cohort and could have individuals with hearing loss present
- This analysis can be used as evidence for pathogenicity, but should not be used as evidence against pathogenicity
- The rule can be applied if the % of positive case alleles is higher than the % of positive alleles from the general population with a P value ≤0.05

**Process:**
1. **Cases:** From publications or patient cohorts, determine (race-matching as closely as possible): number of positive case alleles, number of negative case alleles
2. **"Controls":** Using ExAC or gnomAD, determine (race-matching to cases as closely as possible): number of positive alleles, number of negative alleles
3. Fill out a 2x2 contingency table using Chi-squared Test with Yates correction, Two-tailed P value

|  | Variant Positive Alleles | Variant Negative Alleles |
|--|--------------------------|--------------------------|
| **Cases** | # | # |
| **General Population** | # | # |

---

### PM1 - Mutational Hot Spot

**Original ACMG Summary:** Located in a mutational hot spot and/or critical and well-established functional domain without benign variation.

**VCEP Specifications:**

- **Not applicable for OTOF and MYO15A.** No regions are specified for OTOF or MYO15A.

---

### PM2 - Absent from Controls

**Original ACMG Summary:** Absent from controls (or at extremely low frequency if recessive) in population databases.

**VCEP Specification (Supporting only):**
- Per SVI recommendation, PM2 will not be used at Moderate strength
- **PM2_Supporting:** Absent/Rare in population databases (absent or ≤0.00007 (0.007%)) for autosomal recessive
- Can apply PM2_Supporting if MAF is an order of magnitude below BS1_Supporting (i.e., ≤0.007%)

**Notes on MAF:**
- For PM2_Supporting, use actual frequencies in gnomAD; do not apply confidence interval or filtering allele frequency
- For BA1, BS1, and BS1_Supporting, use filtering allele frequency in ExAC or 95% confidence interval, typically using http://cardiodb.org/allelefrequencyapp/
- If the variant is present at high frequency in the Ashkenazi Jewish population in gnomAD, you can calculate the filtering allele frequency using a 95% confidence interval by selecting "Inverse AF" at the frequency app

---

### PM3 - In Trans with Pathogenic

**Original ACMG Summary:** For recessive disorders, detected in trans with a pathogenic variant.

**VCEP Specifications:**

Use the point system as recommended by the Sequence Variation Interpretation working group. Determine appropriate points for each proband by using Table 1. Sum the total number of points for all probands, and determine what strength evidence should be applied by using Table 2.

**Caution:** Use caution if the variant is observed in an isolated population in multiple probands, especially if the same pathogenic variant is observed in trans. Consider downgrading strength in this scenario.

#### Table 1: Default Points for Scoring Variants Observed In Trans (PM3 Rules)

| Classification/Zygosity of Other Variant | Known In Trans | Phase Unknown |
|------------------------------------------|----------------|---------------|
| Pathogenic/Likely pathogenic | 1.0 | 0.5 |
| Homozygous occurrence (Max points from homozygotes = 1.0) | 0.5 | N/A |
| Rare uncertain significance variant on other allele, OR Homozygous occurrence due to consanguinity (Max point = 0.5) | 0.25 | N/A |

#### Table 2: PM3 Evidence Strength Thresholds

| Supporting (PM3_Supporting) | Moderate (PM3) | Strong (PM3_Strong) | Very Strong (PM3_VeryStrong) |
|-----------------------------|----------------|---------------------|------------------------------|
| 0.5 points | 1.0 points | 2.0 points | 4.0 points |

---

### PM4 - Protein Length Changes

**Original ACMG Summary:** Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Moderate** | Protein length change due to an in-frame deletion or insertion that are not located in repetitive regions. |

**Notes:**
- No changes. Follow recommendations as outlined in ACMG/AMP guidelines and/or Sequence Variant Interpretation working group.

---

### PM5 - Novel Missense at Same Residue

**Original ACMG Summary:** Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong (PM5_Strong)** | Missense change at same codon as two different pathogenic missense variants. Located at an amino acid residue with known pathogenic variation (at least 2 other variants at the same site meet pathogenic criteria based on independent data). |
| **Moderate (PM5)** | Missense change at same codon as another pathogenic missense variant. No changes. Follow recommendations as outlined in ACMG/AMP guidelines and/or Sequence Variant Interpretation working group. |

**Caveat:** Assess whether the variants in question could have an impact at the DNA level, such as through splicing impacts.

---

### PM6 - De Novo (Assumed)

**Original ACMG Summary:** Assumed de novo, but without confirmation of paternity and maternity.

**VCEP Specifications:** Same as PS2 — use point-based system above. See [PS2 - De Novo (Confirmed)](#ps2---de-novo-confirmed).

---

### PP1 - Co-segregation

**Original ACMG Summary:** Co-segregation with disease in multiple affected family members.

**VCEP Specifications:**

Follow general recommendations from ClinGen's Sequence Variant Interpretation working group as outlined below.

| Strength | Criteria |
|----------|----------|
| **Supporting** | Segregation in one affected relative for recessive. |
| **Moderate** | Segregation in two affected relatives for recessive. |
| **Strong** | Segregation in three affected relatives for recessive. |

#### Segregation Counting Rules
- For both autosomal dominant and autosomal recessive segregation counting, do not count probands as a segregation
  - Affected segregations = # affected individuals in the family with the variant (dominant) or variants (recessive) − 1
- **Autosomal recessive segregations:**
  - LOD scores are calculated with the following equation:
    - Z (LOD score) = (1 / (0.25^#affected_segregations × 0.75^#unaffected_segregations))
  - The "0.25" and "0.75" numbers represent the risk of being affected vs. unaffected in a classic AR disease model in which both parents are carriers
  - The two variants identified in the proband must be confirmed in trans
  - **Affected segregations** are defined as affected family members (typically siblings) who harbor the variant in question and a second variant on the remaining allele
  - **Unaffected segregations** are defined as unaffected family members, typically siblings, who are at risk to inherit the two variants identified in the proband. These individuals should be either wild-type for both variants identified in the proband, or a heterozygous carrier for a single variant
  - Unaffected, carrier parents DO NOT count as unaffected segregations
  - There may be scenarios where individuals other than siblings could be counted as segregations, such as in families where one parent is affected with the autosomal recessive disorder, in large families with multiple branches, or in consanguineous families

#### General Recommendations (Phenocopy Not an Issue)

| | Supporting | Moderate | Strong |
|--|-----------|----------|--------|
| **Likelihood** | 4:1 | 16:1 | 32:1 |
| **LOD Score** | 0.6 | 1.2 | 1.5 |
| **Autosomal dominant threshold** | 2 affected segregations | 4 affected segregations | 5 affected segregations |
| **Autosomal recessive threshold** | See LOD Table | See LOD Table | See LOD Table |

#### LOD Score Lookup Table (Autosomal Recessive)

| Affected Seg. \ Unaffected Seg. | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|----------------------------------|---|---|---|---|---|---|---|---|---|---|---|
| **0** | 0 | 0.12 | 0.25 | 0.37 | 0.5 | 0.62 | 0.75 | 0.87 | 1 | 1.12 | 1.25 |
| **1** | 0.6 | 0.73 | 0.85 | 0.98 | 1.1 | 1.23 | 1.35 | 1.48 | 1.6 | 1.73 | 1.85 |
| **2** | 1.2 | 1.33 | 1.45 | 1.58 | 1.7 | 1.83 | 1.95 | 2.08 | 2.2 | 2.33 | 2.45 |
| **3** | 1.81 | 1.93 | 2.06 | 2.18 | 2.31 | 2.43 | 2.56 | 2.68 | 2.81 | 2.93 | 3.06 |
| **4** | 2.41 | 2.53 | 2.66 | 2.78 | 2.91 | 3.03 | 3.16 | 3.28 | 3.41 | 3.53 | 3.66 |
| **5** | 3.01 | 3.14 | 3.26 | 3.39 | 3.51 | 3.63 | 3.76 | 3.88 | 4.01 | 4.13 | 4.26 |
| **6** | 3.61 | 3.74 | 3.86 | 3.99 | 4.11 | 4.24 | 4.36 | 4.49 | 4.61 | 4.74 | 4.86 |
| **7** | 4.21 | 4.34 | 4.46 | 4.59 | 4.71 | 4.84 | 4.96 | 5.09 | 5.21 | 5.34 | 5.46 |
| **8** | 4.82 | 4.94 | 5.07 | 5.19 | 5.32 | 5.44 | 5.57 | 5.69 | 5.82 | 5.94 | 6.07 |
| **9** | 5.42 | 5.54 | 5.67 | 5.79 | 5.92 | 6.04 | 6.17 | 6.29 | 6.42 | 6.54 | 6.67 |
| **10** | 6.02 | 6.15 | 6.27 | 6.4 | 6.52 | 6.65 | 6.77 | 6.9 | 7.02 | 7.15 | 7.27 |

---

### PP2 - Missense in Constrained Gene

**Original ACMG Summary:** Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.

**VCEP Specifications:**

- ~~**Not applicable.**~~ Advise against using this rule because there are few such genes that this would apply to, particularly genes associated with autosomal recessive hearing loss.

---

### PP3 - Computational Evidence

**Original ACMG Summary:** Multiple lines of computational evidence support a deleterious effect on the gene or gene product.

**VCEP Specifications (Supporting):**

- REVEL score ≥0.7, or predicted impact to splicing using MaxEntScan
- Use REVEL and MAXENTSCAN:
  - For missense variants, award PP3 if REVEL score is ≥0.7
  - If splicing is predicted to be impacted, either creation of a cryptic splice site, or disruption of a native splice site, award PP3
  - For splice variants (except for canonical −/+1 or 2), use MAXENTSCAN
    - For −/+1 or 2 splice variants, do not use PP3 if you are using PVS1

---

### PP4 - Phenotype Specificity

**Original ACMG Summary:** Patient's phenotype or family history is highly specific for a disease with a single genetic etiology.

**VCEP Specifications (Supporting):**

- Patient's phenotype highly specific for gene or fully sequenced gene set (see specifications in table below)
- The HL-EP applied this rule to HL syndromes if all causative genes have been sequenced and the detection rate at least doubles when the added clinical feature is present
- See table below for applicable gene-disease phenotypes
- **Advise against using PP4 for patients with nonsyndromic or apparently nonsyndromic hearing loss, given genetic heterogeneity**

#### PP4 Applicable Gene-Disease Phenotypes

| Gene | Syndrome | Phenotype | Detection Rate in Unselected HL | Detection Rate with Specified Phenotype |
|------|----------|-----------|-------------------------------|---------------------------------------|
| OTOF | ANSD | Auditory neuropathy spectrum disorder | 1% (Sloan-Heggen et al., 2016) | 9–50% (Matsunaga et al., 2012; Rodriguez-Ballesteros et al., 2008; Varga et al., 2006) |

> **Note:** PP4 is applicable to OTOF for patients presenting with auditory neuropathy spectrum disorder (ANSD). There is no comparable syndrome-specific phenotype listed for MYO15A.

---

### PP5 - Reputable Source

**Original ACMG Summary:** Reputable source recently reports variant as pathogenic, but the evidence is not available to the laboratory to perform an independent evaluation.

**VCEP Specifications:**

- ~~**Not applicable.**~~ Do not use. Not expected to have scenarios where classification is provided in a database without supporting evidence. This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PMID: 29543229).

---

## Benign Criteria

### BA1 - Allele Frequency >0.5%

**Original ACMG Summary:** Allele frequency is above 5% in population databases.

**VCEP Specification (Stand Alone):**
- MAF of ≥0.005 (0.5%) for autosomal recessive

> **Note:** See the variant exclusion list below for high-frequency pathogenic variants to which BA1/BS1 should NOT be applied.

---

### BS1 - Frequency Greater Than Expected

**Original ACMG Summary:** Allele frequency is greater than expected for disorder.

**VCEP Specifications:**

| Strength | Threshold | Notes |
|----------|-----------|-------|
| **Strong (BS1)** | MAF of ≥0.003 (0.3%) | For autosomal recessive. Likely benign, provided there is no conflicting evidence. |
| **Supporting (BS1_Supporting)** | MAF of ≥0.0007 (0.07%) | For autosomal recessive. |

---

### BS2 - Observed in Healthy Adult

**Original ACMG Summary:** Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder.

**VCEP Specifications (Strong):**

- Observation of variant (biallelic with known pathogenic variant for recessive) in controls inconsistent with disease penetrance
- Advise caution when using this rule, since most hearing loss is autosomal recessive, and autosomal dominant hearing loss could display reduced penetrance or variable expression
- However, if biallelic observations in controls are inconsistent with disease penetrance, this may be applicable
  - Ensure age of the unaffected individual is appropriate
  - MYO15A and OTOF are expected to cause congenital or childhood onset hearing loss
  - Therefore, an adult (i.e., >18 years) may be an appropriate individual to consider application of this criteria
  - Please see additional considerations listed under BS4 "Genotype+/phenotype−"

---

### BS3 - Functional Studies (No Effect)

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

**VCEP Specifications (Supporting only):**

- Functional study shows no deleterious effect (none are defined for OTOF and MYO15A)
- Recommend that functional evidence is not used as strong evidence, due to the absence of well-established functional studies for hearing loss genes
- No specific assays are listed for OTOF or MYO15A. However, BS3_Supporting can be used for functional analyses if:
  - The assay has been validated by a known pathogenic and benign variant **AND**
  - There is plausible reason that the function the assay is testing relates to the phenotype **AND**
  - The assay conditions are likely to mimic the physiological environment

---

### BS4 - Lack of Segregation

**Original ACMG Summary:** Lack of segregation in affected members of a family.

**VCEP Specifications (Strong):**

Non-segregation with disease.

**Phenotype+/genotype−:**
- Strong evidence for benign
- Be cautious when using this as the possibility for phenocopy is high. The hearing loss phenotype should be consistent within the family to consider it a non-segregation, though intra-familial variability has been reported. Factors to consider are:
  - **Age of onset** (i.e., congenital/early childhood vs. adult onset)
  - **Hearing loss prevalence** increases significantly with age. A congenital hearing loss in a child and a late onset hearing loss in a grandparent would not be a consistent phenotype
  - **Severity** (i.e., mild vs. profound)
  - **Minor differences** may exist among family members
  - Keep in mind that **progression** in older individuals may account for a discrepancy between individuals
  - **Audiogram shape** — may not be completely consistent among family members even with same etiology

**Genotype+/phenotype−:**
- Confounding variables to applying this rule: Age-related penetrance, variable expressivity, etc.
- If the gene is associated with later onset and individual with the non-segregation is beyond the expected age that the hearing loss would occur, consider applying BS4_Supporting
- Recommend only using for fully penetrant genes (typically genes associated with AR hearing loss)
  - Must be confident that patient is truly unaffected and a hearing loss is not missed or subclinical
  - Be cautious if only phenotyping was newborn hearing screening
  - Diagnostic audiometric testing (auditory brainstem response (ABR) or audiogram should be required)
- Any evidence for reduced penetrance, do not use BS4

---

### BP1–BP7 - Benign Supporting

| Criterion | Status | Comment |
|-----------|--------|---------|
| **BP1** | ~~Not applicable~~ | ~~Missense variant in a gene where only truncating variants cause disease.~~ |
| **BP2** | Applicable (Supporting) | Observed in trans with a dominant variant/observed in cis with a pathogenic variant (use with caution). For genes associated with both dominant and recessive hearing loss, consider whether an earlier onset/more severe phenotype could be present if variant is identified in trans with a dominant variant. |
| **BP3** | Applicable (Supporting) | In-frame indels in repeat region without known function. No changes. Follow recommendations as outlined in Richards 2015 and/or ClinGen's Sequence Variant Interpretation working group. |
| **BP4** | Applicable (Supporting) | Computational evidence suggests no impact; REVEL score ≤0.15 or no impact to splicing in MaxEntScan. Use REVEL, award BP4 if score is 0.15 or lower. Make sure to also check MAXENTSCAN to rule out the creation of a cryptic splice site. |
| **BP5** | ~~Not applicable~~ | Autosomal recessive: Do not use. An individual could be carrier of pathogenic variant and have an alternate cause. Therefore, BP5 shouldn't be used as evidence for benign in this case. |
| **BP6** | ~~Not applicable~~ | ~~Reputable source without shared data classified variant as benign.~~ Not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PMID: 29543229). |
| **BP7** | Applicable (Supporting) | Silent variant with no predicted impact to splicing. No changes. Follow recommendations as outlined in Richards 2015 and/or ClinGen's Sequence Variant Interpretation working group. |

---

## Rules for Combining Criteria

### Pathogenic Classification

| Criteria Combination |
|---------------------|
| 1 Very Strong **AND** (≥1 Strong) |
| 1 Very Strong **AND** (≥2 Moderate) |
| 1 Very Strong **AND** (1 Moderate **AND** 1 Supporting) |
| 1 Very Strong **AND** (≥2 Supporting) |
| ≥2 Strong |
| 1 Strong **AND** (≥3 Moderate) |
| 1 Strong **AND** (2 Moderate **AND** ≥2 Supporting) |
| 1 Strong **AND** (1 Moderate **AND** ≥4 Supporting) |

### Likely Pathogenic Classification

| Criteria Combination |
|---------------------|
| PVS1 **AND** PM2_Supporting# |
| 1 Very Strong **AND** 1 Moderate |
| 1 Strong **AND** 1–2 Moderate |
| 1 Strong **AND** ≥2 Supporting |
| ≥3 Moderate |
| 2 Moderate **AND** ≥2 Supporting |
| 1 Moderate **AND** ≥4 Supporting |

> **#** The addition of the rule "PVS1 AND PM2_Supporting" is the only modification made from the original ACMG/AMP published guidelines for combining criteria.

### Benign Classification

| Criteria Combination |
|---------------------|
| 1 Stand-Alone (BA1) |
| ≥2 Strong |

### Likely Benign Classification

| Criteria Combination |
|---------------------|
| BS1 with no conflicting evidence# |
| 1 Strong **AND** 1 Supporting |
| ≥2 Supporting |

> **#** The addition of the rule "BS1 with no conflicting evidence" is the only modification made from the original ACMG/AMP published guidelines for combining criteria. This is consistent with the recommendations made by the Cardiomyopathy Expert Panel and the RASopathy Expert Panel.

---

## Appendices

### Appendix A: Population Frequency Thresholds Summary

| ACMG-AMP Criteria | MAF | Prevalence | Allelic Heterogeneity | Penetrance | Notes |
|-------------------|-----|------------|----------------------|-----------|-------|
| **BA1** | ≥0.005 (0.5%) | 1/200# | 7.2%$ | 100% | Stand Alone |
| **BS1** | ≥0.003 (0.3%) | 1/200 | 4.4%& | 100% | Strong |
| **BS1_Supporting** | ≥0.0007 (0.07%) | 1/200 | 1.0%* | 100% | Supporting |
| **PM2_Supporting** | ≤0.00007 (0.007%) | — | — | — | Can apply if MAF is an order of magnitude below BS1_Supporting (≤0.007%) |

> **#** Congenital and childhood onset hearing loss, based on Morton and Nance, Lin 2012
> **$** Rationale = Based most common variant (35delG) in the most common AR gene, 7% derived from LMM data
> **&** Based 2nd most common variant (Val37Ile) in the most common AR gene, 4% derived from LMM data
> **\*** Based most common variant (2299delG) in the 2nd most common AR gene (USH2A), 1.2% derived from LMM data

### Appendix B: Variant Exclusion List for BA1/BS1

The following high-frequency pathogenic variants should **not** be classified as benign or likely benign based on allele frequency alone:

| Gene | Transcript | cDNA | Protein | ClinVar ID | Pathogenicity | MAF* |
|------|-----------|------|---------|-----------|---------------|------|
| OTOF | NM_194248.3 | c.2485C>T | p.Gln829Ter | 6137 | Pathogenic | 0.0006 (Latino) |
| OTOF | NM_194248.3 | c.5098G>C | p.Glu1700Gln | 48253 | VUS | 0.0068 (EA) |

> *The highest subpopulation frequency in the Genome Aggregation Database (gnomAD) is shown. EA: East Asian; AJ: Ashkenazi Jewish; SA: South Asian; EF: European (Finnish)

### Appendix C: PVS1 Exon Exceptions

The following exons are exceptions to standard PVS1 application:
- **OTOF:** NM_194248.2 Exon 46 (c.5841 to c.5994; PMID: 19250381)
- **MYO15A:** NM_016239.3 Exon 8 (c.4033 to c.4038; PMID: 10552926) and Exon 26 (c.5911 to c.5964; PMID: 30096381)

### Appendix D: Summary of Criteria Specifications

| Criterion | Default ACMG Strength | VCEP Strength | Key Modification |
|-----------|----------------------|---------------|------------------|
| PVS1 | Very Strong | Very Strong / Strong / Moderate / Supporting | PVS1 flowchart with exon exceptions |
| PS1 | Strong | Strong | Includes splice variants at same nucleotide |
| PS2 | Strong | Very Strong / Strong / Moderate / Supporting | Point-based system; de novo not "highly specific" for OTOF/MYO15A |
| PS3 | Strong | Strong / Moderate / Supporting | Strong only for knock-in mouse model |
| PS4 | Strong | Strong | Chi-squared/Fisher's Exact for AR; proband count not in use |
| PM1 | Moderate | Not applicable | No regions defined for OTOF or MYO15A |
| PM2 | Moderate | Supporting only | Per SVI recommendation |
| PM3 | Moderate | Very Strong / Strong / Moderate / Supporting | Point-based system |
| PM4 | Moderate | Moderate | No changes |
| PM5 | Moderate | Strong / Moderate | PM5_Strong if ≥2 other pathogenic missense at same codon |
| PM6 | Moderate | See PS2 | Point-based system |
| PP1 | Supporting | Strong / Moderate / Supporting | LOD score-based for AR |
| PP2 | Supporting | Not applicable | Not recommended for AR hearing loss genes |
| PP3 | Supporting | Supporting | REVEL ≥0.7 or MaxEntScan |
| PP4 | Supporting | Supporting | OTOF: ANSD phenotype; not for nonsyndromic HL |
| PP5 | Supporting | Not applicable | Per SVI/VCEP recommendation |
| BA1 | Stand Alone | Stand Alone | MAF ≥0.005 (0.5%) for AR |
| BS1 | Strong | Strong / Supporting | BS1: ≥0.003 (0.3%); BS1_Supporting: ≥0.0007 (0.07%) |
| BS2 | Strong | Strong | Biallelic in controls; age >18 appropriate |
| BS3 | Strong | Supporting only | No specific assays defined |
| BS4 | Strong | Strong / Supporting | With detailed phenotype/genotype considerations |
| BP1 | Supporting | Not applicable | — |
| BP2 | Supporting | Supporting | Use with caution |
| BP3 | Supporting | Supporting | No changes |
| BP4 | Supporting | Supporting | REVEL ≤0.15 or no splicing impact |
| BP5 | Supporting | Not applicable | AR: could be carrier |
| BP6 | Supporting | Not applicable | Per SVI/VCEP recommendation |
| BP7 | Supporting | Supporting | No changes |

### Appendix E: Reference PMIDs

- **PMID 30311386** — Primary specification publication
- **PMID 29543229** — ClinGen Sequence Variant Interpretation VCEP Review Committee (PP5/BP6 removal)
- **PMID 19250381** — OTOF Exon 46 exception
- **PMID 10552926** — MYO15A Exon 8 exception
- **PMID 30096381** — MYO15A Exon 26 exception

---

## Version History

| Version | Date | Notes |
|---------|------|-------|
| 1.0.0 | March 30, 2022 | Initial approved version |

---

*This document was compiled from ClinGen Hearing Loss VCEP specifications for OTOF and MYO15A. For the most current version, please refer to the [ClinGen website](https://www.clinicalgenome.org/affiliation/50007/docs/assertion-criteria).*
