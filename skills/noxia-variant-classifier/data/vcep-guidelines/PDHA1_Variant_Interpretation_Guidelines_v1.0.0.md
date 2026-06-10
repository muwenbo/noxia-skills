# ClinGen Mitochondrial Disease VCEP Variant Interpretation Guidelines for PDHA1

**Version:** 1.0.0
**Released:** 4/30/2020
**Affiliation:** Mitochondrial Diseases VCEP
**Based on:** Richards et al., 2015 ACMG/AMP Guidelines

---

## Gene Information

| Attribute | Value |
|-----------|-------|
| **Gene** | PDHA1 (HGNC:8806) |
| **HGNC Name** | pyruvate dehydrogenase E1 subunit alpha 1 |
| **Transcript** | NM_000284.4 |
| **Disease** | Pyruvate dehydrogenase deficiency (MONDO:0019169) |
| **Inheritance** | X-linked |

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

**VCEP Specifications:** *Not Applicable*

---

### PM1 - Mutational Hot Spot

**Original ACMG Summary:** Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Moderate** | Located in one of the following functional domains |

#### Functional Domains for PM1:

1. **Thiamine pyrophosphate (TPP) binding site:**
   - Amino acid positions: 118Y, 119R, 165G, 167V, 195G, 196D, 197G, 198A, 225N, 227Y, 292H

2. **α β heterodimer interface:**
   - Amino acid positions: 160F, 162G, 164N, 169A, 172P, 173L, 176G, 177I, 179L, 180A, 183Y, 202G, 203Q, 209N, 210M, 213L

3. **α2 β2 heterotetramer interface:**
   - Amino acid positions: 88R, 140G, 165G, 166I, 197G, 199A, 200N, 201Q, 202G, 205F, 209N, 213L, 228G, 229M, 230G, 231T, 245R, 296D, 300S

4. **Phosphorylation loop region:**
   - Amino acid positions: 287Y, 288R, 289Y, 290H, 291G, 292H, 293S, 295S, 296D, 297P, 298G, 299V, 300S, 301Y, 302R, 303T, 304R, 305E, 314S, 315D, 316P

---

### PM2 - Absent from Controls

**Original ACMG Summary:** Absent from controls (or at extremely low frequency if recessive) in population databases.

**VCEP Specification:**

| Strength | Criteria |
|----------|----------|
| **Moderate** | gnomAD popmax filtering allele frequency **<0.0000092 (<0.00092%)** |

---

### PM3 - In Trans with Pathogenic

**Original ACMG Summary:** For recessive disorders, detected in trans with a pathogenic variant.

**VCEP Specifications:** *Not Applicable*

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
| **Supporting** | Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease |

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
| **Supporting** | No gene-specific predictors; agree to utilize REVEL, with thresholds of **>0.75** for PP3 and **<0.15** for BP4, respectively |

---

### PP4 - Phenotype Specificity

**Original ACMG Summary:** Patient's phenotype or family history is highly specific for a disease with a single genetic etiology.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Supporting** | One of the following criteria are met (see below) |

**PP4 Supporting Criteria:**
1. Pyruvate radioactive enzyme assay showing decreased (defined as <3rd percentile of controls) for PDC, activated and decreased ratios (PDC/E3 and/or PDC/CS) in fibroblasts, muscle, and/or lymphocytes
2. Other assays showing decrease in PDC activity (i.e., western blot, immunocapture, and activity; commercial kits for research)
3. Abnormally high pyruvate and/or pyruvate/lactate ratio

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
- gnomAD popmax filtering allele frequency **>0.00092 (>0.092%)**

---

### BS1 - Frequency Greater Than Expected

**Original ACMG Summary:** Allele frequency is greater than expected for disorder.

**VCEP Specification (Strong):**
- gnomAD popmax filtering allele frequency **>0.000092 (>0.0092%)**

---

### BS2 - Observed in Healthy Adult

**Original ACMG Summary:** Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | Observed in at least two healthy male adults. **Note:** Individual's phenotype is well-characterized (not just seen in database of presumed healthy individuals) AND/OR ≥16 hemizygotes in gnomAD |
| **Supporting** | Observed in 4-15 hemizygotes in gnomAD AND/OR Pyruvate radioactive enzyme assay showing normal (defined as >3rd percentile of controls) for PDC, activated and normal ratios (PDC/E3 and/or PDC/CS) in fibroblasts with no evidence of skewed X-inactivation in fibroblasts |

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
| **BP2** | Not Applicable | Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder or observed in cis with a pathogenic variant in any inheritance pattern |
| **BP3** | Supporting | In-frame deletions/insertions in a repetitive region without a known function |
| **BP4** | Supporting | No gene-specific predictors; agree to utilize REVEL, with thresholds of >0.75 for PP3 and <0.15 for BP4, respectively |
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
| BA1 | >0.00092 (>0.092%) | Stand Alone |
| BS1 | >0.000092 (>0.0092%) | Strong |
| PM2 | <0.0000092 (<0.00092%) | Moderate |

### Appendix B: Computational Predictor Thresholds

| Predictor | PP3 Threshold | BP4 Threshold |
|-----------|---------------|---------------|
| REVEL | >0.75 | <0.15 |

### Appendix C: PM1 Functional Domain Summary

| Domain | Amino Acid Positions |
|--------|---------------------|
| TPP binding site | 118Y, 119R, 165G, 167V, 195G, 196D, 197G, 198A, 225N, 227Y, 292H |
| α β heterodimer interface | 160F, 162G, 164N, 169A, 172P, 173L, 176G, 177I, 179L, 180A, 183Y, 202G, 203Q, 209N, 210M, 213L |
| α2 β2 heterotetramer interface | 88R, 140G, 165G, 166I, 197G, 199A, 200N, 201Q, 202G, 205F, 209N, 213L, 228G, 229M, 230G, 231T, 245R, 296D, 300S |
| Phosphorylation loop region | 287Y, 288R, 289Y, 290H, 291G, 292H, 293S, 295S, 296D, 297P, 298G, 299V, 300S, 301Y, 302R, 303T, 304R, 305E, 314S, 315D, 316P |

### Appendix D: Reference PMIDs

- ClinGen SVI VCEP Review Committee: PMID 29543229
- PVS1 Flowsheet (Abou Tayoun et al.)

---

*This document was compiled from ClinGen VCEP specifications and ClinGen SVI recommendations. For the most current version, please refer to the ClinGen website.*
