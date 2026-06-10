# ClinGen SCID VCEP Variant Interpretation Guidelines for DCLRE1C

**Version:** 2.1.0
**Released:** October 1, 2025
**Affiliation:** Severe Combined Immunodeficiency Disease VCEP
**Based on:** Richards et al., 2015 ACMG/AMP Guidelines

---

## Gene Information

| Attribute | Value |
|-----------|-------|
| **Gene** | DCLRE1C (HGNC:17642) |
| **HGNC Name** | DNA cross-link repair 1C |
| **Transcript** | NM_001033855.3 |
| **Disease** | Severe combined immunodeficiency due to DCLRE1C deficiency (MONDO:0011225) |
| **Inheritance** | Autosomal recessive |

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

**VCEP Specifications:** Use the attached PVS1 flowchart (see Appendix A).

#### Strength Levels

| Strength | Criteria |
|----------|----------|
| **Very Strong** | Use ClinGen SVI recommendations (Tayoun et al., 2018; PMID: 30192042) |
| **Strong** | For variants NOT predicted to undergo NMD but removing >10% of protein (i.e., variants in exon 14 or last 50 nucleotides of exon 13 after c.1106, codon 369), apply PVS1_Strong only if **at least one pathogenic variant is present downstream** |
| **Moderate** | For variants NOT predicted to undergo NMD but removing >10% of protein, when at least one pathogenic variant is **NOT** present downstream, downgrade to PVS1_Moderate |

**Important Note:** Exons 1-3 and exons 1-4 have been reported as a hot spot for deletion variants due to homologous recombination of the wild-type DCLRE1C gene with a DCLRE1C pseudogene (PMID: 19953608).

#### PVS1 Decision Flowchart Summary

| Variant Type | NMD Predicted | Exon in Biologically-Relevant Transcript | Strength |
|--------------|---------------|------------------------------------------|----------|
| Nonsense/Frameshift | Yes | Yes | PVS1 |
| Nonsense/Frameshift | No, removes >10% protein | - | PVS1_Strong (if P/LP downstream) or PVS1_Moderate |
| Nonsense/Frameshift | No, removes <10% protein | - | PVS1_Moderate |
| Splice site (±1,2) | Disrupts frame + NMD | Yes | PVS1 |
| Splice site (±1,2) | Preserves frame, removes >10% | - | PVS1_Strong or PVS1_Moderate |
| Full gene deletion | - | - | PVS1 |
| Single/multi-exon deletion | Disrupts frame + NMD | Yes | PVS1 |
| Initiation codon | No alternative start | P/LP upstream of closest in-frame start | PVS1_Moderate |
| Initiation codon | No alternative start | No P/LP upstream | PVS1_Supporting |

---

### PS1 - Same Amino Acid Change

**Original ACMG Summary:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | Applicable if previously established variant is classified as **pathogenic** by SCID VCEP specifications for DCLRE1C. Also applicable for splice variants at the same nucleotide with similar or greater SpliceAI impact prediction. |
| **Moderate** | Applicable if previously established variant is classified as **likely pathogenic** by SCID VCEP specifications for DCLRE1C. |

**Example:** c.105+1G>C is known to be pathogenic → can use PS1 for c.105+1G>T

---

### PS2 - De Novo (Confirmed)

**Original ACMG Summary:** De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.

**VCEP Specifications:** Use ClinGen SVI recommendations with the following phenotype guidelines:

| Phenotype Category | Required Criteria |
|-------------------|-------------------|
| Phenotype highly specific for gene | Must meet at least PP4_Moderate |
| Phenotype consistent but not highly specific | Must meet PP4 |
| Phenotype consistent with high genetic heterogeneity | Proband has SCID phenotype but does not meet PP4 |

**Reduce points by half if phase is unconfirmed.**

#### PS2/PM6 Point System

| Phenotypic Consistency | Confirmed Parental Relationships | Unconfirmed |
|------------------------|----------------------------------|-------------|
| Phenotype highly specific for gene | 2 points | 1 point |
| Phenotype consistent but not highly specific | 1 point | 0.5 points |
| Phenotype consistent + high genetic heterogeneity | 0.5 points | 0.25 points |
| Phenotype not consistent | 0 points | 0 points |

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

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | Evidence from an **animal model** expressing the variant of interest and recapitulating the DCLRE1C-SCID phenotype. Reviewed case-by-case by VCEP. |
| **Moderate** | Abnormal result in **BOTH** an *in vitro* DNA repair activity assay **AND** an *in vitro* V(D)J recombination assay (defined as <25% of wild-type activity for both). |
| **Supporting** | Abnormal result in an *in vitro* V(D)J recombination assay only (same threshold, <25% of wild-type activity). |

**Required:** At least one previously observed proband with the DCLRE1C variant meeting PP4 is required to apply PS3 at any strength.

#### Approved Assay Instances

**DNA Repair Activity Assay:**
- Felgentreff et al., 2015 (PMID: 25917813)

**V(D)J Recombination Assay:**
- Pannicke et al., 2004 (PMID: 15071507)
- Ege et al., 2005 (PMID: 15731174)
- Felgentreff et al., 2015 (PMID: 25917813)
- Volk et al., 2015 (PMID: 26476407)

#### General Classes of Functional Assays for DCLRE1C

| Assay Type | Reference PMIDs |
|------------|-----------------|
| V(D)J recombination assay | 26476407, 15731174, 25917813, 15071507, 19349461 |
| DNA cleavage assay | 15731174, 24500713, 15071507, 19349461 |
| DNA-PKcs assay (binding/phosphorylation) | 15731174, 15071507, 19349461 |
| DNA repair activity assay | 25917813 |

---

### PS4 - Prevalence in Affected

**Not Applicable** for DCLRE1C variant classification.

---

### PM1 - Mutational Hot Spot

**Not Applicable.** No known missense variation hot spots in the DCLRE1C gene have been described.

**Note:** Exons 1-3 and exons 1-4 are a hot spot for **deletion variants** (not missense) due to homologous recombination with a DCLRE1C pseudogene (PMID: 19953608).

---

### PM2 - Absent from Controls

**Original ACMG Summary:** Absent from controls (or at extremely low frequency if recessive) in population databases.

**VCEP Specification (Supporting only):**
- gnomAD popmax filtering allele frequency **<0.00003266**
- **Additional requirement:** No homozygotes observed in gnomAD

---

### PM3 - In Trans with Pathogenic

**Original ACMG Summary:** For recessive disorders, detected in trans with a pathogenic variant.

**SVI Revised Definition:** For recessive disorders, detected in trans with a pathogenic or likely pathogenic variant **in an affected patient**.

**VCEP Specifications:** Use ClinGen SVI adapted recommendations with the additional requirement that the co-occurring variant must be classified using SCID VCEP specifications for DCLRE1C.

**Caveat:** All variants should be sufficiently rare (meet PM2 specification). The applicability of PM3 to suspected founder variants with allele frequencies exceeding PM2 threshold will be evaluated case-by-case.

#### PM3 Point System (Per Proband)

| Classification/Zygosity of Other Variant | Confirmed in Trans | Phase Unknown |
|------------------------------------------|-------------------|---------------|
| Pathogenic or Likely pathogenic variant | 1.0 | 0.5 (P) / 0.25 (LP) |
| Homozygous (non-consanguineous) | 1.0 | 1.0 |
| Homozygous (consanguineous, max 0.5/family) | 0.5 | 0.5 |
| VUS (max 0.5 total) | 0.25 | 0.0 |

#### PM3 Evidence Strength Thresholds

| Total Points | Strength Level |
|--------------|----------------|
| 0.5 | PM3_Supporting |
| 1.0 | PM3 (Moderate) |
| 2.0 | PM3_Strong |
| 4.0 | PM3_VeryStrong |

#### Important Considerations

1. **Allele Frequency:** Both variants must be sufficiently rare (meet PM2 threshold)
2. **Phasing:** If phase cannot be determined, at least two different LP/P variants are needed to equal one confirmed in trans
3. **Classification:** To avoid circularity, classification of variant on other allele should not use evidence from the variant being interrogated
4. **Homozygous:** Max 1.0 points from all homozygous cases to prevent overclassification

---

### PM4 - Protein Length Changes

**Original ACMG Summary:** Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Moderate** | Deleted region must contain a known **pathogenic or likely pathogenic** variant not predicted/observed to alter splicing |
| **Supporting** | Deleted region must contain a known **VUS** variant not predicted/observed to alter splicing |

---

### PM5 - Novel Missense at Same Residue

**Original ACMG Summary:** Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.

**VCEP Specifications for Missense Variants:**
- **PM5 (Moderate):** Applicable if previously established variant is classified as pathogenic
- **PM5_Supporting:** Applicable if previously established variant is classified as likely pathogenic

**VCEP Specifications for Nonsense Variants:**

| Strength | Criteria |
|----------|----------|
| **PM5_Strong** | ≥4 points from informative variants. Downgrade to PM5_Moderate if PVS1 applied at any strength. |
| **PM5_Moderate** | ≥2 points from informative variants. Cannot combine with PVS1_VeryStrong (downgrade to PM5_Supporting). |
| **PM5_Supporting** | 1 point from informative variants |

#### PM5 Nonsense Variant Point Table

| VUA Type | Informative Variant | Points |
|----------|---------------------|--------|
| Nonsense predicted to lead to NMD | P/LP in same exon predicted to lead to NMD | +1 |
| Nonsense predicted to lead to NMD | B/LB in same exon | -2 |
| Nonsense in final exon (no NMD) | P/LP in same exon **downstream** of VUA | +1 |
| Nonsense in final exon (no NMD) | B/LB in same exon **upstream** of VUA | -2 |

**Notes:**
- Informative variant must be classified by SCID VCEP specifications
- Cannot be the same variant used for "+1 pathogenic variant downstream" on PVS1 flowchart
- If negative points calculated, do not apply PM5 and reconsider PVS1
- VUA must meet PM2_Supporting
- Frameshift/nonsense informative variants must be P/LP without PM5 and without only PVS1+PM2

---

### PM6 - De Novo (Assumed)

**Original ACMG Summary:** Assumed de novo, but without confirmation of paternity and maternity.

**VCEP Specifications:** Same as PS2 - use ClinGen SVI recommendations with the same phenotype guidelines and point system (see PS2 section above).

---

### PP1 - Co-segregation

**Original ACMG Summary:** Co-segregation with disease in multiple affected family members.

**VCEP Specifications:** Use ClinGen SVI recommendations (PMID: 30311386) with the additional specification that unaffected individuals contributing to LOD score must be **heterozygous carriers** of one of the variants observed in affected individuals (do not count wild-type/wild-type individuals).

#### PP1 Thresholds (General)

| Strength | Likelihood | LOD Score | AD Threshold |
|----------|------------|-----------|--------------|
| Supporting | 4:1 | 0.6 | 2 affected segregations |
| Moderate | 16:1 | 1.2 | 4 affected segregations |
| Strong | 32:1 | 1.5 | 5 affected segregations |

#### Autosomal Recessive LOD Score Table

| Affected Seg. | 0 Unaff | 1 Unaff | 2 Unaff | 3 Unaff | 4 Unaff | 5 Unaff |
|---------------|---------|---------|---------|---------|---------|---------|
| 0 | 0 | 0.12 | 0.25 | 0.37 | 0.50 | 0.62 |
| 1 | 0.60 | 0.73 | 0.85 | 0.98 | 1.10 | 1.23 |
| 2 | 1.20 | 1.33 | 1.45 | 1.58 | 1.70 | 1.83 |
| 3 | 1.81 | 1.93 | 2.06 | 2.18 | 2.31 | 2.43 |
| 4 | 2.41 | 2.53 | 2.66 | 2.78 | 2.91 | 3.03 |
| 5 | 3.01 | 3.14 | 3.26 | 3.39 | 3.51 | 3.63 |

**Color coding:** Green (Supporting, LOD ≥0.6), Yellow (Moderate, LOD ≥1.2), Red (Strong, LOD ≥1.5)

---

### PP2 - Missense in Constrained Gene

**Not Applicable.** The gnomAD v2.1.1 missense Z score for DCLRE1C (Z = -0.68) suggests this gene is not constrained for missense variation. Both benign and pathogenic missense variants are present.

---

### PP3 - Computational Evidence

**Original ACMG Summary:** Multiple lines of computational evidence support a deleterious effect.

**VCEP Specification (Supporting only):**
- Only applicable to **synonymous or intronic variants** predicted to impact splicing by SpliceAI with delta score **≥0.2**
- **Do NOT apply to missense variants**

---

### PP4 - Phenotype Specificity

**Original ACMG Summary:** Patient's phenotype or family history is highly specific for a disease with a single genetic etiology.

**VCEP Specifications:** PP4 applicability and strength is determined by total points accumulated by a single affected individual.

#### PP4 Strength Thresholds

| Total Points | Strength |
|--------------|----------|
| <1 | PP4 not met |
| 1 to <2 | PP4 (Supporting) |
| 2 to <6 | PP4_Moderate |
| ≥6 | PP4_Strong¹ |

¹CNV testing is required for PP4_Strong to certify the variant is causative.

#### PP4 Point System

| Evidence Description | Points |
|---------------------|--------|
| Diagnostic criteria met for SCID (Criteria 1 and 3 or Criterion 4 alone) or Leaky SCID/Omenn syndrome (excluding Criterion 2)² | 0.5 |
| SCID gene panel or exome/genome sequencing conducted (no alternative explanation found) | 1.0 |
| Family history of SCID (with negative genetic testing on proband) | 0.5 |
| Navajo or Apache descent | 0.25 |
| Increased cellular radiosensitivity (>1 log decreased proliferation/survival OR impaired gH2AX correction) **AND** P/LP variants in PRKDC, NHEJ1, LIG4 **excluded** | 4.5 |
| Increased cellular radiosensitivity **AND** P/LP variants in PRKDC, NHEJ1, LIG4 **NOT excluded** | 0.5 |
| Decreased V(D)J recombination **AND** P/LP variants in RAG1, RAG2, PRKDC, NHEJ1, LIG4, NUDCD3 **excluded** | 4.5 |
| Decreased V(D)J recombination **AND** P/LP variants in RAG1, RAG2, PRKDC, NHEJ1, LIG4, NUDCD3 **NOT excluded** | 1.0 |
| Vector-based complementation corrected radiosensitivity and/or V(D)J recombination and/or T cell maturation | 5.0 |
| SCID phenotype corrected by DCLRE1C gene therapy **WITHOUT** CNV testing | 4.5 |
| SCID phenotype corrected by DCLRE1C gene therapy **WITH** CNV testing | 6.0 |
| T-B-NK+ lymphocyte subset profile* | 0.5 |

²Diagnostic criteria follow PIDTC 2022 specification.

**Notes:**
- If NK cells not noted or present, criteria may still be applied if genetic testing ruled out alternative causes
- If maternal T cells present, T lymphocyte profile is still considered T- (autologous T cells absent)

---

### PP5 - Reputable Source

**Not Applicable.** This criterion is not for use as recommended by ClinGen SVI VCEP Review Committee (PMID: 29543229).

---

## Benign Criteria

### BA1 - Allele Frequency >5%

**Original ACMG Summary:** Allele frequency is above 5% in population databases.

**VCEP Specification (Stand Alone):**
- gnomAD popmax filtering allele frequency **>0.00346**

Calculated using Whiffin/Ware calculator with:
- Prevalence: 1:5,000
- Allelic heterogeneity: 1
- Genetic heterogeneity: 0.03 (3.2% contribution to SCID per PIDTC 6901 cohort)
- Penetrance: 50%

---

### BS1 - Frequency Greater Than Expected

**Original ACMG Summary:** Allele frequency is greater than expected for disorder.

**VCEP Specification (Strong):**
- gnomAD popmax filtering allele frequency **>0.00078**
- Consider also bottleneck populations

Calculated using Whiffin/Ware calculator with:
- Prevalence: 1:50,000
- Allelic heterogeneity: 1
- Genetic heterogeneity: 0.03
- Penetrance: 100%

---

### BS2 - Observed in Healthy Adult

**Original ACMG Summary:** Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder.

**VCEP Specification (Supporting only):**
- Only apply when variant is observed **in the homozygous state** in a healthy adult

---

### BS3 - Functional Studies (No Effect)

**Not Applicable.** There is not a well-established functional study which can rule out all damaging effects on protein function.

---

### BS4 - Lack of Segregation

**Original ACMG Summary:** Lack of segregation in affected members of a family.

**VCEP Specification (Strong):** Can be applied without additional specifications.

---

### BP1-BP7 - Benign Supporting

| Criterion | Status | Comment |
|-----------|--------|---------|
| **BP1** | Not Applicable | DCLRE1C missense variants are a known mechanism of disease |
| **BP2** | Not Applicable | - |
| **BP3** | Not Applicable | No repetitive regions without known function |
| **BP4** | Not Applicable | - |
| **BP5** | Not Applicable | - |
| **BP6** | Not Applicable | Per ClinGen SVI VCEP Review Committee (PMID: 29543229) |
| **BP7** | **Supporting** | Applicable to synonymous and deep intronic variants (≥+7 donor, ≥-21 acceptor) predicted NOT to impact splicing by ≥2/3 in silico tools (GeneSplicer, MaxEntScan, NNSplice, SpliceAI, SSF, varSEAK). Nucleotide conservation not required. |

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

### Appendix A: PVS1 Flowchart for DCLRE1C

The PVS1 flowchart guides assignment of strength levels for predicted loss-of-function variants.

**Key Decision Points:**

1. **Variant Type:** Nonsense/Frameshift, Splice Site, Deletion, Duplication, or Initiation Codon
2. **NMD Prediction:** Whether the variant is predicted to undergo nonsense-mediated decay
3. **Exon Presence:** Whether the exon is present in biologically-relevant transcripts
4. **Protein Impact:** Whether truncated/altered region is critical to protein function
5. **Downstream Pathogenic Variants:** For variants not predicted to undergo NMD

**DCLRE1C-Specific Considerations:**
- NMD boundary: c.1106 (codon 369) in exon 13
- Last exon: Exon 14
- Deletion hotspot: Exons 1-3 and 1-4 (pseudogene recombination)

### Appendix B: Reference PMIDs

| Topic | PMID |
|-------|------|
| PVS1 Recommendations | 30192042 |
| PP1 Co-segregation | 30311386 |
| PP5/BP6 Not Applicable | 29543229 |
| PIDTC SCID Cohort | 30193840 |
| Deletion Hotspot | 19953608 |
| Functional Studies | 25917813, 15071507, 15731174, 26476407 |

### Appendix C: Population Frequency Thresholds Summary

| Criterion | Threshold | Strength |
|-----------|-----------|----------|
| BA1 | >0.00346 | Stand Alone |
| BS1 | >0.00078 | Strong |
| PM2 | <0.00003266 + no homozygotes | Supporting |

### Appendix D: SCID Diagnostic Criteria (PIDTC 2022)

For PP4 scoring, diagnostic criteria for SCID include:
- **Criterion 1:** T cell lymphopenia
- **Criterion 3:** Functional T cell impairment
- **Criterion 4:** Maternal T cell engraftment

Leaky SCID/Omenn syndrome criteria exclude Criterion 2.

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 2.1.0 | 10/1/2025 | Updated PM5 (Strong/Moderate/Supporting), PP4 tables, PM3 attachment, Likely Benign rules corrected |
| 2.0.0 | - | Added 1 Strong + 1 Supporting to Likely Benign (unintentional) |
| 1.0.0 | - | Initial release |

---

*This document was compiled from ClinGen SCID VCEP specifications and ClinGen SVI recommendations. For the most current version, please refer to the ClinGen website.*
