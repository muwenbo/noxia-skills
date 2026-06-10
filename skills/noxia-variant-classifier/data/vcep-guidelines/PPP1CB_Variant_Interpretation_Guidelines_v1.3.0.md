# ClinGen RASopathy VCEP Variant Interpretation Guidelines for PPP1CB

**Version:** 1.3.0
**Released:** 12/3/2024
**Affiliation:** RASopathy VCEP
**Based on:** Richards et al., 2015 ACMG/AMP Guidelines

---

## Gene Information

| Attribute | Value |
|-----------|-------|
| **Gene** | PPP1CB (HGNC:9282) |
| **HGNC Name** | protein phosphatase 1 catalytic subunit beta |
| **Transcript** | NM_002709.3 |
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

**VCEP Specifications:**

***Not Applicable***

**Comments:** Not applicable. The disease mechanism for PPP1CB-associated RASopathy is gain-of-function, not loss-of-function. PVS1 should not be applied.

---

### PS1 - Same Amino Acid Change

**Original ACMG Summary:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.

**VCEP Specifications:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Strong** | Same amino acid change as a previously established pathogenic variant in *PPP1CB* regardless of nucleotide change. | Analogous Gene |

**Caveat:** Beware of changes that impact splicing rather than at the amino acid/protein level.

---

### PS2 - De Novo (Confirmed)

**Original ACMG Summary:** De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.

**VCEP Specifications:** Follow SVI recommendations for point-based scoring in conjunction with PM6 (see Reference 1) and phenotypic specifications: full points awarded with RASopathy phenotypes, reduced points applicable to cases with minimal phenotypic information (i.e. prenatal cases, cases with a clinical order of a RASopathy panel without clinical information, and cases with limited clinical information in other global tests (such as WES)).

#### PS2/PM6 Point System (Per Proband)

| Phenotypic Consistency | Confirmed *de novo* (PS2) | Assumed *de novo* (PM6) |
|------------------------|---------------------------|-------------------------|
| Phenotype is consistent with a RASopathy\* | 2 | 1 |
| Limited phenotypic information\*\* | 1 | 0.5 |
| Phenotype not consistent with RASopathy | 0 | 0 |

\*Exclusive of prenatal cases.
\*\*Applicable to prenatal cases, cases with a clinical order of a RASopathy panel without clinical information, and cases with limited clinical information in other global tests (such as WES). Phenotypes for prenatal cases include hypertrophic cardiomyopathy, increased nuchal translucency, cystic hygroma, or hydrops.

#### PS2/PM6 Evidence Strength Thresholds

| Points | Strength Level |
|--------|----------------|
| 0.5 | Supporting (PS2_Supporting or PM6_Supporting) |
| 1.0 | Moderate (PS2_Moderate or PM6) |
| 2.0 | Strong (PS2 or PM6_Strong) |
| 4.0 | Very Strong (PS2_VeryStrong or PM6_VeryStrong) |

---

### PS3 - Functional Studies

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.

**VCEP Specifications:**

***Not Applicable***

**Comments:** Approved functional studies are available for each individual gene in the supplemental material. Additional functional studies can be submitted to the expert panel for approval. PS3 is not applicable for PPP1CB at this time.

**Note from functional assay comparisons:** Effect on MAPK and MEK/ERK phosphorylation needs elucidation for both PPP1CB and SHOC2. The VCEP does not recommend application of PS3 at any level for PPP1CB due to uncertainty of the impact on approved RASopathy functional studies.

#### Approved RASopathy Functional Assays (General Reference)

The following assays are approved by the RASopathy VCEP for other genes in the panel. They are listed for reference but **none are currently approved for PPP1CB**:

| Assay | General Description | Assay Specificity |
|-------|---------------------|-------------------|
| RAS Activation Assay | Measures the bound RAS protein that immunoprecipitated with RAF1 or RBD (synthetic) | Pathway Specific: works for genes upstream from RAS and RAS proteins themselves but not for downstream components |
| MEK Activation Assay | Measures the ratio of phosphorylated MEK to unphosphorylated MEK, basally and following RTK stimulation | Pathway Specific |
| ERK Activation Assay | Measures the ratio of phosphorylated ERK to unphosphorylated ERK, basally and following stimulation | Pathway Specific |
| SHP-2 Phosphatase Activity | Measures the ratio of phosphorylated and dephosphorylated SHP2 | Gene Specific (PTPN11) |
| BRAF Kinase Activity | Measures activity of kinase phosphorylating species of MEK and ERK in transfected cells | Gene Specific (BRAF) |
| RAF1 Kinase Activity | Measures activity of kinase phosphorylating species of MEK and ERK in transfected cells | Gene Specific (RAF1) |
| LZTR1 Stability Localization | Expression levels and stability of LZTR1 variants by Western blot analysis | Gene Specific (LZTR1) |

**Important:** Prior to evaluation of an assay for a variant, all assays are expected to be validated by the performing laboratory in accordance with standard procedures with all appropriate control inclusions (PMID: 31892348). Two or more unique assay types for a given variant provides sufficient evidence to upgrade PS3 to Moderate strength (for genes where PS3 is applicable).

---

### PS4 - Prevalence in Affected

**Original ACMG Summary:** The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.

**VCEP Specifications:** Strength adjustment using point-based scoring for autosomal dominant cases with phenotypic specifications: full points awarded with RASopathy phenotypes, reduced points applicable to cases with minimal phenotypic information (i.e. prenatal cases, cases with a clinical order of a RASopathy panel without clinical information, and cases with limited clinical information in other global tests (such as WES)).

#### PS4 Point System (Per Proband)

| Phenotypic Consistency | Points per Proband |
|------------------------|--------------------|
| Individual well-phenotyped with features of a RASopathy | 1 |
| Limited phenotypic information compatible with RASopathy\* | 0.5 |
| No clinical information or isolated clinical features | 0 |
| Well-phenotyped but consistent with non-RASopathy disorder\*\* | -1 |

\*Applicable to prenatal cases, cases with a clinical order of a RASopathy panel without clinical information, and cases with limited clinical information in other global tests (such as WES). Phenotypes for prenatal cases include hypertrophic cardiomyopathy, increased nuchal translucency, cystic hygroma, or hydrops.
\*\*Negative points for PS4 represent proband affected with a non-RASopathy congenital disorder rather than a healthy individual (BS2). This typically applies to probands tested by exome analysis with multiple other clinical features supporting a distinct syndromic disorder (e.g. CHARGE, CdLS).

#### PS4 Evidence Strength Thresholds

| Total Points | Strength Level |
|--------------|----------------|
| >=1.0 | Supporting (PS4_Supporting) |
| >=3.0 | Moderate (PS4_Moderate) |
| >=5.0 | Strong (PS4) |

---

### PM1 - Mutational Hot Spot

**Original ACMG Summary:** Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.

**VCEP Specifications:**

***Not Applicable***

**Comments:** Not applicable for PPP1CB.

---

### PM2 - Absent from Controls

**Original ACMG Summary:** Absent from controls (or at extremely low frequency if recessive) in population databases.

**VCEP Specification (Supporting only):**
- The variant must be **absent from controls (gnomAD)**
- Modification Type: Strength (downgraded from Moderate to Supporting)

---

### PM3 - In Trans with Pathogenic

**Original ACMG Summary:** For recessive disorders, detected in trans with a pathogenic variant.

**VCEP Specifications:**

***Not Applicable***

**Comments:** Not applicable. PPP1CB-associated RASopathy follows autosomal dominant inheritance.

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

**VCEP Specifications:** Applicable for observed analogous residue positions in PPP1CB. PM1 and PM5 may be used in conjunction at moderate levels, however, PM1 may not be applied if PM5_Strong is applied to avoid overweighting.

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Strong** | >=2 different [likely] pathogenic residue changes at the same codon observed in >=5 probands. | Strength |
| **Moderate** | 1 [likely] pathogenic residue change at the same codon. | Disease-specific |

---

### PM6 - De Novo (Assumed)

**Original ACMG Summary:** Assumed de novo, but without confirmation of paternity and maternity.

**VCEP Specifications:** Follow SVI recommendations for point-based scoring in conjunction with PS2 (see Reference 1) and phenotypic specifications: full points awarded with RASopathy phenotypes, reduced points applicable to cases with minimal phenotypic information (i.e. prenatal cases, cases with a clinical order of a RASopathy panel without clinical information, and cases with limited clinical information in other global tests (such as WES)).

Uses the same point-based system as PS2 - see [PS2/PM6 Point System](#ps2pm6-point-system-per-proband) above.

| Strength | Points | Modification Type |
|----------|--------|-------------------|
| **Strong** | 2 Points | Strength |
| **Moderate** | 1 Point | None |
| **Supporting** | 0.5 Points | Strength |

---

### PP1 - Co-segregation

**Original ACMG Summary:** Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.

**VCEP Specifications:** Segregation in more than one family is recommended.

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Strong** | >=7 informative meioses | Strength |
| **Moderate** | >=5 informative meioses | Strength |
| **Supporting** | >=3 informative meioses | Disease-specific |

---

### PP2 - Missense in Constrained Gene

**Original ACMG Summary:** Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.

**VCEP Specifications:** Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Supporting** | Missense z score is >3.09 in gnomAD. | Gene-specific |

---

### PP3 - Computational Evidence

**Original ACMG Summary:** Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).

**VCEP Specifications:** For missense variants: REVEL >= 0.7. For splicing impact, predicted outcome must match disease mechanism.

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Supporting** | For missense variants: REVEL >= 0.7. For splicing impact, predicted outcome must match disease mechanism. | Disease-specific |

**Caveat:** PP3 can be used only once in any evaluation of a variant.

---

### PP4 - Phenotype Specificity

**Original ACMG Summary:** Patient's phenotype or family history is highly specific for a disease with a single genetic etiology.

**VCEP Specifications:**

***Not Applicable***

**Comments:** Not applicable, see PS4. Phenotypic information is incorporated into the PS4 point-based scoring system.

---

### PP5 - Reputable Source

**Original ACMG Summary:** Reputable source recently reports variant as pathogenic, but the evidence is not available to the laboratory to perform an independent evaluation.

**VCEP Specifications:**

***Not Applicable***

This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PMID: 29543229).

---

## Benign Criteria

### BA1 - Allele Frequency >5%

**Original ACMG Summary:** Allele frequency is above 5% in population databases.

**VCEP Specification (Stand Alone):**
- gnomAD filtering allele frequency **>=0.05%**
- Modification Type: Disease-specific

---

### BS1 - Frequency Greater Than Expected

**Original ACMG Summary:** Allele frequency is greater than expected for disorder.

**VCEP Specification (Strong):**
- gnomAD filtering allele frequency **>=0.025%**
- Modification Type: Disease-specific

---

### BS2 - Observed in Healthy Adult

**Original ACMG Summary:** Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

**VCEP Specifications:** Strength adjustment using point-based scoring based on phenotypic specifications. Phenotypic specifications: based on healthy homozygote or heterozygote individuals, reduced points for apparently unaffected heterozygous individuals, applicable to parent or sibling samples during clinical family evaluations.

#### BS2 Point System (Per Individual)

| Phenotypic Consistency | Points per Individual |
|------------------------|-----------------------|
| Healthy homozygous individual assessed for a RASopathy | -3 |
| Healthy heterozygous individual assessed for a RASopathy | -1 |
| No phenotypic information other than "unaffected" heterozygote\* | -0.25 |
| No clinical information or nonspecific clinical features | 0 |

\*Typically applicable to parental or sibling samples during clinical family evaluations.

#### BS2 Evidence Strength Thresholds

| Total Points | Strength Level |
|--------------|----------------|
| -1 points | Supporting (BS2_Supporting) |
| N/A | Moderate (not used) |
| -3.0 points | Strong (BS2) |

---

### BS3 - Functional Studies (No Effect)

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

**VCEP Specifications:**

***Not Applicable***

**Comments:** Approved functional studies are available for each individual gene in the supplemental material. Additional functional studies can be submitted to the expert panel for approval. BS3 is not applicable for PPP1CB at this time (same rationale as PS3).

---

### BS4 - Lack of Segregation

**Original ACMG Summary:** Lack of segregation in affected members of a family.

**VCEP Specifications:** Lack of segregation in affected members of a family.

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Strong** | Requires only one informative meiosis. | General recommendation |

---

### BP1-BP7 - Benign Supporting

| Criterion | Status | Strength | Comment |
|-----------|--------|----------|---------|
| **BP1** | Applicable (Modified) | Supporting | Truncating, LOF variant in a gene for which primarily missense, GOF variants are known to cause disease. Given the disease mechanism is gain-of-function for RASopathies, BP1 should be used for any truncating variant (nonsense, frameshift, affects canonical splice sites, initiation codon, entire gene or multi-exon deletion) in genes without established LOF correlation to disease. See supplemental material regarding dosage sensitivity information. |
| **BP2** | Applicable (Modified) | Supporting / Moderate / Strong | Points are awarded for an alternative molecular cause of a RASopathy in the same gene (and/or in conjunction with BP5) and the phenotype is consistent with expected severity of the RASopathy. See [BP5/BP2 scoring](#appendix-b-bp5bp2-scoring) below. |
| **BP3** | Not Applicable | N/A | No known benign repetitive areas in RASopathy genes. |
| **BP4** | Applicable (Modified) | Supporting | For missense variants: REVEL <=0.3. For splicing variants: predicted outcome is negligible or does not match disease mechanism. |
| **BP5** | Applicable (Modified) | Supporting / Moderate / Strong | Points are awarded for an alternative molecular cause of a RASopathy in a different gene (and/or in conjunction with BP2) and the phenotype is consistent with expected severity of the RASopathy. Points are also awarded for phenotypes inconsistent with a RASopathy and fully explained by a different causative variant (e.g. WES testing). See [BP5/BP2 scoring](#appendix-b-bp5bp2-scoring) below. |
| **BP6** | Not Applicable | N/A | Not for use as recommended by the ClinGen SVI VCEP Review Committee (PMID: 29543229). |
| **BP7** | Applicable (Modified) | Supporting | A synonymous (silent) variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved. Also applicable for intronic positions (except canonical splice sites) or non-coding variants and should be used in conjunction with BP4. |

---

## Rules for Combining Criteria

### Pathogenic Classification

| Criteria Combination |
|---------------------|
| 1 Very Strong *(PS2_VeryStrong)* **AND** >=1 Strong *(PS1, PS2, PS4, PM5_Strong, PM6_Strong, PP1_Strong)* |
| 1 Very Strong *(PS2_VeryStrong)* **AND** >=2 Moderate *(PS2_Moderate, PS4_Moderate, PM4, PM5, PM6, PP1_Moderate)* |
| 1 Very Strong *(PS2_VeryStrong)* **AND** 1 Moderate *(PS2_Moderate, PS4_Moderate, PM4, PM5, PM6, PP1_Moderate)* **AND** 1 Supporting *(PS3_Supporting, PS4_Supporting, PM2_Supporting, PM6_Supporting, PP1, PP2, PP3)* |
| 1 Very Strong *(PS2_VeryStrong)* **AND** >=2 Supporting *(PS3_Supporting, PS4_Supporting, PM2_Supporting, PM6_Supporting, PP1, PP2, PP3)* |
| >=2 Strong *(PS1, PS2, PS4, PM5_Strong, PM6_Strong, PP1_Strong)* |
| 1 Strong *(PS1, PS2, PS4, PM5_Strong, PM6_Strong, PP1_Strong)* **AND** >=3 Moderate *(PS2_Moderate, PS4_Moderate, PM4, PM5, PM6, PP1_Moderate)* |
| 1 Strong *(PS1, PS2, PS4, PM5_Strong, PM6_Strong, PP1_Strong)* **AND** 2 Moderate *(PS2_Moderate, PS4_Moderate, PM4, PM5, PM6, PP1_Moderate)* **AND** >=2 Supporting *(PS3_Supporting, PS4_Supporting, PM2_Supporting, PM6_Supporting, PP1, PP2, PP3)* |
| 1 Strong *(PS1, PS2, PS4, PM5_Strong, PM6_Strong, PP1_Strong)* **AND** 1 Moderate *(PS2_Moderate, PS4_Moderate, PM4, PM5, PM6, PP1_Moderate)* **AND** >=4 Supporting *(PS3_Supporting, PS4_Supporting, PM2_Supporting, PM6_Supporting, PP1, PP2, PP3)* |

### Likely Pathogenic Classification

| Criteria Combination |
|---------------------|
| 1 Very Strong *(PS2_VeryStrong)* **AND** 1 Moderate *(PS2_Moderate, PS4_Moderate, PM4, PM5, PM6, PP1_Moderate)* |
| 1 Strong *(PS1, PS2, PS4, PM5_Strong, PM6_Strong, PP1_Strong)* **AND** 1 Moderate *(PS2_Moderate, PS4_Moderate, PM4, PM5, PM6, PP1_Moderate)* |
| 1 Strong *(PS1, PS2, PS4, PM5_Strong, PM6_Strong, PP1_Strong)* **AND** >=2 Supporting *(PS3_Supporting, PS4_Supporting, PM2_Supporting, PM6_Supporting, PP1, PP2, PP3)* |
| >=3 Moderate *(PS2_Moderate, PS4_Moderate, PM4, PM5, PM6, PP1_Moderate)* |
| 2 Moderate *(PS2_Moderate, PS4_Moderate, PM4, PM5, PM6, PP1_Moderate)* **AND** >=2 Supporting *(PS3_Supporting, PS4_Supporting, PM2_Supporting, PM6_Supporting, PP1, PP2, PP3)* |
| 1 Moderate *(PS2_Moderate, PS4_Moderate, PM4, PM5, PM6, PP1_Moderate)* **AND** >=4 Supporting *(PS3_Supporting, PS4_Supporting, PM2_Supporting, PM6_Supporting, PP1, PP2, PP3)* |

### Benign Classification

| Criteria Combination |
|---------------------|
| >=2 Strong *(BS1, BS2, BS4, BP2_Strong, BP5_Strong)* |
| 1 Stand Alone *(BA1)* |

### Likely Benign Classification

| Criteria Combination |
|---------------------|
| 1 Strong *(BS1, BS2, BS4, BP2_Strong, BP5_Strong)* **AND** 1 Supporting *(BS2_Supporting, BP1, BP2, BP4, BP5, BP7)* |
| >=2 Supporting *(BS2_Supporting, BP1, BP2, BP4, BP5, BP7)* |
| 1 Strong *(BS1, BS2, BS4, BP2_Strong, BP5_Strong)* |
| 1 Strong *(BS1)* |

---

## Appendices

### Appendix A: Criteria Applicability Summary

| Criterion | Status | Max Strength |
|-----------|--------|--------------|
| PVS1 | Not Applicable | - |
| PS1 | Applicable | Strong |
| PS2 | Applicable (Point-based) | Very Strong |
| PS3 | Not Applicable | - |
| PS4 | Applicable (Point-based) | Strong |
| PM1 | Not Applicable | - |
| PM2 | Applicable (Supporting only) | Supporting |
| PM3 | Not Applicable | - |
| PM4 | Applicable | Moderate |
| PM5 | Applicable | Strong |
| PM6 | Applicable (Point-based) | Strong |
| PP1 | Applicable | Strong |
| PP2 | Applicable | Supporting |
| PP3 | Applicable | Supporting |
| PP4 | Not Applicable | - |
| PP5 | Not Applicable | - |
| BA1 | Applicable | Stand Alone |
| BS1 | Applicable | Strong |
| BS2 | Applicable (Point-based) | Strong |
| BS3 | Not Applicable | - |
| BS4 | Applicable | Strong |
| BP1 | Applicable (Modified) | Supporting |
| BP2 | Applicable (Point-based) | Strong |
| BP3 | Not Applicable | - |
| BP4 | Applicable | Supporting |
| BP5 | Applicable (Point-based) | Strong |
| BP6 | Not Applicable | - |
| BP7 | Applicable | Supporting |

### Appendix B: BP5/BP2 Scoring

#### BP5/BP2 Point System (Per Individual)

| Phenotypic Consistency | Points per Individual |
|------------------------|-----------------------|
| Phenotype inconsistent with a RASopathy and causative variant has been identified, -or- Molecular cause of a RASopathy is identified in a different RASopathy gene, -or- Molecular cause of a RASopathy is identified in *trans* or *cis* with the variant being classified | -1 |
| Phenotype inconsistent with a RASopathy and no causative variant identified/reported | 0 |

**Note:** BP2 applies when the alternative molecular cause is in the **same gene**. BP5 applies when the alternative molecular cause is in a **different gene**. BP2 and BP5 may be used in conjunction.

#### BP5/BP2 Evidence Strength Thresholds

| Total Points | Strength Level |
|--------------|----------------|
| -1 points | Supporting (BP5/BP2) |
| N/A | Moderate (not used) |
| -3.0 points | Strong (BP5_Strong/BP2_Strong) |

### Appendix C: Population Frequency Thresholds Summary

| Criterion | Threshold | Strength |
|-----------|-----------|----------|
| BA1 | >=0.05% (gnomAD FAF) | Stand Alone |
| BS1 | >=0.025% (gnomAD FAF) | Strong |
| PM2 | Absent from gnomAD | Supporting |

### Appendix D: Computational Prediction Thresholds Summary

| Criterion | Tool | Pathogenic Threshold | Benign Threshold |
|-----------|------|---------------------|------------------|
| PP3/BP4 (missense) | REVEL | >=0.7 | <=0.3 |
| PP3/BP4 (splicing) | Splicing predictors | Predicted outcome matches disease mechanism | Predicted outcome is negligible or does not match disease mechanism |

### Appendix E: Reference PMIDs

| PMID | Context |
|------|---------|
| 29543229 | ClinGen SVI recommendation against use of PP5/BP6 |
| 31892348 | Laboratory validation standards for functional assays |

### Appendix F: References

1. ClinGen SVI Proposal for De Novo Criteria v1.1: https://clinicalgenome.org/site/assets/files/3461/svi_proposal_for_de_novo_criteria_v1_1.pdf

---

## Version History

| Version | Date | Notes |
|---------|------|-------|
| 1.3.0 | 12/3/2024 | "Observed in >=5 probands" removed from PM5 at Moderate strength. Pilot variants included in the LZTR1 submission. |
| 1.0.0 | Prior | Initial release of PPP1CB VCEP specifications. |

---

*This document was compiled from ClinGen RASopathy VCEP specifications and ClinGen SVI recommendations. For the most current version, please refer to the ClinGen website.*
