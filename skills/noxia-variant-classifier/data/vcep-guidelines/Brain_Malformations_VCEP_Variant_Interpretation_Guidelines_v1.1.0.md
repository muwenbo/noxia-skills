# ClinGen Brain Malformations VCEP Variant Interpretation Guidelines for AKT3, MTOR, PIK3CA, PIK3R2

**Version:** 1.1.0
**Released:** 8/19/2022
**Affiliation:** Brain Malformations VCEP (ClinGen Affiliation ID: 50020)
**Based on:** Richards et al., 2015 ACMG/AMP Guidelines
**Expert Panel Page:** https://www.clinicalgenome.org/affiliation/50020

---

## Gene Information

| Attribute | Value |
|-----------|-------|
| **Gene** | AKT3 (HGNC:393) |
| **HGNC Name** | AKT serine/threonine kinase 3 |
| **Transcript** | NM_005465.4 |
| **Disease** | Cerebral malformation (MONDO:0016054) |
| **Inheritance** | Autosomal Dominant (de novo / mosaic) |

| Attribute | Value |
|-----------|-------|
| **Gene** | MTOR (HGNC:3942) |
| **HGNC Name** | Mechanistic target of rapamycin kinase |
| **Transcript** | NM_004958.3 |
| **Disease** | Cerebral malformation (MONDO:0016054) |
| **Inheritance** | Autosomal Dominant (de novo / mosaic) |

| Attribute | Value |
|-----------|-------|
| **Gene** | PIK3CA (HGNC:8975) |
| **HGNC Name** | Phosphatidylinositol-4,5-bisphosphate 3-kinase catalytic subunit alpha |
| **Transcript** | NM_006218.3 |
| **Disease** | Cerebral malformation (MONDO:0016054) |
| **Inheritance** | Autosomal Dominant (de novo / mosaic) |

| Attribute | Value |
|-----------|-------|
| **Gene** | PIK3R2 (HGNC:8980) |
| **HGNC Name** | Phosphoinositide-3-kinase regulatory subunit 2 |
| **Transcript** | NM_005027.3 |
| **Disease** | Cerebral malformation (MONDO:0016054) |
| **Inheritance** | Autosomal Dominant (de novo / mosaic) |

> **Disease Mechanism:** The disease mechanism for these genes is **gain of function (GOF)**. LOF and/or haploinsufficiency have not been clearly identified as disease mechanisms underlying brain malformations related to these genes.

---

## Release Notes (v1.0 → v1.1)

The following criteria descriptions were modified for clarity based on feedback:
- **PS2** modified to make the distinction between PS2_Strong vs PS2_Moderate more clear and provide an example within the text
- **PS3** modified so it is clear the supplementary document applies to the SVI recommendation and not the animal model section
- **PS4** upper margins were modified to make it clear that curators should not round off any of the values in Table 2A since it is not possible to obtain a value that is .99 or .49
- **BA1 and BS1** calculations corrected, rationale provided in supplement
- **BS2** modified to make it clear that either homozygous instances in gnomAD or phenotyped family members can be utilized for this criterion
- **BP2** modified to indicate that this criterion can be used for either a cis or trans variant
- **BP4** modified to be consistent with detailed description provided later in the document

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

**VCEP Specifications:**

| Strength | Specification |
|----------|---------------|
| **Not Applicable** | LOF and/or haploinsufficiency have not been clearly identified as disease mechanisms underlying brain malformations related to these genes, so in general this rule is not applicable. The disease mechanism for these genes is gain of function (GOF). |

> **Caveats (general ACMG):**
> - Use caution interpreting LOF variants at the extreme 3' end of a gene
> - Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact
> - Use caution in the presence of multiple transcripts

---

### PS1 - Same Amino Acid Change

**Original ACMG Summary:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | No change from original ACMG definition. Previously established variant must meet criteria as pathogenic per BMVCEP criteria independent of this point. |

> **Caveat:** Beware of changes that impact splicing rather than at the amino acid/protein level.

---

### PS2 - De Novo (Confirmed)

**Original ACMG Summary:** De novo (both maternity and paternity confirmed) in a patient with the disease and no family history. Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | Award the PS2_Strong point if **Criteria 1 AND Criteria 2** are fulfilled. |
| **Moderate** | Award the PS2_Moderate point if Criteria 1 is fulfilled, **OR** if parents are not available but Criteria 2 is fulfilled. |

#### PS2 Criteria Definitions

- **Criteria 1:** The variant is present at a detectable allele fraction in a proband with the disease but is absent from parental samples with confirmed maternity and paternity.
- **Criteria 2:** The variant is present at a detectable allele fraction in an affected tissue sample but is absent from or detected at a lower allelic fraction in another tissue (e.g., if present in 5% of brain tissue but absent from the blood or skin, this point can be awarded).

> **Implementation Note:** For the sake of implementation, these criteria are intended to apply to high-confidence somatic mutations identified by the reporting CLIA laboratory. The expert panel recognizes that in practice there may be significant heterogeneity in the technical methods and thresholds used to identify such variants as "high confidence", and flags the need to establish consensus statistical frameworks (e.g., Phred-scaled genotype qualities) or experimental approaches (e.g., confirmation of somatic variants by sequencing on orthogonal platforms) by which quality thresholds can be consistently applied.

> **Note:** PM6 is addressed by PS2 and will not be used separately.

---

### PS3 - Functional Studies

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product. Note: Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | Award PS3 if the functional assay meets the acceptability criteria delimited in (PMID: 31892348) with specifications added by the BMVCEP for quality metrics and minimum validation controls required (Supplementary Document 1). Animal models are considered in a different manner — award PS4_Strong if the animal model generated with the variant of interest expressed in neural progenitors shows a complementary brain phenotype. |
| **Moderate** | Follow recommendations set forth by the SVI in conjunction with specifications added by the BMVCEP for quality metrics and minimum validation controls required (PMID: 31892348). Animal models are considered in a different manner — award PS4_Moderate if the animal model generated with the variant of interest expressed in non-neural tissues shows an increased cancer burden. |
| **Supporting** | Follow recommendations set forth by the SVI in conjunction with specifications added by the BMVCEP for quality metrics and minimum validation controls required (PMID: 31892348). |

#### Functional Assay Validation (PMID: 31892348)

1. The 4 classes of assays (phosphorylation, DEPTOR binding, cell survivability, cell proliferation) are considered "broadly accepted historically" for these genes.
2. Any publication within the spreadsheet can be used as evidence for a supporting level of evidence (PS3).
3. Any paper must have validation controls (positive and negative) in order to be used as evidence for a level above supporting:
   - Positive validation controls: variants classified as pathogenic/likely pathogenic (P/LP) independent of the PS3 criterion
   - Negative validation controls: variants classified as benign/likely benign independent of the BS3 criterion
   - **8–34 variants** are required for moderate evidence
   - **35+ variants** are required for strong evidence
4. For a publication to be used for any strength of evidence above supporting, it must also meet the minimum criteria below, depending on the type of evidence.

#### Assay-Specific Minimum Requirements

**Phosphorylation / DEPTOR Binding / Cell Survivability Assays:**
| Requirement | Specification |
|-------------|---------------|
| Basic Positive Control | WT necessary |
| Basic Negative Control | Empty vector or blank transfection can be used |
| Biological Replicates | Not necessary |
| Technical Replicates | Yes, documented in at least triplicate (contact researcher if not specifically mentioned in publication) |

**Cell Proliferation Assays:**
| Requirement | Specification |
|-------------|---------------|
| Basic Positive Control | WT necessary |
| Basic Negative Control | Empty vector or blank transfection can be used |
| Biological Replicates | Necessary for animal studies (e.g., each mouse is a replicate, need at least 2) |
| Technical Replicates | Necessary, multiple samples measured from the same animal or experiment done in triplicate (at least 3) |

> **Caveat:** Studies of cell lines derived from the affected patient as the only source of functional characterization are by themselves insufficient to provide strong evidence of pathogenicity. This is because cells derived from patient affected tissue are likely to exhibit the desired phenotype since the patient tissue exhibits the phenotype. It is therefore impossible to determine whether the variant of interest was solely responsible for that phenotype. Instead, functional readout of patient-derived cells are now included in PS4.

---

### PS4 - Prevalence in Affected

**Original ACMG Summary:** The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls. Note 1: Relative risk (RR) or odds ratio (OR), as obtained from case-control studies, is >5.0 and the confidence interval around the estimate of RR or OR does not include 1.0. Note 2: In instances of very rare variants where case-control studies may not reach statistical significance, the prior observation of the variant in multiple unrelated patients with the same phenotype, and its absence in controls, may be used as moderate level of evidence.

**VCEP Specifications:**

Points are assigned for phenotype according to Table 2A. Phenotype criteria can only be used if the variant is absent/rare from controls according to PM2 to ensure the variant is not simply present due to being common in the general population.

For PS4, for cases reported in the literature, assign each case to the **SINGLE category** below that is associated with the **highest point value** (Table 2A). The total score obtained for all reported cases with a particular variant will determine the strength of PS4 assigned according to the scale (Table 2B).

> **Important:** Curators should not round off any of the values in Table 2A since it is not possible to obtain a value that is .99 or .49.

#### Table 2A: PS4 Phenotype Point Values

*(Points assigned per case based on the highest applicable category)*

| Category | Points |
|----------|--------|
| *Details from VCEP-specified phenotype scoring table* | *See Supplementary Document* |

#### Table 2B: PS4 Strength Thresholds

| Strength | Point Range |
|----------|-------------|
| **Very Strong** | ≥16 points |
| **Strong** | 3.5–15.75 points |
| **Moderate** | 1.5–3.25 points |
| **Supporting** | 0.5–1.25 points |

---

### PM1 - Mutational Hot Spot

**Original ACMG Summary:** Located in a mutational hot spot and/or critical and well-established functional domain (e.g., active site of an enzyme) without benign variation.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Supporting** | A supporting point may be awarded if the variant of interest is located in an exon within one of the approved functional domains listed in Table 4 for each gene. |

> **Note:** The strength of this criterion has been modified from Moderate to **Supporting**. Specific residues subject to recurrent gain-of-function mutations are not covered by this criterion; these are instead accounted for by PS4.

#### Table 4: Critical Functional Domains by Gene

*(Gene-specific functional domain regions — see Supplementary Document for complete Table 4 with residue-level detail)*

---

### PM2 - Absent from Controls

**Original ACMG Summary:** Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium. Caveat: Population data for indels may be poorly called by next generation sequencing.

**VCEP Specification (Supporting only):**
- Absent/rare from controls in an ethnically-matched cohort population sample (**≤1 individual**)
- This criterion accounts for sequencing artifacts that may have been included in population databases. This number accounts for false calls due to sequencing/calling errors since the data sets from ExAC/gnomAD are from various sources and GATK calling is also known to call false positives (PMID: 22827831)
- This criterion has been downgraded to **Supporting** per recommendation by the SVI working group

---

### PM3 - In Trans with Pathogenic

**Original ACMG Summary:** For recessive disorders, detected in trans with a pathogenic variant. Note: This requires testing of parents (or offspring) to determine phase.

**VCEP Specifications:**

| Strength | Specification |
|----------|---------------|
| **Not Applicable** | Not applicable since disease-causing variants are heterozygous. |

---

### PM4 - Protein Length Changes

**Original ACMG Summary:** Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

**VCEP Specifications:**

| Strength | Specification |
|----------|---------------|
| **Not Applicable** | Although there have been reported in-frame deletion/insertions in these genes which cause the overgrowth phenotype, they are exceptionally rare. Most insertion/deletions are associated with a LoF disease mechanism and so this point will still not be used even though we recognize that it is possible that a variant is an in-frame indel that results in a GoF mechanism. |

---

### PM5 - Novel Missense at Same Residue

**Original ACMG Summary:** Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before. Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Moderate** | No change from original ACMG definition. Previously established variant must meet criteria as pathogenic per BMVCEP criteria independent of this point. |

---

### PM6 - De Novo (Assumed)

**Original ACMG Summary:** Assumed de novo, but without confirmation of paternity and maternity.

**VCEP Specifications:**

| Strength | Specification |
|----------|---------------|
| **Not Applicable** | This point is addressed according to PS2 and will not be used. |

---

### PP1 - Co-segregation

**Original ACMG Summary:** Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease. Note: May be used as stronger evidence with increasing segregation data.

**VCEP Specifications:**

| Strength | Specification |
|----------|---------------|
| **Not Applicable** | Not applicable since disease-causing variants are germline mosaic, de novo or mosaic. |

---

### PP2 - Missense in Constrained Gene

**Original ACMG Summary:** Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Supporting** | Missense constraint computed in ExAC/gnomAD was utilized. Award PP2 if the z-score > 3.09. |

> **Gene Applicability:** Applicable to **MTOR, PIK3CA, and AKT3** but **not PIK3R2**.

---

### PP3 - Computational Evidence

**Original ACMG Summary:** Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.). Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.

**VCEP Specifications:**

| Strength | Specification |
|----------|---------------|
| **Not Applicable** | This criterion is not applicable since these variants are GOF, and traditional mutation pathogenicity prediction algorithms focus on LOF mechanisms. Use of this criterion can be revisited if there emerges additional published experience with predictive algorithms specifically designed to detect gain of function mutations. |

---

### PP4 - Phenotype Specificity

**Original ACMG Summary:** Patient's phenotype or family history is highly specific for a disease with a single genetic etiology.

**VCEP Specifications:**

| Strength | Specification |
|----------|---------------|
| **Not Applicable** | Not applicable since this criterion is accounted for under PS4. |

---

### PP5 - Reputable Source

**Original ACMG Summary:** Reputable source recently reports variant as pathogenic, but the evidence is not available to the laboratory to perform an independent evaluation.

**VCEP Specifications:**

| Strength | Specification |
|----------|---------------|
| **Not Applicable** | This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PMID: 29543229). |

---

## Benign Criteria

### BA1 - Allele Frequency >5%

**Original ACMG Summary:** Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes, or ExAC.

**VCEP Specification (Stand Alone):**
- gnomAD popmax filtering allele frequency **>0.0926%**
- Note: This was adjusted from ACMG Guidelines due to maintaining the 5x threshold for benign (consistent with previously established guidelines)
- Rationale provided in Supplementary Table 3

---

### BS1 - Frequency Greater Than Expected

**Original ACMG Summary:** Allele frequency is greater than expected for disorder.

**VCEP Specification (Strong):**
- gnomAD popmax filtering allele frequency **>0.0185%**
- An allele frequency (>0.0185%) was approved (Supplementary Table 3)

---

### BS2 - Observed in Healthy Adult

**Original ACMG Summary:** Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | Award BS2 if **≥3 homozygotes** present in gnomAD **or** **≥3 heterozygous** in well phenotyped family members. Clinical laboratories are encouraged to accumulate more than 2 (≥3) instances of well phenotyped family members before applying this strong criterion. To be considered for this point, the variant should be either germline (most common), or somatic in a relevant tissue. Homozygous occurrences in gnomAD or ExAC can also be counted for this point (≥3). |

---

### BS3 - Functional Studies (No Effect)

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | Follow recommendations set forth by the SVI in conjunction with specifications added by the Brain Malformation Group for quality metrics and minimum validation controls required (PMID: 31892348) (Supplementary Document 1). |
| **Supporting** | Follow recommendations set forth by the SVI in conjunction with specifications added by the Brain Malformation Group for quality metrics and minimum validation controls required. |

---

### BS4 - Lack of Segregation

**Original ACMG Summary:** Lack of segregation in affected members of a family. Caveat: The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.

**VCEP Specifications:**

| Strength | Specification |
|----------|---------------|
| **Not Applicable** | Not applicable as these are de novo, germline mosaic or post-zygotic mutations. |

---

### BP1-BP7 - Benign Supporting

| Criterion | Status | Specification |
|-----------|--------|---------------|
| **BP1** | Not Applicable | Not applicable as LOF is not the disease mechanism. |
| **BP2** | Supporting | Observed in cis or trans with a known pathogenic variant in the same gene. |
| **BP3** | Not Applicable | This is not applicable for the genes specified since the exon regions do not have repetitive regions without a known function. |
| **BP4** | Supporting | Award BP4 for a synonymous, intronic positions (except canonical splice sites) or non-coding variants in the UTRs, if two out of three of the splicing prediction tools predicted no impact on splicing function. Not applicable for any variant type except for synonymous, intronic positions (except canonical splice sites) and non-coding variants in the UTRs. The splicing prediction tools used are: **varSEAK**, **spliceAI**, and **MaxEntScan**. |
| **BP5** | Supporting | No change from original ACMG definition. Observed in a case with an alternate molecular basis for disease in a different gene. |
| **BP6** | Not Applicable | This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PMID: 29543229). |
| **BP7** | Supporting | For synonymous, intronic positions (except canonical splice sites) and non-coding variants in the UTRs, if the nucleotide is non-conserved award this point. Not conserved is defined as the same nucleotide NOT present in all vertebrae or PhyloP score <0.1. |

---

## Rules for Combining Criteria

The Brain Malformations VCEP utilizes the **numerical point-based system** presented in the Tavtigian et al. publication (PMID: 32720330) for determining classification.

### Point Values

| Evidence Direction | Strength | Points |
|-------------------|----------|--------|
| Pathogenic | Supporting | +1 |
| Pathogenic | Moderate | +2 |
| Pathogenic | Strong | +4 |
| Pathogenic | Very Strong | +8 |
| Benign | Supporting | −1 |
| Benign | Moderate | −2 |
| Benign | Strong | −4 |
| Benign | Very Strong | −8 |

### Classification Ranges

| Point Range | Classification |
|-------------|---------------|
| ≥10 | Pathogenic (P) |
| 6 to 9 | Likely Pathogenic (LP) |
| 0 to 5 | Variant of Uncertain Significance (VUS) |
| −6 to −1 | Likely Benign (LB) |
| < −6 | Benign (B) |

---

## Appendices

### Appendix A: Criteria Summary Table

#### Pathogenic Criteria

| Criteria | Strength | Specification Type | Status |
|----------|----------|--------------------|--------|
| PVS1 | Very Strong | — | Not Applicable |
| PS4_VeryStrong | Very Strong | Disease-specific; Strength | ≥16 points (phenotype-based) |
| PS1 | Strong | None | No change |
| PS2 | Strong | Disease-specific; Strength | Criteria 1 AND Criteria 2 fulfilled |
| PS3 | Strong | Disease-specific | Functional assay per PMID: 31892348 |
| PS4 | Strong | Disease-specific | 3.5–15.75 points |
| PM1 | Supporting | Strength (downgraded) | Functional domains per Table 4 |
| PM2 | Supporting | Disease-specific | ≤1 individual in ethnically-matched cohort |
| PM3 | Moderate | — | Not Applicable |
| PM4 | Moderate | — | Not Applicable |
| PM5 | Moderate | None | No change |
| PM6 | Moderate | — | Not Applicable (addressed by PS2) |
| PS2_Moderate | Moderate | Disease-specific; Strength | Criteria 1 only, OR parents unavailable + Criteria 2 |
| PS3_Moderate | Moderate | Strength | Per SVI + BMVCEP; animal model in non-neural tissue |
| PS4_Moderate | Moderate | Strength | 1.5–3.25 points |
| PP1 | Supporting | — | Not Applicable |
| PP2 | Supporting | Disease-specific | z-score > 3.09 (MTOR, PIK3CA, AKT3 only) |
| PP3 | Supporting | — | Not Applicable |
| PP4 | Supporting | — | Not Applicable (under PS4) |
| PP5 | Supporting | — | Not Applicable (PMID: 29543229) |
| PS3_Supporting | Supporting | Strength | Per SVI + BMVCEP |
| PS4_Supporting | Supporting | Strength | 0.5–1.25 points |

#### Benign Criteria

| Criteria | Strength | Specification Type | Status |
|----------|----------|--------------------|--------|
| BA1 | Stand Alone | Disease-specific | >0.0926% |
| BS1 | Strong | Disease-specific | >0.0185% |
| BS2 | Strong | Disease-specific | ≥3 homozygotes in gnomAD or ≥3 heterozygous in phenotyped family |
| BS3 | Strong | Disease-specific | Per SVI + Brain Malformation Group (PMID: 31892348) |
| BS4 | Strong | — | Not Applicable |
| BP1 | Supporting | — | Not Applicable |
| BP2 | Supporting | Disease-specific | Observed in cis or trans with known pathogenic variant |
| BP3 | Supporting | — | Not Applicable |
| BP4 | Supporting | Disease-specific | Splicing prediction (varSEAK, spliceAI, MaxEntScan); 2/3 no impact |
| BP5 | Supporting | None | No change |
| BP6 | Supporting | — | Not Applicable (PMID: 29543229) |
| BP7 | Supporting | Disease-specific | Non-conserved nucleotide (PhyloP <0.1) |
| BS3_Supporting | Supporting | Strength | Per SVI + Brain Malformation Group (PMID: 31892348) |

### Appendix B: Population Frequency Thresholds Summary

| Criterion | Threshold | Strength |
|-----------|-----------|----------|
| BA1 | >0.0926% | Stand Alone |
| BS1 | >0.0185% | Strong |
| PM2 | ≤1 individual in ethnically-matched cohort | Supporting |

### Appendix C: Reference PMIDs

| PMID | Description |
|------|-------------|
| 31892348 | Functional assay acceptability criteria (PS3/BS3 validation framework) |
| 32720330 | Tavtigian et al. — Bayesian point-based classification system |
| 29543229 | ClinGen SVI recommendation — PP5/BP6 not for use |
| 22827831 | GATK false positive calling rates (PM2 justification) |

---

## Version History

| Version | Date | Notes |
|---------|------|-------|
| 1.0.0 | May 14, 2021 | Initial approved specifications |
| 1.1.0 | August 19, 2022 | Clarifications to PS2, PS3, PS4, BA1, BS1, BS2, BP2, BP4 |

---

*This document was compiled from ClinGen Brain Malformations VCEP specifications. For the most current version, please refer to the [ClinGen website](https://www.clinicalgenome.org/affiliation/50020/docs/assertion-criteria).*
