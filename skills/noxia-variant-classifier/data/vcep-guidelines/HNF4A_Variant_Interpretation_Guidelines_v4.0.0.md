# ClinGen Monogenic Diabetes Expert Panel Variant Interpretation Guidelines for HNF4A

**Version:** 4.0.0
**Released:** 10/10/2025
**Affiliation:** Monogenic Diabetes VCEP
**Based on:** Richards et al., 2015 ACMG/AMP Guidelines

---

## Gene Information

| Attribute | Value |
|-----------|-------|
| **Gene** | HNF4A (HGNC:5024) |
| **HGNC Name** | hepatocyte nuclear factor 4 alpha |
| **Transcript** | NM_175914.5 |
| **Disease** | monogenic diabetes (MONDO:0015967) |
| **Inheritance** | Autosomal dominant inheritance |

---

## Release Notes (v4.0.0)

- Updating PS2 to clarify when a family history of diabetes prevents this criterion from being applied
- Changing PM1 application for variants occurring within the HNF1A/HNF1B and PDX1 (formerly IPF1) binding sites of the promoter

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
   - [BA1 - Allele Frequency](#ba1---allele-frequency)
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

**Caveats:**
- Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7)
- Use caution interpreting LOF variants at the extreme 3' end of a gene
- Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact
- Use caution in the presence of multiple transcripts

**VCEP Specifications:**

Per recommendations from the SVI, when RNA analysis demonstrates abnormal splicing from non-canonical splice site variants, apply PS3 instead of PVS1.

**General Comments:** Upgrade initiation codon variants from PVS1_Moderate to PVS1_Strong on the basis that next methionine is Met71 and multiple variants not found in gnomAD have been reported in patients meeting diagnostic criteria for MODY (PMID: 23348805)

#### PVS1 Strength Levels

| Strength | Criteria |
|----------|----------|
| **Very Strong (PVS1)** | Use HNF4A PVS1 decision tree. See detailed specifications below. |
| **Strong** | Use HNF4A PVS1 decision tree. See detailed specifications below. |
| **Supporting** | Apply PVS1_Supporting to nonsense or frameshift variants at c.1258 (G)/p.Gly420 and 3'. |

#### PVS1 Decision Tree Details

##### Nonsense or Frameshift Variants

| Location | Strength |
|----------|----------|
| Exons 1-9 (5' of c.1162) because NMD is expected | **PVS1** |
| Last 55 base pairs of exon 9 (c.1162–c.1216) and first 41 base pairs of exon 10 (c.1217–c.1257) because known MODY nonsense/frameshift variants occur at and 5' of corresponding aa Ser419 | **PVS1** |
| Exon 10 3' of c.1257 (Gly420) | **PVS1_Supporting** |

**Note:** Variants generating PTCs in exon 10 and last 55 nucleotides of exon 9 (c.1162-1216) are not expected to cause NMD. The most 3' nonsense or frameshift variant is c.1256C>G, p.S419X in the last exon, classified as Pathogenic by the MDEP. The collective evidence supports applying PVS1 for variants at codon 419 (c.1257) and 5' and PVS1_Supporting for variants at c.1258 (G)/p.Gly420 and 3'.

##### GT-AG 1,2 Splice Sites

| Predicted Outcome | Strength |
|-------------------|----------|
| Skipping of exon 1, 2, 3, 4, or 6 or use of a cryptic splice site results in frameshift that causes PTC 5' of c.1257/Ser419 | **PVS1** |
| Skipping of exon 5, 7, 8, or 9 (preserves reading frame but removes >10% of protein) | **PVS1_Strong** |
| Skipping of or stop loss in exon 10 (removes transactivation domain) | **PVS1_Strong** |

##### Deletions (Single Exon to Full Gene)

| Type | Strength |
|------|----------|
| Full gene deletion | **PVS1** |
| Single to multi-exon deletion – exons 1, 2, 3, 4, or 6 | **PVS1** |
| Single exon deletion: exon 5, 7, 8, 9, or 10 | **PVS1_Strong** |

**Exon Deletion/Skipping Details:**
- Exons 1, 2 (LRG 4), 3 (LRG 5), 4 (LRG 6), 6 (LRG 8): deletion or skipping causes frameshift → **PVS1**
- Exons 5 (LRG 7), 7 (LRG 9), 8 (LRG 10), 9 (LRG 11): deletion or skipping causes in-frame deletion, 52/52/79/51-79 AA deleted (>10% of protein) → **PVS1_Strong**
- Exon 10 (LRG 12): 46 AA, contains the transactivation domain, includes stop loss → **PVS1_Strong**

##### Duplications (≥1 Exon, Completely Contained Within Gene)

| Tandem Status | Reading Frame Impact | Strength |
|---------------|----------------------|----------|
| Proven in tandem | Reading frame disrupted and NMD predicted to occur | **PVS1** |
| Proven in tandem | No or unknown impact on reading frame and NMD | **N/A** |
| Presumed in tandem | Reading frame presumed disrupted and NMD predicted to occur | **PVS1_Strong** |
| Proven not in tandem | — | **N/A** |

##### Initiation Codon Variants

| Variant Type | Strength |
|--------------|----------|
| Initiation codon variants | **PVS1_Strong** |

**Note:** Apply PVS1_Strong to initiation codon variants. MDEP has classified two start codon variants as likely pathogenic (c.3G>A and c.1delA) and there are multiple P/LP variants before the next methionine, p.Met71.

---

### PS1 - Same Amino Acid Change

**Original ACMG Summary:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.

**Example:** Val->Leu caused by either G>C or G>T in the same codon.

**Caveat:** Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | Applicable for a same amino acid change if the previously established variant is classified as **pathogenic** by ClinGen MDEP specifications. PS1 can also be applied for canonical and non-canonical splicing variants that have a SpliceAI score within 10% of the original variant, or a greater predicted deleterious impact than the comparison (likely) pathogenic variant. See Table 2 from PMID: 37352859 for determining strength. |
| **Moderate** | Applicable for a same amino acid change if the previously established variant is classified as **likely pathogenic** by ClinGen MDEP specifications. PS1 can also be applied for canonical and non-canonical splicing variants per PMID: 37352859. |
| **Supporting** | PS1 can be applied for canonical and non-canonical splicing variants per PMID: 37352859 guidelines. |

---

### PS2 - De Novo (Confirmed)

**Original ACMG Summary:** De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.

**Note:** Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.

**VCEP Specifications:**

Use SVI recommended point-based system with specifications for "Phenotype Consistency" per instructions.

**Phenotype Specifications:**
- **"Phenotype highly specific for gene"**: Patient must meet criteria for PP4 (result of ≥50% chance or higher of testing positive for MODY on the MODY Probability Calculator AND negative HNF1A testing)
- **"Phenotype consistent with gene but not highly specific"**: The phenotype of the patient must include diabetes

**Exclusion Criteria for Probands/Family Members:**
Probands (and/or family members when assessing segregation for PP1) with evidence of an autoimmune etiology of diabetes and/or absolute or near-absolute insulin deficiency will be excluded when assessing criteria that includes phenotype information. Such evidence includes:
- One or more positive diabetes autoantibodies (IA-2A, ZnT8A+, GAD)
- Very low or negative C-peptide, defined as either fasting or non-fasting random C-peptide (<200pmol/L or 0.6ng/mL) or urinary C-peptide/creatinine ratio <0.2 nmol/mmol

**Important:** Do not apply PS2 if the proband has an affected parent with any of the following:
- Affected parent meets PP4 specifications
- Parent is described as having similarly atypical diabetes to the proband
- Parent was diagnosed with non-autoimmune diabetes before age 30

#### PS2 Point System

**Table 1: Points Awarded Per De Novo Occurrence**

| Phenotypic Consistency | De Novo with Confirmed Parental Relationships | De Novo with Unconfirmed Parental Relationships |
|------------------------|-----------------------------------------------|------------------------------------------------|
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

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | Applicable to non-canonical splice site variants that have RNA and in silico evidence of aberrant splicing. |
| **Supporting** | See list of approved functional studies below. |

#### Approved Functional Studies and Guidelines for Interpretation

**1. EMSA for DNA Binding**
- "Decreased function" is defined as activity less than 60% of wildtype
- **Note:** The effect of the variant on DNA binding will be highly dependent on whether the variant is located within the DNA binding domain

**2. Luciferase Assays for Transactivation**
- "Decreased function" is defined as activity less than 60% of wildtype
- **Note:** This threshold is not 100% specific for transactivation (TA) activity and is complicated by the fact that TA activity will vary depending on many factors, for instance cell line that is used (HeLa, INS, MIN6 etc.)

**3. Western Blotting and Indirect Immunofluorescence for Protein Expression**
- Specifically for levels and nuclear/cytoplasmic localization
- Determining appropriate thresholds for protein expression is more difficult due to variability in results due to the complexity of the technique
- Sample preparations, gel loading, transfer efficiency, specificity of the antibody, choice of internal control and inaccurate detection and quantification can contribute to varying and inconsistent results
- If a reduction in protein expression is seen by immunoblotting, then further testing by quantitative PCR (qPCR) is recommended to measure the mRNA level and assess whether a reduction in amount of protein is due to a reduced mRNA level

**Important:** To use PS3_Supporting, functional study must have been performed on a transfected variant. If a study was performed on a cell line generated from a patient sample (and therefore contains the variant plus wild-type allele) it does not count as PS3_Supporting.

---

### PS4 - Prevalence in Affected

**Original ACMG Summary:** The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.

**Notes:**
- Relative risk (RR) or odds ratio (OR), as obtained from case-control studies, is >5.0 and the confidence interval around the estimate of RR or OR does not include 1.0
- In instances of very rare variants where case-control studies may not reach statistical significance, the prior observation of the variant in multiple unrelated patients with the same phenotype, and its absence in controls, may be used as moderate level of evidence

**VCEP Specifications:**

The phenotype of the patient must include diabetes, with evidence of an autoimmune etiology and/or absolute or near-absolute insulin deficiency (see PS2 exclusions) considered as exclusionary. Variant should meet PM2_Supporting in order to use PS4 at any level (careful review of gnomAD QC data may be necessary to assess whether variant is real or an artifact, especially if variant is in a polyC region).

| Strength | Criteria |
|----------|----------|
| **Strong** | 7 (seven) or more unrelated occurrences. Variant should meet PM2_Supporting. Phenotype of affected individuals must include diabetes, without clear evidence of an autoimmune etiology. |
| **Moderate** | 4-6 unrelated occurrences. Variant should meet PM2_Supporting. Phenotype of affected individuals must include diabetes, without clear evidence of an autoimmune etiology. |

**Exclusion Criteria:**
- One or more positive diabetes autoantibodies (IA-2A, ZnT8A+, GAD)
- Very low or negative C-peptide (<200pmol/L or 0.6ng/mL fasting/non-fasting, or urinary C-peptide/creatinine ratio <0.2 nmol/mmol)

---

### PM1 - Mutational Hot Spot

**Original ACMG Summary:** Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Moderate** | Applicable to amino acids that directly bind DNA and are necessary for Zinc-finger or homodimer formation. Also applicable to variants within the promoter region that are direct HNF1A/HNF1B binding sites. |
| **Supporting** | Applicable to missense variants in well-conserved regions within the DNA and ligand-binding domains. Also applicable to variants within certain conserved transcription factor binding sites in the promoter. |

#### PM1_Moderate - Critical Residues

**Directly Bind DNA:**
Asp43, His49, Tyr50, Gly51, Asp56, Gly57, Lys59, Arg63, Arg64, Arg67, His70, Tyr72, Arg87, Asn88, Arg91, Arg94, Gln109, Arg112

**Homodimer Formation:**
Arg75, Gln89, Glu111, Asp113

**Zinc Finger:**
Cys38, Cys41, Cys55, Cys58, Cys74, Cys80, Cys90, Cys93

**Promoter Region - HNF1A/HNF1B Binding Sites (NM_175914.4):**
- c.-170 to c.-173
- c.-178 to c.-181

#### PM1_Supporting - Conserved Regions

**Promoter Region:**
- c.-132 to c.-141 (HNF6/OC2 binding site)
- c.-143 to c.-149, c.-151 (PDX1 (formerly IPF1) binding site)
- c.-169, c.-174, c.-176, and c.-177 (HNF1A/HNF1B binding site)

**DNA Binding Domain:**
- Codons 37-113 (NM_175914.4:c.175C-339C p.Leu37-Asp113)
- Note: While the paper describing the crystal structure of HNF4A shows the sequence as amino acids 33-113, amino acids 33-36 do not bind DNA and the conserved sequence starts at Leu37

**Ligand Binding Domain:**
- Codons 180-220 (NM_175914.4:c.538G-658G p.Ala180-Val220)
- Codons 300-350 (NM_175914.4:c.898T-1048G p.Tyr300-Glu350)

---

### PM2 - Absent from Controls

**Original ACMG Summary:** Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

**Caveat:** Population data for indels may be poorly called by next generation sequencing.

**VCEP Specifications:**

Recommend using as supporting level of evidence (PM2_Supporting) per ClinGen guidance. Per guidance from ClinGen/SVI, PM2_Supporting + PVS1 is sufficient evidence of a variant being likely pathogenic.

| Strength | Threshold |
|----------|-----------|
| **Supporting** | gnomAD Grpmax FAF ≤ 1:333,000 (≤ 0.000003 or 0.0003%) |

**Notes:**
- Investigate the genotype metrics in gnomAD for variants that have been flagged for having failed one or more quality parameters, as it is possible that some of these filtered variants are actually real
- The number of filtered alleles can be counted to determine whether PM2_Supporting would be met even if they were genuine calls
- If the filtered calls are sufficient in number to not meet PM2_Supporting, then do not use it
- Because it is also possible that these calls are false positives, do not use filtered variants to support BA1 or BS1

---

### PM3 - In Trans with Pathogenic

**Original ACMG Summary:** For recessive disorders, detected in trans with a pathogenic variant.

**Note:** This requires testing of parents (or offspring) to determine phase.

**VCEP Specifications:** ***Not Applicable*** - HNF4A-related monogenic diabetes is autosomal dominant.

---

### PM4 - Protein Length Changes

**Original ACMG Summary:** Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Moderate** | For deletions/insertions of more than one amino acid in a non-repeat region |
| **Supporting** | For single amino acid deletions/insertions |

---

### PM5 - Novel Missense at Same Residue

**Original ACMG Summary:** Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.

**Example:** Arg156His is pathogenic; now you observe Arg156Cys.

**Caveat:** Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | Applicable once two amino acid changes have been classified as pathogenic at the same amino acid residue |
| **Moderate** | The novel amino acid change must have a Grantham distance greater than or equal to the previously classified pathogenic variant |
| **Supporting** | Apply if the previously classified amino acid change is likely pathogenic (rather than pathogenic) OR if the previously classified variant is pathogenic but has a greater Grantham distance than the novel variant |

---

### PM6 - De Novo (Assumed)

**Original ACMG Summary:** Assumed de novo, but without confirmation of paternity and maternity.

**VCEP Specifications:** ***Not Applicable*** - Subsumed by PS2. Use PS2 point-based system (see PS2 section above).

---

### PP1 - Co-segregation

**Original ACMG Summary:** Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.

**Note:** May be used as stronger evidence with increasing segregation data.

**VCEP Specifications:**

Variable penetrance and phenocopies complicate co-segregation studies. The presence of type 1 and type 2 diabetes phenocopies and significance of variants in unaffected individuals will need to be considered.

**Exclusion Criteria:**
If a family member(s) shows evidence of an autoimmune etiology for their diabetes and/or absolute or near-absolute insulin deficiency, do not include them in PP1 calculation:
- One or more positive diabetes autoantibodies (IA-2A, ZnT8A+, GAD)
- Very low or negative C-peptide (<200pmol/L or 0.6ng/mL) or urinary C-peptide/creatinine ratio <0.2 nmol/mmol

**Unaffected Family Members:**
Unaffected family members without the variant under assessment can also be used in segregation analysis. An individual is considered "unaffected" if over age 70 and non-diabetic (based on Exeter work showing penetrance of HNF4A-MODY at 98% by age 70).

#### PP1 Thresholds (Jarvik and Browning)

| Strength | Single Family | >1 Family |
|----------|---------------|-----------|
| **Strong** | ≤ 1/32 (5 meioses) | ≤ 1/16 (4 meioses) |
| **Moderate** | ≤ 1/16 (4 meioses) | ≤ 1/8 (3 meioses) |
| **Supporting** | ≤ 1/8 (3 meioses) | ≤ 1/4 (2 meioses) |

---

### PP2 - Missense in Constrained Gene

**Original ACMG Summary:** Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.

**VCEP Specifications:** ***Not Applicable***

**Comments:** While missense variants in HNF4A are a common mechanism of monogenic diabetes, and the constraint score for HNF4A (gene) is 1.81, the MDEP does not support using this criterion at this time.

---

### PP3 - Computational Evidence

**Original ACMG Summary:** Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).

**Caveat:** As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Supporting** | Use REVEL score of ≥0.70 as supportive evidence of pathogenicity. Also support using SpliceAI to assess the predicted impact of non-canonical splicing variants and synonymous variants: apply PP3 when the predicted change is at least 0.2. |

---

### PP4 - Phenotype Specificity

**Original ACMG Summary:** Patient's phenotype or family history is highly specific for a disease with a single genetic etiology.

**VCEP Specifications:**

MODY probability calculator result of ≥50% chance of testing positive (https://www.diabetesgenes.org/mody-probability-calculator/) AND negative HNF1A genetic analysis, given the similarities in phenotypes between HNF1A-MODY and HNF4A-MODY.

**Clinical Judgment Notes:**
- The MODY Probability Calculator is not as reliable for non-European ancestry individuals or people diagnosed >35
- Use of PP4 is acceptable in the absence of HNF1A analysis when the MPC is >50% and the phenotype is specific to HNF4A (e.g., someone in the family with neonatal hypoglycemia responsive to diazoxide or hyperinsulinemic hypoglycemia)
- If individual was tested due to neonatal hypoglycemia, PP4 can be used if ABCC8 and KCNJ11 testing are negative (no MODY Probability Calculator result required)

**MODY Probability Calculator Assumptions:**
- If no specific clinical info about parents is given but lab/literature states "Family history of diabetes", click "Parent with diabetes" in calculator
- If no information about family history of diabetes is provided, run the calculator in both conditions (yes/no) and document whether this makes a difference in overall probability score
- If Weight/Height/BMI not given but lab/literature states patient is "lean", enter BMI of 30
- If HbA1c is not provided, enter 6% and 10% and document whether this makes a difference in overall probability score
- If treatment information is not provided, cannot use calculator

| Strength | Criteria |
|----------|----------|
| **Moderate** | MODY Probability Calculator result ≥50% chance of testing positive AND negative HNF1A testing AND presence of at least one additional feature characteristic of HNF4A-MODY (see list below) |
| **Supporting** | MODY Probability Calculator (MPC) result ≥50% chance of testing positive AND negative HNF1A testing |

#### Features Characteristic of HNF4A-MODY (for PP4_Moderate)

- Antibody negative and/or persistent C-peptide after five years following T1DM diagnosis
- Personal or family history of persistent neonatal hypoglycemia
- Personal or family history of large for gestational age (LGA) infants or macrosomia in the absence of sufficient maternal hyperglycemia
- Response to low-dose SU (extreme response - hypoglycemia)
- Biochemical/Molecular phenotypic evidence from patient cell lines
- Fanconi phenotype in conjunction with c.187C>T p.R63W

---

### PP5 - Reputable Source

**Original ACMG Summary:** Reputable source recently reports variant as pathogenic, but the evidence is not available to the laboratory to perform an independent evaluation.

**VCEP Specifications:** ***Not Applicable***

This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PMID: 29543229).

---

## Benign Criteria

### BA1 - Allele Frequency

**Original ACMG Summary:** Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

**VCEP Specification (Stand Alone):**

| Threshold |
|-----------|
| gnomAD Grpmax FAF ≥ 1:10,000 (≥ 0.01% or 0.0001) |

---

### BS1 - Frequency Greater Than Expected

**Original ACMG Summary:** Allele frequency is greater than expected for disorder.

**VCEP Specifications:**

If there is a Grpmax Filtering AF for both exomes and genomes, use the one with the larger denominator.

| Strength | Threshold |
|----------|-----------|
| **Strong** | gnomAD Grpmax FAF ≥ 1:30,000 (≥0.0033% or 0.000033) |

---

### BS2 - Observed in Healthy Adult

**Original ACMG Summary:** Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | Apply to normoglycemic individuals age 70 or older (i.e., genotype positive, phenotype negative) |

---

### BS3 - Functional Studies (No Effect)

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

**VCEP Specifications:**

To use BS3, functional study must have been performed on a transfected variant. If a study was performed on a cell line generated from a patient sample (and therefore contains the variant plus wild-type allele) it cannot count as BS3.

| Strength | Criteria |
|----------|----------|
| **Strong** | Applicable to non-canonical splice site variants that have RNA and in silico evidence of normal splicing |
| **Supporting** | See approved functional studies below |

#### Approved Functional Studies for BS3_Supporting

**1. EMSA for DNA Binding**
- "No functional impact" is defined as ≥75% activity of wildtype
- **Note:** The effect of the variant on DNA binding will be highly dependent on whether the variant is located within the DNA binding domain

**2. Luciferase Assays for Transactivation**
- "No functional impact" is defined as ≥75% activity of wildtype
- **Note:** This threshold is not 100% specific for transactivation (TA) activity and is complicated by the fact that TA activity will vary depending on many factors, for instance cell line that is used (HeLa, INS, MIN6 etc.)
- Assays should include controls for WT, T2DM and known MODY variants

**3. Western Blotting and Indirect Immunofluorescence for Protein Expression**
- Specifically for levels and nuclear/cytoplasmic localization
- Determining appropriate thresholds for protein expression is more difficult due to variability in results
- If a difference in protein expression compared to WT is seen by immunoblotting, then further testing by qPCR is recommended to measure the mRNA level and assess whether the difference in amount of protein is due to a reduced mRNA level

---

### BS4 - Lack of Segregation

**Original ACMG Summary:** Lack of segregation in affected members of a family.

**Caveat:** The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | Applicable to family members without variant who have MPC score ≥50% (i.e., genotype negative, phenotype positive) |

---

### BP1-BP7 - Benign Supporting

| Criterion | Status | Specification |
|-----------|--------|---------------|
| **BP1** | Not Applicable | — |
| **BP2** | Supporting | Also applicable when in cis or trans with a likely pathogenic variant |
| **BP3** | Not Applicable | — |
| **BP4** | Supporting | Use a REVEL score of ≤0.15 as supportive evidence of no predicted impact on the gene or gene product. Also support using SpliceAI to assess the predicted impact of non-canonical splicing variants and synonymous variants: apply BP4 when the predicted change is below 0.2 |
| **BP5** | Supporting | A variant in another monogenic diabetes gene is Pathogenic/Likely Pathogenic |
| **BP6** | Not Applicable | This criterion is not for use as recommended by the ClinGen SVI (PMID: 29543229) |
| **BP7** | Supporting | Apply BP7 when the predicted change from SpliceAI is below 0.2 AND phyloP100 way < 2.0 |

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
| 1 Strong **AND** 1 Supporting |
| ≥2 Supporting |

---

## Appendices

### Appendix A: PVS1 Decision Tree Flowchart

```
VARIANT TYPE                    OUTCOME                                          STRENGTH
─────────────────────────────────────────────────────────────────────────────────────────

Nonsense or        ──▶ Exons 1-9 (5' of c.1162) - NMD expected         ──▶ PVS1
Frameshift         ──▶ Last 55 bp exon 9 + first 41 bp exon 10         ──▶ PVS1
                   ──▶ Exon 10 3' of c.1257 (Gly420)                   ──▶ PVS1_Supporting

GT-AG 1,2          ──▶ Skip exon 1,2,3,4,6 → frameshift → PTC          ──▶ PVS1
Splice Sites       ──▶ Skip exon 5,7,8,9 → in-frame, >10% removed      ──▶ PVS1_Strong
                   ──▶ Skip/stop loss exon 10                          ──▶ PVS1_Strong

Deletion           ──▶ Full gene deletion                              ──▶ PVS1
(single to full    ──▶ Exons 1,2,3,4,6 deletion                        ──▶ PVS1
gene)              ──▶ Single exon: 5,7,8,9,10 deletion                ──▶ PVS1_Strong

Duplication        ──▶ Proven in tandem + frameshift + NMD             ──▶ PVS1
(≥1 exon,          ──▶ Proven in tandem + no/unknown impact            ──▶ N/A
within gene)       ──▶ Presumed in tandem + frameshift + NMD           ──▶ PVS1_Strong
                   ──▶ Proven not in tandem                            ──▶ N/A

Initiation         ──▶ Any initiation codon variant                    ──▶ PVS1_Strong
Codon
```

### Appendix B: Population Frequency Thresholds Summary

| Criterion | Threshold | Strength |
|-----------|-----------|----------|
| BA1 | gnomAD Grpmax FAF ≥ 1:10,000 (≥0.01%) | Stand Alone |
| BS1 | gnomAD Grpmax FAF ≥ 1:30,000 (≥0.0033%) | Strong |
| PM2 | gnomAD Grpmax FAF ≤ 1:333,000 (≤0.0003%) | Supporting |

### Appendix C: Functional Assay Thresholds Summary

| Assay Type | PS3_Supporting (Damaging) | BS3_Supporting (No Effect) |
|------------|---------------------------|----------------------------|
| EMSA (DNA binding) | <60% of wildtype | ≥75% of wildtype |
| Luciferase (Transactivation) | <60% of wildtype | ≥75% of wildtype |
| Western blot/Immunofluorescence | Variable - requires qPCR confirmation | Variable - requires qPCR confirmation |

### Appendix D: References

1. Popp MW, Maquat LE. *Organizing principles of mammalian nonsense-mediated mRNA decay.* Annu Rev Genet (2013) 47:139-65. PMID: 24274751
2. Lu P, Rha GB, et al. *Structural basis of natural promoter recognition by a unique nuclear receptor, HNF4alpha.* J Biol Chem (2008) 283(48):33685-97. PMID: 18829458
3. Jaganathan K, Kyriazopoulou Panagiotopoulou S, et al. *Predicting Splicing from Primary Sequence with Deep Learning.* Cell (2019) 176(3):535-548.e24. PMID: 30661751
4. Wai HA, Lord J, et al. *Blood RNA analysis can increase clinical diagnostic rate and resolve variants of uncertain significance.* Genet Med (2020) 22(6):1005-1014. PMID: 32123317
5. Jarvik GP, Browning BL. *Consideration of Cosegregation in the Pathogenicity Classification of Genomic Variants.* Am J Hum Genet (2016) 98(6):1077-1081. PMID: 27236918
6. MODY Probability Calculator: https://www.diabetesgenes.org/mody-probability-calculator/
7. McDonald TJ, Colclough K, et al. *Islet autoantibodies can discriminate maturity-onset diabetes of the young (MODY) from Type 1 diabetes.* Diabet Med (2011) 28(9):1028-33. PMID: 21395678
8. Shields BM, Shepherd M, et al. *Population-Based Assessment of a Biomarker-Based Screening Pathway to Aid Diagnosis of Monogenic Diabetes in Young-Onset Patients.* Diabetes Care (2017) 40(8):1017-1025. PMID: 28701371
9. Patel KA, Weedon MN, et al. *Zinc Transporter 8 Autoantibodies (ZnT8A) and a Type 1 Diabetes Genetic Risk Score Can Exclude Individuals With Type 1 Diabetes From Inappropriate Genetic Testing for Monogenic Diabetes.* Diabetes Care (2019) 42(2):e16-e17. PMID: 30409810
10. Carlsson A, Shepherd M, et al. *Absence of Islet Autoantibodies and Modestly Raised Glucose Values at Diabetes Diagnosis Should Lead to Testing for MODY: Lessons From a 5-Year Pediatric Swedish National Cohort Study.* Diabetes Care (2020) 43(1):82-89. PMID: 31704690
11. Hattersley AT, Greeley SAW, et al. *ISPAD Clinical Practice Consensus Guidelines 2018: The diagnosis and management of monogenic diabetes in children and adolescents.* Pediatr Diabetes (2018) 19 Suppl 27:47-63. PMID: 30225972
12. Pihoker C, Gilliam LK, et al. *Prevalence, characteristics and clinical diagnosis of maturity onset diabetes of the young due to mutations in HNF1A, HNF4A, and glucokinase: results from the SEARCH for Diabetes in Youth.* J Clin Endocrinol Metab (2013) 98(10):4055-62. PMID: 23771925
13. Patel KA, Kettunen J, et al. *Heterozygous RFX6 protein truncating variants are associated with MODY with reduced penetrance.* Nat Commun (2017) 8(1):888. PMID: 29026101
14. Hamilton AJ, Bingham C, et al. *The HNF4A R76W mutation causes atypical dominant Fanconi syndrome in addition to a β cell phenotype.* J Med Genet (2014) 51(3):165-9. PMID: 24285859
15. Jolma A, Yan J, et al. *DNA-binding specificities of human transcription factors.* Cell (2013) 152(1-2):327-39. PMID: 23332764
16. Ng NHJ, Ghosh S, et al. *HNF4A and HNF1A exhibit tissue specific target gene regulation in pancreatic beta cells and hepatocytes.* Nat Commun (2024) 15(1):4288. PMID: 38909044

---

## Version History

| Version | Date | Notes |
|---------|------|-------|
| 4.0.0 | 10/10/2025 | Updated PS2 to clarify family history exclusions; Changed PM1 for HNF1A/HNF1B and PDX1 binding sites in promoter |
| 1.0.0 | — | Initial release |

---

*This document was compiled from ClinGen VCEP specifications. For the most current version, please refer to the ClinGen website at https://clinicalgenome.org/*
