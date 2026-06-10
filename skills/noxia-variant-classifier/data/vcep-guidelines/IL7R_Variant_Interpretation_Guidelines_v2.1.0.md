# ClinGen Severe Combined Immunodeficiency Disease VCEP Variant Interpretation Guidelines for IL7R

**Version:** 2.1.0
**Released:** 10/1/2025
**Affiliation:** Severe Combined Immunodeficiency Disease VCEP
**Based on:** Richards et al., 2015 ACMG/AMP Guidelines

---

## Gene Information

| Attribute | Value |
|-----------|-------|
| **Gene** | IL7R (HGNC:6024) |
| **HGNC Name** | interleukin 7 receptor |
| **Transcript** | NM_002185.5 |
| **Disease** | immunodeficiency 104 (MONDO:0012163) |
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

**Original ACMG Summary:** Null variant (nonsense, frameshift, canonical +/-1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.

**Caveats:**
- Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7).
- Use caution interpreting LOF variants at the extreme 3' end of a gene.
- Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact.
- Use caution in the presence of multiple transcripts.

**VCEP Specifications:** See attached PVS1 flowchart (Appendix A).

#### Strength Levels

| Strength | Criteria |
|----------|----------|
| **Very Strong** | Use ClinGen SVI recommendations for loss of function criterion (Tayoun et al., 2018 (PMID: 30192042)). |
| **Strong** | Use ClinGen SVI recommendations with two specifications: (1) For variants not predicted to undergo NMD but removing >10% of protein (i.e. variants in the last exon, exon 8, or variants in the last 50 nucleotides of the penultimate exon after c.826, codon 276, in exon 7), at least one pathogenic variant **must be** present downstream to apply PVS1_Strong. (2) PVS1_Strong can be applied to variants not predicted to undergo NMD but causing truncation of the transmembrane domain (which begins at amino acid 240) or any distal region (i.e. cytoplasmic domain). |
| **Moderate** | Use ClinGen SVI recommendations with one specification: For variants not predicted to undergo NMD but removing >10% of protein (i.e. variants in the last exon, exon 8, or variants in the last 50 nucleotides of the penultimate exon after c.826, codon 276, in exon 7), when at least one pathogenic variant is **not** present downstream, downgrade to PVS1_Moderate. |
| **Supporting** | For initiation codon variants with no pathogenic variant(s) upstream of closest potential in-frame start codon. |

---

### PS1 - Same Amino Acid Change

**Original ACMG Summary:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.

**Example:** Val->Leu caused by either G>C or G>T in the same codon.

**Caveat:** Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | Applicable if the previously established variant is classified as **pathogenic** by SCID VCEP specifications for IL7R. Can also be applied for splice variants at the same nucleotide and with similar impact prediction as previously reported pathogenic variant (if the predicted impact is equal to or greater than the known pathogenic variant per in silico splicing tool SpliceAI). Example: c.105+1G>C is known to be pathogenic, can use PS1 for c.105+1G>T. |
| **Moderate** | Applicable if the previously established variant is classified as **likely pathogenic** by SCID VCEP specifications for IL7R. Can also be applied for splice variants at the same nucleotide and with similar impact prediction as previously reported likely pathogenic variant (if the predicted impact is equal to or greater than the known pathogenic variant per in silico splicing tool SpliceAI). Example: c.105+1G>C is known to be likely pathogenic, can use PS1 for c.105+1G>T. |

---

### PS2 - De Novo (Confirmed)

**Original ACMG Summary:** De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.

**Note:** Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.

**VCEP Specifications:**

The following guidelines should be used when determining the phenotypic consistency of each proband:
- **"Phenotype highly specific for gene"** proband must meet at least PP4_Moderate criteria
- **"Phenotype consistent with gene but not highly specific"** proband must meet PP4 criteria
- **"Phenotype consistent with gene but not highly specific and high genetic heterogeneity"** proband has been asserted to have a SCID phenotype but does not meet PP4 criteria
- Reduce points per proband by half if the phase is unconfirmed

Use ClinGen SVI recommendations for *de novo* criteria.

#### PS2/PM6 Point System

| Phenotypic Consistency | Confirmed Parental Relationships | Unconfirmed Parental Relationships |
|------------------------|----------------------------------|-------------------------------------|
| Phenotype highly specific for gene | 2 points | 1 point |
| Phenotype consistent but not highly specific | 1 point | 0.5 points |
| Phenotype consistent + high genetic heterogeneity | 0.5 points | 0.25 points |
| Phenotype not consistent | 0 points | 0 points |

*Note: Maximum allowable value of 1 may contribute to overall score for high genetic heterogeneity category.*

#### Evidence Strength Thresholds

| Points | Strength Level |
|--------|----------------|
| 0.5 | PS2_Supporting or PM6_Supporting |
| 1.0 | PS2_Moderate or PM6 |
| 2.0 | PS2 or PM6_Strong |
| 4.0 | PS2_VeryStrong or PM6_VeryStrong |

---

### PS3 - Functional Studies

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.

**Note:** Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | PS3 may potentially be applied at the default strength level of strong for evidence from an animal model expressing the variant of interest and recapitulating the IL7R-SCID phenotype. Animal models will be reviewed on a case-by-case basis by the VCEP to determine the appropriate strength level. |
| **Supporting** | PS3_Supporting can be applied based on an abnormal result in **at least one** approved *in vitro* assay (IL-7-induced Jak3 phosphorylation assay, IL-7 binding assay, IL-7-induced STAT5 DNA binding/transcriptional induction). |

**Important:** At least one previously observed proband with the expressed IL7R variant meeting PP4 is required to apply PS3 at any strength on the basis of a cellular model/in vitro study.

#### Approved Assay Instances

| Assay | PMID | Description | Strength |
|-------|------|-------------|----------|
| **IL-7-induced Jak3 phosphorylation assay** | 11023514 (Roifman et al., 2000) | COS-7 cells transfected with wild type and variant IL7R cDNA constructs; readout is presence/intensity of band corresponding to Jak3 tyrosine phosphorylation | PS3_Supporting |
| **IL-7 binding assay** | 9843216 (Puel et al., 1998) | 293T cells transfected with wild type and variant IL7R and wild type gamma-c cDNA constructs; readout is ratio of specific binding to concentration of free radioligand | PS3_Supporting |
| **IL-7-induced STAT5 DNA binding activity** | 9843216 (Puel et al., 1998) | Stat5 DNA binding evaluated by electrophoretic mobility shift assay in 293T cells; readout is presence/intensity of band corresponding to DNA-bound Stat5 | PS3_Supporting |
| **IL-7-induced STAT5 transcription activity** | 9843216 (Puel et al., 1998) | Transcription from a Stat5-responsive reporter construct evaluated by luciferase activity in 293T cells; readout is relative luciferase activity | PS3_Supporting |

---

### PS4 - Prevalence in Affected

**Original ACMG Summary:** The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.

**VCEP Specifications:** *Not Applicable*

---

### PM1 - Mutational Hot Spot

**Original ACMG Summary:** Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.

**VCEP Specifications:** *Not Applicable*

---

### PM2 - Absent from Controls

**Original ACMG Summary:** Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

**Caveat:** Population data for indels may be poorly called by next generation sequencing.

**VCEP Specification (Supporting only):**

- gnomAD popmax filtering allele frequency **<0.00004129**
- An additional requirement is that **no homozygotes** have been observed in gnomAD

---

### PM3 - In Trans with Pathogenic

**Original ACMG Summary:** For recessive disorders, detected in trans with a pathogenic variant.

**Note:** This requires testing of parents (or offspring) to determine phase.

**VCEP Specifications:** Use ClinGen SVI adapted recommendations for *in trans* criterion with the additional requirement that the co-occurring variant must be classified using the SCID VCEP specifications for IL7R.

**Caveat:** All variants should be sufficiently rare (meet PM2 specification). The applicability of PM3 to suspected founder variants with allele frequencies exceeding the PM2 threshold will be evaluated on a case-by-case basis by the VCEP.

#### PM3 Point System (Per Proband)

| Classification/Zygosity of Other Variant | Confirmed in Trans | Phase Unknown |
|------------------------------------------|-------------------|---------------|
| Pathogenic or Likely pathogenic variant | 1.0 | 0.5 (P) / 0.25 (LP) |
| Homozygous (non-consanguineous, no max) | 1.0 | 1.0 |
| Homozygous (consanguineous, max 0.5/family) | 0.5 | 0.5 |
| VUS (max 0.5 total) | 0.25 | 0.0 |

*All variants should be sufficiently rare (meet PM2 specification); P = Pathogenic; LP = Likely pathogenic*

#### PM3 Evidence Strength Thresholds

| Total Points | Strength Level |
|--------------|----------------|
| 0.5 | PM3_Supporting |
| 1.0 | PM3 (Moderate) |
| 2.0 | PM3_Strong |
| 4.0 | PM3_VeryStrong |

#### PM3 Considerations

- **Allele Frequency:** Application of PM3 is contingent on the allele frequency of the variant being assessed and the variant presumably on the other allele both being sufficiently rare (meets PM2 threshold).
- **Phasing:** If the phase cannot be determined, it is recommended that at least two different LP/P variants are needed to equal the weight of one LP/P co-occurrence confirmed in trans. If only one parent is tested and found to carry one allele, variants can be counted as in trans.
- **Classification:** Probands should be weighted less when the variant on the other allele is of uncertain significance and rare (meets PM2). To avoid circularity, the classification of the variant on the other allele should not use evidence from the variant being interrogated.
- **Homozygous occurrences:** For homozygous occurrences, the default weight is dropped to 0.5 points, as a rare homozygous occurrence may be due to consanguinity. A recommended max of 1.0 points of all homozygous cases is suggested.

---

### PM4 - Protein Length Changes

**Original ACMG Summary:** Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Moderate** | When applied to deletion variants, the deleted region must contain a known **pathogenic or likely pathogenic** variant that is not predicted/observed to alter splicing. |
| **Supporting** | When applied to deletion variants, the deleted region must contain a known **VUS** variant that is not predicted/observed to alter splicing. |

---

### PM5 - Novel Missense at Same Residue

**Original ACMG Summary:** Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.

**Example:** Arg156His is pathogenic; now you observe Arg156Cys.

**Caveat:** Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:**

#### For Missense Variants

| Strength | Criteria |
|----------|----------|
| **Moderate (PM5)** | Applicable at default strength if previously established variant is classified as **pathogenic**. |
| **Supporting (PM5_Supporting)** | Applicable if previously established variant is classified as **likely pathogenic**. |

#### For Nonsense Variants (Point-Based System)

| Strength | Criteria |
|----------|----------|
| **Strong (PM5_Strong)** | PM5 may be applied at a Strong level of evidence for any nonsense variant with **4+ points** from informative variants. PM5_Strong should be downgraded to PM5_Moderate if PVS1 is applied at any strength. |
| **Moderate (PM5_Moderate)** | PM5 may be applied at a Moderate level of evidence for any nonsense variant with **2+ points** from informative variants. PM5_Moderate may not be combined with PVS1_VeryStrong (should be downgraded to PM5_Supporting if PVS1_VeryStrong is applied). |
| **Supporting (PM5_Supporting)** | Applicable to a nonsense variant with **1 point** from an informative variant. |

#### PM5 Point Table for Nonsense Variants

| Type of Variant Under Assessment (VUA) | Informative Variant | Score |
|----------------------------------------|---------------------|-------|
| Nonsense variant predicted to lead to NMD | P/LP variant in the exon of DNA change predicted to lead to NMD | +1 pt |
| Nonsense variant predicted to lead to NMD | B/LB variant in the exon predicted to lead to NMD | -2 pt |
| Nonsense variant, resulting in a PTC in the final exon, not predicted to lead to NMD | P/LP variant resulting in a PTC in the same exon but downstream of VUA | +1 pt |
| Nonsense variant, resulting in a PTC in the final exon, not predicted to lead to NMD | B/LB variant resulting in PTC in the same exon but upstream of the VUA | -2 pt |

*NMD = nonsense-mediated decay; PTC = premature termination codon*

**Notes:**
- The informative variant must be classified by the SCID VCEP specifications and may not be the same variant used to meet "+1 pathogenic variant downstream" on the PVS1 flowchart.
- If negative points are calculated, the curator should not apply PM5 and should reconsider if PVS1 is applicable for the VUA.
- The VUA must be sufficiently rare, meet PM2_Supporting, to apply this point system.
- If the informative variant is a frameshift or nonsense variant, it must reach classification as Pathogenic or Likely Pathogenic without use of PM5 and without use of only PVS1 plus PM2.

---

### PM6 - De Novo (Assumed)

**Original ACMG Summary:** Assumed de novo, but without confirmation of paternity and maternity.

**VCEP Specifications:** Same as PS2 - use point-based system above. Points per proband should be reduced by half when parental relationships are unconfirmed.

---

### PP1 - Co-segregation

**Original ACMG Summary:** Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.

**Note:** May be used as stronger evidence with increasing segregation data.

**VCEP Specifications:** Use ClinGen SVI recommendations for co-segregation criterion (PMID: 30311386) with the additional specification that unaffected individuals contributing to the calculated LOD score must be heterozygous carriers of one of the variants observed in the affected individuals (i.e. do not count wild-type/wild-type individuals).

#### PP1 Thresholds

| Strength | Likelihood | LOD Score |
|----------|------------|-----------|
| Supporting | 4:1 | 0.6 |
| Moderate | 16:1 | 1.2 |
| Strong | 32:1 | 1.5 |

#### PP1 for Autosomal Recessive Segregation

Use Table 4b from PMID: 30311386 for autosomal recessive segregation evidence. Affected segregations are counted in rows and unaffected segregations in columns. Affected segregations are affected family members in whom biallelic compound heterozygous or homozygous variants segregate. Unaffected segregations are defined as unaffected family members, typically siblings, who are at risk to inherit the two variants identified in the proband. These individuals should be either wild-type for both variants identified in the proband, or a heterozygous carrier for a single variant. Unaffected, carrier parents DO NOT count as unaffected segregations.

---

### PP2 - Missense in Constrained Gene

**Original ACMG Summary:** Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.

**VCEP Specifications:** *Not Applicable*

**Comments:** Does not apply. The gnomAD v2.1.1 missense Z score for IL7R (Z = -1.29) suggests this gene is not constrained for missense variation. Both benign and pathogenic missense variants are present in IL7R.

---

### PP3 - Computational Evidence

**Original ACMG Summary:** Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).

**Caveat:** As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.

**VCEP Specifications (Supporting):**
- Only applicable to **synonymous or intronic variants** predicted to impact splicing by SpliceAI with a delta score **greater than or equal to 0.2**
- **Do not apply to missense variants**

---

### PP4 - Phenotype Specificity

**Original ACMG Summary:** Patient's phenotype or family history is highly specific for a disease with a single genetic etiology.

**VCEP Specifications:** PP4 applicability and strength is determined by the total points accumulated by a single affected individual according to the table below and the following total point ranges:

#### PP4 Strength Thresholds

| Total Points | Strength |
|--------------|----------|
| <1 | PP4 not met |
| 1 to <2 | PP4 (Supporting) |
| 2 to <6 | PP4_Moderate |
| >=6 | PP4_Strong |

#### PP4 Point Table

| Evidence Description | Points |
|---------------------|--------|
| Diagnostic criteria met for SCID (Criteria 1 and 3 or Criterion 4 by itself) or Leaky SCID/Omenn syndrome (excluding Criterion 2)^1^ | 0.5 |
| SCID gene panel or exome/genome sequencing conducted (only applicable if genetic testing did not provide an alternative genetic explanation for SCID/Leaky SCID/Omenn syndrome phenotype) | 1 |
| Family history of SCID (only applicable if SCID gene panel or exome/genome sequencing was conducted on proband and did not provide an alternative genetic explanation for phenotype) | 0.5 |
| Absent CD127 expression (demonstrated by RT-PCR, Western blot, flow cytometry) PMIDs: 9843216, 11023514, 17827065 | 4.5 |
| Reduced CD127 expression (demonstrated by RT-PCR, or Western blot) as established by the laboratory PMIDs: 9843216, 11023514, 17827065 | 3 |
| Reduced CD127 expression (demonstrated by flow cytometry) as established by the laboratory AND pathogenic or likely pathogenic variants in IL2RG have been excluded; OR reduced IL-7-induced phosphorylation of STAT5 in patient-derived T-cells as established by the laboratory AND pathogenic or likely pathogenic variants in IL2RG, JAK3, STAT5A, and STAT5B have been excluded PMID: 38587703 | 3 |
| Reduced CD127 expression (demonstrated by flow cytometry) as established by the laboratory AND pathogenic or likely pathogenic variants in IL2RG have **NOT** been excluded; OR reduced IL-7-induced phosphorylation of STAT5 in patient-derived T-cells as established by the laboratory AND pathogenic or likely pathogenic variants in IL2RG, JAK3, STAT5A, and STAT5B have **NOT** been excluded PMID: 38587703 | 1 |
| SCID phenotype corrected by IL7R gene therapy **WITHOUT** CNV testing performed | 4.5 |
| SCID phenotype corrected by IL7R gene therapy **WITH** CNV testing performed | 6 |
| T-B+NK+ lymphocyte subset profile* (See notes) | 0.25 |

^1^The diagnostic criteria should follow the PIDTC 2022 specification.

**Notes:**
1. CNV (Copy number variation) testing is required to consider PP4_Strong in order to certify that the variant in question is the causative for the phenotype, and not one CNV event corrected by gene therapy and not identified previously.
2. If NK cells are not noted or are present, criteria may still be applied if SCID gene panel or exome/genome sequencing has ruled out alternative causes.
3. If maternal T cells are present, the T lymphocyte profile is still considered to be T- (autologous T cells are absent).

---

### PP5 - Reputable Source

**Original ACMG Summary:** Reputable source recently reports variant as pathogenic, but the evidence is not available to the laboratory to perform an independent evaluation.

**VCEP Specifications:** *Not Applicable*

This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PMID: 29543229).

---

## Benign Criteria

### BA1 - Allele Frequency >5%

**Original ACMG Summary:** Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

**VCEP Specifications:** Maximum credible population allele frequency threshold is determined using Whiffin/Ware calculator (https://www.cardiodb.org/allelefrequencyapp/) and the following parameters:
- Prevalence: 1:5,000
- Allelic heterogeneity: 1
- Genetic heterogeneity: 0.08 (based on the contribution of IL7R variants to total SCID in the PIDTC 6901 cohort reported in Dvorak et al., 2019 (PMID: 30193840, Table 1): 7.6%, rounded to 8%)
- Penetrance: 50%

**VCEP Specification (Stand Alone):**
- gnomAD popmax filtering allele frequency **>0.00566**

---

### BS1 - Frequency Greater Than Expected

**Original ACMG Summary:** Allele frequency is greater than expected for disorder.

**VCEP Specifications:** Maximum credible population allele frequency threshold determined using Whiffin/Ware calculator (https://www.cardiodb.org/allelefrequencyapp/) and the following parameters:
- Prevalence: 1:50,000
- Allelic heterogeneity: 1
- Genetic heterogeneity: 0.08 (based on the contribution of IL7R variants to total SCID in the PIDTC 6901 cohort reported in Dvorak et al., 2019 (PMID: 30193840, Table 1): 7.6%, rounded to 8%)
- Penetrance: 100%

**VCEP Specification (Strong):**
- gnomAD popmax filtering allele frequency **>0.00126**
- Consider also bottleneck populations

---

### BS2 - Observed in Healthy Adult

**Original ACMG Summary:** Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

**VCEP Specification (Supporting):**
- Only to be used when the variant is observed in the **homozygous state** in a healthy adult.

---

### BS3 - Functional Studies (No Effect)

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

**VCEP Specifications:** *Not Applicable*

**Comments:** There is not a well-established functional study which can rule out all damaging effects on protein function.

---

### BS4 - Lack of Segregation

**Original ACMG Summary:** Lack of segregation in affected members of a family.

**Caveat:** The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.

**VCEP Specification (Strong):**
- Can be applied without additional specifications.

---

### BP1-BP7 - Benign Supporting

| Criterion | Status | Comment |
|-----------|--------|---------|
| **BP1** | Not Applicable | Does not apply. IL7R missense variants are a known mechanism of disease. |
| **BP2** | Not Applicable | - |
| **BP3** | Not Applicable | Does not apply. |
| **BP4** | Not Applicable | - |
| **BP5** | Not Applicable | - |
| **BP6** | Not Applicable | This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PMID: 29543229). |
| **BP7** | Supporting | Applicable to both synonymous variants and deep intronic variants affecting nucleotides at or beyond the +7 (donor) and -21 (acceptor) positions. The variant should be predicted not to impact splicing by at least two out of three in silico tools (freely available tools include GeneSplicer, MaxEntScan, NNSplice, SpliceAI, Splicing Sequences Finder (SSF), and varSEAK). Given the potential for poor conservation of genes related to T cell and B cell development among vertebrates, nucleotide conservation is not required in order to apply BP7. |

---

## Rules for Combining Criteria

### Pathogenic Classification

| Criteria Combination |
|---------------------|
| 1 Very Strong **AND** >=1 Strong |
| 1 Very Strong **AND** >=2 Moderate |
| 1 Very Strong **AND** 1 Moderate **AND** 1 Supporting |
| 1 Very Strong **AND** >=2 Supporting |
| >=2 Strong |
| 1 Strong **AND** >=3 Moderate |
| 1 Strong **AND** 2 Moderate **AND** >=2 Supporting |
| 1 Strong **AND** 1 Moderate **AND** >=4 Supporting |

### Likely Pathogenic Classification

| Criteria Combination |
|---------------------|
| 1 Very Strong **AND** 1 Moderate |
| 1 Strong **AND** 1 Moderate |
| 1 Strong **AND** >=2 Supporting |
| >=3 Moderate |
| 2 Moderate **AND** >=2 Supporting |
| 1 Moderate **AND** >=4 Supporting |
| 1 Strong **AND** 2 Moderate |

### Benign Classification

| Criteria Combination |
|---------------------|
| >=2 Strong |
| 1 Stand Alone (BA1) |

### Likely Benign Classification

| Criteria Combination |
|---------------------|
| 1 Strong (BS1, BS4) |
| >=2 Supporting (BS2_Supporting, BP7) |

---

## Appendices

### Appendix A: PVS1 Flowchart

The PVS1 flowchart for IL7R includes specific guidance for different variant types:

#### Nonsense or Frameshift Variants

| Scenario | Strength |
|----------|----------|
| Predicted to undergo NMD, exon is present in biologically-relevant transcript(s) | PVS1 |
| Predicted to undergo NMD, exon is absent from biologically-relevant transcript(s) | N/A |
| Not predicted to undergo NMD (PTC in last exon or last 50 nt of penultimate exon [c.826, codon 276, in exon 7]), truncated region is critical (transmembrane domain at aa 240 or distal) | PVS1_Strong |
| Not predicted to undergo NMD, role of region unknown, LoF variants not frequent, variant removes >10% of protein, 1+ pathogenic variant downstream | PVS1_Strong |
| Not predicted to undergo NMD, role of region unknown, LoF variants not frequent, variant removes >10% of protein, no pathogenic variant downstream | PVS1_Moderate |
| Not predicted to undergo NMD, role of region unknown, LoF variants not frequent, variant removes <10% of protein | PVS1_Moderate |

#### GT-AG 1,2 Splice Site Variants

| Scenario | Strength |
|----------|----------|
| Exon skipping/cryptic splice disrupts reading frame, predicted to undergo NMD, exon present in biologically-relevant transcript(s) | PVS1 |
| Exon skipping/cryptic splice disrupts reading frame, NOT predicted to undergo NMD, truncated region is critical (transmembrane domain at aa 240 or distal) | PVS1_Strong |
| Exon skipping/cryptic splice disrupts reading frame, NOT predicted to undergo NMD, role unknown, LoF variants not frequent, variant removes >10%, 1+ pathogenic variant downstream | PVS1_Strong |
| Exon skipping/cryptic splice disrupts reading frame, NOT predicted to undergo NMD, role unknown, LoF variants not frequent, variant removes >10%, no pathogenic variant downstream | PVS1_Moderate |
| Exon skipping/cryptic splice preserves reading frame, role unknown, LoF variants not frequent, variant removes >10%, 1+ pathogenic variant within deleted region | PVS1_Strong |
| Exon skipping/cryptic splice preserves reading frame, role unknown, LoF variants not frequent, variant removes >10%, no pathogenic variants within deleted region | PVS1_Moderate |

#### Deletion (Single Exon to Full Gene)

| Scenario | Strength |
|----------|----------|
| Full gene deletion | PVS1 |
| Single to multi exon deletion, disrupts reading frame, predicted to undergo NMD, exon present | PVS1 |
| Single to multi exon deletion, disrupts reading frame, NOT predicted to undergo NMD, truncated region is critical | PVS1_Strong |
| Single to multi exon deletion, disrupts reading frame, NOT predicted to undergo NMD, role unknown, LoF variants not frequent, variant removes >10%, 1+ pathogenic variant within deleted region | PVS1_Strong |
| Single to multi exon deletion, disrupts reading frame, NOT predicted to undergo NMD, role unknown, LoF variants not frequent, variant removes >10%, no pathogenic variants within deleted region | PVS1_Moderate |
| Single to multi exon deletion, preserves reading frame, truncated region is critical | PVS1_Strong |
| Single to multi exon deletion, preserves reading frame, role unknown, LoF variants not frequent, variant removes >10%, 1+ pathogenic variant within deleted region | PVS1_Strong |
| Single to multi exon deletion, preserves reading frame, role unknown, LoF variants not frequent, variant removes >10%, no pathogenic variants within deleted region | PVS1_Moderate |

#### Duplication (>=1 exon, completely contained within gene)

| Scenario | Strength |
|----------|----------|
| Proven in tandem, reading frame disrupted and NMD predicted | PVS1 |
| Presumed in tandem, reading frame presumed disrupted and NMD predicted | PVS1_Strong |
| Proven not in tandem | N/A |
| No or unknown impact on reading frame and NMD | N/A |

#### Initiation Codon Variants

| Scenario | Strength |
|----------|----------|
| No known alternative start codon, >=1 pathogenic variant upstream of closest potential in-frame start codon | PVS1_Moderate |
| No known alternative start codon, no pathogenic variant upstream of closest potential in-frame start codon | PVS1_Supporting |
| Different functional transcript uses alternative start codon | N/A |

### Appendix B: Population Frequency Thresholds Summary

| Criterion | Threshold | Strength |
|-----------|-----------|----------|
| BA1 | >0.00566 | Stand Alone |
| BS1 | >0.00126 | Strong |
| PM2 | <0.00004129 | Supporting |

### Appendix C: Reference PMIDs

| PMID | Reference | Usage |
|------|-----------|-------|
| 30192042 | Tayoun et al., 2018 | PVS1 flowchart/SVI recommendations for LOF criterion |
| 30311386 | Oza et al., 2018 | PP1 co-segregation criterion |
| 30193840 | Dvorak et al., 2019 | Population frequency calculations (genetic heterogeneity) |
| 29543229 | Biesecker et al., 2018 | PP5/BP6 not recommended |
| 11023514 | Roifman et al., 2000 | IL-7-induced Jak3 phosphorylation assay (PS3) |
| 9843216 | Puel et al., 1998 | IL-7 binding assay, STAT5 DNA binding/transcription (PS3) |
| 17827065 | - | CD127 expression studies (PP4) |
| 38587703 | - | CD127/STAT5 phosphorylation studies (PP4) |

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 2.1.0 | 10/1/2025 | Updated: PM5_Strong, PM5_Moderate, PM5_Supporting, PM5 Instructions; PP4 attachment table updates; PP4 instructions; PM3 attachment criterion table updates; Edited Likely Benign Rules for Combining Criteria (V1 had 1 strong, the change in V2 to 1 strong + 1 supporting was unintentional) |

---

*This document was compiled from ClinGen VCEP specifications and ClinGen SVI recommendations. For the most current version, please refer to the ClinGen website.*
