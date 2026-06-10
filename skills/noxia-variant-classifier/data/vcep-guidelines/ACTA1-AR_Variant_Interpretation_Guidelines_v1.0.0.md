# ClinGen Congenital Myopathies VCEP Variant Interpretation Guidelines for ACTA1 (Autosomal Recessive)

**Version:** 1.0.0
**Released:** 8/7/2024
**Affiliation:** Congenital Myopathies VCEP
**Based on:** Richards et al., 2015 ACMG/AMP Guidelines

---

## Gene Information

| Attribute | Value |
|-----------|-------|
| **Gene** | ACTA1 (HGNC:129) |
| **HGNC Name** | actin alpha 1, skeletal muscle |
| **Transcript** | NM_001100.4 |
| **Disease** | alpha-actinopathy (MONDO:0100084) |
| **Inheritance** | Autosomal recessive inheritance |

---

## General Comments

**Note on multiple Modes of Inheritance:** In general, the easiest way to tell whether a variant is AD or AR is to look at the clinical situation of probands with the variant, along with the family and inheritance. If it's de novo, it's much more likely to be AD and if it's observed with a second variant, it's much more likely to be AR. Loss of function variants are almost always associated with AR disease. For truncating/putative LOF variants, this is easier to determine, but some missense variants are observed that may have LOF functional consequence. The AD and AR specifications are listed separately.

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

**VCEP Specifications:** See the PVS1 flow chart. PVS1 should only be used for loss of function variants associated with autosomal recessive disease.

#### Strength Levels

| Strength | Criteria |
|----------|----------|
| **Very Strong (PVS1)** | Null variant (nonsense, frameshift, canonical +/-1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease. See PVS1 flowchart for specific guidance. |
| **Strong (PVS1_Strong)** | See PVS1 flowchart |
| **Moderate (PVS1_Moderate)** | See PVS1 flowchart |
| **Supporting (PVS1_Supporting)** | See PVS1 flowchart |

#### PVS1 Decision Tree for ACTA1

**Nonsense or Frameshift:**
- Predicted to undergo NMD (up to c.940, p.314):
  - Exon is present in biologically-relevant transcript(s) (NM_001100.4) → **PVS1**
  - Exon is absent from biologically-relevant transcript(s) → **N/A**
- Not predicted to undergo NMD:
  - Truncated/altered region is critical to protein function (no specified regions) → **PVS1_Strong**
  - Role of region in protein function is unknown:
    - LoF variants in this exon are frequent in the general population and/or exon is absent from biologically-relevant transcript(s) → **N/A**
    - LoF variants in this exon are not frequent in the general population and exon is present in biologically-relevant transcript(s):
      - Variant removes >10% of protein → **PVS1_Strong**
      - Variant removes <10% of protein → **PVS1_Moderate**

**Canonical GT-AG +/-1,2 Splice Sites:**
- Exon skipping or use of a cryptic splice site disrupts reading frame and is predicted to undergo NMD:
  - Exon is present in biologically-relevant transcript(s) → **PVS1**
  - Exon is absent from biologically-relevant transcript(s) → **N/A**
- Exon skipping or use of a cryptic splice site preserves reading frame (In-frame exons: 2, 4, 5):
  - Truncated/altered region is critical to protein function (no specified regions) → **PVS1_Strong**
  - Role of region in protein function is unknown:
    - LoF variants in this exon are frequent in the general population and/or exon is absent from biologically-relevant transcript(s) → **N/A**
    - LoF variants in this exon are not frequent in the general population and exon is present in biologically-relevant transcript(s):
      - Variant removes >10% of protein → **PVS1_Strong**
      - Variant removes <10% of protein → **PVS1_Moderate**
- Exon skipping or use of a cryptic splice site disrupts reading frame and is NOT predicted to undergo NMD:
  - Truncated/altered region is critical to protein function (no specified regions) → **PVS1_Strong**
  - Role of region in protein function is unknown:
    - LoF variants in this exon are frequent in the general population and/or exon is absent from biologically-relevant transcript(s) → **N/A**
    - LoF variants in this exon are not frequent in the general population and exon is present in biologically-relevant transcript(s):
      - Variant removes >10% of protein → **PVS1_Strong**
      - Variant removes <10% of protein → **PVS1_Moderate**

**Deletion (Single exon to full gene):**
- Single to multi exon deletion – Disrupts reading frame and is predicted to undergo NMD:
  - Exon is present in biologically-relevant transcript(s) → **PVS1**
  - Exon is absent from biologically-relevant transcript(s) → **N/A**
- Single to multi exon deletion – Preserves reading frame:
  - Truncated/altered region is critical to protein function (no specified regions) → **PVS1_Strong**
  - Role of region in protein function is unknown:
    - LoF variants in this exon are frequent in the general population and/or exon is absent from biologically-relevant transcript(s) → **N/A**
    - LoF variants in this exon are not frequent in the general population and exon is present in biologically-relevant transcript(s):
      - Variant removes >10% of protein → **PVS1_Strong**
      - Variant removes <10% of protein → **PVS1_Moderate**
- Single to multi exon deletion – Disrupts reading frame and is NOT predicted to undergo NMD:
  - Truncated/altered region is critical to protein function (no specified regions) → **PVS1_Strong**
  - Role of region in protein function is unknown:
    - LoF variants in this exon are frequent in the general population and/or exon is absent from biologically-relevant transcript(s) → **N/A**
    - LoF variants in this exon are not frequent in the general population and exon is present in biologically-relevant transcript(s):
      - Variant removes >10% of protein → **PVS1_Strong**
      - Variant removes <10% of protein → **PVS1_Moderate**
- Full gene deletion → **PVS1**

**Duplication (≥1 exon in size and must be completely contained within gene):**
- Proven in tandem:
  - Reading frame disrupted and NMD predicted to occur → **PVS1**
  - No or unknown impact on reading frame and NMD → **N/A**
- Presumed in tandem:
  - Reading frame presumed disrupted and NMD predicted to occur → **PVS1_Strong**
- Proven not in tandem → **N/A**

**Initiation Codon:**
- Different functional transcript uses alternative start codon → **N/A**
- No known alternative start codon in other transcripts:
  - ≥1 pathogenic variant(s) upstream of closest potential in-frame start codon → **PVS1_Moderate**
  - No pathogenic variant(s) upstream of closest potential in-frame start codon → **PVS1_Supporting**

---

### PS1 - Same Amino Acid Change

**Original ACMG Summary:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.

Example: Val->Leu caused by either G>C or G>T in the same codon.

**Caveat:** Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:** No change - use as originally described.

| Strength | Criteria |
|----------|----------|
| **Strong** | Same amino acid change as a previously established pathogenic variant regardless of nucleotide change. |
| **Moderate** | No change - use as originally described |
| **Supporting** | No change - use as originally described |

---

### PS2 - De Novo (Confirmed)

**Original ACMG Summary:** De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.

**Note:** Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.

**VCEP Specifications:** No change - use as originally described.

| Strength | Criteria |
|----------|----------|
| **Very Strong** | No change - use as originally described |
| **Strong** | De novo (both maternity and paternity confirmed) in a patient with the disease and no family history. |
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
| **Supporting** | There are no specific functional assays listed for the ACTA1 AR specifications; all should be used for AD specifications. However, it is acceptable to use PS3_Supporting for functional analyses if: (1) The assay has been validated by a known pathogenic and benign variant AND (2) There is plausible reason that the function the assay is testing relates to the phenotype AND (3) The assay conditions are likely to mimic the physiological environment. |

---

### PS4 - Prevalence in Affected

**Original ACMG Summary:** The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.

**Note 1:** Relative risk (RR) or odds ratio (OR), as obtained from case-control studies, is >5.0 and the confidence interval around the estimate of RR or OR does not include 1.0.

**Note 2:** In instances of very rare variants where case-control studies may not reach statistical significance, the prior observation of the variant in multiple unrelated patients with the same phenotype, and its absence in controls, may be used as moderate level of evidence.

**VCEP Specifications:** *Not Applicable*

**Comments:** These specifications are only for autosomal recessively inherited ACTA1 variants. Please use PM3 for case counting. There are separate specifications for AD ACTA1 variants.

---

### PM1 - Mutational Hot Spot

**Original ACMG Summary:** Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.

**VCEP Specifications:** *Not Applicable*

**Comments:** There are no defined hotspots or critical functional domains in ACTA1 at this time.

---

### PM2 - Absent from Controls

**Original ACMG Summary:** Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

**Caveat:** Population data for indels may be poorly called by next generation sequencing.

**VCEP Specifications:** If the mode of inheritance for the variant is unclear (largely with missense variants as loss of function variants are predicted to cause AR disease), use the more conservative AD cutoff for PM2_Supporting. See the AD specifications.

| Strength | Criteria |
|----------|----------|
| **Supporting** | PM2_Supporting may be applied if the minor allele frequency in population databases of at least 2000 alleles is **≤0.000005** for autosomal recessive |

---

### PM3 - In Trans with Pathogenic

**Original ACMG Summary:** For recessive disorders, detected in trans with a pathogenic variant.

**Note:** This requires testing of parents (or offspring) to determine phase.

**VCEP Specifications:** Please use the SVI-recommended PM3 chart to count observations. Points for each proband should be summed to get to a final PM3 strength. In order to count case counts for your variant of interest, it should be rare enough to not meet BS1. For variants that follow an autosomal dominant mode of inheritance, please see the autosomal dominant ACTA1 specifications.

#### PM3 Point System (Per Proband)

| Classification/Zygosity of Other Variant | Points Per Proband - Known in Trans | Points Per Proband - Phase Unknown |
|------------------------------------------|-------------------------------------|-----------------------------------|
| Likely Pathogenic/Pathogenic | 1.0 | 0.5 |
| Homozygous occurrence (max point 1.0) or Rare VUS on other allele | 0.5 | N/A |

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

**VCEP Specifications:** No change - use as originally described.

| Strength | Criteria |
|----------|----------|
| **Strong** | No change - use as originally described |
| **Moderate** | Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants. |
| **Supporting** | No change - use as originally described |

---

### PM5 - Novel Missense at Same Residue

**Original ACMG Summary:** Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.

Example: Arg156His is pathogenic; now you observe Arg156Cys.

**Caveat:** Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:** No change - use as originally described.

| Strength | Criteria |
|----------|----------|
| **Strong** | No change - use as originally described |
| **Moderate** | Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before. |
| **Supporting** | No change - use as originally described |

---

### PM6 - De Novo (Assumed)

**Original ACMG Summary:** Assumed de novo, but without confirmation of paternity and maternity.

**VCEP Specifications:** No change - use as originally described.

| Strength | Criteria |
|----------|----------|
| **Strong** | No change - use as originally described |
| **Moderate** | Assumed de novo, but without confirmation of paternity and maternity. |
| **Supporting** | No change - use as originally described |

---

### PP1 - Co-segregation

**Original ACMG Summary:** Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.

**Note:** May be used as stronger evidence with increasing segregation data.

**VCEP Specifications:** The segregation chart (adopted from Biesecker et al 2023 PMID: 38103548) should be used to determine the strength level of the total number of affected and unaffected segregations. In order to count unaffected segregations, the unaffected individuals can be heterozygous carriers or WT, but should have the same risk of inheriting the variant as the affected individuals (e.g. siblings in the same generation).

**Important:** The combination of PP1 and PP4 cannot exceed strong.

| Strength | Criteria |
|----------|----------|
| **Strong** | See segregation chart (Biesecker et al 2023) |
| **Moderate** | See segregation chart |
| **Supporting** | See segregation chart |

For full segregation guidance, please refer to Biesecker et al 2023 (PMID: 38103548).

---

### PP2 - Missense in Constrained Gene

**Original ACMG Summary:** Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.

**VCEP Specifications:** *Not Applicable*

**Comments:** PP2 may only be used for missense variants with an autosomal dominant mode of inheritance. See autosomal dominant specifications if this is applicable.

---

### PP3 - Computational Evidence

**Original ACMG Summary:** Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).

**Caveat:** As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Supporting** | PP3 is met if the **REVEL score ≥0.7** or if the variant is predicted to impact splicing using **SpliceAI score ≥0.5** |

---

### PP4 - Phenotype Specificity

**Original ACMG Summary:** Patient's phenotype or family history is highly specific for a disease with a single genetic etiology.

**VCEP Specifications:** The strength of PP4 should be determined based on the case with the most specific phenotype. It should only be applied once per variant, even if there are multiple cases that meet PP4 criteria. The combination of PP4 and PP1 is capped at strong.

PP4 follows the published SVI guidance from Biesecker et al 2023 (PMID: 38103548). For ACTA1, a conservative estimate of the diagnostic yield is 33%, which corresponds to +2 points and a moderate strength in Table 2 of this guidance.

| Strength | Criteria |
|----------|----------|
| **Strong** | If the proband meets PP4_Moderate criteria AND has had a comprehensive myopathy panel, exome, or genome testing that is negative for all other causes of myopathy, PP4 can be applied at strong, per the SVI guidance. The combination of PP1 and PP4 is capped at strong. |
| **Moderate** | PP4_Moderate is met with the presence of any of these features on **Muscle Biopsy**: Accumulated thin filaments, Intranuclear rods, Cores/fiber type disproportion, Zebra bodies |
| **Supporting** | If a biopsy demonstrates a presence of nemaline rods, this is suggestive of ACTA1-related congenital myopathy and can be given PP4 at a supporting level. |

---

### PP5 - Reputable Source

**Original ACMG Summary:** Reputable source recently reports variant as pathogenic, but the evidence is not available to the laboratory to perform an independent evaluation.

**VCEP Specifications:** *Not Applicable*

This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PMID: 29543229).

---

## Benign Criteria

### BA1 - Allele Frequency >5%

**Original ACMG Summary:** Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

**VCEP Specifications:** If the mode of inheritance for the variant is unclear (this largely applies to missense variants as loss of function variants are suspected to cause AR disease), use the more conservative AR cutoff for BA1.

| Strength | Criteria |
|----------|----------|
| **Stand Alone** | The minor allele frequency using the filtering allele frequency of either exomes or genomes in gnomAD is **≥0.0025** for AR variants. All continental populations in gnomAD used should have at least 2000 alleles and >1 observation. |

#### BA1 Exclusion Variants

The following well-known pathogenic variants are above the specified BA1 threshold and should NOT be classified as benign based on allele frequency alone:
- NM_001100.4(ACTA1):c.541del (p.Asp181fs)
- NM_001100.4(ACTA1):c.121C>T (p.Arg41*)

---

### BS1 - Frequency Greater Than Expected

**Original ACMG Summary:** Allele frequency is greater than expected for disorder.

**VCEP Specifications:** If the mode of inheritance for the variant is unclear (this largely applies to missense variants as loss of function variants are suspected to cause AR disease), use the more conservative AR cutoff for BS1.

| Strength | Criteria |
|----------|----------|
| **Strong** | The minor allele frequency using the filtering allele frequency of either exomes or genomes in gnomAD is **≥0.00025** for AR variants. All continental populations used in gnomAD should have at least 2000 alleles and >1 observation. |

---

### BS2 - Observed in Healthy Adult

**Original ACMG Summary:** Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

**VCEP Specifications:** No change - use as originally described.

| Strength | Criteria |
|----------|----------|
| **Strong** | Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age. |
| **Moderate** | No change - use as originally described |
| **Supporting** | No change - use as originally described |

---

### BS3 - Functional Studies (No Effect)

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

**VCEP Specifications:** *Not Applicable*

**Comments:** The VCEP has decided that lack of demonstrated effect in a functional assay should not count against the pathogenicity of an ACTA1 variant because of the numerous possible functions of Actin; therefore all specified functional assays will only be used as evidence for pathogenicity.

---

### BS4 - Lack of Segregation

**Original ACMG Summary:** Lack of segregation in affected members of a family.

**Caveat:** The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.

**VCEP Specifications:** No change - use as originally described.

| Strength | Criteria |
|----------|----------|
| **Strong** | Lack of segregation in affected members of a family. |
| **Moderate** | No change - use as originally described |
| **Supporting** | No change - use as originally described |

---

### BP1-BP7 - Benign Supporting

| Criterion | Status | Comment |
|-----------|--------|---------|
| **BP1** | *Not Applicable* | Both missense and truncating variants in ACTA1 are disease-causing. |
| **BP2** | Applicable (Supporting) | Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder or observed in cis with a pathogenic variant in any inheritance pattern. No change from original. |
| **BP3** | *Not Applicable* | There are no regions in ACTA1 where BP3 would apply. |
| **BP4** | Applicable (Supporting) | BP4 is met if the **REVEL score ≤0.15** or if the variant is not predicted to impact splicing using SpliceAI. |
| **BP5** | Applicable (Supporting) | Variant found in a case with an alternate molecular basis for disease. No change from original. |
| **BP6** | *Not Applicable* | This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PMID: 29543229). |
| **BP7** | Applicable (Supporting) | A synonymous variant for which SpliceAI predicts no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved. |

---

## Rules for Combining Criteria

### Pathogenic Classification

| Criteria Combination |
|---------------------|
| 1 Very Strong (PVS1, PS2_Very Strong, PM3_Very Strong) **AND** ≥1 Strong (PVS1_Strong, PS1, PS2, PS3, PM3_Strong, PM4_Strong, PM5_Strong, PM6_Strong, PP1_Strong) |
| 1 Very Strong (PVS1, PS2_Very Strong, PM3_Very Strong) **AND** ≥2 Moderate (PVS1_Moderate, PS1_Moderate, PS2_Moderate, PS3_Moderate, PM3, PM4, PM5, PM6, PP1_Moderate) |
| 1 Very Strong (PVS1, PS2_Very Strong, PM3_Very Strong) **AND** 1 Moderate (PVS1_Moderate, PS1_Moderate, PS2_Moderate, PS3_Moderate, PM3, PM4, PM5, PM6, PP1_Moderate) **AND** 1 Supporting (PVS1_Supporting, PS1_Supporting, PS2_Supporting, PS3_Supporting, PM2_Supporting, PM3_Supporting, PM4_Supporting, PM5_Supporting, PM6_Supporting, PP1, PP3, PP4) |
| 1 Very Strong (PVS1, PS2_Very Strong, PM3_Very Strong) **AND** ≥2 Supporting (PVS1_Supporting, PS1_Supporting, PS2_Supporting, PS3_Supporting, PM2_Supporting, PM3_Supporting, PM4_Supporting, PM5_Supporting, PM6_Supporting, PP1, PP3, PP4) |
| ≥2 Strong (PVS1_Strong, PS1, PS2, PS3, PM3_Strong, PM4_Strong, PM5_Strong, PM6_Strong, PP1_Strong) |
| 1 Strong (PVS1_Strong, PS1, PS2, PS3, PM3_Strong, PM4_Strong, PM5_Strong, PM6_Strong, PP1_Strong) **AND** ≥3 Moderate (PVS1_Moderate, PS1_Moderate, PS2_Moderate, PS3_Moderate, PM3, PM4, PM5, PM6, PP1_Moderate) |
| 1 Strong (PVS1_Strong, PS1, PS2, PS3, PM3_Strong, PM4_Strong, PM5_Strong, PM6_Strong, PP1_Strong) **AND** 2 Moderate (PVS1_Moderate, PS1_Moderate, PS2_Moderate, PS3_Moderate, PM3, PM4, PM5, PM6, PP1_Moderate) **AND** ≥2 Supporting (PVS1_Supporting, PS1_Supporting, PS2_Supporting, PS3_Supporting, PM2_Supporting, PM3_Supporting, PM4_Supporting, PM5_Supporting, PM6_Supporting, PP1, PP3, PP4) |
| 1 Strong (PVS1_Strong, PS1, PS2, PS3, PM3_Strong, PM4_Strong, PM5_Strong, PM6_Strong, PP1_Strong) **AND** 1 Moderate (PVS1_Moderate, PS1_Moderate, PS2_Moderate, PS3_Moderate, PM3, PM4, PM5, PM6, PP1_Moderate) **AND** ≥4 Supporting (PVS1_Supporting, PS1_Supporting, PS2_Supporting, PS3_Supporting, PM2_Supporting, PM3_Supporting, PM4_Supporting, PM5_Supporting, PM6_Supporting, PP1, PP3, PP4) |

### Likely Pathogenic Classification

| Criteria Combination |
|---------------------|
| 1 Very Strong (PVS1, PS2_Very Strong, PM3_Very Strong) **AND** 1 Moderate (PVS1_Moderate, PS1_Moderate, PS2_Moderate, PS3_Moderate, PM3, PM4, PM5, PM6, PP1_Moderate) |
| 1 Strong (PVS1_Strong, PS1, PS2, PS3, PM3_Strong, PM4_Strong, PM5_Strong, PM6_Strong, PP1_Strong) **AND** 1 Moderate (PVS1_Moderate, PS1_Moderate, PS2_Moderate, PS3_Moderate, PM3, PM4, PM5, PM6, PP1_Moderate) |
| 1 Strong (PVS1_Strong, PS1, PS2, PS3, PM3_Strong, PM4_Strong, PM5_Strong, PM6_Strong, PP1_Strong) **AND** ≥2 Supporting (PVS1_Supporting, PS1_Supporting, PS2_Supporting, PS3_Supporting, PM2_Supporting, PM3_Supporting, PM4_Supporting, PM5_Supporting, PM6_Supporting, PP1, PP3, PP4) |
| ≥3 Moderate (PVS1_Moderate, PS1_Moderate, PS2_Moderate, PS3_Moderate, PM3, PM4, PM5, PM6, PP1_Moderate) |
| 2 Moderate (PVS1_Moderate, PS1_Moderate, PS2_Moderate, PS3_Moderate, PM3, PM4, PM5, PM6, PP1_Moderate) **AND** ≥2 Supporting (PVS1_Supporting, PS1_Supporting, PS2_Supporting, PS3_Supporting, PM2_Supporting, PM3_Supporting, PM4_Supporting, PM5_Supporting, PM6_Supporting, PP1, PP3, PP4) |
| 1 Moderate (PVS1_Moderate, PS1_Moderate, PS2_Moderate, PS3_Moderate, PM3, PM4, PM5, PM6, PP1_Moderate) **AND** ≥4 Supporting (PVS1_Supporting, PS1_Supporting, PS2_Supporting, PS3_Supporting, PM2_Supporting, PM3_Supporting, PM4_Supporting, PM5_Supporting, PM6_Supporting, PP1, PP3, PP4) |
| 1 Strong (PVS1_Strong, PS1, PS2, PS3, PM3_Strong, PM4_Strong, PM5_Strong, PM6_Strong, PP1_Strong) **AND** 2 Moderate (PVS1_Moderate, PS1_Moderate, PS2_Moderate, PS3_Moderate, PM3, PM4, PM5, PM6, PP1_Moderate) |

### Benign Classification

| Criteria Combination |
|---------------------|
| ≥2 Strong (BS1, BS2, BS4) |
| 1 Stand Alone (BA1) |

### Likely Benign Classification

| Criteria Combination |
|---------------------|
| 1 Strong (BS1, BS2, BS4) **AND** 1 Supporting (BS2_Supporting, BS4_Supporting, BP2, BP4, BP5, BP7) |
| ≥2 Supporting (BS2_Supporting, BS4_Supporting, BP2, BP4, BP5, BP7) |

---

## Appendices

### Appendix A: Population Frequency Thresholds Summary

| Criterion | Threshold | Strength |
|-----------|-----------|----------|
| BA1 | ≥0.0025 (0.25%) | Stand Alone |
| BS1 | ≥0.00025 (0.025%) | Strong |
| PM2 | ≤0.000005 (0.0005%) | Supporting |

**Note:** All thresholds use gnomAD filtering allele frequency (exomes or genomes). All continental populations should have at least 2000 alleles and >1 observation.

### Appendix B: Computational Prediction Thresholds

| Criterion | Tool | Threshold | Direction |
|-----------|------|-----------|-----------|
| PP3 | REVEL | ≥0.7 | Pathogenic |
| PP3 | SpliceAI | ≥0.5 | Pathogenic (splicing) |
| BP4 | REVEL | ≤0.15 | Benign |
| BP4 | SpliceAI | No impact | Benign (splicing) |

### Appendix C: NMD Prediction

For ACTA1 (NM_001100.4), nonsense-mediated decay (NMD) is predicted for variants up to **c.940** (p.314).

### Appendix D: In-Frame Exons

The following exons result in in-frame transcripts when skipped: **Exons 2, 4, 5**

---

## References

1. Chan C, Fan J, et al. *Myopathy-inducing mutation H40Y in ACTA1 hampers actin filament structure and function.* **Biochim Biophys Acta** (2016) 1862(8):1453-8. PMID: 27112274

2. Oza AM, DiStefano MT, et al. *Expert specification of the ACMG/AMP variant interpretation guidelines for genetic hearing loss.* **Hum Mutat** (2018) 39(11):1593-1613. PMID: 30311386

3. Yao X, Grade S, et al. *His(73), often methylated, is an important structural determinant for actin. A mutagenic analysis of HIS(73) of yeast actin.* **J Biol Chem** (1999) 274(52):37443-9. PMID: 10601317

4. Clarke NF, Ilkovski B, et al. *The pathogenesis of ACTA1-related congenital fiber type disproportion.* **Ann Neurol** (2007) 61(6):552-61. PMID: 17387733

5. D'Amico A, Graziano C, et al. *Fatal hypertrophic cardiomyopathy and nemaline myopathy associated with ACTA1 K336E mutation.* **Neuromuscul Disord** (2006) 16(9-10):548-52. PMID: 16945537

6. Marston S, Mirza M, et al. *Functional characterisation of a mutant actin (Met132Val) from a patient with nemaline myopathy.* **Neuromuscul Disord** (2004) 14(2):167-74. PMID: 14733965

7. Domazetovska A, Ilkovski B, et al. *Intranuclear rod myopathy: molecular pathogenesis and mechanisms of weakness.* **Ann Neurol** (2007) 62(6):597-608. PMID: 17705262

8. Ilkovski B, Nowak KJ, et al. *Evidence for a dominant-negative effect in ACTA1 nemaline myopathy caused by abnormal folding, aggregation and altered polymerization of mutant actin isoforms.* **Hum Mol Genet** (2004) 13(16):1727-43. PMID: 15198992

9. Fan J, Chan C, et al. *Molecular Consequences of the Myopathy-Related D286G Mutation on Actin Function.* **Front Physiol** (2018) 9:1756. PMID: 30564146

10. Feng JJ, Ushakov DS, et al. *Direct visualisation and kinetic analysis of normal and nemaline myopathy actin polymerisation using total internal reflection microscopy.* **J Muscle Res Cell Motil** (2009) 30(1-2):85-92. PMID: 19418233

11. Ross JA, Levy Y, et al. *Impairments in contractility and cytoskeletal organisation cause nuclear defects in nemaline myopathy.* **Acta Neuropathol** (2019) 138(3):477-495. PMID: 31218456

12. Costa CF, Rommelaere H, et al. *Myopathy mutations in alpha-skeletal-muscle actin cause a range of molecular defects.* **J Cell Sci** (2004) 117(Pt 15):3367-77. PMID: 15226407

13. Bathe FS, Rommelaere H, et al. *Phenotypes of myopathy-related actin mutants in differentiated C2C12 myotubes.* **BMC Cell Biol** (2007) 8:2. PMID: 17227580

14. Biesecker LG, Byrne AB, et al. *ClinGen guidance for use of the PP1/BS4 co-segregation and PP4 phenotype specificity criteria for sequence variant pathogenicity classification.* **Am J Hum Genet** (2024) 111(1):24-38. PMID: 38103548

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 8/7/2024 | Initial release |

---

*This document was compiled from ClinGen VCEP specifications and ClinGen SVI recommendations. For the most current version, please refer to the [ClinGen website](https://clinicalgenome.org/).*
