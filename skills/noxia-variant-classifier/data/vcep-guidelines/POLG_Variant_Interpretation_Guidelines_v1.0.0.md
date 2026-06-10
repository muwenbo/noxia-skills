# ClinGen Mitochondrial Disease VCEP Variant Interpretation Guidelines for POLG

**Version:** 1.0.0
**Released:** 4/30/2020
**Affiliation:** Mitochondrial Diseases VCEP
**Based on:** Richards et al., 2015 ACMG/AMP Guidelines

---

## Gene Information

| Attribute | Value |
|-----------|-------|
| **Gene** | POLG (HGNC:9179) |
| **HGNC Name** | DNA polymerase gamma, catalytic subunit |
| **Transcript** | NM_002693.2 |
| **Disease** | Mitochondrial disease (MONDO:0044970) |
| **Inheritance** | Autosomal Recessive (primarily); Autosomal Dominant (rarely) |

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

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Very Strong** | Applied per PVS1 flowsheet of Abou Tayoun et al. |

---

### PS1 - Same Amino Acid Change

**Original ACMG Summary:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.

**Caveat:** Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | Same amino acid change as a previously established pathogenic variant regardless of nucleotide change |

---

### PS2 - De Novo (Confirmed)

**Original ACMG Summary:** De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.

**Note:** Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | De novo in a patient with the disease and no family history |

---

### PS3 - Functional Studies

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.

**VCEP Specifications:** *Not Applicable*

---

### PS4 - Prevalence in Affected

**Original ACMG Summary:** The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | Rarely, pathogenic variants cause disease in an AD manner. For these variants only: presence in 16 unrelated probands will be strong evidence |
| **Moderate** | For AD variants only: presence in 4 unrelated probands will be moderate evidence |
| **Supporting** | For AD variants only: presence in 2 unrelated probands will be supporting evidence |

**Note:** This will only be utilized when there is segregation evidence supporting autosomal dominant inheritance.

---

### PM1 - Mutational Hot Spot

**Original ACMG Summary:** Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.

**VCEP Specifications:** *Not Applicable*

---

### PM2 - Absent from Controls

**Original ACMG Summary:** Absent from controls (or at extremely low frequency if recessive) in population databases.

**VCEP Specification:**

| Strength | Criteria |
|----------|----------|
| **Moderate** | gnomAD popmax filtering allele frequency **<0.0005 (<0.05%)** |

---

### PM3 - In Trans with Pathogenic

**Original ACMG Summary:** For recessive disorders, detected in trans with a pathogenic variant.

**Note:** This requires testing of parents (or offspring) to determine phase.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Moderate** | Use per SVI guidance |

**Important Note:** T251I and P587L are almost always in cis.

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

---

### PM4 - Protein Length Changes

**Original ACMG Summary:** Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Moderate** | Protein length changes as a result of in-frame deletions/insertions in a nonrepeat region or stop-loss variants |

---

### PM5 - Novel Missense at Same Residue

**Original ACMG Summary:** Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.

**Caveat:** Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Moderate** | Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before |

---

### PM6 - De Novo (Assumed)

**Original ACMG Summary:** Assumed de novo, but without confirmation of paternity and maternity.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | De novo in a patient with the disease and no family history |
| **Moderate** | Assumed de novo, but without confirmation of paternity and maternity |

---

### PP1 - Co-segregation

**Original ACMG Summary:** Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.

**Note:** May be used as stronger evidence with increasing segregation data.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Supporting** | Further define "affected" as an individual in whom there is objective evidence of manifestations consistent with POLG-related disorders spectrum |

**POLG-Related Disorders Spectrum:**
- Alpers-Huttenlocher syndrome (AHS)
- Childhood myocerebrohepatopathy spectrum (MCHS)
- Myoclonic epilepsy myopathy sensory ataxia (MEMSA)
- Ataxia neuropathy spectrum (ANS)
- Progressive external ophthalmoplegia (PEO)

---

### PP2 - Missense in Constrained Gene

**Original ACMG Summary:** Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.

**VCEP Specifications:** *Not Applicable*

---

### PP3 - Computational Evidence

**Original ACMG Summary:** Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).

**Caveat:** As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Supporting** | Agree to utilize REVEL, with thresholds of **>0.75** for PP3 and **<0.15** for BP4, respectively. Will also utilize POLG pathogenicity prediction server if/when live again (PMID: 28480171); both tools (REVEL and server) will have to be in agreement to score |

---

### PP4 - Phenotype Specificity

**Original ACMG Summary:** Patient's phenotype or family history is highly specific for a disease with a single genetic etiology.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Moderate** | (1) Mitochondrial DNA depletion showing ≤20% of controls, OR (2) Multiple mitochondrial DNA deletions |
| **Supporting** | (1) Mitochondrial DNA depletion showing 20-50% of controls in children (<18 years of age), AND/OR (2) COX negative fibers in muscle in children and/or adults |

**Notes for PP4_Moderate:**
- Depletion and/or deletion analysis must be performed in muscle and/or liver; other tissues such as blood, fibroblast, and buccal are not acceptable
- Must be performed in child, as defined as <18 years old
- For both scenarios, will only apply if other mtDNA maintenance disorders have been excluded (exome sequencing or comprehensive panel-based testing)

**Notes for PP4_Supporting:**
- Will only apply if other mtDNA maintenance disorders have been excluded (exome sequencing or comprehensive panel-based testing)

---

### PP5 - Reputable Source

**Original ACMG Summary:** Reputable source recently reports variant as pathogenic, but the evidence is not available to the laboratory to perform an independent evaluation.

**VCEP Specifications:** *Not Applicable*

This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PMID: 29543229).

---

## Benign Criteria

### BA1 - Allele Frequency >5%

**Original ACMG Summary:** Allele frequency is above 5% in population databases.

**VCEP Specification (Stand Alone):**
- gnomAD popmax filtering allele frequency **>0.01 (>1%)**

---

### BS1 - Frequency Greater Than Expected

**Original ACMG Summary:** Allele frequency is greater than expected for disorder.

**VCEP Specification (Strong):**
- gnomAD popmax filtering allele frequency **>0.005 (>0.5%)** for autosomal recessive

---

### BS2 - Observed in Healthy Adult

**Original ACMG Summary:** Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | Observed in a healthy adult individual in the homozygous state AND/OR Normal mtDNA content |
| **Supporting** | Lack of COX negative fibers in muscle (children and adults) |

**Notes for BS2_Strong:**
1. Must be performed in muscle and/or liver; blood, fibroblast, and buccal not acceptable
2. Must be performed in children only - defined as <18 years old
3. A normal level is defined as >50%

---

### BS3 - Functional Studies (No Effect)

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

**VCEP Specifications:** *Not Applicable*

---

### BS4 - Lack of Segregation

**Original ACMG Summary:** Lack of segregation in affected members of a family.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | Lack of segregation in affected and/or treated members of a family |

---

### BP1-BP7 - Benign Supporting

| Criterion | Status | Specification |
|-----------|--------|---------------|
| **BP1** | Not Applicable | Missense variant in a gene for which primarily truncating variants are known to cause disease |
| **BP2** | Supporting | Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder or observed in cis with a pathogenic variant in any inheritance pattern |
| **BP3** | Supporting | In-frame deletions/insertions in a repetitive region without a known function |
| **BP4** | Supporting | Agree to utilize REVEL, with thresholds of >0.75 for PP3 and <0.15 for BP4, respectively. Will also utilize POLG pathogenicity prediction server if/when live again (PMID: 28480171); both tools (REVEL and server) will have to be in agreement to score |
| **BP5** | Supporting | Variant found in a case with an alternate molecular basis for disease |
| **BP6** | Not Applicable | This criterion is not for use as recommended by the ClinGen SVI VCEP Review Committee (PMID: 29543229) |
| **BP7** | Supporting | A synonymous (silent) variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved |

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

---

## Appendices

### Appendix A: Population Frequency Thresholds Summary

| Criterion | Threshold | Strength |
|-----------|-----------|----------|
| BA1 | >0.01 (>1%) | Stand Alone |
| BS1 | >0.005 (>0.5%) | Strong (AR) |
| PM2 | <0.0005 (<0.05%) | Moderate |

### Appendix B: Computational Predictor Thresholds

| Predictor | PP3 Threshold | BP4 Threshold |
|-----------|---------------|---------------|
| REVEL | >0.75 | <0.15 |
| POLG pathogenicity prediction server (PMID: 28480171) | Both must agree | Both must agree |

### Appendix C: POLG-Related Disorders Spectrum

| Disorder | Abbreviation |
|----------|--------------|
| Alpers-Huttenlocher syndrome | AHS |
| Childhood myocerebrohepatopathy spectrum | MCHS |
| Myoclonic epilepsy myopathy sensory ataxia | MEMSA |
| Ataxia neuropathy spectrum | ANS |
| Progressive external ophthalmoplegia | PEO |

### Appendix D: Important Cis Variants

The following variants are almost always in cis:
- T251I and P587L

### Appendix E: Reference PMIDs

- ClinGen SVI VCEP Review Committee: PMID 29543229
- POLG Pathogenicity Prediction Server: PMID 28480171
- PVS1 Flowsheet (Abou Tayoun et al.)

---

*This document was compiled from ClinGen VCEP specifications and ClinGen SVI recommendations. For the most current version, please refer to the ClinGen website.*
