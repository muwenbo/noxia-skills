# ClinGen Severe Combined Immunodeficiency Disease VCEP Variant Interpretation Guidelines for FOXN1

**Version:** 2.2.0
**Released:** December 12, 2025
**Affiliation:** Severe Combined Immunodeficiency Disease VCEP
**Based on:** Richards et al., 2015 ACMG/AMP Guidelines

---

## Gene Information

| Attribute | Value |
|-----------|-------|
| **Gene** | FOXN1 (HGNC:12765) |
| **HGNC Name** | forkhead box N1 |
| **Transcript** | NM_001369369.1 |
| **Disease** | T-cell immunodeficiency, congenital alopecia, and nail dystrophy (MONDO:0011132) |
| **Inheritance** | Semidominant inheritance |

**General Comments:** All observations of FOXN1 variants may be curated under this single set of specifications and classified for T-cell immunodeficiency, congenital alopecia, and nail dystrophy with semidominant inheritance.

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

**VCEP Specifications:** See attached PVS1 flowchart. Use ClinGen SVI recommendations for loss of function criterion (Tayoun et al., 2018; PMID: 30192042).

#### Strength Levels

| Strength | Criteria |
|----------|----------|
| **Very Strong** | PVS1 can be applied to variants not predicted to undergo nonsense-mediated decay but removing/altering the critical **forkhead domain (amino acids 270-367)**; Newman et al., 2020; PMID: 31914405) based on recommendations from Walker et al., 2023 (PMID: 37352859). |
| **Strong** | For variants not predicted to undergo NMD but removing >10% of protein (i.e., variants in the last exon, exon 9, or variants in the last 50 nucleotides of the penultimate exon after c.1577, codon 526, in exon 8), at least one pathogenic variant must be present downstream. **OR** PVS1_Strong can be applied to variants not predicted to undergo NMD but removing/altering the **transactivation domain (amino acids 511-563)**; Schlake et al., 2000 PMID: 10767081). |
| **Moderate** | For variants not predicted to undergo NMD but removing >10% of protein (i.e., variants in the last exon, exon 9, or variants in the last 50 nucleotides of the penultimate exon after c.1577, codon 526, in exon 8), when at least one pathogenic variant is **not** present downstream, downgrade to PVS1_Moderate. |
| **Supporting** | Per SVI flowchart recommendations for specific variant types. |

#### Critical Functional Domains

| Domain | Amino Acid Range | Notes |
|--------|------------------|-------|
| Forkhead domain (DNA binding) | 270-367 | Critical functional domain |
| Transactivation domain | 511-563 | Critical functional domain |

#### NMD Prediction Note
Variants creating a premature stop codon in the last exon or the last 50 nucleotides of the penultimate exon (c.1577, codon 526, in exon 8) are **not** predicted to undergo nonsense-mediated decay.

---

### PS1 - Same Amino Acid Change

**Original ACMG Summary:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.

**Example:** Val->Leu caused by either G>C or G>T in the same codon.

**Caveat:** Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | Applicable for a same amino acid change if previously established variant is classified as **Pathogenic** by SCID VCEP specifications for FOXN1. Can also be applied for variants with the same predicted splicing event as a known Pathogenic variant (see PS1 Splice table below). |
| **Moderate** | Applicable for a same amino acid change if previously established variant is classified as **Likely Pathogenic** by SCID VCEP specifications for FOXN1. Can also be applied for variants with the same predicted splicing event as a known (Likely) Pathogenic variant (see PS1 Splice table below). |
| **Supporting** | Can be applied for variants with the same predicted splicing event as a known (Likely) Pathogenic variant (see PS1 Splice table below). |

#### PS1 Splice Code Weights (from PMID: 37352859, Table 2)

| Variant Under Assessment (VUA) | Baseline Code | Position of Comparison Variant | With P Variant | With LP Variant |
|--------------------------------|---------------|--------------------------------|----------------|-----------------|
| Located outside splice donor/acceptor +/-1,2 positions | PP3 | same nucleotide | PS1 | PS1_Moderate |
| Located outside splice donor/acceptor +/-1,2 positions | PP3 | within same splice donor/acceptor motif (including at +/-1,2 positions) | PS1_Moderate | PS1_Supporting |
| Located at splice donor/acceptor +/-1,2 positions | PVS1 | within same splice donor/acceptor +/-1,2 dinucleotide | PS1_Supporting | N/A |
| Located at splice donor/acceptor +/-1,2 positions | PVS1 | within same splice donor/acceptor region, but outside +/-1,2 dinucleotide | PS1_Supporting | PS1_Supporting |
| Located at splice donor/acceptor +/-1,2 positions | PVS1_Strong, PVS1_Moderate, or PVS1_Supporting | within same splice donor/acceptor +/-1,2 dinucleotide | PS1 | N/A |
| Located at splice donor/acceptor +/-1,2 positions | PVS1_Strong, PVS1_Moderate, or PVS1_Supporting | within same splice donor/acceptor motif, but outside +/-1,2 dinucleotide | PS1_Moderate | PS1_Supporting |

**Prerequisites for PS1 Splice Application:**
- The predicted event of the VUA must precisely match the predicted event of the comparison (likely) pathogenic variant (e.g., both predicted to lead to exon skipping, or both to lead to enhanced use of a cryptic splice motif)
- The strength of the prediction for the VUA must be of similar or higher strength than the strength of the prediction for the comparison (likely) pathogenic variant
- For GT-AG introns: donor motif = last 3 bases of exon + 6 nucleotides of intronic sequence; acceptor motif = first base of exon + 20 nucleotides upstream from exon boundary

---

### PS2 - De Novo (Confirmed)

**Original ACMG Summary:** De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.

**Note:** Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.

**VCEP Specifications:** Use ClinGen SVI recommendations for de novo criteria (PMID: 30311386).

**Phenotypic Consistency Guidelines for FOXN1:**
- **"Phenotype highly specific for gene"**: proband must meet PP4_Moderate criteria
- **"Phenotype consistent with gene but not highly specific"**: proband must meet PP4 criteria
- **"Phenotype consistent with gene but not highly specific and high genetic heterogeneity"**: proband does not meet PP4 criteria but has at least one of three core FOXN1 deficiency features (Congenital alopecia, Nail dystrophy, T lymphopenia)

#### PS2/PM6 Point System (Per Proband)

| Phenotypic Consistency | De Novo with Confirmed Parental Relationships | De Novo with Unconfirmed Parental Relationships |
|------------------------|----------------------------------------------|------------------------------------------------|
| Phenotype highly specific for gene | 2 points | 1 point |
| Phenotype consistent with gene but not highly specific | 1 point | 0.5 points |
| Phenotype consistent with gene but not highly specific and high genetic heterogeneity | 0.5 points | 0.25 points |
| Phenotype not consistent with gene | 0 points | 0 points |

*Note: Maximum allowable value of 1 may contribute to overall score for the "high genetic heterogeneity" category*

#### Evidence Strength Thresholds

| Total Points | Strength Level |
|--------------|----------------|
| 0.5 | PS2_Supporting / PM6_Supporting |
| 1.0 | PS2_Moderate / PM6 |
| 2.0 | PS2 (Strong) / PM6_Strong |
| 4.0 | PS2_VeryStrong / PM6_VeryStrong |

---

### PS3 - Functional Studies

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.

**Note:** Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | PS3 may be applied at the strong level for evidence from an **animal model** expressing the variant of interest and recapitulating FOXN1 deficiency (i.e., a mouse model with T cell lymphopenia). |
| **Moderate** | PS3 may be applied at the moderate level based on a **luciferase assay** showing reduced (<50%) activity, as part of a **validated assay** with pathogenic and benign controls (PMID: 37419334). |
| **Supporting** | PS3 may be applied at the supporting level based on a **luciferase assay**, without sufficient validation controls, showing reduced (<50%) activity, such as those reported in PMIDs: 31566583, 33464451, 34860543. |

#### Approved Luciferase Assay Specifications

| Parameter | Validated Assay (PS3_Moderate) | Non-validated Assays (PS3_Supporting) |
|-----------|-------------------------------|---------------------------------------|
| **PMID** | Manuscript in press (van Oers) | 31566583, 33464451, 34860543 |
| **Assay Type** | Luciferase reporter (Psmb11/beta5t promoter) | Luciferase reporter (beta5t promoter) |
| **Cell Lines** | HEK 293T or 4D6 cells | HEK 293T or 4D6 cells |
| **Validation Controls (P/LP)** | 10 | Not sufficient |
| **Validation Controls (B/LB)** | 5 | Not sufficient |
| **Threshold for Normal** | >75% WT activity | >75% WT activity |
| **Threshold for Abnormal** | <50% WT activity | <50% WT activity |

#### Validation Control Data (Unpublished, van Oers)

**Benign/Likely Benign Controls (>75% WT):**
| Variant | Activity (%WT) |
|---------|----------------|
| P430S | 92% |
| R69C | 91% |
| A121V | 89% |
| G238D | 105% |
| P230R | 103% |
| P242S | 85% |
| S339D | 83% |
| P350L | 88% |
| E359K | 112% |
| G523R | 84% |
| G543E | 107% |

**Pathogenic/Likely Pathogenic Controls (<50% WT):**
| Variant | Activity (%WT) |
|---------|----------------|
| V294I | 18% |
| R320W | 2% |
| H321N | 5% |
| L325P | 1.5% |
| E303Sfs247 | 1.2% |
| T313fsX169 | 0.9% |
| P401Afs144 | 1.4% |
| P432fs118 | 0.4% |
| Y455CfsX94 | 1.6% |
| H457Pfs93 | 0.6% |

---

### PS4 - Prevalence in Affected

**Original ACMG Summary:** The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.

**VCEP Specifications:** Evaluate each unrelated **heterozygous** affected individual with the Affected Observations Scoring Guide and sum points across all probands.

**Caveats:**
- Exclude the proband used to satisfy the PP4 criteria
- Variant must be sufficiently rare (meet PM2_Supporting specification)

#### PS4 Evidence Strength Thresholds

| Total Points | Strength Level |
|--------------|----------------|
| 1-1.75 | PS4_Supporting |
| 2-3.75 | PS4 (Moderate) |
| 4-7.75 | PS4_Strong |
| >=8 | PS4_VeryStrong |

#### PS4 Scoring Guide (Heterozygous Probands)

| Phenotype Consistency | Points |
|-----------------------|--------|
| Phenotype specific with gene (meets PP4) AND all relevant genes tested (SCID gene panel or exome/genome sequencing), with no other variant of interest | +1.0 point |
| Phenotype specific with gene (meets PP4) but NOT all relevant genes tested, and/or more than one variant of interest | +0.5 point |
| Phenotype consistent with gene (has at least one core feature, see PP4) AND all relevant genes tested, with no other variant of interest | +0.5 point |
| Phenotype consistent with gene (has at least one core feature, see PP4) but NOT all relevant genes tested, and/or more than one variant of interest | +0.25 point |
| Phenotype not consistent with gene | +0 point |

---

### PM1 - Mutational Hot Spot

**Original ACMG Summary:** Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Moderate** | Applicable for variants in the **DNA binding forkhead domain (amino acids 270-367)**, which is a well-established functional domain (Newman et al., 2020; PMID: 31914405) of FOXN1 with low tolerance for benign variation. |

---

### PM2 - Absent from Controls

**Original ACMG Summary:** Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

**Caveat:** Population data for indels may be poorly called by next generation sequencing.

**VCEP Specifications:** This value is based on the HMAF of NM_001369369.1(FOXN1):c.1585del (p.Leu529fs), the most common pLOF variant present in gnomADv4.0.0 that classifies as Pathogenic based on specified guidelines.

| Strength | Criteria |
|----------|----------|
| **Supporting** | gnomAD Grpmax filtering allele frequency **<=0.00002412** |

---

### PM3 - In Trans with Pathogenic

**Original ACMG Summary:** For recessive disorders, detected in trans with a pathogenic variant.

**Note:** This requires testing of parents (or offspring) to determine phase.

**VCEP Specifications:** Evaluate each unrelated **homozygous or compound heterozygous** affected individual with the Affected Observations Scoring Guide and sum points across all probands.

**Caveats:**
- The co-occurring variant must be classified using the SCID VCEP specifications for FOXN1
- Variants must be sufficiently rare (meet PM2_Supporting specification)

#### PM3 Evidence Strength Thresholds

| Total Points | Strength Level |
|--------------|----------------|
| 1-1.75 | PM3_Supporting |
| 2-3.75 | PM3 (Moderate) |
| 4-7.75 | PM3_Strong |
| >=8 | PM3_VeryStrong |

#### PM3 Scoring Guide (Homozygous/Compound Heterozygous Probands)

| Phenotype Consistency | VBC Confirmed in Trans with P/LP | VBC Assumed in Trans with P/LP | VBC Confirmed in Trans with VUS | VBC Homozygous |
|-----------------------|----------------------------------|--------------------------------|--------------------------------|----------------|
| Phenotype specific (meets PP4) + all genes tested, no other variant | +2.0 | +1.5 | +1.0 | +1.0 |
| Phenotype specific (meets PP4) but not all genes tested, and/or >1 variant of interest | +1.0 | +0.75 | +0.5 | +0.5 |
| Phenotype consistent (>=1 core feature) + all genes tested, no other variant | +0.5 | +0.5 | +0.5 | +0.5 |
| Phenotype consistent (>=1 core feature) but not all genes tested, and/or >1 variant of interest | +0.25 | +0.25 | +0.25 | +0.25 |
| Phenotype not consistent with gene | +0 | +0 | +0 | +0 |

*VBC = Variant Being Curated*

---

### PM4 - Protein Length Changes

**Original ACMG Summary:** Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Moderate** | Additional requirement that when applied to deletion variants, the deleted region must contain a known **Pathogenic or Likely Pathogenic** variant that is not predicted/observed to alter splicing. |
| **Supporting** | Additional requirement that when applied to deletion variants, the deleted region must contain a known **VUS** variant that is not predicted/observed to alter splicing. |

---

### PM5 - Novel Missense at Same Residue

**Original ACMG Summary:** Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.

**Example:** Arg156His is pathogenic; now you observe Arg156Cys.

**Caveat:** Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:**

**For Missense Variants:**
- **PM5 (Moderate)**: Applicable at default strength if previously established variant is classified as **Pathogenic**
- **PM5_Supporting**: Applicable if previously established variant is classified as **Likely Pathogenic**

**For Nonsense Variants - Point-Based System:**

| Type of Variant Under Assessment (VUA) | Informative Variant | Score |
|----------------------------------------|---------------------|-------|
| Nonsense variant predicted to lead to NMD | P/LP variant in the exon of DNA change predicted to lead to NMD | +1 pt |
| Nonsense variant predicted to lead to NMD | B/LB variant in the exon predicted to lead to NMD | -2 pt |
| Nonsense variant in final exon, not predicted to lead to NMD | P/LP variant resulting in PTC in same exon but downstream of VUA | +1 pt |
| Nonsense variant in final exon, not predicted to lead to NMD | B/LB variant resulting in PTC in same exon but upstream of VUA | -2 pt |

*NMD = nonsense-mediated decay; PTC = premature termination codon*

#### PM5 Strength Levels for Nonsense Variants

| Total Points | Strength | Notes |
|--------------|----------|-------|
| 1 | PM5_Supporting | - |
| >=2 | PM5_Moderate | May not be combined with PVS1_VeryStrong (downgrade to PM5_Supporting) |
| >=4 | PM5_Strong | Should be downgraded to PM5_Moderate if PVS1 is applied at any strength |

**Important Notes:**
- The informative variant must be classified by the SCID VCEP specifications
- May not be the same variant used to meet "+1 pathogenic variant downstream" on the PVS1 flowchart
- If negative points are calculated, do not apply PM5 and reconsider if PVS1 is applicable
- The VUA must be sufficiently rare (meet PM2_Supporting)
- If the informative variant is a frameshift or nonsense variant, it must reach classification as P/LP without use of PM5 and without use of only PVS1 plus PM2

---

### PM6 - De Novo (Assumed)

**Original ACMG Summary:** Assumed de novo, but without confirmation of paternity and maternity.

**VCEP Specifications:** Same as PS2 - use point-based system above. See [PS2 - De Novo (Confirmed)](#ps2---de-novo-confirmed) for details.

**Phenotypic Consistency Guidelines for FOXN1:**
- **"Phenotype highly specific for gene"**: proband must meet PP4_Moderate criteria
- **"Phenotype consistent with gene but not highly specific"**: proband must meet PP4 criteria
- **"Phenotype consistent with gene but not highly specific and high genetic heterogeneity"**: proband does not meet PP4 criteria but has at least one of three core FOXN1 deficiency features

---

### PP1 - Co-segregation

**Original ACMG Summary:** Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.

**Note:** May be used as stronger evidence with increasing segregation data.

**VCEP Specifications:** The estimated LOD (Z) score is calculated as follows:

**Z = log10{1/[(0.25)^x (0.5)^y]}**

Where:
- **x** = number of affected relatives with at least one core feature (see PP4) harboring **biallelic** FOXN1 variants (confirmed by genetic analysis), not including the proband
- **y** = number of affected relatives with at least one core feature (see PP4) harboring a **heterozygous** FOXN1 variant (confirmed by genetic analysis or an obligate carrier), not including the proband

#### PP1 Strength Thresholds

| Strength | Likelihood Ratio | LOD Score |
|----------|------------------|-----------|
| Supporting | 4:1 | 0.6 to <1.2 |
| Moderate | 16:1 | 1.2 to <1.5 |
| Strong | 32:1 | >=1.5 |

---

### PP2 - Missense in Constrained Gene

**Original ACMG Summary:** Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.

**VCEP Specifications:**

| Status | Comment |
|--------|---------|
| **Not Applicable** | Does not apply. FOXN1 does not have a low rate of benign missense variation, with a missense constraint score of Z=0.66. |

---

### PP3 - Computational Evidence

**Original ACMG Summary:** Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).

**Caveat:** As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Moderate** | REVEL score **>=0.932** (downgraded from Strong per Pejaver et al., 2022; PMID: 36413997) |
| **Supporting** | REVEL score **>=0.644** (to <0.932) based on Pejaver et al., 2022 (PMID: 36413997). **OR** Missense, synonymous, or intronic variants predicted to impact splicing by **SpliceAI delta score >=0.2** |

---

### PP4 - Phenotype Specificity

**Original ACMG Summary:** Patient's phenotype or family history is highly specific for a disease with a single genetic etiology.

**VCEP Specifications:** PP4 applicability and strength is determined by the total points accumulated by a single affected individual according to the list below:

#### PP4 Point System

**Core Features:**

| Feature | Points |
|---------|--------|
| Congenital, or early-onset, alopecia or absent eyebrows | 0.25 |
| Nail dystrophy | 0.25 |
| Absent/very low T cell number of <0.05x10^9/L | 0.5 |
| **OR if >0.05x10^9/L, then:** | |
| - Low T cell number for age 0.05-1.0x10^9/L OR T- B+ [NK+]* SCID OR Poor/absent proliferative response to phytohemagglutinin (PHA) | 0.25 |
| - Abnormal TRECs OR <20% of CD4+ T cells are naive (via CD3/CD4/CD45RA, or with additional naive markers) OR low CD8+ T cell number relative to age-matched controls | 0.25 |

**Additional Features:**

| Feature | Points |
|---------|--------|
| Development of T cells in an artificial thymic organoid (ATO) system | 0.25 |
| Transplant of thymic tissue corrects T cell deficiency | 0.5 |
| SCID gene panel or exome/genome sequencing, with no other variant of interest reported | 0.5 |

*\*Absent NK cells would not be consistent with a FOXN1 specific phenotype, however if absence/presence of NK cells is not noted, points may still be awarded if SCID gene panel or exome/genome sequencing has ruled out alternative causes*

#### PP4 Strength Thresholds

| Total Points | Strength |
|--------------|----------|
| <1 | PP4 not met |
| 1 to <2 | PP4 (Supporting) |
| >=2 | PP4_Moderate |

---

### PP5 - Reputable Source

**Original ACMG Summary:** Reputable source recently reports variant as pathogenic, but the evidence is not available to the laboratory to perform an independent evaluation.

**VCEP Specifications:**

| Status | Comment |
|--------|---------|
| **Not Applicable** | This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PMID: 29543229). |

---

## Benign Criteria

### BA1 - Allele Frequency >5%

**Original ACMG Summary:** Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

**VCEP Specifications:** Maximum credible population allele frequency threshold determined using Whiffin/Ware calculator (https://www.cardiodb.org/allelefrequencyapp/) and the following parameters:
- Prevalence: 1:5,000
- Allelic heterogeneity: 1
- Genetic heterogeneity: 0.01
- Penetrance: 10%

| Strength | Criteria |
|----------|----------|
| **Stand Alone** | gnomAD Grpmax filtering allele frequency **>0.00447** |

---

### BS1 - Frequency Greater Than Expected

**Original ACMG Summary:** Allele frequency is greater than expected for disorder.

**VCEP Specifications:** Maximum credible population allele frequency threshold determined using Whiffin/Ware calculator (https://www.cardiodb.org/allelefrequencyapp/) and the following parameters:
- Prevalence: 1:50,000
- Allelic heterogeneity: 1
- Genetic heterogeneity: 0.01
- Penetrance: 10%

| Strength | Criteria |
|----------|----------|
| **Strong** | gnomAD Grpmax filtering allele frequency **>0.00141** OR a bottle-necked population with MAF >0.00141 may be used. **Caveat:** If the variant is known to be a founder variant in the bottle-necked population, do not consider the frequency in that population for BS1. |

---

### BS2 - Observed in Healthy Adult

**Original ACMG Summary:** Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

**VCEP Specifications:**

| Status | Comment |
|--------|---------|
| **Not Applicable** | Does not apply due to reduced penetrance. |

---

### BS3 - Functional Studies (No Effect)

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

**VCEP Specifications:**

| Status | Comment |
|--------|---------|
| **Not Applicable** | There is not a well-established functional study which can rule out all damaging effects on protein function. |

---

### BS4 - Lack of Segregation

**Original ACMG Summary:** Lack of segregation in affected members of a family.

**Caveat:** The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.

| Strength | Criteria |
|----------|----------|
| **Strong** | Use with default ACMG recommendations (no modification). |

---

### BP1-BP7 - Benign Supporting

| Criterion | Status | Comment |
|-----------|--------|---------|
| **BP1** | Not Applicable | Does not apply. |
| **BP2** | Supporting | Applicable only when observed **in cis** with a pathogenic variant in any inheritance pattern, with the additional requirement that the co-occurring variant must be classified using the SCID VCEP specifications for FOXN1. |
| **BP3** | Not Applicable | Does not apply. |
| **BP4** | Supporting | REVEL score **<0.290** based on Pejaver et al., 2022 (PMID: 36413997). **OR** Synonymous or intronic variants not predicted to impact splicing by **SpliceAI delta score <=0.1** |
| **BP5** | Supporting | Use with no specification. |
| **BP6** | Not Applicable | This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PMID: 29543229). |
| **BP7** | Supporting | A synonymous variant, or deep intronic variant affecting nucleotides at or beyond the +7 (donor) and -21 (acceptor) positions, for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site (**SpliceAI delta score <=0.1**) AND the nucleotide is not highly conserved. |

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
| 1 Very Strong (PVS1, PS2_VeryStrong, PS4_VeryStrong, PM3_VeryStrong) **AND** 1 Supporting (PS1_Supporting, PS2_Supporting, PS3_Supporting, PS4_Supporting, PM2_Supporting, PM3_Supporting, PM4_Supporting, PM5_Supporting, PM6_Supporting, PP1, PP3, PP4) |

### Benign Classification

| Criteria Combination |
|---------------------|
| >=2 Strong |
| 1 Stand Alone (BA1) |

### Likely Benign Classification

| Criteria Combination |
|---------------------|
| 1 Strong (BS1, BS4) |
| >=2 Supporting (BP2, BP4, BP5, BP7) |

---

## Appendices

### Appendix A: PVS1 Flowchart

```
FOXN1 PVS1 Decision Tree

1. NONSENSE OR FRAMESHIFT
   |
   +-- Predicted to undergo NMD?
   |   |
   |   +-- YES --> Exon present in biologically-relevant transcript(s)?
   |   |           |
   |   |           +-- YES --> PVS1
   |   |           +-- NO --> N/A
   |   |
   |   +-- NO (PTC in last exon or last 50nt of penultimate exon [c.1577, codon 526, exon 8])
   |       |
   |       +-- Occurs within forkhead domain (aa 270-367)? --> PVS1
   |       +-- Occurs within transactivation domain (aa 511-563)? --> PVS1_Strong
   |       +-- Removes >10% of protein?
   |           |
   |           +-- YES --> 1+ pathogenic variant downstream? --> PVS1_Strong
   |           |           No downstream P variant? --> PVS1_Moderate
   |           +-- NO (<10%) --> Role of region known?
   |               |
   |               +-- Critical region --> PVS1_Strong or PVS1_Moderate
   |               +-- Unknown --> 1+ P variant downstream? --> PVS1_Moderate

2. CANONICAL SPLICE SITES (GT-AG, +/-1,2)
   |
   +-- Exon skipping/cryptic splice disrupts reading frame + NMD predicted?
   |   |
   |   +-- YES --> Exon present in biologically-relevant transcript(s)?
   |   |           |
   |   |           +-- YES --> PVS1
   |   |           +-- NO --> N/A
   |   |
   |   +-- NO (preserves reading frame or no NMD)
   |       |
   |       +-- Evaluate based on region affected (see nonsense criteria above)

3. SINGLE/MULTI-EXON DELETION
   |
   +-- Disrupts reading frame + NMD predicted?
   |   |
   |   +-- YES --> Exon present in biologically-relevant transcript(s)?
   |   |           |
   |   |           +-- YES --> PVS1
   |   |           +-- NO --> N/A
   |   |
   |   +-- NO (preserves reading frame or no NMD)
   |       |
   |       +-- Evaluate based on region affected

4. FULL GENE DELETION --> PVS1

5. DUPLICATION (>=1 exon, completely within gene)
   |
   +-- Proven in tandem + reading frame disrupted + NMD? --> PVS1
   +-- Presumed in tandem + reading frame disrupted + NMD? --> PVS1_Strong
   +-- Proven not in tandem or unknown impact --> N/A

6. INITIATION CODON
   |
   +-- Different functional transcript uses alternative start? --> PVS1_Supporting
   +-- No known alternative start?
       |
       +-- >=1 pathogenic variant upstream of closest in-frame start (Met28)? --> PVS1_Moderate
       +-- No P variant upstream? --> N/A
```

### Appendix B: Population Frequency Thresholds Summary

| Criterion | Threshold | Strength | Database |
|-----------|-----------|----------|----------|
| BA1 | >0.00447 | Stand Alone | gnomAD Grpmax FAF |
| BS1 | >0.00141 | Strong | gnomAD Grpmax FAF |
| PM2 | <=0.00002412 | Supporting | gnomAD Grpmax FAF |

### Appendix C: Critical Domains Summary

| Domain | Amino Acid Range | Significance |
|--------|------------------|--------------|
| Forkhead domain (DNA binding) | 270-367 | Critical functional domain; PM1 applicable; PVS1 for variants removing/altering this region |
| Transactivation domain | 511-563 | Critical functional domain; PVS1_Strong for variants removing/altering this region |

### Appendix D: Reference PMIDs

| PMID | Reference | Relevance |
|------|-----------|-----------|
| 30192042 | Tayoun et al., 2018 | ClinGen SVI recommendations for PVS1 |
| 31914405 | Newman et al., 2020 | Forkhead domain definition (aa 270-367) |
| 37352859 | Walker et al., 2023 | SVI recommendations for PS1 splice variants |
| 10767081 | Schlake et al., 2000 | Transactivation domain definition (aa 511-563) |
| 30311386 | Jarvik & Browning, 2016 | Co-segregation LOD score recommendations |
| 36413997 | Pejaver et al., 2022 | REVEL score thresholds for PP3/BP4 |
| 29543229 | Biesecker et al., 2018 | Recommendation against PP5/BP6 |
| 37419334 | van Oers et al., 2023 | Validated luciferase assay |
| 31566583 | Du et al., 2019 | Luciferase assay (non-validated) |
| 33464451 | Giardino et al., 2021 | Luciferase assay (non-validated) |
| 34860543 | Rota et al., 2021 | Luciferase assay (non-validated) |

---

## Version History

| Version | Date | Notes |
|---------|------|-------|
| 2.2.0 | 12/12/2025 | PM5 Specification Updates. Edited Likely Benign Rules for Combining Criteria (V1 had 1 strong, V2 change to 1 strong + 1 supporting was unintentional). Edited Likely Pathogenic Rules for Combining Criteria (V1 had 1 Very Strong + 1 Supporting code, accidentally removed during version change; added back). |
| 2.1.0 | - | Previous version |
| 1.0.0 | - | Initial release |

---

*This document was compiled from ClinGen VCEP specifications and ClinGen SVI recommendations. For the most current version, please refer to the ClinGen website.*
