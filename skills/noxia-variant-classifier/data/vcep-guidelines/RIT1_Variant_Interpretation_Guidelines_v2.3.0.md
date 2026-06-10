# ClinGen RASopathy VCEP Variant Interpretation Guidelines for RIT1

**Version:** 2.3.0
**Released:** 12/3/2024
**Affiliation:** RASopathy VCEP
**Based on:** Richards et al., 2015 ACMG/AMP Guidelines

---

## Gene Information

| Attribute | Value |
|-----------|-------|
| **Gene** | RIT1 (HGNC:10023) |
| **HGNC Name** | Ras like without CAAX 1 |
| **Transcript** | NM_006912.6 |
| **Disease** | RASopathy (MONDO:0021060) |
| **Inheritance** | Autosomal dominant inheritance |
| **Disease Mechanism** | Gain-of-function |

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

**VCEP Specifications:**

***Not Applicable***

**Comments:** Not applicable. The disease mechanism for RIT1-associated RASopathy is gain-of-function, not loss-of-function. PVS1 should not be used for variant classification in RIT1.

---

### PS1 - Same Amino Acid Change

**Original ACMG Summary:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change. Example: Val->Leu caused by either G>C or G>T in the same codon. Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Strong** | Same amino acid change as a previously established pathogenic variant regardless of nucleotide change. Applicable for observed analogous residue positions in *HRAS*, *KRAS*, *MRAS*, *NRAS*, *RIT1*, and *RRAS2*. | Analogous Gene |

> **Note:** See Appendix A for analogous residue mapping across RAS genes.

---

### PS2 - De Novo (Confirmed)

**Original ACMG Summary:** De novo (both maternity and paternity confirmed) in a patient with the disease and no family history. Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.

**VCEP Specifications:** Follow SVI recommendations for point-based scoring in conjunction with PM6 (see Reference 1) and phenotypic specifications: full points awarded with RASopathy phenotypes, reduced points applicable to cases with minimal phenotypic information (i.e. prenatal cases, cases with a clinical order of a RASopathy panel without clinical information, and cases with limited clinical information in other global tests (such as WES)).

#### PS2/PM6 Points Per Proband

| Phenotypic Consistency | Confirmed *de novo* (PS2) | Assumed *de novo* (PM6) |
|------------------------|:-------------------------:|:-----------------------:|
| Phenotype is consistent with a RASopathy\* | 2 | 1 |
| Limited phenotypic information\*\* | 1 | 0.5 |
| Phenotype not consistent with RASopathy | 0 | 0 |

\*Exclusive of prenatal cases
\*\*Applicable to prenatal cases, cases with a clinical order of a RASopathy panel without clinical information, and cases with limited clinical information in other global tests (such as WES). Phenotypes for prenatal cases include hypertrophic cardiomyopathy, increased nuchal translucency, cystic hygroma, or hydrops.

#### PS2/PM6 Evidence Strength Thresholds

| Points | Strength Level |
|:------:|----------------|
| 0.5 | Supporting (PS2_Supporting or PM6_Supporting) |
| 1.0 | Moderate (PS2_Moderate or PM6) |
| 2.0 | Strong (PS2 or PM6_Strong) |
| 4.0 | Very Strong (PS2_VeryStrong or PM6_VeryStrong) |

| Strength | Points | Modification Type |
|----------|:------:|-------------------|
| **Very Strong** | 4 Points | Strength |
| **Strong** | 2 Points | None |
| **Moderate** | 1 Point | Strength |

---

### PS3 - Functional Studies

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product. Note: Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.

**VCEP Specifications:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product. Approved assays are available in the supplemental materials.

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Moderate** | Two or more different approved assays. | Disease-specific, Gene-specific, Strength |
| **Supporting** | One approved assay. | Disease-specific, Gene-specific, Strength |

> **Note:** Two or more *unique* assay types (e.g., RAS activation assay AND MEK activation assay) for a given variant provides sufficient evidence to upgrade PS3 to Moderate strength.

#### Approved Assay Instances for RIT1

| Assay | General Description | Assay Specificity | RIT1 PMIDs | Proposed Strength |
|-------|--------------------|--------------------|------------|-------------------|
| **RAS Activation Assay** | Measures the bound RAS protein that immunoprecipitated with RAF1 or RBD (synthetic) | Pathway Specific | 27226556, 37450595 (Fang 2016, Cuevas-Navarro 2023) | PS3_Supporting; BS3_NA |
| **MEK Activation Assay** | Measures the ratio of phosphorylated MEK to unphosphorylated MEK, basally and following RTK stimulation | Pathway Specific | 24469055, 25959749 (Berger 2014, Koenighofer 2016) | PS3_Supporting; BS3_NA |
| **ERK Activation Assay** | Measures the ratio of phosphorylated ERK to unphosphorylated ERK, basally and following stimulation | Pathway Specific | 25959749, 29734338 (Koenighofer 2016, Buschenfelde 2018) | PS3_Supporting; BS3_NA |

> **Important:** Prior to evaluation of an assay for a variant, all assays are expected to be validated by the performing laboratory in accordance with standard procedures with all appropriate control inclusions (PMID: 31892348) to enable accurate detection of abnormal and normal results. As most of these assays are semi-quantitative in nature, abnormal results should be compared relative to the known status of the controls included in the assay. Multiple assays are pathway specific, meaning controls from any RAS/MAPK gene may be used to support abnormal pathway function.

> **BS3 Note:** BS3 is **Not Applicable** for RIT1. Approved functional studies are available for each individual gene in the supplemental material, but no BS3 assays are currently approved. Additional functional studies can be submitted to the expert panel for approval.

---

### PS4 - Prevalence in Affected

**Original ACMG Summary:** The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls. Note 1: Relative risk (RR) or odds ratio (OR), as obtained from case-control studies, is >5.0 and the confidence interval around the estimate of RR or OR does not include 1.0. Note 2: In instances of very rare variants where case-control studies may not reach statistical significance, the prior observation of the variant in multiple unrelated patients with the same phenotype, and its absence in controls, may be used as moderate level of evidence.

**VCEP Specifications:** Strength adjustment using point-based scoring for autosomal dominant cases with phenotypic specifications: full points awarded with RASopathy phenotypes, reduced points applicable to cases with minimal phenotypic information (i.e. prenatal cases, cases with a clinical order of a RASopathy panel without clinical information, and cases with limited clinical information in other global tests (such as WES)).

#### PS4 Points Per Proband

| Phenotypic Consistency | Points per Proband |
|------------------------|--------------------|
| Individual well-phenotyped with features of a RASopathy | 1 |
| Limited phenotypic information compatible with RASopathy\* | 0.5 |
| No clinical information or isolated clinical features | 0 |
| Well-phenotyped but consistent with non-RASopathy disorder\*\* | -1 |

\*Applicable to prenatal cases, cases with a clinical order of a RASopathy panel without clinical information, and cases with limited clinical information in other global tests (such as WES). Phenotypes for prenatal cases include hypertrophic cardiomyopathy, increased nuchal translucency, cystic hygroma, or hydrops.
\*\*Negative points for PS4 represent proband affected with a non-RASopathy congenital disorder rather than a healthy individual (BS2). This typically applies to probands tested by exome analysis with multiple other clinical features supporting a distinct syndromic disorder (e.g. CHARGE, CdLS).

#### PS4 Evidence Strength Thresholds

| Points | Strength Level |
|:------:|----------------|
| 1.0 | Supporting (PS4_Supporting) |
| 3.0 | Moderate (PS4_Moderate) |
| 5.0 | Strong (PS4) |

---

### PM1 - Mutational Hot Spot

**Original ACMG Summary:** Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.

**VCEP Specifications:** Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation. PM1 and PM5 may be used in conjunction at moderate levels, however, PM1 may not be applied if PM5_Strong is applied to avoid overweighting.

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Moderate** | Applicable only to critical and well-established functional domains available in the supplementary table. Not applicable to specific amino acid residues (see PM5). | Gene-specific |

#### RIT1 Functional Domains for PM1

| Domain | Amino Acid Range | Notes |
|--------|:----------------:|-------|
| P-loop | AA 28-35 | Critical functional domain |
| Switch I (SW1) | AA 43-58 | Critical functional domain |
| Switch II (SW2) | AA 75-82 | Critical functional domain |
| SAK | N/A | **Not applicable** for PM1 in RIT1 |

> **Important:** PM1 and PM5 may be used in conjunction at moderate levels. However, PM1 may **not** be applied if PM5_Strong is applied to avoid overweighting.

---

### PM2 - Absent from Controls

**Original ACMG Summary:** Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium. Caveat: Population data for indels may be poorly called by next generation sequencing.

**VCEP Specification (Supporting only):**
- The variant must be absent from controls (gnomAD).

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Supporting** | The variant must be absent from controls (gnomAD). | Strength |

---

### PM3 - In Trans with Pathogenic

**Original ACMG Summary:** For recessive disorders, detected in trans with a pathogenic variant. Note: This requires testing of parents (or offspring) to determine phase.

**VCEP Specifications:**

***Not Applicable***

**Comments:** Not applicable. RIT1-associated RASopathy follows autosomal dominant inheritance; PM3 is only applicable to recessive disorders.

---

### PM4 - Protein Length Changes

**Original ACMG Summary:** Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

**VCEP Specifications:** Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Moderate** | No known repetitive areas in gene. Use as described. | General recommendation |

---

### PM5 - Novel Missense at Same Residue

**Original ACMG Summary:** Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before. Example: Arg156His is pathogenic; now you observe Arg156Cys. Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:** Applicable for observed analogous residue positions in *HRAS*, *KRAS*, *MRAS*, *NRAS*, *RIT1*, and *RRAS2*. PM1 and PM5 may be used in conjunction at moderate levels, however, PM1 may not be applied if PM5_Strong is applied to avoid overweighting.

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Strong** | ≥2 different [likely] pathogenic residue changes at the same codon observed in ≥5 probands. | Analogous Gene, Strength |
| **Moderate** | 1 [likely] pathogenic residue change at the same codon. | Analogous Gene, Disease-specific |

> **Note:** PM1 and PM5 may be used in conjunction at moderate levels. However, PM1 may **not** be applied if PM5_Strong is applied to avoid overweighting.

---

### PM6 - De Novo (Assumed)

**Original ACMG Summary:** Assumed de novo, but without confirmation of paternity and maternity.

**VCEP Specifications:** Follow SVI recommendations for point-based scoring in conjunction with PS2 (see Reference 1) and phenotypic specifications: full points awarded with RASopathy phenotypes, reduced points applicable to cases with minimal phenotypic information (i.e. prenatal cases, cases with a clinical order of a RASopathy panel without clinical information, and cases with limited clinical information in other global tests (such as WES)).

Same point-based system as PS2 -- see [PS2/PM6 Point System](#ps2pm6-points-per-proband) above.

| Strength | Points | Modification Type |
|----------|:------:|-------------------|
| **Strong** | 2 Points | Strength |
| **Moderate** | 1 Point | None |
| **Supporting** | 0.5 Points | Strength |

---

### PP1 - Co-segregation

**Original ACMG Summary:** Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease. Note: May be used as stronger evidence with increasing segregation data.

**VCEP Specifications:** Segregation in more than one family is recommended.

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Strong** | ≥7 informative meioses | Strength |
| **Moderate** | ≥5 informative meioses | Strength |
| **Supporting** | ≥3 informative meioses | Disease-specific |

---

### PP2 - Missense in Constrained Gene

**Original ACMG Summary:** Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.

**VCEP Specifications:**

***Not Applicable***

**Comments:** Not applicable because missense z score is <3.09 in gnomAD.

---

### PP3 - Computational Evidence

**Original ACMG Summary:** Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.). Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.

**VCEP Specifications:** For missense variants: REVEL ≥ 0.7. For splicing impact, predicted outcome must match disease mechanism.

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Supporting** | For missense variants: REVEL ≥ 0.7. For splicing impact, predicted outcome must match disease mechanism. | Disease-specific |

---

### PP4 - Phenotype Specificity

**Original ACMG Summary:** Patient's phenotype or family history is highly specific for a disease with a single genetic etiology.

**VCEP Specifications:**

***Not Applicable***

**Comments:** Not applicable, see PS4.

---

### PP5 - Reputable Source

**Original ACMG Summary:** Reputable source recently reports variant as pathogenic, but the evidence is not available to the laboratory to perform an independent evaluation.

**VCEP Specifications:**

***Not Applicable***

This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PMID: 29543229).

---

## Benign Criteria

### BA1 - Allele Frequency >5%

**Original ACMG Summary:** Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

**VCEP Specification (Stand Alone):**
- gnomAD filtering allele frequency **≥0.05%**

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Stand Alone** | gnomAD filtering allele frequency ≥0.05%. | Disease-specific |

---

### BS1 - Frequency Greater Than Expected

**Original ACMG Summary:** Allele frequency is greater than expected for disorder.

**VCEP Specification (Strong):**
- gnomAD filtering allele frequency **≥0.025%**

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Strong** | gnomAD filtering allele frequency ≥0.025%. | Disease-specific |

---

### BS2 - Observed in Healthy Adult

**Original ACMG Summary:** Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

**VCEP Specifications:** Strength adjustment using point-based scoring based on phenotypic specifications. Phenotypic specifications: based on healthy homozygote or heterozygote individuals, reduced points for apparently unaffected heterozygous individuals, applicable to parent or sibling samples during clinical family evaluations.

#### BS2 Points Per Individual

| Phenotypic Consistency | Points per Individual |
|------------------------|-----------------------|
| Healthy homozygous individual assessed for a RASopathy | -3 |
| Healthy heterozygous individual assessed for a RASopathy | -1 |
| No phenotypic information other than "unaffected" heterozygote\* | -0.25 |
| No clinical information or nonspecific clinical features | 0 |

\*Typically applicable to parental or sibling samples during clinical family evaluations.

#### BS2 Evidence Strength Thresholds

| Points | Strength Level |
|:------:|----------------|
| -1 | Supporting (BS2_Supporting) |
| N/A | Moderate (N/A) |
| -3.0 | Strong (BS2) |

| Strength | Points | Modification Type |
|----------|:------:|-------------------|
| **Strong** | -4 Points | Strength |
| **Supporting** | -1 Point | Strength |

---

### BS3 - Functional Studies (No Effect)

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

**VCEP Specifications:**

***Not Applicable***

**Comments:** Approved functional studies are available for each individual gene in the supplemental material. Additional functional studies can be submitted to the expert panel for approval. No BS3 assays are currently approved for RIT1.

---

### BS4 - Lack of Segregation

**Original ACMG Summary:** Lack of segregation in affected members of a family. Caveat: The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.

**VCEP Specifications:** Lack of segregation in affected members of a family.

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Strong** | Requires only one informative meiosis. | General recommendation |

---

### BP1-BP7 - Benign Supporting

| Criterion | Status | Specifications |
|-----------|--------|----------------|
| **BP1** | Applicable (Modified) | Truncating, LOF variant in a gene for which primarily missense, GOF variants are known to cause disease. This rule has contraindications for use with RASopathies. Given the disease mechanism is gain-of-function, BP1 should be used for any truncating variant (nonsense, frameshift, affects canonical splice sites, initiation codon, entire gene or multi-exon deletion) in genes without established LOF correlation to disease. See supplemental material regarding dosage sensitivity information. |
| **BP2** | Applicable (Modified) | Points are awarded for an alternative molecular cause of a RASopathy in the same gene (and/or in conjunction with BP5) and the phenotype is consistent with expected severity of the RASopathy. **Supporting:** ≥(-1) Point. **Moderate:** ≥(-2) Points. **Strong:** ≥(-4) Points. |
| **BP3** | Not Applicable | No known benign repetitive areas in RASopathy genes. |
| **BP4** | Applicable (Modified) | For missense variants: REVEL ≤0.3. For splicing variants: predicted outcome is negligible or does not match disease mechanism. |
| **BP5** | Applicable (Modified) | Points are awarded for an alternative molecular cause of a RASopathy in a different gene (and/or in conjunction with BP2) and the phenotype is consistent with expected severity of the RASopathy. Points are also awarded for phenotypes inconsistent with a RASopathy and fully explained by a different causative variant (e.g. WES testing). **Supporting:** ≥(-1) Point. **Moderate:** ≥(-2) Points. **Strong:** ≥(-4) Points. |
| **BP6** | Not Applicable | This criterion is not for use as recommended by the ClinGen SVI VCEP Review Committee (PMID: 29543229). |
| **BP7** | Applicable | A synonymous (silent) variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved. This rule is also applicable for intronic positions (except canonical splice sites) or non-coding variants and should be used in conjunction with BP4. |

#### BP5/BP2 Point System

| Phenotypic Consistency | Points per Individual |
|------------------------|:---------------------:|
| Phenotype inconsistent with a RASopathy and causative variant has been identified, **-or-** Molecular cause of a RASopathy is identified in a different RASopathy gene, **-or-** Molecular cause of a RASopathy is identified in *trans* or *cis* with the variant being classified | -1 |
| Phenotype inconsistent with a RASopathy and no causative variant identified/reported | 0 |

#### BP5/BP2 Evidence Strength Thresholds

| Points | Strength Level |
|:------:|----------------|
| -1 | Supporting (BP5/BP2) |
| N/A | Moderate (N/A) |
| -3.0 | Strong (BP5_Strong / BP2_Strong) |

---

## Rules for Combining Criteria

### Pathogenic Classification

| Criteria Combination |
|---------------------|
| 1 Very Strong (PS2_VeryStrong) **AND** ≥1 Strong (PS1, PS2, PS4, PM5_Strong, PM6_Strong, PP1_Strong) |
| 1 Very Strong (PS2_VeryStrong) **AND** ≥2 Moderate (PS2_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate) |
| 1 Very Strong (PS2_VeryStrong) **AND** 1 Moderate (PS2_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate) **AND** 1 Supporting (PS3_Supporting, PS4_Supporting, PM2_Supporting, PM6_Supporting, PP1, PP3) |
| 1 Very Strong (PS2_VeryStrong) **AND** ≥2 Supporting (PS3_Supporting, PS4_Supporting, PM2_Supporting, PM6_Supporting, PP1, PP3) |
| ≥2 Strong (PS1, PS2, PS4, PM5_Strong, PM6_Strong, PP1_Strong) |
| 1 Strong (PS1, PS2, PS4, PM5_Strong, PM6_Strong, PP1_Strong) **AND** ≥3 Moderate (PS2_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate) |
| 1 Strong (PS1, PS2, PS4, PM5_Strong, PM6_Strong, PP1_Strong) **AND** 2 Moderate (PS2_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate) **AND** ≥2 Supporting (PS3_Supporting, PS4_Supporting, PM2_Supporting, PM6_Supporting, PP1, PP3) |
| 1 Strong (PS1, PS2, PS4, PM5_Strong, PM6_Strong, PP1_Strong) **AND** 1 Moderate (PS2_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate) **AND** ≥4 Supporting (PS3_Supporting, PS4_Supporting, PM2_Supporting, PM6_Supporting, PP1, PP3) |

### Likely Pathogenic Classification

| Criteria Combination |
|---------------------|
| 1 Very Strong (PS2_VeryStrong) **AND** 1 Moderate (PS2_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate) |
| 1 Strong (PS1, PS2, PS4, PM5_Strong, PM6_Strong, PP1_Strong) **AND** 1 Moderate (PS2_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate) |
| 1 Strong (PS1, PS2, PS4, PM5_Strong, PM6_Strong, PP1_Strong) **AND** ≥2 Supporting (PS3_Supporting, PS4_Supporting, PM2_Supporting, PM6_Supporting, PP1, PP3) |
| ≥3 Moderate (PS2_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate) |
| 2 Moderate (PS2_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate) **AND** ≥2 Supporting (PS3_Supporting, PS4_Supporting, PM2_Supporting, PM6_Supporting, PP1, PP3) |
| 1 Moderate (PS2_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate) **AND** ≥4 Supporting (PS3_Supporting, PS4_Supporting, PM2_Supporting, PM6_Supporting, PP1, PP3) |

### Benign Classification

| Criteria Combination |
|---------------------|
| ≥2 Strong (BS1, BS2, BS4, BP2_Strong, BP5_Strong) |
| 1 Stand Alone (BA1) |

### Likely Benign Classification

| Criteria Combination |
|---------------------|
| 1 Strong (BS1, BS2, BS4, BP2_Strong, BP5_Strong) **AND** 1 Supporting (BS2_Supporting, BP1, BP2, BP4, BP5, BP7) |
| ≥2 Supporting (BS2_Supporting, BP1, BP2, BP4, BP5, BP7) |
| 1 Strong (BS1, BS2, BS4, BP2_Strong, BP5_Strong) |
| 1 Strong (BS1) |

---

## Appendices

### Appendix A: Analogous Residue Mapping

The following table specifies analogous functional domains between RAS genes associated with RASopathies. PS1 and PM5 may use analogous residue positions across *HRAS*, *KRAS*, *MRAS*, *NRAS*, *RIT1*, and *RRAS2*.

| Domain | HRAS (NP_005334.1) | KRAS (NP_004976.2) | MRAS (NP_036351.3) | NRAS (NP_002515.1) | RIT1 (NP_008843.1) | RRAS2 (NP_036382.2) |
|--------|:---:|:---:|:---:|:---:|:---:|:---:|
| **P-loop** | AA 10-17 | AA 10-17 | AA 20-27 | AA 10-17 | AA 28-35 | AA 21-28 |
| **Switch I** | AA 25-40 | AA 25-40 | AA 35-50 | AA 25-40 | AA 43-58 | AA 36-51 |
| **Switch II** | AA 57-64 | AA 57-64 | AA 67-74 | AA 57-64 | AA 75-82 | AA 68-75 |

### Appendix B: Approved Functional Assays Summary

| Assay Type | Specificity | Applicable to RIT1 | Strength |
|------------|-------------|:-------------------:|----------|
| RAS Activation Assay | Pathway Specific | Yes | PS3_Supporting |
| MEK Activation Assay | Pathway Specific | Yes | PS3_Supporting |
| ERK Activation Assay | Pathway Specific | Yes | PS3_Supporting |
| SHP-2 Phosphatase Activity | Gene Specific (PTPN11) | No | N/A |
| BRAF Kinase Activity | Gene Specific (BRAF) | No | N/A |
| RAF1 Kinase Activity | Gene Specific (RAF1) | No | N/A |
| LZTR1 Stability/Localization | Gene Specific (LZTR1) | No | N/A |

> **Upgrading PS3:** Two or more unique assay types (e.g., RAS activation assay AND MEK activation assay) for a given variant provides sufficient evidence to upgrade PS3 to Moderate strength.

### Appendix C: Population Frequency Thresholds Summary

| Criterion | Threshold | Strength |
|-----------|-----------|----------|
| BA1 | ≥0.05% (gnomAD filtering allele frequency) | Stand Alone |
| BS1 | ≥0.025% (gnomAD filtering allele frequency) | Strong |
| PM2 | Absent from gnomAD | Supporting |

### Appendix D: Criteria Applicability Summary

| Criterion | Status | Max Strength |
|-----------|--------|:------------:|
| PVS1 | Not Applicable | - |
| PS1 | Applicable | Strong |
| PS2 | Applicable (Point-based) | Very Strong |
| PS3 | Applicable (Modified) | Moderate |
| PS4 | Applicable (Point-based) | Strong |
| PM1 | Applicable (Gene-specific domains) | Moderate |
| PM2 | Applicable (Supporting only) | Supporting |
| PM3 | Not Applicable | - |
| PM4 | Applicable | Moderate |
| PM5 | Applicable (Analogous genes) | Strong |
| PM6 | Applicable (Point-based) | Strong |
| PP1 | Applicable (Modified thresholds) | Strong |
| PP2 | Not Applicable | - |
| PP3 | Applicable (REVEL ≥ 0.7) | Supporting |
| PP4 | Not Applicable | - |
| PP5 | Not Applicable | - |
| BA1 | Applicable (≥0.05%) | Stand Alone |
| BS1 | Applicable (≥0.025%) | Strong |
| BS2 | Applicable (Point-based) | Strong |
| BS3 | Not Applicable | - |
| BS4 | Applicable | Strong |
| BP1 | Applicable (Modified for GOF) | Supporting |
| BP2 | Applicable (Point-based) | Strong |
| BP3 | Not Applicable | - |
| BP4 | Applicable (REVEL ≤ 0.3) | Supporting |
| BP5 | Applicable (Point-based) | Strong |
| BP6 | Not Applicable | - |
| BP7 | Applicable | Supporting |

### Appendix E: Reference PMIDs

| Reference | Description |
|-----------|-------------|
| PMID: 29543229 | ClinGen SVI recommendation for PP5/BP6 deprecation |
| PMID: 31892348 | SVI recommendations for PS3/BS3 functional evidence |
| SVI De Novo Criteria v1.1 | SVI proposal for point-based de novo scoring (PS2/PM6) |

---

## Version History

| Version | Date | Notes |
|---------|------|-------|
| 2.3.0 | 12/3/2024 | Submitting Pilot Rules. All pilot variants are attached in the LZTR1 submission. "Observed in ≥5 probands" removed from PM5 at Moderate strength. |

---

*This document was compiled from ClinGen RASopathy VCEP specifications and ClinGen SVI recommendations. For the most current version, please refer to the ClinGen website.*
