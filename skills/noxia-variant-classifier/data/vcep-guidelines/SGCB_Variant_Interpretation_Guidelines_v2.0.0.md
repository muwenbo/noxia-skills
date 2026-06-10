# ClinGen Limb Girdle Muscular Dystrophy VCEP Variant Interpretation Guidelines for SGCB

**Version:** 2.0.0
**Released:** 7/9/2025
**Affiliation:** Limb Girdle Muscular Dystrophy VCEP
**Based on:** Tavtigian et al., 2020 - Bayesian adaptation of Richards et al., 2015 ACMG/AMP Guidelines

**Release Notes (v2.0.0):**
- Specification type defined as Bayesian adaptation
- Correction to in-frame exons in PVS1 flowchart: PVS1
- Clarification on use of experimental RNA/splice data: PVS1, PP3, BP4, BP7
- Clarification on use of gnomAD population frequency data (no change to thresholds): PM2, BA1, BS1
- Reduced weighting of de novo observation: PS2, PM6
- Updated guidance on evaluating missense variants at the same position: PM5

---

## Gene Information

| Attribute | Value |
|-----------|-------|
| **Gene** | SGCB (HGNC:10806) |
| **HGNC Name** | sarcoglycan beta |
| **Transcript** | NM_000232.5 |
| **Disease** | Autosomal recessive limb-girdle muscular dystrophy (MONDO:0015152) |
| **Inheritance** | Autosomal recessive inheritance |

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
   - [BA1 - Allele Frequency >0.2%](#ba1---allele-frequency-02)
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
- Beware of genes where LOF is not a known disease mechanism (e.g., GFAP, MYH7).
- Use caution interpreting LOF variants at the extreme 3' end of a gene.
- Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact.
- Use caution in the presence of multiple transcripts.

**VCEP Specifications:**

Please see the SGCB PVS1 flowchart (Appendix A). In addition, for any variant with RNA/splicing data, follow the SVI Working Group's recommendations (Walker et al. 2023; PMID: 37352859). See Appendix B for the experimental splice data decision tree.

#### Strength Levels

| Strength | Default Points | Criteria |
|----------|---------------|----------|
| **Very Strong** | 8 | Follow the SGCB PVS1 decision tree. For any variant with RNA/splicing data, follow SVI Working Group recommendations (Walker et al. 2023; PMID: 37352859). |
| **Strong** | 4 | Follow the SGCB PVS1 decision tree. For any variant with RNA/splicing data, follow SVI Working Group recommendations (Walker et al. 2023; PMID: 37352859). |
| **Moderate** | 2 | Follow the SGCB PVS1 decision tree. For any variant with RNA/splicing data, follow SVI Working Group recommendations (Walker et al. 2023; PMID: 37352859). |
| **Supporting** | 1 | Follow the SGCB PVS1 decision tree. For any variant with RNA/splicing data, follow SVI Working Group recommendations (Walker et al. 2023; PMID: 37352859). |

#### PVS1 Decision Tree Summary for SGCB

**Nonsense or Frameshift:**
- **Predicted to undergo NMD** (premature truncation in codons 35-233): **PVS1**
- **Premature truncation within first 100 bp** (codons 1-34; PMID: 27618451): **PVS1_Moderate**
- **Not predicted to undergo NMD:**
  - Exon present in biologically relevant transcript (NM_000232.5):
    - Truncated/altered region critical to protein function (none specified): **PVS1_Strong**
    - Role of region unknown:
      - LoF variants in exon frequent in general population / exon absent from biologically relevant transcripts: **N/A**
      - LoF variants not frequent AND exon present:
        - Variant removes >10% of protein: **PVS1_Strong**
        - Variant removes <10% of protein: **PVS1_Moderate**

**Canonical GT-AG +/-1,2 Splice Sites:**
- Use SpliceAI prediction of the most likely splice effect, then determine expected protein consequence
- **Exon skipping/cryptic splice site disrupts reading frame AND predicted to undergo NMD:** **PVS1**
- **Exon skipping/cryptic splice site preserves reading frame:**
  - In-frame exons for which exon skipping is not expected to result in NMD: **exons 1, 2, 3, 4, 5, 6**
  - Exon present in biologically relevant transcript:
    - Truncated/altered region critical to protein function (none specified): **PVS1_Strong**
    - Role unknown:
      - LoF variants frequent / exon absent from biologically relevant transcripts: **N/A**
      - LoF variants not frequent AND exon present:
        - Variant removes >10% of protein: **PVS1_Strong**
        - Variant removes <10% of protein: **PVS1_Moderate**
- **Exon skipping/cryptic splice site disrupts reading frame, NOT predicted to undergo NMD:** Same logic as above for protein impact assessment

**Deletion (Single exon to full gene):**
- **Single/multi-exon deletion disrupting reading frame AND predicted to undergo NMD:** **PVS1**
- **Full gene deletion:** **PVS1**
- **Single/multi-exon deletion preserving reading frame:** Apply same logic as splice site variants for protein impact
- **Single/multi-exon deletion disrupting reading frame, NOT predicted to undergo NMD:** Apply same logic for protein impact

**Duplication (≥1 exon, completely contained within gene):**
- **Proven in tandem, reading frame disrupted and NMD predicted:** **PVS1**
- **Proven in tandem, no or unknown impact on reading frame:** **N/A**
- **Presumed in tandem, reading frame presumed disrupted and NMD predicted:** **PVS1_Strong**
- **Proven not in tandem:** **N/A**

**Initiation Codon:**
- Different functional transcript uses alternative start codon: **PVS1_Supporting**
- No known alternative start codon:
  - ≥1 pathogenic variant upstream of closest potential in-frame start codon: **PVS1_Moderate**
  - No pathogenic variants upstream: **N/A**

---

### PS1 - Same Amino Acid Change

**Original ACMG Summary:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change. Example: Val->Leu caused by either G>C or G>T in the same codon. Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:**

#### For Missense Variants (Amino Acid Change as Expected Mechanism)

| Strength | Default Points | Criteria |
|----------|---------------|----------|
| **Strong** | 4 | Apply for 1 pathogenic or 2 likely pathogenic variants resulting in the same amino acid change. The LP/P variant(s) must have been classified using LGMD VCEP specifications. Potential splice effects must be excluded for both the variant under curation and the variant(s) resulting in the same amino acid change (SpliceAI score ≤0.10 or experimental evidence of normal splicing). PS1 can be applied to multiple nucleotide changes at the same residue as long as the variant classification that determines the strength level does not depend on PS1 application. |
| **Moderate** | 2 | Apply for 1 likely pathogenic variant resulting in the same amino acid change. The LP variant must have been classified using LGMD VCEP specifications. Same splice exclusion requirements as Strong. |

**Note:** For missense variants encoded by the first or last 3 nucleotides of an exon, PS1 should be considered only in the context of altered splicing (see below), unless a splice effect has been experimentally ruled out for the variant under curation and the variant(s) resulting in the same amino acid change.

#### For Splice Variants (Nucleotide Change as Expected Mechanism)

| Strength | Default Points | Criteria |
|----------|---------------|----------|
| **Strong** | 4 | Follow SVI Working Group recommendations (Walker et al. 2023; PMID: 37352859), as outlined in the PS1 splicing table (Appendix C). |
| **Moderate** | 2 | Follow SVI Working Group recommendations (Walker et al. 2023; PMID: 37352859). |
| **Supporting** | 1 | Follow SVI Working Group recommendations (Walker et al. 2023; PMID: 37352859). |

---

### PS2 - De Novo (Confirmed)

**Original ACMG Summary:** De novo (both maternity and paternity confirmed) in a patient with the disease and no family history. Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.

**VCEP Specifications:**

| Strength | Default Points | Criteria |
|----------|---------------|----------|
| **Supporting** | 1 | Apply for confirmed *de novo* occurrence in a proband meeting the criteria for PP4 (Supporting). Maternity and paternity should be confirmed by trio WES/WGS or other testing. |

> **Note:** This is a reduced strength from the default ACMG PS2 (Strong), reflecting the autosomal recessive inheritance pattern. Only Supporting level is applicable for SGCB.

---

### PS3 - Functional Studies

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product. Note: Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.

**VCEP Specifications:**

| Strength | Default Points | Criteria |
|----------|---------------|----------|
| **Strong** | 4 | Variant-specific animal model meeting ALL of the following conditions (regardless of species): (1) signs of myopathy or dystrophy in skeletal muscle, (2) an effect on gene or protein function demonstrated (e.g., decreased protein expression, impaired membrane localization, or other functional abnormality), (3) behavioral signs of muscle weakness, (4) progression over time. |
| **Moderate** | 2 | Variant-specific animal model meeting: (1) signs of myopathy or dystrophy in skeletal muscle, (2) an effect on gene or protein function demonstrated. **OR** Sarcoglycan complex membrane localization assays clinically validated with ≥11 control variants per Brnich et al. 2020 (PMID: 31892348). Specifically: cell surface localization functional score <-0.5 in Li et al. 2023 (PMID: 37317968). |
| **Supporting** | 1 | Variant expressed in heterologous cell lines/model organisms showing absent membrane localization of the sarcoglycan protein complex and fewer than 11 control variants used, per Brnich et al. 2020 (PMID: 31892348). |

**Important Notes:**
- For any variant type, experimental evidence for altered splicing should be scored under **PVS1** (not PS3), in accordance with the decision tree for RNA splicing assay results outlined in Walker et al. 2023 (PMID: 37352859).
- Apply PS3 only once, for the piece of evidence that meets the highest possible strength level.

#### Approved Assay Instances

| Assay | Instance 1 (Soheili et al. 2012) | Instance 2 (Li et al. 2023) |
|-------|----------------------------------|----------------------------|
| **PMID** | 22095924 | 37317968 |
| **General Description** | Membrane localization of sarcoglycan complex | Membrane localization of sarcoglycan complex |
| **Material** | Vectors expressing SGCB variant transfected into HER-911 cells expressing the three other sarcoglycans | Lentiviral vectors expressing SGCB variant transduced into HEK293 cells stably expressing the three other sarcoglycans |
| **Readout** | Qualitative - confocal immunofluorescence of nonpermeabilized cells | Quantitative - functional scores ranging from -2.9 to 1.46 |
| **Biological Replicates** | Not described | Met |
| **Technical Replicates** | Not described | Met (mean ± SEM reported) |
| **Positive Control** | WT | WT |
| **Negative Control** | Expression of α-sarcoglycan alone | Expression of SGCB fusion protein alone |
| **P/LP Validation Controls** | 7 (2 validated by VCEP) | 15 (3 validated by VCEP) |
| **B/LB Validation Controls** | 0 | 3 + 318 synonymous variants (9 validated by VCEP) |
| **Normal Threshold** | Membrane localized | Functional score ≥-0.5 |
| **Abnormal Threshold** | Absent at membrane | Functional score <-0.5 |
| **Approved Strength** | PS3_Supporting; BS3 not applied | PS3_Moderate; BS3 not applied |

---

### PS4 - Prevalence in Affected

**Original ACMG Summary:** The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls. Note 1: Relative risk (RR) or odds ratio (OR), as obtained from case-control studies, is >5.0 and the confidence interval around the estimate of RR or OR does not include 1.0. Note 2: In instances of very rare variants where case-control studies may not reach statistical significance, the prior observation of the variant in multiple unrelated patients with the same phenotype, and its absence in controls, may be used as moderate level of evidence.

**VCEP Specifications:**

| Strength | Default Points | Criteria |
|----------|---------------|----------|
| **Strong** | 4 | Use without disease-specific modification if case-control studies are available. |

> **Note:** While case-control studies could potentially be considered for a few pathogenic variants with high minor allele frequency, the VCEP is unaware of any such studies being conducted for *SGCB*. Any case-control study would require careful selection of an appropriate control population given the potential for late onset and mild disease.

---

### PM1 - Mutational Hot Spot

**Original ACMG Summary:** Located in a mutational hot spot and/or critical and well-established functional domain (e.g., active site of an enzyme) without benign variation.

**VCEP Specification:** ***Not Applicable***

> Not applicable at this time.

---

### PM2 - Absent from Controls

**Original ACMG Summary:** Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium. Caveat: Population data for indels may be poorly called by next generation sequencing.

**VCEP Specification (Supporting only):**

| Strength | Default Points | Criteria |
|----------|---------------|----------|
| **Supporting** | 1 | Apply if the Grpmax variant allele frequency / upper bound of the 95% CI of the Grpmax variant allele frequency in gnomAD is **<0.00009**. |

**Detailed Rules:**
- If only 1 or 2 variant alleles are present in the Grpmax population, use the Grpmax variant allele frequency
- If at least 3 variant alleles are present in the Grpmax population, use the upper bound of the 95% confidence interval (95% CI) of the Grpmax variant allele frequency
- **Grpmax** refers to the gnomAD subpopulation with the highest variant allele frequency
- **Exclude** from Grpmax: Amish, Ashkenazi Jewish, European Finnish, and Remaining Individuals groups, as well as the genomes-only data for the Middle Eastern group
- The upper bound of the 95% CI must be calculated using variant allele numbers and counts from gnomAD. Confidence interval tools such as Confit-de-MAF (https://www.genecalculators.net/confit-de-maf.html) can be used
- Use the gnomAD version with the largest allele number
- Do not use data for which the variant does not pass quality control filters
- For larger deletions or duplications that may not be well represented in gnomAD (e.g., single- or multi-exon events), also confirm the variant is not common in gnomAD SVs, gnomAD CNVs, or the Database of Genomic Variants (DGV) (https://dgv.tcag.ca/dgv/app/home)

---

### PM3 - In Trans with Pathogenic

**Original ACMG Summary:** For recessive disorders, detected in trans with a pathogenic variant. Note: This requires testing of parents (or offspring) to determine phase.

**VCEP Specifications:** Use the SVI Working Group's recommended point system to determine PM3 strength.

#### PM3 Point System (Per Proband)

| Classification/Zygosity of Other Variant | Confirmed in Trans | Phase Unknown |
|------------------------------------------|-------------------|---------------|
| Pathogenic or Likely pathogenic variant | 1.0 | 0.5 (P) / 0.25 (LP) |
| Homozygous occurrence (max 1.0 pt; downgrade to 0.25 pts for consanguinity) | 0.5 | N/A |
| Uncertain significance variant (max 0.5 pts total) | 0.25 | 0 |

**Footnotes:**
1. Author assertions on phase, including based on allele-specific transcript expression, are acceptable.
2. For variants identified in unknown phase, PM3 points should **not** be awarded under the following circumstances:
   - The same variants were ever confirmed in *cis* (e.g., in a different patient in the literature)
   - gnomAD co-occurrence data (https://gnomad.broadinstitute.org/variant-cooccurrence) predict the variants may be part of the same haplotype in at least one genetic ancestry group
   - More than 2 variants are reported in the patient, none of which can be classified as likely benign or benign
3. Any variant awarded points as likely pathogenic or pathogenic must have been classified using the LGMD VCEP specifications.
4. For any variant awarded points as VUS, benign frequency codes (BA1, BS1) cannot be applicable.

#### PM3 Evidence Strength Thresholds

| Total Points | Strength Level | Default Points |
|--------------|----------------|---------------|
| ≥0.5 but <1.0 | PM3_Supporting | 1 |
| ≥1.0 but <2.0 | PM3 (Moderate) | 2 |
| ≥2.0 but <4.0 | PM3_Strong | 4 |
| ≥4.0 | PM3_VeryStrong | 8 |

#### PM3 Co-Application Rules

It is possible to award PM3 points to **both** variants identified in an individual as long as the evidence related to their co-observation in that individual does not contribute to the variant classification that determines the number of points applied. This excludes all evidence derived from the co-observation, including:
- Inter-dependent PM3 points (pathogenicity of variant in trans/unknown phase)
- PP1 (genotype-phenotype co-segregation)
- PP4 (phenotype specificity)

**Example 1 — PM3 can be awarded to both variants:**
Variants A and B are observed in trans in patient X (who meets PP4). Variant A is classified as LP independent of patient X (e.g., PVS1 + PM2_Supporting). Variant B is also classified as LP independent of patient X (e.g., PS3_Moderate + PP3 + PM2_Supporting + PP4_Moderate from patient Y + PM3 from variant C in patient Y). In this scenario, 1.0 PM3 pt can be awarded to each variant for the observation in patient X, since both are independently LP.

**Example 2 — PM3 cannot be awarded to both variants:**
Variants A and B are observed in trans in patient X. Variant A is LP independent of patient X (PVS1 + PM2_Supporting). Variant B is VUS independent of patient X (PS3_Moderate + PP3 + PM2_Supporting + PP4 from patient Y). PM3 can be awarded to variant B (confirmed in trans with LP variant A = 1.0 pt), but PM3 cannot meaningfully be awarded to variant A for patient X because variant B is only VUS independent of that observation (0.25 pts, insufficient for any PM3 strength level).

---

### PM4 - Protein Length Changes

**Original ACMG Summary:** Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

**VCEP Specifications:**

| Strength | Default Points | Criteria |
|----------|---------------|----------|
| **Moderate** | 2 | Use as is, regardless of the length of the in-frame insertion or deletion. |

---

### PM5 - Novel Missense at Same Residue

**Original ACMG Summary:** Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before. Example: Arg156His is pathogenic; now you observe Arg156Cys. Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:**

Apply only for missense variants for which the amino acid change is the expected mechanism of disease. For the missense variant under curation and the variant(s) resulting in a different amino acid change:
- Exclude likely splice effects (SpliceAI score <0.5 or experimental evidence of normal splicing)
- The REVEL score for the missense variant under curation should be >0.7
- Missense changes at the same residue must be classified according to LGMD VCEP specifications
- No benign missense variation should be present at the residue
- Do not apply for missense variants encoded by the first or last 3 nucleotides of an exon unless a splice effect has been ruled out

PM5 can potentially be applied to multiple amino acid changes at the same residue as long as the variant classification that determines the strength level does not depend on PM5 application.

| Strength | Default Points | Criteria |
|----------|---------------|----------|
| **Strong** | 4 | 2 pathogenic or 3 likely pathogenic variants resulting in different amino acid changes at the same residue. |
| **Moderate** | 2 | 1 pathogenic or 2 likely pathogenic variants resulting in different amino acid changes at the same residue. |
| **Supporting** | 1 | 1 likely pathogenic variant resulting in a different amino acid change at the same residue. |

---

### PM6 - De Novo (Assumed)

**Original ACMG Summary:** Assumed de novo, but without confirmation of paternity and maternity.

**VCEP Specification:** ***Not Applicable***

> Not applicable. See PS2.

---

### PP1 - Co-segregation

**Original ACMG Summary:** Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease. Note: May be used as stronger evidence with increasing segregation data.

**VCEP Specifications:**

Segregations should be counted across families, with the total number of segregations determining the strength level.

| Strength | Default Points | Criteria |
|----------|---------------|----------|
| **Strong** | 4 | 3 affected segregations (in addition to proband) across ≥2 families. |
| **Moderate** | 2 | 2 affected segregations (in addition to proband; may be from a single family). |
| **Supporting** | 1 | 1 affected segregation (in addition to proband). |

> **Important:** When applied together, PP1 and PP4 cannot exceed 5 Bayesian points (Supporting + Strong or Moderate + Moderate).

---

### PP2 - Missense in Constrained Gene

**Original ACMG Summary:** Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.

**VCEP Specification:** ***Not Applicable***

> Not applicable. SGCB is not constrained for missense variation (Z-score <3).

---

### PP3 - Computational Evidence

**Original ACMG Summary:** Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.). Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.

**VCEP Specifications:**

| Strength | Default Points | Criteria |
|----------|---------------|----------|
| **Supporting** | 1 | **For missense variants:** use REVEL with a score **≥0.7**. **For variants that may affect splicing:** use SpliceAI with a score **≥0.5**. |

> **Note:** For any variant with RNA or other experimental data indicating an impact on splicing, follow the SVI Working Group's recommendations (Walker et al. 2023; PMID: 37352859). See Appendix B for the experimental splice data decision tree.

---

### PP4 - Phenotype Specificity

**Original ACMG Summary:** Patient's phenotype or family history is highly specific for a disease with a single genetic etiology.

**VCEP Specifications:**

Use the PP4 table below to determine the appropriate PP4 strength level. Apply PP4 only once, for a patient meeting the highest possible strength level.

| Strength | Default Points | Criteria |
|----------|---------------|----------|
| **Strong** | 4 | All three criteria met (clinical + genetic testing + protein expression). |
| **Moderate** | 2 | Use the PP4 table. If PP1_Moderate is applied and the criteria for PP4_Strong are also met, a downgraded PP4_Moderate can be applied. |
| **Supporting** | 1 | Clinical and genetic testing criteria met (protein expression not required). |

> **Important:** When applied together, PP1 and PP4 cannot exceed 5 Bayesian points (Supporting + Strong or Moderate + Moderate).

#### PP4 Point Table

|  | Criteria | PP4 Supporting | PP4 Strong |
|--|----------|---------------|------------|
| **Clinical** | Progressive limb-girdle pattern of muscle weakness observed over ≥6 months OR clinical suspicion of LGMD | **Y** (required) | **Y** (required) |
| **Genetic Testing** | 2 presumed diagnostic variants in SGCB, 1 of which is the variant under curation | **Y** (required) | **Y** (required) |
| **Protein Expression** | Reduced expression or membrane localization of full-length protein in skeletal muscle (e.g., WB or IHC) | **N** (not required) | **Y** (required) |

**Y** = Required to apply PP4 at specified strength level; **N** = Not required.

**Footnotes:**
1. May be accompanied by supporting EMG, MRI, muscle histology, elevated CK but not required.
2. Screening of all exons and exon/intron boundaries of SGCB required for Supporting. To apply at Strong, screening of SGCA, SGCG, and SGCD also required. Do not apply if 2 presumed diagnostic variants also identified in SGCA, SGCG, or SGCD. Screening of additional neuromuscular disease genes (e.g., through a panel) is recommended but not required.
3. If variants have not yet been curated by the LGMD VCEP, confirm they cannot be classified as LB or B (e.g., through application of BA1, BS1, and/or BP4/BP7). If phase is unknown, do not apply if the identified variants were ever confirmed in cis or if gnomAD co-occurrence data predict the variants may be part of the same haplotype in at least one genetic ancestry group.
4. Reduced = <~30% normal; may be described as "severely" / "drastically" / "strongly" reduced or as "absent", "trace", or "barely detectable".

---

### PP5 - Reputable Source

**Original ACMG Summary:** Reputable source recently reports variant as pathogenic, but the evidence is not available to the laboratory to perform an independent evaluation.

**VCEP Specification:** ***Not Applicable***

> This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PMID: 29543229).

---

## Benign Criteria

### BA1 - Allele Frequency >0.2%

**Original ACMG Summary:** Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

**VCEP Specification (Stand Alone):**

Apply if the variant **Grpmax FAF** (the lower bound of the 95% confidence interval of the maximum credible genetic ancestry group allele frequency) is **>0.002**.

- This value can be taken directly from gnomAD
- Do not use data for which the variant does not pass quality control filters
- See Appendix D for a list of variants defined as exceptions to the benign frequency rules
- Ongoing updates to the exception list will be available at the LGMD VCEP webpage: https://clinicalgenome.org/affiliation/50061/
- Variants whose frequency may not be reliable (e.g., variants that may reflect a sequencing artifact) should be critically evaluated and brought to the attention of the LGMD VCEP

---

### BS1 - Frequency Greater Than Expected

**Original ACMG Summary:** Allele frequency is greater than expected for disorder.

**VCEP Specification (Strong):**

Apply if the variant **Grpmax FAF** (the lower bound of the 95% confidence interval of the maximum credible genetic ancestry group allele frequency) is **>0.0009**.

| Strength | Default Points | Criteria |
|----------|---------------|----------|
| **Strong** | -4 | Grpmax FAF >0.0009 in gnomAD. |

- This value can be taken directly from gnomAD
- Do not use data for which the variant does not pass quality control filters
- See Appendix D for a list of variants defined as exceptions to the benign frequency rules
- Ongoing updates to the exception list will be available at the LGMD VCEP webpage: https://clinicalgenome.org/affiliation/50061/
- Variants whose frequency may not be reliable (e.g., variants that may reflect a sequencing artifact) should be critically evaluated and brought to the attention of the LGMD VCEP

---

### BS2 - Observed in Healthy Adult

**Original ACMG Summary:** Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

**VCEP Specification:** ***Not Applicable***

> Not applicable as LGMD is characterized by variable expressivity and late-onset LGMD is not uncommon.

---

### BS3 - Functional Studies (No Effect)

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

**VCEP Specification:** ***Not Applicable***

> Not applicable. Since muscle disease mechanisms are complex, it is not feasible at this time to exclude all pathogenic functional abnormalities through available assays.

---

### BS4 - Lack of Segregation

**Original ACMG Summary:** Lack of segregation in affected members of a family. Caveat: The presence of phenocopies for common phenotypes (i.e., cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.

**VCEP Specifications:**

| Strength | Default Points | Criteria |
|----------|---------------|----------|
| **Strong** | -4 | Use as is. One affected individual (genotype-, phenotype+) is sufficient for BS4. Do not apply for genotype+, phenotype- individuals, as LGMD is characterized by variable expressivity and late onset is not uncommon. |

---

### BP1-BP7 - Benign Supporting

| Criterion | Status | Default Points | Specification |
|-----------|--------|---------------|---------------|
| **BP1** | Not Applicable | — | Not applicable as missense variants are also known to cause disease. |
| **BP2** | Applicable (Supporting) | -1 | Use when variant is found *in cis* with a variant classified as pathogenic or likely pathogenic using the LGMD VCEP specifications. |
| **BP3** | Not Applicable | — | Not applicable. Repetitive regions without a known function are not well described in SGCB. |
| **BP4** | Applicable (Supporting) | -1 | **For missense variants:** use REVEL with a score **≤0.1** AND SpliceAI with a score **≤0.05**. **For variants that may affect splicing:** use SpliceAI with a score **≤0.05**. For any variant with RNA or other experimental data indicating no impact on splicing, follow SVI Working Group recommendations (Walker et al. 2023; PMID: 37352859). |
| **BP5** | Not Applicable | — | Not applicable. |
| **BP6** | Not Applicable | — | This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PMID: 29543229). |
| **BP7** | Applicable (Supporting/Strong) | -1 / -4 | See below. |

#### BP7 - Synonymous/Splicing Variants

| Strength | Default Points | Criteria |
|----------|---------------|----------|
| **Strong** | -4 | For any variant experimentally shown to have no splice impact, follow SVI Working Group recommendations (Walker et al. 2023; PMID: 37352859). Apply BP7_Strong if a splicing assay shows no effect on splicing and a protein impact can be ruled out. |
| **Supporting** | -1 | For splice predictions, use SpliceAI with a score **≤0.05**. BP7 may be co-applied with BP4 for synonymous, UTR, and intronic variants located outside the splice donor/acceptor regions designated in Walker et al. 2023 (+6/-3 for donor; +1/-20 for acceptor). |

---

## Rules for Combining Criteria

This VCEP uses a **Bayesian point-based classification framework** (Tavtigian et al., 2020).

### Point-Based Variant Classification Categories

| Category | Point Range |
|----------|-------------|
| **Pathogenic** | ≥10 |
| **Likely Pathogenic** | 6 to 9 |
| **Uncertain Significance** | 0 to 5 |
| **Likely Benign** | -6 to -1 |
| **Benign** | ≤-7 |

> **Additional Note:** A Benign classification can also be assigned when BA1 applies.

### Default Bayesian Point Values

| Strength Level | Pathogenic Points | Benign Points |
|---------------|-------------------|---------------|
| Very Strong | 8 | — |
| Strong | 4 | -4 |
| Moderate | 2 | — |
| Supporting | 1 | -1 |
| Stand Alone | — | BA1 (Benign) |

### Summary of Applicable Criteria and Point Values for SGCB

| Criterion | Applicable Strengths | Points |
|-----------|---------------------|--------|
| PVS1 | Very Strong / Strong / Moderate / Supporting | 8 / 4 / 2 / 1 |
| PS1 | Strong / Moderate / Supporting | 4 / 2 / 1 |
| PS2 | Supporting only | 1 |
| PS3 | Strong / Moderate / Supporting | 4 / 2 / 1 |
| PS4 | Strong | 4 |
| PM1 | Not Applicable | — |
| PM2 | Supporting only | 1 |
| PM3 | Very Strong / Strong / Moderate / Supporting | 8 / 4 / 2 / 1 |
| PM4 | Moderate | 2 |
| PM5 | Strong / Moderate / Supporting | 4 / 2 / 1 |
| PM6 | Not Applicable (see PS2) | — |
| PP1 | Strong / Moderate / Supporting | 4 / 2 / 1 |
| PP2 | Not Applicable | — |
| PP3 | Supporting | 1 |
| PP4 | Strong / Moderate / Supporting | 4 / 2 / 1 |
| PP5 | Not Applicable | — |
| BA1 | Stand Alone | Benign |
| BS1 | Strong | -4 |
| BS2 | Not Applicable | — |
| BS3 | Not Applicable | — |
| BS4 | Strong | -4 |
| BP1 | Not Applicable | — |
| BP2 | Supporting | -1 |
| BP3 | Not Applicable | — |
| BP4 | Supporting | -1 |
| BP5 | Not Applicable | — |
| BP6 | Not Applicable | — |
| BP7 | Strong / Supporting | -4 / -1 |

### Special Combination Rules

- **PP1 + PP4 cap:** When applied together, PP1 and PP4 cannot exceed 5 Bayesian points (Supporting + Strong or Moderate + Moderate). If PP1_Moderate is applied and the criteria for PP4_Strong are also met, a downgraded PP4_Moderate can be applied.

---

## Appendices

### Appendix A: PVS1 Decision Tree for SGCB

The PVS1 decision tree covers the following variant types on transcript NM_000232.5:

```
VARIANT TYPE                    DECISION PATH                                        STRENGTH
─────────────────────────────────────────────────────────────────────────────────────────────────
Nonsense/Frameshift
  ├─ Predicted NMD (codons 35-233)                                               → PVS1
  ├─ Premature truncation codons 1-34 (PMID: 27618451)                           → PVS1_Moderate
  └─ Not predicted NMD
      └─ Exon present in NM_000232.5
          ├─ Critical region (none specified)                                     → PVS1_Strong
          └─ Role unknown
              ├─ LoF frequent / exon absent                                      → N/A
              └─ LoF not frequent, exon present
                  ├─ Removes >10% protein                                        → PVS1_Strong
                  └─ Removes <10% protein                                        → PVS1_Moderate

Canonical ±1,2 Splice Sites (use SpliceAI for predicted effect)
  ├─ Exon skipping/cryptic → disrupts frame + NMD                                → PVS1
  ├─ Exon skipping/cryptic → preserves frame
  │   (In-frame exons: 1, 2, 3, 4, 5, 6)
  │   └─ [Same logic as nonsense/frameshift for protein impact]
  └─ Disrupts frame, NOT NMD
      └─ [Same logic as nonsense/frameshift for protein impact]

Deletion (single exon to full gene)
  ├─ Disrupts frame + NMD                                                        → PVS1
  ├─ Full gene deletion                                                          → PVS1
  ├─ Preserves frame → [same logic for protein impact]
  └─ Disrupts frame, NOT NMD → [same logic for protein impact]

Duplication (≥1 exon, contained within gene)
  ├─ Proven in tandem + frame disrupted + NMD                                    → PVS1
  ├─ Proven in tandem, unknown frame impact                                      → N/A
  ├─ Presumed in tandem + frame disrupted + NMD                                  → PVS1_Strong
  └─ Proven not in tandem                                                        → N/A

Initiation Codon
  ├─ Alternative start codon in other transcript                                 → PVS1_Supporting
  └─ No alternative start codon
      ├─ ≥1 P variant upstream of closest in-frame start                         → PVS1_Moderate
      └─ No P variants upstream                                                  → N/A
```

---

### Appendix B: Experimental Splice Data Decision Tree

For variants with RNA/splicing data, follow the SVI Working Group's recommendations (Walker et al. 2023; PMID: 37352859):

```
RNA/Splicing Data Available
│
├─ Silent / Intronic variant
│   ├─ No variant-specific observed impact → BP7_S (RNA) applied
│   │   └─ Consider splicing predictive data
│   │       ├─ Can protein impact be ruled out? → YES → BP7_S (RNA) + prediction (PP3/BP4)
│   │       └─ NO → BP7_S (RNA) + prediction (PP3/BP4)
│   │           Note: Document as "BP7_S (RNA) Not Met" to indicate data was present and reviewed
│   └─ Variant-specific impact observed (compared to controls)
│       └─ Follow PVS1 flowchart for OBSERVED RNA impact for your gene
│           └─ PVS1_Strength assigned to at least 1 transcript
│               └─ Proportion of alternative transcripts produced by variant allele:
│                   ├─ Complete → Keep strength level
│                   ├─ Near complete → Reduce strength by 1 level
│                   └─ Incomplete → Do not apply codes
│
├─ Other variants
│   ├─ No variant-specific observed impact
│   │   └─ Assess pathogenicity using protein pathway
│   └─ Variant-specific impact observed
│       └─ Follow PVS1 flowchart for OBSERVED RNA impact
│           └─ [Same proportion logic as above]
│
└─ If background rate considered at low-moderate levels suggestive of being biased,
    consider reducing PVS1 (RNA) codes by an additional level
```

**Combined analysis:**
- Determine PVS1 (RNA) weight from combined analysis (PP3/BP4 not applicable)
- If PVS1 (RNA) or BP7_S (RNA) not applicable → reconsider PVS1 decision tree as appropriate

---

### Appendix C: PS1 Splicing Table

**Table 2: PS1 code weights for variants with same predicted splicing event as a known (likely) pathogenic variant**

| Variant Under Assessment (VUA) | Baseline Computational/Predictive Code Applicable to VUA | Position of Comparison Variant Relative to VUA | PS1 Code with P Comparison Variant | PS1 Code with LP Comparison Variant |
|-------------------------------|--------------------------------------------------------|-----------------------------------------------|-----------------------------------|-------------------------------------|
| Located outside splice donor/acceptor ±1,2 dinucleotide positions | PP3 | Same nucleotide | PS1 | PS1_Moderate |
| Located outside splice donor/acceptor ±1,2 dinucleotide positions | PP3 | Within same splice donor/acceptor motif (including at ±1,2 positions) | PS1_Moderate | PS1_Supporting |
| Located at splice donor/acceptor ±1,2 dinucleotide positions | PVS1 | Within same splice donor/acceptor ±1,2 dinucleotide | PS1_Supporting | N/A |
| Located at splice donor/acceptor ±1,2 dinucleotide positions | PVS1 | Within same splice donor/acceptor region, but outside ±1,2 dinucleotide* | PS1_Supporting | PS1_Supporting |
| Located at splice donor/acceptor ±1,2 dinucleotide positions | PVS1_Strong, PVS1_Moderate, or PVS1_Supporting | Within same splice donor/acceptor ±1,2 dinucleotide | PS1 | N/A |
| Located at splice donor/acceptor ±1,2 dinucleotide positions | PVS1_Strong, PVS1_Moderate, or PVS1_Supporting | Within same splice donor/acceptor motif, but outside ±1,2 dinucleotide* | PS1_Moderate | PS1_Supporting |

**Prerequisites:**
- The predicted event of the VUA must precisely match the predicted event of the comparison (likely) pathogenic variant (e.g., both predicted to lead to exon skipping, or both to lead to enhanced use of a cryptic splice motif)
- The strength of the prediction for the VUA must be of similar or higher strength than the strength of the prediction for the comparison [likely] pathogenic variant
- For an exonic variant, predicted or proven functional effect of missense substitution(s) encoded by the VUA and (likely) pathogenic variant should also be considered before application of this code
- Dinucleotide positions refer to donor and acceptor dinucleotides in reference transcript(s) used for curation
- Designated donor and acceptor motif ranges should be based on position weight matrices for intron category (see methods)
- For GT-AG introns: donor motif = last 3 bases of exon and 6 nucleotides of intronic sequence adjacent to the exon; acceptor motif = first base of the exon and 20 nucleotides upstream from the exon boundary. Consider other motif ranges for non-GT-AG introns.

*\* If relevant, splicing assay data for a pathogenic variant outside a ±1,2 dinucleotide position may be used to update a PVS1 decision tree and hence the applicable PVS1 code for a ±1,2 dinucleotide variant.*

---

### Appendix D: Benign Frequency Exceptions

The following variants are defined as exceptions to the benign frequency rules (BA1/BS1). These variants exceed the population frequency thresholds but are known pathogenic variants:

| Variant | Status | Comment |
|---------|--------|---------|
| NM_003494.3(DYSF):c.2643+1G>A | BS1 exception | Common pathogenic variant |
| NM_213599.3(ANO5):c.191dup (p.Asn64LysfsTer15) | BS1 exception | Common pathogenic variant |
| NM_000070.3(CAPN3):c.1746-20C>G | BS1 exception | Proposed hypomorph |
| NM_000070.3(CAPN3):c.2120A>G (p.Asp707Gly) | BS1 exception | Likely founder in East Asian population |

> **Note:** These exceptions apply across the LGMD VCEP specifications. No SGCB-specific exceptions are currently listed. Ongoing updates to this list will be available at the LGMD VCEP webpage: https://clinicalgenome.org/affiliation/50061/

---

### Appendix E: Population Frequency Thresholds Summary

| Criterion | Metric | Threshold | Strength |
|-----------|--------|-----------|----------|
| BA1 | Grpmax FAF | >0.002 | Stand Alone (Benign) |
| BS1 | Grpmax FAF | >0.0009 | Strong (Benign) |
| PM2 | Grpmax AF / upper bound 95% CI | <0.00009 | Supporting (Pathogenic) |

**Grpmax FAF** = Lower bound of the 95% confidence interval of the maximum credible genetic ancestry group allele frequency (taken directly from gnomAD).

**Grpmax AF/95% CI** (for PM2) = Use Grpmax variant allele frequency if ≤2 alleles; use upper bound of 95% CI if ≥3 alleles.

**Excluded populations for Grpmax:** Amish, Ashkenazi Jewish, European Finnish, Remaining Individuals, and genomes-only Middle Eastern group.

---

### Appendix F: Reference PMIDs

| PMID | Reference | Relevance |
|------|-----------|-----------|
| 37352859 | Walker et al. 2023 | SVI Working Group recommendations for RNA/splicing data interpretation |
| 31892348 | Brnich et al. 2020 | SVI recommendations for PS3/BS3 functional evidence evaluation |
| 37317968 | Li et al. 2023 | Sarcoglycan complex cell surface localization assay (PS3_Moderate for SGCB) |
| 22095924 | Soheili et al. 2012 | Membrane localization assay (PS3_Supporting for SGCB) |
| 29543229 | Biesecker et al. 2018 | ClinGen SVI recommendation against use of PP5/BP6 |
| 27618451 | — | Reference for premature truncation within first 100 bp (PVS1 flowchart) |

---

## Version History

| Version | Date | Notes |
|---------|------|-------|
| 2.0.0 | 7/9/2025 | Bayesian adaptation; correction to in-frame exons in PVS1 flowchart; clarification on experimental RNA/splice data (PVS1, PP3, BP4, BP7); clarification on gnomAD population frequency data (PM2, BA1, BS1); reduced weighting of de novo observation (PS2, PM6); updated PM5 guidance |

---

*This document was compiled from ClinGen VCEP specifications and ClinGen SVI recommendations. For the most current version, please refer to the ClinGen website.*
