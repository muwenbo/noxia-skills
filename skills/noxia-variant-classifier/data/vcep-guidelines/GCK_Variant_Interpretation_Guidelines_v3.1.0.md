# ClinGen Monogenic Diabetes Expert Panel Variant Interpretation Guidelines for GCK

**Version:** 3.1.0
**Released:** 10/10/2025
**Affiliation:** Monogenic Diabetes VCEP
**Based on:** Richards et al., 2015 ACMG/AMP Guidelines

---

## Gene Information

| Attribute | Value |
|-----------|-------|
| **Gene** | GCK (HGNC:4195) |
| **HGNC Name** | glucokinase |
| **Transcript** | NM_000162.5 |
| **Disease** | monogenic diabetes (MONDO:0015967) |
| **Inheritance** | Semidominant inheritance |

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
   - [Appendix A: PVS1 Decision Tree](#appendix-a-pvs1-decision-tree)
   - [Appendix B: PS2/PM6 De Novo Points Table](#appendix-b-ps2pm6-de-novo-points-table)
   - [Appendix C: PM3 Points Table](#appendix-c-pm3-points-table)
   - [Appendix D: PM1 Residues](#appendix-d-pm1-residues)
   - [Appendix E: PS3/BS3 Decision Tree](#appendix-e-ps3bs3-decision-tree)
   - [Appendix F: Population Frequency Thresholds Summary](#appendix-f-population-frequency-thresholds-summary)
   - [Appendix G: References](#appendix-g-references)

---

## Pathogenic Criteria

### PVS1 - Null Variant

**Original ACMG Summary:** Null variant (nonsense, frameshift, canonical +/-1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.

**Caveats:**
- Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7)
- Use caution interpreting LOF variants at the extreme 3' end of a gene
- Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact
- Use caution in the presence of multiple transcripts

**VCEP Specifications:** Use GCK PVS1 decision tree (see [Appendix A](#appendix-a-pvs1-decision-tree)).

#### Strength Levels

| Strength | Criteria |
|----------|----------|
| **Very Strong** | Use GCK PVS1 decision tree created based on PVS1 decision tree from ClinGen SVI group. See detailed specifications below. |
| **Strong** | Apply PVS1_Strong to duplications ≥1 exon in size, contained completely within gene, presumed in tandem, reading frame presumed disrupted, and NMD predicted to occur. |
| **Supporting** | Apply PVS1_Supporting to initiation codon variants. The next methionine is at codon 8 and there are no variants classified as pathogenic 5' of p.Met8. |

#### Gene-Specific PVS1 Notes

**NMD Escape Region:**
- Variants generating PTCs 3' of c.1198 (p.Asp400) of NM_000162.3, which includes the last 55 nucleotides of exon 9 and exon 10, are not expected to cause NMD
- The α13 helix (p.444-456), located at the C-end of the protein, has a critical role in GCK conformational change upon glucose binding
- Individuals with PTCs in exon 10 have a MODY phenotype; therefore, **PVS1 (Very Strong)** level of evidence will be applied for PTCs in exon 10

**Exon Skipping/Deletions:**
| Exon(s) | Effect | Strength |
|---------|--------|----------|
| Exon 1 | In-frame but >20 families with GCK-MODY phenotype and exon 1 deletion (some also have promoter deletions) | PVS1 |
| Exons 2, 3, 6, 7 | Cause frameshift | PVS1 |
| Exons 8, 9 | In-frame, proportion >10% (52 AA and 78 AA, respectively) | PVS1 |
| Exons 4, 5 | In-frame, proportion <10% (40 AA and 32 AA). Exon 4 (p.122-161) and exon 5 (p.162-193) contain each a part of the active site that binds glucose (p.151-180) | PVS1 |
| Exon 10 | 47 AA - Multiple patients with GCK-MODY phenotype reported with missense, frameshift, PTC, splice acceptor, and stop loss variants | PVS1 |

**Important Notes:**
- Per recommendations from the SVI, when RNA analysis demonstrates abnormal splicing from non-canonical splice site variants, apply **PS3** instead of PVS1
- Full gene deletion warrants pathogenic classification given GCK is a known haploinsufficient gene (in the absence of conflicting data)

---

### PS1 - Same Amino Acid Change

**Original ACMG Summary:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.

**Example:** Val->Leu caused by either G>C or G>T in the same codon.

**Caveat:** Beware of changes that impact splicing rather than at the amino acid/protein level.

#### Strength Levels

| Strength | Criteria |
|----------|----------|
| **Strong** | Applicable for a same amino acid change if the previously established variant is classified as **pathogenic** by ClinGen MDEP specifications. |
| **Moderate** | Applicable for a same amino acid change if the previously established variant is classified as **likely pathogenic** by ClinGen MDEP specifications. |
| **Supporting** | See splicing guidance below. |

**Splicing Variants:** PS1 can also be applied for canonical and non-canonical splicing variants that have a SpliceAI score within 10% of the original variant, or a greater predicted deleterious impact than the comparison (likely) pathogenic variant. See Table 2 from PMID: 37352859 for determining when PS1 should be applied at the Strong, Moderate, or Supporting level in these instances.

---

### PS2 - De Novo (Confirmed)

**Original ACMG Summary:** De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.

**Note:** Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.

**VCEP Specifications:**

**Phenotype Requirements:**
- To obtain **maximum points** ("phenotype highly specific for gene"), patient must meet criteria for PP4
- To obtain **standard points** ("phenotype consistent with gene but not highly specific"), the phenotype of the patient must include hyperglycemia or impaired fasting glucose, with no evidence of an autoimmune etiology of diabetes and/or absolute or near-absolute insulin deficiency

**Exclusionary Evidence (autoimmune etiology or absolute/near-absolute insulin deficiency):**
- One or more positive diabetes autoantibodies (IA-2A, ZnT8A+, GAD)
- Very low or negative C-peptide, defined as either fasting or non-fasting random C-peptide (<200 pmol/L or 0.6 ng/mL) or urinary C-peptide/creatinine ratio <0.2 nmol/mmol
- Presence of clinically significant diabetes complications in anyone with the variant is an exclusion

**Determining Unaffected Status:**
- We expect to see hyperglycemia at birth in an individual with GCK-MODY and therefore consider an individual unaffected if euglycemic in childhood or adulthood
- Since individuals typically do not present with symptoms of diabetes, a statement that someone is "nondiabetic" is insufficient to consider a parent unaffected
- Fasting glucose must be tested and found to be within normal limits (<100 mg/dl = 5.5 mmol/L) or HbA1c ≤5.5% (37 mmol/mol) since the GCK range was 5.6 - 7.6% (38-60 mmol/mol)

**Do NOT apply PS2 if the proband has an affected parent with any of the following:**
- Affected parent meets PP4 specifications
- Parent is described as having similarly atypical diabetes to the proband
- Parent was diagnosed with non-autoimmune diabetes before age 30

#### PS2/PM6 Point System

See [Appendix B](#appendix-b-ps2pm6-de-novo-points-table) for the complete points table.

**Table 1: Points awarded per de novo occurrence**

| Phenotypic Consistency | Confirmed Parental Relationships | Unconfirmed Parental Relationships |
|------------------------|----------------------------------|-----------------------------------|
| Phenotype highly specific for gene | 2 points | 1 point |
| Phenotype consistent with gene but not highly specific | 1 point | 0.5 points |

**Table 2: Evidence Strength Thresholds**

| Points | Strength Level |
|--------|----------------|
| 0.5 | PS2_Supporting or PM6_Supporting |
| 1.0 | PS2_Moderate or PM6 |
| 2.0 | PS2 or PM6_Strong |
| 4.0 | PS2_VeryStrong or PM6_VeryStrong |

---

### PS3 - Functional Studies

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.

**Note:** Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.

**VCEP Specifications:**

Use GCK PS3/BS3 decision tree (see [Appendix E](#appendix-e-ps3bs3-decision-tree)), which incorporates:
- **Relative Activity Index (RAI)**
- **Relative Stability Index (RSI)**
- Assays that measure the impact of variants on binding with **GKRP** and **GKA**

**Important Requirements:**
- For canonical splice site variants, do not use PS3 for RNA studies demonstrating abnormal splicing, since PVS1 will already be used at some level
- To use PS3, functional study must have been performed on a **transfected variant**
- If a study was performed on a cell line generated from a patient sample (and therefore contains the variant plus any other genomic variation the patient has), it does not count as PS3

#### Strength Levels

| Strength | Criteria |
|----------|----------|
| **Strong** | Applicable to non-canonical splice site variants that have RNA and in silico evidence of aberrant splicing. |
| **Moderate** | RAI ≤0.5 (see decision tree for details). |
| **Supporting** | MT: Kcat/S0.5 / WT: Kcat/S0.5 < 0.5 OR RSI ≤0.5 with impact on GKRP and/or GKA interaction (see decision tree for details). |

#### Functional Study Parameters

**WT GCK kinetic parameters that must be met (including SEM):**
1. Kcat: 40-80
2. S0.5: 6.0-9.0
3. h: 1.4-1.8

**Activity Index Calculation:**
```
Ia = [ATP]/([ATP] + Km) × Kcat/S0.5^h
RAI = Ia-MT / Ia-WT
```

**Decision Points:**
- Is the WT Km available and between 0.2-0.5? → If YES, calculate RAI
- RAI ≤0.5 → **PS3_Moderate**
- RSI ≤0.5 → Proceed to assess GKRP/GKA impact
- Impact on GKRP and/or GKA interaction → **PS3_Supporting**

---

### PS4 - Prevalence in Affected

**Original ACMG Summary:** The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.

**Note 1:** Relative risk (RR) or odds ratio (OR), as obtained from case-control studies, is >5.0 and the confidence interval around the estimate of RR or OR does not include 1.0.

**Note 2:** In instances of very rare variants where case-control studies may not reach statistical significance, the prior observation of the variant in multiple unrelated patients with the same phenotype, and its absence in controls, may be used as moderate level of evidence.

**VCEP Specifications:**
- Variant should meet **PM2_Supporting** in order to use PS4 at any level
- Careful review of gnomAD QC data may be necessary to assess whether variant is real or an artifact, especially if variant is in a polyC region
- Phenotype of the patient must include diabetes, with evidence of an autoimmune etiology and/or absolute or near-absolute insulin deficiency considered as **exclusionary**

**Exclusionary Evidence:**
- One or more positive diabetes autoantibodies (IA-2A, ZnT8A+, GAD)
- Very low or negative C-peptide (<200 pmol/L or 0.6 ng/mL) or urinary C-peptide/creatinine ratio <0.2 nmol/mmol

#### Strength Levels

| Strength | Criteria |
|----------|----------|
| **Strong** | ≥7 occurrences in unrelated individuals |
| **Moderate** | 4-6 occurrences in unrelated individuals |

---

### PM1 - Mutational Hot Spot

**Original ACMG Summary:** Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.

**VCEP Specifications:** Applicable for glucose- and ATP-binding sites (see [Appendix D](#appendix-d-pm1-residues) for details).

#### PM1 (Moderate) - Applicable Residues

**Glucose-binding sites (22 residues):**
- Ser151 - Pro153
- Thr168 - Lys169
- Asn204 - Thr206
- Ile225 - Asn231
- Asn254 - Gly258
- Gln287
- Glu290

**ATP-binding sites (29 residues):**
- Asp78 - Arg85
- Ser151
- Lys169
- Asp205
- Ile225 - Gly229
- Gly295 - Lys296
- Glu331 - Arg333
- Ser336
- Gly410 - His416

---

### PM2 - Absent from Controls

**Original ACMG Summary:** Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

**Caveat:** Population data for indels may be poorly called by next generation sequencing.

**VCEP Specifications:**
- Recommend using as **supporting level** of evidence (PM2_Supporting) per ClinGen guidance
- Per guidance from ClinGen/SVI, PM2_Supporting + PVS1 is sufficient evidence of a variant being likely pathogenic
- We recommend investigating the genotype metrics in gnomAD for variants that have been flagged for having failed one or more quality parameters, as it is possible that some of these filtered variants are actually real
- The number of filtered alleles can be counted to determine whether PM2_Supporting would be met even if they were genuine calls
- If the filtered calls are sufficient in number to not meet PM2_Supporting, then we would not use it
- Because it is also possible that these calls are false positives, we would not use filtered variants to support BA1 or BS1
- Use Grpmax FAF cutoffs using combined frequencies or dataset (exomes or genomes) with highest denominator if combined not available in gnomAD v4.1

#### Strength Level

| Strength | Criteria |
|----------|----------|
| **Supporting** | gnomAD Grpmax FAF ≤ 1:333,000 (≤ 0.000003 or 0.0003%) |

---

### PM3 - In Trans with Pathogenic

**Original ACMG Summary:** For recessive disorders, detected in trans with a pathogenic variant.

**Note:** This requires testing of parents (or offspring) to determine phase.

**VCEP Specifications:**
- Applicable for variants found in **neonatal diabetes**
- Criterion can also be used to interpret the pathogenicity of a heterozygous variant (i.e., GCK-MODY) if the variant under assessment has also been identified in a patient with neonatal diabetes in the homozygous state or in trans (or phase unknown per the point system) with a P/LP variant or VUS
- Use SVI-recommended point-based system (see [Appendix C](#appendix-c-pm3-points-table))

#### PM3 Point System

**Table 1: Points awarded per in trans proband**

| Classification/Zygosity of Other Variant | Confirmed in Trans | Phase Unknown |
|------------------------------------------|-------------------|---------------|
| Pathogenic or Likely pathogenic variant | 1.0 | 0.5 (P) / 0.25 (LP) |
| Homozygous occurrence (max point 1.0) | 0.5 | N/A |
| Uncertain significance variant (max point 0.5) | 0.25 | 0.0 |

*Note: All variants should be sufficiently rare (meet PM2 specification)*

**Table 2: Evidence Strength Thresholds**

| Total Points | Strength Level |
|--------------|----------------|
| 0.5 | PM3_Supporting |
| 1.0 | PM3 (Moderate) |
| 2.0 | PM3_Strong |
| 4.0 | PM3_VeryStrong |

---

### PM4 - Protein Length Changes

**Original ACMG Summary:** Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

#### Strength Levels

| Strength | Criteria |
|----------|----------|
| **Moderate** | For deletions/insertions of **more than one amino acid** in a non-repeat region |
| **Supporting** | Apply at the Supporting level when there is an insertion or deletion of a **single amino acid** in a non-repeat region |

---

### PM5 - Novel Missense at Same Residue

**Original ACMG Summary:** Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.

**Example:** Arg156His is pathogenic; now you observe Arg156Cys.

**Caveat:** Beware of changes that impact splicing rather than at the amino acid/protein level.

#### Strength Levels

| Strength | Criteria |
|----------|----------|
| **Strong** | Applicable once **two amino acid changes** have been classified as pathogenic at the same amino acid residue |
| **Moderate** | The novel amino acid change must have a Grantham distance **greater than or equal to** the previously classified pathogenic variant |
| **Supporting** | Apply if the previously classified amino acid change is **likely pathogenic** (rather than pathogenic) OR if the previously classified variant is pathogenic but has a **greater Grantham distance** |

---

### PM6 - De Novo (Assumed)

**Original ACMG Summary:** Assumed de novo, but without confirmation of paternity and maternity.

**VCEP Specifications:** *Not Applicable* - Subsumed in PS2. Use the PS2/PM6 point-based system above.

---

### PP1 - Co-segregation

**Original ACMG Summary:** Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.

**Note:** May be used as stronger evidence with increasing segregation data.

**VCEP Specifications:**
- Variable penetrance and phenocopies complicate co-segregation studies
- The presence of type 1 and type 2 diabetes phenocopies and significance of variants in unaffected individuals as defined above will need to be considered
- We expect to see hyperglycemia at birth in an individual with GCK-MODY and therefore consider an individual unaffected if euglycemic in childhood or adulthood
- Since individuals typically do not present with symptoms of diabetes, a statement that someone is "nondiabetic" is insufficient to classify a family member as unaffected
- Fasting glucose must be tested and found to be within normal limits (<100 mg/dl = 5.5 mmol/L) or HbA1c test ≤5.5% since the GCK range was 5.6 - 7.6%
- Presence of clinically significant diabetes complications in anyone with the variant is an exclusion

#### PP1 Thresholds (Jarvik and Browning)

| Strength | Single Family | >1 Family |
|----------|--------------|-----------|
| **Strong** | ≤ 1/32 (5 meioses) | ≤ 1/16 (4 meioses) |
| **Moderate** | ≤ 1/16 (4 meioses) | ≤ 1/8 (3 meioses) |
| **Supporting** | ≤ 1/8 (3 meioses) | ≤ 1/4 (2 meioses) |

---

### PP2 - Missense in Constrained Gene

**Original ACMG Summary:** Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.

**VCEP Specification (Supporting):**

Apply to **all missense variants in GCK**. gnomAD missense constraint score for GCK is 3.07 (observed/expected = 0.5), which is significant.

---

### PP3 - Computational Evidence

**Original ACMG Summary:** Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).

**Caveat:** As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.

**VCEP Specification (Supporting):**
- Use **REVEL score of ≥0.70** as supportive evidence of pathogenicity
- We also support using **SpliceAI** to assess the predicted impact of non-canonical splicing variants and synonymous variants: apply PP3 when the predicted change is **at least 0.2**

---

### PP4 - Phenotype Specificity

**Original ACMG Summary:** Patient's phenotype or family history is highly specific for a disease with a single genetic etiology.

**VCEP Specifications:**
- Negative testing of other genes not necessary because phenotype is very specific
- Sixty percent of patients with GCK-MODY phenotype will test positive
- There is a small chance that patient has HNF1A- or HNF4A-MODY in the early stages of disease (can get info about likelihood from family history)
- Non-glycemic factors including hemoglobinopathies can affect HbA1c levels. This should be considered in cases where the HbA1c is outside the typical GCK range but fasting glucose and other features are consistent with GCK-hyperglycemia
- About 1% of patients with GCK-MODY will have deletions or other variants (e.g., promoter) that are not identified via Sanger sequencing - consider testing via NGS or other technology
- For patients tested because of neonatal diabetes, PP4 can be applied if there has been negative testing for three most common monogenic causes for neonatal diabetes: ABCC8, KCNJ11, and INS
- In consanguineous cases, EIF2AK3 should be tested as well

#### Strength Levels

| Strength | Criteria |
|----------|----------|
| **Moderate** | HbA1C 5.6-7.6% (38-60 mmol/mol) AND fasting plasma glucose (FPG) always 5.5-8 mmol/L (100-144 mg/dL) AND presence of any additional features (see below) |
| **Supporting** | HbA1C 5.6-7.6% (38-60 mmol/mol) AND fasting plasma glucose (FPG) always 5.5-8 mmol/L (100-144 mg/dL) |

**Additional Features for PP4_Moderate:**
- Pediatric patient (prepubertal or <10 years) picked up in the absence of symptoms, either incidentally during workup for an unrelated indication or during routine screening
- Multiple values (=persistent) of mild fasting hyperglycemia in PP4 range:
  - Either (≥1 HbA1c + ≥2 FPG) OR (≥2 HbA1c + ≥1 FPG)
  - Only 1 HbA1c and 1 FPG in range but they are at least 6 months apart
  - Patient in literature is described as having a multi-year history of impaired fasting glucose (IFG)
- OGTT (oral glucose tolerance test) with 2-hour increment <3 mmol/L (54 mg/dl)
- Antibody negative
- Macrosomia in normoglycemic offspring of hyperglycemic gestational parent
- Low birthweight in hyperglycemic offspring of hyperglycemic gestational parent
- Three-generation, dominant family history of diabetes or hyperglycemia (in a family not used for PP1)

---

### PP5 - Reputable Source

**Original ACMG Summary:** Reputable source recently reports variant as pathogenic, but the evidence is not available to the laboratory to perform an independent evaluation.

**VCEP Specifications:** *Not Applicable*

This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee. (PubMed: 29543229)

---

## Benign Criteria

### BA1 - Allele Frequency >5%

**Original ACMG Summary:** Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

**VCEP Specification (Stand Alone):**
- gnomAD Grpmax FAF **≥ 1:10,000** (≥ 0.01% or 0.0001)

---

### BS1 - Frequency Greater Than Expected

**Original ACMG Summary:** Allele frequency is greater than expected for disorder.

**VCEP Specification (Strong):**
- gnomAD Grpmax FAF **≥ 1:25,000** (0.004% or 0.00004)

---

### BS2 - Observed in Healthy Adult

**Original ACMG Summary:** Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

**VCEP Specification (Strong):**
- We expect to see hyperglycemia at birth in an individual with GCK-MODY and therefore consider an individual unaffected if euglycemic in childhood or adulthood
- Since individuals typically do not present with symptoms of diabetes, evidence that someone is "nondiabetic" is insufficient
- Fasting glucose must be tested and found to be within normal limits (<100 mg/dl / 5.5 mmol/L)

---

### BS3 - Functional Studies (No Effect)

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

**VCEP Specifications:**
- To use BS3, functional study must have been performed on a **transfected variant**
- If a study was performed on a cell line generated from a patient sample (and therefore contains the variant plus any other genomic variants the patient has) it cannot count as BS3
- Use GCK PS3/BS3 decision tree (see [Appendix E](#appendix-e-ps3bs3-decision-tree))

#### Strength Levels

| Strength | Criteria |
|----------|----------|
| **Strong** | Applicable to non-canonical splice site variants that have RNA and in silico evidence of **normal splicing** (see BP4) |
| **Supporting** | Normal RAI (>0.5) + normal RSI (>0.5) + normal inhibition/activation with GKRP/GKA = BS3_Supporting |

**Note:** Normal RAI (>0.5) + normal RSI (>0.5) but no studies investigating GKRP/GKA = **Cannot use PS3 or BS3**

---

### BS4 - Lack of Segregation

**Original ACMG Summary:** Lack of segregation in affected members of a family.

**Caveat:** The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.

**VCEP Specification (Strong):**

Applicable to family members without variant who meet PP4 criteria:
- HbA1C 5.6-7.6% (38-60 mmol/mol) (if given multiple results, use maximum value) AND
- Fasting glucose 5.5-8 mmol/L (100-144 mg/dL)

---

### BP1-BP7 - Benign Supporting

| Criterion | Status | Specification |
|-----------|--------|---------------|
| **BP1** | *Not Applicable* | Missense variant in a gene for which primarily truncating variants are known to cause disease. |
| **BP2** | Supporting | Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder or observed in cis with a pathogenic variant in any inheritance pattern. Also applicable when in cis or trans with a **likely pathogenic** variant. |
| **BP3** | *Not Applicable* | In-frame deletions/insertions in a repetitive region without a known function. |
| **BP4** | Supporting | Use a **REVEL score of ≤0.15** as supportive evidence of no predicted impact on the gene or gene product. We also support using **SpliceAI** to assess the predicted impact of non-canonical splicing variants and synonymous variants: apply BP4 when the predicted change is **below 0.2**. |
| **BP5** | Supporting | Variant found in a case with an alternate molecular basis for disease. A variant in another monogenic diabetes gene is P/LP. |
| **BP6** | *Not Applicable* | Reputable source recently reports variant as benign, but the evidence is not available to the laboratory to perform an independent evaluation. This criterion is not for use as recommended by the ClinGen SVI VCEP Review Committee. (PubMed: 29543229) |
| **BP7** | Supporting | A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved. Apply BP7 when the predicted change from **SpliceAI is below 0.2** AND **phyloP100 way < 2.0**. |

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

### Appendix A: PVS1 Decision Tree

#### Nonsense or Frameshift Variants
```
Nonsense or Frameshift
├── Predicted to undergo NMD → PVS1
└── Not predicted to undergo NMD
    └── Truncated/altered region is critical to protein function → PVS1
```

#### GT-AG 1,2 Splice Site Variants
```
GT-AG 1,2 splice sites
├── Exon skipping or use of cryptic splice site disrupts reading frame
│   ├── Predicted to undergo NMD → PVS1
│   └── NOT predicted to undergo NMD
│       └── Truncated/altered region is critical to protein function → PVS1
└── Exon skipping or use of cryptic splice site preserves reading frame
    (exons 1, 4, 5, 8, 9, 10)
    └── Truncated/altered region is critical to protein function → PVS1
```

#### Deletion Variants
```
Deletion (Single exon to full gene)
├── Full gene deletion → PVS1*
├── Single to multi exon deletion
│   ├── Disrupts reading frame and predicted to undergo NMD → PVS1
│   ├── Disrupts reading frame and NOT predicted to undergo NMD
│   │   └── Truncated/altered region is critical to protein function → PVS1
│   └── Preserves reading frame
│       └── Truncated/altered region is critical to protein function → PVS1
```

*Given that GCK is a known haploinsufficient gene, a pathogenic classification is warranted for a full gene deletion (in the absence of conflicting data).

#### Duplication Variants
```
Duplication (≥1 exon in size and must be completely contained within gene)
├── Proven in tandem
│   ├── Reading frame disrupted and NMD predicted to occur → PVS1
│   └── No or unknown impact on reading frame and NMD → N/A
├── Presumed in tandem
│   └── Reading frame presumed disrupted and NMD predicted to occur → PVS1_Strong
└── Proven not in tandem → N/A
```

#### Initiation Codon Variants
```
Initiation Codon
└── No known alternative start codon in other transcripts
    └── No pathogenic variant(s) upstream of closest potential in-frame start codon → PVS1_Supp
```

**Notes:**
- (a) This criterion should not be applied in combination with in silico splicing predictions (PP3). Additionally, splice site variants must have no detectable nearby (+/- 20 nts) strong consensus splice sequence that may reconstitute in-frame splicing.
- (b) NMD prediction based on the premature termination codon not occurring in the 3'-most exon or the 3'-most 50 bp of the penultimate exon.
- (c) Relevant domain indicated by experimental evidence proving a critical role of the domain and/or presence of non-truncating pathogenic variants in the region.

---

### Appendix B: PS2/PM6 De Novo Points Table

**Table 1: Points awarded per de novo occurrence**

| Phenotypic Consistency | De novo with Confirmed Parental Relationships | De novo with Unconfirmed Parental Relationships |
|------------------------|----------------------------------------------|------------------------------------------------|
| Phenotype highly specific for gene | 2 | 1 |
| Phenotype consistent with gene but not highly specific | 1 | 0.5 |

*Note: These points are NOT equivalent to the points used to classify a variant per the Tavtigian et al 2020 "Fitting a naturally scaled point system to the ACMG/AMP variant classification guidelines"*

**Table 2: Recommendation for determining the appropriate ACMG/AMP evidence strength level for de novo occurrence(s)**

| Supporting (PS2_Supporting or PM6_Supporting) | Moderate (PS2_Moderate or PM6) | Strong (PS2 or PM6_Strong) | Very Strong (PS2_VeryStrong or PM6_VeryStrong) |
|----------------------------------------------|-------------------------------|---------------------------|-----------------------------------------------|
| 0.5 | 1 | 2 | 4 |

---

### Appendix C: PM3 Points Table

**Table 1: Points awarded per in trans proband**

| Classification/Zygosity of Other Variant | Confirmed in Trans | Phase Unknown |
|------------------------------------------|-------------------|---------------|
| Pathogenic or Likely pathogenic variant | 1.0 | 0.5 (P) / 0.25 (LP) |
| Homozygous occurrence (max point 1.0) | 0.5 | N/A |
| Uncertain significance variant (max point 0.5) | 0.25 | 0.0 |

*All variants should be sufficiently rare (meet PM2 specification); P - Pathogenic; LP - Likely pathogenic*

**Table 2: Recommendation for determining the appropriate evidence strength level for PM3**

| PM3_Supporting | PM3 | PM3_Strong | PM3_VeryStrong |
|----------------|-----|------------|----------------|
| 0.5 | 1.0 | 2.0 | 4.0 |

---

### Appendix D: PM1 Residues

#### Glucose Binding Site (22 residues)

| Residue | Domain | Comment |
|---------|--------|---------|
| Ser151 - Pro153 | S | Ser151 makes H-bond interaction with Glc in closed conf. |
| Thr168 - Lys169 | S | Thr168 and Lys169 make H-bond interaction with Glc in closed conf. Lys169 is a general acid catalyst in the catalytic ternary complex. |
| Asn204 - Thr206 | L / CRII | Asn204 and Asp205 make H-bond interaction with Glc in closed conf. Asp205 is part of the catalytic ternary complex (general base catalyst). |
| Ile225 - Asn231 | L | Asn231 makes H-bond interaction with Glc in closed conf. |
| Asn254 - Gly258 | L | Glu256 makes H-bond interaction with Glc in closed conf. |
| Gln287 | L | Gln287 makes H-bond interaction with Glc in closed conf. |
| Glu290 | L | Glu290 makes H-bond interaction with Glc in closed conf. |

#### Mg²⁺-ATP Binding Site (29 residues)

| Residue | Domain | Comment |
|---------|--------|---------|
| Asp78 - Arg85 | S | Phosphate 1 motif. Asp78 is important for coordinating the Mg²⁺ ion in ternary complex. Thr82 H-binding to ATP-γ-S in crystal structure 3VEY. |
| Ser151 | S | Ser151 is important for coordinating the Mg²⁺ ion in ternary complex. |
| Lys169 | S | Lys169 makes H-bond interaction with ATP in closed conf. Lys169 is a general acid catalyst in the catalytic ternary complex. |
| Asp205 | L / CRII | Part of the Connect 1 motif. Asp205 makes H-bond interactions with Mg²⁺ and ATP. Part of the catalytic ternary complex (general base catalyst). |
| Ile225 - Gly229 | L | Phosphate 2 motif. Thr228 makes H-bond interaction with ATP and is part of the catalytic scaffold of GK. Gly229: H-binding to AMP-PNP according to crystal structure GK•Glc•AMP-PNP. |
| Gly295 - Lys296 | L | |
| Glu331 - Arg333 | L | |
| Ser336 | L | H-binding to AMP-PNP according to crystal structures. |
| Gly410 - His416 | L | Adenosine motif. Ser411: H-binding to AMP-PNP according to crystal structures. |

---

### Appendix E: PS3/BS3 Decision Tree

#### Functional Study Requirements

**WT GCK kinetic parameters that must be met (including SEM):**
1. Kcat: 40-80
2. S0.5: 6.0-9.0
3. h: 1.4-1.8

If the above parameters are NOT met → **Cannot Use PS3 or BS3**

#### Activity Index Calculation

```
Ia = [ATP] / ([ATP] + Km) × Kcat / S0.5^h
RAI = Ia-MT / Ia-WT
```

#### Decision Flow

```
Are WT GCK kinetic parameters met?
├── NO → Cannot Use PS3 or BS3
└── YES
    └── Is the WT Km available and between 0.2-0.5?
        ├── YES → Calculate RAI
        │   └── RAI ≤ 0.5?
        │       ├── YES → PS3_Moderate
        │       └── NO → Is RSI available?
        │           ├── NO → Cannot Use PS3 or BS3
        │           └── YES → RSI ≤ 0.5?
        │               ├── YES → PS3_Supporting
        │               └── NO → Does the variant impact interaction with GKRP and/or GKA?
        │                   ├── YES → PS3_Supporting
        │                   └── NO → BS3_Supporting
        └── NO → MT: Kcat/S0.5 / WT: Kcat/S0.5 < 0.5?
            ├── YES → PS3_Supporting
            └── NO → Continue with RSI assessment (see above)
```

#### Key for Decision Tree

| Abbreviation | Meaning |
|--------------|---------|
| WT | Wild type |
| MT | Mutant |
| SEM | Standard error of the mean |
| Kcat | Turnover number |
| S0.5 | Affinity for glucose |
| h | Hill number |
| Km | ATP affinity |
| RAI | Relative Activity Index |
| RSI | Relative Stability Index |

---

### Appendix F: Population Frequency Thresholds Summary

| Criterion | Threshold | Strength |
|-----------|-----------|----------|
| BA1 | gnomAD Grpmax FAF ≥ 1:10,000 (≥0.01% or 0.0001) | Stand Alone |
| BS1 | gnomAD Grpmax FAF ≥ 1:25,000 (≥0.004% or 0.00004) | Strong |
| PM2 | gnomAD Grpmax FAF ≤ 1:333,000 (≤0.000003 or 0.0003%) | Supporting |

---

### Appendix G: References

1. DiStefano MT, Hemphill SE, et al. *Curating Clinically Relevant Transcripts for the Interpretation of Sequence Variants.* J Mol Diagn (2018) 20(6):789-801. PMID: 30096381

2. Popp MW, Maquat LE. *Organizing principles of mammalian nonsense-mediated mRNA decay.* Annu Rev Genet (2013) 47:139-65. PMID: 24274751

3. Beck T, Miller BG. *Structural basis for regulation of human glucokinase by glucokinase regulatory protein.* Biochemistry (2013) 52(36):6232-9. PMID: 23957911

4. Brnich SE, Abou Tayoun AN, et al. *Recommendations for application of the functional evidence PS3/BS3 criterion using the ACMG/AMP sequence variant interpretation framework.* Genome Med (2019) 12(1):3. PMID: 31892348

5. Gloyn AL, Odili S, et al. *Insights into the structure and regulation of glucokinase from a novel mutation (V62M), which causes maturity-onset diabetes of the young.* J Biol Chem (2005) 280(14):14105-13. PMID: 15677479

6. Beer NL, Osbak KK, et al. *Insights into the pathogenicity of rare missense GCK variants from the identification and functional characterization of compound heterozygous and double mutations inherited in cis.* Diabetes Care (2012) 35(7):1482-4. PMID: 22611063

7. Raimondo A, Chakera AJ, et al. *Phenotypic severity of homozygous GCK mutations causing neonatal or childhood-onset diabetes is primarily mediated through effects on protein stability.* Hum Mol Genet (2014) 23(24):6432-40. PMID: 25015100

8. Jarvik GP, Browning BL. *Consideration of Cosegregation in the Pathogenicity Classification of Genomic Variants.* Am J Hum Genet (2016) 98(6):1077-1081. PMID: 27236918

9. Wai HA, Lord J, et al. *Blood RNA analysis can increase clinical diagnostic rate and resolve variants of uncertain significance.* Genet Med (2020) 22(6):1005-1014. PMID: 32123317

10. Jaganathan K, Kyriazopoulou Panagiotopoulou S, et al. *Predicting Splicing from Primary Sequence with Deep Learning.* Cell (2019) 176(3):535-548.e24. PMID: 30661751

11. MODY Probability Calculator: https://www.diabetesgenes.org/mody-probability-calculator/

12. Gloyn, et al. (2004). *Glucokinase and the Regulation of Blood Sugar.* In Matschinsky FM & Magnuson MA (Eds), Glucokinase and Glycemic Disease: From Basics to Novel Therapeutics. (pp. 92-109). Karger. DOI:10.1159/000079009

13. Hattersley AT, Greeley SAW, et al. *ISPAD Clinical Practice Consensus Guidelines 2018: The diagnosis and management of monogenic diabetes in children and adolescents.* Pediatr Diabetes (2018) 19 Suppl 27:47-63. PMID: 30225972

14. Pihoker C, Gilliam LK, et al. *Prevalence, characteristics and clinical diagnosis of maturity onset diabetes of the young due to mutations in HNF1A, HNF4A, and glucokinase: results from the SEARCH for Diabetes in Youth.* J Clin Endocrinol Metab (2013) 98(10):4055-62. PMID: 23771925

15. McDonald TJ, Colclough K, et al. *Islet autoantibodies can discriminate maturity-onset diabetes of the young (MODY) from Type 1 diabetes.* Diabet Med (2011) 28(9):1028-33. PMID: 21395678

16. Shields BM, Shepherd M, et al. *Population-Based Assessment of a Biomarker-Based Screening Pathway to Aid Diagnosis of Monogenic Diabetes in Young-Onset Patients.* Diabetes Care (2017) 40(8):1017-1025. PMID: 28701371

17. Patel KA, Weedon MN, et al. *Zinc Transporter 8 Autoantibodies (ZnT8A) and a Type 1 Diabetes Genetic Risk Score Can Exclude Individuals With Type 1 Diabetes From Inappropriate Genetic Testing for Monogenic Diabetes.* Diabetes Care (2019) 42(2):e16-e17. PMID: 30409810

18. Carlsson A, Shepherd M, et al. *Absence of Islet Autoantibodies and Modestly Raised Glucose Values at Diabetes Diagnosis Should Lead to Testing for MODY: Lessons From a 5-Year Pediatric Swedish National Cohort Study.* Diabetes Care (2020) 43(1):82-89. PMID: 31704690

19. Steele AM, Wensley KJ, et al. *Use of HbA1c in the identification of patients with hyperglycaemia caused by a glucokinase mutation: observational case control studies.* PLoS One (2013) 8(6):e65326. PMID: 23799006

---

## Version History

| Version | Date | Notes |
|---------|------|-------|
| 3.1.0 | 10/10/2025 | Updating PS2 to clarify when a family history of diabetes prevents the application of this criterion. Updating PS3/BS3 Decision Tree for clarity. |

---

*This document was compiled from ClinGen VCEP specifications and ClinGen SVI recommendations. For the most current version, please refer to the ClinGen website.*
