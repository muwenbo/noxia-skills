# ClinGen Limb Girdle Muscular Dystrophy VCEP Variant Interpretation Guidelines for CAPN3

**Version:** 2.0.0
**Released:** 7/9/2025
**Affiliation:** Limb Girdle Muscular Dystrophy VCEP
**Based on:** Tavtigian et al., 2020 - Bayesian adaptation of Richards et al., 2015 ACMG/AMP Guidelines

---

## Release Notes (v2.0.0)

- Specification type defined as Bayesian adaptation
- Correction to in-frame exons in PVS1 flowchart
- Clarification on use of experimental RNA/splice data: PVS1, PP3, BP4, BP7
- Clarification on use of gnomAD population frequency data (no change to thresholds): PM2, BA1, BS1
- Reduced weighting of de novo observation: PS2, PM6
- Updated guidance on evaluating missense variants at the same position: PM5

---

## Gene Information

| Attribute | Value |
|-----------|-------|
| **Gene** | CAPN3 (HGNC:1480) |
| **HGNC Name** | calpain 3 |
| **Transcript** | NM_000070.3 |
| **Disease** | Autosomal recessive limb-girdle muscular dystrophy (MONDO:0015152) |
| **Inheritance** | Autosomal recessive |

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
   - [BA1 - Allele Frequency >0.3%](#ba1---allele-frequency-03)
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
- Beware of genes where LOF is not a known disease mechanism (e.g., GFAP, MYH7)
- Use caution interpreting LOF variants at the extreme 3' end of a gene
- Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact
- Use caution in the presence of multiple transcripts

**VCEP Specifications:**

Please see the CAPN3 PVS1 flowchart in Appendix A. For any variant with RNA/splicing data, follow the SVI Working Group's recommendations (Walker et al. 2023; PMID: 37352859).

#### Strength Levels

| Strength | Point Value | Criteria |
|----------|-------------|----------|
| **Very Strong** | 8 | See PVS1 flowchart. Applies to nonsense/frameshift variants predicted to undergo NMD (premature truncation in codons 35-795), canonical splice site variants leading to frameshift + NMD, single/multi-exon deletions disrupting reading frame + NMD, full gene deletions, and duplications proven in tandem with frameshift + NMD. |
| **Strong** | 4 | See PVS1 flowchart. Applies to variants where truncated/altered region is critical to protein function, in-frame exon skipping removing >10% of protein, presumed in-tandem duplications with frameshift + NMD. |
| **Moderate** | 2 | See PVS1 flowchart. Applies to variants where role of region in protein function is unknown, in-frame exon skipping removing <10% of protein, initiation codon variants with pathogenic variants upstream of closest potential in-frame start codon, premature truncation within first 100 bp (codons 1-34). |
| **Supporting** | 1 | See PVS1 flowchart. Applies to initiation codon variants with a different functional transcript using alternative start codon. |

#### PVS1 Decision Tree Key Points for CAPN3

**Nonsense or Frameshift:**
- Predicted to undergo NMD (premature truncation in codons 35-795): **PVS1**
- Not predicted to undergo NMD: Evaluate based on region criticality and percent of protein removed
- Premature truncation within first 100 bp (codons 1-34): **PVS1_Moderate**

**GT-AG +/-1,2 Splice Sites:**
- Use SpliceAI prediction for most likely splice effect
- Exon skipping/cryptic splice disrupting reading frame + NMD predicted: **PVS1**
- Exon skipping/cryptic splice preserving reading frame: Evaluate based on region criticality
- In-frame exons where exon skipping is NOT expected to result in NMD: 1, 6, 7, 9, 12, 15, 16, 17, 20, 22, 24

**Deletions:**
- Single/multi-exon deletion disrupting reading frame + NMD predicted: **PVS1**
- Single/multi-exon deletion preserving reading frame: Evaluate based on region criticality
- Full gene deletion: **PVS1**

**Duplications (must be completely contained within gene):**
- Proven in tandem with reading frame disrupted + NMD: **PVS1**
- Presumed in tandem with reading frame presumed disrupted + NMD: **PVS1_Strong**
- No or unknown impact on reading frame: **N/A**

**Initiation Codon:**
- Different functional transcript uses alternative start codon: **PVS1_Supporting**
- No known alternative start codon + pathogenic variant(s) upstream of closest potential in-frame start codon: **PVS1_Moderate**
- No known alternative start codon + no pathogenic variants upstream: **N/A**

---

### PS1 - Same Amino Acid Change

**Original ACMG Summary:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.

**Caveat:** Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:**

#### For Missense Variants (amino acid change is expected mechanism):

| Strength | Point Value | Criteria |
|----------|-------------|----------|
| **Strong** | 4 | Apply for 1 pathogenic OR 2 likely pathogenic variants resulting in the same amino acid change. The LP/P variant(s) must be classified using LGMD VCEP specifications. Potential splice effects must be excluded (SpliceAI score ≤0.10 or experimental evidence of normal splicing). |
| **Moderate** | 2 | Apply for 1 likely pathogenic variant resulting in the same amino acid change. The LP variant must be classified using LGMD VCEP specifications. Potential splice effects must be excluded (SpliceAI score ≤0.10 or experimental evidence of normal splicing). |

#### For Variants with Altered Splicing (nucleotide change is expected mechanism):

| Strength | Point Value | Criteria |
|----------|-------------|----------|
| **Strong** | 4 | Follow SVI Working Group recommendations (Walker et al. 2023; PMID: 37352859). See PS1 splicing table in Appendix B. |
| **Moderate** | 2 | Follow SVI Working Group recommendations (Walker et al. 2023; PMID: 37352859). See PS1 splicing table in Appendix B. |
| **Supporting** | 1 | Follow SVI Working Group recommendations (Walker et al. 2023; PMID: 37352859). See PS1 splicing table in Appendix B. |

**Important Notes:**
- For missense variants encoded by the first or last 3 nucleotides of an exon, PS1 should be considered only in the context of altered splicing, unless a splice effect has been experimentally ruled out
- PS1 can potentially be applied to multiple nucleotide changes at the same residue as long as the variant classification that determines the strength level does not depend on PS1 application

---

### PS2 - De Novo (Confirmed)

**Original ACMG Summary:** De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.

**Note:** Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.

**VCEP Specifications:**

| Strength | Point Value | Criteria |
|----------|-------------|----------|
| **Supporting** | 1 | Apply for confirmed *de novo* occurrence in a proband meeting the criteria for PP4 (Supporting). Maternity and paternity should be confirmed by trio WES/WGS or other testing. |

---

### PS3 - Functional Studies

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.

**Note:** Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.

**VCEP Specifications:**

#### Variant-Specific Animal Models

| Strength | Point Value | Criteria |
|----------|-------------|----------|
| **Strong** | 4 | Apply for a variant-specific animal model (any species) meeting ALL of the following: (1) signs of myopathy or dystrophy in skeletal muscle, (2) effect on gene/protein function demonstrated (e.g., decreased protein expression, impaired membrane localization), (3) behavioral signs of muscle weakness, (4) progression over time. |
| **Moderate** | 2 | Apply for a variant-specific animal model (any species) meeting: (1) signs of myopathy or dystrophy in skeletal muscle, AND (2) effect on gene/protein function demonstrated (e.g., decreased protein expression, impaired membrane localization). |

#### In Vitro Assays

**Not applicable at this time** for CAPN3. Functional studies in heterologous systems are hard to conduct and rare in the literature. Assays that may be considered in the future include:
- Titin ectopic expression
- Titin degradation assay
- Baculovirus-based titin cleavage assay
- Assays of autolytic activity

#### RNA/Splicing Evidence

For any variant type, experimental evidence for altered splicing should be scored under **PVS1** in accordance with the decision tree for RNA splicing assay results outlined in Walker et al. 2023 (PMID: 37352859).

**Note:** Apply PS3 only once, for the piece of evidence that meets the highest possible strength level.

---

### PS4 - Prevalence in Affected

**Original ACMG Summary:** The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.

**VCEP Specifications:**

| Strength | Point Value | Criteria |
|----------|-------------|----------|
| **Strong** | 4 | Use without disease-specific modification if case-control studies are available. Relative risk (RR) or odds ratio (OR) >5.0 and confidence interval does not include 1.0. |

**Notes:**
- While case-control studies could potentially be considered for a few pathogenic variants with high minor allele frequency, the VCEP is unaware of any such studies being conducted for CAPN3
- Any case-control study would require careful selection of an appropriate control population given the potential for late onset and mild disease

---

### PM1 - Mutational Hot Spot

**Original ACMG Summary:** Located in a mutational hot spot and/or critical and well-established functional domain without benign variation.

**VCEP Specifications:** **Not applicable at this time.**

---

### PM2 - Absent from Controls

**Original ACMG Summary:** Absent from controls (or at extremely low frequency if recessive) in population databases.

**Caveat:** Population data for indels may be poorly called by next generation sequencing.

**VCEP Specifications:**

| Strength | Point Value | Criteria |
|----------|-------------|----------|
| **Supporting** | 1 | Apply if the Grpmax variant allele frequency / upper bound of the 95% CI of the Grpmax variant allele frequency in gnomAD is **<0.0001** |

#### Application Guidelines:

1. **Do not use** data for which the variant does not pass quality control filters
2. **If only 1 or 2 variant alleles** are present in the Grpmax population: use the Grpmax variant allele frequency
3. **If at least 3 variant alleles** are present in the Grpmax population: use the upper bound of the 95% confidence interval (95% CI) of the Grpmax variant allele frequency
4. **Grpmax** refers to the gnomAD subpopulation with the highest variant allele frequency
5. **Avoid using** the following groups for Grpmax: Amish, Ashkenazi Jewish, European Finnish, Remaining Individuals, and genomes-only data for Middle Eastern group
6. Use confidence interval tools such as [Confit-de-MAF](https://www.genecalculators.net/confit-de-maf.html) to calculate the upper bound of the 95% CI
7. Use the gnomAD version with the largest allele number
8. For larger deletions/duplications (single/multi-exon events), also confirm the variant is not common in gnomAD SVs, gnomAD CNVs, or the [Database of Genomic Variants (DGV)](https://dgv.tcag.ca/dgv/app/home)

---

### PM3 - In Trans with Pathogenic

**Original ACMG Summary:** For recessive disorders, detected in trans with a pathogenic variant.

**Note:** This requires testing of parents (or offspring) to determine phase.

**VCEP Specifications:**

Use the SVI Working Group's recommended point system to determine PM3 strength.

#### PM3 Point System (Per Proband)

| Classification/Zygosity of Other Variant | Confirmed in Trans | Phase Unknown |
|------------------------------------------|-------------------|---------------|
| Pathogenic or Likely pathogenic variant (classified using LGMD VCEP specs) | 1.0 | 0.5 (P) / 0.25 (LP) |
| Homozygous occurrence (max 1.0 pt; downgrade to 0.25 pts for consanguinity) | 0.5 | N/A |
| Uncertain significance variant (max 0.5 pts total; BA1/BS1 cannot be applicable) | 0.25 | 0 |

#### PM3 Evidence Strength Thresholds

| Total Points | Strength Level | Point Value |
|--------------|----------------|-------------|
| ≥0.5 but <1.0 | PM3_Supporting | 1 |
| ≥1.0 but <2.0 | PM3 (Moderate) | 2 |
| ≥2.0 but <4.0 | PM3_Strong | 4 |
| ≥4.0 | PM3_Very Strong | 8 |

#### Important Notes on Phase Unknown:

PM3 points should **NOT** be awarded for variants identified in unknown phase under the following circumstances:
- The same variants were ever confirmed in cis (e.g., in a different patient in the literature)
- gnomAD co-occurrence data ([gnomAD variant co-occurrence](https://gnomad.broadinstitute.org/variant-cooccurrence)) predict the variants may be part of the same haplotype in at least one genetic ancestry group
- More than 2 variants are reported in the patient, none of which can be classified as likely benign or benign

#### PM3 Co-Application Note:

It is possible to award PM3 points to both variants identified in an individual as long as the evidence related to their co-observation in that individual does not contribute to the variant classification that determines the number of points applied. This excludes all evidence derived from the co-observation, including:
- Inter-dependent PM3 points (pathogenicity of variant in trans/unknown phase)
- PP1 (genotype-phenotype co-segregation)
- PP4 (phenotype specificity)

See Appendix C for detailed examples.

---

### PM4 - Protein Length Changes

**Original ACMG Summary:** Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

**VCEP Specifications:**

| Strength | Point Value | Criteria |
|----------|-------------|----------|
| **Moderate** | 2 | Use as is, regardless of the length of the in-frame insertion or deletion. |

---

### PM5 - Novel Missense at Same Residue

**Original ACMG Summary:** Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.

**Example:** Arg156His is pathogenic; now you observe Arg156Cys.

**Caveat:** Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:**

Apply only for missense variants for which the amino acid change is the expected mechanism of disease.

#### Requirements for All Strength Levels:
- Exclude likely splice effects for the variant under curation AND the variant(s) resulting in a different amino acid change (SpliceAI score <0.5 or experimental evidence of normal splicing)
- REVEL score for the variant under curation should be >0.7
- Missense changes at the same residue must be classified according to LGMD VCEP specifications
- No benign missense variation should be present at the residue
- Do NOT apply for missense variants encoded by the first or last 3 nucleotides of an exon unless splice effects have been ruled out

| Strength | Point Value | Criteria |
|----------|-------------|----------|
| **Strong** | 4 | Apply for 2 pathogenic OR 3 likely pathogenic variants resulting in different amino acid changes at the same residue. |
| **Moderate** | 2 | Apply for 1 pathogenic OR 2 likely pathogenic variants resulting in different amino acid changes at the same residue. |
| **Supporting** | 1 | Apply for 1 likely pathogenic variant resulting in a different amino acid change at the same residue. |

**Note:** PM5 can potentially be applied to multiple amino acid changes at the same residue as long as the variant classification that determines the strength level does not depend on PM5 application.

---

### PM6 - De Novo (Assumed)

**Original ACMG Summary:** Assumed de novo, but without confirmation of paternity and maternity.

**VCEP Specifications:** **Not applicable.** See PS2.

---

### PP1 - Co-segregation

**Original ACMG Summary:** Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.

**Note:** May be used as stronger evidence with increasing segregation data.

**VCEP Specifications:**

Segregations should be counted across families, with the total number of segregations determining the strength level.

| Strength | Point Value | Criteria |
|----------|-------------|----------|
| **Strong** | 4 | 3 affected segregations (in addition to proband) across ≥2 families |
| **Moderate** | 2 | 2 affected segregations (in addition to proband; may be from a single family) |
| **Supporting** | 1 | 1 affected segregation (in addition to proband) |

**Important:** When applied together, PP1 and PP4 cannot exceed 5 Bayesian points (Supporting + Strong or Moderate + Moderate).

---

### PP2 - Missense in Constrained Gene

**Original ACMG Summary:** Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.

**VCEP Specifications:** **Not applicable.** CAPN3 is not constrained for missense variation (Z-score <3).

---

### PP3 - Computational Evidence

**Original ACMG Summary:** Multiple lines of computational evidence support a deleterious effect on the gene or gene product.

**Caveat:** As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.

**VCEP Specifications:**

| Strength | Point Value | Criteria |
|----------|-------------|----------|
| **Supporting** | 1 | **For missense variants:** REVEL score ≥0.7. **For variants that may affect splicing:** SpliceAI score ≥0.5 |

For any variant with RNA or other experimental data indicating an impact on splicing, follow the SVI Working Group's recommendations (Walker et al. 2023; PMID: 37352859).

---

### PP4 - Phenotype Specificity

**Original ACMG Summary:** Patient's phenotype or family history is highly specific for a disease with a single genetic etiology.

**VCEP Specifications:**

Use the PP4 table to determine the appropriate strength level. Apply PP4 only once, for a patient meeting the highest possible strength level.

#### PP4 Requirements for CAPN3

|  | PP4 Strength Level |  |  |
|--|-------------------|--|--|
| **Requirement** | **Supporting** | **Moderate** | **Strong** |
| **Clinical:** Progressive limb-girdle pattern of muscle weakness observed over ≥6 months OR clinical suspicion of LGMD | Required | Required | Required |
| **Genetic testing:** 2 presumed diagnostic variants in CAPN3, 1 of which is the variant under curation | Required | Required | Required |
| **Protein expression:** Severely reduced (≤~30% normal) expression of full-length calpain-3 in skeletal muscle (e.g., WB) | Not required | Required (Option A) | Not applicable |
| **Protein expression:** Absent/trace expression of full-length calpain-3 in skeletal muscle (e.g., WB) | Not required | Not applicable | Required (Option B) |

**Notes:**
- Clinical findings may be accompanied by supporting EMG, MRI, muscle histology, elevated CK but not required
- Genetic testing: Screening of all exons and exon/intron boundaries of CAPN3 required; screening of additional neuromuscular disease genes (e.g., through a panel) is recommended but not required
- For genetic testing: If variants have not yet been curated by the LGMD VCEP, confirm they cannot be classified as LB or B (e.g., through application of BA1, BS1, and/or BP4/BP7). If phase is unknown, do not apply if the identified variants were ever confirmed in cis or if gnomAD co-occurrence data predict the variants may be part of the same haplotype
- "Severely reduced" means ≤~30% normal; may also be described as "drastically" or "strongly" reduced
- "Absent" may also be described as "trace" or "barely detectable"

**Important:** When applied together, PP1 and PP4 cannot exceed 5 Bayesian points (Supporting + Strong or Moderate + Moderate). If PP1_Moderate is applied and the criteria for PP4_Strong are also met, a downgraded PP4_Moderate can be applied.

| Strength | Point Value |
|----------|-------------|
| **Strong** | 4 |
| **Moderate** | 2 |
| **Supporting** | 1 |

---

### PP5 - Reputable Source

**Original ACMG Summary:** Reputable source recently reports variant as pathogenic, but the evidence is not available to the laboratory to perform an independent evaluation.

**VCEP Specifications:** **Not applicable.** This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PMID: 29543229).

---

## Benign Criteria

### BA1 - Allele Frequency >0.3%

**Original ACMG Summary:** Allele frequency is above 5% in population databases.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Stand Alone** | Apply if the variant Grpmax FAF (the lower bound of the 95% confidence interval of the maximum credible genetic ancestry group allele frequency) is **>0.003 (0.3%)** |

**Notes:**
- This value can be taken directly from gnomAD, but do not use data for which the variant does not pass quality control filters
- See supplementary file "benign frequency exceptions" for a list of variants defined as exceptions to the benign frequency rules
- Ongoing updates available at the [LGMD VCEP webpage](https://clinicalgenome.org/affiliation/50061/)
- Variants whose frequency may not be reliable (e.g., sequencing artifacts) should be critically evaluated and brought to the attention of the LGMD VCEP

---

### BS1 - Frequency Greater Than Expected

**Original ACMG Summary:** Allele frequency is greater than expected for disorder.

**VCEP Specifications:**

| Strength | Point Value | Criteria |
|----------|-------------|----------|
| **Strong** | -4 | Apply if the variant Grpmax FAF (the lower bound of the 95% confidence interval of the maximum credible genetic ancestry group allele frequency) is **>0.001 (0.1%)** |

**Notes:**
- This value can be taken directly from gnomAD, but do not use data for which the variant does not pass quality control filters
- See benign frequency exceptions table below
- Variants whose frequency may not be reliable should be critically evaluated

#### Benign Frequency Exceptions for CAPN3

| Variant | Status | Comment |
|---------|--------|---------|
| NM_000070.3(CAPN3):c.1746-20C>G | BS1 exception | Proposed hypomorph |
| NM_000070.3(CAPN3):c.2120A>G (p.Asp707Gly) | BS1 exception | Likely founder in East Asian population |

---

### BS2 - Observed in Healthy Adult

**Original ACMG Summary:** Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

**VCEP Specifications:** **Not applicable.** LGMD is characterized by variable expressivity and late-onset LGMD is not uncommon.

---

### BS3 - Functional Studies (No Effect)

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

**VCEP Specifications:** **Not applicable.** Since the muscle disease mechanisms are complex, it is not feasible at this time to exclude all pathogenic functional abnormalities through available assays.

---

### BS4 - Lack of Segregation

**Original ACMG Summary:** Lack of segregation in affected members of a family.

**Caveat:** The presence of phenocopies for common phenotypes can mimic lack of segregation among affected individuals. Families may have more than one pathogenic variant contributing to disease.

**VCEP Specifications:**

| Strength | Point Value | Criteria |
|----------|-------------|----------|
| **Strong** | -4 | Use as is. One affected individual (genotype-, phenotype+) is sufficient for BS4. Do NOT apply for genotype+, phenotype- individuals, as LGMD is characterized by variable expressivity and late onset is not uncommon. |

---

### BP1-BP7 - Benign Supporting

| Criterion | Status | Point Value | Specification |
|-----------|--------|-------------|---------------|
| **BP1** | Not Applicable | - | Missense variants are also known to cause disease in CAPN3. |
| **BP2** | Applicable | -1 | Use when variant is found *in cis* with a variant classified as pathogenic or likely pathogenic using the LGMD VCEP specifications. |
| **BP3** | Not Applicable | - | Repetitive regions without a known function are not well described in CAPN3. |
| **BP4** | Applicable | -1 | **For missense variants:** Use REVEL ≤0.1 AND SpliceAI ≤0.05. **For variants that may affect splicing:** Use SpliceAI ≤0.05. For any variant with RNA/experimental data indicating no impact on splicing, follow SVI Working Group recommendations. |
| **BP5** | Not Applicable | - | Secondary deficiencies of related proteins are often seen in LGMD. |
| **BP6** | Not Applicable | - | Not for use per ClinGen SVI VCEP Review Committee (PMID: 29543229). |
| **BP7** | Applicable (see below) | -1 to -4 | See BP7 specifications below. |

#### BP7 Specifications

| Strength | Point Value | Criteria |
|----------|-------------|----------|
| **Strong** | -4 | For any variant that has been experimentally shown to have no splice impact, follow SVI Working Group recommendations (Walker et al. 2023; PMID: 37352859). Apply if a splicing assay shows no effect on splicing AND a protein impact can be ruled out. |
| **Supporting** | -1 | For splice predictions, use SpliceAI ≤0.05. BP7 may be co-applied with BP4 for synonymous, UTR, and intronic variants located outside the splice donor/acceptor regions designated in Walker et al. 2023 (+6/-3 for donor; +1/-20 for acceptor). |

---

## Rules for Combining Criteria

### Point-Based Classification System

| Category | Point Range |
|----------|-------------|
| **Pathogenic** | ≥10 |
| **Likely Pathogenic** | 6 - 9 |
| **Uncertain Significance** | 0 - 5 |
| **Likely Benign** | -6 to -1 |
| **Benign** | ≤-7 OR BA1 applies |

### Bayesian Point Values Summary

| Evidence Strength | Pathogenic Points | Benign Points |
|-------------------|-------------------|---------------|
| Very Strong | 8 | - |
| Strong | 4 | -4 |
| Moderate | 2 | -2 |
| Supporting | 1 | -1 |
| Stand Alone (BA1) | - | Benign |

### Criteria Point Values for CAPN3

| Criterion | Available Strengths | Point Values |
|-----------|---------------------|--------------|
| PVS1 | Very Strong / Strong / Moderate / Supporting | 8 / 4 / 2 / 1 |
| PS1 | Strong / Moderate / Supporting | 4 / 2 / 1 |
| PS2 | Supporting only | 1 |
| PS3 | Strong / Moderate | 4 / 2 |
| PS4 | Strong | 4 |
| PM2 | Supporting only | 1 |
| PM3 | Very Strong / Strong / Moderate / Supporting | 8 / 4 / 2 / 1 |
| PM4 | Moderate | 2 |
| PM5 | Strong / Moderate / Supporting | 4 / 2 / 1 |
| PP1 | Strong / Moderate / Supporting | 4 / 2 / 1 |
| PP3 | Supporting | 1 |
| PP4 | Strong / Moderate / Supporting | 4 / 2 / 1 |
| BA1 | Stand Alone | Benign |
| BS1 | Strong | -4 |
| BS4 | Strong | -4 |
| BP2 | Supporting | -1 |
| BP4 | Supporting | -1 |
| BP7 | Strong / Supporting | -4 / -1 |

### Criteria Not Applicable for CAPN3

| Criterion | Reason |
|-----------|--------|
| PM1 | Not applicable at this time |
| PM6 | Not applicable; see PS2 |
| PP2 | CAPN3 is not constrained for missense variation (Z-score <3) |
| PP5 | Not for use per ClinGen SVI recommendation |
| BS2 | LGMD characterized by variable expressivity and late onset |
| BS3 | Complex muscle disease mechanisms; cannot exclude all pathogenic abnormalities |
| BP1 | Missense variants cause disease in CAPN3 |
| BP3 | No well-described repetitive regions without known function |
| BP5 | Secondary deficiencies of related proteins seen in LGMD |
| BP6 | Not for use per ClinGen SVI recommendation |

---

## Appendices

### Appendix A: PVS1 Flowchart for CAPN3

#### Nonsense or Frameshift Variants

```
Nonsense or Frameshift
         │
         ├── Predicted to undergo NMD (premature truncation codons 35-795)
         │         └── PVS1
         │
         └── NOT predicted to undergo NMD
                   │
                   ├── Premature truncation within first 100 bp (codons 1-34)
                   │         └── PVS1_Moderate
                   │
                   └── Exon present in biologically relevant transcript (NM_000070.3)
                             │
                             ├── Truncated/altered region critical to protein function (none specified)
                             │         └── PVS1_Strong
                             │
                             └── Role of region in protein function unknown
                                       │
                                       ├── LoF variants frequent in exon OR exon absent from transcript
                                       │         └── N/A
                                       │
                                       └── LoF variants NOT frequent AND exon present
                                                 │
                                                 ├── Variant removes >10% of protein
                                                 │         └── PVS1_Strong
                                                 │
                                                 └── Variant removes <10% of protein
                                                           └── PVS1_Moderate
```

#### GT-AG +/-1,2 Splice Sites

```
GT-AG ±1,2 splice sites
         │
         └── Use SpliceAI prediction of most likely splice effect
                   │
                   ├── Exon skipping/cryptic splice DISRUPTS reading frame
                   │         │
                   │         ├── Predicted to undergo NMD
                   │         │         └── PVS1
                   │         │
                   │         └── NOT predicted to undergo NMD
                   │                   └── [Same evaluation as nonsense/frameshift not undergoing NMD]
                   │
                   └── Exon skipping/cryptic splice PRESERVES reading frame
                             │
                             └── In-frame exons (exon skipping NOT expected to result in NMD):
                                 1, 6, 7, 9, 12, 15, 16, 17, 20, 22, 24
                                       │
                                       ├── Truncated/altered region critical (none specified)
                                       │         └── PVS1_Strong
                                       │
                                       └── Role unknown
                                                 │
                                                 ├── LoF variants frequent OR exon absent
                                                 │         └── N/A
                                                 │
                                                 └── LoF NOT frequent AND exon present
                                                           │
                                                           ├── Removes >10% protein
                                                           │         └── PVS1_Strong
                                                           │
                                                           └── Removes <10% protein
                                                                     └── PVS1_Moderate
```

#### Deletions

```
Deletion (single exon to full gene)
         │
         ├── Full gene deletion
         │         └── PVS1
         │
         ├── Single/multi-exon deletion - DISRUPTS reading frame
         │         │
         │         ├── Predicted to undergo NMD
         │         │         └── PVS1
         │         │
         │         └── NOT predicted to undergo NMD
         │                   └── [Same evaluation as nonsense/frameshift not undergoing NMD]
         │
         └── Single/multi-exon deletion - PRESERVES reading frame
                   └── [Same evaluation as in-frame splice variants]
```

#### Duplications

```
Duplication (≥1 exon, completely contained within gene)
         │
         ├── Proven in tandem
         │         │
         │         ├── Reading frame disrupted + NMD predicted
         │         │         └── PVS1
         │         │
         │         └── No or unknown impact on reading frame
         │                   └── N/A
         │
         ├── Presumed in tandem
         │         │
         │         └── Reading frame presumed disrupted + NMD predicted
         │                   └── PVS1_Strong
         │
         └── Proven NOT in tandem
                   └── N/A
```

#### Initiation Codon Variants

```
Initiation Codon
         │
         ├── Different functional transcript uses alternative start codon
         │         └── PVS1_Supporting
         │
         └── No known alternative start codon in other transcripts
                   │
                   ├── ≥1 pathogenic variant(s) upstream of closest potential in-frame start codon
                   │         └── PVS1_Moderate
                   │
                   └── No pathogenic variants upstream of closest potential in-frame start codon
                             └── N/A
```

---

### Appendix B: PS1 Splicing Table

**PS1 code weights for variants with same predicted splicing event as a known (likely) pathogenic variant**

| Variant Under Assessment (VUA) | Baseline Code Applicable to VUA | Position of Comparison Variant Relative to VUA | PS1 with P Comparison Variant | PS1 with LP Comparison Variant |
|-------------------------------|--------------------------------|-----------------------------------------------|------------------------------|-------------------------------|
| Located outside splice donor/acceptor ±1,2 dinucleotide positions | PP3 | Same nucleotide | PS1 | PS1_Moderate |
| Located outside splice donor/acceptor ±1,2 dinucleotide positions | PP3 | Within same splice donor/acceptor motif (including at ±1,2 positions) | PS1_Moderate | PS1_Supporting |
| Located at splice donor/acceptor ±1,2 dinucleotide positions | PVS1 | Within same splice donor/acceptor ±1,2 dinucleotide | PS1_Supporting | N/A |
| Located at splice donor/acceptor ±1,2 dinucleotide positions | PVS1 | Within same splice donor/acceptor region, but outside ±1,2 dinucleotide | PS1_Supporting | PS1_Supporting |
| Located at splice donor/acceptor ±1,2 dinucleotide positions | PVS1_Strong, PVS1_Moderate, or PVS1_Supporting | Within same splice donor/acceptor ±1,2 dinucleotide | PS1 | N/A |
| Located at splice donor/acceptor ±1,2 dinucleotide positions | PVS1_Strong, PVS1_Moderate, or PVS1_Supporting | Within same splice donor/acceptor motif, but outside ±1,2 dinucleotide | PS1_Moderate | PS1_Supporting |

**Prerequisites:**
- The predicted event of the VUA must precisely match the predicted event of the comparison (likely) pathogenic variant (e.g., both predicted to lead to exon skipping, or both to lead to enhanced use of a cryptic splice motif)
- The strength of the prediction for the VUA must be of similar or higher strength than the strength of the prediction for the comparison [likely] pathogenic variant
- For an exonic variant, predicted or proven functional effect of missense substitution(s) encoded by the VUA and (likely) pathogenic variant should also be considered before application of this code
- Dinucleotide positions refer to donor and acceptor dinucleotides in reference transcript(s) used for curation
- Designated donor and acceptor motif ranges should be based on position weight matrices for intron category. For GT-AG introns: donor motif = last 3 bases of exon + 6 nucleotides of intronic sequence adjacent to exon; acceptor motif = first base of exon + 20 nucleotides upstream from exon boundary
- If relevant, splicing assay data for a pathogenic variant outside a ±1,2 dinucleotide position may be used to update a PVS1 decision tree and hence the applicable PVS1 code for a ±1,2 dinucleotide variant

---

### Appendix C: PM3 Co-Application Examples

#### Example 1: PM3 can be awarded to both variants without circularity

**Scenario:**
- Variants A and B are observed in trans in patient X, who meets PP4 criteria
- Variant A has not been observed in any other patients
- Variant B has also been observed in patient Y, where it was confirmed in trans with pathogenic variant C (1.0 PM3 pt) in an individual meeting PP4_Moderate

**Classifications (independent of patient X observation):**
- Variant A: LP (PVS1 + PM2_Supporting)
- Variant B: LP (PS3_Moderate + PP3 + PM2_Supporting + PP4_Moderate [patient Y] + PM3 [variant C in patient Y])

**PM3 Application:**
- For Variant B curation: 1.0 PM3 pt can be awarded for patient X (confirmed in trans with LP variant A). With additional 1.0 pt, PM3 upgrades to PM3_Strong. Final classification: **P** (PS3_Moderate + PP3 + PM2_Supporting + PP4_Moderate [patient Y] + PM3_Strong [patients X + Y])
- For Variant A curation: 1.0 PM3 pt can be awarded for patient X (confirmed in trans with LP variant B). Final classification: **P** (PVS1 + PM2_Supporting + PM3 [patient X] + PP4 [patient X])

**Key principle:** The classification used when awarding PM3 points is the classification reached WITHOUT counting evidence from the co-observation in patient X.

#### Example 2: PM3 cannot be awarded to both variants without circularity

**Scenario:**
- Variants A and B are observed in trans in patient X, who meets PP4 criteria
- Variant A has not been observed in any other patients
- Variant B has also been observed in patient Y, where it was observed in unknown phase with VUS variant C (0 PM3 pts) in an individual meeting PP4

**Classifications (independent of patient X observation):**
- Variant A: LP (PVS1 + PM2_Supporting)
- Variant B: VUS (PS3_Moderate + PP3 + PM2_Supporting + PP4 [patient Y])

**PM3 Application:**
- For Variant B curation: PM3 can be awarded for patient X (confirmed in trans with LP variant A = 1.0 pt). Final classification: **LP** (PS3_Moderate + PP3 + PM2_Supporting + PP4 [patient Y] + PM3 [patient X])
- For Variant A curation: PM3 CANNOT be awarded for patient X because variant B was classified as VUS independent of patient X observation, and 0.25 PM3 pts (for being in trans with VUS) is insufficient for any PM3 strength level. However, PP4 can be applied. Final classification: **P** (PVS1 + PM2_Supporting + PP4 [patient X])

---

### Appendix D: Experimental Splice Data Interpretation

For any variant with RNA/splicing data, follow the SVI Working Group's recommendations (Walker et al. 2023; PMID: 37352859).

#### Decision Tree for RNA Splicing Assay Results

**Categorization of splicing data needs to consider multiple factors:**
- Assay/technique
- RNA source
- Gene-specific knowledge

**For Silent/Intronic Variants:**
- No variant-specific observed impact (compared to controls): Apply BP7_S (RNA)
- Variant-specific impact (compared to controls): Follow PVS1 flowchart for OBSERVED RNA impact for your gene

**For Other Variants:**
- Assess pathogenicity using protein pathway
- If PVS1_Strength assigned to at least 1 transcript: Follow flowchart

**Proportion of Alternative Transcripts:**
- Complete (variant allele): Keep strength level
- Near complete: Reduce strength by 1 level
- Incomplete: Do not apply codes

**If background rate is considered to be at/above tolerable levels suggesting tolerance of being tolerated:**
- Consider reducing PVS1 (RNA) codes by an additional level

---

### Appendix E: Population Frequency Thresholds Summary

| Criterion | Threshold | Metric | Strength |
|-----------|-----------|--------|----------|
| BA1 | >0.003 (0.3%) | Grpmax FAF | Stand Alone (Benign) |
| BS1 | >0.001 (0.1%) | Grpmax FAF | Strong (-4 points) |
| PM2 | <0.0001 (0.01%) | Grpmax VAF or upper bound 95% CI | Supporting (1 point) |

**Grpmax FAF:** The lower bound of the 95% confidence interval of the maximum credible genetic ancestry group allele frequency (taken directly from gnomAD)

**Grpmax VAF:** The variant allele frequency in the gnomAD subpopulation with the highest frequency

**Populations to avoid for Grpmax:** Amish, Ashkenazi Jewish, European Finnish, Remaining Individuals, genomes-only Middle Eastern data

---

### Appendix F: Computational Prediction Thresholds Summary

| Criterion | Tool | Pathogenic Threshold | Benign Threshold |
|-----------|------|---------------------|------------------|
| PP3/BP4 (missense) | REVEL | ≥0.7 | ≤0.1 |
| PP3/BP4/BP7 (splicing) | SpliceAI | ≥0.5 | ≤0.05 |
| PS1/PM5 (splice exclusion) | SpliceAI | >0.10 suggests splice effect | ≤0.10 excludes splice effect |
| PM5 (missense requirement) | REVEL | >0.7 required | - |
| PM5 (splice exclusion) | SpliceAI | ≥0.5 suggests splice effect | <0.5 excludes splice effect |

**SpliceAI Lookup:** https://spliceailookup.broadinstitute.org/

---

### Appendix G: Key Resources

| Resource | URL |
|----------|-----|
| LGMD VCEP Webpage | https://clinicalgenome.org/affiliation/50061/ |
| gnomAD Browser | https://gnomad.broadinstitute.org/ |
| gnomAD Variant Co-occurrence | https://gnomad.broadinstitute.org/variant-cooccurrence |
| SpliceAI Lookup | https://spliceailookup.broadinstitute.org/ |
| Confit-de-MAF Calculator | https://www.genecalculators.net/confit-de-maf.html |
| Database of Genomic Variants | https://dgv.tcag.ca/dgv/app/home |

---

### Appendix H: Key References

| PMID | Reference |
|------|-----------|
| 37352859 | Walker et al. 2023 - SVI Working Group recommendations for RNA/splicing data interpretation |
| 29543229 | ClinGen SVI VCEP Review Committee recommendation on PP5/BP6 |

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 2.0.0 | 7/9/2025 | Specification type defined as Bayesian adaptation; Correction to in-frame exons in PVS1 flowchart; Clarification on use of experimental RNA/splice data (PVS1, PP3, BP4, BP7); Clarification on use of gnomAD population frequency data (PM2, BA1, BS1); Reduced weighting of de novo observation (PS2, PM6); Updated guidance on evaluating missense variants at same position (PM5) |

---

*This document was compiled from ClinGen VCEP specifications. For the most current version, please refer to the [ClinGen website](https://clinicalgenome.org/) and the [LGMD VCEP page](https://clinicalgenome.org/affiliation/50061/).*
