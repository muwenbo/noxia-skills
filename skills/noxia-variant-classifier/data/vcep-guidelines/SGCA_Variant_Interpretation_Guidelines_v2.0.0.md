# ClinGen Limb Girdle Muscular Dystrophy Expert Panel Variant Interpretation Guidelines for SGCA

**Version:** 2.0.0
**Released:** 7/9/2025
**Affiliation:** Limb Girdle Muscular Dystrophy VCEP
**Based on:** Tavtigian et al., 2020 - Bayesian adaptation of Richards et al., 2015

**Release Notes (v2.0.0):**
- Specification type defined as Bayesian adaptation
- Clarification on use of experimental RNA/splice data: PVS1, PP3, BP4, BP7
- Clarification on use of gnomAD population frequency data (no change to thresholds): PM2, BA1, BS1
- Reduced weighting of de novo observation: PS2, PM6
- Updated guidance on evaluating missense variants at the same position: PM5

---

## Gene Information

| Attribute | Value |
|-----------|-------|
| **Gene** | SGCA (HGNC:10805) |
| **HGNC Name** | sarcoglycan alpha |
| **Transcript** | NM_000023.4 |
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

Caveats:
- Beware of genes where LOF is not a known disease mechanism (e.g., GFAP, MYH7).
- Use caution interpreting LOF variants at the extreme 3' end of a gene.
- Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact.
- Use caution in the presence of multiple transcripts.

**VCEP Specifications:**

Please see the SGCA PVS1 flowchart (Appendix A). In addition, for any variant with RNA/splicing data, follow the SVI Working Group's recommendations (Walker et al. 2023; PMID: 37352859). See supplementary file "experimental splice data" (Appendix D).

#### Strength Levels

| Strength | Default Points | Criteria |
|----------|---------------|----------|
| **Very Strong** | 8 | Follow the SGCA PVS1 decision tree. Applies to nonsense/frameshift variants predicted to undergo NMD (premature truncation in codons 35-327), splice site variants where exon skipping/cryptic splice site disrupts reading frame and NMD is predicted, reading-frame-disrupting deletions predicted to undergo NMD, and full gene deletions. |
| **Strong** | 4 | Follow the SGCA PVS1 decision tree. Applies to: nonsense/frameshift not predicted to undergo NMD where exon is present in biologically relevant transcript and the role of the region in protein function is unknown (if variant removes >10% of protein); splice variants preserving reading frame where the truncated/altered region is critical or variant removes >10% of protein; reading-frame-disrupting deletions not predicted to undergo NMD (>10% protein removed); proven or presumed in-tandem duplications disrupting reading frame with NMD. |
| **Moderate** | 2 | Follow the SGCA PVS1 decision tree. Applies to: nonsense/frameshift not predicted to undergo NMD where variant removes <10% of protein; splice variants where altered region role is unknown and variant removes <10% of protein; initiation codon variants with no known alternative start codon and >=1 pathogenic variant upstream of closest potential in-frame start codon. |
| **Supporting** | 1 | Follow the SGCA PVS1 decision tree. Applies to initiation codon variants where a different functional transcript uses an alternative start codon. |

**Key gene-specific notes for PVS1 decision tree:**
- NMD boundary: premature truncation in codons 35-327 is predicted to undergo NMD; premature truncation within the first 100 bp (codons 1-34) warrants PVS1_Moderate (PMID: 27618451)
- Biologically relevant transcript: NM_000023.4
- In-frame exons for which exon skipping is not expected to result in NMD: exons 2 and 8
- No truncated/altered regions critical to protein function have been specified at this time

---

### PS1 - Same Amino Acid Change

**Original ACMG Summary:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change. Example: Val->Leu caused by either G>C or G>T in the same codon.

Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:**

#### For missense variants (amino acid change is the expected mechanism):

| Strength | Default Points | Criteria |
|----------|---------------|----------|
| **Strong** | 4 | Apply for 1 pathogenic or 2 likely pathogenic variants resulting in the same amino acid change. The LP/P variant(s) must have been classified using LGMD VCEP specifications. Potential splice effects must be excluded for the missense variant under curation and the variant(s) resulting in the same amino acid change (SpliceAI score ≤0.10 or experimental evidence of normal splicing). PS1 can potentially be applied to multiple nucleotide changes at the same residue as long as the variant classification that determines the strength level does not depend on PS1 application. |
| **Moderate** | 2 | Apply for 1 likely pathogenic variant resulting in the same amino acid change. The LP variant must have been classified using LGMD VCEP specifications. Potential splice effects must be excluded (SpliceAI score ≤0.10 or experimental evidence of normal splicing). |

**Important caveats:**
- For missense variants encoded by the first or last 3 nucleotides of an exon, PS1 should be considered only in the context of altered splicing (see below), unless a splice effect has been experimentally ruled out for the variant under curation and the variant(s) resulting in the same amino acid change.

#### For splice variants (nucleotide change is the expected mechanism):

| Strength | Default Points | Criteria |
|----------|---------------|----------|
| **Supporting** | 1 | Follow SVI Working Group recommendations (Walker et al. 2023; PMID: 37352859), as outlined in supplementary file "PS1 splicing" (Appendix C). |

See Appendix C (PS1 Splicing Table) for the complete PS1 code weights for variants with same predicted splicing event as a known (likely) pathogenic variant.

---

### PS2 - De Novo (Confirmed)

**Original ACMG Summary:** De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.

Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.

**VCEP Specifications:**

| Strength | Default Points | Criteria |
|----------|---------------|----------|
| **Supporting** | 1 | Apply for confirmed *de novo* occurrence in a proband meeting the criteria for PP4 (Supporting). Maternity and paternity should be confirmed by trio WES/WGS or other testing. |

> **Note:** PS2 is available only at Supporting strength for SGCA. Higher strength levels are not applicable due to the autosomal recessive inheritance pattern and genetic heterogeneity of LGMD.

---

### PS3 - Functional Studies

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.

Note: Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.

**VCEP Specifications:**

| Strength | Default Points | Criteria |
|----------|---------------|----------|
| **Strong** | 4 | Variant-specific animal models assessed on a case-by-case basis. Apply at Strong for a model (regardless of species) meeting **all** of: (1) signs of myopathy or dystrophy in skeletal muscle, (2) effect on gene/protein function demonstrated (e.g., decreased protein expression, impaired membrane localization), (3) behavioral signs of muscle weakness, (4) progression over time. |
| **Moderate** | 2 | Variant-specific animal models meeting: (1) signs of myopathy or dystrophy in skeletal muscle, AND (2) effect on gene/protein function demonstrated. **OR** Sarcoglycan complex membrane localization assays clinically validated with ≥11 control variants meeting Brnich et al. 2020 (PMID: 31892348) criteria for the number of pathogenic and benign control variants. |
| **Supporting** | 1 | Variant expressed in heterologous cell lines/model organisms showing absent membrane localization of the sarcoglycan protein complex with fewer than 11 control variants used, in accordance with Brnich et al. 2020 (PMID: 31892348). |

**Important notes:**
- For any variant type, experimental evidence for altered splicing should be scored under PVS1 in accordance with the decision tree for RNA splicing assay results outlined in Walker et al. 2023 (PMID: 37352859).
- Apply PS3 only once, for the piece of evidence that meets the highest possible strength level.

#### Approved Assay Instances

| Attribute | Membrane Localization Assay |
|-----------|---------------------------|
| **PMID** | 22095924 |
| **Author/Year** | Soheili, 2012 |
| **Assay** | Membrane localization of sarcoglycan complex |
| **Material** | Vectors expressing the SGCA variant of interest transfected into HER-911 cells expressing the three other sarcoglycans |
| **Readout** | Qualitative - membrane localization assessed via confocal immunofluorescence analysis of nonpermeabilized cells |
| **Positive Control** | Wild-type |
| **Negative Control** | Expression of alpha-sarcoglycan alone |
| **Validation Controls (P/LP)** | 12 (3 validated by VCEP) |
| **Validation Controls (B/LB)** | 0 |
| **Threshold (Normal)** | Membrane localized |
| **Threshold (Abnormal)** | Absent at membrane |
| **Approved** | Yes |
| **Proposed Strength** | PS3_Supporting; BS3 not applied |

---

### PS4 - Prevalence in Affected

**Original ACMG Summary:** The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.

Note 1: Relative risk (RR) or odds ratio (OR), as obtained from case-control studies, is >5.0 and the confidence interval around the estimate of RR or OR does not include 1.0.

Note 2: In instances of very rare variants where case-control studies may not reach statistical significance, the prior observation of the variant in multiple unrelated patients with the same phenotype, and its absence in controls, may be used as moderate level of evidence.

**VCEP Specifications:**

| Strength | Default Points | Criteria |
|----------|---------------|----------|
| **Strong** | 4 | Use without disease-specific modification if case-control studies are available. |

> **Note:** While case-control studies could potentially be considered for a few pathogenic variants with high minor allele frequency, the VCEP is unaware of any such studies being conducted for *SGCA*. Any case-control study would require careful selection of an appropriate control population given the potential for late onset and mild disease.

---

### PM1 - Mutational Hot Spot

**Original ACMG Summary:** Located in a mutational hot spot and/or critical and well-established functional domain (e.g., active site of an enzyme) without benign variation.

**VCEP Specifications:** ***Not Applicable***

Not applicable at this time.

---

### PM2 - Absent from Controls

**Original ACMG Summary:** Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

Caveat: Population data for indels may be poorly called by next generation sequencing.

**VCEP Specification (Supporting only):**

| Strength | Default Points | Criteria |
|----------|---------------|----------|
| **Supporting** | 1 | Apply if the Grpmax variant allele frequency / upper bound of the 95% CI of the Grpmax variant allele frequency in gnomAD is **<0.00009**. |

**Detailed rules:**
- If only 1 or 2 variant alleles are present in the Grpmax population, use the Grpmax variant allele frequency
- If at least 3 variant alleles are present in the Grpmax population, use the upper bound of the 95% confidence interval (95% CI) of the Grpmax variant allele frequency
- **Grpmax** refers to the gnomAD subpopulation with the highest variant allele frequency
- **Exclude** the following groups from Grpmax: Amish, Ashkenazi Jewish, European Finnish, and Remaining Individuals groups, as well as the genomes-only data for the Middle Eastern group
- The upper bound of the 95% CI must be calculated using variant allele numbers and counts from gnomAD. Confidence interval tools such as Confit-de-MAF (https://www.genecalculators.net/confit-de-maf.html) can be used
- Use the gnomAD version with the largest allele number
- Do not use data for which the variant does not pass quality control filters
- For larger deletions or duplications (e.g., single- or multi-exon events), also confirm the variant is not common in gnomAD SVs, gnomAD CNVs, or the Database of Genomic Variants (DGV) (https://dgv.tcag.ca/dgv/app/home)

---

### PM3 - In Trans with Pathogenic

**Original ACMG Summary:** For recessive disorders, detected in trans with a pathogenic variant. Note: This requires testing of parents (or offspring) to determine phase.

**VCEP Specifications:** Use the SVI Working Group's recommended point system to determine PM3 strength.

#### PM3 Point System (Per Proband)

| Classification/Zygosity of Other Variant | Confirmed in Trans^1 | Phase Unknown^2 |
|------------------------------------------|----------------------|-----------------|
| Pathogenic or Likely pathogenic variant^3 | 1.0 | 0.5 (P) / 0.25 (LP) |
| Homozygous occurrence (max 1.0 pt; downgrade to 0.25 pts for consanguinity) | 0.5 | N/A |
| Uncertain significance variant^4 (max 0.5 pts) | 0.25 | 0 |

#### PM3 Evidence Strength Thresholds

| Total Points | Strength Level | Default Points |
|--------------|----------------|---------------|
| ≥0.5 to <1.0 | PM3_Supporting | 1 |
| ≥1.0 to <2.0 | PM3 (Moderate) | 2 |
| ≥2.0 to <4.0 | PM3_Strong | 4 |
| ≥4.0 | PM3_VeryStrong | 8 |

**Footnotes:**
1. Author assertions on phase, including based on allele-specific transcript expression, are acceptable.
2. For variants identified in unknown phase, PM3 points should **not** be awarded under the following circumstances:
   - The same variants were ever confirmed in *cis* (e.g., in a different patient in the literature)
   - gnomAD co-occurrence data (https://gnomad.broadinstitute.org/variant-cooccurrence) predict the variants may be part of the same haplotype in at least one genetic ancestry group
   - More than 2 variants are reported in the patient, none of which can be classified as likely benign or benign
3. Any variant awarded points as likely pathogenic or pathogenic must have been classified using the LGMD VCEP specifications.
4. For any variant awarded points as VUS, benign frequency codes (BA1, BS1) cannot be applicable.

**PM3 Co-Application Note:** It is possible to award PM3 points to both variants identified in an individual as long as the evidence related to their co-observation in that individual does not contribute to the variant classification that determines the number of points applied. This excludes all evidence derived from the co-observation, including inter-dependent PM3 points (pathogenicity of variant in trans/unknown phase), PP1 (genotype-phenotype co-segregation), and PP4 (phenotype specificity). See Appendix E for detailed co-application examples.

---

### PM4 - Protein Length Changes

**Original ACMG Summary:** Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

**VCEP Specifications:**

| Strength | Default Points | Criteria |
|----------|---------------|----------|
| **Moderate** | 2 | Use as is, regardless of the length of the in-frame insertion or deletion. |

---

### PM5 - Novel Missense at Same Residue

**Original ACMG Summary:** Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before. Example: Arg156His is pathogenic; now you observe Arg156Cys.

Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:**

Apply only for missense variants for which the amino acid change is the expected mechanism of disease. For the missense variant under curation and the variant(s) resulting in a different amino acid change, exclude likely splice effects (SpliceAI score <0.5 or experimental evidence of normal splicing). The REVEL score for the missense variant under curation should be >0.7. Missense changes at the same residue must be classified according to LGMD VCEP specifications, and no benign missense variation should be present at the residue. Do not apply for missense variants encoded by the first or last 3 nucleotides of an exon unless a splice effect has been ruled out for the variant under curation and the variant(s) resulting in the same amino acid change.

| Strength | Default Points | Criteria |
|----------|---------------|----------|
| **Strong** | 4 | 2 pathogenic or 3 likely pathogenic variants resulting in different amino acid changes at the same residue as the variant under curation. |
| **Moderate** | 2 | 1 pathogenic or 2 likely pathogenic variants resulting in different amino acid changes at the same residue as the variant under curation. |
| **Supporting** | 1 | 1 likely pathogenic variant resulting in a different amino acid change at the same residue as the variant under curation. |

> **Note:** PM5 can potentially be applied to multiple amino acid changes at the same residue as long as the variant classification that determines the strength level does not depend on PM5 application.

---

### PM6 - De Novo (Assumed)

**Original ACMG Summary:** Assumed de novo, but without confirmation of paternity and maternity.

**VCEP Specifications:** ***Not Applicable***

Not applicable. See PS2.

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

> **Important:** When applied together, PP1 and PP4 cannot exceed 5 Bayesian pts (Supporting + Strong or Moderate + Moderate).

---

### PP2 - Missense in Constrained Gene

**Original ACMG Summary:** Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.

**VCEP Specifications:** ***Not Applicable***

Not applicable. SGCA is not constrained for missense variation (Z-score <3).

---

### PP3 - Computational Evidence

**Original ACMG Summary:** Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).

Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.

**VCEP Specifications:**

| Strength | Default Points | Criteria |
|----------|---------------|----------|
| **Supporting** | 1 | For missense variants: REVEL score **≥0.7**. For variants that may affect splicing: SpliceAI score **≥0.5**. |

> **Note:** For any variant with RNA or other experimental data indicating an impact on splicing, follow the SVI Working Group's recommendations (Walker et al. 2023; PMID: 37352859). See supplementary file "experimental splice data" (Appendix D).

---

### PP4 - Phenotype Specificity

**Original ACMG Summary:** Patient's phenotype or family history is highly specific for a disease with a single genetic etiology.

**VCEP Specifications:**

Use the PP4 table below to determine the appropriate PP4 strength level. Apply PP4 only once, for a patient meeting the highest possible strength level.

| Strength | Default Points | Criteria |
|----------|---------------|----------|
| **Strong** | 4 | All of: (1) progressive limb-girdle pattern of muscle weakness observed over ≥6 months OR clinical suspicion of LGMD, AND (2) 2 presumed diagnostic variants in SGCA (1 of which is the variant under curation), AND (3) reduced expression or membrane localization of full-length protein in skeletal muscle (e.g., WB or IHC; <~30% normal). |
| **Moderate** | 2 | See note below regarding PP1+PP4 cap. If PP1_Moderate is applied and the criteria for PP4_Strong are also met, a downgraded PP4_Moderate can be applied. |
| **Supporting** | 1 | All of: (1) progressive limb-girdle pattern of muscle weakness observed over ≥6 months OR clinical suspicion of LGMD, AND (2) 2 presumed diagnostic variants in SGCA (1 of which is the variant under curation). |

#### PP4 Point Table

|  | | **PP4 Strength** | |
|--|--|------------------|--|
| **Category** | **Requirement** | **Supporting** | **Strong** |
| **Clinical^1** | Progressive limb-girdle pattern of muscle weakness observed over ≥6 mo OR clinical suspicion of LGMD | Required | Required |
| **Genetic testing^2** | 2 presumed diagnostic^3 variants in SGCA, 1 of which is the variant under curation | Required | Required |
| **Protein expression in patient tissue** | Reduced^4 expression or membrane localization of full-length protein in skeletal muscle (e.g., WB or IHC) | Not required | Required |

**PP4 Table Footnotes:**
1. May be accompanied by supporting EMG, MRI, muscle histology, elevated CK but not required.
2. Screening of all exons and exon/intron boundaries of SGCA required for Supporting. To apply at Strong, screening of SGCB, SGCG, and SGCD also required. Do not apply if 2 presumed diagnostic variants also identified in SGCB, SGCG, or SGCD. Screening of additional neuromuscular disease genes (e.g., through a panel) is recommended but not required.
3. If variants have not yet been curated by the LGMD VCEP, confirm they cannot be classified as LB or B (e.g., through application of BA1, BS1, and/or BP4/BP7). If phase is unknown, do not apply if the identified variants were ever confirmed in *cis* or if gnomAD co-occurrence data (https://gnomad.broadinstitute.org/variant-cooccurrence) predict the variants may be part of the same haplotype in at least one genetic ancestry group.
4. <~30% normal; may be described as "severely" / "drastically" / "strongly" reduced or as "absent", "trace", or "barely detectable".

> **Important:** When applied together, PP1 and PP4 cannot exceed 5 Bayesian pts (Supporting + Strong or Moderate + Moderate). If PP1_Moderate is applied and the criteria for PP4_Strong are also met, a downgraded PP4_Moderate can be applied.

---

### PP5 - Reputable Source

**Original ACMG Summary:** Reputable source recently reports variant as pathogenic, but the evidence is not available to the laboratory to perform an independent evaluation.

**VCEP Specifications:** ***Not Applicable***

This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PMID: 29543229).

---

## Benign Criteria

### BA1 - Allele Frequency >5%

**Original ACMG Summary:** Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

**VCEP Specification (Stand Alone):**
- Apply if the variant **Grpmax FAF** (the lower bound of the 95% confidence interval of the maximum credible genetic ancestry group allele frequency) is **>0.002**
- This value can be taken directly from gnomAD, but do not use data for which the variant does not pass quality control filters
- See supplementary file "benign frequency exceptions" (Appendix F) for a list of variants defined as exceptions to the benign frequency rules
- Ongoing updates to this list will be available at the LGMD VCEP webpage: https://clinicalgenome.org/affiliation/50061/
- Variants whose frequency may not be reliable (e.g., variants that may reflect a sequencing artifact) should be critically evaluated and brought to the attention of the LGMD VCEP

---

### BS1 - Frequency Greater Than Expected

**Original ACMG Summary:** Allele frequency is greater than expected for disorder.

**VCEP Specification (Strong):**
- Apply if the variant **Grpmax FAF** (the lower bound of the 95% confidence interval of the maximum credible genetic ancestry group allele frequency) is **>0.0009**
- This value can be taken directly from gnomAD, but do not use data for which the variant does not pass quality control filters
- See supplementary file "benign frequency exceptions" (Appendix F) for a list of variants defined as exceptions to the benign frequency rules
- Default Point Value: -4

---

### BS2 - Observed in Healthy Adult

**Original ACMG Summary:** Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

**VCEP Specifications:** ***Not Applicable***

Not applicable as LGMD is characterized by variable expressivity and late-onset LGMD is not uncommon.

---

### BS3 - Functional Studies (No Effect)

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

**VCEP Specifications:** ***Not Applicable***

Not applicable. Since muscle disease mechanisms are complex, it is not feasible at this time to exclude all pathogenic functional abnormalities through available assays.

---

### BS4 - Lack of Segregation

**Original ACMG Summary:** Lack of segregation in affected members of a family.

Caveat: The presence of phenocopies for common phenotypes (i.e., cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.

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
| **BP3** | Not Applicable | — | Not applicable. Repetitive regions without a known function are not well described in SGCA. |
| **BP4** | Applicable (Supporting) | -1 | For missense variants: REVEL score **≤0.1** AND SpliceAI score **≤0.05**. For variants that may affect splicing: SpliceAI score **≤0.05**. For any variant with RNA or other experimental data indicating no impact on splicing, follow the SVI Working Group's recommendations (Walker et al. 2023; PMID: 37352859). |
| **BP5** | Not Applicable | — | Not applicable. |
| **BP6** | Not Applicable | — | This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PMID: 29543229). |
| **BP7** | Applicable (Supporting/Strong) | -1 / -4 | **Supporting:** For splice predictions, use SpliceAI score ≤0.05. BP7 may be co-applied with BP4 for synonymous, UTR, and intronic variants located outside the splice donor/acceptor regions designated in Walker et al. 2023 (+6/-3 for donor; +1/-20 for acceptor). **Strong (-4 pts):** For any variant experimentally shown to have no splice impact, follow SVI Working Group recommendations (Walker et al. 2023; PMID: 37352859). Apply BP7_Strong if a splicing assay shows no effect on splicing and a protein impact can be ruled out. |

---

## Rules for Combining Criteria

This specification uses the **Bayesian point-based classification framework** (Tavtigian et al., 2020).

### Point-Based Variant Classification Categories

| Category | Point Range |
|----------|-------------|
| **Pathogenic** | ≥10 |
| **Likely Pathogenic** | 6 - 9 |
| **Uncertain Significance** | 0 - 5 |
| **Likely Benign** | -6 to -1 |
| **Benign** | ≤-7 |

**Additional Note:** A Benign classification can also be assigned when BA1 applies.

### Default Point Values Reference

| Strength Level | Default Points (Pathogenic) | Default Points (Benign) |
|----------------|---------------------------|------------------------|
| Very Strong | 8 | — |
| Strong | 4 | -4 |
| Moderate | 2 | — |
| Supporting | 1 | -1 |
| Stand Alone | — | BA1 (Stand Alone Benign) |

### Equivalent Traditional Criteria Combinations

#### Pathogenic Classification (≥10 points)

| Criteria Combination | Point Calculation |
|---------------------|-------------------|
| 1 Very Strong **AND** ≥1 Strong | 8 + 4 = 12 |
| 1 Very Strong **AND** ≥2 Moderate | 8 + 2 + 2 = 12 |
| 1 Very Strong **AND** 1 Moderate **AND** 1 Supporting | 8 + 2 + 1 = 11 |
| 1 Very Strong **AND** ≥2 Supporting | 8 + 1 + 1 = 10 |
| ≥2 Strong | 4 + 4 = 8 (+ additional evidence to reach 10) |
| 1 Strong **AND** ≥3 Moderate | 4 + 2 + 2 + 2 = 10 |
| 1 Strong **AND** 2 Moderate **AND** ≥2 Supporting | 4 + 2 + 2 + 1 + 1 = 10 |
| 1 Strong **AND** 1 Moderate **AND** ≥4 Supporting | 4 + 2 + 1 + 1 + 1 + 1 = 10 |

#### Likely Pathogenic Classification (6-9 points)

| Criteria Combination | Point Calculation |
|---------------------|-------------------|
| 1 Very Strong **AND** 1 Moderate | 8 + 2 = 10 (Note: reaches P) |
| 1 Strong **AND** 1 Moderate | 4 + 2 = 6 |
| 1 Strong **AND** ≥2 Supporting | 4 + 1 + 1 = 6 |
| ≥3 Moderate | 2 + 2 + 2 = 6 |
| 2 Moderate **AND** ≥2 Supporting | 2 + 2 + 1 + 1 = 6 |
| 1 Moderate **AND** ≥4 Supporting | 2 + 1 + 1 + 1 + 1 = 6 |

#### Benign Classification (≤-7 points)

| Criteria Combination |
|---------------------|
| ≥2 Strong benign criteria (e.g., BS1 + BS4 = -4 + -4 = -8) |
| 1 Stand Alone (BA1) |

#### Likely Benign Classification (-6 to -1 points)

| Criteria Combination |
|---------------------|
| 1 Strong **AND** ≥1 Supporting (e.g., BS1 + BP4 = -4 + -1 = -5) |
| ≥2 Supporting (e.g., BP4 + BP7 = -1 + -1 = -2) |

---

## Appendices

### Appendix A: PVS1 Flowchart for SGCA

The PVS1 decision tree for SGCA covers the following variant types:

#### Nonsense or Frameshift Variants
- **Predicted to undergo NMD** (premature truncation in codons 35-327): → **PVS1**
- **Premature truncation within first 100 bp** (codons 1-34; PMID: 27618451): → **PVS1_Moderate**
- **Not predicted to undergo NMD:**
  - Exon present in biologically relevant transcript (NM_000023.4):
    - Truncated/altered region is critical to protein function (none specified): → **PVS1_Strong**
    - Role of region in protein function is unknown:
      - LoF variants in this exon NOT frequent in general population AND exon present in biologically relevant transcript:
        - Variant removes >10% of protein: → **PVS1_Strong**
        - Variant removes <10% of protein: → **PVS1_Moderate**
      - LoF variants in this exon ARE frequent in general population and/or exon absent from biologically relevant transcript: → **N/A**
  - Exon absent from biologically relevant transcript (NM_000023.4): → **N/A**

#### Canonical GT-AG ±1,2 Splice Sites
- Use the SpliceAI prediction of the most likely splice effect, then determine the expected protein consequence (https://spliceailookup.broadinstitute.org)
- **Exon skipping or cryptic splice site disrupts reading frame and NMD predicted:** → **PVS1**
- **Exon skipping or cryptic splice site disrupts reading frame, NMD NOT predicted:**
  - Follow same logic as nonsense/frameshift "not predicted to undergo NMD" above
- **Exon skipping or cryptic splice site preserves reading frame** (in-frame exons: 2, 8):
  - Exon present in biologically relevant transcript:
    - Truncated/altered region critical (none specified): → **PVS1_Strong**
    - Role unknown, LoF variants not frequent, variant removes >10%: → **PVS1_Strong**
    - Role unknown, LoF variants not frequent, variant removes <10%: → **PVS1_Moderate**
  - Exon absent from biologically relevant transcript / LoF variants frequent: → **N/A**

#### Deletions (Single Exon to Full Gene)
- **Single to multi-exon deletion disrupting reading frame, NMD predicted:** → **PVS1**
- **Single to multi-exon deletion disrupting reading frame, NMD NOT predicted:** → Follow NMD-negative logic above
- **Single to multi-exon deletion preserving reading frame:** → Follow in-frame logic above
- **Full gene deletion:** → **PVS1**

#### Duplications (≥1 Exon, Completely Contained Within Gene)
- **Proven in tandem, reading frame disrupted, NMD predicted:** → **PVS1**
- **Proven in tandem, no/unknown impact on reading frame:** → **N/A**
- **Presumed in tandem, reading frame presumed disrupted, NMD predicted:** → **PVS1_Strong**
- **Proven not in tandem:** → **N/A**

#### Initiation Codon Variants
- Different functional transcript uses alternative start codon: → **PVS1_Supporting**
- No known alternative start codon in other transcripts:
  - ≥1 pathogenic variant upstream of closest potential in-frame start codon: → **PVS1_Moderate**
  - No pathogenic variant upstream: → **N/A**

---

### Appendix B: Reference PMIDs

| PMID | Reference | Context |
|------|-----------|---------|
| 37352859 | Walker et al. 2023 | SVI Working Group recommendations for RNA/splice data interpretation |
| 31892348 | Brnich et al. 2020 | Recommendations for PS3/BS3 functional evidence evaluation |
| 29543229 | Biesecker et al. 2018 | ClinGen SVI recommendation against use of PP5/BP6 |
| 27618451 | — | NMD boundary for premature truncation within first 100 bp |
| 22095924 | Soheili et al. 2012 | Sarcoglycan complex membrane localization assay |

---

### Appendix C: PS1 Splicing Table

**Table 2. PS1 code weights for variants with same predicted splicing event as a known (likely) pathogenic variant**

| Variant Under Assessment (VUA) | Baseline Computational/Predictive Code Applicable to VUA | Position of Comparison Variant Relative to VUA | PS1 Code with P Comparison Variant | PS1 Code with LP Comparison Variant |
|-------------------------------|--------------------------------------------------------|----------------------------------------------|-----------------------------------|-------------------------------------|
| Located outside splice donor/acceptor ±1,2 dinucleotide positions | PP3 | Same nucleotide | PS1 | PS1_Moderate |
| Located outside splice donor/acceptor ±1,2 dinucleotide positions | PP3 | Within same splice donor/acceptor motif (including at ±1,2 positions) | PS1_Moderate | PS1_Supporting |
| Located at splice donor/acceptor ±1,2 dinucleotide positions | PVS1 | Within same splice donor/acceptor ±1,2 dinucleotide | PS1_Supporting | N/A |
| Located at splice donor/acceptor ±1,2 dinucleotide positions | PVS1 | Within same splice donor/acceptor region, but outside ±1,2 dinucleotide^a | PS1_Supporting | PS1_Supporting |
| Located at splice donor/acceptor ±1,2 dinucleotide positions | PVS1_Strong, PVS1_Moderate, or PVS1_Supporting | Within same splice donor/acceptor ±1,2 dinucleotide | PS1 | N/A |
| Located at splice donor/acceptor ±1,2 dinucleotide positions | PVS1_Strong, PVS1_Moderate, or PVS1_Supporting | Within same splice donor/acceptor motif, but outside ±1,2 dinucleotide^a | PS1_Moderate | PS1_Supporting |

**Prerequisites for all:** The predicted event of the VUA must precisely match the predicted event of the comparison (likely) pathogenic variant (e.g., both predicted to lead to exon skipping, or both to lead to enhanced use of a cryptic splice motif, AND the strength of the prediction for the VUA must be of similar or higher strength than the strength of the prediction for the comparison [likely] pathogenic variant). For an exonic variant, predicted or proven functional effect of missense substitution(s) encoded by the VUA and (likely) pathogenic variant should also be considered before application of this code. Dinucleotide positions refer to donor and acceptor dinucleotides in reference transcript(s) used for curation. Designated donor and acceptor motif ranges should be based on position weight matrices for intron category (see methods). For GT-AG introns these are defined as follows: the donor motif, last 3 bases of the exon and 6 nucleotides of intronic sequence adjacent to the exon; acceptor motif, first base of the exon and 20 nucleotides upstream from the exon boundary. Consider other motif ranges for non-GT-AG introns.

^a If relevant, splicing assay data for a pathogenic variant outside a ±1,2 dinucleotide position may be used to update a PVS1 decision tree and hence the applicable PVS1 code for a ±1,2 dinucleotide variant.

---

### Appendix D: Experimental Splice Data Decision Flowchart

**For variants with RNA/Splicing data:**

1. **Categorization of splicing data** — need to consider multiple factors, including assay technique, RNA source, and gene-specific knowledge.

2. **If no variant-specific observed impact:**
   - **Silent / Intronic variants:** → BP7_S (RNA) applied → Consider splicing predictive data → Can the protein impact be ruled out (based on functional and/or clinical data)?
     - **YES:** → BP7_S (RNA) + prediction (PP3/BP4)
     - **NO:** → Document as "BP7_S (RNA) Not Met" to indicate that data was present and reviewed
   - **Other variants:** → Assess pathogenicity using protein pathway

3. **If variant-specific impact observed (compared to controls):**
   - Follow PVS1 flowchart for OBSERVED RNA impact for your gene
   - PVS1_Strength assigned to at least 1 transcript
   - **Proportion of alternative transcript(s) (inferred to be) produced by variant allele:**
     - **Complete:** → Keep strength level
     - **Near complete:** → Reduce strength by 1 level (if background rate is considered to be at low/moderate levels suggestive of being tolerated, consider reducing PVS1 (RNA) codes by an additional level)
     - **Incomplete:** → Do not apply codes
   - Then → Determine PVS1 (RNA) weight from combined analysis (PP3/BP4 not applicable)
   - If PVS1 (RNA) or BP7_S (RNA) not applicable → reconsider PVS1 decision tree as appropriate

---

### Appendix E: PM3 Co-Application Examples

#### Example 1: PM3 can be awarded to both variants in a pair without circularity

Variants A and B are observed in trans in patient X, who meets the criteria for PP4. Variant A has not been observed in any other patients. Variant B has also been observed in patient Y, where it was confirmed in trans with a pathogenic variant (variant C, 1.0 PM3 pt) in an individual meeting the criteria for PP4_Moderate.

- **Variant A** is classified as LP independent of the observation in patient X (e.g., PVS1 + PM2_Supporting).
- **Variant B** is also classified as LP independent of the observation in patient X (e.g., PS3_Moderate + PP3 + PM2_Supporting + PP4_Moderate (for patient Y) + PM3 (for variant C in patient Y)).

In the curation of **variant B**, 1.0 PM3 pt can be awarded for the observation in patient X, since variant B was confirmed in trans with an LP variant (variant A). With an additional 1.0 pt from patient X, PM3 can be upgraded to PM3_Strong, resulting in a final classification of **P** for variant B.

In the curation of **variant A**, 1.0 PM3 pt can be awarded for the observation in patient X as well, since variant A was also confirmed in trans with an LP variant (variant B). With 1.0 pt, PM3 can be applied, resulting in a final classification of **P** for variant A (PVS1 + PM2_Supporting + PM3 (patient X) + PP4 (patient X)).

> *While the final classification of variants A and B is P, the classification that would be reached without counting the evidence from their co-observation in patient X is used when awarding PM3 points for the observation in patient X. This avoids circularity and double counting of evidence.*

#### Example 2: PM3 cannot be awarded to both variants in a pair without circularity

Variants A and B are observed in trans in patient X, who meets the criteria for PP4. Variant A has not been observed in any other patients. Variant B has also been observed in patient Y, where it was observed in unknown phase with a VUS variant (variant C, 0 PM3 pts) in an individual meeting the criteria for PP4.

- **Variant A** is classified as LP independent of patient X (PVS1 + PM2_Supporting).
- **Variant B** is classified as VUS independent of patient X (PS3_Moderate + PP3 + PM2_Supporting + PP4 (for patient Y)).

In the curation of **variant B**, PM3 can be awarded for the observation in patient X (1.0 PM3 pt for being confirmed in trans with LP variant A). With PM3, variant B can be classified as **LP**.

In the curation of **variant A**, PM3 **cannot** be awarded for the observation in patient X, since variant B was classified as VUS independent of the observation in patient X, and the 0.25 PM3 pts awarded for being confirmed in trans with a VUS are not sufficient for PM3 to be applied. However, PP4 can be applied, resulting in a final classification of **P** for variant A (PVS1 + PM2_Supporting + PP4 (patient X)).

---

### Appendix F: Benign Frequency Exceptions

The following variants are defined as exceptions to the benign frequency rules (BA1, BS1). These are variants that may exceed population frequency thresholds but are known or suspected pathogenic variants.

| Variant | Status | Comment |
|---------|--------|---------|
| NM_003494.3(DYSF):c.2643+1G>A | BS1 exception | Common pathogenic variant |
| NM_213599.3(ANO5):c.191dup (p.Asn64LysfsTer15) | BS1 exception | Common pathogenic variant |
| NM_000070.3(CAPN3):c.1746-20C>G | BS1 exception | Proposed hypomorph |
| NM_000070.3(CAPN3):c.2120A>G (p.Asp707Gly) | BS1 exception | Likely founder in East Asian population |

> **Note:** No SGCA-specific exceptions are currently defined. The above exceptions apply to other LGMD genes covered by the same VCEP. Ongoing updates to this list will be available at the LGMD VCEP webpage: https://clinicalgenome.org/affiliation/50061/

---

### Appendix G: Population Frequency Thresholds Summary

| Criterion | Metric | Threshold | Strength |
|-----------|--------|-----------|----------|
| BA1 | Grpmax FAF | >0.002 | Stand Alone (Benign) |
| BS1 | Grpmax FAF | >0.0009 | Strong (Benign) |
| PM2 | Grpmax VAF / upper 95% CI | <0.00009 | Supporting (Pathogenic) |

**Definitions:**
- **Grpmax FAF:** The lower bound of the 95% confidence interval of the maximum credible genetic ancestry group allele frequency (taken directly from gnomAD)
- **Grpmax VAF:** The variant allele frequency of the gnomAD subpopulation with the highest allele frequency
- **Excluded populations for Grpmax:** Amish, Ashkenazi Jewish, European Finnish, Remaining Individuals, and genomes-only Middle Eastern group

---

### Appendix H: Criteria Applicability Summary

| Criterion | Status | Max Strength | Default Points |
|-----------|--------|-------------|---------------|
| PVS1 | Applicable | Very Strong | 8 |
| PS1 | Applicable | Strong | 4 |
| PS2 | Applicable (modified) | Supporting | 1 |
| PS3 | Applicable | Strong | 4 |
| PS4 | Applicable | Strong | 4 |
| PM1 | **Not Applicable** | — | — |
| PM2 | Applicable (Supporting only) | Supporting | 1 |
| PM3 | Applicable | Very Strong | 8 |
| PM4 | Applicable | Moderate | 2 |
| PM5 | Applicable | Strong | 4 |
| PM6 | **Not Applicable** | — | — |
| PP1 | Applicable | Strong | 4 |
| PP2 | **Not Applicable** | — | — |
| PP3 | Applicable | Supporting | 1 |
| PP4 | Applicable | Strong | 4 |
| PP5 | **Not Applicable** | — | — |
| BA1 | Applicable | Stand Alone | N/A |
| BS1 | Applicable | Strong | -4 |
| BS2 | **Not Applicable** | — | — |
| BS3 | **Not Applicable** | — | — |
| BS4 | Applicable | Strong | -4 |
| BP1 | **Not Applicable** | — | — |
| BP2 | Applicable | Supporting | -1 |
| BP3 | **Not Applicable** | — | — |
| BP4 | Applicable | Supporting | -1 |
| BP5 | **Not Applicable** | — | — |
| BP6 | **Not Applicable** | — | — |
| BP7 | Applicable | Strong | -4 / -1 |

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 2.0.0 | 7/9/2025 | Specification type defined as Bayesian adaptation; clarification on experimental RNA/splice data (PVS1, PP3, BP4, BP7); clarification on gnomAD population frequency data (PM2, BA1, BS1); reduced weighting of de novo observation (PS2, PM6); updated guidance on evaluating missense variants at same position (PM5). |

---

*This document was compiled from ClinGen VCEP specifications and ClinGen SVI recommendations. For the most current version, please refer to the ClinGen website.*
