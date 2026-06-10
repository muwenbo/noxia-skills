# ClinGen Glaucoma Expert Panel Variant Interpretation Guidelines for CYP1B1

**Version:** 1.0.0
**Released:** 11/6/2025
**Affiliation:** Glaucoma VCEP
**Type:** Tavtigian et al., 2020 - Bayesian adaptation of Richards et al., 2015
**Based on:** Richards et al., 2015 ACMG/AMP Guidelines

---

## Gene Information

| Attribute | Value |
|-----------|-------|
| **Gene** | CYP1B1 (HGNC:2597) |
| **HGNC Name** | cytochrome P450 family 1 subfamily B member 1 |
| **Transcript** | NM_000104.4 |
| **Disease** | CYP1B1-related glaucoma with or without anterior segment dysgenesis (MONDO:0800472) |
| **Inheritance** | Autosomal recessive inheritance |

### Gene Structure Overview

- CYP1B1 primary transcript (NM_000104.4) consists of 5,218 bp and encodes a 543 amino acid protein
- Contains 3 exons, although only exons 2 and 3 are coding
- CYP1B1 variants cause the phenotype through a **loss of function (LoF)** disease mechanism
- NMD is predicted to be activated for nonsense or frameshift variants where the premature termination codon is prior to amino acid 330 (last 50bp of exon 2)
- The **haem-binding domain** (aa460-493, located in exon 3) is vital for CYP1B1 enzymatic activity

---

## Table of Contents

1. [Pathogenic Criteria](#pathogenic-criteria)
   - [PVS1 - Null Variant](#pvs1---null-variant)
   - [PS1 - Same Amino Acid Change](#ps1---same-amino-acid-change)
   - [PS2 - De Novo](#ps2---de-novo)
   - [PS3 - Functional Studies](#ps3---functional-studies)
   - [PS4 - Prevalence in Affected](#ps4---prevalence-in-affected)
   - [PM1 - Mutational Hot Spot/Critical Domain](#pm1---mutational-hot-spotcritical-domain)
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
3. [Point-Based Classification System](#point-based-classification-system)
4. [Rules for Combining Criteria](#rules-for-combining-criteria)
5. [Appendices](#appendices)

---

## Pathogenic Criteria

### PVS1 - Null Variant

**Original ACMG Summary:** Null variant (nonsense, frameshift, canonical +/-1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.

**Caveats:**
- Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7)
- Use caution interpreting LOF variants at the extreme 3' end of a gene
- Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact
- Use caution in the presence of multiple transcripts

**VCEP Specifications:**

Use CYP1B1 decision tree for PVS1 (see Appendix A) adapted from Abou Tayoun et al.

**Key Considerations:**
- The haem-binding domain is considered vital for CYP1B1 enzymatic activity and the biological effect of removing the haem-binding domain is equivalent to NMD
- Truncating variants that are predicted to escape NMD but remove the haem-binding domain can meet PVS1
- There are no LoF variants in gnomAD after the end of haem-binding domain at residue 493
- There are no other biologically relevant transcripts of this gene

#### PVS1 Strength Levels by Variant Type

##### Nonsense or Frameshift Variants

| Condition | Strength |
|-----------|----------|
| Predicted to undergo NMD (aa1-330) | **PVS1** (Very Strong) |
| Not predicted to undergo NMD BUT removes haem-binding domain (aa1-493) | **PVS1** (Very Strong) |
| Does NOT remove haem-binding domain (aa494-Ter) | **PVS1_Moderate** |

##### GT-AG 1,2 Splice Site Variants

| Condition | Strength |
|-----------|----------|
| Exon skipping/intron inclusion/cryptic splice site disrupts reading frame AND predicted to undergo NMD (aa1-330) | **PVS1** (Very Strong) |
| Exon skipping/cryptic splice site disrupts reading frame prior to haem domain (aa331-493) | **PVS1** (Very Strong) |
| Exon skipping/cryptic splice site alters reading frame after haem domain (aa494-Ter) | **PVS1_Moderate** |

##### Deletions

| Condition | Strength |
|-----------|----------|
| Full gene deletion | **PVS1_SA** (Stand Alone) |
| Removes exon 2 and/or exon 3 (disrupts reading frame and removes/alters haem-binding domain aa460-493) | **PVS1** (Very Strong) |
| Removes exon 1 only (no alteration to reading frame or haem-binding domain) | **PVS1_Supporting** |

##### Duplications (≥1 exon and completely contained within the gene)

| Condition | Strength |
|-----------|----------|
| Reading frame disrupted and NMD predicted (aa1-330) AND **proven in tandem** | **PVS1** (Very Strong) |
| Reading frame in haem domain disrupted, no NMD predicted (aa331-493) AND **proven in tandem** | **PVS1** (Very Strong) |
| Reading frame disrupted after haem domain (aa494-Ter) AND **proven in tandem** | **PVS1_Moderate** |
| Reading frame disrupted and NMD predicted (aa1-330) AND **presumed in tandem** | **PVS1_Strong** |
| Reading frame in haem domain disrupted, no NMD predicted (aa331-493) AND **presumed in tandem** | **PVS1_Strong** |
| Reading frame disrupted after haem domain (aa494-Ter) AND **presumed in tandem** | **PVS1_Supporting** |
| No impact on reading frame OR proven not in tandem | N/A |

##### Initiation Codon Variants

| Condition | Strength |
|-----------|----------|
| No known alternative start codon in other transcripts AND ≥1 pathogenic variant upstream of closest potential in-frame start codon | **PVS1_Moderate** |
| Different functional transcript uses alternative start codon | N/A |

#### PVS1 Default Point Values

| Strength | Points |
|----------|--------|
| PVS1_SA (Stand Alone) | Stand Alone for Pathogenic |
| PVS1 (Very Strong) | 8 |
| PVS1_Strong | 4 |
| PVS1_Moderate | 2 |
| PVS1_Supporting | 1 |

---

### PS1 - Same Amino Acid Change

**Original ACMG Summary:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.

**Caveat:** Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:**
- The combination of PP3, PM1 and PS1 should not be higher than 6 points
- This rule does not apply to initiation codons

#### Strength Levels

| Strength | Criteria | Points |
|----------|----------|--------|
| **Strong** | For missense variants that do not affect splicing (SpliceAI ≤ 0.2): same amino acid change as a previously established **pathogenic** variant. For variants that affect splicing (SpliceAI > 0.2), refer to Table 3. | 4 |
| **Moderate** | For missense variants that do not affect splicing (SpliceAI ≤ 0.2): same amino acid change as a previously established **likely pathogenic** variant. For variants that affect splicing (SpliceAI > 0.2), refer to Table 3. | 2 |
| **Supporting** | For variants that affect splicing (SpliceAI > 0.2), refer to Table 3. | 1 |

#### Table 3: PS1 Code Weights for Variants with Same Predicted Splicing Event

| Variant under assessment (VUA) | Baseline computational/predictive code applicable to VUA | Position of comparison variant relative to VUA | PS1 code with P comparison variant | PS1 code with LP comparison variant |
|-------------------------------|----------------------------------------------------------|------------------------------------------------|-----------------------------------|-------------------------------------|
| Located outside splice donor/acceptor ± 1,2 dinucleotide positions | PP3 | same nucleotide | PS1 | PS1_Moderate |
| Located outside splice donor/acceptor ± 1,2 dinucleotide positions | PP3 | within same splice donor/acceptor motif (including at ± 1,2 positions) | PS1_Moderate | PS1_Supporting |
| Located at splice donor/acceptor PVS1 ± 1,2 dinucleotide positions | PVS1 | within same splice donor/acceptor ± 1,2 dinucleotide | PS1_Supporting | N/A |
| Located at splice donor/acceptor PVS1 ± 1,2 dinucleotide positions | PVS1 | within same splice donor/acceptor region, but outside ± 1,2 dinucleotide | PS1_Supporting | PS1_Supporting |
| Located at splice donor/acceptor PVS1 ± 1,2 dinucleotide positions | PVS1_Strong, PVS1_Moderate, or PVS1_Supporting | within same splice donor/acceptor ± 1,2 dinucleotide | PS1 | N/A |
| Located at splice donor/acceptor PVS1 ± 1,2 dinucleotide positions | PVS1_Strong, PVS1_Moderate, or PVS1_Supporting | within same splice donor/acceptor motif, but outside ± 1,2 dinucleotide | PS1_Moderate | PS1_Supporting |

**Prerequisites:** The predicted event of the VUA must precisely match the predicted event of the comparison (likely) pathogenic variant, AND the strength of the prediction for the VUA must be of similar or higher strength than the prediction for the comparison (likely) pathogenic variant.

---

### PS2 - De Novo

**Original ACMG Summary:** De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.

**Note:** Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.

**VCEP Specifications:**

PS2 and PM6 have been combined under PS2. See Table 2 for point system.

**Key Requirements:**
- Paternity and/or maternity of the non-carrier parent(s) need to be proven for confirmed de novo variants
- Both parents need to be clinically assessed and should not have a diagnosis of CYP1B1-related glaucoma phenotypes
- If a parent has glaucoma or suspicious signs of glaucoma, the age at diagnosis and the phenotype should be considered before applying criteria due to the prevalence of JOAG/POAG in the population and the possibility of phenocopies
- **Decrease the strength of evidence by one level for de novo occurrences without an additional P/LP variant**

#### Table 2: Point System for PS2

| Phenotype | Points per proband | |
|-----------|-------------------|---|
| | **Confirmed de novo** | **Assumed de novo** |
| PCG (phenotype consistent with gene but not highly specific) | 1 | 0.5 |
| Other CYP1B1-related glaucoma phenotype (JOAG, POAG, ASD) (phenotype consistent with gene but not highly specific and with high genetic heterogeneity) | 0.5 | 0.25 |

#### PS2 Evidence Strength Thresholds

| Points | Strength Level |
|--------|----------------|
| ≥ 0.5 | PS2_Supporting |
| ≥ 1.0 | PS2_Moderate |
| ≥ 2.0 | PS2 (Strong) |
| ≥ 4.0 | PS2_VeryStrong |

#### PS2 Default Point Values

| Strength | Points |
|----------|--------|
| Very Strong | 8 |
| Strong | 4 |
| Moderate | 2 |
| Supporting | 1 |

---

### PS3 - Functional Studies

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.

**Note:** Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.

**VCEP Specifications:**

The mechanism by which CYP1B1 variants cause the associated phenotype is a LoF mechanism. Cyp1b1-deficient mice show oxidative damage to trabecular meshwork cells, leading to apoptosis and increased IOP.

**Animal models** of specific variants (e.g. knock in mice models) would need to replicate the phenotype reported in humans (e.g. increase in IOP, degeneration of the optic nerve and/or damage to trabecular meshwork cells) in order to meet PS3.

**Functional assay requirements:**
- It has an appropriate number of validation controls (level of evidence to be established based on validation controls and associated OddsPath)
- The results show clear differentiation between LP/P and LB/B variants to establish threshold (or include indeterminate results in OddsPath calculation)
- The assay includes both negative and positive controls as well as technical and/or biological replicates
- Controls from the same general class of assays and with same methodology can be combined to calculate OddsPath
- If the results from different assays are conflicting for a single variant, then the level of validation of each assay should be considered
- Ideally variants should be assessed against their background haplotype

#### Strength Levels

| Strength | Criteria | Points |
|----------|----------|--------|
| **Strong** | Assays with OddsPath >18.7 as per the SVI recommendations; Animal models that replicate the glaucoma phenotype | 4 |
| **Moderate** | Assays with OddsPath >4.3 as per the SVI recommendations | 2 |
| **Supporting** | Assays with OddsPath >2.1 as per the SVI recommendations | 1 |

**Approved Studies for PS3_Supporting (as of 11/6/2025):**
- Chavarria-Soley et al. 2008
- Pasutto et al. 2010
- Mammen et al. 2003

---

### PS4 - Prevalence in Affected

**Original ACMG Summary:** The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.

***Not Applicable***

**Comments:** CYP1B1 variants cause autosomal recessive disorders associated with glaucoma. The number of probands with the variant will be addressed by PM3.

---

### PM1 - Mutational Hot Spot/Critical Domain

**Original ACMG Summary:** Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.

**VCEP Specifications:**

Although the crystal structure of CYP1B1 has not yet been established, cytochrome P450 proteins have known conserved regions and CYP1B1 structure can be predicted by comparative modeling.

The Glaucoma VCEP analyzed the presence of known pathogenic and benign variants in each of the characterized domains and helices and supporting functional evidence.

**Critical Point Caps:**
- The combination of PP3 and PM1 should not be higher than **4 points**
- The combination of PP3, PM1 and PM5 should not be higher than **5 points**
- The combination of PP3, PM1 and PS1 should not be higher than **6 points**

#### Strength Levels

| Strength | Region | Points |
|----------|--------|--------|
| **Moderate** | Hinge region (aa51-61) OR L-helix including haem-binding domain (aa460-493) | 2 |
| **Supporting** | G helix (aa253-282) OR I helix (aa339-365) | 1 |

**Rationale for regions:**
- **Hinge region (aa51-61)** and **haem-binding domain (aa463-472)** - critical and well-established functional domains without benign variation
- **L-helix region (aa460-493)** - whole region important for protein function, contains functional variants
- **Meander region (aa437-445)** - excluded as contains benign variation
- **G helix (aa253-282)** and **I helix (aa339-365)** - important for substrate binding, no benign variation, but less well defined in CYP1B1 context

---

### PM2 - Absent from Controls

**Original ACMG Summary:** Absent from controls (or at extremely low frequency if recessive) in population databases.

**Caveat:** Population data for indels may be poorly called by next generation sequencing.

**VCEP Specifications:**
- The highest allele frequency in population databases should be used
- Only applies to populations of ≥ 2,000 alleles
- **PM2 should be used at a Supporting level** as per the SVI recommendations

The Whiffin/Ware calculator for autosomal recessive disorders was used with:
- Prevalence of PCG in Europeans (lowest): 1/30,000
- Biallelic CYP1B1 variants in 22% of families with maximum allelic contribution of 19%
- Penetrance: 100%
- **Maximum credible allele frequency calculated: 0.000515**

#### Strength Level

| Strength | Threshold | Points |
|----------|-----------|--------|
| **Supporting** | Allele frequency ≤ 0.0005 in population databases | 1 |

---

### PM3 - In Trans with Pathogenic

**Original ACMG Summary:** For recessive disorders, detected in trans with a pathogenic variant.

**Note:** This requires testing of parents (or offspring) to determine phase.

**VCEP Specifications:**

See Table 1 for point system.

**Key Requirements:**
- Variants must not meet BS1 (instead of PM2 requirement from SVI)
- Variants need to meet PM4 (for in-frame indels) or PVS1 at any strength (for null variants) and must not meet BS1 or BP4
- Affected is defined as a diagnosis of PCG, ASD, JOAG or POAG
- To avoid circularity, the classification of the variant on the other allele should not use evidence from the variant being interrogated
- The variant on the other allele must have been classified following these VCEP specifications
- Multiple probands from different studies can be counted if they are independent
- The number of points given to multiple compound heterozygous cases with the same genotype has been capped to two when variants are not confirmed in trans
- Testing of one parent (or an unaffected first-degree relative carrying one of the two variants) is sufficient to confirm in trans for compound heterozygous cases
- Parental testing is not required for homozygous cases
- Individuals with multiple VUS/LP/P variants cannot be considered as evidence of either variant when the phase is unknown or for multiple variants in cis

#### Table 1: Point System for PM3

| Classification/Zygosity of other variant | Points per proband | |
|-----------------------------------------|-------------------|---|
| | **Non-consanguinity** | **Consanguinity** |
| Homozygous occurrence (max points 1.0) | 0.5 | 0.25 |
| | **Confirmed in trans** | **Phase unknown** |
| Compound Heterozygous occurrence with Pathogenic/Likely Pathogenic | 1.0 | 0.5* |
| Compound Heterozygous occurrence with VUS (max points 0.5) | 0.25 | 0.0 |

*No more than 2 cases can be counted when multiple compound heterozygous cases have the same genotype and the variants are not confirmed in trans.

#### PM3 Evidence Strength Thresholds

| Total Points | Strength Level | Default Points |
|--------------|----------------|----------------|
| ≥ 0.5 | PM3_Supporting | 1 |
| ≥ 1.0 | PM3 (Moderate) | 2 |
| ≥ 2.0 | PM3_Strong | 4 |
| ≥ 4.0 | PM3_VeryStrong | 8 |

---

### PM4 - Protein Length Changes

**Original ACMG Summary:** Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

**VCEP Specifications:**

| Strength | Criteria | Points |
|----------|----------|--------|
| **Moderate** | In-frame deletions/insertions in a non-repeat region. **Stop loss variants are not a known disease mechanism, therefore PM4 does not apply to that variant type** | 2 |

---

### PM5 - Novel Missense at Same Residue

**Original ACMG Summary:** Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.

**Caveat:** Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:**
- The novel change must not affect splicing (SpliceAI ≤ 0.2)
- Must meet PP3
- Must have a Grantham score equal or greater than the previously established pathogenic or likely pathogenic variant
- The combination of PP3, PM1 and PM5 should not be higher than **5 points**

#### Strength Levels

| Strength | Criteria | Points |
|----------|----------|--------|
| **Strong** | Same residue as 2 previously established **pathogenic** variants (both variants must be assessed independently of PM5) | 4 |
| **Moderate** | Same residue as previously established **pathogenic** variant (assessed independently of PM5) OR 2 previously established **likely pathogenic** variants (both assessed independently of PM5) | 2 |
| **Supporting** | Same residue as previously established **likely pathogenic** variant (assessed independently of PM5) | 1 |

---

### PM6 - De Novo (Assumed)

**Original ACMG Summary:** Assumed de novo, but without confirmation of paternity and maternity.

***Not Applicable***

**Comments:** Refer to PS2 - PM6 has been combined with PS2 under the point system.

---

### PP1 - Co-segregation

**Original ACMG Summary:** Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.

**Note:** May be used as stronger evidence with increasing segregation data.

**VCEP Specifications:**

See Table 4 for number of segregations for each level of strength.

**Key Requirements:**
- Affected segregations are affected family members in whom compound heterozygous (in trans) or homozygous variants segregate
- Affected is defined as a diagnosis of PCG, ASD, JOAG or POAG
- Use caution and consider phenotypes, age at diagnosis and pedigree structure before applying to segregations with POAG due to risk of phenocopy
- Segregations from multiple families can be added
- Unaffected family members are individuals at risk to inherit the two variants identified in the proband and are either wild-type for both variants or a heterozygous carrier for a single variant
- The variant in trans needs to be independently assessed and classified as VUS/LP/P

#### Strength Levels

| Strength | Criteria | Points |
|----------|----------|--------|
| **Strong** | ≥3 affected segregations OR 2 affected segregations AND ≥3 unaffected segregations OR 1 affected segregation AND ≥8 unaffected segregations | 4 |
| **Moderate** | 2 affected segregations OR 1 affected segregation AND ≥5 unaffected segregations OR ≥10 unaffected segregations | 2 |
| **Supporting** | 1 affected segregation OR ≥5 unaffected segregations | 1 |

#### Table 4: Recommendations for Counting Segregations

General recommendations (phenocopy not an issue):

| Affected segregations | Unaffected recessive segregations |||||||||||
|----------------------|---|-----|------|------|-----|------|------|------|-----|------|------|
| | **0** | **1** | **2** | **3** | **4** | **5** | **6** | **7** | **8** | **9** | **10** |
| 0 | 0 | 0.12 | 0.25 | 0.37 | 0.5 | 0.62 | 0.75 | 0.87 | 1 | 1.12 | 1.25 |
| 1 | 0.6 | 0.73 | 0.85 | 0.98 | 1.1 | 1.23 | 1.35 | 1.48 | 1.6 | 1.73 | 1.85 |
| 2 | 1.2 | 1.33 | 1.45 | 1.58 | 1.7 | 1.83 | 1.95 | 2.08 | 2.2 | 2.33 | 2.45 |
| 3 | 1.81 | 1.93 | 2.06 | 2.18 | 2.31 | 2.43 | 2.56 | 2.68 | 2.81 | 2.93 | 3.06 |
| 4 | 2.41 | 2.53 | 2.66 | 2.78 | 2.91 | 3.03 | 3.16 | 3.28 | 3.41 | 3.53 | 3.66 |
| 5 | 3.01 | 3.14 | 3.26 | 3.39 | 3.51 | 3.63 | 3.76 | 3.88 | 4.01 | 4.13 | 4.26 |

**Color coding:** Green = Supporting (0.5-0.99), Yellow = Moderate (1.0-1.99), Orange/Red = Strong (≥2.0)

---

### PP2 - Missense in Constrained Gene

**Original ACMG Summary:** Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.

***Not Applicable***

**Comments:** Although pathogenic missense variants are common in CYP1B1, the gene also has a significant amount of benign missense variants as shown by the missense constraint z score in gnomAD (z = -0.75) supporting tolerance to variation.

---

### PP3 - Computational Evidence

**Original ACMG Summary:** Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).

**Caveat:** As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.

**VCEP Specifications:**
- Use only one in silico predictor (REVEL) as recommended due to lower concordance when multiple software is used
- Follow SVI recommendations for REVEL thresholds
- Apply the highest level of strength met
- **Point caps:** The combination of PP3 and PM1 should not be higher than 4 points; the combination of PP3, PM1 and PM5 should not be higher than 5 points; and the combination of PP3, PM1 and PS1 should not be higher than 6 points

#### Strength Levels

| Strength | Criteria | Points |
|----------|----------|--------|
| **Strong** | For missense variants: REVEL score ≥ 0.932 | 4 |
| **Moderate** | For missense variants: REVEL score 0.773-0.931 | 2 |
| **Supporting** | For missense variants: SpliceAI ≥ 0.2 OR REVEL score 0.644-0.772; For all other variants located outside of donor/acceptor ±1,2 dinucleotide positions (when splicing assay is not available): SpliceAI ≥ 0.2 | 1 |

---

### PP4 - Phenotype Specificity

**Original ACMG Summary:** Patient's phenotype or family history is highly specific for a disease with a single genetic etiology.

***Not Applicable***

**Comments:** The phenotype associated with CYP1B1 variants is not highly specific and there is genetic heterogeneity.

---

### PP5 - Reputable Source

**Original ACMG Summary:** Reputable source recently reports variant as pathogenic, but the evidence is not available to the laboratory to perform an independent evaluation.

***Not Applicable***

This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PMID: 29543229).

---

## Benign Criteria

### BA1 - Allele Frequency >5%

**Original ACMG Summary:** Allele frequency is above 5% in population databases.

**VCEP Specifications:**
- The highest allele frequency in population databases should be used
- Variant must be present in ≥ 5 alleles in any validated general continental population dataset of at least 2,000 observed alleles

The Whiffin/Ware calculator for autosomal recessive disorders was used with the population with the highest ever reported genetic contribution and prevalence (Romani people in Slovakia: 1/2,210, 100% genetic contribution). The calculated maximum credible allele frequency was 0.0213.

**However**, the VCEP revised the threshold to **0.05** because:
- Populations with highest incidences of PCG (India, Pakistan, Romani) are currently not well represented in gnomAD v4
- Only two ClinVar variants have highest allele frequency between 0.02 and 0.05: A443G (0.04963) and R368H (0.03079)
- R368H has complex, conflicting evidence and the higher threshold accounts for uncertainty

| Strength | Threshold |
|----------|-----------|
| **Stand Alone** | Allele frequency ≥ 0.05 (5%) in population databases |

---

### BS1 - Frequency Greater Than Expected

**Original ACMG Summary:** Allele frequency is greater than expected for disorder.

**VCEP Specifications:**
- The highest allele frequency in population databases should be used
- Variant must be present in ≥ 5 alleles in any validated general continental population dataset of at least 2,000 observed alleles

The Whiffin/Ware calculator was used with the population with highest genetic contribution and prevalence in a well-defined population (Saudi Arabia: prevalence 1/4,500, 77% genetic contribution with 91% penetrance, most common variant G61E at 76% of CYP1B1 families).

**Maximum credible allele frequency calculated: 0.01**

| Strength | Threshold | Points |
|----------|-----------|--------|
| **Strong** | Allele frequency ≥ 0.01 (1%) in population databases | -4 |

---

### BS2 - Observed in Healthy Adult

**Original ACMG Summary:** Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

***Not Applicable***

**Comments:** CYP1B1 variants can have an incomplete penetrance and late age of onset. Adults with known pathogenic homozygous CYP1B1 variants who had a normal eye examination have been reported.

---

### BS3 - Functional Studies (No Effect)

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

***Not Applicable***

**Comments:** Given that normal protein abundance and stability does not rule out impact on enzymatic activity, and that normal enzymatic activity for one substrate is not indicative of other substrates, the Glaucoma VCEP decided to not apply BS3.

---

### BS4 - Lack of Segregation

**Original ACMG Summary:** Lack of segregation in affected members of a family.

**Caveat:** The presence of phenocopies for common phenotypes can mimic lack of segregation. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder.

**VCEP Specifications:**

| Strength | Criteria | Points |
|----------|----------|--------|
| **Strong** | Non-segregations with PCG, ASD or JOAG. Use caution and consider phenotypes of the affected segregations, age at diagnosis and pedigree structure before applying to non-segregations with JOAG or POAG. | -4 |

---

### BP1-BP7 - Benign Supporting

| Criterion | Status | Comment | Points |
|-----------|--------|---------|--------|
| **BP1** | *Not Applicable* | Both truncating and missense CYP1B1 variants are causative | - |
| **BP2** | *Not Applicable* | Two missense variants in cis could act synergistically or the effect of a variant occurring after a truncating variant may not be predicted | - |
| **BP3** | *Not Applicable* | CYP1B1 does not have a repetitive region without a known function | - |
| **BP4** | Applicable | See below | Variable |
| **BP5** | *Not Applicable* | Multiple molecular diagnoses are possible and variants in different genes could have an additive effect | - |
| **BP6** | *Not Applicable* | This criterion is not for use as recommended by the ClinGen SVI VCEP Review Committee (PMID: 29543229) | - |
| **BP7** | Applicable | See below | -1 |

#### BP4 - Computational Evidence (Benign)

**Original ACMG Summary:** Multiple lines of computational evidence suggest no impact on gene or gene product.

**VCEP Specifications:**
- Follow SVI recommendations for REVEL thresholds
- Use SpliceAI for variants located outside of donor/acceptor ±1,2 dinucleotide positions
- Apply the highest level of strength met

| Strength | Criteria | Points |
|----------|----------|--------|
| **Strong** | For missense variants: SpliceAI ≤ 0.1 AND REVEL score ≤ 0.016 | -4 |
| **Moderate** | For missense variants: SpliceAI ≤ 0.1 AND REVEL score 0.017-0.183 | -2 |
| **Supporting** | For missense variants: SpliceAI ≤ 0.1 AND REVEL score 0.184-0.290; For all other variants (not meeting PVS1 or PM4) located outside of donor/acceptor ±1,2 dinucleotide positions (when splicing assay is not available): SpliceAI ≤ 0.1 | -1 |

#### BP7 - Synonymous Variant

**Original ACMG Summary:** A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.

| Strength | Criteria | Points |
|----------|----------|--------|
| **Supporting** | Applies to intronic/noncoding variants outside the donor/acceptor splice region (intronic variants at or beyond positions +7/-21) and synonymous (silent) exonic variants located outside of the first and the last 3 bases of the exon **if BP4 is met** | -1 |

---

## Point-Based Classification System

### Classification Thresholds

| Category | Point Range |
|----------|-------------|
| **Pathogenic** | ≥ 10 |
| **Likely Pathogenic** | 6 to 9 |
| **Uncertain Significance (VUS)** | -1 to 5 |
| **Likely Benign** | -6 to -2 |
| **Benign** | ≤ -7 |

**Additional Note:** PVS1_SA is stand alone for Pathogenic classification (full gene deletions)

### Default Point Values Summary

| Strength Level | Default Points |
|----------------|----------------|
| Very Strong (Pathogenic) | 8 |
| Strong (Pathogenic) | 4 |
| Moderate (Pathogenic) | 2 |
| Supporting (Pathogenic) | 1 |
| Supporting (Benign) | -1 |
| Moderate (Benign) | -2 |
| Strong (Benign) | -4 |
| Stand Alone (BA1) | Benign |

---

## Rules for Combining Criteria

### Important Combination Limits

| Combination | Maximum Points |
|-------------|----------------|
| PP3 + PM1 | 4 |
| PP3 + PM1 + PM5 | 5 |
| PP3 + PM1 + PS1 | 6 |

### Standard ACMG/AMP Combination Rules

#### Pathogenic Classification (≥10 points)

| Criteria Combination |
|---------------------|
| 1 Very Strong (8) AND 1 Moderate (2) |
| 1 Very Strong (8) AND 2 Supporting (2) |
| 2 Strong (8) AND 1 Moderate (2) |
| 1 Strong (4) AND 3 Moderate (6) |
| 1 Strong (4) AND 2 Moderate (4) AND 2 Supporting (2) |

#### Likely Pathogenic Classification (6-9 points)

| Criteria Combination |
|---------------------|
| 1 Very Strong (8) AND 1 Supporting (1) = 9 |
| 1 Strong (4) AND 1-2 Moderate (2-4) |
| 1 Strong (4) AND 2 Supporting (2) = 6 |
| 3 Moderate (6) |
| 2 Moderate (4) AND 2 Supporting (2) = 6 |

#### Benign Classification (≤-7 points)

| Criteria Combination |
|---------------------|
| 1 Stand Alone (BA1) |
| 2 Strong (-8) |

#### Likely Benign Classification (-6 to -2 points)

| Criteria Combination |
|---------------------|
| 1 Strong (-4) AND 1 Supporting (-1) = -5 |
| 1 Strong (-4) AND 1 Moderate (-2) = -6 |

---

## Appendices

### Appendix A: CYP1B1 Gene Schematic

```
                              aa330
                    NMD      |      No NMD
                  assumed    ↓      assumed
                    ←————————|————————→
    ┌────┐    ┌══════════════════════════┐    ┌════════════════════════════════┐
    │  1 │────│            2             │────│              3                 │
    └────┘    └══════════════════════════┘    └════════════════════════════════┘
   (non-coding)       (coding)                         (coding)
                                                    ┌─────┐
                                                    │HAEM │ ← Haem-binding domain
                                                    │     │   (aa460-493)
                                                    └─────┘
                                                         ↑
                                                      aa489 = Last 10% of protein
```

- **Exon 1:** Non-coding (5'UTR)
- **Exon 2:** Coding - NMD predicted for variants with PTC before aa330
- **Exon 3:** Coding - Contains haem-binding domain (aa460-493)
- **Haem-binding domain (aa460-493):** Critical for enzymatic activity

### Appendix B: PVS1 Decision Tree Summary

| Variant Type | Condition | Strength |
|--------------|-----------|----------|
| **Nonsense/Frameshift** | PTC aa1-330 (NMD predicted) | PVS1 |
| | PTC aa331-493 (removes haem domain) | PVS1 |
| | PTC aa494-Ter (after haem domain) | PVS1_Moderate |
| **Splice (GT-AG ±1,2)** | Disrupts frame, NMD predicted (aa1-330) | PVS1 |
| | Disrupts frame prior to haem domain (aa331-493) | PVS1 |
| | Disrupts frame after haem domain (aa494-Ter) | PVS1_Moderate |
| **Deletion** | Full gene | PVS1_SA |
| | Exon 2 and/or 3 | PVS1 |
| | Exon 1 only | PVS1_Supporting |
| **Duplication (proven in tandem)** | NMD predicted or removes haem domain | PVS1 |
| | After haem domain | PVS1_Moderate |
| **Duplication (presumed in tandem)** | NMD predicted or removes haem domain | PVS1_Strong |
| | After haem domain | PVS1_Supporting |
| **Initiation codon** | No alt start, ≥1 P variant upstream | PVS1_Moderate |

### Appendix C: Population Frequency Thresholds Summary

| Criterion | Threshold | Strength | Justification |
|-----------|-----------|----------|---------------|
| **BA1** | ≥ 0.05 (5%) | Stand Alone | Conservative threshold due to underrepresentation of high-incidence populations in gnomAD |
| **BS1** | ≥ 0.01 (1%) | Strong | Based on Saudi Arabian population (highest well-defined prevalence) |
| **PM2** | ≤ 0.0005 | Supporting | Based on European population (lowest prevalence) |

### Appendix D: CYP1B1-Related Diseases

**Primary phenotypes:**
- Primary congenital glaucoma (PCG)
- Juvenile open angle glaucoma (JOAG)
- Primary open angle glaucoma (POAG)
- Anterior segment dysgenesis (ASD)

**Other terms used:**
- Congenital glaucoma
- (Primary) Childhood glaucoma
- (Primary) Infantile glaucoma
- (Primary) Pediatric glaucoma
- (Primary) Early age of onset glaucoma
- (Primary) Juvenile onset glaucoma

**Anterior segment dysgenesis (ASD) includes:**
- Axenfeld-Rieger anomaly (ARA) or Axenfeld-Rieger syndrome (ARS)
- Axenfeld anomaly or Axenfeld syndrome
- Rieger anomaly or Rieger syndrome
- Iridogoniodysgenesis
- Peters anomaly or Peters syndrome
- Aniridia or partial aniridia
- Congenital ectropion uveae
- Congenital iris hypoplasia

### Appendix E: Functional Domains for PM1

| Domain | Amino Acid Range | PM1 Strength | Notes |
|--------|-----------------|--------------|-------|
| Hinge region | aa51-61 | Moderate | Critical functional domain, no benign variation |
| G helix | aa253-282 | Supporting | Important for substrate binding, no benign variation, less well defined |
| I helix | aa339-365 | Supporting | Important for substrate binding, no benign variation, less well defined |
| Meander region | aa437-445 | N/A | Contains benign variation - excluded |
| L-helix (including haem-binding domain) | aa460-493 | Moderate | Critical for protein function |
| Haem-binding domain (subset of L-helix) | aa463-472 | Moderate | Critical and well-established functional domain |

### Appendix F: References

1. Abou Tayoun AN, Pesaran T, et al. Recommendations for interpreting the loss of function PVS1 ACMG/AMP variant criterion. Hum Mutat (2018) 39(11):1517-1524. PMID: 30192042
2. Campos-Mollo E, López-Garrido MP, et al. CYP1B1 mutations in Spanish patients with primary congenital glaucoma: phenotypic and functional variability. Mol Vis (2009) 15:417-31. PMID: 19234632
3. Jansson I, Stoilov I, et al. Effect of two mutations of human CYP1B1, G61E and R469W, on stability and endogenous steroid substrate metabolism. Pharmacogenetics (2001) 11(9):793-801. PMID: 11740343
4. Medina-Trillo C, Ferre-Fernández JJ, et al. Functional characterization of eight rare missense CYP1B1 variants involved in congenital glaucoma and their association with null genotypes. Acta Ophthalmol (2016) 94(7):e555-e560. PMID: 27060699
5. Teixeira LB, Zhao Y, et al. Ultrastructural abnormalities of the trabecular meshwork extracellular matrix in Cyp1b1-deficient mice. Vet Pathol (2015) 52(2):397-403. PMID: 24879660
6. Walker LC, Hoya M, et al. Using the ACMG/AMP framework to capture evidence related to predicted and observed impact on splicing. Am J Hum Genet (2023) 110(7):1046-1067. PMID: 37352859
7. Zhao Y, Wang S, et al. Cyp1b1 mediates periostin regulation of trabecular meshwork development by suppression of oxidative stress. Mol Cell Biol (2013) 33(21):4225-40. PMID: 23979599
8. Choudhary D, Jansson I, et al. Metabolism of retinoids and arachidonic acid by human and mouse cytochrome P450 1b1. Drug Metab Dispos (2004) 32(8):840-7. PMID: 15258110
9. Vasiliou V, Gonzalez FJ. Role of CYP1B1 in glaucoma. Annu Rev Pharmacol Toxicol (2008) 48:333-58. PMID: 17914928
10. Brnich SE, Abou Tayoun AN, et al. Recommendations for application of the functional evidence PS3/BS3 criterion using the ACMG/AMP sequence variant interpretation framework. Genome Med (2019) 12(1):3. PMID: 31892348
11. Chavarria-Soley G, Sticht H, et al. Mutations in CYP1B1 cause primary congenital glaucoma by reduction of either activity or abundance of the enzyme. Hum Mutat (2008) 29(9):1147-53. PMID: 18470941
12. Szklarz GD, He YA, et al. Site-directed mutagenesis as a tool for molecular modeling of cytochrome P450 2B1. Biochemistry (1995) 34(44):14312-22. PMID: 7578035
13. Bart AG, Harris KL, et al. Structure of an ancestral mammalian family 1B1 cytochrome P450 with increased thermostability. J Biol Chem (2020) 295(17):5640-5653. PMID: 32156703
14. Whiffin N, Minikel E, et al. Using high-resolution variant frequencies to empower clinical genome interpretation. Genet Med (2017) 19(10):1151-1158. PMID: 28518168
15. MacKinnon JR, Giubilato A, et al. Primary infantile glaucoma in an Australian population. Clin Exp Ophthalmol (2004) 32(1):14-8. PMID: 14746584
16. Dimasi DP, Hewitt AW, et al. Prevalence of CYP1B1 mutations in Australian patients with primary congenital glaucoma. Clin Genet (2007) 72(3):255-60. PMID: 17718864
17. Oza AM, DiStefano MT, et al. Expert specification of the ACMG/AMP variant interpretation guidelines for genetic hearing loss. Hum Mutat (2018) 39(11):1593-1613. PMID: 30311386
18. Pejaver V, Byrne AB, et al. Calibration of computational tools for missense variant pathogenicity classification and ClinGen recommendations for PP3/BP4 criteria. Am J Hum Genet (2022) 109(12):2163-2177. PMID: 36413997
19. Ghosh R, Oak N, et al. Evaluation of in silico algorithms for use with ACMG/AMP clinical variant interpretation guidelines. Genome Biol (2017) 18(1):225. PMID: 29179779
20. Plásilová M, Stoilov I, et al. Identification of a single ancestral CYP1B1 mutation in Slovak Gypsies (Roms) affected with primary congenital glaucoma. J Med Genet (1999) 36(4):290-4. PMID: 10227395
21. Genčík A. Epidemiology and genetics of primary congenital glaucoma in Slovakia. Dev Ophthalmol (1989) 16:76-115. PMID: 2676634
22. Alsaif HS, Khan AO, et al. Congenital glaucoma and CYP1B1: an old story revisited. Hum Genet (2019) 138(8-9):1043-1049. PMID: 29556725
23. Reddy AB, Kaur K, et al. Mutation spectrum of the CYP1B1 gene in Indian primary congenital glaucoma patients. Mol Vis (2004) 10:696-702. PMID: 15475877
24. Chakrabarti S, Kaur K, et al. Globally, CYP1B1 mutations in primary congenital glaucoma are strongly structured by geographic and haplotype backgrounds. Invest Ophthalmol Vis Sci (2006) 47(1):43-7. PMID: 16384942
25. Abouelhoda M, Faquih T, et al. Revisiting the morbid genome of Mendelian disorders. Genome Biol (2016) 17(1):235. PMID: 27884173
26. Mammen JS, Pittman GS, et al. Single amino acid mutations, but not common polymorphisms, decrease the activity of CYP1B1 against (-)benzo[a]pyrene-7R-trans-7,8-dihydrodiol. Carcinogenesis (2003) 24(7):1247-55. PMID: 12807732
27. Pasutto F, Chavarria-Soley G, et al. Heterozygous loss-of-function variants in CYP1B1 predispose to primary open-angle glaucoma. Invest Ophthalmol Vis Sci (2010) 51(1):249-54. PMID: 19643970

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 11/6/2025 | Initial approved version following pilot phase |

**Modifications to the rules following pilot phase:**
- PVS1_SA was added for full gene deletions (stand alone for Pathogenic classification)
- PS1: Specified that this rule does not apply to initiation codons
- PS3: Specified conditions for animal models of specific variants to meet PS3 if developed
- PM3: Piloted the use of VUS compound heterozygous in trans
- PM3: Specified that variants must not meet BP4 (instead of meeting PP3)
- PM3: Specified that individuals with multiple VUS/LP/P variants cannot be considered as evidence of either variant when the phase is unknown or variants are in cis
- PP1: Specified that compound heterozygous variants in affected segregations need to be in trans
- BA1: Threshold updated with justification
- BP4: Specified that the SpliceAI threshold applies to non-missense variants not meeting PVS1 or PM4

---

*This document was compiled from ClinGen Glaucoma VCEP specifications. For the most current version, please refer to the ClinGen website.*
