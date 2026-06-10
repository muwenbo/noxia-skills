# ClinGen Severe Combined Immunodeficiency Disease VCEP Variant Interpretation Guidelines for JAK3

**Version:** 2.1.0
**Released:** 10/1/2025
**Affiliation:** Severe Combined Immunodeficiency Disease VCEP
**Based on:** Richards et al., 2015 ACMG/AMP Guidelines

---

## Gene Information

| Attribute | Value |
|-----------|-------|
| **Gene** | JAK3 (HGNC:6193) |
| **HGNC Name** | Janus kinase 3 |
| **Transcript** | NM_000215.4 |
| **Disease** | T-B+ severe combined immunodeficiency due to JAK3 deficiency (MONDO:0010938) |
| **Inheritance** | Autosomal recessive inheritance |

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

**Original ACMG Summary:** Null variant (nonsense, frameshift, canonical ±1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.

**Caveats:**
- Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7)
- Use caution interpreting LOF variants at the extreme 3' end of a gene
- Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact
- Use caution in the presence of multiple transcripts

**VCEP Specifications:** See attached PVS1 flowchart (Appendix A).

#### Strength Levels

| Strength | Criteria |
|----------|----------|
| **Very Strong (PVS1)** | Use ClinGen SVI recommendations for loss of function criterion (Tayoun et al., 2018 (PMID: 30192042)) |
| **Strong (PVS1_Strong)** | Use ClinGen SVI recommendations with specification: For variants not predicted to undergo NMD but removing >10% of protein (i.e., variants in the last exon, exon 24, or variants in the last 50 nucleotides of the penultimate exon after c.3157, codon 1053, in exon 23), at least one pathogenic variant **must be** present downstream to apply PVS1_Strong |
| **Moderate (PVS1_Moderate)** | Use ClinGen SVI recommendations with specification: For variants not predicted to undergo NMD but removing >10% of protein (i.e., variants in the last exon, exon 24, or variants in the last 50 nucleotides of the penultimate exon after c.3157, codon 1053, in exon 23), when at least one pathogenic variant is **not** present downstream, downgrade to PVS1_Moderate |
| **Supporting (PVS1_Supporting)** | Per PVS1 flowchart for initiation codon variants with no pathogenic variants upstream of closest potential in-frame start codon |

#### PVS1 Decision Tree Summary

**Nonsense or Frameshift:**
- Predicted to undergo NMD + exon present in biologically-relevant transcripts → **PVS1**
- Not predicted to undergo NMD (last exon or last 50nt of penultimate exon):
  - Variant removes >10% protein + 1+ pathogenic variant downstream → **PVS1_Strong**
  - Variant removes >10% protein + no downstream pathogenic variants → **PVS1_Moderate**
  - Variant removes <10% protein → **PVS1_Moderate**

**Canonical Splice Sites (GT-AG ±1,2):**
- Exon skipping disrupts reading frame + predicted NMD + exon present → **PVS1**
- Exon skipping disrupts reading frame + NOT predicted NMD:
  - Variant removes >10% protein + 1+ pathogenic variant downstream → **PVS1_Strong**
  - Variant removes >10% protein + no downstream pathogenic variants → **PVS1_Moderate**
- Exon skipping preserves reading frame:
  - Truncated region critical to protein function → **PVS1_Strong**
  - Role unknown + removes >10% + pathogenic variant in deleted region → **PVS1_Strong**
  - Role unknown + removes >10% + no pathogenic variants in deleted region → **PVS1_Moderate**

**Deletions:**
- Full gene deletion → **PVS1**
- Single/multi exon deletion disrupts reading frame + NMD predicted + exon present → **PVS1**
- Single/multi exon deletion preserves reading frame follows same logic as splice variants

**Duplications:**
- Proven in tandem + reading frame disrupted + NMD predicted → **PVS1**
- Presumed in tandem + reading frame presumed disrupted + NMD predicted → **PVS1_Strong**

**Initiation Codon:**
- No known alternative start codon + ≥1 pathogenic variants upstream → **PVS1_Moderate**
- No known alternative start codon + no pathogenic variants upstream → **PVS1_Supporting**

---

### PS1 - Same Amino Acid Change

**Original ACMG Summary:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.

**Example:** Val->Leu caused by either G>C or G>T in the same codon.

**Caveat:** Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong (PS1)** | Applicable if the previously established variant is classified as **pathogenic** by SCID VCEP specifications for JAK3. Can also be applied for splice variants at the same nucleotide with similar impact prediction as previously reported pathogenic variant (if predicted impact is equal to or greater than known pathogenic variant per SpliceAI). Example: c.105+1G>C is known to be pathogenic, can use PS1 for c.105+1G>T. |
| **Moderate (PS1_Moderate)** | Applicable if the previously established variant is classified as **likely pathogenic** by SCID VCEP specifications for JAK3. Can also be applied for splice variants at the same nucleotide with similar impact prediction as previously reported likely pathogenic variant. |

---

### PS2 - De Novo (Confirmed)

**Original ACMG Summary:** De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.

**Note:** Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.

**VCEP Specifications:**

The following guidelines should be used when determining the phenotypic consistency of each proband:
- **"Phenotype highly specific for gene"**: proband must meet at least PP4_Moderate criteria
- **"Phenotype consistent with gene but not highly specific"**: proband must meet PP4 criteria
- **"Phenotype consistent with gene but not highly specific and high genetic heterogeneity"**: proband has been asserted to have a SCID phenotype but does not meet PP4 criteria
- Reduce points per proband by half if the phase is unconfirmed

#### PS2/PM6 Point System

| Phenotypic Consistency | Confirmed Parental Relationships | Unconfirmed Parental Relationships |
|------------------------|----------------------------------|-----------------------------------|
| Phenotype highly specific for gene | 2 points | 1 point |
| Phenotype consistent but not highly specific | 1 point | 0.5 points |
| Phenotype consistent + high genetic heterogeneity | 0.5 points | 0.25 points |
| Phenotype not consistent | 0 points | 0 points |

**Note:** Maximum allowable value of 1 may contribute to overall score for "Phenotype consistent + high genetic heterogeneity" category.

#### Evidence Strength Thresholds

| Points | Strength Level |
|--------|----------------|
| 0.5 | PS2_Supporting / PM6_Supporting |
| 1.0 | PS2_Moderate / PM6 |
| 2.0 | PS2 / PM6_Strong |
| 4.0 | PS2_VeryStrong / PM6_VeryStrong |

#### Additional Considerations
- **Autosomal recessive conditions:** For a de novo occurrence in a gene associated with an autosomal recessive pattern without an additional pathogenic/likely pathogenic variant identified, the strength of evidence should be decreased by one level
- **Mosaicism:** For cases with apparent germline mosaicism (multiple affected siblings with both parents negative for the variant), parental relationships must be confirmed for de novo criteria to apply

---

### PS3 - Functional Studies

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.

**Note:** Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong (PS3)** | May potentially be applied at strong level for evidence from an animal model expressing the variant of interest and recapitulating the JAK3-SCID phenotype. Animal models will be reviewed on a case-by-case basis by the VCEP to determine appropriate strength level. |
| **Supporting (PS3_Supporting)** | Can be applied based on an abnormal result in an *in vitro* kinase activity assay. Approved assay instance: Roberts et al., 2004 (PMID: 14615376). |

**Important:** At least one previously observed proband with the JAK3 variant meeting PP4 is required to apply PS3 at any strength on the basis of a cellular model/in vitro study.

#### Approved Assay Instances

| Assay | PMID | Strength | Description |
|-------|------|----------|-------------|
| In vitro kinase assay (JAK3 autophosphorylation) | 14615376 | PS3_Supporting | Clarified whole cell lysates from JAK3-negative COS-7 cells transiently transfected with wild type or variant JAK3 cDNA expression vectors were immunoprecipitated with a JAK3 C-terminus antibody, incubated with [γ-32P]ATP for 1 min or 5 min, and analyzed on an SDS-PAGE gel to assess JAK3 phosphorylation |

**Assay Details (PMID: 14615376):**
- **Author:** Roberts...Buckley (2004)
- **Material:** JAK3-negative COS-7 cells transiently transfected with wild type or variant JAK3 cDNA expression vectors
- **Readout:** Semi-quantitative - Presence/intensity of band corresponding to phosphorylated JAK3
- **Positive Control:** Wild type JAK3-transfected cells
- **Negative Control:** Vector-only transfected cells; JAK3 p.Lys855Ala (artificial catalytically inactive JAK3 variant)
- **Threshold for normal:** Wild type-like level of phosphorylated JAK3
- **Threshold for abnormal:** Absence/reduced level of phosphorylated JAK3
- **Variants Tested:** c.266_268del (p.Ala58del), c.602C>A (p.Glu169Asp), c.1860G>A (p.Gly589Ser)

---

### PS4 - Prevalence in Affected

**Original ACMG Summary:** The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.

**Note 1:** Relative risk (RR) or odds ratio (OR), as obtained from case-control studies, is >5.0 and the confidence interval around the estimate of RR or OR does not include 1.0.

**Note 2:** In instances of very rare variants where case-control studies may not reach statistical significance, the prior observation of the variant in multiple unrelated patients with the same phenotype, and its absence in controls, may be used as moderate level of evidence.

**VCEP Specification:** *Not Applicable*

---

### PM1 - Mutational Hot Spot

**Original ACMG Summary:** Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.

**VCEP Specification (Moderate):**

Defined to include missense alterations of two JH2 domain residues:
- **R651W**
- **C759R**

Reference: PMID: 11668610

---

### PM2 - Absent from Controls

**Original ACMG Summary:** Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

**Caveat:** Population data for indels may be poorly called by next generation sequencing.

**VCEP Specification (Supporting only):**

- gnomAD popmax filtering allele frequency **<0.000115**
- **Additional requirement:** No homozygotes have been observed in gnomAD

---

### PM3 - In Trans with Pathogenic

**Original ACMG Summary:** For recessive disorders, detected in trans with a pathogenic variant.

**Note:** This requires testing of parents (or offspring) to determine phase.

**VCEP Specifications:**

Use ClinGen SVI adapted recommendations for *in trans* criterion with the additional requirement that the co-occurring variant must be classified using the SCID VCEP specifications for JAK3.

**Caveat:** All variants should be sufficiently rare (meet PM2 specification). The applicability of PM3 to suspected founder variants with allele frequencies exceeding the PM2 threshold will be evaluated on a case-by-case basis by the VCEP.

#### PM3 Point System (Per Proband)

| Classification/Zygosity of Other Variant | Confirmed in Trans | Phase Unknown |
|------------------------------------------|-------------------|---------------|
| Pathogenic or Likely pathogenic variant | 1.0 | 0.5 (P) / 0.25 (LP) |
| Homozygous (non-consanguineous, no max) | 1.0 | 1.0 |
| Homozygous (consanguineous, max 0.5/family) | 0.5 | 0.5 |
| VUS (max 0.5 total) | 0.25 | 0.0 |

#### PM3 Evidence Strength Thresholds

| Total Points | Strength Level |
|--------------|----------------|
| 0.5 | PM3_Supporting |
| 1.0 | PM3 (Moderate) |
| 2.0 | PM3_Strong |
| 4.0 | PM3_VeryStrong |

#### PM3 Considerations

- **Allele Frequency:** Application of PM3 is contingent on both the variant being assessed and the variant on the other allele being sufficiently rare (meets PM2 threshold)
- **Phasing:** If phase cannot be determined, at least two different LP/P variants are needed to equal the weight of one LP/P co-occurrence confirmed in trans. If only one parent is tested and found to carry one allele, variants can be counted as in trans.
- **Classification:** To avoid circularity, the classification of the variant on the other allele should not use evidence from the variant being interrogated
- **Homozygous occurrences:** Default weight is dropped to 0.5 points as a rare homozygous occurrence may be due to consanguinity. A recommended max of 1.0 points of all homozygous cases is suggested.

---

### PM4 - Protein Length Changes

**Original ACMG Summary:** Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Moderate (PM4)** | When applied to deletion variants, the deleted region must contain a known **pathogenic or likely pathogenic** variant that is not predicted/observed to alter splicing |
| **Supporting (PM4_Supporting)** | When applied to deletion variants, the deleted region must contain a known **VUS** variant that is not predicted/observed to alter splicing |

---

### PM5 - Novel Missense at Same Residue

**Original ACMG Summary:** Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.

**Example:** Arg156His is pathogenic; now you observe Arg156Cys.

**Caveat:** Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:**

#### For Missense Variants:
| Strength | Criteria |
|----------|----------|
| **Moderate (PM5)** | Applicable at default strength if previously established variant is classified as **pathogenic** |
| **Supporting (PM5_Supporting)** | Applicable if previously established variant is classified as **likely pathogenic** |

#### For Nonsense Variants (Point-Based System):

| Strength | Criteria |
|----------|----------|
| **Strong (PM5_Strong)** | ≥4 points from informative variants. PM5_Strong should be downgraded to PM5_Moderate if PVS1 is applied at any strength. |
| **Moderate (PM5_Moderate)** | ≥2 points from informative variants. PM5_Moderate may not be combined with PVS1_VeryStrong (should be downgraded to PM5_Supporting if PVS1_VeryStrong is applied). |
| **Supporting (PM5_Supporting)** | 1 point from an informative variant |

#### PM5 Nonsense Variant Point Table

| Type of VUA | Informative Variant | Score |
|-------------|---------------------|-------|
| Nonsense predicted to lead to NMD | P/LP variant in the exon of DNA change predicted to lead to NMD | +1 pt |
| Nonsense predicted to lead to NMD | B/LB variant in the exon predicted to lead to NMD | -2 pt |
| Nonsense in final exon, not predicted to lead to NMD | P/LP variant resulting in PTC in same exon but downstream of VUA | +1 pt |
| Nonsense in final exon, not predicted to lead to NMD | B/LB variant resulting in PTC in same exon but upstream of VUA | -2 pt |

**NMD** = nonsense-mediated decay; **PTC** = premature termination codon

**Important Notes:**
- The informative variant must be classified by the SCID VCEP specifications and may not be the same variant used to meet "+1 pathogenic variant downstream" on the PVS1 flowchart
- If negative points are calculated, do not apply PM5 and reconsider if PVS1 is applicable
- The VUA must be sufficiently rare (meet PM2_Supporting) to apply this point system
- If the informative variant is a frameshift or nonsense variant, it must reach classification as P/LP without use of PM5 and without use of only PVS1 plus PM2

---

### PM6 - De Novo (Assumed)

**Original ACMG Summary:** Assumed de novo, but without confirmation of paternity and maternity.

**VCEP Specifications:** Same as PS2 - use point-based system above. See [PS2 - De Novo (Confirmed)](#ps2---de-novo-confirmed).

---

### PP1 - Co-segregation

**Original ACMG Summary:** Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.

**Note:** May be used as stronger evidence with increasing segregation data.

**VCEP Specifications:**

Use ClinGen SVI recommendations for co-segregation criterion (PMID: 30311386) with the additional specification that unaffected individuals contributing to the calculated LOD score must be **heterozygous carriers** of one of the variants observed in the affected individuals (i.e., do not count wild-type/wild-type individuals).

#### PP1 Thresholds (General)

| Strength | Likelihood | LOD Score |
|----------|------------|-----------|
| Supporting (PP1) | 4:1 | 0.6 |
| Moderate (PP1_Moderate) | 16:1 | 1.2 |
| Strong (PP1_Strong) | 32:1 | 1.5 |

#### Autosomal Recessive Segregation (LOD Score Table)

For autosomal recessive inheritance, use the following table where affected segregations are counted in rows and unaffected segregations in columns:

|  | **Unaffected Recessive Segregations** |||||||||||
|---|---|---|---|---|---|---|---|---|---|---|---|
| **Affected** | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| 0 | 0 | 0.12 | 0.25 | 0.37 | 0.5 | 0.62 | 0.75 | 0.87 | 1 | 1.12 | 1.25 |
| 1 | 0.6 | 0.73 | 0.85 | 0.98 | 1.1 | 1.23 | 1.35 | 1.48 | 1.6 | 1.73 | 1.85 |
| 2 | 1.2 | 1.33 | 1.45 | 1.58 | 1.7 | 1.83 | 1.95 | 2.08 | 2.2 | 2.33 | 2.45 |
| 3 | 1.81 | 1.93 | 2.06 | 2.18 | 2.31 | 2.43 | 2.56 | 2.68 | 2.81 | 2.93 | 3.06 |
| 4 | 2.41 | 2.53 | 2.66 | 2.78 | 2.91 | 3.03 | 3.16 | 3.28 | 3.41 | 3.53 | 3.66 |
| 5 | 3.01 | 3.14 | 3.26 | 3.39 | 3.51 | 3.63 | 3.76 | 3.88 | 4.01 | 4.13 | 4.26 |

**Color coding:**
- LOD 0.6-1.19: Supporting (PP1)
- LOD 1.2-1.49: Moderate (PP1_Moderate)
- LOD ≥1.5: Strong (PP1_Strong)

**Definitions:**
- **Affected segregations:** Affected family members in whom biallelic compound heterozygous or homozygous variants segregate
- **Unaffected segregations:** Unaffected family members (typically siblings) who are at risk to inherit the two variants identified in the proband. These individuals should be either wild-type for both variants OR a heterozygous carrier for a single variant. Unaffected carrier parents DO NOT count as unaffected segregations.

---

### PP2 - Missense in Constrained Gene

**Original ACMG Summary:** Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.

**VCEP Specification:** *Not Applicable*

**Comments:** The gnomAD v2.1.1 missense Z score for JAK3 (Z = 2.81) suggests this gene is not constrained for missense variation. Both benign and pathogenic missense variants are present in JAK3.

---

### PP3 - Computational Evidence

**Original ACMG Summary:** Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).

**Caveat:** As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.

**VCEP Specification (Supporting):**

- Only applicable to **synonymous or intronic variants** predicted to impact splicing by SpliceAI with a delta score **≥0.2**
- **Do not apply to missense variants**

---

### PP4 - Phenotype Specificity

**Original ACMG Summary:** Patient's phenotype or family history is highly specific for a disease with a single genetic etiology.

**VCEP Specifications:**

PP4 applicability and strength is determined by the total points accumulated by a single affected individual according to the table below.

#### PP4 Strength Thresholds

| Total Points | Strength |
|--------------|----------|
| <1 | PP4 not met |
| 1 to <2 | PP4 (Supporting) |
| 2 to <6 | PP4_Moderate |
| ≥6 | PP4_Strong¹ |

¹CNV (Copy number variation) testing is required to consider PP4_Strong in order to certify that the variant in question is the causative for the phenotype, and not one CNV event corrected by gene therapy and not identified previously.

#### PP4 Point System

| Evidence Description | Points |
|---------------------|--------|
| Diagnostic criteria met for SCID (Criteria 1 and 3 or Criterion 4 by itself) or Leaky SCID/Omenn syndrome (excluding Criterion 2)² | 0.5 |
| SCID gene panel or exome/genome sequencing conducted (only applicable if genetic testing did not provide an alternative genetic explanation for SCID/Leaky SCID/Omenn syndrome phenotype) | 1 |
| Family history of SCID (only applicable if SCID gene panel or exome/genome sequencing was conducted on proband and did not provide an alternative genetic explanation for phenotype) | 0.5 |
| Reduced constitutive or IL-2, IL-7, or IL-15-induced JAK3 tyrosine phosphorylation in patient cells as established by the laboratory **AND** pathogenic or likely pathogenic variants in IL2RG, STAT5A, STAT5B, IL2RA, IL2RB, IL7R, and IL15RA **have been excluded** | 3 |
| Reduced constitutive or IL-2, IL-7, or IL-15-induced JAK3 tyrosine phosphorylation in patient cells as established by the laboratory **AND** pathogenic or likely pathogenic variants in IL2RG, STAT5A, STAT5B, IL2RA, IL2RB, IL7R, and IL15RA **have NOT been excluded** | 1 |
| Reduced constitutive or IL-2, IL-7, or IL-15-induced phosphorylation of STAT5 in patient-derived T or B cells as established by the laboratory **AND** pathogenic or likely pathogenic variants in IL2RG, STAT5A, STAT5B, IL2RA, IL2RB, IL7R, and IL15RA **have been excluded** | 3 |
| Reduced constitutive or IL-2, IL-7, or IL-15-induced phosphorylation of STAT5 in patient-derived T or B cells as established by the laboratory **AND** pathogenic or likely pathogenic variants in IL2RG, STAT5A, STAT5B, IL2RA, IL2RB, IL7R, and IL15RA **have NOT been excluded** | 1 |
| SCID phenotype corrected by JAK3 gene therapy **WITHOUT** CNV testing performed | 4.5 |
| SCID phenotype corrected by JAK3 gene therapy **WITH** CNV testing performed | 6 |
| T-B+NK- lymphocyte subset profile* | 0.5 |

²The diagnostic criteria should follow the PIDTC 2022 specification.

**Notes:**
1. If NK cells are not noted or are present, criteria may still be applied if SCID gene panel or exome/genome sequencing has ruled out alternative causes
2. If maternal T cells are present, the T lymphocyte profile is still considered to be T- (autologous T cells are absent)

**Reference PMIDs:** 8676091, 9354668, 10075926, 14615376, 19889552, 38598033

---

### PP5 - Reputable Source

**Original ACMG Summary:** Reputable source recently reports variant as pathogenic, but the evidence is not available to the laboratory to perform an independent evaluation.

**VCEP Specification:** *Not Applicable*

This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PMID: 29543229).

---

## Benign Criteria

### BA1 - Allele Frequency >5%

**Original ACMG Summary:** Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

**VCEP Specification (Stand Alone):**

- gnomAD popmax filtering allele frequency **>0.00447**

The maximum credible population allele frequency threshold was determined using Whiffin/Ware calculator with the following parameters:
- Prevalence: 1:5,000
- Allelic heterogeneity: 1
- Genetic heterogeneity: 0.05 (based on the contribution of JAK3 variants to total SCID in the PIDTC 6901 cohort reported in Dvorak et al., 2019 (PMID: 30193840, Table 1): 5.2%, rounded to 5%)
- Penetrance: 50%

---

### BS1 - Frequency Greater Than Expected

**Original ACMG Summary:** Allele frequency is greater than expected for disorder.

**VCEP Specification (Strong):**

- gnomAD popmax filtering allele frequency **>0.00100**
- Consider also bottleneck populations

The maximum credible population allele frequency threshold was determined using Whiffin/Ware calculator with the following parameters:
- Prevalence: 1:50,000
- Allelic heterogeneity: 1
- Genetic heterogeneity: 0.05 (based on the contribution of JAK3 variants to total SCID in the PIDTC 6901 cohort reported in Dvorak et al., 2019 (PMID: 30193840, Table 1): 5.2%, rounded to 5%)
- Penetrance: 100%

---

### BS2 - Observed in Healthy Adult

**Original ACMG Summary:** Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

**VCEP Specification (Supporting):**

Only to be used when the variant is observed in the **homozygous state** in a healthy adult.

---

### BS3 - Functional Studies (No Effect)

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

**VCEP Specification:** *Not Applicable*

**Comments:** There is not a well-established functional study which can rule out all damaging effects on protein function.

---

### BS4 - Lack of Segregation

**Original ACMG Summary:** Lack of segregation in affected members of a family.

**Caveat:** The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.

**VCEP Specification (Strong):**

Can be applied without additional specifications.

---

### BP1-BP7 - Benign Supporting

| Criterion | Status | Comment |
|-----------|--------|---------|
| **BP1** | *Not Applicable* | Does not apply. JAK3 missense variants are a known mechanism of disease. |
| **BP2** | *Not Applicable* | Does not apply (JAK3 is autosomal recessive). |
| **BP3** | *Not Applicable* | Does not apply. |
| **BP4** | *Not Applicable* | Does not apply. |
| **BP5** | *Not Applicable* | Does not apply. |
| **BP6** | *Not Applicable* | This criterion is not for use as recommended by the ClinGen SVI VCEP Review Committee (PMID: 29543229). |
| **BP7** | Supporting | Applicable to both synonymous variants and deep intronic variants affecting nucleotides at or beyond the +7 (donor) and -21 (acceptor) positions. The variant should be predicted not to impact splicing by at least two out of three *in silico* tools (GeneSplicer, MaxEntScan, NNSplice, SpliceAI, Splicing Sequences Finder (SSF), and varSEAK). Given the potential for poor conservation of genes related to T cell and B cell development among vertebrates, nucleotide conservation is not required in order to apply BP7. |

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
| 1 Strong **AND** 2 Moderate |

### Benign Classification

| Criteria Combination |
|---------------------|
| ≥2 Strong |
| 1 Stand Alone (BA1) |

### Likely Benign Classification

| Criteria Combination |
|---------------------|
| 1 Strong (BS1, BS4) |
| ≥2 Supporting (BS2_Supporting, BP7) |

---

## Appendices

### Appendix A: PVS1 Flowchart Summary

The PVS1 flowchart provides decision pathways for different variant types in JAK3:

**Key Gene-Specific Information:**
- **Last exon:** Exon 24
- **Penultimate exon NMD boundary:** After c.3157 (codon 1053) in exon 23
- **Biologically-relevant transcript:** NM_000215.4

The flowchart guides strength assignment based on:
1. Variant type (nonsense, frameshift, splice, deletion, duplication, initiation codon)
2. NMD prediction status
3. Protein region affected
4. Presence of downstream/upstream pathogenic variants

### Appendix B: Population Frequency Thresholds Summary

| Criterion | Threshold | Strength |
|-----------|-----------|----------|
| BA1 | >0.00447 | Stand Alone |
| BS1 | >0.00100 | Strong |
| PM2 | <0.000115 | Supporting |

### Appendix C: Reference PMIDs

| PMID | Reference Description |
|------|----------------------|
| 30192042 | Tayoun et al., 2018 - ClinGen SVI recommendations for PVS1 |
| 30311386 | Oza et al., 2018 - ClinGen SVI recommendations for PP1 segregation |
| 29543229 | ClinGen SVI VCEP Review Committee - PP5/BP6 not recommended |
| 14615376 | Roberts et al., 2004 - Approved functional assay for PS3 |
| 11668610 | PM1 hot spot residues reference |
| 30193840 | Dvorak et al., 2019 - JAK3 contribution to SCID |
| 8676091 | PP4 functional evidence reference |
| 9354668 | PP4 functional evidence reference |
| 10075926 | PP4 functional evidence reference |
| 19889552 | PP4 functional evidence reference |
| 38598033 | PP4 functional evidence reference |

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 2.1.0 | 10/1/2025 | Updated: PM5_Strong, PM5_Moderate, PM5_Supporting, PM5 Instructions; PP4 attachment table updates including addition of JAK3 PMIDs; PP4 instructions updated and harmonized with attached tables; PM3 attachment criterion table updates; Edited Likely Benign Rules (V1 had 1 strong, changed to 1 strong + 1 supporting was unintentional, reverted back to 1 strong) |
| 1.0.0 | Initial | Initial release |

---

*This document was compiled from ClinGen VCEP specifications and ClinGen SVI recommendations. For the most current version, please refer to the ClinGen website.*
