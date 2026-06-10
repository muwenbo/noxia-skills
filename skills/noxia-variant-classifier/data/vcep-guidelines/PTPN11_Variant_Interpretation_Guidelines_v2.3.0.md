# ClinGen RASopathy VCEP Variant Interpretation Guidelines for PTPN11

**Version:** 2.3.0
**Released:** 12/3/2024
**Affiliation:** RASopathy VCEP
**Based on:** Richards et al., 2015 ACMG/AMP Guidelines

---

## Gene Information

| Attribute | Value |
|-----------|-------|
| **Gene** | PTPN11 (HGNC:9644) |
| **HGNC Name** | protein tyrosine phosphatase non-receptor type 11 |
| **Transcript** | NM_002834.5 |
| **Disease** | RASopathy (MONDO:0021060) |
| **Inheritance** | Autosomal dominant inheritance |

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

**VCEP Specifications:** *Not Applicable*

LOF and/or haploinsufficiency has not been clearly identified as disease mechanisms for these genes relative to the RASopathy spectrum phenotype, therefore in general this rule is not applicable.

> **Note:** PTPN11 is currently the only gene with a confirmed association to another non-RASopathy disorder due to LOF alleles. Variants in PTPN11 with predicted LOF should not be evaluated by these RASopathy-specific criteria, but should defer to non-adjusted criteria. Given that some historical LOF variants (e.g. canonical splice sites) could potentially result in a gain of function, users should assess using these criteria and non-adjusted criteria to identify the highest likelihood of pathogenicity for all associated diseases. The ClinGen Dosage Sensitivity Map Status should be reviewed for any new apparently LOF disease associations prior to classification assessment.

---

### PS1 - Same Amino Acid Change

**Original ACMG Summary:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change. Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | Same amino acid change as a previously established pathogenic variant in *PTPN11* regardless of nucleotide change. |

**Modification Type:** Gene-specific

---

### PS2 - De Novo (Confirmed)

**Original ACMG Summary:** De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.

**VCEP Specifications:** Follow SVI recommendations for point-based scoring in conjunction with PM6 (see Reference 1) and phenotypic specifications: full points awarded with RASopathy phenotypes, reduced points applicable to cases with minimal phenotypic information (i.e. prenatal cases, cases with a clinical order of a RASopathy panel without clinical information, and cases with limited clinical information in other global tests (such as WES)).

#### PS2/PM6 Point System (Per Proband)

| Phenotypic Consistency | Confirmed *de novo* (PS2) | Assumed *de novo* (PM6) |
|------------------------|:-------------------------:|:-----------------------:|
| Phenotype is consistent with a RASopathy\* | 2 | 1 |
| Limited phenotypic information\*\* | 1 | 0.5 |
| Phenotype not consistent with RASopathy | 0 | 0 |

\*Exclusive of prenatal cases

\*\*Applicable to prenatal cases, cases with a clinical order of a RASopathy panel without clinical information, and cases with limited clinical information in other global tests (such as WES). Phenotypes for prenatal cases include hypertrophic cardiomyopathy, increased nuchal translucency, cystic hygroma, or hydrops.

#### Evidence Strength Thresholds

| Points | Strength Level |
|:------:|----------------|
| 0.5 | PS2_Supporting or PM6_Supporting |
| 1.0 | PS2_Moderate or PM6 (Moderate) |
| 2.0 | PS2 (Strong) or PM6_Strong |
| 4.0 | PS2_VeryStrong or PM6_VeryStrong |

---

### PS3 - Functional Studies

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.

**VCEP Specifications:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product. Approved assays are available in the supplemental materials.

| Strength | Criteria |
|----------|----------|
| **Moderate** | Two or more different approved assays showing abnormal result. |
| **Supporting** | One approved assay showing abnormal result. |

> **Note:** PS3 at Strong level is not applicable for PTPN11 per VCEP specifications. Two or more unique assay types are required for PS3_Moderate.

#### Approved Assay Instances for PTPN11

All approved functional assays are expected to be validated by the performing laboratory with appropriate controls (PMID: 31892348). Abnormal results should be compared relative to the known status of the controls included in the assay.

##### 1. SHP-2 Phosphatase Activity (Gene-Specific)

| Attribute | Details |
|-----------|---------|
| **Assay Type** | Gene-Specific (PTPN11) |
| **Description** | Measures the ratio of phosphorylated and dephosphorylated SHP2; substrate dephosphorylation (e.g. PNPP) |
| **Material** | COS7 cells transfected with WT or mutant SHP-2 cDNAs; recombinant proteins expressed in *E. coli* |
| **Readout** | Semi-quantitative; substrate dephosphorylation |
| **Threshold (Normal)** | Normal dephosphorylation |
| **Threshold (Abnormal)** | Increased dephosphorylation |
| **Validation Controls (P/LP)** | 16 variants (T42A, D61N, Y63C, F71I, A72S, A72V, T73I, E76D, E76K, E76A, Q79R, E139D, I282V, N308D, S502T, M504V) |
| **Validation Controls (B/LB)** | 17 variants (T42I, T42K, T42P, T42R, T42S, E139A, E139G, E139K, E139Q, E139V, I282L, I282F, I282N, I282T, I282S, I282M, (N308D);(C459G) trans) |
| **PMIDs** | 14974085, 15834506, 17177198, 18372317 |
| **Approved** | Yes |
| **Proposed Strength** | PS3/BS3 |

##### 2. RAS Activation Assay (Pathway-Specific)

| Attribute | Details |
|-----------|---------|
| **Assay Type** | Pathway-Specific (works for genes upstream from RAS and RAS proteins) |
| **Description** | Measures the bound RAS protein that immunoprecipitated with RAF1 or RBD (synthetic) |
| **Readout** | Semi-quantitative; ratio of GTP-bound RAS to total RAS |
| **Threshold (Normal)** | Normal (WT) pattern |
| **Threshold (Abnormal)** | Increased RAS/RBD complexes compared with positive control range in assay |
| **Approved** | Yes |
| **Proposed Strength** | PS3_Supporting; BS3 not applicable |

##### 3. MEK Activation Assay (Pathway-Specific)

| Attribute | Details |
|-----------|---------|
| **Assay Type** | Pathway-Specific |
| **Description** | Measures the ratio of phosphorylated MEK to unphosphorylated MEK, basally and following RTK stimulation |
| **Material (for PTPN11)** | COS-7 cells / HEK293 cells transfected with WT or variant |
| **Readout** | Semi-quantitative; pMEK/MEK ratio basally and/or after RTK stimulation |
| **Threshold (Normal)** | Normal (WT) pattern |
| **Threshold (Abnormal)** | Constitutively active, increased phosphorylation protein, and/or prolonged phosphorylation |
| **Validation Controls (P/LP)** | 7 variants (D61N, Y63C, A72S, E76D, Q79R, I282V, N308D) |
| **Validation Controls (B/LB)** | 1 ((N308D);(C459G) trans, catalytically inactive / C459S) |
| **PMIDs** | 14974085, 15834506 |
| **Approved** | Yes |
| **Proposed Strength** | PS3_Supporting; BS3 not applicable |

##### 4. ERK Activation Assay (Pathway-Specific)

| Attribute | Details |
|-----------|---------|
| **Assay Type** | Pathway-Specific |
| **Description** | Measures the ratio of phosphorylated ERK to unphosphorylated ERK, basally and following stimulation |
| **Material (for PTPN11)** | COS-7 cells / HEK293 cells transfected with WT or variant |
| **Readout** | Semi-quantitative; pERK/ERK ratio basally and after RTK stimulation |
| **Threshold (Normal)** | Normal (WT) pattern |
| **Threshold (Abnormal)** | Constitutively active, increased phosphorylation protein, and/or prolonged phosphorylation |
| **Validation Controls (P/LP)** | 3 variants (A72S, I282V, N308D) |
| **Validation Controls (B/LB)** | 3 ((N308D);(C459G) trans or C459S catalytically inactive, D61N, E76D) |
| **PMIDs** | 14974085, 15834506 |
| **Approved** | Yes |
| **Proposed Strength** | PS3_Supporting; BS3 not applicable |

> **Note on combining assays:** Multiple pathway-specific assays (e.g. RAS activation + MEK activation) count as different assay types and may be combined for PS3_Moderate. Animal models and variant-specific assays (e.g. myristoylation assays) have been excluded as the approved assays are considered the most appropriate to evaluate variant pathogenicity for all genes.

---

### PS4 - Prevalence in Affected

**Original ACMG Summary:** The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.

**VCEP Specifications:** Strength adjustment using point-based scoring for autosomal dominant cases with phenotypic specifications: full points awarded with RASopathy phenotypes, reduced points applicable to cases with minimal phenotypic information.

#### PS4 Point System (Per Proband)

| Phenotypic Consistency | Points per Proband |
|------------------------|:------------------:|
| Individual well-phenotyped with features of a RASopathy | 1 |
| Limited phenotypic information compatible with RASopathy\* | 0.5 |
| No clinical information or isolated clinical features | 0 |
| Well-phenotyped but consistent with non-RASopathy disorder\*\* | -1 |

\*Applicable to prenatal cases, cases with a clinical order of a RASopathy panel without clinical information, and cases with limited clinical information in other global tests (such as WES). Phenotypes for prenatal cases include hypertrophic cardiomyopathy, increased nuchal translucency, cystic hygroma, or hydrops.

\*\*Negative points for PS4 represent proband affected with a non-RASopathy congenital disorder rather than a healthy individual (BS2). This typically applies to probands tested by exome analysis with multiple other clinical features supporting a distinct syndromic disorder (e.g. CHARGE, CdLS).

#### PS4 Evidence Strength Thresholds

| Total Points | Strength Level |
|:------------:|----------------|
| ≥1.0 | PS4_Supporting |
| ≥3.0 | PS4_Moderate |
| ≥5.0 | PS4 (Strong) |

---

### PM1 - Mutational Hot Spot

**Original ACMG Summary:** Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.

**VCEP Specifications:** Located in a mutational hot spot and/or critical and well-established functional domain without benign variation. PM1 and PM5 may be used in conjunction at moderate levels, however, PM1 may not be applied if PM5_Strong is applied to avoid overweighting.

| Strength | Criteria |
|----------|----------|
| **Moderate** | Applicable only to critical and well-established functional domains: directly interacting residues between N-SH2 and PTPN domains. |

#### PM1 Applicable Residues (N-SH2/PTPN Domain Interaction)

| Residue Positions |
|-------------------|
| AA 4 |
| AA 7-9 |
| AA 58-63 |
| AA 69-77 |
| AA 247 |
| AA 251 |
| AA 255-256 |
| AA 258 |
| AA 261 |
| AA 265 |
| AA 278-281 |
| AA 284 |

> **Note:** PM1 is not applicable to specific amino acid residues that qualify under PM5.

**Modification Type:** Gene-specific

---

### PM2 - Absent from Controls

**Original ACMG Summary:** Absent from controls (or at extremely low frequency if recessive) in population databases.

**VCEP Specification (Supporting only):**
- The variant must be **absent from controls (gnomAD)**

**Modification Type:** Strength (downgraded to Supporting)

---

### PM3 - In Trans with Pathogenic

**Original ACMG Summary:** For recessive disorders, detected in trans with a pathogenic variant.

**VCEP Specifications:** *Not Applicable*

> **Note:** RASopathy associated with PTPN11 follows autosomal dominant inheritance. PM3 is not applicable.

---

### PM4 - Protein Length Changes

**Original ACMG Summary:** Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Moderate** | No known repetitive areas in gene. Use as described per original ACMG criteria. |

**Modification Type:** General recommendation

---

### PM5 - Novel Missense at Same Residue

**Original ACMG Summary:** Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.

**VCEP Specifications:** Applicable for observed analogous residue positions in *PTPN11*. PM1 and PM5 may be used in conjunction at moderate levels, however, PM1 may not be applied if PM5_Strong is applied to avoid overweighting.

| Strength | Criteria |
|----------|----------|
| **Strong** | ≥2 different [likely] pathogenic residue changes at the same codon observed in ≥5 probands. |
| **Moderate** | 1 [likely] pathogenic residue change at the same codon. |

---

### PM6 - De Novo (Assumed)

**Original ACMG Summary:** Assumed de novo, but without confirmation of paternity and maternity.

**VCEP Specifications:** Same as PS2 - use point-based system above. Follow SVI recommendations for point-based scoring in conjunction with PS2.

See [PS2/PM6 Point System](#ps2pm6-point-system-per-proband) above.

---

### PP1 - Co-segregation

**Original ACMG Summary:** Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.

**VCEP Specifications:** Segregation in more than one family is recommended.

| Strength | Criteria |
|----------|----------|
| **Strong** | ≥7 informative meioses |
| **Moderate** | ≥5 informative meioses |
| **Supporting** | ≥3 informative meioses |

---

### PP2 - Missense in Constrained Gene

**Original ACMG Summary:** Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Supporting** | Missense z score is >3.09 in gnomAD. |

**Modification Type:** Gene-specific

---

### PP3 - Computational Evidence

**Original ACMG Summary:** Multiple lines of computational evidence support a deleterious effect on the gene or gene product.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Supporting** | For missense variants: REVEL ≥ 0.7. For splicing impact, predicted outcome must match disease mechanism. |

**Modification Type:** Disease-specific

---

### PP4 - Phenotype Specificity

**Original ACMG Summary:** Patient's phenotype or family history is highly specific for a disease with a single genetic etiology.

**VCEP Specifications:** *Not Applicable* - see PS4.

---

### PP5 - Reputable Source

**Original ACMG Summary:** Reputable source recently reports variant as pathogenic, but the evidence is not available to the laboratory to perform an independent evaluation.

**VCEP Specifications:** *Not Applicable*

This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PMID: 29543229).

---

## Benign Criteria

### BA1 - Allele Frequency >5%

**Original ACMG Summary:** Allele frequency is above 5% in population databases.

**VCEP Specification (Stand Alone):**
- gnomAD filtering allele frequency **≥0.05%** (0.0005)

**Modification Type:** Disease-specific

---

### BS1 - Frequency Greater Than Expected

**Original ACMG Summary:** Allele frequency is greater than expected for disorder.

**VCEP Specification (Strong):**
- gnomAD filtering allele frequency **≥0.025%** (0.00025)

**Modification Type:** Disease-specific

---

### BS2 - Observed in Healthy Adult

**Original ACMG Summary:** Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

**VCEP Specifications:** Strength adjustment using point-based scoring based on phenotypic specifications.

#### BS2 Point System (Per Individual)

| Phenotypic Consistency | Points per Individual |
|------------------------|:---------------------:|
| Healthy homozygous individual assessed for a RASopathy | -3 |
| Healthy heterozygous individual assessed for a RASopathy | -1 |
| No phenotypic information other than "unaffected" heterozygote\* | -0.25 |
| No clinical information or nonspecific clinical features | 0 |

\*Typically applicable to parental or sibling samples during clinical family evaluations.

#### BS2 Evidence Strength Thresholds

| Total Points | Strength Level |
|:------------:|----------------|
| ≤ -1 | BS2_Supporting |
| N/A | BS2_Moderate (not applicable) |
| ≤ -3 | BS2 (Strong) |

---

### BS3 - Functional Studies (No Effect)

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

**VCEP Specifications:** *Not Applicable*

> **Note:** Approved functional studies are available for each individual gene in the supplemental material. The SHP-2 Phosphatase Activity assay is the only approved assay for BS3 application in PTPN11 (at PS3/BS3 strength). All pathway-specific assays (RAS activation, MEK activation, ERK activation) are approved for PS3_Supporting only, with BS3 not applicable. Additional functional studies can be submitted to the expert panel for approval.

---

### BS4 - Lack of Segregation

**Original ACMG Summary:** Lack of segregation in affected members of a family.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | Requires only one informative meiosis showing lack of segregation. |

**Modification Type:** General recommendation

---

### BP1-BP7 - Benign Supporting

| Criterion | Status | Specifications |
|-----------|--------|----------------|
| **BP1** | Applicable (Supporting) | Truncating, LOF variant in a gene for which primarily missense, GOF variants are known to cause disease. Given the disease mechanism is gain-of-function for RASopathies, BP1 should be used for any truncating variant (nonsense, frameshift, affects canonical splice sites, initiation codon, entire gene or multi-exon deletion) in genes without established LOF correlation to disease. See supplemental material for dosage sensitivity information. |
| **BP2** | Applicable (Supporting / Moderate / Strong) | Points awarded for an alternative molecular cause of a RASopathy in the **same gene** (and/or in conjunction with BP5) and the phenotype is consistent with expected severity of the RASopathy. Supporting: ≥(-1) point; Moderate: ≥(-2) points; Strong: ≥(-4) points. |
| **BP3** | Not Applicable | No known benign repetitive areas in RASopathy genes. |
| **BP4** | Applicable (Supporting) | For missense variants: REVEL ≤0.3. For splicing variants: predicted outcome is negligible or does not match disease mechanism. |
| **BP5** | Applicable (Supporting / Moderate / Strong) | Points awarded for an alternative molecular cause of a RASopathy in a **different gene** (and/or in conjunction with BP2) and the phenotype is consistent with expected severity of the RASopathy. Points also awarded for phenotypes inconsistent with a RASopathy and fully explained by a different causative variant (e.g. WES testing). Supporting: ≥(-1) point; Moderate: ≥(-2) points; Strong: ≥(-4) points. |
| **BP6** | Not Applicable | This criterion is not for use as recommended by the ClinGen SVI VCEP Review Committee (PMID: 29543229). |
| **BP7** | Applicable (Supporting) | A synonymous (silent) variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved. Also applicable for intronic positions (except canonical splice sites) or non-coding variants; should be used in conjunction with BP4. |

#### BP5/BP2 Point System (Per Individual)

| Phenotypic Consistency | Points per Individual |
|------------------------|:---------------------:|
| Phenotype inconsistent with a RASopathy and causative variant has been identified, **-or-** molecular cause of a RASopathy is identified in a different RASopathy gene, **-or-** molecular cause of a RASopathy is identified in *trans* or *cis* with the variant being classified | -1 |
| Phenotype inconsistent with a RASopathy and no causative variant identified/reported | 0 |

#### BP5/BP2 Evidence Strength Thresholds

| Total Points | Strength Level |
|:------------:|----------------|
| ≤ -1 | BP5/BP2 (Supporting) |
| N/A | Moderate (not applicable) |
| ≤ -3 | BP5_Strong / BP2_Strong |

---

## Rules for Combining Criteria

### Pathogenic Classification

| Criteria Combination |
|---------------------|
| 1 Very Strong *(PS2_VeryStrong)* **AND** ≥1 Strong *(PS1, PS2, PS4, PM5_Strong, PM6_Strong, PP1_Strong)* |
| 1 Very Strong *(PS2_VeryStrong)* **AND** ≥2 Moderate *(PS2_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate)* |
| 1 Very Strong *(PS2_VeryStrong)* **AND** 1 Moderate *(PS2_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate)* **AND** 1 Supporting *(PS3_Supporting, PS4_Supporting, PM2_Supporting, PM6_Supporting, PP1, PP2, PP3)* |
| 1 Very Strong *(PS2_VeryStrong)* **AND** ≥2 Supporting *(PS3_Supporting, PS4_Supporting, PM2_Supporting, PM6_Supporting, PP1, PP2, PP3)* |
| ≥2 Strong *(PS1, PS2, PS4, PM5_Strong, PM6_Strong, PP1_Strong)* |
| 1 Strong *(PS1, PS2, PS4, PM5_Strong, PM6_Strong, PP1_Strong)* **AND** ≥3 Moderate *(PS2_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate)* |
| 1 Strong *(PS1, PS2, PS4, PM5_Strong, PM6_Strong, PP1_Strong)* **AND** 2 Moderate *(PS2_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate)* **AND** ≥2 Supporting *(PS3_Supporting, PS4_Supporting, PM2_Supporting, PM6_Supporting, PP1, PP2, PP3)* |
| 1 Strong *(PS1, PS2, PS4, PM5_Strong, PM6_Strong, PP1_Strong)* **AND** 1 Moderate *(PS2_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate)* **AND** ≥4 Supporting *(PS3_Supporting, PS4_Supporting, PM2_Supporting, PM6_Supporting, PP1, PP2, PP3)* |

### Likely Pathogenic Classification

| Criteria Combination |
|---------------------|
| 1 Very Strong *(PS2_VeryStrong)* **AND** 1 Moderate *(PS2_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate)* |
| 1 Strong *(PS1, PS2, PS4, PM5_Strong, PM6_Strong, PP1_Strong)* **AND** 1 Moderate *(PS2_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate)* |
| 1 Strong *(PS1, PS2, PS4, PM5_Strong, PM6_Strong, PP1_Strong)* **AND** ≥2 Supporting *(PS3_Supporting, PS4_Supporting, PM2_Supporting, PM6_Supporting, PP1, PP2, PP3)* |
| ≥3 Moderate *(PS2_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate)* |
| 2 Moderate *(PS2_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate)* **AND** ≥2 Supporting *(PS3_Supporting, PS4_Supporting, PM2_Supporting, PM6_Supporting, PP1, PP2, PP3)* |
| 1 Moderate *(PS2_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate)* **AND** ≥4 Supporting *(PS3_Supporting, PS4_Supporting, PM2_Supporting, PM6_Supporting, PP1, PP2, PP3)* |

### Benign Classification

| Criteria Combination |
|---------------------|
| ≥2 Strong *(BS1, BS2, BS4, BP2_Strong, BP5_Strong)* |
| 1 Stand Alone *(BA1)* |

### Likely Benign Classification

| Criteria Combination |
|---------------------|
| 1 Strong *(BS1, BS2, BS4, BP2_Strong, BP5_Strong)* **AND** 1 Supporting *(BS2_Supporting, BP1, BP2, BP4, BP5, BP7)* |
| ≥2 Supporting *(BS2_Supporting, BP1, BP2, BP4, BP5, BP7)* |
| 1 Strong *(BS1, BS2, BS4, BP2_Strong, BP5_Strong)* |
| 1 Strong *(BS1)* |

---

## Appendices

### Appendix A: Criteria Applicability Summary

| Criterion | Applicable | Max Strength | Notes |
|-----------|:----------:|:------------:|-------|
| PVS1 | No | - | LOF/haploinsufficiency not established for RASopathy; use non-adjusted criteria for LOF variants |
| PS1 | Yes | Strong | Gene-specific |
| PS2 | Yes | Very Strong | Point-based with PM6 |
| PS3 | Yes | Moderate | Two or more different approved assays |
| PS4 | Yes | Strong | Point-based; ≥5 points |
| PM1 | Yes | Moderate | N-SH2/PTPN domain interacting residues only |
| PM2 | Yes | Supporting | Absent from gnomAD |
| PM3 | No | - | Autosomal dominant disorder |
| PM4 | Yes | Moderate | No repetitive regions |
| PM5 | Yes | Strong | ≥2 P/LP residue changes at same codon in ≥5 probands |
| PM6 | Yes | Very Strong | Point-based with PS2 |
| PP1 | Yes | Strong | ≥7 informative meioses |
| PP2 | Yes | Supporting | Missense z score >3.09 |
| PP3 | Yes | Supporting | REVEL ≥0.7 |
| PP4 | No | - | See PS4 |
| PP5 | No | - | Not recommended (PMID: 29543229) |
| BA1 | Yes | Stand Alone | gnomAD FAF ≥0.05% |
| BS1 | Yes | Strong | gnomAD FAF ≥0.025% |
| BS2 | Yes | Strong | Point-based; ≤-3 points |
| BS3 | No | - | See supplemental; only SHP-2 phosphatase assay approved for BS3 |
| BS4 | Yes | Strong | 1 informative meiosis |
| BP1 | Yes | Supporting | Truncating/LOF variant in GOF gene |
| BP2 | Yes | Strong | Point-based; alternative RASopathy cause in same gene |
| BP3 | No | - | No benign repetitive areas |
| BP4 | Yes | Supporting | REVEL ≤0.3 |
| BP5 | Yes | Strong | Point-based; alternative RASopathy cause in different gene |
| BP6 | No | - | Not recommended (PMID: 29543229) |
| BP7 | Yes | Supporting | Synonymous + no splicing impact + not conserved |

### Appendix B: Population Frequency Thresholds Summary

| Criterion | Threshold | Strength |
|-----------|-----------|----------|
| BA1 | ≥0.05% (gnomAD FAF) | Stand Alone |
| BS1 | ≥0.025% (gnomAD FAF) | Strong |
| PM2 | Absent from gnomAD | Supporting |

### Appendix C: PM1 Domain Residues

Directly interacting residues between N-SH2 and PTPN domains:

AA 4, AA 7-9, AA 58-63, AA 69-77, AA 247, AA 251, AA 255, AA 256, AA 258, AA 261, AA 265, AA 278-281, AA 284

### Appendix D: Approved Functional Assays Summary

| Assay | Specificity | Approved Genes | PS3 Strength | BS3 |
|-------|------------|----------------|:------------:|:---:|
| SHP-2 Phosphatase Activity | Gene-specific (PTPN11) | PTPN11 | Supporting (PS3/BS3 for SHP-2) | Yes |
| RAS Activation Assay | Pathway-specific | MRAS, HRAS, KRAS, NRAS, SOS1, SOS2, LZTR1, RRAS2, RIT1 | Supporting | N/A |
| MEK Activation Assay | Pathway-specific | PTPN11, MRAS, NRAS, HRAS, KRAS, MAP2K1, MAP2K2, RAF1, BRAF, SOS1, SOS2, LZTR1, RIT1, RRAS2 | Supporting | N/A |
| ERK Activation Assay | Pathway-specific | PTPN11, MRAS, HRAS, KRAS, NRAS, MAP2K1, MAP2K2, RAF1, BRAF, SOS1, SOS2, LZTR1, RIT1, RRAS2 | Supporting | N/A |

> Two or more unique assay types (e.g. SHP-2 phosphatase + MEK activation) for a given variant provides sufficient evidence to upgrade PS3 to Moderate strength.

### Appendix E: Reference PMIDs

| PMID | Reference |
|------|-----------|
| 29543229 | ClinGen SVI recommendation to discontinue PP5/BP6 |
| 31892348 | SVI functional evidence PS3/BS3 recommendations |
| 14974085 | Fragale et al. (2004) - SHP-2 phosphatase, MEK, ERK studies |
| 15834506 | Niihori et al. (2005) - SHP-2 phosphatase, MEK, ERK studies |
| 17177198 | Bocchinfuso et al. (2007) - SHP-2 phosphatase studies |
| 18372317 | Martinelli et al. (2008) - SHP-2 phosphatase studies |

### Appendix F: References

1. SVI Proposal for De Novo Criteria v1.1: https://clinicalgenome.org/site/assets/files/3461/svi_proposal_for_de_novo_criteria_v1_1.pdf

---

## Version History

| Version | Date | Notes |
|---------|------|-------|
| 2.3.0 | 12/3/2024 | Submitting Pilot Rules. All pilot variants attached in LZTR1 submission. "Observed in ≥5 probands" removed from PM5 at Moderate strength. |

---

*This document was compiled from ClinGen VCEP specifications and ClinGen SVI recommendations. For the most current version, please refer to the ClinGen website.*
