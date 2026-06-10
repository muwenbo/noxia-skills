# ClinGen Congenital Myopathies VCEP Variant Interpretation Guidelines for DNM2

**Version:** 1.0.0
**Released:** 8/7/2024
**Affiliation:** Congenital Myopathies VCEP
**Based on:** Richards et al., 2015 ACMG/AMP Guidelines

---

## Gene Information

| Attribute | Value |
|-----------|-------|
| **Gene** | DNM2 (HGNC:2974) |
| **HGNC Name** | dynamin 2 |
| **Transcript** | NM_001005361.3 |
| **Disease** | Centronuclear myopathy (MONDO:0018947) |
| **Inheritance** | Autosomal dominant inheritance |

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
| **All Levels** | **Not Applicable** |

**Comments:** Loss of function is not a mechanism of disease for DNM2-related AD Centronuclear myopathy.

---

### PS1 - Same Amino Acid Change

**Original ACMG Summary:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.

**Example:** Val->Leu caused by either G>C or G>T in the same codon.

**Caveat:** Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | Same amino acid change as a previously established pathogenic variant regardless of nucleotide change. No change from original ACMG. |
| **Moderate** | No change - use as originally described |
| **Supporting** | No change - use as originally described |

---

### PS2 - De Novo (Confirmed)

**Original ACMG Summary:** De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.

**Note:** Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Very Strong** | No change - use as originally described |
| **Strong** | De novo (both maternity and paternity confirmed) in a patient with the disease and no family history. No change from original ACMG. |
| **Moderate** | No change - use as originally described |
| **Supporting** | No change - use as originally described |

---

### PS3 - Functional Studies

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.

**Note:** Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | Strong may only be considered for variant-specific mouse models. Currently, no other assays are applicable at this strength. |
| **Moderate** | The two assays from PS3_Supporting may be stacked to reach a Moderate Strength |
| **Supporting** | Two specific assays are currently suggested to be applied at Supporting (see below) |

#### PS3_Supporting Approved Assays

**1. Oligomerization Assay**
- **Abnormal readout:** Increased dynamin stability compared to wild type dynamin
- **Normal readout:** Dynamin assembly/disassembly dynamics similar to wild type DNM2

**2. GTPase Activity Assay**
- **Abnormal readout:** Increased GTPase activity or increased stability compared to wild type dynamin
- **Normal readout:** GTPase activity and stability similar to wild type DNM2

#### Other Functional Analyses

If not listed above, it is acceptable to use PS3_Supporting for other functional analyses if:
- The assay has been validated by a known pathogenic and benign variant AND
- There is plausible reason that the function the assay is testing relates to the phenotype AND
- The assay conditions are likely to mimic the physiological environment

#### Approved Assay Instances

| Assay | PMID | Author | Year | Proposed Strength | Variants Evaluated |
|-------|------|--------|------|-------------------|-------------------|
| **Oligomerization** | 20529869 | Wang...Albanesi | 2010 | Supporting | p.Glu368Lys, p.Arg369Trp, p.Arg465Trp, p.Ala618Thr |
| **Oligomerization** | 24016602 | James...Jameson | 2014 | Supporting | p.Arg369Trp |
| **GTPase Activity** | 20529869 | Wang...Albanesi | 2010 | Supporting | p.Glu368Lys, p.Arg369Trp, p.Arg465Trp, p.Ala618Thr |

---

### PS4 - Prevalence in Affected

**Original ACMG Summary:** The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.

**Note 1:** Relative risk (RR) or odds ratio (OR), as obtained from case-control studies, is >5.0 and the confidence interval around the estimate of RR or OR does not include 1.0.

**Note 2:** In instances of very rare variants where case-control studies may not reach statistical significance, the prior observation of the variant in multiple unrelated patients with the same phenotype, and its absence in controls, may be used as moderate level of evidence.

**VCEP Specifications:** Please account for specific phenotype by increasing the weight of PS4 case counts.

#### Specific Phenotype Requirements

A Congenital myopathy panel should be run and negative for other variants (must include BIN1, RYR1, MTM1) **AND** at least two of these features:

1. Presence on Muscle Biopsy of: Oxidative activity and/or radial stranding with spokes on a wheel appearance with centrally nucleated muscle fibers
2. Distal weakness
3. Characteristic muscle imaging (See Figure 9 of Saade et al 2019 PMID: 31060725 for example)
4. Ophthalmoparesis and Ptosis (both of these must be observed to count this as one phenotype criteria)

#### PS4 Point System

| Proband Phenotype | Specificity | Points per Proband |
|-------------------|-------------|-------------------|
| PP4 Met (meets criteria above) | Specific | 0.5 points |
| One PP4 feature | Suggestive | 0.25 points |

#### PS4 Strength Thresholds

| Total Points | Strength Level |
|--------------|----------------|
| 0.25 points | PS4_Supporting |
| 0.5 points | PS4_Moderate |
| 1 point | PS4_Strong |

---

### PM1 - Mutational Hot Spot

**Original ACMG Summary:** Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **All Levels** | **Not Applicable** |

**Comments:** There are no defined hotspots or critical functional domains in DNM2 at this time.

---

### PM2 - Absent from Controls

**Original ACMG Summary:** Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

**Caveat:** Population data for indels may be poorly called by next generation sequencing.

**VCEP Specification (Supporting only):**

| Strength | Criteria |
|----------|----------|
| **Supporting** | PM2_Supporting may be applied if the minor allele frequency in population databases of at least 2000 alleles is absent (1 allele allowed) |

---

### PM3 - In Trans with Pathogenic

**Original ACMG Summary:** For recessive disorders, detected in trans with a pathogenic variant.

**Note:** This requires testing of parents (or offspring) to determine phase.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **All Levels** | **Not Applicable** |

**Comments:** Biallelic case counts should not be used for DNM2 (autosomal dominant inheritance).

---

### PM4 - Protein Length Changes

**Original ACMG Summary:** Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

**VCEP Specifications:** Loss of function is not a mechanism of disease for DNM2-associated centronuclear myopathy. PM4 is to be used with caution.

| Strength | Criteria |
|----------|----------|
| **Strong** | No change - use as originally described |
| **Moderate** | Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants |
| **Supporting** | No change - use as originally described |

---

### PM5 - Novel Missense at Same Residue

**Original ACMG Summary:** Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.

**Example:** Arg156His is pathogenic; now you observe Arg156Cys.

**Caveat:** Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | No change - use as originally described |
| **Moderate** | Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before |
| **Supporting** | No change - use as originally described |

---

### PM6 - De Novo (Assumed)

**Original ACMG Summary:** Assumed de novo, but without confirmation of paternity and maternity.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | No change - use as originally described |
| **Moderate** | Assumed de novo, but without confirmation of paternity and maternity |
| **Supporting** | No change - use as originally described |

---

### PP1 - Co-segregation

**Original ACMG Summary:** Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.

**Note:** May be used as stronger evidence with increasing segregation data.

**VCEP Specifications:** The segregation chart (adopted from Oza et al 2018 PMID:30311386) should be used to determine the strength level of the total number of affected segregations.

#### PP1 Thresholds for Autosomal Dominant

| Strength | Likelihood | LOD Score | Affected Segregations |
|----------|------------|-----------|----------------------|
| Supporting | 4:1 | 0.6 | 2 |
| Moderate | 16:1 | 1.2 | 4 |
| Strong | 32:1 | 1.5 | 5 |

#### Segregation Table (Phenocopy Not an Issue)

*LOD scores based on affected vs. unaffected recessive segregations*

| Affected Segregations | 0 Unaffected | 1 Unaffected | 2 Unaffected | 3 Unaffected | 4 Unaffected | 5 Unaffected |
|----------------------|--------------|--------------|--------------|--------------|--------------|--------------|
| 0 | 0 | 0.12 | 0.25 | 0.37 | 0.5 | 0.62 |
| 1 | 0.6 | 0.73 | 0.85 | 0.98 | 1.1 | 1.23 |
| 2 | 1.2 | 1.33 | 1.45 | 1.58 | 1.7 | 1.83 |
| 3 | 1.81 | 1.93 | 2.06 | 2.18 | 2.31 | 2.43 |
| 4 | 2.41 | 2.53 | 2.66 | 2.78 | 2.91 | 3.03 |
| 5 | 3.01 | 3.14 | 3.26 | 3.39 | 3.51 | 3.63 |
| 6 | 3.61 | 3.74 | 3.86 | 3.99 | 4.11 | 4.24 |
| 7 | 4.21 | 4.34 | 4.46 | 4.59 | 4.71 | 4.84 |
| 8 | 4.82 | 4.94 | 5.07 | 5.19 | 5.32 | 5.44 |
| 9 | 5.42 | 5.54 | 5.67 | 5.79 | 5.92 | 6.04 |
| 10 | 6.02 | 6.15 | 6.27 | 6.4 | 6.52 | 6.65 |

---

### PP2 - Missense in Constrained Gene

**Original ACMG Summary:** Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Supporting** | DNM2 is a gene that is constrained for missense variation (gnomAD v4.1 z=4.87). PP2 may be used for missense variants. |

---

### PP3 - Computational Evidence

**Original ACMG Summary:** Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).

**Caveat:** As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Supporting** | PP3 is met if the **REVEL score ≥ 0.7** OR if the variant is predicted to impact splicing using **SpliceAI score ≥ 0.5** |

---

### PP4 - Phenotype Specificity

**Original ACMG Summary:** Patient's phenotype or family history is highly specific for a disease with a single genetic etiology.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **All Levels** | **Not Applicable** |

**Comments:** PP4 is factored into the strength of PS4. See case counting specifications above.

---

### PP5 - Reputable Source

**Original ACMG Summary:** Reputable source recently reports variant as pathogenic, but the evidence is not available to the laboratory to perform an independent evaluation.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **All Levels** | **Not Applicable** |

This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee. (PubMed: 29543229)

---

## Benign Criteria

### BA1 - Allele Frequency >5%

**Original ACMG Summary:** Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

**VCEP Specification (Stand Alone):**

| Strength | Criteria |
|----------|----------|
| **Stand Alone** | The minor allele frequency using the filtering allele frequency of either exomes or genomes in gnomAD is **≥0.0000015**. All continental populations used in gnomAD should have at least 2000 alleles and >1 observation. |

---

### BS1 - Frequency Greater Than Expected

**Original ACMG Summary:** Allele frequency is greater than expected for disorder.

**VCEP Specification (Strong):**

| Strength | Criteria |
|----------|----------|
| **Strong** | The minor allele frequency using the filtering allele frequency of either exomes or genomes in gnomAD is **≥0.00000015**. All continental populations used in gnomAD should have at least 2000 alleles and >1 observation. |

---

### BS2 - Observed in Healthy Adult

**Original ACMG Summary:** Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age. No change from original ACMG. |
| **Moderate** | No change - use as originally described |
| **Supporting** | No change - use as originally described |

---

### BS3 - Functional Studies (No Effect)

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

**VCEP Specifications:** BS3_Supporting is **only** met if **both** of the specified assays have WT readouts.

| Strength | Criteria |
|----------|----------|
| **Supporting** | BS3_Supporting is met if **both** of these assays have WT readouts: |

**Required Assays for BS3_Supporting:**
1. **Oligomerization Assay:** DNM2 assembly/disassembly dynamics similar to wild type DNM2
2. **GTPase Activity Assay:** GTPase activity and stability similar to wild type DNM2

---

### BS4 - Lack of Segregation

**Original ACMG Summary:** Lack of segregation in affected members of a family.

**Caveat:** The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | Lack of segregation in affected members of a family. No change from original ACMG. |
| **Moderate** | No change - use as originally described |
| **Supporting** | No change - use as originally described |

---

### BP1-BP7 - Benign Supporting

| Criterion | Status | Specification |
|-----------|--------|---------------|
| **BP1** | Not Applicable | Both missense and truncating variants in DNM2 are disease-causing. |
| **BP2** | Applicable | Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder or observed in cis with a pathogenic variant in any inheritance pattern. No change from original ACMG. Available at Supporting, Moderate, and Strong levels. |
| **BP3** | Not Applicable | There are no regions in DNM2 where BP3 would apply. |
| **BP4** | Applicable (Supporting) | BP4 is met if the **REVEL score ≤ 0.15** OR if the variant is not predicted to impact splicing using SpliceAI. |
| **BP5** | Applicable | Variant found in a case with an alternate molecular basis for disease. No change from original ACMG. Available at Supporting, Moderate, and Strong levels. |
| **BP6** | Not Applicable | This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PubMed: 29543229). |
| **BP7** | Applicable (Supporting) | A synonymous variant for which SpliceAI predicts no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved. |

---

## Rules for Combining Criteria

### Pathogenic Classification

| Criteria Combination |
|---------------------|
| 1 Very Strong (PS2_Very Strong, PS3_Very Strong, PS4_Very Strong) **AND** ≥1 Strong (PS1, PS2, PS3, PS4, PM4_Strong, PM5_Strong, PM6_Strong, PP1_Strong, PP3_Strong, PP4_Strong) |
| 1 Very Strong **AND** ≥2 Moderate (PS1_Moderate, PS2_Moderate, PS3_Moderate, PS4_Moderate, PM4, PM5, PM6, PP1_Moderate, PP3_Moderate, PP4_Moderate) |
| 1 Very Strong **AND** 1 Moderate **AND** 1 Supporting (PS1_Supporting, PS2_Supporting, PS3_Supporting, PS4_Supporting, PM2_Supporting, PM4_Supporting, PM5_Supporting, PM6_Supporting, PP1, PP2, PP3, PP4) |
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
| ≥2 Strong (BS1, BS2, BS4, BP2_Strong, BP5_Strong, BP7_Strong) |
| 1 Stand Alone (BA1) |

### Likely Benign Classification

| Criteria Combination |
|---------------------|
| 1 Strong (BS1, BS2, BS4, BP2_Strong, BP5_Strong, BP7_Strong) **AND** 1 Supporting (BS2_Supporting, BS3_Supporting, BS4_Supporting, BP2, BP4, BP5, BP7) |
| ≥2 Supporting (BS2_Supporting, BS3_Supporting, BS4_Supporting, BP2, BP4, BP5, BP7) |

---

## Appendices

### Appendix A: Population Frequency Thresholds Summary

| Criterion | Threshold | Strength |
|-----------|-----------|----------|
| BA1 | ≥0.0000015 | Stand Alone |
| BS1 | ≥0.00000015 | Strong |
| PM2 | Absent (1 allele allowed in ≥2000 alleles) | Supporting |

### Appendix B: Computational Predictor Thresholds

| Criterion | Tool | Pathogenic Threshold | Benign Threshold |
|-----------|------|---------------------|------------------|
| PP3/BP4 | REVEL | ≥0.7 | ≤0.15 |
| PP3/BP4 | SpliceAI | ≥0.5 | Not predicted to impact splicing |

### Appendix C: Approved Functional Assays Summary

| Assay Type | PMID | Abnormal Readout | Normal Readout | Strength |
|------------|------|------------------|----------------|----------|
| Oligomerization | 20529869 | Increased dynamin stability | Assembly/disassembly similar to WT | Supporting |
| Oligomerization | 24016602 | Formation of higher-order oligomers | Similar to WT | Supporting |
| GTPase Activity | 20529869 | Increased GTPase activity | Activity similar to WT | Supporting |

### Appendix D: Reference PMIDs

1. **Wang L, Barylko B et al.** Dynamin 2 mutants linked to centronuclear myopathies form abnormally stable polymers. *J Biol Chem* (2010) 285(30):22753-7. PMID: 20529869
2. **James NG, Digman MA et al.** A mutation associated with centronuclear myopathy enhances the size and stability of dynamin 2 complexes in cells. *Biochim Biophys Acta* (2014) 1840(1):315-21. PMID: 24016602
3. **Bitoun M, Durieux AC et al.** Dynamin 2 mutations associated with human diseases impair clathrin-mediated receptor endocytosis. *Hum Mutat* (2009) 30(10):1419-27. PMID: 19623537
4. **Oza AM et al.** Expert specification of the ACMG/AMP variant interpretation guidelines for genetic hearing loss. *Hum Mutat* (2018) 39(11):1593-1613. PMID: 30311386
5. **Saade D et al.** Diagnostic value of muscle MRI pattern recognition in centronuclear myopathy. *Neuromuscul Disord* (2019) 29(5):385-393. PMID: 31060725
6. **Biesecker LG, Harrison SM.** The ACMG/AMP reputable source criteria for the interpretation of sequence variants. *Genet Med* (2018) 20(12):1687-1688. PMID: 29543229

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 8/7/2024 | Initial release |

---

*This document was compiled from ClinGen VCEP specifications and ClinGen SVI recommendations. For the most current version, please refer to the ClinGen website.*
