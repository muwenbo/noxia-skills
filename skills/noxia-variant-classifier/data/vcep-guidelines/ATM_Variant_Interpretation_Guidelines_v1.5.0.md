# ClinGen Hereditary Breast, Ovarian and Pancreatic Cancer VCEP Variant Interpretation Guidelines for ATM

**Version:** 1.5.0
**Released:** 11/7/2025
**Affiliation:** Hereditary Breast, Ovarian and Pancreatic Cancer VCEP
**Expert Panel Page:** https://www.clinicalgenome.org/affiliation/50039
**Based on:** Richards et al., 2015 ACMG/AMP Guidelines

---

## Gene Information

| Attribute | Value |
|-----------|-------|
| **Gene** | ATM (HGNC:795) |
| **HGNC Name** | ATM serine/threonine kinase |
| **Transcript** | NM_000051.3 / ENST00000278616.8 |
| **Diseases** | ATM-related cancer predisposition (MONDO:0700270) - AD; Ataxia telangiectasia (MONDO:0008840) - AR; Ataxia-telangiectasia variant (MONDO:0018266) - AR |
| **Inheritance** | Autosomal dominant (AD) and Autosomal recessive (AR) |

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
   - [BA1 - Allele Frequency](#ba1---allele-frequency)
   - [BS1 - Frequency Greater Than Expected](#bs1---frequency-greater-than-expected)
   - [BS2 - Observed in Healthy Adult](#bs2---observed-in-healthy-adult)
   - [BS3 - Functional Studies (No Effect)](#bs3---functional-studies-no-effect)
   - [BS4 - Lack of Segregation](#bs4---lack-of-segregation)
   - [BP1 - Missense in Truncating Gene](#bp1---missense-in-truncating-gene)
   - [BP2 - Observed in Trans/Cis](#bp2---observed-in-transcis)
   - [BP3 - In-frame Deletions/Insertions](#bp3---in-frame-deletionsinsertions)
   - [BP4 - Computational Evidence (Benign)](#bp4---computational-evidence-benign)
   - [BP5 - Alternate Molecular Basis](#bp5---alternate-molecular-basis)
   - [BP6 - Reputable Source (Benign)](#bp6---reputable-source-benign)
   - [BP7 - Synonymous Variants](#bp7---synonymous-variants)
3. [Rules for Combining Criteria](#rules-for-combining-criteria)
4. [Appendices](#appendices)

---

## Pathogenic Criteria

### PVS1 - Null Variant

**Original ACMG Summary:** Null variant (nonsense, frameshift, canonical ±1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.

**Caveats:**
- Beware of genes where LOF is not a known disease mechanism
- Use caution interpreting LOF variants at the extreme 3' end of a gene
- Use caution with splice variants predicted to lead to exon skipping but leave the remainder of the protein intact
- Use caution in the presence of multiple transcripts

**VCEP Specifications:**

Use the **ATM PVS1 Decision Tree** (see Appendix A).

Key specifications:
- **PVS1:** Predicted splice defect
- **PVS1_Strength(RNA):** Observed splice defect
- The default RefSeq transcript for nucleotide (c.) annotation is **NM_000051.3/ENST00000278616.8**
- All exons from this transcript can be considered constitutive exons without major alternate splice isoforms
- ATM is occasionally annotated with multiple non-coding first exons; exon numbering must be carefully reviewed

**Critical Domains:**
- **FATKIN domains (FAT/PI3K/FATC)** - considered *critical* for ATM protein function (PMID: 28508083, 31740029, 31320732)
  - PVS1 alterations predicted to escape NMD but adversely affecting these domains → **PVS1** (upgraded from PVS1_Strong)
- **HEAT repeat domain** - considered *important* for protein function (PMID: 10980530, 19535770, 30819809, 15054841, 22927201, 19691550, 10330348, 17124347, 8845835, 16266405, 9463314, 24090759, 22213089)
  - PVS1-eligible alterations predicted to escape NMD but adversely affecting HEAT repeat domain → **PVS1_Strong** (limited to strong due to lack of known missense pathogenic alterations)
- The most 3'/C-terminal residue considered to be pathogenic is **p.R3047** (PMID: 8755918, 19691550, 18560558, 10980530, 26628246)

**NOTE:** Many diagrams show FAT, PI3K and FATC domains as separated by spacers; however, these are not empirically derived and there is evidence of missense pathogenic alterations in the 'spacer' regions. This VCEP considers them a contiguous domain (PMID: 28508083).

**RNA Evidence Considerations for PVS1_Variable(RNA):**
- Starting material (patient material preferable to in vitro minigene)
- Use of NMD inhibitors (critical in assays using cells vs. blood)
- Primer design (comprehensive to capture multicassette events)
- Method of quantification (capillary electrophoresis preferable; SNP analysis most preferred)
- Quantification (complete effects have increased weight over incomplete effects)

**Important:** If RNA data reflect substantial variant-specific impact, do not use both PVS1(RNA) and PP3 or BP4. If RNA data reflect no variant-specific impacts, PP3 or BP4 may be applied in conjunction with BP7(RNA).

#### Strength Levels

| Strength | Criteria |
|----------|----------|
| **Very Strong** | Use ATM PVS1 Decision Tree |
| **Strong** | Use ATM PVS1 Decision Tree |
| **Moderate** | Use ATM PVS1 Decision Tree |
| **Supporting** | Use ATM PVS1 Decision Tree |

---

### PS1 - Same Amino Acid Change

**Original ACMG Summary:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.

**Caveat:** Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:**

- **Missense:** Use as ascribed only when a splice defect is ruled out for both alterations (by RNA analysis and/or in silico splice predictions)
- **Splicing:** Use ATM PS1 Splicing table for splicing variants with similar predictions or observations of splice defect (PMID: 36865205)

#### PS1 Splicing Code Weights

| VUA Location | Baseline Code | Reference Position | P Reference | LP Reference |
|--------------|---------------|-------------------|-------------|--------------|
| Outside ±1,2 dinucleotide | PP3 | Same nucleotide | PS1 | PS1_Moderate |
| Outside ±1,2 dinucleotide | PP3 | Within same donor/acceptor motif (including ±1,2) | PS1_Moderate | PS1_Supporting |
| At ±1,2 dinucleotide | PVS1 | Within same donor/acceptor dinucleotide | PS1_Supporting | N/A |
| At ±1,2 dinucleotide | PVS1 | Within same motif, outside dinucleotide | PS1_Supporting | PS1_Supporting |
| At ±1,2 dinucleotide | PVS1_Strong/Moderate/Supporting | Within same donor/acceptor dinucleotide | PS1 | N/A |
| At ±1,2 dinucleotide | PVS1_Strong/Moderate/Supporting | Within same motif, outside dinucleotide | PS1_Moderate | PS1_Supporting |

**Prerequisites:**
- The predicted event of the VUA must precisely match the predicted event of the known (likely) pathogenic variant
- The strength of prediction for VUA must be similar or higher than the known variant
- (Likely) pathogenic variant should be assigned classification using VCEP specifications
- For GT-AG introns: donor motif = last 3 bases of exon + 6 nt intronic; acceptor motif = first base of exon + 20 nt upstream

#### Strength Levels

| Strength | Criteria |
|----------|----------|
| **Strong** | Missense: Use for missense changes as long as splicing is ruled-out for both alterations; Splicing: Use ATM PS1 Splicing table |
| **Moderate** | Use ATM PS1 Splicing table for splicing variants with similar predictions or observations |
| **Supporting** | Use ATM PS1 Splicing table for splicing variants with similar predictions or observations |

---

### PS2 - De Novo (Confirmed)

**Original ACMG Summary:** De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.

**VCEP Specifications:** ***Not Applicable***

**Reason:** Do not use for AD or AR disease: Informative de novo occurrences have not yet been observed and de novo AR conditions are unlikely to be informed by phase.

---

### PS3 - Functional Studies

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.

**VCEP Specifications:**

- For **protein**: See detailed notes on ATM-specific assays below
- For **RNA**: Use code PVS1_Strength(RNA) and modulate strength based on assay quality and quantity (curator discretion)

**IMPORTANT NOTE:** Do not use phenotypic evidence (e.g., lack of ATM activity in cells from an A-T patient) as functional data. That is a general assay that confirms the patient's diagnosis and should be considered as part of PM3. However, splice data from patient material can be considered a functional effect because the effect is relatively specific to the variant.

#### Strength Levels

| Strength | Criteria |
|----------|----------|
| **Strong** | Do not use as strong |
| **Moderate** | Use when a variant fails to rescue **both** an ATM-specific feature (e.g., phosphorylation of ATM-specific targets) **AND** radiosensitivity |
| **Supporting** | Use when a variant fails to rescue an ATM-specific feature only (e.g., phosphorylation of ATM-specific targets). Do not use for radiosensitivity-only as that is not specific to ATM deficiency |

#### Approved Functional Assays

**1. ATM Kinase Activity Assays**

| Parameter | Mitui 2009 (PMID: 18634022) | Barone 2009 (PMID: 19431188) | Scott 2002 (PMID: 11805335) |
|-----------|----------------------------|-----------------------------|-----------------------------|
| **Assay Description** | Stable transfection of ATM cDNA constructs in ATM null cell line; kinase activity by Western Blot | Stable transfection of ATM cDNA constructs in ATM null cell line; kinase activity by Western Blot | Stable transfection of ATM cDNA constructs in ATM null cell line; kinase activity by Western Blot |
| **Material** | ATM null patient LCL (AT7LA1); variants by site-directed mutagenesis | ATM null patient LCLs (patient 118-3); variants by site-directed mutagenesis | ATM null patient LCLs (AT1ABR); variants by site-directed mutagenesis |
| **Readout** | Phosphorylation of ATM-S1981 and SMC1 (S957 or S966) after irradiation | Phosphorylation of SMC1, NBS1, CHK2, p53, ATM-S1981 at multiple timepoints | Phosphorylation of p53-Ser-15 (in vivo and in vitro) |
| **Positive Control** | WT cDNA (pMAT1) and ATM WT LCLs (NAT2) | WT cDNA (pTAM2) | WT cDNA (pMAT3) |
| **Negative Control** | ATM null cells (AT7LA1) | Empty cDNA (pMEP4) | Un-induced cells |
| **Approved** | Yes | Yes | Yes |
| **Proposed Strength** | PS3_Supporting / BS3_Supporting | PS3_Supporting / BS3_Supporting | PS3_Supporting / BS3_Supporting |

**2. ATM Radiosensitivity Assays**

| Parameter | Mitui 2009 (PMID: 18634022) | Scott 2002 - ICA (PMID: 11805335) | Scott 2002 - Viability (PMID: 11805335) |
|-----------|----------------------------|----------------------------------|----------------------------------------|
| **Assay Description** | Stable expression of cDNA in ATM null cell line; cellular radiosensitivity | Stable transfection; radiation induced chromosome aberrations (ICAs) | Stable transfection; cell viability post-irradiation |
| **Material** | ATM null patient LCL (AT7LA1) | ATM null patient LCLs (AT1ABR) | ATM null patient LCLs (AT1ABR) |
| **Readout** | % survival fraction (SF) by MTT staining after 1 Gy | ICAs per metaphase after 1 Gy | Viable cells up to 4 days post 1-4 Gy |
| **Normal Threshold** | SF >36% (50.1±13.5%) | ~1 ICA (<1.5) | % survival >10 at 4 days |
| **Abnormal Threshold** | SF <21% (13.1±7.2%) | 2.98-3.20 ICAs per metaphase | % survival <10 at 4 days |
| **Proposed Strength** | PS3_Moderate (only with PS3_Supporting from kinase) / BS3_Supporting | PS3_Moderate (only with PS3_Supporting from kinase) / BS3_Supporting | PS3_Moderate (only with PS3_Supporting from kinase) / BS3_Supporting |

**Important Notes:**
- No weight should be applied if only radiosensitivity is available
- No weight should be applied if radiosensitivity and kinase assay are conflicting

---

### PS4 - Prevalence in Affected

**Original ACMG Summary:** The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.

**VCEP Specifications:**

- **PS4_Moderate:** Do not use. Proband counting for genes causing a common disorder needs to be calibrated in a population-specific way before use.

#### Strength Levels

| Strength | Criteria |
|----------|----------|
| **Strong** | Case-control studies; p-value ≤0.05 **AND** (Odds ratio, hazard ratio, or relative risk ≥2 **OR** lower 95% CI ≥1.5) |

---

### PM1 - Mutational Hot Spot

**Original ACMG Summary:** Located in a mutational hot spot and/or critical and well-established functional domain without benign variation.

**VCEP Specifications:** ***Not Applicable***

**Reason:** Do not use: Benign and pathogenic variants are known to occur within the same domains and germline mutational hotspots are not well defined at this time.

---

### PM2 - Absent from Controls

**Original ACMG Summary:** Absent from controls (or at extremely low frequency if recessive) in population databases.

**VCEP Specifications:**

- Is not considered a conflicting piece of evidence for variants that otherwise are likely benign/benign
- Use as **PM2_Supporting** (not moderate)

#### Strength Level

| Strength | Criteria |
|----------|----------|
| **Supporting** | Frequency **≤0.001%** in gnomAD v4 dataset. If n=1 in a single subpopulation, that is sufficiently rare and PM2_Supporting would apply. |

---

### PM3 - In Trans with Pathogenic

**Original ACMG Summary:** For recessive disorders, detected in trans with a pathogenic variant.

**VCEP Specifications:**

See **ATM PM3/BP2 table** for approach to assign points per proband.

**General Considerations:**
- Ataxia Telangiectasia (A-T) is a rare, severe, early-onset disease with some exceptions denoted 'variant' or 'atypical' A-T
- Phenotypes associated with A-T are very specific and do not generally require differential diagnosis
- Publications claiming a 'clinical diagnosis of A-T' are taken at face value and granted a 'confident' diagnosis
- Variant may not exceed general population frequency >0.01%
- If the variant has co-occurred with at least 2 different P/LP variants, one co-occurrence must be weighed as phase unknown while remaining can be assumed in trans
- Multiple unrelated cases are additive

#### Phenotype Definitions

**CONFIDENT PHENOTYPE** (must include Laboratory result):
- Presence of ≥2 Laboratory results 1-4, **OR**
- Presence of Clinical feature 1a or 1b **AND** Laboratory result 1 or 2, **OR**
- Presence of Clinical feature 2 or 3 **AND** Laboratory result 1 or 2

**CONSISTENT PHENOTYPE** (does not require laboratory result):
- Presence of two or more Clinical features of ataxia (1a-1e), **OR**
- Presence of one Clinical feature 1a or 1b **AND** either Clinical feature 2 or 3

#### Clinical Features (Neurological and MRI findings)

1. **Progressive cerebellar ataxia**, manifesting as:
   - a. Progressive truncal/limb ataxia
   - b. Cerebellar degeneration (atrophy of frontal and posterior vermis and both hemispheres by MRI)
   - c. Oculomotor apraxia or abnormal ocular saccades
   - d. Choreoathetosis or dystonia
   - e. Peripheral axonal neuropathy OR Anterior horn cell neuronopathy
2. **Oculocutaneous telangiectasia** of the conjunctivae, ears, or face
3. **Immunodeficiency** (often frequent infections) and/or leukemia/lymphoma

#### Laboratory Results

1. ATM protein levels **≤15%** of controls in patient fibroblast or lymphoblastoid cell lines (if slightly >15%, ATM kinase activity must be "negative or low or residual")
2. Elevated serum alpha-fetoprotein (AFP) levels **>65 µg/L** in a patient ≥2 years old
3. Increased sensitivity to ionizing radiation in patient fibroblast or lymphoblastoid cell lines
4. Presence of a 7;14 chromosomal translocation in patient peripheral blood cells (≥5% of cells)

**Notes:**
1. ATM protein levels ≤15% show >95% sensitivity and >98% specificity for diagnosing A-T
2. Protein levels >15% may arise due to missense variant, leaky splicing variant, kinase-dead protein, or diagnosis other than A-T

#### PM3 Point System (Per A-T Proband)

| Classification/Zygosity | Confirmed in Trans | Phase Unknown | Second Variant Unidentified or VUS | Homozygous (max 2 individuals) |
|------------------------|-------------------|---------------|-----------------------------------|-------------------------------|
| **Phenotype confident** | 4.0 | 2.0 | 1.0 | 2.0 |
| **Phenotype consistent** | 2.0 | 1.0 | 0.5 | 1.0 |

#### PM3 Evidence Strength Thresholds

| Total Points | Strength Level |
|--------------|----------------|
| 1.0 | PM3_Supporting |
| 2.0 | PM3 (Moderate) |
| 4.0 | PM3_Strong |
| ≥8.0 | PM3_VeryStrong |

**Example:** One individual with 'confident A-T phenotype' homozygous for a variant = 2.0 points. Another individual with 'consistent A-T phenotype' with same variant and another phase-unknown truncating ATM variant = 1.0 points. Total = 3.0 points → PM3 (Moderate).

---

### PM4 - Protein Length Changes

**Original ACMG Summary:** Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

**VCEP Specifications:**

- Do **not** use for in-frame insertions or deletions less than a single exon
- Use for **stop-loss variants only**

#### Strength Level

| Strength | Criteria |
|----------|----------|
| **Moderate** | Use for stop-loss variants |

---

### PM5 - Novel Missense at Same Residue

**Original ACMG Summary:** Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.

**VCEP Specifications:**

Based on location of the most C-terminal known pathogenic variant: **p.Arg3047***

- Use as **PM5_Supporting** (not moderate)
- Do **not** use for start-loss variants
- Do **not** use for missense changes: Multiple amino acid substitutions at the same residue can be pathogenic or benign and bioinformatic tools cannot yet confidently distinguish them

#### Strength Level

| Strength | Criteria |
|----------|----------|
| **Supporting** | Apply to frameshifting or truncating variants with PTCs upstream of p.Arg3047; Apply to splice variants with PTCs upstream of p.Arg3047 where PVS1_VS(RNA) is applied based on high quality observed splicing impact and must be NMD prone |

---

### PM6 - De Novo (Assumed)

**Original ACMG Summary:** Assumed de novo, but without confirmation of paternity and maternity.

**VCEP Specifications:** ***Not Applicable***

**Reason:** Do not use for AD or AR disease: Informative de novo occurrences have not yet been observed and de novo AR conditions are unlikely to be informed by phase.

---

### PP1 - Co-segregation

**Original ACMG Summary:** Co-segregation with disease in multiple affected family members.

**VCEP Specifications:**

- **AR Condition:** Affected relatives must have both variants identified in proband
- **AD Condition:** Do not use - Co-segregation analysis in lower-penetrance genes can lead to false positive results (PMID: 32773770)

#### Strength Levels (AR Condition Only)

| Strength | Criteria |
|----------|----------|
| **Strong** | Segregation in ≥3 affected relatives |
| **Moderate** | Segregation in 2 affected relatives |
| **Supporting** | Segregation in 1 affected relative |

---

### PP2 - Missense in Constrained Gene

**Original ACMG Summary:** Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.

**VCEP Specifications:** ***Not Applicable***

**Reason:** Do not use: ATM does not have a defined low rate of missense benign variation.

---

### PP3 - Computational Evidence

**Original ACMG Summary:** Multiple lines of computational evidence support a deleterious effect on the gene or gene product.

**VCEP Specifications:**

**Important Notes:**
- Splice analysis needs to be considered for all variant types (including missense, frameshift, nonsense, etc.)
- PP3 for splice predictions may **not** be applied in addition to PVS1 or PVS1_Variable(RNA) codes
- Use caution in applying the wrong type of computational evidence (protein vs. RNA)
- The VCEP uses **SpliceAI** as sole predictor for splicing (Jaganathan et al., 2019)
- If RNA data reflect substantial variant-specific impact, do not use both PVS1(RNA) and PP3

#### Strength Level

| Strength | Criteria |
|----------|----------|
| **Supporting** | **Missense:** REVEL >0.7333; **Splicing:** SpliceAI ≥0.2 for silent, missense/in-frame and intronic variants outside donor/acceptor ±1,2 sites |

---

### PP4 - Phenotype Specificity

**Original ACMG Summary:** Patient's phenotype or family history is highly specific for a disease with a single genetic etiology.

**VCEP Specifications:** ***Not Applicable***

**Reasons:**
- **Autosomal Dominant:** Do not use - breast cancer is a disease with multiple genetic etiology (genetic heterogeneity) and there are no features that can readily distinguish hereditary from sporadic causes
- **Autosomal Recessive:** Do not use as a separate line of evidence - such evidence is built into the Ataxia Telangiectasia PM3|BP2 table

---

### PP5 - Reputable Source

**Original ACMG Summary:** Reputable source recently reports variant as pathogenic, but the evidence is not available.

**VCEP Specifications:** ***Not Applicable***

This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PMID: 29543229).

---

## Benign Criteria

### BA1 - Allele Frequency

**Original ACMG Summary:** Allele frequency is above 5% in population databases.

**VCEP Specification (Stand Alone):**

Follow all SVI general guidance on applying population filters.

| Strength | Threshold |
|----------|-----------|
| **Stand Alone** | Grpmax Filtering AF **>0.5%** in gnomAD v4 dataset |

---

### BS1 - Frequency Greater Than Expected

**Original ACMG Summary:** Allele frequency is greater than expected for disorder.

**VCEP Specification:**

Follow all SVI general guidance on applying population filters.

| Strength | Threshold |
|----------|-----------|
| **Strong** | Grpmax Filtering AF **>0.05%** in gnomAD v4 dataset |

---

### BS2 - Observed in Healthy Adult

**Original ACMG Summary:** Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder.

**VCEP Specifications:** ***Not Applicable***

**Reason:** Do not use: ATM has incomplete penetrance.

---

### BS3 - Functional Studies (No Effect)

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

**VCEP Specifications:**

- For **protein**: See detailed notes on ATM-specific assays (same as PS3)
- For **RNA**: Use code BP7_RNA and modulate strength based on assay quality and quantity (curator discretion)

#### Strength Levels

| Strength | Criteria |
|----------|----------|
| **Moderate** | Use when a variant rescues **both** an ATM-specific feature (e.g., phosphorylation of ATM-specific targets) **AND** radiosensitivity |
| **Supporting** | Use when a variant rescues **either** an ATM-specific feature **OR** rescues radiosensitivity |

---

### BS4 - Lack of Segregation

**Original ACMG Summary:** Lack of segregation in affected members of a family.

**VCEP Specifications:** ***Not Applicable***

**Reasons:**
- **AD Condition:** Co-segregation analysis in low penetrance genes can lead to false positive results (PMID: 32773770)
- **AR Condition:** Informative instances of lack of co-segregation in A-T families are too rare to be considered; can also be considered for BP2 if biallelic unaffected patients are observed in an A-T family

---

### BP1 - Missense in Truncating Gene

**Original ACMG Summary:** Missense variant in a gene for which primarily truncating variants are known to cause disease.

**VCEP Specifications:** ***Not Applicable***

**Reason:** Do not use: Missense pathogenic variants are known for ATM.

---

### BP2 - Observed in Trans/Cis

**Original ACMG Summary:** Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder or observed in cis with a pathogenic variant.

**VCEP Specifications:**

See **ATM PM3/BP2 table** for approach to assign points per proband.

**Important:** When assessing homozygous or in trans variants (with a P/LP ATM variant) for possible downgrade in an unaffected individual, the individual should be **≥18 years old** with no evidence of A-T.

#### BP2 Point System (Per Unaffected Non-A-T Adult >18yo Proband)

| Classification | Confirmed in Trans | Phase Unknown | Homozygous |
|---------------|-------------------|---------------|------------|
| **P or LP variant in patient** | -4.0 | -2.0 | Laboratory Setting: -2.0; Database Setting: -1.0 |

*Maximum of -2.0 from homozygous individuals*

#### BP2 Evidence Strength Thresholds

| Total Points | Strength Level |
|--------------|----------------|
| -1.0 | BP2 (Supporting) |
| -2.0 | BP2_Moderate |
| ≤-4.0 | BP2_Strong |

**Notes:**
- Apply only for phenotyped individuals from clinical or research cohorts
- NOT to be applied for data used to assign frequency-based codes
- Variants observed as ≥2 homozygotes in gnomAD are already captured by BA1 or BS1
- VUA should NOT be bioinformatically predicted (or experimentally proven) to have a clinically important effect on protein or mRNA splicing
- Do not use observations in cis

---

### BP3 - In-frame Deletions/Insertions

**Original ACMG Summary:** In-frame deletions/insertions in a repetitive region without a known function.

**VCEP Specifications:** ***Not Applicable***

**Reason:** Do not use.

---

### BP4 - Computational Evidence (Benign)

**Original ACMG Summary:** Multiple lines of computational evidence suggest no impact on gene or gene product.

**VCEP Specifications:**

**Important Notes:**
- Splice analysis needs to be considered for all variant types
- BP4 for splice predictions may **not** be applied in conjunction with BP7_Variable(RNA)
- Use caution in applying the wrong type of computational evidence (protein vs. RNA)
- The VCEP uses **SpliceAI** as sole predictor (thresholds per Walker et al., 2023)
- If RNA data reflect no variant-specific impacts, PP3 or BP4 may be applied with BP7(RNA)

#### Strength Level

| Strength | Criteria |
|----------|----------|
| **Supporting** | **Missense:** REVEL score ≤0.249; **Splicing:** SpliceAI ≤0.1 |

---

### BP5 - Alternate Molecular Basis

**Original ACMG Summary:** Variant found in a case with an alternate molecular basis for disease.

**VCEP Specifications:** ***Not Applicable***

**Reason:** Do not use: Cases with multiple pathogenic variants have been observed with no noticeable difference in phenotype (e.g., BRCA1 and BRCA2). ATM has low penetrance and will naturally occur with other pathogenic variants more frequently.

---

### BP6 - Reputable Source (Benign)

**Original ACMG Summary:** Reputable source recently reports variant as benign, but the evidence is not available.

**VCEP Specifications:** ***Not Applicable***

This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PMID: 29543229).

---

### BP7 - Synonymous Variants

**Original ACMG Summary:** A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.

**VCEP Specifications:**

**BP7: Synonymous and deep intronic**
- Can be used for deep intronic variants beyond (but not including) **+7** (donor) and **-21** (acceptor)
- May also apply BP4 to achieve Likely Benign
- Is not considered a conflicting piece of evidence against a body of evidence supporting a pathogenic splice defect

**BP7_Variable(RNA): RNA functional studies**
- Lack of aberrant splice defect: See PVS1_Variable(RNA) guidance for baseline weights and modifications
- If RNA data reflect substantial variant-specific impact, do not use both PVS1(RNA) and PP3 or BP4
- If RNA data reflect no variant-specific impacts, PP3 or BP4 may be applied with BP7(RNA)

#### Strength Levels

| Strength | Criteria |
|----------|----------|
| **Strong** | BP7_Strong(RNA): Observed lack of aberrant RNA defect for silent substitutions and intronic variants (curator discretion for assay quality) |
| **Moderate** | BP7_Moderate(RNA): Observed lack of aberrant RNA defect for silent substitutions and intronic variants (curator discretion for assay quality) |
| **Supporting** | BP7: Synonymous and deep intronic beyond +7 and -21; BP7(RNA): Observed lack of aberrant RNA defect (curator discretion) |

---

## Rules for Combining Criteria

### Pathogenic Classification

| Criteria Combination |
|---------------------|
| 1 Very Strong **AND** ≥1 Strong |
| 1 Very Strong **AND** ≥2 Moderate |
| 1 Very Strong **AND** 1 Moderate **AND** 1 Supporting |
| 1 Very Strong **AND** ≥2 Supporting |
| ≥2 Strong |
| 1 Strong **AND** ≥3 Moderate |
| 1 Strong **AND** 2 Moderate **AND** ≥2 Supporting |
| 1 Strong **AND** 1 Moderate **AND** ≥4 Supporting |

### Likely Pathogenic Classification

| Criteria Combination |
|---------------------|
| 1 Very Strong **AND** 1 Moderate |
| 1 Strong **AND** 1 Moderate |
| 1 Strong **AND** ≥2 Supporting |
| ≥3 Moderate |
| 2 Moderate **AND** ≥2 Supporting |
| 1 Moderate **AND** ≥4 Supporting |
| 1 Very Strong *(PVS1, PM3_VeryStrong)* **AND** 1 Supporting *(PVS1_Supporting, PS1_Supporting, PS3_Supporting, PM2_Supporting, PM3_Supporting, PM5_Supporting, PP1, PP3)* |

### Benign Classification

| Criteria Combination |
|---------------------|
| ≥2 Strong |
| 1 Stand Alone (BA1) |

### Likely Benign Classification

| Criteria Combination |
|---------------------|
| 1 Strong **AND** 1 Supporting |
| ≥2 Supporting |
| 1 Strong *(BS1, BP2_Strong, BP7_Strong)* |

---

## Appendices

### Appendix A: ATM PVS1 Decision Tree

#### ATM Domain Structure (PMID: 28508083)

| Domain | Amino Acid Range | Exons (Total) | Notes |
|--------|------------------|---------------|-------|
| Spiral | 1-1160 | 2-19 | N-Solenoid containing HEAT/TAN repeats |
| N-pillar | ~1160-1430 | 19-26 | N-Solenoid |
| Pincer Bridge | ~1430-1600 | 26-30 | |
| Pincer C-pillar | ~1600-1680 | 30-32 | |
| Pincer Railing | ~1680-1800 | 32-34 | |
| Pincer Cap | ~1800-1893 | 34-38 | |
| FAT (TRD1) | ~1893+ | 38-40 | FATKIN domain begins |
| FAT (TRD2) | | 40-45 | FATKIN |
| FAT (TRD3) | | 45-50 | FATKIN |
| FAT (HRD) | | 50-55 | FATKIN |
| Kinase domain | 2612-3056 | 55-63 | FATKIN |

#### ATM Exon Map (NM_000051.3/ENST00000278616.8)

**Key:**
- 63 total exons, 62 coding exons
- Start codon in total exon 2 (coding exon 1)
- 3056aa protein
- Overhang on top = 2-nt overhang; Overhang on bottom = 1-nt overhang
- Parallel lines indicate in-frame deletions

#### PVS1 Decision Tree Summary

**Initiation Codon:**
- ≥1 pathogenic variant upstream of closest potential in-frame start codon (p.Met94) → **PVS1** (upgraded from PVS1_Moderate)

**Nonsense or Frameshift:**
- Predicted to undergo NMD (p.Ser2_Glu2979) → **PVS1**
- Not predicted to undergo NMD (p.Leu2980_Val3056):
  - Truncated/altered region is critical (FATKIN 2980-3047), p.Arg3047Ter is most C-terminal known pathogenic → **PVS1** (upgraded from PVS1_Strong)
  - FATKIN (3048-3056), role unknown → **PVS1_N/A** (downgraded from PVS1_Moderate)

**Deletion (Single exon to full gene):**
- Full gene deletion → **PVS1_SA**
- Single/multi-exon deletion disrupting reading frame, predicted NMD → **PVS1**
- Single/multi-exon deletion NOT disrupting reading frame, NOT predicted NMD:
  - Altered region is critical (deletion involving ≥1 exon in FATKIN, exons 38-63) → **PVS1** (upgraded from PVS1_Strong)
  - Altered region is relevant (deletion involving ≥1 exon in HEAT repeats, exons 2-38) → **PVS1_Strong**
- Single/multi-exon deletion preserving reading frame:
  - Truncated/altered region is critical (FATKIN, exons 38-63) → **PVS1** (upgraded from PVS1_Strong)

**Duplication (≥1 exon, completely within gene):**
- Reading frame disrupted, NMD predicted → **PVS1** (if proven in tandem) or **PVS1_Strong** (if presumed)
- Preserves reading frame, disrupts FATKIN (both breakpoints within domain) → **PVS1** (proven) or **PVS1_Strong** (presumed)
- Preserves reading frame, disrupts HEAT repeats (both breakpoints within domain) → **PVS1_Strong** (proven) or **PVS1_Moderate** (presumed)
- Preserves reading frame, contains full coding sequence of one HEAT repeats and one FATKIN domain → **PVS1_N/A**
- Proven NOT in tandem → **PVS1_N/A**

**GT-AG ±1,2 Splice Sites (G>non-G at last nucleotide of exon when adjacent intronic sequence is not GT):**

*N-Solenoid (HEAT repeats) - p.Met1_Glu1892, exons 2-38:*

| Consequence | PVS1 Level |
|-------------|------------|
| Exon skipping/cryptic site disrupts reading frame (all predicted NMD) | **PVS1** (List A) |
| Exon skipping/cryptic site preserves reading frame | **PVS1_Strong** (List B) |
| Special case: cryptic site preserves frame + very small indel + PROVEAN pathogenic | **PVS1_Supporting** (List C - downgraded from PVS1_Strong) |

*FATKIN - p.Ser1893_Val3056, exons 38-63 (p.Arg3047Ter is most C-terminal known pathogenic):*

| Consequence | PVS1 Level |
|-------------|------------|
| Exon skipping/cryptic site disrupts reading frame, predicted NMD (p.Ser1893_Glu2979) | **PVS1** (List D) |
| Exon skipping/cryptic site disrupts reading frame, NOT predicted NMD (p.Leu2980_Val3056) | **PVS1** (List E - upgraded from PVS1_Strong) |
| Special case: cryptic site preserves frame + very small indel + PROVEAN pathogenic | **PVS1_Supporting** (List F - downgraded from PVS1_Strong) |

**GC-AG ±1,2 Splice Sites:**
- No splicing alteration predicted (creates GC functional site): c.6347+2T>, c.6807+2T>, c.7629+2T>, c.8786+2T>, c.8987+2T> → **PVS1_N/A**
- Variant improves donor site: c.7515+2C>T → **PVS1_N/A**

### Appendix B: Population Frequency Thresholds Summary

| Criterion | Threshold | Strength | Database |
|-----------|-----------|----------|----------|
| BA1 | >0.5% (>0.005) Grpmax Filtering AF | Stand Alone | gnomAD v4 |
| BS1 | >0.05% (>0.0005) Grpmax Filtering AF | Strong | gnomAD v4 |
| PM2 | ≤0.001% (≤0.00001) | Supporting | gnomAD v4 |

### Appendix C: Computational Predictor Thresholds

| Predictor | Pathogenic (PP3) | Benign (BP4) |
|-----------|------------------|--------------|
| REVEL (missense) | >0.7333 | ≤0.249 |
| SpliceAI (splicing) | ≥0.2 | ≤0.1 |

### Appendix D: Key PMIDs

| Topic | PMIDs |
|-------|-------|
| FATKIN domain importance | 28508083, 31740029, 31320732 |
| HEAT repeat domain importance | 10980530, 19535770, 30819809, 15054841, 22927201, 19691550, 10330348, 17124347, 8845835, 16266405, 9463314, 24090759, 22213089 |
| Most C-terminal pathogenic variant (p.R3047) | 8755918, 19691550, 18560558, 10980530, 26628246 |
| PVS1 recommendations | 30192042 |
| PS1 splicing | 36865205 |
| SpliceAI | Jaganathan et al., 2019 |
| SpliceAI thresholds | Walker et al., 2023 |
| Co-segregation caution in low-penetrance genes | 32773770 |
| PP5/BP6 not recommended | 29543229 |
| ATM kinase assays | 18634022, 19431188, 11805335 |

---

## Version History

| Version | Date | Notes |
|---------|------|-------|
| 1.5.0 | 11/7/2025 | Uploaded supporting documents by individual codes (PVS1, PS1, PS3/BS3, PM3/BP2) instead of one packet. Moved notes from old packet to CSPEC for PS3 instructions. No changes to any specifications. |

---

*This document was compiled from ClinGen VCEP specifications. For the most current version, please refer to the ClinGen website: https://www.clinicalgenome.org/affiliation/50039/docs/assertion-criteria*
