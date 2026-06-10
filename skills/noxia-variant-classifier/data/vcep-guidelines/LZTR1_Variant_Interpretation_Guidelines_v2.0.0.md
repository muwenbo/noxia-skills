# ClinGen RASopathy VCEP Variant Interpretation Guidelines for LZTR1

**Version:** 2.0.0
**Released:** 12/3/2024
**Affiliation:** RASopathy VCEP
**Based on:** Richards et al., 2015 ACMG/AMP Guidelines

---

## Gene Information

| Attribute | Value |
|-----------|-------|
| **Gene** | LZTR1 (HGNC:6742) |
| **HGNC Name** | Leucine zipper like transcription regulator 1 |
| **Transcript** | NM_006767.4 |
| **Disease** | RASopathy (MONDO:0021060) |
| **Inheritance** | Autosomal recessive inheritance, Autosomal dominant inheritance |

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

## Important Notes

### Case Level Inheritance Determination

Before applying criteria, reference the **Case Level Inheritance Flowchart** to determine the inheritance pattern of variants in LZTR1. The flowchart indicates which ACMG/AMP criteria can be applied to autosomal dominant (AD) vs. autosomal recessive (AR) variants.

**Key considerations:**
- **Dominant-negative variants**: Use point-based scoring for autosomal dominant cases
- **Loss-of-function variants**: Usage is case specific based on inheritance pattern
- Only PS4 OR PM3 can be applied to a single case (not both)
- Cases with autosomal recessive NS should use PM3
- Cases with autosomal dominant isolated schwannomatosis should use PS4

---

## Pathogenic Criteria

### PVS1 - Null Variant

**Original ACMG Summary:** Null variant (nonsense, frameshift, canonical +/-1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.

**Caveats:**
- Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7)
- Use caution interpreting LOF variants at the extreme 3' end of a gene
- Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact
- Use caution in the presence of multiple transcripts

**VCEP Specifications:** Follow SVI recommendations for application. **This rule can be applied when curating for AR disease only.** Please reference the attached, LZTR1-specific PVS1 Decision Tree before applying PVS1.

#### Strength Levels

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Very Strong (PVS1)** | Null variant in a gene where loss of function is a known mechanism of disease | Disease-specific, Gene-specific |
| **Strong (PVS1_Strong)** | Null variant in a gene where loss of function is a known mechanism of disease | Disease-specific, Gene-specific, Strength |
| **Moderate (PVS1_Moderate)** | Null variant in a gene where loss of function is a known mechanism of disease | Disease-specific, Gene-specific, Strength |
| **Supporting (PVS1_Supporting)** | Null variant in a gene where loss of function is a known mechanism of disease | Disease-specific, Gene-specific, Strength |

#### PVS1 Decision Tree

**For Nonsense or Frameshift variants:**

| Scenario | Exon Status | NMD Prediction | Strength |
|----------|-------------|----------------|----------|
| Predicted to undergo NMD (c.2357 or p.786 are terminal) | Present in biologically-relevant transcript(s) (NM_006767.4) | Yes | PVS1 |
| Predicted to undergo NMD | Absent from biologically-relevant transcript(s) | Yes | N/A |
| Not predicted to undergo NMD | LoF variants in exon frequent OR exon absent from relevant transcript | - | N/A |
| Not predicted to undergo NMD | LoF not frequent, exon present, variant removes >10% of protein | - | PVS1_Strong |
| Not predicted to undergo NMD | LoF not frequent, exon present, variant removes <10% of protein | - | PVS1_Moderate |

**For GT-AG +/-1,2 splice site variants:**

| Scenario | NMD/Reading Frame | Strength |
|----------|-------------------|----------|
| Exon skipping or cryptic splice disrupts reading frame, predicted to undergo NMD | Exon present in relevant transcript | PVS1 |
| Exon skipping or cryptic splice disrupts reading frame, NOT predicted to undergo NMD | LoF frequent OR exon absent | N/A |
| Exon skipping or cryptic splice disrupts reading frame, NOT predicted to undergo NMD, LoF not frequent, exon present | Removes >10% of protein | PVS1_Strong |
| Exon skipping or cryptic splice disrupts reading frame, NOT predicted to undergo NMD, LoF not frequent, exon present | Removes <10% of protein | PVS1_Moderate |
| Exon skipping preserves reading frame (Exons 10, 11, 12, 13, 20, 21 are in frame) | LoF frequent OR exon absent | N/A |
| Exon skipping preserves reading frame, LoF not frequent, exon present | Removes >10% of protein | PVS1_Strong |
| Exon skipping preserves reading frame, LoF not frequent, exon present | Removes <10% of protein | PVS1_Moderate |

**For Deletion variants:**

| Type | NMD/Function | Strength |
|------|--------------|----------|
| Full gene deletion | - | PVS1^d |
| Single to multi exon deletion - Disrupts reading frame, predicted to undergo NMD | Exon present in relevant transcript | PVS1 |
| Single to multi exon deletion - Disrupts reading frame, predicted to undergo NMD | Exon absent | N/A |
| Single to multi exon deletion - Disrupts reading frame, NOT predicted to undergo NMD | Truncated region critical to protein function | PVS1_Strong |
| Single to multi exon deletion - Disrupts reading frame, NOT predicted to undergo NMD | LoF frequent OR exon absent | N/A |
| Single to multi exon deletion - Disrupts reading frame, NOT predicted to undergo NMD, LoF not frequent, exon present | Removes >10% of protein | PVS1_Strong |
| Single to multi exon deletion - Disrupts reading frame, NOT predicted to undergo NMD, LoF not frequent, exon present | Removes <10% of protein | PVS1_Moderate |
| Single to multi exon deletion - Preserves reading frame | Role of region unknown | See above criteria |

**For Duplication variants (>=1 exon, completely contained within gene):**

| Tandem Status | Reading Frame Impact | Strength |
|---------------|---------------------|----------|
| Proven in tandem | Reading frame disrupted, NMD predicted | PVS1 |
| Proven in tandem | No or unknown impact on reading frame/NMD | N/A |
| Presumed in tandem | Reading frame presumed disrupted, NMD predicted | PVS1_Strong |
| Proven not in tandem | - | N/A |

**For Initiation Codon variants:**

| Alternative Start | Upstream P/LP Variants | Strength |
|-------------------|------------------------|----------|
| No known alternative start codon in other transcripts | >=1 pathogenic variant(s) upstream of closest potential in-frame start codon | PVS1_Moderate |
| No known alternative start codon in other transcripts | No pathogenic variant(s) upstream | PVS1_Supp |
| Different functional transcript uses alternative start | - | N/A |

---

### PS1 - Same Amino Acid Change

**Original ACMG Summary:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.

**Example:** Val->Leu caused by either G>C or G>T in the same codon.

**Caveat:** Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Strong (PS1)** | Same amino acid change as a previously established pathogenic variant in LZTR1 regardless of nucleotide change | No change |

---

### PS2 - De Novo (Confirmed)

**Original ACMG Summary:** De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.

**Note:** Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.

**VCEP Specifications:** Follow SVI recommendations for point-based scoring in conjunction with PM6 (see Reference 1) and phenotypic specifications.

#### PS2/PM6 Point System

| Phenotypic Consistency | Confirmed *de novo* (PS2) | Assumed *de novo* (PM6) |
|------------------------|---------------------------|-------------------------|
| Phenotype is consistent with a RASopathy* | 2 points | 1 point |
| Limited phenotypic information** | 1 point | 0.5 points |
| Phenotype not consistent with RASopathy | 0 points | 0 points |

*\*Exclusive of prenatal cases*

*\*\*Applicable to prenatal cases, cases with a clinical order of a RASopathy panel without clinical information, and cases with limited clinical information in other global tests (such as WES). Phenotypes for prenatal cases include hypertrophic cardiomyopathy, increased nuchal translucency, cystic hygroma, or hydrops.*

#### Evidence Strength Thresholds

| Points | Strength Level |
|--------|----------------|
| 0.5 | Supporting (PS2_Supporting or PM6_Supporting) |
| 1.0 | Moderate (PS2_Moderate or PM6) |
| 2.0 | Strong (PS2 or PM6_Strong) |
| 4.0 | Very Strong (PS2_VeryStrong or PM6_VeryStrong) |

---

### PS3 - Functional Studies

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.

**Note:** Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.

**VCEP Specifications:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product. Approved assays for PS3 usage are available in the supplemental materials.

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Moderate (PS3_Moderate)** | Two or more different approved assays | Gene-specific, Strength |
| **Supporting (PS3_Supporting)** | One approved assay | Gene-specific, Strength |

#### Approved Functional Assay for LZTR1

**LZTR1 Stability and Localization Assay**

| Parameter | Details |
|-----------|---------|
| **PMID** | 30481304, 30442766 |
| **Authors** | Motta, Bigenzahn |
| **Year** | 2019, 2018 |
| **Assay Description** | Expression levels and stability of a representative panel of NS-causing and dominant schwannomatosis-associated LZTR1 variants. Western blot analysis shows WT and variant LZTR1 protein levels in transfected COS-1/HeLa/HEK293T cells, with or without stimulation following basal conditions |
| **Material Used** | Transfected COS-1 cells basally and after CHX treatment; Transfected HeLa cells under basal conditions; Transfected HEK293T cells under basal conditions |
| **Readout Type** | Semi-quantitative (Qualitative) |
| **Readout Description** | Accelerated degradation/visualization of the subcellular localization/stability of mutant LZTR1 protein |
| **Biological Replicates** | Met |
| **Technical Replicates** | Met; Stability & Localization are assayed in tandem |
| **Positive Control** | Met; WT |
| **Negative Control** | Met; empty, LZTR1 ΔBTB2, ΔKelch, and/or ΔBTB1+2 |
| **Statistical Analysis** | Student's t-test |
| **Threshold for Normal** | Normal LZTR1 protein levels/Golgi localization (applies to DN variants and a subset of LoF variants) |
| **Threshold for Abnormal** | Decreased LZTR1 protein levels/abnormal localization within cells (applies to a subset of LoF variants only - recessive NS form) |
| **Approved Strength** | PS3_Supporting; BS3_NA |
| **Comment** | Due to limited control availability and reproducibility by multiple laboratories, this gene-specific assay may only provide supporting evidence at this time |

---

### PS4 - Prevalence in Affected

**Original ACMG Summary:** The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.

**Note 1:** Relative risk (RR) or odds ratio (OR), as obtained from case-control studies, is >5.0 and the confidence interval around the estimate of RR or OR does not include 1.0.

**Note 2:** In instances of very rare variants where case-control studies may not reach statistical significance, the prior observation of the variant in multiple unrelated patients with the same phenotype, and its absence in controls, may be used as moderate level of evidence.

**VCEP Specifications:** Please reference the Case Level Inheritance Flowchart before applying PS4.

**For Dominant-negative variants:** Strength adjustment using point-based scoring for autosomal dominant cases with RASopathy phenotypic specifications.

**For Dominant loss-of-function variants:** Usage of this rule is case specific based on the inheritance of the variant and only PS4 OR PM3 can be applied to a single case. 1 point awarded for autosomal dominant cases with isolated schwannomatosis consistent with the loss-of-function disease mechanism. Loss-of-function variants observed in cases with autosomal recessive NS should only be counted using PM3.

#### PS4 Point System

| Phenotypic Consistency | Points per Proband |
|------------------------|-------------------|
| Individual well-phenotyped with features of a RASopathy | 1 |
| Limited phenotypic information compatible with RASopathy* | 0.5 |
| No clinical information or isolated clinical features | 0 |
| Well-phenotyped but consistent with non-RASopathy disorder** | -1 |

*\*Applicable to prenatal cases, cases with a clinical order of a RASopathy panel without clinical information, and cases with limited clinical information in other global tests (such as WES). Phenotypes for prenatal cases include hypertrophic cardiomyopathy, increased nuchal translucency, cystic hygroma, or hydrops.*

*\*\*Negative points for PS4 represent proband affected with a non-RASopathy congenital disorder rather than a healthy individual (BS2). This typically applies to probands tested by exome analysis with multiple other clinical features supporting a distinct syndromic disorder (e.g. CHARGE, CdLS).*

#### PS4 Evidence Strength Thresholds

| Points | Strength Level |
|--------|----------------|
| >=1 | Supporting (PS4_Supporting) |
| >=3 | Moderate (PS4_Moderate) |
| >=5 | Strong (PS4) |

---

### PM1 - Mutational Hot Spot

**Original ACMG Summary:** Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.

**VCEP Specifications:** *Not Applicable*

**Comments:** Not applicable at this time.

---

### PM2 - Absent from Controls

**Original ACMG Summary:** Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

**Caveat:** Population data for indels may be poorly called by next generation sequencing.

**VCEP Specifications:** The variant must be absent from controls (gnomAD). For variants in LZTR1, PM2_P <=0.0025% may be applied to support AR disease.

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Supporting (PM2_Supporting)** | The variant must be absent from controls (gnomAD). For variants in LZTR1, PM2_P <=0.0025% may be applied to support AR disease. | Disease-specific, Gene-specific, Strength |

---

### PM3 - In Trans with Pathogenic

**Original ACMG Summary:** For recessive disorders, detected in trans with a pathogenic variant.

**Note:** This requires testing of parents (or offspring) to determine phase.

**VCEP Specifications:** Please reference the Case Level Inheritance Flowchart before applying PM3.

Usage of this rule is case specific based on the inheritance of the variant and only PS4 OR PM3 can be applied to a single case. Cases with autosomal recessive NS are scored using PM3, as defined by SVI. Cases with autosomal dominant isolated schwannomatosis should be counted using PS4.

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Very Strong (PM3_VeryStrong)** | >=4 points | Disease-specific, Gene-specific, Strength |
| **Strong (PM3_Strong)** | >=2 points | Disease-specific, Gene-specific, Strength |
| **Moderate (PM3)** | >=1 points | Disease-specific, Gene-specific |
| **Supporting (PM3_Supporting)** | >=0.5 points | Disease-specific, Gene-specific, Strength |

#### PM3 Point System (Per Proband) - Standard SVI Scoring

| Classification/Zygosity of Other Variant | Confirmed in Trans | Phase Unknown |
|------------------------------------------|-------------------|---------------|
| Pathogenic or Likely pathogenic variant | 1.0 | 0.5 (P) / 0.25 (LP) |
| Homozygous (non-consanguineous) | 1.0 | 1.0 |
| Homozygous (consanguineous, max 0.5/family) | 0.5 | 0.5 |
| VUS (max 0.5 total) | 0.25 | 0.0 |

---

### PM4 - Protein Length Changes

**Original ACMG Summary:** Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

**VCEP Specifications:** Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Moderate (PM4)** | No known repetitive areas in gene. Use as described. | General recommendation |

---

### PM5 - Novel Missense at Same Residue

**Original ACMG Summary:** Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.

**Example:** Arg156His is pathogenic; now you observe Arg156Cys.

**Caveat:** Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:** Applicable for observed analogous residue positions in LZTR1. PM1 and PM5 may be used in conjunction at moderate levels, however, PM1 may not be applied if PM5_Strong is applied to avoid overweighting.

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Strong (PM5_Strong)** | >=2 different [likely] pathogenic residue changes at the same codon observed in >=5 probands | Strength |
| **Moderate (PM5)** | 1 [likely] pathogenic residue change at the same codon | Disease-specific |

---

### PM6 - De Novo (Assumed)

**Original ACMG Summary:** Assumed de novo, but without confirmation of paternity and maternity.

**VCEP Specifications:** Follow SVI recommendations for point-based scoring in conjunction with PS2 (see Reference 1) and phenotypic specifications: full points awarded with RASopathy phenotypes, reduced points applicable to cases with minimal phenotypic information (i.e. prenatal cases, cases with a clinical order of a RASopathy panel without clinical information, and cases with limited clinical information in other global tests (such as WES)).

| Strength | Points | Modification Type |
|----------|--------|-------------------|
| **Strong (PM6_Strong)** | 2 points | Strength |
| **Moderate (PM6)** | 1 point | None |
| **Supporting (PM6_Supporting)** | 0.5 points | Strength |

*See PS2 section for full point scoring table.*

---

### PP1 - Co-segregation

**Original ACMG Summary:** Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.

**Note:** May be used as stronger evidence with increasing segregation data.

**VCEP Specifications:** Segregation in more than one family is recommended.

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Strong (PP1_Strong)** | >=7 informative meioses | Strength |
| **Moderate (PP1_Moderate)** | >=5 informative meioses | Strength |
| **Supporting (PP1)** | >=3 informative meioses | Disease-specific |

---

### PP2 - Missense in Constrained Gene

**Original ACMG Summary:** Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.

**VCEP Specifications:** *Not Applicable*

**Comments:** Not applicable because missense z score is <3.09 in gnomAD.

---

### PP3 - Computational Evidence

**Original ACMG Summary:** Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).

**Caveat:** As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.

**VCEP Specifications:** For missense variants: REVEL >= 0.7. For splicing impact, predicted outcome must match disease mechanism.

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Supporting (PP3)** | For missense variants: REVEL >= 0.7. For splicing impact, predicted outcome must match disease mechanism. | Disease-specific |

---

### PP4 - Phenotype Specificity

**Original ACMG Summary:** Patient's phenotype or family history is highly specific for a disease with a single genetic etiology.

**VCEP Specifications:** *Not Applicable*

**Comments:** PP4 is not applicable due to genetic heterogeneity.

---

### PP5 - Reputable Source

**Original ACMG Summary:** Reputable source recently reports variant as pathogenic, but the evidence is not available to the laboratory to perform an independent evaluation.

**VCEP Specifications:** *Not Applicable*

This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee. (PMID: 29543229)

---

## Benign Criteria

### BA1 - Allele Frequency >5%

**Original ACMG Summary:** Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

**VCEP Specifications:** GnomAD filtering allele frequency >=0.05%.

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Stand Alone (BA1)** | GnomAD filtering allele frequency >=0.05% | Disease-specific |

---

### BS1 - Frequency Greater Than Expected

**Original ACMG Summary:** Allele frequency is greater than expected for disorder.

**VCEP Specifications:** GnomAD filtering allele frequency >=0.025%.

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Strong (BS1)** | GnomAD filtering allele frequency >=0.025% | Disease-specific |

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

#### BS2 Evidence Strength Thresholds

| Points | Strength Level |
|--------|----------------|
| -1 | Supporting (BS2_Supporting) |
| N/A | Moderate (not applicable) |
| -3.0 | Strong (BS2) |

---

### BS3 - Functional Studies (No Effect)

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

**VCEP Specifications:** *Not Applicable*

**Comments:** Approved functional studies are available for each individual gene in the supplemental material. Additional functional studies can be submitted to the expert panel for approval.

---

### BS4 - Lack of Segregation

**Original ACMG Summary:** Lack of segregation in affected members of a family.

**Caveat:** The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.

**VCEP Specifications:** Lack of segregation in affected members of a family.

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Strong (BS4)** | Requires only one informative meiosis | General recommendation |

---

### BP1-BP7 - Benign Supporting

| Criterion | Status | Specification |
|-----------|--------|---------------|
| **BP1** | *Not Applicable* | Not applicable, both missense and truncating variants can cause disease |
| **BP2** | Applicable | For each case, -1 point applies when phenotype inconsistent with a RASopathy and causative variant has been identified (ex. WES cases) OR alternative molecular cause of a RASopathy and the phenotype is consistent with expected severity of the RASopathy in the same gene (and/or in conjunction with BP5 in a different gene) |
| **BP3** | *Not Applicable* | No known benign repetitive areas in RASopathy genes |
| **BP4** | Applicable | For missense variants: REVEL <=0.3. For splicing variants: predicted outcome is negligible or does not match disease mechanism |
| **BP5** | Applicable | For each case, -1 point applies when phenotype inconsistent with a RASopathy and causative variant has been identified (ex. WES cases) OR alternative molecular cause of a RASopathy and the phenotype is consistent with expected severity of the RASopathy in a different gene (and/or in conjunction with BP2 in the same gene) |
| **BP6** | *Not Applicable* | This criterion is not for use as recommended by the ClinGen SVI VCEP Review Committee (PMID: 29543229) |
| **BP7** | Applicable | A synonymous (silent) variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved. This rule is also applicable for intronic positions (except canonical splice sites) or non-coding variants and should be used in conjunction with BP4 |

#### BP2/BP5 Point System

| Phenotypic Consistency | Points per Individual |
|------------------------|----------------------|
| Phenotype inconsistent with a RASopathy and causative variant has been identified, **OR** Molecular cause of a RASopathy is identified in a different RASopathy gene, **OR** Molecular cause of a RASopathy is identified in *trans* or *cis* with the variant being classified | -1 |
| Phenotype inconsistent with a RASopathy and no causative variant identified/reported | 0 |

#### BP2/BP5 Evidence Strength Thresholds

| Points | Strength Level |
|--------|----------------|
| -1 | Supporting (BP5/BP2) |
| N/A | Moderate (not applicable) |
| -3.0 | Strong (BP5_Strong/BP2_Strong) |

---

## Rules for Combining Criteria

### Pathogenic Classification

| Criteria Combination |
|---------------------|
| 1 Very Strong (PVS1, PS2_VeryStrong, PM3_VeryStrong) **AND** >=1 Strong (PVS1_Strong, PS1, PS2, PS4, PM3_Strong, PM5_Strong, PM6_Strong, PP1_Strong) |
| 1 Very Strong (PVS1, PS2_VeryStrong, PM3_VeryStrong) **AND** >=2 Moderate (PVS1_Moderate, PS2_Moderate, PS4_Moderate, PM3, PM4, PM5, PM6, PP1_Moderate) |
| 1 Very Strong (PVS1, PS2_VeryStrong, PM3_VeryStrong) **AND** 1 Moderate (PVS1_Moderate, PS2_Moderate, PS4_Moderate, PM3, PM4, PM5, PM6, PP1_Moderate) **AND** 1 Supporting (PVS1_Supporting, PS3_Supporting, PS4_Supporting, PM2_Supporting, PM3_Supporting, PM6_Supporting, PP1, PP3) |
| 1 Very Strong (PVS1, PS2_VeryStrong, PM3_VeryStrong) **AND** >=2 Supporting (PVS1_Supporting, PS3_Supporting, PS4_Supporting, PM2_Supporting, PM3_Supporting, PM6_Supporting, PP1, PP3) |
| >=2 Strong (PVS1_Strong, PS1, PS2, PS4, PM3_Strong, PM5_Strong, PM6_Strong, PP1_Strong) |
| 1 Strong (PVS1_Strong, PS1, PS2, PS4, PM3_Strong, PM5_Strong, PM6_Strong, PP1_Strong) **AND** >=3 Moderate (PVS1_Moderate, PS2_Moderate, PS4_Moderate, PM3, PM4, PM5, PM6, PP1_Moderate) |
| 1 Strong (PVS1_Strong, PS1, PS2, PS4, PM3_Strong, PM5_Strong, PM6_Strong, PP1_Strong) **AND** 2 Moderate (PVS1_Moderate, PS2_Moderate, PS4_Moderate, PM3, PM4, PM5, PM6, PP1_Moderate) **AND** >=2 Supporting (PVS1_Supporting, PS3_Supporting, PS4_Supporting, PM2_Supporting, PM3_Supporting, PM6_Supporting, PP1, PP3) |
| 1 Strong (PVS1_Strong, PS1, PS2, PS4, PM3_Strong, PM5_Strong, PM6_Strong, PP1_Strong) **AND** 1 Moderate (PVS1_Moderate, PS2_Moderate, PS4_Moderate, PM3, PM4, PM5, PM6, PP1_Moderate) **AND** >=4 Supporting (PVS1_Supporting, PS3_Supporting, PS4_Supporting, PM2_Supporting, PM3_Supporting, PM6_Supporting, PP1, PP3) |

### Likely Pathogenic Classification

| Criteria Combination |
|---------------------|
| 1 Very Strong (PVS1, PS2_VeryStrong, PM3_VeryStrong) **AND** 1 Moderate (PVS1_Moderate, PS2_Moderate, PS4_Moderate, PM3, PM4, PM5, PM6, PP1_Moderate) |
| 1 Strong (PVS1_Strong, PS1, PS2, PS4, PM3_Strong, PM5_Strong, PM6_Strong, PP1_Strong) **AND** 1 Moderate (PVS1_Moderate, PS2_Moderate, PS4_Moderate, PM3, PM4, PM5, PM6, PP1_Moderate) |
| 1 Strong (PVS1_Strong, PS1, PS2, PS4, PM3_Strong, PM5_Strong, PM6_Strong, PP1_Strong) **AND** >=2 Supporting (PVS1_Supporting, PS3_Supporting, PS4_Supporting, PM2_Supporting, PM3_Supporting, PM6_Supporting, PP1, PP3) |
| >=3 Moderate (PVS1_Moderate, PS2_Moderate, PS4_Moderate, PM3, PM4, PM5, PM6, PP1_Moderate) |
| 2 Moderate (PVS1_Moderate, PS2_Moderate, PS4_Moderate, PM3, PM4, PM5, PM6, PP1_Moderate) **AND** >=2 Supporting (PVS1_Supporting, PS3_Supporting, PS4_Supporting, PM2_Supporting, PM3_Supporting, PM6_Supporting, PP1, PP3) |
| 1 Moderate (PVS1_Moderate, PS2_Moderate, PS4_Moderate, PM3, PM4, PM5, PM6, PP1_Moderate) **AND** >=4 Supporting (PVS1_Supporting, PS3_Supporting, PS4_Supporting, PM2_Supporting, PM3_Supporting, PM6_Supporting, PP1, PP3) |

### Benign Classification

| Criteria Combination |
|---------------------|
| >=2 Strong (BS1, BS2, BS4, BP2_Strong, BP5_Strong) |
| 1 Stand Alone (BA1) |

### Likely Benign Classification

| Criteria Combination |
|---------------------|
| 1 Strong (BS1, BS2, BS4, BP2_Strong, BP5_Strong) **AND** 1 Supporting (BS2_Supporting, BP1, BP2, BP4, BP5, BP7) |
| >=2 Supporting (BS2_Supporting, BP1, BP2, BP4, BP5, BP7) |
| 1 Strong (BS1, BS2, BS4, BP2_Strong, BP5_Strong) |
| 1 Strong (BS1) |

---

## Appendices

### Appendix A: Population Frequency Thresholds Summary

| Criterion | Threshold | Strength |
|-----------|-----------|----------|
| BA1 | >=0.05% (gnomAD FAF) | Stand Alone |
| BS1 | >=0.025% (gnomAD FAF) | Strong |
| PM2 | <=0.0025% (gnomAD FAF) | Supporting |

### Appendix B: Computational Predictor Thresholds

| Criterion | Tool | Threshold | Interpretation |
|-----------|------|-----------|----------------|
| PP3 | REVEL | >= 0.7 | Supports pathogenicity |
| BP4 | REVEL | <= 0.3 | Supports benign interpretation |

### Appendix C: Key PMIDs and References

| Reference | Description |
|-----------|-------------|
| PMID: 29543229 | ClinGen SVI recommendations for PP5/BP6 |
| PMID: 30311384 | RASopathy phenotype reference (Table 1) |
| PMID: 30481304 | Motta et al. - LZTR1 functional studies |
| PMID: 30442766 | Bigenzahn et al. - LZTR1 functional studies |
| SVI De Novo Criteria v1.1 | https://clinicalgenome.org/site/assets/files/3461/svi_proposal_for_de_novo_criteria_v1_1.pdf |

### Appendix D: RASopathy Phenotype Reference

For phenotypic assessment in PS2/PM6 and PS4 scoring, refer to Table 1 in PMID: 30311384 for consistent RASopathy phenotypes.

**Phenotypes for prenatal cases include:**
- Hypertrophic cardiomyopathy
- Increased nuchal translucency
- Cystic hygroma
- Hydrops

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 2.0.0 | 12/3/2024 | Current version |
| 1.3.0 | 12/3/2024 | "Observed in >=5 probands" removed from PM5 at Moderate strength |

---

*This document was compiled from ClinGen RASopathy VCEP specifications. For the most current version, please refer to the ClinGen website.*
