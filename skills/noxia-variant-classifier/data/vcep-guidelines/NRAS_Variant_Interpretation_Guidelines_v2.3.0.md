# ClinGen RASopathy VCEP Variant Interpretation Guidelines for NRAS

**Version:** 2.3.0
**Released:** 12/3/2024
**Affiliation:** RASopathy VCEP
**Based on:** Richards et al., 2015 ACMG/AMP Guidelines

**Release Notes:** Submitting Pilot Rules. All pilot variants are attached in the LZTR1 submission. "Observed in ≥5 probands" removed from PM5 at Moderate strength.

---

## Gene Information

| Attribute | Value |
|-----------|-------|
| **Gene** | NRAS (HGNC:7989) |
| **HGNC Name** | NRAS proto-oncogene, GTPase |
| **Transcript** | NM_002524.5 |
| **Disease** | RASopathy (MONDO:0021060) |
| **Inheritance** | Autosomal dominant |
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
   - [BP1 - Truncating Variant](#bp1---truncating-variant)
   - [BP2 - Observed in Trans/Cis](#bp2---observed-in-transcis)
   - [BP3 - In-frame in Repetitive Region](#bp3---in-frame-in-repetitive-region)
   - [BP4 - Computational Evidence (Benign)](#bp4---computational-evidence-benign)
   - [BP5 - Alternate Molecular Basis](#bp5---alternate-molecular-basis)
   - [BP6 - Reputable Source (Benign)](#bp6---reputable-source-benign)
   - [BP7 - Synonymous Variant](#bp7---synonymous-variant)
3. [Rules for Combining Criteria](#rules-for-combining-criteria)
4. [Appendices](#appendices)

---

## Pathogenic Criteria

### PVS1 - Null Variant

**Original ACMG Summary:** Null variant (nonsense, frameshift, canonical ±1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.

**VCEP Specification:** *Not Applicable*

**Comments:** Not applicable. The disease mechanism for NRAS-associated RASopathies is gain-of-function, not loss-of-function.

---

### PS1 - Same Amino Acid Change

**Original ACMG Summary:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change. Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Strong** | Same amino acid change as a previously established pathogenic variant regardless of nucleotide change. Applicable for observed analogous pathogenic residue positions in *HRAS*, *KRAS*, *MRAS*, *NRAS*, *RIT1*, and *RRAS2*. | Analogous Gene |

---

### PS2 - De Novo (Confirmed)

**Original ACMG Summary:** De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.

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
|--------|----------------|
| 0.5 | Supporting (PS2_Supporting or PM6_Supporting) |
| 1.0 | Moderate (PS2_Moderate or PM6) |
| 2.0 | Strong (PS2 or PM6_Strong) |
| 4.0 | Very Strong (PS2_VeryStrong or PM6_VeryStrong) |

---

### PS3 - Functional Studies

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.

**VCEP Specifications:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product. Approved assays are available in the supplemental materials.

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Moderate** | Two or more different approved assays | Disease-specific, Gene-specific, Strength |
| **Supporting** | One approved assay | Disease-specific, Gene-specific, Strength |

> **Note:** Prior to evaluation of an assay for a variant, all assays are expected to be validated by the performing laboratory in accordance with standard procedures with all appropriate control inclusions (PMID: 31892348). As most of these assays are semi-quantitative in nature, abnormal results should be compared relative to the known status of the controls included in the assay. Assays not listed below are presumed to lack sufficient historical evidence and may only be sufficient for PS3_Supporting. Animal models and variant-specific assays (i.e. myristoylation assays) have been excluded.

#### Approved Assay Instances for NRAS

| Assay | General Description | Assay Specificity | Approved Strength | Key NRAS PMIDs |
|-------|--------------------|--------------------|-------------------|----------------|
| **RAS Activation Assay** | Measures bound RAS protein immunoprecipitated with RAF1 or RBD (synthetic) | Pathway Specific (upstream from RAS and RAS proteins) | PS3_Supporting; BS3_NA | 19966803, 28594414, 21263000 |
| **MEK Activation Assay** | Measures ratio of phosphorylated MEK to unphosphorylated MEK, basally and following RTK stimulation | Pathway Specific | PS3_Supporting; BS3_NA | 19966803, 28594414 |
| **ERK Activation Assay** | Measures ratio of phosphorylated ERK to unphosphorylated ERK, basally and following stimulation | Pathway Specific | PS3_Supporting; BS3_NA | 19966803, 28594414 |

> **Note:** Multiple assays are pathway-specific, meaning they evaluate the effect of a variant on the Ras/MAPK pathway; controls from any gene may be used. Gene-specific assays (SHP-2 Phosphatase Activity, BRAF Kinase Activity, RAF1 Kinase Activity, LZTR1 Stability/Localization) are not applicable to NRAS. The AKT Phosphorylation Assay is **not currently approved** as a standalone assay for RASopathy-associated variants.

#### Abnormal Readout Thresholds

- **RAS Activation Assay:** Increased RAS/RBD complexes compared with positive control range in assay
- **MEK Activation Assay:** Abnormal pattern indicating constitutively active, increased phosphorylation protein, and/or prolonged phosphorylation
- **ERK Activation Assay:** Constitutively active, increased phosphorylation protein, and/or prolonged phosphorylation

---

### PS4 - Prevalence in Affected

**Original ACMG Summary:** The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.

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
|--------|----------------|
| ≥1.0 | Supporting (PS4_Supporting) |
| ≥3.0 | Moderate (PS4_Moderate) |
| ≥5.0 | Strong (PS4) |

---

### PM1 - Mutational Hot Spot

**Original ACMG Summary:** Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.

**VCEP Specifications:** Located in a mutational hot spot and/or critical and well-established functional domain without benign variation. PM1 and PM5 may be used in conjunction at moderate levels, however, PM1 may **not** be applied if PM5_Strong is applied to avoid overweighting.

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Moderate** | Applicable only to critical and well-established functional domains (see table below). Not applicable to specific amino acid residues (see PM5). | Gene-specific |

#### NRAS Functional Domains for PM1

| Domain | NRAS Amino Acid Positions |
|--------|--------------------------|
| P-loop | AA 10–17 |
| Switch I (SW1) | AA 25–40 |
| Switch II (SW2) | AA 57–64 |
| SAK | AA 145–156 |

---

### PM2 - Absent from Controls

**Original ACMG Summary:** Absent from controls (or at extremely low frequency if recessive) in population databases.

**VCEP Specification (Supporting only):**

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Supporting** | The variant must be absent from controls (gnomAD) | Strength |

---

### PM3 - In Trans with Pathogenic

**Original ACMG Summary:** For recessive disorders, detected in trans with a pathogenic variant.

**VCEP Specification:** *Not Applicable*

**Comments:** Not applicable. NRAS-associated RASopathy follows autosomal dominant inheritance.

---

### PM4 - Protein Length Changes

**Original ACMG Summary:** Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

**VCEP Specifications:** Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Moderate** | No known repetitive areas in gene. Use as described. | General recommendation |

---

### PM5 - Novel Missense at Same Residue

**Original ACMG Summary:** Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before. Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:** Applicable for observed analogous residue positions in *HRAS*, *KRAS*, *MRAS*, *NRAS*, *RIT1*, and *RRAS2*. PM1 and PM5 may be used in conjunction at moderate levels, however, PM1 may **not** be applied if PM5_Strong is applied to avoid overweighting.

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Strong** | ≥2 different [likely] pathogenic residue changes at the same codon | Analogous Gene, Strength |
| **Moderate** | 1 [likely] pathogenic residue change at the same codon | Analogous Gene, Disease-specific |

---

### PM6 - De Novo (Assumed)

**Original ACMG Summary:** Assumed de novo, but without confirmation of paternity and maternity.

**VCEP Specifications:** Follow SVI recommendations for point-based scoring in conjunction with PS2 (see Reference 1) and phenotypic specifications: full points awarded with RASopathy phenotypes, reduced points applicable to cases with minimal phenotypic information (i.e. prenatal cases, cases with a clinical order of a RASopathy panel without clinical information, and cases with limited clinical information in other global tests (such as WES)).

| Strength | Points | Modification Type |
|----------|--------|-------------------|
| **Strong** | 2 Points | Strength |
| **Moderate** | 1 Point | None |
| **Supporting** | 0.5 Points | Strength |

> **Note:** See [PS2/PM6 Points Per Proband table](#ps2pm6-points-per-proband) above for phenotypic scoring details.

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

**Comments:** Not applicable because missense z score is <3.09 in gnomAD.

---

### PP3 - Computational Evidence

**Original ACMG Summary:** Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).

**VCEP Specifications:** For missense variants: REVEL ≥ 0.7. For splicing impact, predicted outcome must match disease mechanism.

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Supporting** | For missense variants: REVEL ≥ 0.7. For splicing impact, predicted outcome must match disease mechanism. | Disease-specific |

---

### PP4 - Phenotype Specificity

**Original ACMG Summary:** Patient's phenotype or family history is highly specific for a disease with a single genetic etiology.

**VCEP Specification:** *Not Applicable*

**Comments:** Not applicable, see PS4.

---

### PP5 - Reputable Source

**Original ACMG Summary:** Reputable source recently reports variant as pathogenic, but the evidence is not available to the laboratory to perform an independent evaluation.

**VCEP Specification:** *Not Applicable*

This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PMID: 29543229).

---

## Benign Criteria

### BA1 - Allele Frequency >5%

**Original ACMG Summary:** Allele frequency is above 5% in population databases.

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
|--------|----------------|
| ≤ -1 | Supporting (BS2_Supporting) |
| N/A | Moderate (not applicable) |
| ≤ -3.0 | Strong (BS2) |

---

### BS3 - Functional Studies (No Effect)

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

**VCEP Specification:** *Not Applicable*

**Comments:** Approved functional studies are available for each individual gene in the supplemental material. Additional functional studies can be submitted to the expert panel for approval. BS3 is not applicable for any of the currently approved assays for NRAS (all are BS3_NA).

---

### BS4 - Lack of Segregation

**Original ACMG Summary:** Lack of segregation in affected members of a family.

**VCEP Specifications:** Lack of segregation in affected members of a family.

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Strong** | Requires only one informative meiosis | General recommendation |

---

### BP1 - Truncating Variant

**Original ACMG Summary:** Missense variant in a gene for which primarily truncating variants are known to cause disease.

**VCEP Specifications:** Truncating, LOF variant in a gene for which primarily missense, GOF variants are known to cause disease.

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Supporting** | This rule has contraindications for use with RASopathies. Given the disease mechanism is gain-of-function, BP1 should be used for any truncating variant (nonsense, frameshift, affects canonical splice sites, initiation codon, entire gene or multi exon deletion) in genes without established LOF correlation to disease. See supplemental material regarding dosage sensitivity information for each individual gene and potential association to disorders associated with LOF variants. | Disease-specific |

---

### BP2 - Observed in Trans/Cis

**Original ACMG Summary:** Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder or observed in cis with a pathogenic variant in any inheritance pattern.

**VCEP Specifications:** Points are awarded for an alternative molecular cause of a RASopathy in the same gene (and/or in conjunction with BP5) and the phenotype is consistent with expected severity of the RASopathy.

| Strength | Points | Modification Type |
|----------|--------|-------------------|
| **Strong** | ≥ (-4) Points | Strength |
| **Moderate** | ≥ (-2) Points | Strength |
| **Supporting** | ≥ (-1) Point | None |

> See [BP5/BP2 Scoring](#bp5bp2-scoring-table) for point calculation details.

---

### BP3 - In-frame in Repetitive Region

**Original ACMG Summary:** In-frame deletions/insertions in a repetitive region without a known function.

**VCEP Specification:** *Not Applicable*

**Comments:** No known benign repetitive areas in RASopathy genes.

---

### BP4 - Computational Evidence (Benign)

**Original ACMG Summary:** Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc.).

**VCEP Specifications:** For missense variants: REVEL ≤0.3. For splicing variants: predicted outcome is negligible or does not match disease mechanism.

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Supporting** | For missense variants: REVEL ≤0.3 | Disease-specific |

---

### BP5 - Alternate Molecular Basis

**Original ACMG Summary:** Variant found in a case with an alternate molecular basis for disease.

**VCEP Specifications:** Points are awarded for an alternative molecular cause of a RASopathy in a different gene (and/or in conjunction with BP2) and the phenotype is consistent with expected severity of the RASopathy. Points are also awarded for phenotypes inconsistent with a RASopathy and fully explained by a different causative variant (e.g. WES testing).

| Strength | Points | Modification Type |
|----------|--------|-------------------|
| **Strong** | ≥ (-4) Points | Strength |
| **Moderate** | ≥ (-2) Points | Strength |
| **Supporting** | ≥ (-1) Point | None |

#### BP5/BP2 Scoring Table

| Phenotypic Consistency | Points per Individual |
|------------------------|-----------------------|
| Phenotype inconsistent with a RASopathy and causative variant has been identified, **-or-** Molecular cause of a RASopathy is identified in a different RASopathy gene, **-or-** Molecular cause of a RASopathy is identified in *trans* or *cis* with the variant being classified | -1 |
| Phenotype inconsistent with a RASopathy and no causative variant identified/reported | 0 |

#### BP5/BP2 Evidence Strength Thresholds

| Supporting (BP5/BP2) | Moderate (N/A) | Strong (BP5_Strong / BP2_Strong) |
|:--------------------:|:--------------:|:-------------------------------:|
| -1 points | N/A | -3.0 points |

---

### BP6 - Reputable Source (Benign)

**Original ACMG Summary:** Reputable source recently reports variant as benign, but the evidence is not available to the laboratory to perform an independent evaluation.

**VCEP Specification:** *Not Applicable*

This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PMID: 29543229).

---

### BP7 - Synonymous Variant

**Original ACMG Summary:** A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.

**VCEP Specifications:** A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Supporting** | A synonymous (silent) variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved. This rule is also applicable for intronic positions (except canonical splice sites) or non-coding variants and should be used in conjunction with BP4. | General recommendation |

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

### Appendix A: Criteria Summary Table

| Criterion | VCEP Status | Max Strength | Key Modification |
|-----------|-------------|--------------|------------------|
| PVS1 | Not Applicable | — | GOF mechanism, LOF not applicable |
| PS1 | Specified | Strong | Includes analogous genes (HRAS, KRAS, MRAS, NRAS, RIT1, RRAS2) |
| PS2 | Specified | Very Strong (4 pts) | Point-based scoring with phenotypic specifications |
| PS3 | Specified | Moderate (2+ assays) | Approved pathway-specific assays; Supporting for 1 assay |
| PS4 | Specified | Strong (≥5 pts) | Point-based scoring with phenotypic specifications |
| PM1 | Specified | Moderate | P-loop, SW1, SW2, SAK domains only |
| PM2 | Specified | Supporting | Absent from gnomAD |
| PM3 | Not Applicable | — | AD inheritance |
| PM4 | Specified | Moderate | No repetitive areas; use as described |
| PM5 | Specified | Strong | Analogous gene positions; ≥2 different P/LP changes for Strong |
| PM6 | Specified | Strong (2 pts) | Point-based scoring with PS2 |
| PP1 | Specified | Strong (≥7 meioses) | Segregation in >1 family recommended |
| PP2 | Not Applicable | — | Missense z score <3.09 |
| PP3 | Specified | Supporting | REVEL ≥0.7 for missense |
| PP4 | Not Applicable | — | See PS4 |
| PP5 | Not Applicable | — | Not recommended (PMID: 29543229) |
| BA1 | Specified | Stand Alone | gnomAD FAF ≥0.05% |
| BS1 | Specified | Strong | gnomAD FAF ≥0.025% |
| BS2 | Specified | Strong (≤-3 pts) | Point-based scoring with phenotypic specifications |
| BS3 | Not Applicable | — | No approved BS3 assays for NRAS |
| BS4 | Specified | Strong | 1 informative meiosis sufficient |
| BP1 | Specified | Supporting | Inverted: truncating variants in GOF gene |
| BP2 | Specified | Strong (≥-4 pts) | Point-based with BP5 for alternative molecular cause |
| BP3 | Not Applicable | — | No benign repetitive areas |
| BP4 | Specified | Supporting | REVEL ≤0.3 for missense |
| BP5 | Specified | Strong (≥-4 pts) | Point-based with BP2 for alternative molecular cause |
| BP6 | Not Applicable | — | Not recommended (PMID: 29543229) |
| BP7 | Specified | Supporting | Also applicable to intronic/non-coding; use with BP4 |

### Appendix B: Analogous Residue Alignment

The following genes are used for analogous residue comparisons in PS1 and PM5: **HRAS**, **KRAS**, **MRAS**, **NRAS**, **RIT1**, and **RRAS2**.

**Key functional domains (NRAS numbering):**

| Domain | NRAS Positions | HRAS Equivalent |
|--------|---------------|-----------------|
| P-loop | AA 10–17 | HRAS 10–17 |
| Switch I | AA 25–40 | HRAS 25–40 |
| Switch II | AA 57–64 | HRAS 57–64 |
| SAK | AA 145–156 | HRAS 145–156 |

**Protein accessions for alignment:**
| Gene | Protein Accession |
|------|-------------------|
| HRAS | NP_005334.1 |
| KRAS | NP_004976.2 |
| MRAS | NP_036351.3 |
| NRAS | NP_002515.1 |
| RIT1 | NP_008843.1 |
| RRAS2 | NP_036382.2 |

### Appendix C: Population Frequency Thresholds Summary

| Criterion | Threshold | Strength |
|-----------|-----------|----------|
| BA1 | ≥0.05% (gnomAD FAF) | Stand Alone |
| BS1 | ≥0.025% (gnomAD FAF) | Strong |
| PM2 | Absent from gnomAD | Supporting |

### Appendix D: Computational Predictor Thresholds

| Predictor | Pathogenic Threshold (PP3) | Benign Threshold (BP4) |
|-----------|---------------------------|----------------------|
| REVEL | ≥0.7 | ≤0.3 |

### Appendix E: References

1. SVI Proposal for De Novo Criteria v1.1: https://clinicalgenome.org/site/assets/files/3461/svi_proposal_for_de_novo_criteria_v1_1.pdf
2. ClinGen SVI Recommendation on PP5/BP6: PMID 29543229
3. ClinGen SVI PS3/BS3 Functional Evidence Recommendations: PMID 31892348

---

## Version History

| Version | Date | Notes |
|---------|------|-------|
| 2.3.0 | 12/3/2024 | Submitting Pilot Rules. "Observed in ≥5 probands" removed from PM5 at Moderate strength. |

---

*This document was compiled from ClinGen RASopathy VCEP specifications and ClinGen SVI recommendations. For the most current version, please refer to the ClinGen website.*
