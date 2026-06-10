# ClinGen RASopathy Expert Panel Variant Interpretation Guidelines for SOS2

**Version:** 2.3.0
**Released:** 12/3/2024
**Affiliation:** RASopathy VCEP
**Based on:** Richards et al., 2015 ACMG/AMP Guidelines

**Release Notes:** Submitting Pilot Rules. All pilot variants are attached in the LZTR1 submission. "Observed in ≥5 probands" removed from PM5 at Moderate strength.

---

## Gene Information

| Attribute | Value |
|-----------|-------|
| **Gene** | SOS2 (HGNC:11188) |
| **HGNC Name** | SOS Ras/Rho guanine nucleotide exchange factor 2 |
| **Transcript** | NM_006939.4 |
| **Protein** | NP_008870.2 |
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
   - [BP1 - Truncating Variant](#bp1---truncating-variant)
   - [BP2 - Observed in Trans/Cis](#bp2---observed-in-transcis)
   - [BP3 - In-Frame in Repetitive Region](#bp3---in-frame-in-repetitive-region)
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

**VCEP Specification:** ***Not Applicable***

**Comments:** Not applicable. The disease mechanism for SOS2-related RASopathy is gain-of-function, not loss-of-function.

---

### PS1 - Same Amino Acid Change

**Original ACMG Summary:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.

**VCEP Specifications:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Strong** | Same amino acid change as a previously established pathogenic variant regardless of nucleotide change. Applicable for observed analogous residue positions in *SOS1* and *SOS2*. | Analogous Gene |

> **Note:** Beware of changes that impact splicing rather than at the amino acid/protein level. The analogous gene extension allows use of pathogenic variants established in SOS1 at analogous residues in SOS2 (see Appendix A for alignment).

---

### PS2 - De Novo (Confirmed)

**Original ACMG Summary:** De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.

**VCEP Specifications:** Follow SVI recommendations for point-based scoring in conjunction with PM6 (see Reference 1) and phenotypic specifications: full points awarded with RASopathy phenotypes, reduced points applicable to cases with minimal phenotypic information (i.e. prenatal cases, cases with a clinical order of a RASopathy panel without clinical information, and cases with limited clinical information in other global tests (such as WES)).

#### PS2/PM6 Point System (Per Proband)

| Phenotypic Consistency | Confirmed *de novo* (PS2) | Assumed *de novo* (PM6) |
|------------------------|:-------------------------:|:-----------------------:|
| Phenotype is consistent with a RASopathy* | 2 | 1 |
| Limited phenotypic information** | 1 | 0.5 |
| Phenotype not consistent with RASopathy | 0 | 0 |

\*Exclusive of prenatal cases.
\*\*Applicable to prenatal cases, cases with a clinical order of a RASopathy panel without clinical information, and cases with limited clinical information in other global tests (such as WES). Phenotypes for prenatal cases include hypertrophic cardiomyopathy, increased nuchal translucency, cystic hygroma, or hydrops.

#### PS2/PM6 Evidence Strength Thresholds

| Points | Strength Level |
|:------:|----------------|
| 0.5 | Supporting (PS2_Supporting or PM6_Supporting) |
| 1.0 | Moderate (PS2_Moderate or PM6) |
| 2.0 | Strong (PS2 or PM6_Strong) |
| 4.0 | Very Strong (PS2_VeryStrong or PM6_VeryStrong) |

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Very Strong** | ≥4 Points | Strength |
| **Strong** | ≥2 Points | None |
| **Moderate** | ≥1 Point | Strength |

---

### PS3 - Functional Studies

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.

**VCEP Specifications:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product. Approved assays are available in the supplemental materials.

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Moderate** | Two or more different approved assays | Disease-specific, Gene-specific, Strength |
| **Supporting** | One approved assay | Disease-specific, Gene-specific, Strength |

> **Note:** PS3 at Strong level is not available for SOS2. The maximum achievable strength is Moderate (with ≥2 different approved assays).

#### Approved Assay Instances for SOS2

All approved assays are from Cordeddu et al., 2015 (PMID: 26173643; DOI: 10.1002/humu.22834).

**1. RAS Activation Assay**

| Attribute | Details |
|-----------|---------|
| **Description** | Measure the bound RAS protein that immunoprecipitated with RAF1 or RBD (synthetic) |
| **Material** | Flp-In T-REx 293 cells co-transfected with pcDNA5/FRT/TO expression plasmid and Flp recombinase-expressing plasmid pOG44, using FuGENE HD |
| **Readout** | Semi-quantitative (qualitative) — measure bound RAS protein immunoprecipitated with RAF1 or RBD |
| **Biological Replicates** | Met |
| **Technical Replicates** | Not met |
| **Positive Control** | Met; WT |
| **Negative Control** | Met; Vector |
| **Validation Controls (P/LP)** | 3 (T264K, M267R, T376S) |
| **Validation Controls (B/LB)** | None |
| **Statistical Analysis** | One-tailed Student's t test |
| **Normal Threshold** | Normal (WT) pattern |
| **Abnormal Threshold** | Increased RAS/RBD complexes compared with positive control range in assay |
| **Approved** | Yes |
| **Strength** | PS3_Supporting; BS3 N/A |

**2. MEK Activation Assay**

| Attribute | Details |
|-----------|---------|
| **Description** | Measure the ratio of phosphorylated MEK to unphosphorylated MEK, basally and following RTK stimulation |
| **Material** | HEK293T/17 cells transfected with WT or mutant SOS2 plasmids along with HA-tagged ERK expression construct at 4:1 ratio, using FuGENE HD |
| **Readout** | Semi-quantitative (qualitative) — pMEK/MEK ratio basally and/or after RTK stimulation |
| **Biological Replicates** | Met |
| **Technical Replicates** | Not met |
| **Positive Control** | Met; WT |
| **Negative Control** | Met; Vector |
| **Validation Controls (P/LP)** | 3 (T264K - P/LP, M267R - P/LP, T376S - P) |
| **Validation Controls (B/LB)** | None |
| **Statistical Analysis** | ANOVA with Bonferroni post-hoc correction |
| **Normal Threshold** | Normal (WT) pattern |
| **Abnormal Threshold** | Abnormal pattern indicating constitutively active, increased phosphorylation protein, and/or prolonged phosphorylation |
| **Approved** | Yes |
| **Strength** | PS3_Supporting; BS3 N/A |

**3. ERK Activation Assay**

| Attribute | Details |
|-----------|---------|
| **Description** | Measure the ratio of phosphorylated ERK to unphosphorylated ERK, basally and following stimulation |
| **Material** | HEK293T/17 cells transfected with WT or mutant SOS2 plasmids along with HA-tagged ERK expression construct at 4:1 ratio, using FuGENE HD |
| **Readout** | Semi-quantitative (qualitative) — pERK/ERK ratio basally and after stimulation, compared with controls |
| **Biological Replicates** | Met |
| **Technical Replicates** | Not met |
| **Positive Control** | Met; WT |
| **Negative Control** | Met; Vector |
| **Validation Controls (P/LP)** | 3 (T264K - P/LP, M267R - P/LP, T376S - P) |
| **Validation Controls (B/LB)** | None |
| **Statistical Analysis** | ANOVA with Bonferroni post-hoc correction |
| **Normal Threshold** | Normal (WT) pattern |
| **Abnormal Threshold** | Constitutively active, increased phosphorylation protein, and/or prolonged phosphorylation |
| **Approved** | Yes |
| **Strength** | PS3_Supporting; BS3 N/A |

> **Important:** BS3 is not applicable for any of the three approved SOS2 assays. These assays cannot be used to support a benign interpretation.

---

### PS4 - Prevalence in Affected

**Original ACMG Summary:** The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.

**VCEP Specifications:** Strength adjustment using point-based scoring for autosomal dominant cases with phenotypic specifications: full points awarded with RASopathy phenotypes, reduced points applicable to cases with minimal phenotypic information (i.e. prenatal cases, cases with a clinical order of a RASopathy panel without clinical information, and cases with limited clinical information in other global tests (such as WES)).

#### PS4 Point System (Per Proband)

| Phenotypic Consistency | Points per Proband |
|------------------------|:------------------:|
| Individual well-phenotyped with features of a RASopathy | 1 |
| Limited phenotypic information compatible with RASopathy* | 0.5 |
| No clinical information or isolated clinical features | 0 |
| Well-phenotyped but consistent with non-RASopathy disorder** | -1 |

\*Applicable to prenatal cases, cases with a clinical order of a RASopathy panel without clinical information, and cases with limited clinical information in other global tests (such as WES). Phenotypes for prenatal cases include hypertrophic cardiomyopathy, increased nuchal translucency, cystic hygroma, or hydrops.
\*\*Negative points for PS4 represent proband affected with a non-RASopathy congenital disorder rather than a healthy individual (BS2). This typically applies to probands tested by exome analysis with multiple other clinical features supporting a distinct syndromic disorder (e.g. CHARGE, CdLS).

#### PS4 Evidence Strength Thresholds

| Points | Strength Level |
|:------:|----------------|
| ≥1.0 | Supporting (PS4_Supporting) |
| ≥3.0 | Moderate (PS4_Moderate) |
| ≥5.0 | Strong (PS4) |

---

### PM1 - Mutational Hot Spot

**Original ACMG Summary:** Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.

**VCEP Specifications:** Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation. PM1 and PM5 may be used in conjunction at moderate levels, however, PM1 may not be applied if PM5_Strong is applied to avoid overweighting.

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Moderate** | Applicable only to critical and well-established functional domains available in the supplementary table: **PH domain [AA 418–498]**. Not applicable to specific amino acid residues (see PM5). | Gene-specific |

> **Note:** PM1 is only applicable at Moderate strength for variants within the PH domain (amino acids 418–498). PM1 and PM5 may be used together at moderate levels, but PM1 may **not** be applied if PM5_Strong is used, to avoid overweighting evidence.

---

### PM2 - Absent from Controls

**Original ACMG Summary:** Absent from controls (or at extremely low frequency if recessive) in population databases.

**VCEP Specification:**

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Supporting** | The variant must be absent from controls (gnomAD). | Strength |

> **Note:** PM2 is downgraded to Supporting only, per ClinGen SVI recommendations. The variant must be completely absent from gnomAD.

---

### PM3 - In Trans with Pathogenic

**Original ACMG Summary:** For recessive disorders, detected in trans with a pathogenic variant.

**VCEP Specification:** ***Not Applicable***

**Comments:** Not applicable. SOS2-related RASopathy follows autosomal dominant inheritance.

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

**VCEP Specifications:** Applicable for observed analogous residue positions in *SOS1* and *SOS2*. PM1 and PM5 may be used in conjunction at moderate levels, however, PM1 may not be applied if PM5_Strong is applied to avoid overweighting.

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Strong** | ≥2 different [likely] pathogenic residue changes at the same codon observed in ≥5 probands | Analogous Gene, Strength |
| **Moderate** | 1 [likely] pathogenic residue change at the same codon | Analogous Gene, Disease-specific |

> **Notes:**
> - The analogous gene extension allows consideration of pathogenic variants at analogous residues in SOS1 when evaluating SOS2 variants.
> - PM1 and PM5 may be used together at moderate levels, but PM1 may **not** be applied when PM5_Strong is used.
> - Known SOS2 residues with PM5_Strong designation: **AA 264** and **AA 267** (based on case count data).

---

### PM6 - De Novo (Assumed)

**Original ACMG Summary:** Assumed de novo, but without confirmation of paternity and maternity.

**VCEP Specifications:** Follow SVI recommendations for point-based scoring in conjunction with PS2 (see Reference 1) and phenotypic specifications: full points awarded with RASopathy phenotypes, reduced points applicable to cases with minimal phenotypic information (i.e. prenatal cases, cases with a clinical order of a RASopathy panel without clinical information, and cases with limited clinical information in other global tests (such as WES)).

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Strong** | ≥2 Points | Strength |
| **Moderate** | ≥1 Point | None |
| **Supporting** | ≥0.5 Points | Strength |

> **Note:** Uses the same point-based scoring system as PS2. See [PS2/PM6 Point System](#ps2pm6-point-system-per-proband) above.

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

**VCEP Specification:** ***Not Applicable***

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

**VCEP Specification:** ***Not Applicable***

**Comments:** Not applicable, see PS4. Phenotypic specificity is captured through the PS4 point-based scoring system.

---

### PP5 - Reputable Source

**Original ACMG Summary:** Reputable source recently reports variant as pathogenic, but the evidence is not available to the laboratory to perform an independent evaluation.

**VCEP Specification:** ***Not Applicable***

This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PMID: 29543229).

---

## Benign Criteria

### BA1 - Allele Frequency >5%

**Original ACMG Summary:** Allele frequency is above 5% in population databases.

**VCEP Specification:**

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Stand Alone** | gnomAD filtering allele frequency **≥0.05%** | Disease-specific |

---

### BS1 - Frequency Greater Than Expected

**Original ACMG Summary:** Allele frequency is greater than expected for disorder.

**VCEP Specification:**

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Strong** | gnomAD filtering allele frequency **≥0.025%** | Disease-specific |

---

### BS2 - Observed in Healthy Adult

**Original ACMG Summary:** Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

**VCEP Specifications:** Strength adjustment using point-based scoring based on phenotypic specifications. Phenotypic specifications: based on healthy homozygote or heterozygote individuals, reduced points for apparently unaffected heterozygous individuals, applicable to parent or sibling samples during clinical family evaluations.

#### BS2 Point System (Per Individual)

| Phenotypic Consistency | Points per Individual |
|------------------------|:---------------------:|
| Healthy homozygous individual assessed for a RASopathy | -3 |
| Healthy heterozygous individual assessed for a RASopathy | -1 |
| No phenotypic information other than "unaffected" heterozygote* | -0.25 |
| No clinical information or nonspecific clinical features | 0 |

\*Typically applicable to parental or sibling samples during clinical family evaluations.

#### BS2 Evidence Strength Thresholds

| Points | Strength Level |
|:------:|----------------|
| ≤ -1 | Supporting (BS2_Supporting) |
| N/A | Moderate — not available |
| ≤ -3 | Strong (BS2) |

> **Note:** Points are negative (benign direction). The threshold is met when total points reach or exceed the negative value shown (e.g., -4 points meets BS2 Strong at -3).

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Strong** | ≤ -4 Points | Strength |
| **Supporting** | ≤ -1 Point | Strength |

---

### BS3 - Functional Studies (No Effect)

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

**VCEP Specification:** ***Not Applicable***

**Comments:** Approved functional studies are available for each individual gene in the supplemental material. Additional functional studies can be submitted to the expert panel for approval. **BS3 is not applicable for SOS2** — none of the three approved assays (RAS Activation, MEK Activation, ERK Activation) support benign interpretation (all listed as BS3_NA).

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
| **Supporting** | This rule has contraindications for use with RASopathies. Given the disease mechanism is gain-of-function for RASopathies, BP1 should be used for any truncating variant (nonsense, frameshift, affects canonical splice sites, initiation codon, entire gene or multi-exon deletion) in genes without established LOF correlation to disease. See the supplemental material regarding dosage sensitivity information for each individual gene and potential association to disorders associated with LOF variants. | Disease-specific |

> **Note:** BP1 usage is inverted from the original ACMG intent. For RASopathies (GOF mechanism), truncating/LOF variants are less likely to be pathogenic, so BP1 is applied to truncating variants rather than missense variants.

---

### BP2 - Observed in Trans/Cis

**Original ACMG Summary:** Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder or observed in cis with a pathogenic variant in any inheritance pattern.

**VCEP Specifications:** Points are awarded for an alternative molecular cause of a RASopathy in the same gene (and/or in conjunction with BP5) and the phenotype is consistent with expected severity of the RASopathy.

#### BP2/BP5 Point System (Per Individual)

| Phenotypic Consistency | Points per Individual |
|------------------------|:---------------------:|
| Phenotype inconsistent with a RASopathy and causative variant has been identified, **-or-** Molecular cause of a RASopathy is identified in a different RASopathy gene, **-or-** Molecular cause of a RASopathy is identified in *trans* or *cis* with the variant being classified | -1 |
| Phenotype inconsistent with a RASopathy and no causative variant identified/reported | 0 |

#### BP2/BP5 Evidence Strength Thresholds

| Points | Strength Level |
|:------:|----------------|
| ≤ -1 | Supporting (BP5/BP2) |
| N/A | Moderate — not available |
| ≤ -3 | Strong (BP5_Strong/BP2_Strong) |

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Strong** | ≥ (-4) Points | Strength |
| **Moderate** | ≥ (-2) Points | Strength |
| **Supporting** | ≥ (-1) Point | None |

> **Note:** BP2 considers alternative molecular causes within the **same gene**. BP5 considers alternative molecular causes in a **different gene**. Points from both can be combined.

---

### BP3 - In-Frame in Repetitive Region

**Original ACMG Summary:** In-frame deletions/insertions in a repetitive region without a known function.

**VCEP Specification:** ***Not Applicable***

**Comments:** No known benign repetitive areas in RASopathy genes.

---

### BP4 - Computational Evidence (Benign)

**Original ACMG Summary:** Multiple lines of computational evidence suggest no impact on gene or gene product.

**VCEP Specifications:** For missense variants: REVEL ≤0.3. For splicing variants: predicted outcome is negligible or does not match disease mechanism.

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Supporting** | For missense variants: REVEL ≤0.3. | Disease-specific |

---

### BP5 - Alternate Molecular Basis

**Original ACMG Summary:** Variant found in a case with an alternate molecular basis for disease.

**VCEP Specifications:** Points are awarded for an alternative molecular cause of a RASopathy in a different gene (and/or in conjunction with BP2) and the phenotype is consistent with expected severity of the RASopathy. Points are also awarded for phenotypes inconsistent with a RASopathy and fully explained by a different causative variant (e.g. WES testing).

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Strong** | ≥ (-4) Points | Strength |
| **Moderate** | ≥ (-2) Points | Strength |
| **Supporting** | ≥ (-1) Point | None |

> **Note:** Uses the same point system as BP2 (see [BP2/BP5 Point System](#bp2bp5-point-system-per-individual)). BP5 specifically considers alternative molecular causes in a **different RASopathy gene**, while BP2 considers the **same gene**.

---

### BP6 - Reputable Source (Benign)

**Original ACMG Summary:** Reputable source recently reports variant as benign, but the evidence is not available to the laboratory to perform an independent evaluation.

**VCEP Specification:** ***Not Applicable***

This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PMID: 29543229).

---

### BP7 - Synonymous Variant

**Original ACMG Summary:** A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.

**VCEP Specifications:**

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Supporting** | A synonymous (silent) variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved. This rule is also applicable for intronic positions (except canonical splice sites) or non-coding variants and should be used in conjunction with BP4. | General recommendation |

---

## Rules for Combining Criteria

### Pathogenic Classification

| Criteria Combination |
|---------------------|
| 1 Very Strong *(PS2_VeryStrong)* **AND** ≥1 Strong *(PS1, PS2, PS4, PM5_Strong, PM6_Strong, PP1_Strong)* |
| 1 Very Strong *(PS2_VeryStrong)* **AND** ≥2 Moderate *(PS2_Moderate, PS4_Moderate, PM4, PM5, PM6, PP1_Moderate)* |
| 1 Very Strong *(PS2_VeryStrong)* **AND** 1 Moderate *(PS2_Moderate, PS4_Moderate, PM4, PM5, PM6, PP1_Moderate)* **AND** 1 Supporting *(PS3_Supporting, PS4_Supporting, PM2_Supporting, PM6_Supporting, PP1, PP3)* |
| 1 Very Strong *(PS2_VeryStrong)* **AND** ≥2 Supporting *(PS3_Supporting, PS4_Supporting, PM2_Supporting, PM6_Supporting, PP1, PP3)* |
| ≥2 Strong *(PS1, PS2, PS4, PM5_Strong, PM6_Strong, PP1_Strong)* |
| 1 Strong *(PS1, PS2, PS4, PM5_Strong, PM6_Strong, PP1_Strong)* **AND** ≥3 Moderate *(PS2_Moderate, PS4_Moderate, PM4, PM5, PM6, PP1_Moderate)* |
| 1 Strong *(PS1, PS2, PS4, PM5_Strong, PM6_Strong, PP1_Strong)* **AND** 2 Moderate *(PS2_Moderate, PS4_Moderate, PM4, PM5, PM6, PP1_Moderate)* **AND** ≥2 Supporting *(PS3_Supporting, PS4_Supporting, PM2_Supporting, PM6_Supporting, PP1, PP3)* |
| 1 Strong *(PS1, PS2, PS4, PM5_Strong, PM6_Strong, PP1_Strong)* **AND** 1 Moderate *(PS2_Moderate, PS4_Moderate, PM4, PM5, PM6, PP1_Moderate)* **AND** ≥4 Supporting *(PS3_Supporting, PS4_Supporting, PM2_Supporting, PM6_Supporting, PP1, PP3)* |

### Likely Pathogenic Classification

| Criteria Combination |
|---------------------|
| 1 Very Strong *(PS2_VeryStrong)* **AND** 1 Moderate *(PS2_Moderate, PS4_Moderate, PM4, PM5, PM6, PP1_Moderate)* |
| 1 Strong *(PS1, PS2, PS4, PM5_Strong, PM6_Strong, PP1_Strong)* **AND** 1 Moderate *(PS2_Moderate, PS4_Moderate, PM4, PM5, PM6, PP1_Moderate)* |
| 1 Strong *(PS1, PS2, PS4, PM5_Strong, PM6_Strong, PP1_Strong)* **AND** ≥2 Supporting *(PS3_Supporting, PS4_Supporting, PM2_Supporting, PM6_Supporting, PP1, PP3)* |
| ≥3 Moderate *(PS2_Moderate, PS4_Moderate, PM4, PM5, PM6, PP1_Moderate)* |
| 2 Moderate *(PS2_Moderate, PS4_Moderate, PM4, PM5, PM6, PP1_Moderate)* **AND** ≥2 Supporting *(PS3_Supporting, PS4_Supporting, PM2_Supporting, PM6_Supporting, PP1, PP3)* |
| 1 Moderate *(PS2_Moderate, PS4_Moderate, PM4, PM5, PM6, PP1_Moderate)* **AND** ≥4 Supporting *(PS3_Supporting, PS4_Supporting, PM2_Supporting, PM6_Supporting, PP1, PP3)* |

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

### Appendix A: SOS1/SOS2 Protein Alignment

SOS2 specifications use analogous residue positions between SOS1 (NP_005624.2, 1,333 aa) and SOS2 (NP_008870.2, 1,332 aa) for PS1 and PM5 criteria. The two proteins are highly homologous.

**Reference sequences:**
- SOS1: NP_005624.2 (1,333 amino acids)
- SOS2: NP_008870.2 (1,332 amino acids)

**Domain Boundaries (SOS1 numbering):**

| Domain | Amino Acid Range |
|--------|-----------------|
| Histone folds | 1–198 |
| Dbl homology (DH) | 198–418 |
| Pleckstrin homology (PH) | 418–546 |
| Helical linker | 546–567 |
| RAS exchanger motif (REM) | 567–750 |
| Cdc25 | 750–1050 |
| SH3-binding motifs | 1050–1333 |

> **Note:** Due to a 2-residue gap in SOS2 at approximately position 177–178 in the DH domain, SOS2 numbering falls ~2 residues behind SOS1 for positions after residue 239. The C-terminal SH3-binding domain shows more divergence with multiple insertions/deletions.

### Appendix B: Known SOS2 Variant Hotspot Residues

Based on HGMD and clinical case count data, the following analogous residue positions have documented SOS2 missense variants:

| Amino Acid | SOS2 Variants (HGMD) | Clinical Case Counts (GeneDx SOS2) | PM5 Strength | Notes |
|:----------:|:---------------------:|:-----------------------------------:|:------------:|-------|
| 264 | — | 3 | PM5_Strong | Validation P/LP variant: T264K |
| 266 | 1 | — | — | Also 1 SOS1 variant at this position |
| 267 | — | 6 | PM5_Strong | Validation P/LP variant: M267R |
| 269 | 2 | — | — | Also 2 SOS1 variants |
| 376 | — | 3 | — | Validation P variant: T376S |
| 378 | 2 | — | — | Also 1 SOS1 variant |
| 500 | — | 4 | — | |
| 946 | 1 | — | — | SOS2-only (no SOS1 variant) |

### Appendix C: Population Frequency Thresholds Summary

| Criterion | Threshold | Strength |
|-----------|-----------|----------|
| BA1 | ≥0.05% (gnomAD filtering allele frequency) | Stand Alone |
| BS1 | ≥0.025% (gnomAD filtering allele frequency) | Strong |
| PM2 | Absent from gnomAD | Supporting |

### Appendix D: Computational Predictor Thresholds

| Direction | Tool | Threshold | Criterion |
|-----------|------|-----------|-----------|
| Pathogenic | REVEL | ≥0.7 | PP3 (Supporting) |
| Benign | REVEL | ≤0.3 | BP4 (Supporting) |

### Appendix E: Criteria Applicability Summary

| Criterion | Status | Max Strength | Notes |
|-----------|--------|:------------:|-------|
| PVS1 | Not Applicable | — | GOF mechanism, not LOF |
| PS1 | Applicable | Strong | Includes analogous SOS1 residues |
| PS2 | Applicable | Very Strong | Point-based with PM6 |
| PS3 | Applicable | Moderate | Max 2+ approved assays |
| PS4 | Applicable | Strong | Point-based |
| PM1 | Applicable | Moderate | PH domain [AA 418–498] only |
| PM2 | Applicable | Supporting | Absent from gnomAD |
| PM3 | Not Applicable | — | Autosomal dominant |
| PM4 | Applicable | Moderate | No repetitive regions |
| PM5 | Applicable | Strong | Includes analogous SOS1 residues |
| PM6 | Applicable | Strong | Point-based with PS2 |
| PP1 | Applicable | Strong | ≥7 informative meioses |
| PP2 | Not Applicable | — | Missense z score <3.09 |
| PP3 | Applicable | Supporting | REVEL ≥0.7 |
| PP4 | Not Applicable | — | See PS4 |
| PP5 | Not Applicable | — | Per SVI recommendation |
| BA1 | Applicable | Stand Alone | ≥0.05% gnomAD FAF |
| BS1 | Applicable | Strong | ≥0.025% gnomAD FAF |
| BS2 | Applicable | Strong | Point-based |
| BS3 | Not Applicable | — | No approved benign assays |
| BS4 | Applicable | Strong | 1 informative meiosis |
| BP1 | Applicable | Supporting | Truncating/LOF variants |
| BP2 | Applicable | Strong | Point-based, same gene |
| BP3 | Not Applicable | — | No repetitive regions |
| BP4 | Applicable | Supporting | REVEL ≤0.3 |
| BP5 | Applicable | Strong | Point-based, different gene |
| BP6 | Not Applicable | — | Per SVI recommendation |
| BP7 | Applicable | Supporting | Synonymous + splice prediction |

### Appendix F: References

1. ClinGen SVI Proposal for De Novo Criteria v1.1: https://clinicalgenome.org/site/assets/files/3461/svi_proposal_for_de_novo_criteria_v1_1.pdf
2. Cordeddu V, et al. (2015) Functional characterization of SOS2 variants. *Hum Mutat*. PMID: 26173643; DOI: 10.1002/humu.22834
3. Brnich SE, et al. (2018) Recommendations for application of the functional evidence PS3/BS3 criterion. PMID: 29543229

---

## Version History

| Version | Date | Notes |
|---------|------|-------|
| 2.3.0 | 12/3/2024 | Submitting Pilot Rules. All pilot variants are attached in the LZTR1 submission. "Observed in ≥5 probands" removed from PM5 at Moderate strength. |

---

*This document was compiled from ClinGen RASopathy VCEP specifications and ClinGen SVI recommendations. For the most current version, please refer to the ClinGen website.*
