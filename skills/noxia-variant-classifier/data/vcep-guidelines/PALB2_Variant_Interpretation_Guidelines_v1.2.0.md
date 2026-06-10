# ClinGen Hereditary Breast, Ovarian and Pancreatic Cancer VCEP Variant Interpretation Guidelines for PALB2

**Version:** 1.2.0
**Released:** 7/14/2025
**Affiliation:** Hereditary Breast, Ovarian and Pancreatic Cancer VCEP
**Based on:** Richards et al., 2015 ACMG/AMP Guidelines

---

## Gene Information

| Attribute | Value |
|-----------|-------|
| **Gene** | PALB2 (HGNC:26144) |
| **HGNC Name** | partner and localizer of BRCA2 |
| **Transcript** | NM_024675.3 / ENST00000261584.8 |
| **Disease (AD)** | PALB2-related cancer predisposition (MONDO:0700272) |
| **Inheritance (AD)** | Autosomal dominant inheritance |
| **Disease (AR)** | Fanconi anemia complementation group N (MONDO:0012565) |
| **Inheritance (AR)** | Autosomal recessive inheritance |

---

## Table of Contents

1. [Pathogenic Criteria](#pathogenic-criteria)
   - [PVS1 - Null Variant](#pvs1---null-variant)
   - [PS1 - Same Amino Acid / Splice Change](#ps1---same-amino-acid--splice-change)
   - [PS2 - De Novo (Confirmed)](#ps2---de-novo-confirmed)
   - [PS3 - Functional Studies](#ps3---functional-studies)
   - [PS4 - Prevalence in Affected](#ps4---prevalence-in-affected)
   - [PM1 - Mutational Hot Spot](#pm1---mutational-hot-spot)
   - [PM2 - Absent from Controls](#pm2---absent-from-controls)
   - [PM3 - In Trans with Pathogenic (Fanconi Anemia)](#pm3---in-trans-with-pathogenic-fanconi-anemia)
   - [PM4 - Protein Length Changes](#pm4---protein-length-changes)
   - [PM5 - Novel Variant at Known Pathogenic Position](#pm5---novel-variant-at-known-pathogenic-position)
   - [PM6 - De Novo (Assumed)](#pm6---de-novo-assumed)
   - [PP1 - Co-segregation](#pp1---co-segregation)
   - [PP2 - Missense in Constrained Gene](#pp2---missense-in-constrained-gene)
   - [PP3 - Computational Evidence](#pp3---computational-evidence)
   - [PP4 - Phenotype Specificity](#pp4---phenotype-specificity)
   - [PP5 - Reputable Source](#pp5---reputable-source)
2. [Benign Criteria](#benign-criteria)
   - [BA1 - Allele Frequency >0.1%](#ba1---allele-frequency-01)
   - [BS1 - Frequency Greater Than Expected](#bs1---frequency-greater-than-expected)
   - [BS2 - Observed in Healthy Adult (Fanconi Anemia)](#bs2---observed-in-healthy-adult-fanconi-anemia)
   - [BS3 - Functional Studies (No Effect)](#bs3---functional-studies-no-effect)
   - [BS4 - Lack of Segregation](#bs4---lack-of-segregation)
   - [BP1-BP7 - Benign Supporting](#bp1-bp7---benign-supporting)
3. [Rules for Combining Criteria](#rules-for-combining-criteria)
4. [Appendices](#appendices)

---

## Pathogenic Criteria

### PVS1 - Null Variant

**Original ACMG Summary:** Null variant (nonsense, frameshift, canonical +/−1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.

**Caveats:**
- Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7).
- Use caution interpreting LOF variants at the extreme 3' end of a gene.
- Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact.
- Use caution in the presence of multiple transcripts.

**VCEP Specifications:**

- Use PALB2 PVS1 Decision Tree per PALB2 Exon Map and PALB2 PVS1 Guide
- **PVS1:** Predicted splice defect
- **PVS1_Variable(RNA):** Observed splice defect
- The default RefSeq transcript for nucleotide (c.) annotation is NM_024675.3/ENST00000261584.8. Several naturally occurring alternate splicing isoforms have been described (Lopez-Perolio 2019, PMID: 30890586). Yet, after careful examination, none of them is considered a candidate rescue transcript (very low contribution to overall expression, not coding proteins predicted functional, or both). All presumed LoF events (PVS1 decision tree specifications) occur in biologically relevant transcript(s).
- **WD40 beta propeller** and the **Coiled-coil domain (CC)** are considered indispensable for PALB2 protein function.
  - PVS1 alterations that are predicted to escape NMD, but that adversely affect the WD40 domain can be granted **PVS1** (as opposed to PVS1_Strong as the recommended baseline; Tayoun 2018, PMID: 30192042). Evidence supporting this strength change:
    - The WD40 domain interacts with many different protein partners involved in the double strand break repair pathway (Ducy 2019, PMID: 30638972)
    - Two different C-terminal truncating mutations (c.3549C>A and c.3549C>G) resulting in loss of the last 3 amino acids [p.(Tyr1183Ter)], were identified in trans with PALB2 stop-gain variants in three unrelated FA (FA-N) patients (Reid 2007, PMID: 17200671)
    - The PALB2 WD40 toroidal structure is "sealed" in the seventh blade by interaction of the C-terminal strand with the incomplete N-terminal blade. The last four residues of PALB2 (Y1183, H1184, Y1185, and S1186) are directly involved in this interaction (molecular Velcro hydrogen bonding) (Oliver 2017, PMID: 28673926). This is the rationale for the clinical relevance of the last 4 amino acids of the protein.
  - Alterations predicted to lead to in-frame losses adversely affecting the WD40 structure/function are found in trans with LoF PALB2 alterations in Fanconi Anemia patients (Reid 2007, PMID: 17200671):
    - Exon 10 donor: c.3113+5G>C (biallelic with c.395delT)
    - Exon 12 donor: c.3350+4A>G (biallelic with c.2393_2394insCT)
  - LoF alterations are rare in gnomAD in all exons (gnomAD v2.1, accessed 5/30/2019):
    - Total Variants (includes splice acceptor/donor-conservative): 1418 variants, 336,349 carriers
    - LoF Flag (excludes splice acceptor/donor-conservative): 95 variants (6.7%), 239 carriers (0.07%)

**PVS1_Variable(RNA) Guidance:**

PVS1_Variable(RNA) shall be used for observed splice defects, whether from canonical +/-1,2 positions or other spliceogenic regions (including mid-exonic missense/synonymous variants that cause splice defects) with baseline weight as per the PVS1 decision tree. Weight can be further modified based on the quality of the RNA study including consideration of:

- **Starting material** (patient material is preferable to in vitro minigene)
- **Use of NMD inhibitors** where translation does occur such as cell lines (Thermann 1998 PMID: 9628884, Carter 1995 PMID: 7499432)
- **Primer design** (comprehensive to capture possible multicassette events)
- **Method of quantification:**
  - Capillary electrophoresis is preferable to estimation by gel band density
  - SNP analysis is most preferred (analysis of exonic SNPs and their relative presence in aberrant and WT transcripts is informative)
- **Quantification** (complete effects should have increased weight over incomplete effects)

> **Important:** In the event that RNA data are available and they reflect a substantial variant-specific impact, do not use both PVS1(RNA) and PP3 or BP4. However, in the event that RNA data are available and they reflect no variant-specific impacts, PP3 or BP4 may be applied in conjunction with BP7(RNA).

#### Strength Levels

| Strength | Criteria |
|----------|----------|
| **Very Strong** | Use PALB2 PVS1 Decision Tree |
| **Strong** | Use PALB2 PVS1 Decision Tree |
| **Moderate** | Use PALB2 PVS1 Decision Tree |
| **Supporting** | Use PALB2 PVS1 Decision Tree |

**Modification Type:** Gene-specific, Strength

---

### PS1 - Same Amino Acid / Splice Change

**Original ACMG Summary:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.

**Caveat:** Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:**

- **Missense:** Do not use. Missense changes are not yet confirmed as a mechanism of disease for PALB2.
- **Splicing:** Use PALB2 PS1 Splicing Table for splicing variants with similar predictions or observations of splice defect (PMID: 37352859 / 36865205).

| Strength | Criteria |
|----------|----------|
| **Strong** | Use PALB2 PS1 Splicing table |
| **Moderate** | Use PALB2 PS1 Splicing table |
| **Supporting** | Use PALB2 PS1 Splicing table |

**Modification Type:** General recommendation

---

### PS2 - De Novo (Confirmed)

**Original ACMG Summary:** De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.

***Not Applicable***

**Comments:**
- **Autosomal Dominant Disease:** Do not use. Informative de novo occurrences have not yet been observed for autosomal dominant disease. As breast cancer is relatively common and occurs frequently as an apparently sporadic event, de novo is unlikely to ever be informative unless specific features of PALB2-related cancer predisposition are identified.
- **Autosomal Recessive Disease:** Do not use. De novo occurrences are too rare to be informative at this time. In addition, in a biallelic state, de novo occurrences have an exceedingly low probability of being able to be confirmed as in trans because parental testing (and identification of one variant in each parent) is typically required without the use of long-range technologies.

---

### PS3 - Functional Studies

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.

***Not Applicable***

**Comments:**
- **Protein:** Do not use. Due to a lack of known positive controls, do not apply functional criteria at this time.
- **RNA:** Do not use as PS3. RNA functional studies shall be coded as **PVS1_Variable(RNA)**. Please see PVS1 section (above) for guidance on baseline weights and modifications of weight based on quality.

---

### PS4 - Prevalence in Affected

**Original ACMG Summary:** The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.

**VCEP Specifications:**

- **PS4_Moderate:** Do not use. Proband counting for genes causing a common disorder need to be calibrated in a population-specific way before use.

| Strength | Criteria |
|----------|----------|
| **Strong** | Case-control studies; p-value ≤0.05 AND (Odds ratio, hazard ratio, or relative risk ≥3 OR lower 95% CI ≥1.5) |

**Modification Type:** Disease-specific

---

### PM1 - Mutational Hot Spot

**Original ACMG Summary:** Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.

***Not Applicable***

**Comments:** Do not use. Missense pathogenic variation in PALB2 is not yet confirmed as a mechanism of disease.

---

### PM2 - Absent from Controls

**Original ACMG Summary:** Absent from controls (or at extremely low frequency if recessive) in population databases.

**VCEP Specification (Supporting only):**

- Frequency ≤ 1/300,000 (**0.000333%**) in gnomAD v4 dataset
- **EXCEPTION:** under-represented sub-populations with n=1 but frequency >0.0003%
- There must be sufficient coverage at the locus (>30X, PMID: 33600021)
- Is not considered a conflicting piece of evidence for variants that otherwise are likely benign/benign
- Use as **PM2_Supporting** (not moderate)

**Modification Type:** Gene-specific, Strength

---

### PM3 - In Trans with Pathogenic (Fanconi Anemia)

**Original ACMG Summary:** For recessive disorders, detected in trans with a pathogenic variant.

**VCEP Specifications:**

See **Fanconi Anemia PM3 tables** for approach to assign points per proband, and final PM3 code assignment based on the sum of PM3-related points.

Fanconi Anemia (FA) of any subtype is generally considered an exceedingly rare, severe, early-onset disease with variable features. In the case of BRCA2, hypomorphic FA patients have been described who are diagnosed at older ages with less severe phenotypes. The criteria set forth in the tables below are designed to accommodate such hypomorphs and are recommended to be applied to all FA-associated genes which may not be as well described due to the extreme infrequency of their identification, and due to ascertainment bias (for severe phenotype) in the literature.

#### General Considerations

- Variant may not exceed general population frequency >0.01%.
- Consider other gene panel test results as potential explanation for phenotype.
- Multiple unrelated cases are additive.

#### Phenotype Consistent Definition

- Chromosomal breakage with 1 clinical feature, **OR**
  - Ex: Chromosomal breakage testing + microcephaly / triangular face
- At least 2 of 3 clinical features from separate categories without chromosomal breakage studies
  - Ex (without chromosomal breakage): Myelodysplastic Syndrome and microcephaly / triangular face

#### Positive for Chromosome Breakage Test

- Increased chromosome breakage and/or radial forms on cytogenetic testing of lymphocytes with diepoxybutane (DEB) or mitomycin C (MMC)

#### Clinical Features Indicative of FA

**Physical features** (in ~75% of affected persons):
- Prenatal and/or postnatal short stature
- Abnormal skin pigmentation (e.g., cafe au lait macules, hypo-pigmentation)
- Skeletal malformations (e.g., hypoplastic thumb, hypoplastic radius)
- Microcephaly, triangular face
- Ophthalmic anomalies
- Genitourinary tract anomalies
- See Orphanet for full list of >100 HPO terms (and their reported frequency)

**Pathology findings and laboratory findings** (non-cancer related):
- Progressive bone marrow failure (unrelated to cancer treatment)
- Aplastic anemia
- Myelodysplastic syndrome
- Inordinate toxicities from chemotherapy or radiation
- Macrocytosis
- Cytopenia (especially thrombocytopenia, leukopenia, and neutropenia)
- Increased fetal hemoglobin (often precedes anemia)

> **Note:** FA patients with very early onset cancer (≤5yr) may not present with hematologic disease, which is reported to have median age at onset of 7 years in FA patients in general (Ebens 2017, PMID: 27929686).

**Cancer diagnosis ≤5yr**, particularly:
- Blood cancers (AML)
- Brain cancers (medulloblastoma, neuroblastoma)
- Wilms Tumor

Specifications are adapted from definitions from GeneReviews (last revision June 3, 2021).

#### PM3 Evidence Strength Thresholds

| Total Points | Strength Level |
|--------------|----------------|
| 1 | PM3_Supporting |
| 2 | PM3 (Moderate) |
| ≥4 | PM3_Strong |
| ≥8 | PM3_VeryStrong |

**Modification Type:** Disease-specific, Strength

---

### PM4 - Protein Length Changes

**Original ACMG Summary:** Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

***Not Applicable***

**Comments:**
- **In-frame deletions/insertions** that are not already PVS1-eligible: Do not use. No information is available to justify the application of this rule. Missense and small in-frame indels are not yet confirmed as a mechanism of disease for PALB2.
- **Stop-loss:** Do not use due to lack of data on stop-loss variants.

---

### PM5 - Novel Variant at Known Pathogenic Position

**Original ACMG Summary:** Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.

**VCEP Specifications:**

- Based on location of the most C-terminal known pathogenic variant, **p.Tyr1183\***.
- Use as **PM5_Supporting** (not moderate)
- **Do not use for missense changes:** Missense changes are not yet confirmed as a mechanism of disease for PALB2.

| Strength | Criteria |
|----------|----------|
| **Supporting** | Apply to frameshifting or truncating variants with premature termination codons upstream of p.Tyr1183. Apply to splice variants with premature termination codons upstream of p.Tyr1183 where PVS1_VS(RNA) is applied based on high quality observed splicing impact and must be NMD prone. |

**Modification Type:** Gene-specific, Strength

---

### PM6 - De Novo (Assumed)

**Original ACMG Summary:** Assumed de novo, but without confirmation of paternity and maternity.

***Not Applicable***

**Comments:** Do not use for AD or AR disease. Informative de novo occurrences have not yet been observed and de novo AR conditions are unlikely to be informed by phase. See PS2 for justification.

---

### PP1 - Co-segregation

**Original ACMG Summary:** Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.

**VCEP Specifications:**

#### Autosomal Dominant Condition

Quantitative co-segregation analysis is mandated for more accurate assessment of causality for PALB2 alterations. It is strongly preferred that biocurators use a quantitative method that accommodates both pathologies of AD PALB2: breast cancer, ovarian cancer and pancreatic cancer. These methods may be conducted by biostatisticians, particularly if they are able to compute LR scores using multiple phenotypes (Tavtigian 2018, PMID: 29300386).

| Strength | LOD Score | Bayes Factor (LR) |
|----------|-----------|--------------------|
| **PP1_Very Strong** | ≥2.54 | ≥350:1 |
| **PP1_Strong** | ≥1.26 | ≥18:1 |
| **PP1_Moderate** | ≥0.60 | ≥4:1 |
| **PP1 (Supporting)** | ≥0.3 | ≥2:1 |
| **BS4_Supporting** | ≤-0.32 | ≤0.48 |
| **BS4_Moderate** | ≤-0.64 | ≤0.23 |
| **BS4 (Strong)** | ≤-1.28 | ≤0.053:1 |

**COOL Tool:** A freely available tool, COOL (COsegregation OnLine) from Bing-Jian Feng's laboratory can be used to calculate LoD scores for co-segregation analysis:
1. Navigate to COOL (COsegregation OnLine) at https://fengbj-laboratory.org/cool2/server.uu.html
2. Input 'PALB2' into the 'Input a Gene Symbol' field (the PALB2 defaults are approved by this VCEP)
3. Upload your Pedigree File (see https://fengbj-laboratory.org/cool2/manual.html for formatting)
4. Leave all defaults as is. Select 'Submit' to obtain LR based on Full Likelihood Bayes (FLB)

#### Autosomal Recessive Condition

Affected relatives must have both variants identified in proband.

| Strength | Criteria |
|----------|----------|
| **PP1_Strong** | Segregation in ≥3 affected relatives |
| **PP1_Moderate** | Segregation in 2 affected relatives |
| **PP1 (Supporting)** | Segregation in 1 affected relative |

**Modification Type:** Gene-specific

---

### PP2 - Missense in Constrained Gene

**Original ACMG Summary:** Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.

***Not Applicable***

**Comments:** Do not use. Missense is not yet confirmed or refuted as a mechanism of disease for PALB2.

---

### PP3 - Computational Evidence

**Original ACMG Summary:** Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).

**VCEP Specifications:**

- **Missense:** Do not use. So far, published predictors have yet to achieve functional outcome for PALB2 missense variants.
- **Splicing:** Predicted impact via splicing (**SpliceAI ≥0.2**) for silent, missense/in-frame and for intronic variants outside of donor and acceptor 1,2 sites.

**Important Notes:**
- Splice analysis needs to be considered for all variant types (including missense, frameshift, nonsense, etc. as any variant has the potential to impact splicing which may preclude any expected protein effects)
- PP3 for splice predictions may **not** be applied in addition to PVS1 or PVS1_Variable(RNA) codes
- Use caution in applying the wrong type of computational evidence (protein vs. RNA) towards the cumulative body of evidence for the opposite mechanism
- The VCEP uses **SpliceAI** as a sole predictor due to its ability to accurately predict loss of native splice sites and creation of cryptic sites (Jaganathan et al., 2019). This VCEP recommends SpliceAI thresholds set forth by the SVI (Walker et al., 2023):
  - Apply **PP3** for SpliceAI scores **≥0.2**
  - Apply **BP4** for SpliceAI scores **≤0.1**

> **RNA Data Note:** In the event that RNA data are available and they reflect a substantial variant-specific impact, do not use both PVS1(RNA) and PP3 or BP4. However, in the event that RNA data are available and they reflect no variant-specific impacts, PP3 or BP4 may be applied in conjunction with BP7(RNA).

| Strength | Criteria |
|----------|----------|
| **Supporting** | Splicing: Predicted impact via splicing (SpliceAI ≥0.2) for silent, missense/in-frame and for intronic variants outside of donor and acceptor 1,2 sites. Missense: Do not use. |

**Modification Type:** General recommendation (RNA), Gene-specific (protein)

---

### PP4 - Phenotype Specificity

**Original ACMG Summary:** Patient's phenotype or family history is highly specific for a disease with a single genetic etiology.

***Not Applicable***

**Comments:**
- **Autosomal Dominant:** Do not use as breast cancer is a disease with multiple genetic etiology (genetic heterogeneity) and there are no features that can readily distinguish hereditary from sporadic causes.
- **Autosomal Recessive:** Do not use as a separate line of evidence. Such evidence is built into the Fanconi Anemia PM3/BS2 table.

---

### PP5 - Reputable Source

**Original ACMG Summary:** Reputable source recently reports variant as pathogenic, but the evidence is not available to the laboratory to perform an independent evaluation.

***Not Applicable***

This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PMID: 29543229).

---

## Benign Criteria

### BA1 - Allele Frequency >0.1%

**Original ACMG Summary:** Allele frequency is above 5% in population databases.

**VCEP Specification (Stand Alone):**
- Grpmax Filtering AF **>0.1%** in gnomAD v4 dataset
- Follow all SVI general guidance on applying population filters

**Derivation:** Rounded from 0.118% using Whiffin calculator:
- Prevalence (breast cancer): 1:8
- Allelic Heterogeneity: 1
- Genetic Heterogeneity: 0.01
- Penetrance: 0.53

**Modification Type:** Disease-specific, Gene-specific

---

### BS1 - Frequency Greater Than Expected

**Original ACMG Summary:** Allele frequency is greater than expected for disorder.

**VCEP Specification (Strong):**
- Grpmax Filtering AF **>0.01%** in gnomAD v4 dataset
- Follow all SVI general guidance on applying population filters

**Derivation:** Rounded from 0.0118% using Whiffin calculator:
- Prevalence (breast cancer): 1:8
- Allelic Heterogeneity: 0.1
- Genetic Heterogeneity: 0.01
- Penetrance: 0.53

**Modification Type:** Disease-specific, Gene-specific

---

### BS2 - Observed in Healthy Adult (Fanconi Anemia)

**Original ACMG Summary:** Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

**VCEP Specifications:**

See **Fanconi Anemia BS2 tables** for approach to assign points per proband, and final BS2 code assignment based on the sum of BS2-related points.

- Do not use for individuals in population-based cohorts, such as gnomAD
- VUA (Variant Under Assessment) should not be bioinformatically predicted (or experimentally proven) to have a clinically important effect on protein or mRNA splicing. Co-occurrent P or LP variant should be assigned classification using VCEP specifications.
- Consider multiple instances of co-occurrence with the same variant are more likely to be in cis in unrelated individuals when assessing BS2 application

#### BS2 Evidence Strength Thresholds

| Total Points | Strength Level |
|--------------|----------------|
| 1 | BS2_Supporting |
| 2 | BS2_Moderate |
| ≥4 | BS2 (Strong) |

**Modification Type:** Disease-specific

---

### BS3 - Functional Studies (No Effect)

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

***Not Applicable***

**Comments:**
- **Protein functional studies (BS3):** Do not use. See PS3 for details.
- **RNA functional studies:** Do not use as BS3. Use **BP7_Variable(RNA)** instead.

---

### BS4 - Lack of Segregation

**Original ACMG Summary:** Lack of segregation in affected members of a family.

**VCEP Specifications:**

Quantitative co-segregation analysis is mandated for more accurate assessment of causality for PALB2 alterations. Use the same framework as PP1 (see PP1 section above).

#### AD Condition

| Strength | LOD Score | Bayes Factor (LR) |
|----------|-----------|--------------------|
| **BS4_Supporting** | ≤-0.32 | ≤0.48 |
| **BS4_Moderate** | ≤-0.64 | ≤0.23 |
| **BS4 (Strong)** | ≤-1.28 | ≤0.053:1 |

#### AR Condition

Informative instances of co-segregation in FANCN families are too rare to be considered for weight at this time and can also be considered for BS2 if biallelic unaffected patients are observed in a Fanconi Anemia family.

**Modification Type:** Gene-specific

---

### BP1-BP7 - Benign Supporting

| Criterion | Status | Specification |
|-----------|--------|---------------|
| **BP1** | **Applicable** | Apply to all missense variants. Based on published and unpublished functional studies, PALB2 has a low rate of missense variants that are non-functional in relevant assays. True missense pathogenic variants are not yet confirmed or refuted but are thought to be exceedingly rare. |
| **BP2** | **Not Applicable** | Do not use. See Fanconi Anemia BS2 table. |
| **BP3** | **Not Applicable** | Do not use. Small in-frame losses are neither confirmed nor refuted as a mechanism of pathogenicity for PALB2. PALB2 is not considered to have repetitive regions without known function. |
| **BP4** | **Applicable (Splicing only)** | Missense: Do not use. Splicing: No predicted impact via splicing (**SpliceAI ≤0.1**). Do not apply for missense variants. BP4 for splice predictions may not be applied in conjunction with BP7_Variable(RNA). |
| **BP5** | **Not Applicable** | Do not use. Cases with multiple pathogenic variants have been observed with no noticeable difference in phenotype (e.g. BRCA1 and BRCA2). PALB2 has moderate penetrance and will naturally occur with other pathogenic variants more frequently. |
| **BP6** | **Not Applicable** | Discontinued by ACMG/AMP. Not for use as recommended by ClinGen SVI VCEP Review Committee (PMID: 29543229). |
| **BP7 / BP7_Variable(RNA)** | **Applicable** | See below for detailed specifications. |

#### BP7 Detailed Specifications

**BP7: Synonymous and Deep Intronic**
- Can be used for deep intronic variants beyond (but not including) +7 (donor) and -21 (acceptor)
- May also apply BP4 to achieve Likely Benign
- Is not considered a conflicting piece of evidence against a body of evidence supporting a pathogenic splice defect

**BP7_Variable(RNA): RNA Functional Studies**
- Lack of aberrant splice defect: Please see PVS1_Variable(RNA) section (above) for guidance on baseline weights and modifications of weight based on quality for RNA assays
- BP4 splice predictions may **not** be used in conjunction with BP7_Variable(RNA)

> **RNA Data Note:** In the event that RNA data are available and they reflect a substantial variant-specific impact, do not use both PVS1(RNA) and PP3 or BP4. However, in the event that RNA data are available and they reflect no variant-specific impacts, PP3 or BP4 may be applied in conjunction with BP7(RNA).

| Strength | Criteria |
|----------|----------|
| **Strong** | BP7_Strong(RNA): Observed lack of aberrant RNA defect for silent substitutions and intronic variants. Variable weight applied depending on curator discretion of assay quality. |
| **Moderate** | BP7_Moderate(RNA): Observed lack of aberrant RNA defect for silent substitutions and intronic variants. Variable weight applied depending on curator discretion of assay quality. |
| **Supporting** | BP7: Use for synonymous and deep intronic variants defined as further than (but not including) +7 and further than (but not including) -21 at donor and acceptor sites, respectively. BP7(RNA): Observed lack of aberrant RNA defect for silent substitutions and intronic variants. Variable weight applied depending on curator discretion of assay quality. |

**Modification Type:** General recommendation

---

## Rules for Combining Criteria

### Pathogenic Classification

| Criteria Combination |
|---------------------|
| 1 Very Strong (PVS1, PVS1_Variable[RNA], PM3_VeryStrong) **AND** ≥1 Strong (PS1-PS4, PM3_Strong, PP1_Strong) |
| 1 Very Strong **AND** ≥2 Moderate (PM3, PM5, PS1_Moderate, PP1_Moderate) |
| 1 Very Strong **AND** 1 Moderate **AND** 1 Supporting (PP1-PP3, PM2_Supporting, PM3_Supporting, PM5_Supporting) |
| 1 Very Strong **AND** ≥2 Supporting |
| ≥2 Strong (PS1-PS4, PM3_Strong, PP1_Strong) |
| 1 Strong **AND** ≥3 Moderate |
| 1 Strong **AND** 2 Moderate **AND** ≥2 Supporting |
| 1 Strong **AND** 1 Moderate **AND** ≥4 Supporting |

### Likely Pathogenic Classification

| Criteria Combination |
|---------------------|
| 1 Very Strong (PVS1, PVS1_Variable[RNA], PM3_VeryStrong) **AND** 1 Moderate |
| 1 Very Strong (PVS1) **AND** 1 Supporting (PVS1_Supporting, PS1_Supporting, PM2_Supporting, PM3_Supporting, PM5_Supporting, PP1, PP3) |
| 1 Strong **AND** 1 Moderate |
| 1 Strong **AND** ≥2 Supporting |
| ≥3 Moderate |
| 2 Moderate **AND** ≥2 Supporting |
| 1 Moderate **AND** ≥4 Supporting |

### Benign Classification

| Criteria Combination |
|---------------------|
| 1 Stand Alone (BA1) |
| ≥2 Strong (BS1-BS4) |

### Likely Benign Classification

| Criteria Combination |
|---------------------|
| 1 Strong (BS1, BS2, BS4, BP7_Strong) **AND** 1 Supporting |
| ≥2 Supporting (BP1-BP7, BP7_Supporting[RNA]) |
| 1 Strong (BS1, BS2, BS4, BP7_Strong) |

---

## Appendices

### Appendix A: PVS1 Decision Tree Notes

The PALB2 PVS1/PVS1_Variable(RNA) Guide is adapted from PMID: 30192042 (Tayoun et al., 2018) with the following PALB2-specific modifications:

1. PVS1 decision tree introduces some code strength modifications (upgrades and downgrades), and instances not addressed by Tayoun et al.: (i) GT-AG variants not affecting coding exons, (ii) +2T>C variants predicted to create de novo functional GC sites, (iii) +2C>T variants targeting native GC sites, and (iv) considering the relevance of the protein domain targeted by ≥1 exon duplications.

2. NM_024675.3 is the clinically relevant reference transcript (13 exons, 13 coding exons, start codon in exon 1, encoding a 1186aa protein — UniProtKB Q86YC2).

3. No potential rescue transcripts are known (Lopez-Perolio et al., 2019).

4. Two clinically relevant domains: (i) **Coiled-coil (CC) domain** spanning residues 10-40 (Song et al., 2018) and (ii) **WD40 domain** spanning residues 856-1186 (Oliver et al., 2009).

5. In-frame alterations targeting the CC and WD40 domains are considered PVS1 (with exception noted below).

6. In-frame alterations targeting FATKIN are considered PVS1, the only exception being very small in-frame alterations with PROVEAN score suggesting pathogenic, which are considered PVS1_Supporting.

7. p.Tyr1183Ter is the last PTC variant known to be pathogenic (Reid et al., 2007).

8. p.Tyr1183Ter pathogenicity suggests the last four residues (YHYS) are critical for PALB2 function, supported by structural considerations (Oliver et al., 2009).

#### PVS1 Decision Tree Footnotes

| Note | Description |
|------|-------------|
| **A** | Variants introducing stop gains upstream of His1184 are considered PVS1 regardless of NMD status. Two different C-terminal truncating mutations (c.3549C>A, c.3549C>G) introducing p.(Tyr1183Ter) were identified in trans with PALB2 stop-gain variants in three unrelated FA-N patients. |
| **B** | Variants preserving 1-3 residues at C-terminal YHYS end: role of deleted residues is not necessarily critical; <10% protein removed qualifies for moderate. |
| **C** | Variants encoding proteins with alternative C-terminal ends: expected unable to recapitulate molecular Velcro interaction, but cannot exclude partial mimicry. |
| **D** | As per B, but variants code additional residues; cannot exclude alternative C-terminal end mimicking YHYS role. |
| **E** | Exon 6 codes for WD40 beta-strand 7D critical for WD40 toroidal folding, but exon 6 deletion might be hypomorphic (Byrd et al., 2016). |
| **F** | Predicted damaging to CC (exon 2) or WD40 (exons 6-13) domains if ≥1 coding exon skipped. |
| **G** | Exon 2 acceptor site: predicted/observed outcome delta(E2p6) skips p.(Leu17_Lys18del). p.Lys18Arg has no HR impact; p.Leu17Pro shows >50% reduced HR but not considered formal proof of criticality. |
| **H** | Exon 3 donor site: predicted/observed outcome introduces 17 novel residues. Supporting strength based on PROVEAN score -15.84. |

### Appendix B: PALB2 Key Domains

| Domain | Residues | Functional Significance |
|--------|----------|------------------------|
| **Coiled-coil (CC)** | 10-40 | BRCA1 binding domain |
| **FATKIN** | (between CC and WD40) | Intermediate region |
| **WD40 beta propeller** | 856-1186 | BRCA2 and RAD51 binding domain |
| **C-terminal YHYS** | 1183-1186 (Y1183, H1184, Y1185, S1186) | Critical for WD40 toroidal sealing (molecular Velcro) |

### Appendix C: Population Frequency Thresholds Summary

| Criterion | Threshold | Strength | Database |
|-----------|-----------|----------|----------|
| BA1 | >0.1% | Stand Alone | gnomAD v4 Grpmax Filtering AF |
| BS1 | >0.01% | Strong | gnomAD v4 Grpmax Filtering AF |
| PM2 | ≤0.000333% (1/300,000) | Supporting | gnomAD v4 |

### Appendix D: Reference PMIDs

| PMID | Citation |
|------|----------|
| 30890586 | Lopez-Perolio I, Leman R et al. Alternative splicing and ACMG-AMP-2015-based classification of PALB2 genetic variants: an ENIGMA report. *J Med Genet* (2019) 56(7):453-460. |
| 30192042 | Abou Tayoun AN, Pesaran T et al. Recommendations for interpreting the loss of function PVS1 ACMG/AMP variant criterion. *Hum Mutat* (2018) 39(11):1517-1524. |
| 30638972 | Ducy M, Sesma-Sanz L et al. The Tumor Suppressor PALB2: Inside Out. *Trends Biochem Sci* (2019) 44(3):226-240. |
| 17200671 | Reid S, Schindler D et al. Biallelic mutations in PALB2 cause Fanconi anemia subtype FA-N and predispose to childhood cancer. *Nat Genet* (2007) 39(2):162-4. |
| 9628884 | Thermann R, Neu-Yilik G et al. Binary specification of nonsense codons by splicing and cytoplasmic translation. *EMBO J* (1998) 17(12):3484-94. |
| 7499432 | Carter MS, Doskow J et al. A regulatory mechanism that detects premature nonsense codons in T-cell receptor transcripts in vivo is reversed by protein synthesis inhibitors in vitro. *J Biol Chem* (1995) 270(48):28995-9003. |
| 29300386 | Tavtigian SV, Greenblatt MS et al. Modeling the ACMG/AMP variant classification guidelines as a Bayesian classification framework. *Genet Med* (2018) 20(9):1054-1060. |
| 27929686 | Ebens CL, MacMillan ML et al. Hematopoietic cell transplantation in Fanconi anemia: current evidence, challenges and recommendations. *Expert Rev Hematol* (2017) 10(1):81-97. |
| 28673926 | Oliver AW, Swift S et al. Structural basis for recruitment of BRCA2 by PALB2. *EMBO Rep* (2017) 18(7):1264. |
| 29543229 | ClinGen SVI VCEP Review Committee — Recommendation to discontinue PP5/BP6. |
| 37352859 | PALB2 PS1 Splicing table reference. |
| 36865205 | PALB2 PS1 Splicing table reference. |

---

## Version History

| Version | Date | Notes |
|---------|------|-------|
| 1.2.0 | 7/14/2025 | Provided % for PM2 and clarified use of gnomAD v4. Clarified when to assume in trans for PM3. Provided PP1 guidance for AR condition. Added SpliceAI thresholds for PP3 and BP4. Clarified use of PP3/BP4 in the presence of RNA data. Updated MONDO from hereditary breast carcinoma and familial pancreatic carcinoma to PALB2-related cancer predisposition. PVS1 clarification for last nucleotide of exon. Minor formatting adjustments. |

---

*This document was compiled from ClinGen HBOP VCEP specifications for PALB2 (Version 1.2.0). For the most current version, please refer to the ClinGen website.*
