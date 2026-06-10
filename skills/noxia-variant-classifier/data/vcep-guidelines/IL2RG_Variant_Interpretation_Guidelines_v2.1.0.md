# ClinGen Severe Combined Immunodeficiency Disease VCEP Variant Interpretation Guidelines for IL2RG

**Version:** 2.1.0
**Released:** 10/1/2025
**Affiliation:** Severe Combined Immunodeficiency Disease VCEP
**Based on:** Richards et al., 2015 ACMG/AMP Guidelines

---

## Gene Information

| Attribute | Value |
|-----------|-------|
| **Gene** | IL2RG (HGNC:6010) |
| **HGNC Name** | interleukin 2 receptor subunit gamma |
| **Transcript** | NM_000206.3 |
| **Disease** | T-B+ severe combined immunodeficiency due to gamma chain deficiency (MONDO:0010315) |
| **Inheritance** | X-linked inheritance |

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

**VCEP Specifications:** Use ClinGen SVI recommendations for loss of function criterion (Tayoun et al., 2018; PMID: 30192042) with IL2RG-specific modifications. See attached PVS1 flowchart in Appendix A.

#### Strength Levels

| Strength | Criteria |
|----------|----------|
| **Very Strong (PVS1)** | Use SVI recommendations with one specification: PVS1 at default strength (Very Strong) can be applied to variants not predicted to undergo nonsense-mediated decay but truncating the transmembrane domain (which begins at amino acid 255) or any distal region (i.e. cytoplasmic domain) due to the lack of functionality of the protein expressed with this defect. |
| **Strong (PVS1_Strong)** | Use SVI recommendations with one specification: For variants not predicted to undergo nonsense-mediated decay but removing >10% of protein (i.e. variants in the last exon, exon 8, or variants in the last 50 nucleotides of the penultimate exon after c.874, codon 292, in exon 7), at least one pathogenic variant **must be** present downstream in order to apply PVS1_Strong. |
| **Moderate (PVS1_Moderate)** | Use SVI recommendations with one specification: For variants not predicted to undergo nonsense-mediated decay but removing >10% of protein (i.e. variants in the last exon, exon 8, or variants in the last 50 nucleotides of the penultimate exon after c.874, codon 292, in exon 7), when at least one pathogenic variant is **not** present downstream, downgrade to PVS1_Moderate. |
| **Supporting (PVS1_Supporting)** | Use ClinGen SVI recommendations for loss of function criterion (Tayoun et al., 2018; PMID: 30192042). |

**Modification Type:** Gene-specific, Strength

---

### PS1 - Same Amino Acid Change

**Original ACMG Summary:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.

**Example:** Val->Leu caused by either G>C or G>T in the same codon.

**Caveat:** Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:**

Same amino acid change as a previously established pathogenic variant regardless of nucleotide change **OR** splice variants at same nucleotide and with similar impact prediction as previously reported pathogenic variant (if the predicted impact is equal to or greater than the known pathogenic variant per in silico splicing tools, i.e. SpliceAI).

- Can also use PS1 for splice variants located in the splice consensus sequence, at the same nucleotide position as a previously reported pathogenic variant
  - Example: c.105+1G>C is known to be pathogenic, can use PS1 for c.105+1G>T
- Applicable at default strength (PS1) if previously established variant is classified as pathogenic or at reduced strength of PS1_Moderate if previously established variant is classified as likely pathogenic
- Previously established variant must be classified by SCID VCEP specifications for IL2RG

| Strength | Criteria |
|----------|----------|
| **Strong (PS1)** | Strength modification depending upon classification of previously established variant (pathogenic vs. likely pathogenic). Previously established variant must be classified using the SCID VCEP specifications for IL2RG. |
| **Moderate (PS1_Moderate)** | Applicable when previously established variant is classified as likely pathogenic. Previously established variant must be classified using the SCID VCEP specifications for IL2RG. |

**Modification Type:** General recommendation, Strength

---

### PS2 - De Novo (Confirmed)

**Original ACMG Summary:** De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.

**Note:** Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.

**VCEP Specifications:**

The following guidelines should be used when determining the phenotypic consistency of each proband:

- **"Phenotype highly specific for gene":** proband must meet at least PP4_Moderate criteria
- **"Phenotype consistent with gene but not highly specific":** proband must meet PP4 criteria
- **"Phenotype consistent with gene but not highly specific and high genetic heterogeneity":** proband has been asserted to have a SCID phenotype but does not meet PP4 criteria
- Reduce points per proband by half if the phase is unconfirmed
- Unaffected carrier females must have an affected child and maternity and paternity must be confirmed

Use ClinGen SVI recommendations for de novo criteria. Phenotypic consistency determined using points-based system defined in PP4.

#### PS2/PM6 Point System (Per Proband)

| Phenotypic Consistency | Confirmed Parental Relationships | Unconfirmed Parental Relationships |
|------------------------|----------------------------------|-----------------------------------|
| Phenotype highly specific for gene (meets PP4_Moderate) | 2 points | 1 point |
| Phenotype consistent but not highly specific (meets PP4) | 1 point | 0.5 points |
| Phenotype consistent + high genetic heterogeneity (does not meet PP4) | 0.5 points | 0.25 points |
| Phenotype not consistent | 0 points | 0 points |

#### Evidence Strength Thresholds

| Points | Strength Level |
|--------|----------------|
| 0.5 | PS2_Supporting |
| 1.0 | PS2_Moderate |
| 2.0 | PS2_Strong |
| 4.0 | PS2_VeryStrong |

**Modification Type:** Disease-specific, Strength

---

### PS3 - Functional Studies

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.

**Note:** Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.

**VCEP Specifications:**

- PS3 may potentially be applied at the default strength level of **strong** for evidence from an animal model expressing the variant of interest and recapitulating the IL2RG-SCID phenotype. Animal models will be reviewed on a case-by-case basis by the VCEP to determine the appropriate strength level.
- PS3_Supporting can be applied based on an abnormal result in **at least one** approved in vitro assay.
- **At least one previously observed proband with the IL2RG variant meeting PP4 is required to apply PS3 at any strength on the basis of a cellular model/in vitro study.**

| Strength | Criteria |
|----------|----------|
| **Strong (PS3)** | PS3 may potentially be applied at the default strength level of strong for evidence from an animal model expressing the variant of interest and recapitulating the IL2RG-SCID phenotype. |
| **Supporting (PS3_Supporting)** | Strength modification based on an abnormal result in **at least** one approved in vitro assay. |

**Modification Type:** Disease-specific, Strength

#### Approved Assay Instances

| Assay Type | Reference | PMID | Strength |
|------------|-----------|------|----------|
| **Phosphorylation of JAK3/Co-Immunoprecipitation with JAK3** | Sharfe et al., 1997 | 9399950 | PS3_Supporting |
| **Phosphorylation of JAK3/Co-Immunoprecipitation with JAK3** | Kumaki et al., 1999 | 9933465 | PS3_Supporting |
| **Phosphorylation of JAK3/Co-Immunoprecipitation with JAK3** | Arcas-Garcia et al., 2020 | 31799703 | PS3_Supporting |
| **Cytokine binding** | Sharfe et al., 1997 | 9399950 | PS3_Supporting |
| **Cytokine binding** | Kumaki et al., 1995 | 7632950 | PS3_Supporting |
| **Surface expression of the gamma chain** | Kumaki et al., 1995 | 7632950 | PS3_Supporting |
| **Interaction profiling-BioID** | Tuovinen et al., 2020 | 32072341 | PS3_Supporting |

---

### PS4 - Prevalence in Affected

**Original ACMG Summary:** The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.

**Note 1:** Relative risk (RR) or odds ratio (OR), as obtained from case-control studies, is >5.0 and the confidence interval around the estimate of RR or OR does not include 1.0.

**Note 2:** In instances of very rare variants where case-control studies may not reach statistical significance, the prior observation of the variant in multiple unrelated patients with the same phenotype, and its absence in controls, may be used as moderate level of evidence.

**VCEP Specifications:**

When the variant has been detected in multiple affected unrelated individuals, count the number of probands, **excluding** the proband used to satisfy the PP4 criteria:

| Strength | Criteria |
|----------|----------|
| **PS4_Supporting** | 1 proband (Sum of case scores 1-2 points) |
| **PS4_Moderate** | 2 probands (Sum of case scores 2.5-4 points) |
| **PS4_Strong** | 3 probands (Sum of case scores 4.5-16 points) |
| **PS4_VeryStrong** | ≥4 probands (Sum of case scores >16 points) |

**Caveats:**
- Variant must be sufficiently rare (meet PM2 specification)
- Proband must fulfill the diagnostic criteria for SCID as per the PIDTC 2022 guidelines

**Modification Type:** Gene-specific, Strength

---

### PM1 - Mutational Hot Spot

**Original ACMG Summary:** Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.

**VCEP Specifications:**

**Upgraded to PM1_Strong.**

Defined to include missense alterations of the following positions:

- **Conserved cysteine residues:** Cys62, Cys72, Cys102, Cys115
- **CpG dinucleotides:** c.684C (Arg224), c.690C (Arg226), c.691G (Arg691), c.868G (Arg285) (PMID: 7668284)
- **WSxWS motif:** Trp237, Ser238, Glu239, Trp240, Ser241
- **Transmembrane domain residues** by introducing a charged or polar residue (Asn, Asp, Arg, Cys, His, Glu, Gln, Lys, Ser, Thr, Tyr): amino acids 263-283

**Caveat:** Variant must also meet PM2

| Strength | Criteria |
|----------|----------|
| **Strong (PM1_Strong)** | Defined to include IL2RG-specific hot spots and functional domains listed above. |

**Modification Type:** Gene-specific, Strength

---

### PM2 - Absent from Controls

**Original ACMG Summary:** Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

**Caveat:** Population data for indels may be poorly called by next generation sequencing.

**VCEP Specifications:**

**Downgraded to PM2_Supporting.**

- gnomAD popmax filtering allele frequency **<0.000124**
- Additional requirement that no hemizygotes have been observed in gnomAD

| Strength | Criteria |
|----------|----------|
| **Supporting (PM2_Supporting)** | gnomAD popmax filtering allele frequency <0.000124 AND no hemizygotes observed in gnomAD. |

**Modification Type:** Disease-specific, Strength

---

### PM3 - In Trans with Pathogenic

**Original ACMG Summary:** For recessive disorders, detected in trans with a pathogenic variant.

**Note:** This requires testing of parents (or offspring) to determine phase.

**VCEP Specifications:** **Not Applicable**

**Comments:** Does not apply. IL2RG-associated SCID is X-linked; this criterion is for recessive disorders.

---

### PM4 - Protein Length Changes

**Original ACMG Summary:** Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

**VCEP Specifications:**

When applied to deletion variants, the deleted region must contain a known pathogenic or likely pathogenic variant that is not predicted/observed to alter splicing in order to apply PM4 at the default strength or contain a variant of uncertain significance not predicted/observed to alter splicing in order to apply PM4 at the reduced strength of PM4_Supporting.

| Strength | Criteria |
|----------|----------|
| **Moderate (PM4)** | Deleted region must contain a known **pathogenic or likely pathogenic variant** that is not predicted/observed to alter splicing. |
| **Supporting (PM4_Supporting)** | Deleted region must contain a **variant of uncertain significance** that is not predicted/observed to alter splicing. |

**Modification Type:** General recommendation, Strength

---

### PM5 - Novel Missense at Same Residue

**Original ACMG Summary:** Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.

**Example:** Arg156His is pathogenic; now you observe Arg156Cys.

**Caveat:** Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:**

**For missense variants:**
- Applicable at default strength (PM5) if previously established variant is classified as pathogenic or at reduced strength of PM5_Supporting if previously established variant is classified as likely pathogenic.

**For nonsense variants:**

| Strength | Criteria |
|----------|----------|
| **Strong (PM5_Strong)** | PM5 may be applied at a Strong level of evidence for any nonsense variant with **4+ points** from informative variants (see point table below). PM5_Strong should be downgraded to PM5_Moderate if PVS1 is applied at any strength. |
| **Moderate (PM5_Moderate)** | PM5 may also be applied at a Moderate level of evidence for any nonsense variant with **2+ points** from informative variants (see point table below). PM5_Moderate may not be combined with PVS1_VeryStrong (should be downgraded to PM5_Supporting if PVS1_VeryStrong is applied). |
| **Supporting (PM5_Supporting)** | Also applicable to a nonsense variant with **1 point** from an informative variant (see point table). Informative variants must also be classified by these rule specifications. |

#### PM5 Point Table for Nonsense Variants

| Type of Variant Under Assessment (VUA) | Informative Variant | Score |
|----------------------------------------|---------------------|-------|
| Nonsense variant predicted to lead to NMD | P/LP variant in the exon of DNA change predicted to lead to NMD | +1 pt |
| Nonsense variant predicted to lead to NMD | B/LB variant in the exon predicted to lead to NMD | -2 pt |
| Nonsense variant, resulting in a PTC in the final exon, not predicted to lead to NMD | P/LP variant resulting in a PTC in the same exon but downstream of VUA | +1 pt |
| Nonsense variant, resulting in a PTC in the final exon, not predicted to lead to NMD | B/LB variant resulting in PTC in the same exon but upstream of the VUA | -2 pt |

**Notes:**
- NMD = nonsense-mediated decay; PTC = premature termination codon
- The informative variant must be classified by the SCID VCEP specifications and may not be the same variant used to meet "+1 pathogenic variant downstream" on the PVS1 flowchart
- If negative points are calculated, the curator should not apply PM5 and should reconsider if PVS1 is applicable for the VUA
- The VUA must be sufficiently rare, meet PM2_Supporting, to apply this point system
- If the informative variant is a frameshift or nonsense variant, it must reach classification as Pathogenic or Likely Pathogenic without use of PM5 and without use of only PVS1 plus PM2

**Modification Type:** General recommendation, Strength

---

### PM6 - De Novo (Assumed)

**Original ACMG Summary:** Assumed de novo, but without confirmation of paternity and maternity.

**VCEP Specifications:**

Same as PS2 - use point-based system above with the following guidelines for determining phenotypic consistency:

- **"Phenotype highly specific for gene":** proband must meet at least PP4_Moderate criteria
- **"Phenotype consistent with gene but not highly specific":** proband must meet PP4 criteria
- **"Phenotype consistent with gene but not highly specific and high genetic heterogeneity":** proband has been asserted to have a SCID phenotype but does not meet PP4 criteria
- Reduce points per proband by half if the phase is unconfirmed
- Unaffected carrier females must have an affected child and maternity and paternity must be confirmed

Use ClinGen SVI recommendations for de novo criteria. Phenotypic consistency determined using points-based system defined in PP4.

#### Evidence Strength Thresholds

| Points | Strength Level |
|--------|----------------|
| 0.5 | PM6_Supporting |
| 1.0 | PM6_Moderate |
| 2.0 | PM6_Strong |
| 4.0 | PM6_VeryStrong |

**Modification Type:** Disease-specific, Strength

---

### PP1 - Co-segregation

**Original ACMG Summary:** Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.

**Note:** May be used as stronger evidence with increasing segregation data.

**VCEP Specifications:**

Use ClinGen SVI recommendations for co-segregation criterion (PMID: 30311386).

Recommendation for determining the appropriate evidence strength level for PP1:

| Strength | Affected Segregations (not including proband) | Likelihood | LOD Score |
|----------|----------------------------------------------|------------|-----------|
| **Supporting (PP1)** | 2 affected segregations | 4:1 | 0.6 |
| **Moderate (PP1_Moderate)** | 4 affected segregations | 16:1 | 1.2 |
| **Strong (PP1_Strong)** | 5 affected segregations | 32:1 | 1.5 |

**Modification Type:** General recommendation, Strength

---

### PP2 - Missense in Constrained Gene

**Original ACMG Summary:** Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.

**VCEP Specifications:** **Not Applicable**

**Comments:** Does not apply. The gnomAD v2.1.1 missense Z score for IL2RG (Z = 1.49) suggests this gene is not constrained for missense variation. Both benign and pathogenic missense variants are present in IL2RG.

---

### PP3 - Computational Evidence

**Original ACMG Summary:** Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).

**Caveat:** As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Supporting (PP3)** | Only applicable to synonymous or intronic variants predicted to impact splicing by SpliceAI with a delta score **≥0.2**. |

**Important:** Do not apply to missense variants.

**Modification Type:** General recommendation

---

### PP4 - Phenotype Specificity

**Original ACMG Summary:** Patient's phenotype or family history is highly specific for a disease with a single genetic etiology.

**VCEP Specifications:**

PP4 applicability and strength is determined by the total points accumulated by a single affected individual according to the table below and the following total point ranges:

| Total Points | Strength |
|--------------|----------|
| <1 | PP4 not met |
| 1 to <2.5 | PP4 (Supporting) |
| 2.5 to <6 | PP4_Moderate |
| ≥6 | PP4_Strong* |

*CNV (Copy number variation) testing is required to consider PP4_Strong in order to certify that the variant in question is the causative for the phenotype, and not one CNV event corrected by gene therapy and not identified previously.

#### PP4 Point System

| Evidence Description | Points |
|---------------------|--------|
| Diagnostic criteria met for SCID (Criteria 1 and 3 or Criterion 4 by itself) or Leaky SCID/Omenn syndrome (excluding Criterion 2)** | 0.5 |
| SCID gene panel or exome/genome sequencing conducted (only applicable if genetic testing did not provide an alternative genetic explanation for SCID/Leaky SCID/Omenn syndrome phenotype) | 1 |
| Family history of SCID (only applicable if SCID gene panel or exome/genome sequencing was conducted on proband and did not provide an alternative genetic explanation for phenotype) | 0.5 |
| Absent CD132 expression (demonstrated by RT-PCR, Western blot, flow cytometry) | 4.5 |
| Reduced CD132 expression (demonstrated by RT-PCR, Western blot, or flow cytometry) as established by the laboratory | 3 |
| Reduced IL-2-induced phosphorylation of JAK3 or STAT5 in patient-derived cells as established by the laboratory AND pathogenic or likely pathogenic variants in JAK3, STAT5A, STAT5B, IL2RA, and IL2RB **have been excluded** (PMIDs: 10794431, 31799703, 32072341) | 3 |
| Reduced IL-2-induced phosphorylation of JAK3 or STAT5 in patient-derived cells as established by the laboratory AND pathogenic or likely pathogenic variants in JAK3, STAT5A, STAT5B, IL2RA, and IL2RB **have NOT been excluded** (PMIDs: 10794431, 31799703, 32072341) | 1.5 |
| Reduced IL-21-induced phosphorylation of STAT3 in total lymphocytes or B cells as established by the laboratory AND pathogenic or likely pathogenic variants in JAK3, STAT3, and IL21R **have been excluded** (PMIDs: 25042067, 32072341) | 3 |
| Reduced IL-21-induced phosphorylation of STAT3 in total lymphocytes or B cells as established by the laboratory AND pathogenic or likely pathogenic variants in JAK3, STAT3, and IL21R **have NOT been excluded** (PMIDs: 25042067, 32072341) | 1.5 |
| SCID phenotype corrected by IL2RG gene therapy **WITHOUT** CNV testing performed | 4.5 |
| SCID phenotype corrected by IL2RG gene therapy **WITH** CNV testing performed | 6 |
| T-B+ lymphocyte subset profile* (See notes) | 0.5 |
| NK cells below the normal reference range or absent | 1 |

**Notes:**
- **The diagnostic criteria should follow the PIDTC 2022 specification
- *Notes on lymphocyte profile:
  1. If NK cells are not noted or are present, criteria may still be applied if SCID gene panel or exome/genome sequencing has ruled out alternative causes
  2. If maternal T cells are present, the T lymphocyte profile is still considered to be T- (autologous T cells are absent)

**Modification Type:** Disease-specific, Gene-specific

---

### PP5 - Reputable Source

**Original ACMG Summary:** Reputable source recently reports variant as pathogenic, but the evidence is not available to the laboratory to perform an independent evaluation.

**VCEP Specifications:** **Not Applicable**

This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PMID: 29543229).

---

## Benign Criteria

### BA1 - Allele Frequency >5%

**Original ACMG Summary:** Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

**VCEP Specifications:**

Common in population databases.

| Strength | Criteria |
|----------|----------|
| **Stand Alone (BA1)** | gnomAD popmax filtering allele frequency **>0.01110** |

Maximum credible population allele frequency threshold determined using Whiffin/Ware calculator (https://www.cardiodb.org/allelefrequencyapp/) and the following parameters:
- Prevalence: 1:5,000
- Allelic heterogeneity: 1
- Genetic heterogeneity: 0.31 (based on the contribution of IL2RG variants to total SCID in the PIDTC 6901 cohort reported in Dvorak et al., 2019 (PMID: 30193840, Table 1): 30.8%, rounded to 31%)
- Penetrance: 50%

**Modification Type:** Disease-specific

---

### BS1 - Frequency Greater Than Expected

**Original ACMG Summary:** Allele frequency is greater than expected for disorder.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong (BS1)** | gnomAD popmax filtering allele frequency **>0.00249*** |

*Consider bottleneck populations

Maximum credible population allele frequency threshold determined using Whiffin/Ware calculator (https://www.cardiodb.org/allelefrequencyapp/) and the following parameters:
- Prevalence: 1:50,000
- Allelic heterogeneity: 1
- Genetic heterogeneity: 0.31 (based on the contribution of IL2RG variants to total SCID in the PIDTC 6901 cohort reported in Dvorak et al., 2019 (PMID: 30193840, Table 1): 30.8%, rounded to 31%)
- Penetrance: 100%

**Modification Type:** Disease-specific

---

### BS2 - Observed in Healthy Adult

**Original ACMG Summary:** Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong (BS2)** | Observed in **≥3 (3 or more) hemizygotes** in gnomAD. |
| **Supporting (BS2_Supporting)** | Can be applied at Supporting level of evidence if observed at least **2 hemizygotes** in gnomAD. |

**Modification Type:** Gene-specific, Strength

---

### BS3 - Functional Studies (No Effect)

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

**VCEP Specifications:** **Not Applicable**

**Comments:** Does not apply.

---

### BS4 - Lack of Segregation

**Original ACMG Summary:** Lack of segregation in affected members of a family.

**Caveat:** The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong (BS4)** | Can be applied without additional specifications. |

**Modification Type:** None

---

### BP1-BP7 - Benign Supporting

| Criterion | Status | Comment |
|-----------|--------|---------|
| **BP1** | Not Applicable | Does not apply. IL2RG missense variants are a known mechanism of disease. |
| **BP2** | Not Applicable | Does not apply. |
| **BP3** | Not Applicable | Does not apply. |
| **BP4** | Not Applicable | Does not apply. |
| **BP5** | Not Applicable | Does not apply. |
| **BP6** | Not Applicable | This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PMID: 29543229). |
| **BP7** | Applicable (Supporting) | Applicable to both synonymous variants and deep intronic variants affecting nucleotides at or beyond the +7 (donor) and -21 (acceptor) positions. The variant should be predicted not to impact splicing by at least two out of three in silico tools (freely available tools include GeneSplicer, MaxEntScan, NNSplice, SpliceAI, Splicing Sequences Finder (SSF), and varSEAK). Given the potential for poor conservation of genes related to T cell and B cell development among vertebrates, nucleotide conservation is **not required** in order to apply BP7. |

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
| 1 Strong (BS1, BS2, BS4) |
| ≥2 Supporting (BS2_Supporting, BP7) |

---

## Appendices

### Appendix A: PVS1 Flowchart

The PVS1 flowchart for IL2RG follows the ClinGen SVI recommendations (Tayoun et al., 2018; PMID: 30192042) with the following IL2RG-specific modifications:

**Nonsense or Frameshift:**
- **Predicted to undergo NMD:**
  - Exon present in biologically-relevant transcript(s) → **PVS1**
  - Exon absent from biologically-relevant transcript(s) → N/A
- **Not predicted to undergo NMD** (i.e. premature stop codon in the last exon or the last 50 nucleotides of the penultimate exon [c.874 (codon 292) in exon 7]):
  - Truncated/altered region is critical to protein function (causes truncation of the transmembrane domain which begins at amino acid 255 or any distal region i.e. cytoplasmic domain) → **PVS1**
  - Role of region in protein function is unknown:
    - LoF variants in this exon are frequent in general population and/or exon is absent from biologically-relevant transcript(s) → N/A
    - LoF variants not frequent and exon present:
      - Variant removes >10% of protein:
        - 1+ pathogenic variant present downstream → **PVS1_Strong**
        - No known downstream pathogenic variants → **PVS1_Moderate**
      - Variant removes <10% of protein → **PVS1_Moderate**

**GT-AG 1,2 splice sites:**
- Similar logic applies with considerations for exon skipping or cryptic splice site usage

**Deletion (Single exon to full gene):**
- Full gene deletion → **PVS1**
- Single to multi exon deletion with reading frame disruption and NMD prediction → **PVS1** (if exon present in biologically-relevant transcript(s))
- Preserves reading frame: same considerations as nonsense variants not predicted to undergo NMD

**Duplication (≥1 exon in size, completely contained within gene):**
- Proven in tandem with reading frame disruption and NMD predicted → **PVS1**
- Presumed in tandem with reading frame presumed disrupted and NMD predicted → **PVS1_Strong**
- Proven not in tandem or no/unknown impact on reading frame → N/A

**Initiation Codon:**
- No known alternative start codon in other transcripts:
  - ≥1 pathogenic variant(s) upstream of closest potential in-frame start codon → **PVS1_Moderate**
  - No pathogenic variant(s) upstream → **PVS1_Supporting**
- Different functional transcript uses alternative start codon → N/A

### Appendix B: Reference PMIDs

| PMID | Reference | Description |
|------|-----------|-------------|
| 30192042 | Tayoun et al., 2018 | ClinGen SVI recommendations for PVS1 |
| 30311386 | Oza et al., 2018 | ClinGen SVI recommendations for PP1 (co-segregation) |
| 29543229 | Biesecker et al., 2018 | ClinGen SVI recommendations on PP5/BP6 |
| 30193840 | Dvorak et al., 2019 | PIDTC SCID cohort data |
| 7668284 | CpG dinucleotide reference | PM1 specification |
| 9399950 | Sharfe et al., 1997 | PS3 functional assay (JAK3 phosphorylation, cytokine binding) |
| 9933465 | Kumaki et al., 1999 | PS3 functional assay (JAK3 association) |
| 7632950 | Kumaki et al., 1995 | PS3 functional assay (cytokine binding, surface expression) |
| 31799703 | Arcas-Garcia et al., 2020 | PS3 functional assay (JAK3 co-immunoprecipitation) |
| 32072341 | Tuovinen et al., 2020 | PS3 functional assay (BioID interaction profiling) |
| 10794431 | PP4 phosphorylation reference | IL-2-induced phosphorylation of JAK3/STAT5 |
| 25042067 | PP4 phosphorylation reference | IL-21-induced phosphorylation of STAT3 |

### Appendix C: Population Frequency Thresholds Summary

| Criterion | Threshold | Strength |
|-----------|-----------|----------|
| BA1 | >0.01110 | Stand Alone |
| BS1 | >0.00249 | Strong |
| PM2 | <0.000124 | Supporting |

### Appendix D: PS3/BS3 Approved Functional Assays

| PMID | Assay Type | Material Used | Readout | Approved | Strength |
|------|------------|---------------|---------|----------|----------|
| 9399950 | IL-2-induced Jak-3 phosphorylation assay | COS-7 cells transfected with wild type and variants | Presence/intensity of band corresponding to Jak3 tyrosine phosphorylation | Yes | PS3_Supporting |
| 9933465 | JAK3 association by immunoprecipitation | COS-1 transfected cells | Presence/intensity of band corresponding to Jak3 phosphorylation | Yes | PS3_Supporting |
| 31799703 | JAK3 association by immunoprecipitation | COS-7 cells with variant | Presence/intensity of band corresponding to Jak3 phosphorylation | Yes | PS3_Supporting |
| 9399950 | Cytokine binding | COS-7 cells transfected with wild type and variants | Binding change/protein interaction compared to wild type | Yes | PS3_Supporting |
| 7632950 | Cytokine binding | COS-7 cells cotransfected with IL-2 receptor constructs | Binding change/protein interaction compared to wild type | Yes | PS3_Supporting |
| 7632950 | Surface expression of the gamma chain | COS-7 transfected cells | Expression of the mutant chain by IL-2 receptor monoclonal antibody stained on cell surface | Yes | PS3_Supporting |
| 32072341 | Interaction profiling-BioID | HEK293 cells inducibly expressing wild type or variant IL2RG | Fold change in protein interaction compared to wild type | Yes | PS3_Supporting |

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 2.1.0 | 10/1/2025 | Updated: PM5_Strong, PM5_Moderate, PM5_Supporting, PM5 Instructions, PP4 attachment table updates, PP4 instructions edited for harmonization with attached PP4 Tables, Edited Likely Benign Rules for Combining Criteria (V1 had 1 strong, the change in V2 to 1 strong + 1 supporting was unintentional) |
| 2.0.0 | - | Previous version |
| 1.0.0 | - | Initial release |

---

*This document was compiled from ClinGen VCEP specifications and ClinGen SVI recommendations. For the most current version, please refer to the ClinGen website.*
