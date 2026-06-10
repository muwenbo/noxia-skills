# ClinGen Monogenic Diabetes Expert Panel Variant Interpretation Guidelines for HNF1A

**Version:** 3.1.0
**Released:** 10/10/2025
**Affiliation:** Monogenic Diabetes VCEP
**Based on:** Richards et al., 2015 ACMG/AMP Guidelines

---

## Gene Information

| Attribute | Value |
|-----------|-------|
| **Gene** | HNF1A (HGNC:11621) |
| **HGNC Name** | HNF1 homeobox A |
| **Transcript** | NM_000545.8 |
| **Disease** | Monogenic diabetes (MONDO:0015967) |
| **Inheritance** | Autosomal Dominant |

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

## Important Phenotype Requirements

For multiple criteria (PS4, PP1, PP4), the phenotype of affected individuals must include diabetes **without clear evidence of an autoimmune etiology**. Evidence of autoimmune etiology includes:

- One or more positive diabetes autoantibodies (IA-2A, ZnT8A+, GAD)
- Very low or negative C-peptide, defined as:
  - Fasting or non-fasting random C-peptide <200 pmol/L or 0.6 ng/mL
  - Urinary C-peptide/creatinine ratio <0.2 nmol/mmol

---

## Pathogenic Criteria

### PVS1 - Null Variant

**Original ACMG Summary:** Null variant (nonsense, frameshift, canonical ±1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.

**Caveats:**
- Beware of genes where LOF is not a known disease mechanism (e.g., GFAP, MYH7)
- Use caution interpreting LOF variants at the extreme 3' end of a gene
- Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact
- Use caution in the presence of multiple transcripts

**VCEP Specifications:** Use HNF1A PVS1 decision tree. Per recommendations from the SVI, when RNA analysis demonstrates abnormal splicing from non-canonical splice site variants, apply PS3 instead of PVS1.

#### Strength Levels

| Strength | Criteria |
|----------|----------|
| **Very Strong (PVS1)** | See detailed specifications below |
| **Strong (PVS1_Strong)** | See detailed specifications below |
| **Supporting (PVS1_Supporting)** | See detailed specifications below |

#### PVS1 - Very Strong

Apply PVS1 to:

1. **Nonsense or frameshift variants occurring 5' of c.1768**
   - Variants generating PTCs 3' of c.1714 of NM_000545.8 (which includes the last 55 nucleotides of exon 9 and all of exon 10) are not expected to cause NMD
   - The transactivation domain (TAD) of the protein overlaps with this region
   - The last 55 nucleotides of exon 9 (c.1714-1768) is enriched for disease-causing variants and loss-of-function variants in this region have been found in patients/families with a MODY phenotype
   - Therefore, "very strong" level of evidence will be used for loss-of-function variants 5' of c.1768 regardless of where the premature termination codon occurs

2. **Exon skipping or use of a cryptic splice site that preserves reading frame AND Single to multi-exon deletion that preserves reading frame**
   - Apply PVS1 for exon skipping or single to multi exon deletion involving **exons 1-9**
   - Deletions of exon 1 would lead at least to loss of the initiation codon
   - Deletions of single exons 2, 3, 4, 5, 6, 8 or 9 all cause frameshift, and thus PVS1 would be used
   - In HNF1A, only exon 7 (LRG_522t1) is surrounded by introns of the same phase. Skipping or deletion of exon 7 would remove 64 amino acids in the TAD, which is >10% of the protein and 18% of the TAD. Given the significance of the TAD, PVS1 is still used instead of PVS1_Strong

3. **Initiation codon variants**
   - Apply PVS1 to initiation codon variants
   - Four initiation codon variants have been identified in patients with a MODY phenotype
   - The closest potential in-frame start codon is p.Met118
   - Starting the protein at p.Met118 would remove 18% of the protein, including the entire dimerization domain
   - There are many P/LP variants upstream of p.Met118

#### PVS1_Strong

Apply PVS1_Strong to:

1. **Nonsense variants at c.1803 (p.601) and 5'** AND **frameshift variants at c.1854 (p.618) and 5'**
   - The distinction of nonsense and frameshift variants was made following a careful review of the phenotypes of individuals with loss-of-function variants in exon 10
   - The addition of new amino acids from a frameshift will disrupt the TAD and cause a MODY phenotype more so than the deletion of a small part of the end of the TAD
   - Moderate phenotypic evidence was applied to the c.1802del (p.601Ter) variant, but the individual with the next nonsense variant (p.Gln625Ter) was unaffected
   - Frameshift variants at p.Ile618 and 5' have been identified in patients with a phenotype consistent with MODY

2. **Deletions of exon 10 and splicing variants that would predict the skipping of exon 10**
   - A deletion of exon 10 would remove part of the TAD but less than 10% of the protein
   - Since the TAD is critical to protein function, and variants that disrupt all of exon 10 have been found in patients with a MODY phenotype, PVS1_Strong is used
   - This specification is in accordance with Tayoun's recommendation to use PVS1_Strong in cases in which the truncated region is critical to protein function

#### PVS1_Supporting

Apply PVS1_Supporting to:
- Nonsense variants occurring **3' of c.1803 (p.601)**
- Frameshift variants occurring **3' of c.1854 (p.618)**
- Limited evidence of patients with MODY phenotype at this time

---

### PS1 - Same Amino Acid Change

**Original ACMG Summary:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.

**Example:** Val->Leu caused by either G>C or G>T in the same codon.

**Caveat:** Beware of changes that impact splicing rather than at the amino acid/protein level.

#### Strength Levels

| Strength | Criteria |
|----------|----------|
| **Strong** | Applicable for a same amino acid change if the previously established variant is classified as **pathogenic** by ClinGen MDEP specifications |
| **Moderate** | Applicable for a same amino acid change if the previously established variant is classified as **likely pathogenic** by ClinGen MDEP specifications |
| **Supporting** | See splicing variant specifications below |

**For splicing variants:** PS1 can be applied for canonical and non-canonical splicing variants that have a SpliceAI score within 10% of the original variant, or a greater predicted deleterious impact than the comparison (likely) pathogenic variant. See Table 2 from PMID: 37352859 for determining when PS1 should be applied at the Strong, Moderate, or Supporting level in these instances.

---

### PS2 - De Novo (Confirmed)

**Original ACMG Summary:** De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.

**Note:** Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.

**VCEP Specifications:**
- Use SVI recommended point-based system with MDEP specifications for "Phenotype Consistency"
- **Do not apply PS2** if the proband has an affected parent with any of the following:
  - Affected parent meets PP4 specifications
  - Parent is described as having similarly atypical diabetes to the proband
  - Parent was diagnosed with non-autoimmune diabetes before age 30

#### PS2/PM6 Point System

**Table 1: Points awarded per de novo occurrence**

| Phenotypic Consistency | De novo with confirmed parental relationships | De novo with unconfirmed parental relationships |
|------------------------|----------------------------------------------|------------------------------------------------|
| Phenotype highly specific for gene | 2 points | 1 point |
| Phenotype consistent with gene but not highly specific | 1 point | 0.5 points |

*Note: These points are not equivalent to the points used to classify a variant per the Tavtigian et al 2020 "Fitting a naturally scaled point system to the ACMG/AMP variant classification guidelines"*

**Table 2: Evidence Strength Thresholds**

| Points | Strength Level |
|--------|----------------|
| 0.5 | Supporting (PS2_Supporting or PM6_Supporting) |
| 1.0 | Moderate (PS2_Moderate or PM6) |
| 2.0 | Strong (PS2 or PM6_Strong) |
| 4.0 | Very Strong (PS2_VeryStrong or PM6_VeryStrong) |

---

### PS3 - Functional Studies

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.

**Note:** Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.

**VCEP Specifications:** Applied at the strong level for variants with RNA and in silico evidence of aberrant splicing. Otherwise, applied at the supporting level as described in the Supporting specification, except as noted in the Moderate specification.

#### Strength Levels

| Strength | Criteria |
|----------|----------|
| **Strong** | Applicable to non-canonical splice site variants that have RNA and in silico evidence of aberrant splicing |
| **Moderate** | Currently applicable for variants with luciferase assay data (evidence of decreased transactivation ≤40% of wild type) by the Gloyn/Oxford group (Althari et al. 2020). This upgrade from supporting is based on a validation conducted according to the guidelines by Brnich et al. 2019 |
| **Supporting** | See approved functional studies below |

#### Approved Functional Assays (PS3_Supporting)

1. **Luciferase assays for transactivation:**
   - Less than 40% activity of wildtype (WT)
   - Assays should include controls for WT, T2DM-risk, and known MODY variants

2. **EMSA for DNA binding:**
   - Less than 40% activity of WT
   - Recommended positive controls for reduced DNA binding activity (use at least two):
     - c.335C>T (p.Pro112Leu)
     - c.608G>A (p.Arg203His)
     - c.787C>T (p.Arg263Cys)
     - c.686G>A (p.Arg229Gln)

3. **Western blotting and indirect immunofluorescence for protein expression and localization:**
   - Determining appropriate thresholds for protein expression is more difficult due to variability in results between experimental protocols
   - Altered protein expression can be indirectly captured through the read-out from transactivation assay
   - Reduced protein expression can provide an explanation for reduced transactivation
   - When exploring protein mis-localization, use c.589_615del (p.Lys197_Lys205del) as positive control for impaired nuclear localization (cytosolic retention)

---

### PS4 - Prevalence in Affected

**Original ACMG Summary:** The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.

**Note 1:** Relative risk (RR) or odds ratio (OR), as obtained from case-control studies, is >5.0 and the confidence interval around the estimate of RR or OR does not include 1.0.

**Note 2:** In instances of very rare variants where case-control studies may not reach statistical significance, the prior observation of the variant in multiple unrelated patients with the same phenotype, and its absence in controls, may be used as moderate level of evidence.

**VCEP Specifications:**
- Variant should meet **PM2_Supporting** in order to use PS4 at any level
- Careful review of gnomAD QC data may be necessary to assess whether variant is real or an artifact, especially if variant is in a polyC region
- Phenotype of affected individuals must include diabetes, without clear evidence of an autoimmune etiology (see Important Phenotype Requirements above)

#### Strength Levels

| Strength | Criteria |
|----------|----------|
| **Strong** | ≥7 unrelated occurrences |
| **Moderate** | 4-6 unrelated occurrences |

---

### PM1 - Mutational Hot Spot

**Original ACMG Summary:** Located in a mutational hot spot and/or critical and well-established functional domain (e.g., active site of an enzyme) without benign variation.

#### Strength Levels

| Strength | Criteria |
|----------|----------|
| **Moderate** | Variants in residues that directly bind DNA (see list below) |
| **Supporting** | Variants in defined regions in the DNA binding and dimerization domains (see list below) |

#### PM1_Moderate - DNA Binding Residues

Apply PM1 at moderate level for variants in residues that directly bind DNA:
- Gln130, Arg131, Glu132, His143, Leu144, Ser145, Gln146, His147, Leu148, Asn149
- Lys155, Thr156, Gln157, Lys158
- Arg203, Phe204, Lys205, Trp206
- Arg263, Val264, Tyr265, Asn270, Arg271, Arg272, Lys273

#### PM1_Supporting - Functional Domains and Promoter Regions

**Protein domains:**
- **Dimerization domain:** codons 1-32 (NM_000545.8)
- **Subset of DNA binding domains:** codons 107-174 and 201-280

**Transcription factor binding sites in the promoter:**
- c.-187 to c.-195 (AP1 binding site)
- c.-209 to c.-227 (Overlapping HNF3 & NF-Y sites)
- c.-238 to c.-259 (HNF1A binding site)
- c.-276 to c.-288 (HNF4A binding site)

---

### PM2 - Absent from Controls

**Original ACMG Summary:** Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

**Caveat:** Population data for indels may be poorly called by next generation sequencing.

**VCEP Specifications:**
- Recommend using as **supporting level of evidence only** (PM2_Supporting) per ClinGen guidance
- Per guidance from ClinGen/SVI, PM2_Supporting + PVS1 is sufficient evidence of a variant being likely pathogenic
- Recommend investigating the genotype metrics in gnomAD for variants that have been flagged for having failed one or more quality parameters, as it is possible that some of these filtered variants are actually real
- The number of filtered alleles can be counted to determine whether PM2_Supporting would be met even if they were genuine calls
- If the filtered calls are sufficient in number to not meet PM2_Supporting, then do not use it
- Because it is also possible that these calls are false positives, do not use filtered variants to support BA1 or BS1

#### PM2_Supporting Threshold

| Criterion | Threshold |
|-----------|-----------|
| **PM2_Supporting** | gnomAD Grpmax FAF ≤ 1:333,000 (≤ 0.000003 or 0.0003%) |

---

### PM3 - In Trans with Pathogenic

**Original ACMG Summary:** For recessive disorders, detected in trans with a pathogenic variant.

**Note:** This requires testing of parents (or offspring) to determine phase.

**VCEP Specifications:** *Not Applicable* - HNF1A-related monogenic diabetes follows autosomal dominant inheritance.

---

### PM4 - Protein Length Changes

**Original ACMG Summary:** Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

#### Strength Levels

| Strength | Criteria |
|----------|----------|
| **Moderate** | For deletions/insertions of **more than one amino acid** in a non-repeat region |
| **Supporting** | For **single amino acid** deletions/insertions |

---

### PM5 - Novel Missense at Same Residue

**Original ACMG Summary:** Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.

**Example:** Arg156His is pathogenic; now you observe Arg156Cys.

**Caveat:** Beware of changes that impact splicing rather than at the amino acid/protein level.

#### Strength Levels

| Strength | Criteria |
|----------|----------|
| **Strong** | Applicable once **two amino acid changes** have been classified as pathogenic at the same amino acid residue |
| **Moderate** | The novel amino acid change must have a **Grantham distance greater than or equal to** the previously classified pathogenic variant |
| **Supporting** | Apply if the previously classified amino acid change is **likely pathogenic** (rather than pathogenic), OR if the previously classified variant is pathogenic but has a **greater Grantham distance** |

---

### PM6 - De Novo (Assumed)

**Original ACMG Summary:** Assumed de novo, but without confirmation of paternity and maternity.

**VCEP Specifications:** *Not Applicable* - Subsumed by PS2. Use the PS2/PM6 point-based system described above.

---

### PP1 - Co-segregation

**Original ACMG Summary:** Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.

**Note:** May be used as stronger evidence with increasing segregation data.

**VCEP Specifications:** Phenotype of affected individuals must include diabetes, without clear evidence of an autoimmune etiology (see Important Phenotype Requirements above).

#### PP1 Thresholds (Jarvik and Browning)

| Strength | Single Family | >1 Family |
|----------|---------------|-----------|
| **Strong** | ≤ 1/32 (5 meioses) | ≤ 1/16 (4 meioses) |
| **Moderate** | ≤ 1/16 (4 meioses) | ≤ 1/8 (3 meioses) |
| **Supporting** | ≤ 1/8 (3 meioses) | ≤ 1/4 (2 meioses) |

---

### PP2 - Missense in Constrained Gene

**Original ACMG Summary:** Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.

**VCEP Specifications:** *Not Applicable*

**Comments:** Missense variants account for 55% of all published pathogenic variants in this gene (Colclough et al 2013), however the constraint score for HNF1A (gene) is 1.07, which is not significant; therefore, this criterion is not supported at this time. The low constraint score is most likely due to high tolerance for missense variants in the transactivation domain (see PM1 section). There are significantly more pathogenic missense variants in the DNA binding and dimerization domains, which are much less tolerant to missense variation. This may be updated in the future if domain-specific scores can be generated.

---

### PP3 - Computational Evidence

**Original ACMG Summary:** Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).

**Caveat:** As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.

#### PP3_Supporting

| Variant Type | Tool | Threshold |
|--------------|------|-----------|
| Missense variants | REVEL | ≥ 0.70 |
| Non-canonical splicing variants | SpliceAI | > 0.2 |
| Synonymous variants | SpliceAI | > 0.2 |

---

### PP4 - Phenotype Specificity

**Original ACMG Summary:** Patient's phenotype or family history is highly specific for a disease with a single genetic etiology.

**VCEP Specifications:** Phenotype of affected individuals must include diabetes, without clear evidence of an autoimmune etiology (see Important Phenotype Requirements above).

#### PP4 Strength Levels

| Strength | Criteria |
|----------|----------|
| **Moderate** | MODY Probability Calculator (MPC) result ≥50% chance of testing positive ([https://www.diabetesgenes.org/mody-probability-calculator/](https://www.diabetesgenes.org/mody-probability-calculator/)) **AND** negative HNF4A testing **AND** presence of at least one additional feature characteristic of HNF1A-MODY |
| **Supporting** | MODY Probability Calculator (MPC) result ≥50% chance of testing positive **AND** negative HNF4A testing |

#### Additional Features Characteristic of HNF1A-MODY (for PP4_Moderate)

- Antibody negative and/or persistent C-peptide after five years post-T1DM diagnosis
- Response to low-dose sulfonylurea (SU) (extreme response - hypoglycemia)
- Low hsCRP in patient with clinical diagnosis of T2DM
- Biochemical/Molecular phenotypic evidence from patient cell lines
- Hepatocellular adenomas

---

### PP5 - Reputable Source

**Original ACMG Summary:** Reputable source recently reports variant as pathogenic, but the evidence is not available to the laboratory to perform an independent evaluation.

**VCEP Specifications:** *Not Applicable*

This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PMID: 29543229).

---

## Benign Criteria

### BA1 - Allele Frequency >5%

**Original ACMG Summary:** Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

#### BA1 Threshold (Stand Alone)

| Criterion | Threshold |
|-----------|-----------|
| **BA1** | gnomAD Grpmax FAF ≥ 1:10,000 (≥ 0.01% or 0.0001) |

---

### BS1 - Frequency Greater Than Expected

**Original ACMG Summary:** Allele frequency is greater than expected for disorder.

#### BS1 Threshold (Strong)

| Criterion | Threshold |
|-----------|-----------|
| **BS1** | gnomAD Grpmax FAF ≥ 1:30,000 (≥ 0.0033% or 0.000033) |

---

### BS2 - Observed in Healthy Adult

**Original ACMG Summary:** Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

#### BS2 Specification (Strong)

Apply to **normoglycemic individuals age 70 or older** (i.e., genotype positive, phenotype negative).

---

### BS3 - Functional Studies (No Effect)

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

#### Strength Levels

| Strength | Criteria |
|----------|----------|
| **Strong** | Applicable to non-canonical splice site variants that have RNA and in silico evidence of **normal splicing** |
| **Supporting** | See approved functional studies below |

#### Approved Functional Assays (BS3_Supporting)

1. **Luciferase assays for transactivation:** ≥ 75% activity of wildtype
2. **EMSA for DNA binding:** ≥ 75% activity of wildtype
3. **Western blotting and indirect immunofluorescence for protein expression and localization:**
   - Determining appropriate thresholds for protein expression is more difficult due to variability in results between different experimental protocols
   - Altered protein expression can be indirectly captured through the read-out from a transactivation assay
   - Reduced protein expression can provide an explanation for reduced transactivation

---

### BS4 - Lack of Segregation

**Original ACMG Summary:** Lack of segregation in affected members of a family.

**Caveat:** The presence of phenocopies for common phenotypes (i.e., cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.

#### BS4 Specification (Strong)

Applicable to family members without variant who have **MPC score >50%** (i.e., genotype negative, phenotype positive).

---

### BP1-BP7 - Benign Supporting

| Criterion | Status | Specification |
|-----------|--------|---------------|
| **BP1** | *Not Applicable* | Missense variant in a gene for which primarily truncating variants are known to cause disease |
| **BP2** | Supporting | Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder or observed in cis with a pathogenic variant in any inheritance pattern. **Also applicable when in cis or trans with a likely pathogenic variant.** |
| **BP3** | *Not Applicable* | In-frame deletions/insertions in a repetitive region without a known function |
| **BP4** | Supporting | Use REVEL score of **≤0.15** as supportive evidence of no predicted impact. For non-canonical splicing variants and synonymous variants: apply BP4 when SpliceAI predicted change is **below 0.2** |
| **BP5** | Supporting | A variant in other monogenic diabetes gene is P/LP |
| **BP6** | *Not Applicable* | Not for use as recommended by ClinGen SVI VCEP Review Committee (PMID: 29543229) |
| **BP7** | Supporting | Apply BP7 when SpliceAI predicted change is **below 0.2 AND phyloP100 way < 2.0** |

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
| 1 Very Strong (PVS1, PS2_VeryStrong) **AND** 1 Supporting (PS1_Supporting, PS2_Supporting, PS3_Supporting, PM1_Supporting, PM2_Supporting, PM4_Supporting, PM5_Supporting) |

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

### Appendix A: PVS1 Decision Tree Summary

**For Nonsense and Frameshift Variants:**

| Variant Position | Strength |
|------------------|----------|
| Nonsense or frameshift 5' of c.1768 | PVS1 (Very Strong) |
| Nonsense at c.1803 (p.601) and 5' | PVS1_Strong |
| Frameshift at c.1854 (p.618) and 5' | PVS1_Strong |
| Nonsense 3' of c.1803 (p.601) | PVS1_Supporting |
| Frameshift 3' of c.1854 (p.618) | PVS1_Supporting |

**For Exon Skipping/Deletions:**

| Exon(s) Affected | Strength |
|------------------|----------|
| Exons 1-9 (skipping or deletion) | PVS1 (Very Strong) |
| Exon 10 (skipping or deletion) | PVS1_Strong |

**For Initiation Codon Variants:**

| Variant Type | Strength |
|--------------|----------|
| Initiation codon variants | PVS1 (Very Strong) |

### Appendix B: Population Frequency Thresholds Summary

| Criterion | Threshold | Strength |
|-----------|-----------|----------|
| BA1 | gnomAD Grpmax FAF ≥ 0.0001 (≥ 0.01% or 1:10,000) | Stand Alone |
| BS1 | gnomAD Grpmax FAF ≥ 0.000033 (≥ 0.0033% or 1:30,000) | Strong |
| PM2 | gnomAD Grpmax FAF ≤ 0.000003 (≤ 0.0003% or 1:333,000) | Supporting |

### Appendix C: Computational Tool Thresholds

| Tool | Pathogenic Threshold | Benign Threshold | Application |
|------|---------------------|------------------|-------------|
| REVEL | ≥ 0.70 (PP3) | ≤ 0.15 (BP4) | Missense variants |
| SpliceAI | > 0.2 (PP3) | < 0.2 (BP4, BP7) | Splicing variants |
| phyloP100 | N/A | < 2.0 (BP7) | Conservation (with SpliceAI for BP7) |

### Appendix D: Functional Assay Thresholds

| Assay | PS3 Threshold (Damaging) | BS3 Threshold (Normal) |
|-------|--------------------------|------------------------|
| Luciferase transactivation | < 40% of WT | ≥ 75% of WT |
| EMSA DNA binding | < 40% of WT | ≥ 75% of WT |

### Appendix E: Criteria Not Applicable for HNF1A

| Criterion | Reason |
|-----------|--------|
| PM3 | Autosomal dominant inheritance - not applicable for recessive criteria |
| PM6 | Subsumed by PS2 point-based system |
| PP2 | Gene constraint score (1.07) is not significant |
| PP5 | Not for use per ClinGen SVI recommendation |
| BP1 | Not applicable |
| BP3 | Not applicable |
| BP6 | Not for use per ClinGen SVI recommendation |

---

## References

1. Brnich SE, Abou Tayoun AN, et al. Recommendations for application of the functional evidence PS3/BS3 criterion using the ACMG/AMP sequence variant interpretation framework. **Genome Med** (2019) 12(1):3. PMID: 31892348

2. Popp MW, Maquat LE. Organizing principles of mammalian nonsense-mediated mRNA decay. **Annu Rev Genet** (2013) 47:139-65. PMID: 24274751

3. Walker LC, Hoya M, et al. Using the ACMG/AMP framework to capture evidence related to predicted and observed impact on splicing: Recommendations from the ClinGen SVI Splicing Subgroup. **Am J Hum Genet** (2023) 110(7):1046-1067. PMID: 37352859

4. Bjørkhaug L, Ye H, et al. MODY associated with two novel hepatocyte nuclear factor-1alpha loss-of-function mutations (P112L and Q466X). **Biochem Biophys Res Commun** (2000) 279(3):792-8. PMID: 11162430

5. Bjørkhaug L, Sagen JV, et al. Hepatocyte nuclear factor-1 alpha gene mutations and diabetes in Norway. **J Clin Endocrinol Metab** (2003) 88(2):920-31. PMID: 12574234

6. SIGMA Type 2 Diabetes Consortium, Estrada K, et al. Association of a low-frequency variant in HNF1A with type 2 diabetes in a Latino population. **JAMA** (2014) 311(22):2305-14. PMID: 24915262

7. Jarvik GP, Browning BL. Consideration of Cosegregation in the Pathogenicity Classification of Genomic Variants. **Am J Hum Genet** (2016) 98(6):1077-1081. PMID: 27236918

8. Wai HA, Lord J, et al. Blood RNA analysis can increase clinical diagnostic rate and resolve variants of uncertain significance. **Genet Med** (2020) 22(6):1005-1014. PMID: 32123317

9. Jaganathan K, Kyriazopoulou Panagiotopoulou S, et al. Predicting Splicing from Primary Sequence with Deep Learning. **Cell** (2019) 176(3):535-548.e24. PMID: 30661751

10. Althari S, Najmi LA, et al. Unsupervised Clustering of Missense Variants in HNF1A Using Multidimensional Functional Data Aids Clinical Interpretation. **Am J Hum Genet** (2020) 107(4):670-682. PMID: 32910913

11. McDonald TJ, Colclough K, et al. Islet autoantibodies can discriminate maturity-onset diabetes of the young (MODY) from Type 1 diabetes. **Diabet Med** (2011) 28(9):1028-33. PMID: 21395678

12. Shields BM, Shepherd M, et al. Population-Based Assessment of a Biomarker-Based Screening Pathway to Aid Diagnosis of Monogenic Diabetes in Young-Onset Patients. **Diabetes Care** (2017) 40(8):1017-1025. PMID: 28701371

13. Patel KA, Weedon MN, et al. Zinc Transporter 8 Autoantibodies (ZnT8A) and a Type 1 Diabetes Genetic Risk Score Can Exclude Individuals With Type 1 Diabetes From Inappropriate Genetic Testing for Monogenic Diabetes. **Diabetes Care** (2019) 42(2):e16-e17. PMID: 30409810

14. Carlsson A, Shepherd M, et al. Absence of Islet Autoantibodies and Modestly Raised Glucose Values at Diabetes Diagnosis Should Lead to Testing for MODY: Lessons From a 5-Year Pediatric Swedish National Cohort Study. **Diabetes Care** (2020) 43(1):82-89. PMID: 31704690

15. Hattersley AT, Greeley SAW, et al. ISPAD Clinical Practice Consensus Guidelines 2018: The diagnosis and management of monogenic diabetes in children and adolescents. **Pediatr Diabetes** (2018) 19 Suppl 27:47-63. PMID: 30225972

16. Pihoker C, Gilliam LK, et al. Prevalence, characteristics and clinical diagnosis of maturity onset diabetes of the young due to mutations in HNF1A, HNF4A, and glucokinase: results from the SEARCH for Diabetes in Youth. **J Clin Endocrinol Metab** (2013) 98(10):4055-62. PMID: 23771925

17. Abou Tayoun AN, Pesaran T, et al. Recommendations for interpreting the loss of function PVS1 ACMG/AMP variant criterion. **Hum Mutat** (2018) 39(11):1517-1524. PMID: 30192042

---

## Version History

| Version | Date | Notes |
|---------|------|-------|
| 3.1.0 | 10/10/2025 | Updating PS2 to clarify when a family history of diabetes prevents the application of this criterion. Minor edits for clarity and avoiding redundancy in the specifications. Updating citations so reference list populates. |

---

*This document was compiled from ClinGen VCEP specifications. For the most current version, please refer to the [ClinGen website](https://clinicalgenome.org/).*
