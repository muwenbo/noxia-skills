# ClinGen RASopathy Expert Panel Variant Interpretation Guidelines for KRAS

**Version:** 2.3.0
**Released:** 12/3/2024
**Affiliation:** RASopathy VCEP
**Based on:** Richards et al., 2015 ACMG/AMP Guidelines

---

## Gene Information

| Attribute | Value |
|-----------|-------|
| **Gene** | KRAS (HGNC:6407) |
| **HGNC Name** | KRAS proto-oncogene, GTPase |
| **Transcript** | NM_004985.5 |
| **Disease** | RASopathy (MONDO:0021060) |
| **Inheritance** | Autosomal dominant |

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

**Caveats:**
- Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7)
- Use caution interpreting LOF variants at the extreme 3' end of a gene
- Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact
- Use caution in the presence of multiple transcripts

**VCEP Specification:** *Not Applicable*

> **Comment:** Not applicable. Loss of function is not a known disease mechanism for KRAS-associated RASopathies (gain-of-function mechanism).

---

### PS1 - Same Amino Acid Change

**Original ACMG Summary:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.

**VCEP Specifications:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Strong** | Same amino acid change as a previously established pathogenic variant regardless of nucleotide change. Applicable for observed analogous residue positions in *HRAS*, *KRAS*, *MRAS*, *NRAS*, *RIT1*, and *RRAS2*. | Analogous Gene |

> **Note:** Beware of changes that impact splicing rather than at the amino acid/protein level.

---

### PS2 - De Novo (Confirmed)

**Original ACMG Summary:** De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.

**VCEP Specifications:** Follow SVI recommendations for point-based scoring in conjunction with PM6 (see Reference 1) and phenotypic specifications: full points awarded with RASopathy phenotypes, reduced points applicable to cases with minimal phenotypic information (i.e. prenatal cases, cases with a clinical order of a RASopathy panel without clinical information, and cases with limited clinical information in other global tests (such as WES)).

#### PS2/PM6 Point System

| Phenotypic Consistency | Confirmed *de novo* (PS2) | Assumed *de novo* (PM6) |
|------------------------|---------------------------|-------------------------|
| Phenotype is consistent with a RASopathy* | 2 points | 1 point |
| Limited phenotypic information** | 1 point | 0.5 points |
| Phenotype not consistent with RASopathy | 0 points | 0 points |

*\*Exclusive of prenatal cases*

*\*\*Applicable to prenatal cases, cases with a clinical order of a RASopathy panel without clinical information, and cases with limited clinical information in other global tests (such as WES). Phenotypes for prenatal cases include hypertrophic cardiomyopathy, increased nuchal translucency, cystic hygroma, or hydrops.*

#### Evidence Strength Thresholds

| Strength Level | Points Required |
|----------------|-----------------|
| **Supporting** (PS2_Supporting or PM6_Supporting) | 0.5 points |
| **Moderate** (PS2_Moderate or PM6) | 1 point |
| **Strong** (PS2 or PM6_Strong) | 2 points |
| **Very Strong** (PS2_VeryStrong or PM6_VeryStrong) | 4 points |

---

### PS3 - Functional Studies

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.

**VCEP Specifications:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product. Approved assays are available in the supplemental materials.

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Moderate** | Two or more different approved assays | Disease-specific, Gene-specific, Strength |
| **Supporting** | One approved assay | Disease-specific, Gene-specific, Strength |

#### Approved Functional Assays for KRAS

##### 1. RAS Activation Assay

| Attribute | Details |
|-----------|---------|
| **Description** | Measure the bound RAS protein that immunoprecipitated with RAF1 or RBD (synthetic) |
| **PMIDs** | 20949621, 23059812 |
| **Authors** | Gremer, Cirstea |
| **Materials** | Cos-1 cells with HA-RAS or COS-7 cells transfected with wildtype and KRAS variants |
| **Readout** | Semi-quantitative (Qualitative) - Measure the bound RAS protein that immunoprecipitated with RAF1 or RBD |
| **Threshold (Normal)** | Normal (WT) pattern |
| **Threshold (Abnormal)** | Increased RAS/RBD complexes compared with positive control range in assay |
| **Proposed Strength** | PS3_Supporting; BS3_NA |
| **Validation Controls (P/LP)** | 10 variants: G12V-P, F28L-VUS, V14I-P, Q22E-P, P34R-P/LP, P34L-P, T58I-P, G60R-P, K147E-P/LP, F156L-P |
| **Validation Controls (B/LB)** | 4 variants: K5N-P, Q22R-P, D153V-P, Y71H-P |

##### 2. MEK Activation Assay

| Attribute | Details |
|-----------|---------|
| **Description** | Measure the ratio of phosphorylated MEK to unphosphorylated MEK, basally and following RTK stimulation |
| **PMIDs** | 20949621, 23059812 |
| **Authors** | Cirstea, Gremer |
| **Materials** | COS-7 cells transfected with wildtype or variant |
| **Readout** | Semi-quantitative (Qualitative) - pMEK/MEK ratio basally and/or after RTK stimulation |
| **Threshold (Normal)** | Normal (WT) pattern |
| **Threshold (Abnormal)** | Increased pMEK/MEK ratio compared with controls |
| **Proposed Strength** | PS3_Supporting; BS3_NA |
| **Validation Controls (P/LP)** | 14 variants: K5N-P, G12V-P, F28L-VUS, V14I-P, Q22E-P, Q22R-P, P34L-P, P34R-P/LP, T58I-P, G60R-P, Y71H-P, K147E-P/LP, D153V-P, F156L-P |

##### 3. ERK Activation Assay

| Attribute | Details |
|-----------|---------|
| **Description** | Measure the ratio of phosphorylated ERK to unphosphorylated ERK, basally and following stimulation |
| **PMIDs** | 23059812, 20949621 |
| **Authors** | Cirstea, Gremer |
| **Materials** | COS-7 cells transfected with wildtype or variant |
| **Readout** | Semi-quantitative (Qualitative) - pERK/ERK ratio basally and after stimulation |
| **Threshold (Normal)** | Normal (WT) pattern |
| **Threshold (Abnormal)** | Constitutively active, increased phosphorylation protein, and/or prolonged phosphorylation |
| **Proposed Strength** | PS3_Supporting; BS3_NA |
| **Validation Controls (P/LP)** | 12 variants: K5N-P, G12V-P, V14I-P, Q22E-P, Q22R-P, F28L-VUS, P34L-P, P34R-P/LP, T58I-P, G60R-P, K147E-P/LP, F156L-P |
| **Validation Controls (B/LB)** | 2 variants: Y71H-P, D153V-P |

---

### PS4 - Prevalence in Affected

**Original ACMG Summary:** The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.

**VCEP Specifications:** Strength adjustment using point-based scoring for autosomal dominant cases with phenotypic specifications: full points awarded with RASopathy phenotypes, reduced points applicable to cases with minimal phenotypic information (i.e. prenatal cases, cases with a clinical order of a RASopathy panel without clinical information, and cases with limited clinical information in other global tests (such as WES)).

#### PS4 Point System

| Phenotypic Consistency | Points per Proband |
|------------------------|-------------------|
| Individual well-phenotyped with features of a RASopathy | 1 |
| Limited phenotypic information compatible with RASopathy* | 0.5 |
| No clinical information or isolated clinical features | 0 |
| Well-phenotyped but consistent with non-RASopathy disorder** | -1 |

*\*Applicable to prenatal cases, cases with a clinical order of a RASopathy panel without clinical information, and cases with limited clinical information in other global tests (such as WES). Phenotypes for prenatal cases include hypertrophic cardiomyopathy, increased nuchal translucency, cystic hygroma, or hydrops.*

*\*\*Negative points for PS4 represent proband affected with a non-RASopathy congenital disorder rather than a healthy individual (BS2). This typically applies to probands tested by exome analysis with multiple other clinical features supporting a distinct syndromic disorder. (e.g. CHARGE, CdLS)*

#### PS4 Strength Thresholds

| Strength Level | Points Required |
|----------------|-----------------|
| **Supporting** (PS4_Supporting) | 1.0 point |
| **Moderate** (PS4_Moderate) | 3.0 points |
| **Strong** (PS4) | 5.0 points |

---

### PM1 - Mutational Hot Spot

**Original ACMG Summary:** Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.

**VCEP Specifications:** Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation. PM1 and PM5 may be used in conjunction at moderate levels, however, PM1 may not be applied if PM5_Strong is applied to avoid overweighting.

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Moderate** | Applicable only to critical and well-established functional domains available in the supplementary table. Not applicable to specific amino acid residues (see PM5). | Gene-specific |

#### Critical Functional Domains for KRAS

| Domain | Amino Acid Positions |
|--------|---------------------|
| **P-loop** | AA 10-17 |
| **Switch I (SW1)** | AA 25-40 |
| **Switch II (SW2)** | AA 57-64 |
| **SAK** | AA 145-156 |

> **Note:** PM1 and PM5 may be used in conjunction at moderate levels, however, PM1 may not be applied if PM5_Strong is applied to avoid overweighting.

---

### PM2 - Absent from Controls

**Original ACMG Summary:** Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

**VCEP Specification (Supporting only):**

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Supporting** | The variant must be absent from controls (gnomAD) | Strength |

> **Caveat:** Population data for indels may be poorly called by next generation sequencing.

---

### PM3 - In Trans with Pathogenic

**Original ACMG Summary:** For recessive disorders, detected in trans with a pathogenic variant.

**VCEP Specification:** *Not Applicable*

> **Comment:** Not applicable. KRAS-associated RASopathies follow autosomal dominant inheritance.

---

### PM4 - Protein Length Changes

**Original ACMG Summary:** Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

**VCEP Specifications:** Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Moderate** | No known repetitive areas in gene. Use as described. | General recommendation |

---

### PM5 - Novel Missense at Same Residue

**Original ACMG Summary:** Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.

**VCEP Specifications:** Applicable for observed analogous residue positions in *HRAS*, *KRAS*, *MRAS*, *NRAS*, *RIT1*, and *RRAS2*. PM1 and PM5 may be used in conjunction at moderate levels, however, PM1 may not be applied if PM5_Strong is applied to avoid overweighting.

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Strong** | ≥2 different [likely] pathogenic residue changes at the same codon observed in ≥5 probands | Analogous Gene, Strength |
| **Moderate** | 1 [likely] pathogenic residue change at the same codon | Analogous Gene, Disease-specific |

> **Caveat:** Beware of changes that impact splicing rather than at the amino acid/protein level.

---

### PM6 - De Novo (Assumed)

**Original ACMG Summary:** Assumed de novo, but without confirmation of paternity and maternity.

**VCEP Specifications:** Follow SVI recommendations for point-based scoring in conjunction with PS2 (see Reference 1) and phenotypic specifications: full points awarded with RASopathy phenotypes, reduced points applicable to cases with minimal phenotypic information (i.e. prenatal cases, cases with a clinical order of a RASopathy panel without clinical information, and cases with limited clinical information in other global tests (such as WES)).

| Strength | Criteria | Points |
|----------|----------|--------|
| **Strong** | PM6_Strong | 2 points |
| **Moderate** | PM6 | 1 point |
| **Supporting** | PM6_Supporting | 0.5 points |

> **Note:** See PS2 section for the complete point-based scoring system.

---

### PP1 - Co-segregation

**Original ACMG Summary:** Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.

**VCEP Specifications:** Segregation in more than one family is recommended.

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Strong** | ≥7 informative meioses | Strength |
| **Moderate** | ≥5 informative meioses | Strength |
| **Supporting** | ≥3 informative meioses | Disease-specific |

---

### PP2 - Missense in Constrained Gene

**Original ACMG Summary:** Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.

**VCEP Specification:** *Not Applicable*

> **Comment:** Not applicable because missense z score is <3.09 in gnomAD.

---

### PP3 - Computational Evidence

**Original ACMG Summary:** Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).

**VCEP Specifications:**

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Supporting** | For missense variants: REVEL ≥ 0.7. For splicing impact, predicted outcome must match disease mechanism. | Disease-specific |

> **Caveat:** As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.

---

### PP4 - Phenotype Specificity

**Original ACMG Summary:** Patient's phenotype or family history is highly specific for a disease with a single genetic etiology.

**VCEP Specification:** *Not Applicable*

> **Comment:** Not applicable, see PS4.

---

### PP5 - Reputable Source

**Original ACMG Summary:** Reputable source recently reports variant as pathogenic, but the evidence is not available to the laboratory to perform an independent evaluation.

**VCEP Specification:** *Not Applicable*

> This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PubMed: 29543229).

---

## Benign Criteria

### BA1 - Allele Frequency >5%

**Original ACMG Summary:** Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

**VCEP Specification (Stand Alone):**

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Stand Alone** | gnomAD filtering allele frequency ≥0.05% | Disease-specific |

---

### BS1 - Frequency Greater Than Expected

**Original ACMG Summary:** Allele frequency is greater than expected for disorder.

**VCEP Specification (Strong):**

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Strong** | gnomAD filtering allele frequency ≥0.025% | Disease-specific |

---

### BS2 - Observed in Healthy Adult

**Original ACMG Summary:** Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

**VCEP Specifications:** Strength adjustment using point-based scoring based on phenotypic specifications. Phenotypic specifications: based on healthy homozygote or heterozygote individuals, reduced points for apparently unaffected heterozygous individuals, applicable to parent or sibling samples during clinical family evaluations.

#### BS2 Point System

| Phenotypic Consistency | Points per Individual |
|------------------------|----------------------|
| Healthy homozygous individual assessed for a RASopathy | -3 |
| Healthy heterozygous individual assessed for a RASopathy | -1 |
| No phenotypic information other than "unaffected" heterozygote* | -0.25 |
| No clinical information or nonspecific clinical features | 0 |

*\*Typically applicable to parental or sibling samples during clinical family evaluations.*

#### BS2 Strength Thresholds

| Strength Level | Points Required |
|----------------|-----------------|
| **Supporting** (BS2_Supporting) | -1 points |
| **Moderate** | N/A |
| **Strong** (BS2) | -3.0 points |

---

### BS3 - Functional Studies (No Effect)

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

**VCEP Specification:** *Not Applicable*

> **Comment:** Approved functional studies are available for each individual gene in the supplemental material. Additional functional studies can be submitted to the expert panel for approval.

---

### BS4 - Lack of Segregation

**Original ACMG Summary:** Lack of segregation in affected members of a family.

**VCEP Specifications:** Lack of segregation in affected members of a family.

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Strong** | Requires only one informative meiosis | General recommendation |

> **Caveat:** The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.

---

### BP1-BP7 - Benign Supporting

| Criterion | Status | Specification |
|-----------|--------|---------------|
| **BP1** | Modified | Truncating, LOF variant in a gene for which primarily missense, GOF variants are known to cause disease. This rule has contraindications for use with RASopathies. Given the disease mechanism is gain-of-function for RASopathies, BP1 should be used for any truncating variant (nonsense, frameshift, affects canonical splice sites, initiation codon, entire gene or multi-exon deletion) in genes without established LOF correlation to disease. See the supplemental material regarding dosage sensitivity information for each individual gene and potential association to disorders associated with LOF variants. |
| **BP2** | Modified (Point-based) | Points are awarded for an alternative molecular cause of a RASopathy in the same gene (and/or in conjunction with BP5) and the phenotype is consistent with expected severity of the RASopathy. **Supporting:** ≥(-1) Point; **Moderate:** ≥(-2) Points; **Strong:** ≥(-4) Points |
| **BP3** | Not Applicable | No known benign repetitive areas in RASopathy genes. |
| **BP4** | Modified | For missense variants: REVEL ≤0.3. For splicing variants: predicted outcome is negligible or does not match disease mechanism. |
| **BP5** | Modified (Point-based) | Points are awarded for an alternative molecular cause of a RASopathy in a different gene (and/or in conjunction with BP2) and the phenotype is consistent with expected severity of the RASopathy. Points are also awarded for phenotypes inconsistent with a RASopathy and fully explained by a different causative variant (e.g. WES testing). **Supporting:** ≥(-1) Point; **Moderate:** ≥(-2) Points; **Strong:** ≥(-4) Points |
| **BP6** | Not Applicable | This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PubMed: 29543229). |
| **BP7** | Modified | A synonymous (silent) variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved. This rule is also applicable for intronic positions (except canonical splice sites) or non-coding variants and should be used in conjunction with BP4. |

#### BP5/BP2 Point System

| Phenotypic Consistency | Points per Individual |
|------------------------|----------------------|
| Phenotype inconsistent with a RASopathy and causative variant has been identified, -or- Molecular cause of a RASopathy is identified in a different RASopathy gene, -or- Molecular cause of a RASopathy is identified in *trans* or *cis* with the variant being classified | -1 |
| Phenotype inconsistent with a RASopathy and no causative variant identified/reported | 0 |

#### BP5/BP2 Strength Thresholds

| Strength Level | Points Required |
|----------------|-----------------|
| **Supporting** (BP5/BP2) | -1 points |
| **Moderate** | N/A |
| **Strong** (BP5_Strong/BP2_Strong) | -3.0 points |

---

## Rules for Combining Criteria

### Pathogenic Classification

| Criteria Combination |
|---------------------|
| 1 Very Strong (PS2_Very Strong) **AND** ≥1 Strong (PS1, PS2, PS4, PM5_Strong, PM6_Strong, PP1_Strong) |
| 1 Very Strong (PS2_Very Strong) **AND** ≥2 Moderate (PS2_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate) |
| 1 Very Strong (PS2_Very Strong) **AND** 1 Moderate (PS2_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate) **AND** 1 Supporting (PS3_Supporting, PS4_Supporting, PM2_Supporting, PM6_Supporting, PP1, PP3) |
| 1 Very Strong (PS2_Very Strong) **AND** ≥2 Supporting (PS3_Supporting, PS4_Supporting, PM2_Supporting, PM6_Supporting, PP1, PP3) |
| ≥2 Strong (PS1, PS2, PS4, PM5_Strong, PM6_Strong, PP1_Strong) |
| 1 Strong (PS1, PS2, PS4, PM5_Strong, PM6_Strong, PP1_Strong) **AND** ≥3 Moderate (PS2_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate) |
| 1 Strong (PS1, PS2, PS4, PM5_Strong, PM6_Strong, PP1_Strong) **AND** 2 Moderate (PS2_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate) **AND** ≥2 Supporting (PS3_Supporting, PS4_Supporting, PM2_Supporting, PM6_Supporting, PP1, PP3) |
| 1 Strong (PS1, PS2, PS4, PM5_Strong, PM6_Strong, PP1_Strong) **AND** 1 Moderate (PS2_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate) **AND** ≥4 Supporting (PS3_Supporting, PS4_Supporting, PM2_Supporting, PM6_Supporting, PP1, PP3) |

### Likely Pathogenic Classification

| Criteria Combination |
|---------------------|
| 1 Very Strong (PS2_Very Strong) **AND** 1 Moderate (PS2_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate) |
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

### Appendix A: Critical Functional Domains

| Domain | KRAS Positions | Description |
|--------|---------------|-------------|
| **P-loop** | AA 10-17 | Phosphate-binding loop |
| **Switch I (SW1)** | AA 25-40 | Effector binding region |
| **Switch II (SW2)** | AA 57-64 | GTPase activity regulation |
| **SAK** | AA 145-156 | C-terminal region |

### Appendix B: Analogous Residue Mapping

The following genes have analogous residue positions that can be used for PS1 and PM5 criteria:
- HRAS
- KRAS
- MRAS
- NRAS
- RIT1
- RRAS2

Reference sequences:
| Gene | RefSeq Protein | RefSeq Transcript |
|------|----------------|-------------------|
| HRAS | NP_005334.1 | - |
| KRAS | NP_004976.2 | NM_004985.5 |
| MRAS | NP_036351.3 | - |
| NRAS | NP_002515.1 | - |
| RIT1 | NP_008843.1 | - |
| RRAS2 | NP_036382.2 | - |

### Appendix C: Population Frequency Thresholds Summary

| Criterion | Threshold | Strength |
|-----------|-----------|----------|
| BA1 | ≥0.05% (gnomAD FAF) | Stand Alone |
| BS1 | ≥0.025% (gnomAD FAF) | Strong |
| PM2 | Absent from gnomAD | Supporting |

### Appendix D: Computational Predictor Thresholds

| Predictor | Pathogenic Threshold (PP3) | Benign Threshold (BP4) |
|-----------|---------------------------|------------------------|
| REVEL | ≥0.7 | ≤0.3 |

### Appendix E: References

1. ClinGen SVI Proposal for de novo Criteria v1.1: https://clinicalgenome.org/site/assets/files/3461/svi_proposal_for_de_novo_criteria_v1_1.pdf
2. Biesecker LG, Harrison SM; ClinGen Sequence Variant Interpretation Working Group. The ACMG/AMP reputable source criteria for the interpretation of sequence variants. Genet Med. 2018;20(12):1687-1688. (PubMed: 29543229)

---

## Version History

| Version | Date | Notes |
|---------|------|-------|
| 2.3.0 | 12/3/2024 | Submitting Pilot Rules. All pilot variants are attached in the LZTR1 submission. "Observed in ≥5 probands" removed from PM5 at Moderate strength. |

---

*This document was compiled from ClinGen RASopathy VCEP specifications and ClinGen SVI recommendations. For the most current version, please refer to the ClinGen website.*
