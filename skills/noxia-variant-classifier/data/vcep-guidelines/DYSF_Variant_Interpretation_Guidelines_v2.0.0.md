# ClinGen Limb Girdle Muscular Dystrophy VCEP Variant Interpretation Guidelines for DYSF

**Version:** 2.0.0
**Released:** 7/9/2025
**Affiliation:** Limb Girdle Muscular Dystrophy VCEP
**Based on:** Tavtigian et al., 2020 - Bayesian adaptation of Richards et al., 2015

---

## Gene Information

| Attribute | Value |
|-----------|-------|
| **Gene** | DYSF (HGNC:3097) |
| **HGNC Name** | dysferlin |
| **Transcript** | NM_003494.4 |
| **Disease** | Autosomal recessive limb-girdle muscular dystrophy (MONDO:0015152) |
| **Inheritance** | Autosomal recessive |

---

## Release Notes (v2.0.0)

- Specification type defined as Bayesian adaptation
- Correction to in-frame exons in PVS1 flowchart: PVS1
- Clarification on use of experimental RNA/splice data: PVS1, PP3, BP4, BP7
- Clarification on use of gnomAD population frequency data (no change to thresholds): PM2, BA1, BS1
- Reduced weighting of de novo observation: PS2, PM6
- Updated guidance on evaluating missense variants at the same position: PM5

---

## Table of Contents

1. [Point-Based Classification System](#point-based-classification-system)
2. [Pathogenic Criteria](#pathogenic-criteria)
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
3. [Benign Criteria](#benign-criteria)
   - [BA1 - Allele Frequency >0.3%](#ba1---allele-frequency-03)
   - [BS1 - Frequency Greater Than Expected](#bs1---frequency-greater-than-expected)
   - [BS2 - Observed in Healthy Adult](#bs2---observed-in-healthy-adult)
   - [BS3 - Functional Studies (No Effect)](#bs3---functional-studies-no-effect)
   - [BS4 - Lack of Segregation](#bs4---lack-of-segregation)
   - [BP1-BP7 - Benign Supporting](#bp1-bp7---benign-supporting)
4. [Appendices](#appendices)
   - [Appendix A: PVS1 Decision Tree](#appendix-a-pvs1-decision-tree)
   - [Appendix B: PM3 Point System and Examples](#appendix-b-pm3-point-system-and-examples)
   - [Appendix C: PP4 Phenotype Table](#appendix-c-pp4-phenotype-table)
   - [Appendix D: PS3/BS3 Approved Functional Assays](#appendix-d-ps3bs3-approved-functional-assays)
   - [Appendix E: PS1 Splicing Code Weights](#appendix-e-ps1-splicing-code-weights)
   - [Appendix F: Experimental Splice Data Decision Tree](#appendix-f-experimental-splice-data-decision-tree)
   - [Appendix G: Benign Frequency Exceptions](#appendix-g-benign-frequency-exceptions)
   - [Appendix H: Population Frequency Thresholds Summary](#appendix-h-population-frequency-thresholds-summary)

---

## Point-Based Classification System

This VCEP uses a Bayesian point-based variant classification system.

| Category | Point Range |
|----------|-------------|
| **Pathogenic** | ≥10 |
| **Likely Pathogenic** | 6 - 9 |
| **Uncertain Significance** | 0 - 5 |
| **Likely Benign** | -6 to -1 |
| **Benign** | ≤-7 or BA1 applies |

---

## Pathogenic Criteria

### PVS1 - Null Variant

**Original ACMG Summary:** Null variant (nonsense, frameshift, canonical ±1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.

**Caveats:**
- Beware of genes where LOF is not a known disease mechanism (e.g., GFAP, MYH7)
- Use caution interpreting LOF variants at the extreme 3' end of a gene
- Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact
- Use caution in the presence of multiple transcripts

**VCEP Specifications:**

Please see the DYSF PVS1 flowchart in [Appendix A](#appendix-a-pvs1-decision-tree). In addition, for any variant with RNA/splicing data, follow the SVI Working Group's recommendations (Walker et al. 2023; PMID: 37352859). See [Appendix F](#appendix-f-experimental-splice-data-decision-tree) for experimental splice data guidance.

#### Strength Levels

| Strength | Default Points | Criteria |
|----------|----------------|----------|
| **Very Strong** | 8 | See PVS1 flowchart for variant types meeting this level |
| **Strong** | 4 | See PVS1 flowchart for variant types meeting this level |
| **Moderate** | 2 | See PVS1 flowchart for variant types meeting this level |
| **Supporting** | 1 | See PVS1 flowchart for variant types meeting this level |

**Note:** The MANE Select transcript (NM_001130987) is not significantly expressed in skeletal muscle (PMID: 19221801; GTEx). Use NM_003494.4 as the biologically relevant transcript.

**In-frame exons:** Exons for which exon skipping is not expected to result in NMD: 7, 8, 9, 14, 17, 19, 24, 25, 30, 32, 34, 35, 36, 37, 38, 41, 42, 43, 45, 49, 55

---

### PS1 - Same Amino Acid Change

**Original ACMG Summary:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.

**Caveat:** Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:**

#### For Missense Variants (Amino Acid Change Mechanism)

| Strength | Default Points | Criteria |
|----------|----------------|----------|
| **Strong** | 4 | Apply for 1 pathogenic OR 2 likely pathogenic variants resulting in the same amino acid change. The LP/P variant(s) must have been classified using LGMD VCEP specifications. Potential splice effects must be excluded (SpliceAI score ≤0.10 or experimental evidence of normal splicing). |
| **Moderate** | 2 | Apply for 1 likely pathogenic variant resulting in the same amino acid change. The LP variant must have been classified using LGMD VCEP specifications. Potential splice effects must be excluded (SpliceAI score ≤0.10 or experimental evidence of normal splicing). |

**Important Notes:**
- PS1 can potentially be applied to multiple nucleotide changes at the same residue as long as the variant classification that determines the strength level does not depend on PS1 application
- For missense variants encoded by the first or last 3 nucleotides of an exon, PS1 should be considered only in the context of altered splicing (see below), unless a splice effect has been experimentally ruled out

#### For Splice Variants (Nucleotide Change Mechanism)

| Strength | Default Points | Criteria |
|----------|----------------|----------|
| **Strong** | 4 | Follow SVI Working Group recommendations (Walker et al. 2023; PMID: 37352859). See [Appendix E](#appendix-e-ps1-splicing-code-weights). |
| **Moderate** | 2 | Follow SVI Working Group recommendations (Walker et al. 2023; PMID: 37352859). See [Appendix E](#appendix-e-ps1-splicing-code-weights). |
| **Supporting** | 1 | Follow SVI Working Group recommendations (Walker et al. 2023; PMID: 37352859). See [Appendix E](#appendix-e-ps1-splicing-code-weights). |

---

### PS2 - De Novo (Confirmed)

**Original ACMG Summary:** De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.

**Note:** Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.

**VCEP Specifications:**

| Strength | Default Points | Criteria |
|----------|----------------|----------|
| **Supporting** | 1 | Apply for confirmed *de novo* occurrence in a proband meeting the criteria for PP4 (Supporting). Maternity and paternity should be confirmed by trio WES/WGS or other testing. |

---

### PS3 - Functional Studies

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.

**Note:** Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.

**VCEP Specifications:**

| Strength | Default Points | Criteria |
|----------|----------------|----------|
| **Strong** | 4 | Variant-specific animal model meeting ALL of the following: (1) signs of myopathy or dystrophy in skeletal muscle, (2) effect on gene/protein function demonstrated, (3) behavioral signs of muscle weakness, (4) progression over time |
| **Moderate** | 2 | Variant-specific animal model meeting: (1) signs of myopathy or dystrophy in skeletal muscle AND (2) effect on gene/protein function demonstrated. **OR** Dysferlin membrane localization functional score <0.25 AND concordant immunocytochemistry assay result (Tominaga et al. 2022; PMID: 35028538) |
| **Supporting** | 1 | Variant expressed in heterologous cell lines/model organisms showing absent membrane localization of dysferlin protein, but fewer than 11 control variants were used |

**Important Notes:**
- For any variant type, experimental evidence for altered splicing should be scored under PVS1 in accordance with the SVI Working Group decision tree (Walker et al. 2023; PMID: 37352859)
- Apply PS3 only once, for the piece of evidence that meets the highest possible strength level
- Assays that may be considered in the future include membrane resealing activity assays and calcium signaling assays

See [Appendix D](#appendix-d-ps3bs3-approved-functional-assays) for approved assay details.

---

### PS4 - Prevalence in Affected

**Original ACMG Summary:** The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.

**VCEP Specifications:**

| Strength | Default Points | Criteria |
|----------|----------------|----------|
| **Strong** | 4 | Use without disease-specific modification if case-control studies are available. Any case-control study would require careful selection of an appropriate control population given the potential for late onset and mild disease. |

**Note:** While case-control studies could potentially be considered for a few pathogenic variants with high minor allele frequency, the VCEP is unaware of any such studies being conducted for DYSF.

---

### PM1 - Mutational Hot Spot

**Original ACMG Summary:** Located in a mutational hot spot and/or critical and well-established functional domain (e.g., active site of an enzyme) without benign variation.

**VCEP Specifications:**

| Status | Comment |
|--------|---------|
| **Not Applicable** | Not applicable at this time. |

---

### PM2 - Absent from Controls

**Original ACMG Summary:** Absent from controls (or at extremely low frequency if recessive) in population databases.

**Caveat:** Population data for indels may be poorly called by next generation sequencing.

**VCEP Specifications:**

| Strength | Default Points | Criteria |
|----------|----------------|----------|
| **Supporting** | 1 | Apply if the Grpmax variant allele frequency / upper bound of the 95% confidence interval (95% CI) of the Grpmax variant allele frequency in gnomAD is **<0.0001** |

**Detailed Instructions:**
- If only 1 or 2 variant alleles are present in the Grpmax population, use the Grpmax variant allele frequency
- If at least 3 variant alleles are present in the Grpmax population, use the upper bound of the 95% CI of the Grpmax variant allele frequency
- Grpmax refers to the gnomAD subpopulation with the highest variant allele frequency
- **Avoid using:** Amish, Ashkenazi Jewish, European Finnish, and Remaining Individuals groups, as well as the genomes-only data for the Middle Eastern group
- The upper bound of the 95% CI must be calculated using variant allele numbers and counts from gnomAD. Use tools such as [Confit-de-MAF](https://www.genecalculators.net/confit-de-maf.html)
- Use the gnomAD version with the largest allele number
- For larger deletions/duplications, also confirm the variant is not common in gnomAD SVs, gnomAD CNVs, or the [Database of Genomic Variants (DGV)](https://dgv.tcag.ca/dgv/app/home)
- Do not use data for which the variant does not pass quality control filters

---

### PM3 - In Trans with Pathogenic

**Original ACMG Summary:** For recessive disorders, detected in trans with a pathogenic variant.

**Note:** This requires testing of parents (or offspring) to determine phase.

**VCEP Specifications:**

Use the SVI Working Group's recommended point system to determine PM3 strength. See [Appendix B](#appendix-b-pm3-point-system-and-examples) for the complete point table and examples.

| Strength | Default Points | Point Threshold |
|----------|----------------|-----------------|
| **Very Strong** | 8 | ≥4.0 points |
| **Strong** | 4 | ≥2.0 to <4.0 points |
| **Moderate** | 2 | ≥1.0 to <2.0 points |
| **Supporting** | 1 | ≥0.5 to <1.0 points |

---

### PM4 - Protein Length Changes

**Original ACMG Summary:** Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

**VCEP Specifications:**

| Strength | Default Points | Criteria |
|----------|----------------|----------|
| **Moderate** | 2 | Use as is, regardless of the length of the in-frame insertion or deletion |

---

### PM5 - Novel Missense at Same Residue

**Original ACMG Summary:** Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.

**Caveat:** Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:**

Apply only for missense variants for which the amino acid change is the expected mechanism of disease.

**Requirements for all strength levels:**
- For the missense variant under curation and the variant(s) resulting in a different amino acid change, exclude likely splice effects (SpliceAI score <0.5 or experimental evidence of normal splicing)
- The REVEL score for the missense variant under curation should be >0.7
- Missense changes at the same residue must be classified according to LGMD VCEP specifications
- No benign missense variation should be present at the residue
- Do not apply for missense variants encoded by the first or last 3 nucleotides of an exon unless a splice effect has been ruled out
- PM5 can potentially be applied to multiple amino acid changes at the same residue as long as the variant classification that determines the strength level does not depend on PM5 application

| Strength | Default Points | Criteria |
|----------|----------------|----------|
| **Strong** | 4 | 2 pathogenic OR 3 likely pathogenic variants resulting in different amino acid changes at the same residue |
| **Moderate** | 2 | 1 pathogenic OR 2 likely pathogenic variants resulting in different amino acid changes at the same residue |
| **Supporting** | 1 | 1 likely pathogenic variant resulting in a different amino acid change at the same residue |

---

### PM6 - De Novo (Assumed)

**Original ACMG Summary:** Assumed de novo, but without confirmation of paternity and maternity.

**VCEP Specifications:**

| Status | Comment |
|--------|---------|
| **Not Applicable** | See PS2. |

---

### PP1 - Co-segregation

**Original ACMG Summary:** Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.

**Note:** May be used as stronger evidence with increasing segregation data.

**VCEP Specifications:**

Segregations should be counted across families, with the total number of segregations determining the strength level.

| Strength | Default Points | Criteria |
|----------|----------------|----------|
| **Strong** | 4 | 3 affected segregations (in addition to proband) across ≥2 families |
| **Moderate** | 2 | 2 affected segregations (in addition to proband; may be from a single family) |
| **Supporting** | 1 | 1 affected segregation (in addition to proband) |

**Important:** When applied together, PP1 and PP4 cannot exceed 5 Bayesian points (Supporting + Strong or Moderate + Moderate).

---

### PP2 - Missense in Constrained Gene

**Original ACMG Summary:** Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.

**VCEP Specifications:**

| Status | Comment |
|--------|---------|
| **Not Applicable** | DYSF is not constrained for missense variation (Z-score <3). |

---

### PP3 - Computational Evidence

**Original ACMG Summary:** Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).

**Caveat:** As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.

**VCEP Specifications:**

| Strength | Default Points | Criteria |
|----------|----------------|----------|
| **Supporting** | 1 | For missense variants: REVEL score ≥0.7. For variants that may affect splicing: SpliceAI score ≥0.5 |

**Note:** For any variant with RNA or other experimental data indicating an impact on splicing, follow the SVI Working Group's recommendations (Walker et al. 2023; PMID: 37352859). See [Appendix F](#appendix-f-experimental-splice-data-decision-tree).

---

### PP4 - Phenotype Specificity

**Original ACMG Summary:** Patient's phenotype or family history is highly specific for a disease with a single genetic etiology.

**VCEP Specifications:**

Use the PP4 table in [Appendix C](#appendix-c-pp4-phenotype-table) to determine the appropriate PP4 strength level. Apply PP4 only once, for a patient meeting the highest possible strength level.

| Strength | Default Points | Criteria |
|----------|----------------|----------|
| **Strong** | 4 | See PP4 table - requires clinical, genetic testing, AND protein expression criteria |
| **Moderate** | 2 | If PP1_Moderate is applied and the criteria for PP4_Strong are also met, a downgraded PP4_Moderate can be applied |
| **Supporting** | 1 | See PP4 table - requires clinical AND genetic testing criteria |

**Important:** When applied together, PP1 and PP4 cannot exceed 5 Bayesian points (Supporting + Strong or Moderate + Moderate).

---

### PP5 - Reputable Source

**Original ACMG Summary:** Reputable source recently reports variant as pathogenic, but the evidence is not available to the laboratory to perform an independent evaluation.

**VCEP Specifications:**

| Status | Comment |
|--------|---------|
| **Not Applicable** | This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PMID: 29543229). |

---

## Benign Criteria

### BA1 - Allele Frequency >0.3%

**Original ACMG Summary:** Allele frequency is above 5% in population databases.

**VCEP Specifications:**

| Strength | Default Points | Criteria |
|----------|----------------|----------|
| **Stand Alone** | N/A | Apply if the variant Grpmax FAF (the lower bound of the 95% CI of the maximum credible genetic ancestry group allele frequency) is **>0.003** |

**Notes:**
- This value can be taken directly from gnomAD
- Do not use data for which the variant does not pass quality control filters
- See [Appendix G](#appendix-g-benign-frequency-exceptions) for a list of variants defined as exceptions to the benign frequency rules
- Ongoing updates to this list will be available at the [LGMD VCEP webpage](https://clinicalgenome.org/affiliation/50061/)
- Variants whose frequency may not be reliable (e.g., variants that may reflect a sequencing artifact) should be critically evaluated and brought to the attention of the LGMD VCEP

---

### BS1 - Frequency Greater Than Expected

**Original ACMG Summary:** Allele frequency is greater than expected for disorder.

**VCEP Specifications:**

| Strength | Default Points | Criteria |
|----------|----------------|----------|
| **Strong** | -4 | Apply if the variant Grpmax FAF (the lower bound of the 95% CI of the maximum credible genetic ancestry group allele frequency) is **>0.001** |

**Notes:**
- This value can be taken directly from gnomAD
- Do not use data for which the variant does not pass quality control filters
- See [Appendix G](#appendix-g-benign-frequency-exceptions) for a list of variants defined as exceptions to the benign frequency rules

---

### BS2 - Observed in Healthy Adult

**Original ACMG Summary:** Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

**VCEP Specifications:**

| Status | Comment |
|--------|---------|
| **Not Applicable** | Not applicable as LGMD is characterized by variable expressivity and late onset is not uncommon. |

---

### BS3 - Functional Studies (No Effect)

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

**VCEP Specifications:**

| Status | Comment |
|--------|---------|
| **Not Applicable** | Since muscle disease mechanisms are complex, it is not feasible at this time to exclude all pathogenic functional abnormalities through available assays. |

---

### BS4 - Lack of Segregation

**Original ACMG Summary:** Lack of segregation in affected members of a family.

**Caveat:** The presence of phenocopies for common phenotypes (i.e., cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.

**VCEP Specifications:**

| Strength | Default Points | Criteria |
|----------|----------------|----------|
| **Strong** | -4 | Use as is. One affected individual (genotype-, phenotype+) is sufficient for BS4. Do not apply for genotype+, phenotype- individuals, as LGMD is characterized by variable expressivity and late onset is not uncommon. |

---

### BP1-BP7 - Benign Supporting

| Criterion | Status | Default Points | Specification |
|-----------|--------|----------------|---------------|
| **BP1** | Not Applicable | - | Not applicable as missense variants are also known to cause disease. |
| **BP2** | Supporting | -1 | Use when variant is found *in cis* with a variant classified as pathogenic or likely pathogenic using the LGMD VCEP specifications. |
| **BP3** | Not Applicable | - | Not applicable. Repetitive regions without a known function are not well described in DYSF. |
| **BP4** | Supporting | -1 | For missense variants: REVEL ≤0.1 AND SpliceAI ≤0.05. For variants that may affect splicing: SpliceAI ≤0.05. For any variant with RNA/experimental data indicating no impact on splicing, follow SVI Working Group recommendations. |
| **BP5** | Not Applicable | - | Not applicable. |
| **BP6** | Not Applicable | - | This criterion is not for use as recommended by the ClinGen SVI VCEP Review Committee (PMID: 29543229). |
| **BP7** | Strong | -4 | For any variant experimentally shown to have no splice impact, follow SVI Working Group recommendations (Walker et al. 2023; PMID: 37352859). Apply BP7_Strong if a splicing assay shows no effect on splicing and a protein impact can be ruled out. |
| **BP7** | Supporting | -1 | For splice predictions: SpliceAI ≤0.05. BP7 may be co-applied with BP4 for synonymous, UTR, and intronic variants located outside the splice donor/acceptor regions designated in Walker et al. 2023 (+6/-3 for donor; +1/-20 for acceptor). |

---

## Appendices

### Appendix A: PVS1 Decision Tree

#### Nonsense or Frameshift Variants

```
Nonsense or Frameshift
    │
    ├── Predicted to undergo NMD (Premature truncation in codons 35-2050)
    │       │
    │       └── PVS1
    │
    └── Not predicted to undergo NMD
            │
            ├── Premature truncation within the first 100 bp (codons 1-34)
            │       │
            │       └── PVS1_Moderate
            │
            └── Other cases
                    │
                    ├── Exon is present in biologically relevant transcript(s)
                    │       │
                    │       ├── Truncated/altered region is critical to protein function (none specified)
                    │       │       └── PVS1_Strong
                    │       │
                    │       └── Role of region in protein function is unknown
                    │               │
                    │               ├── LoF variants in this exon are frequent in general population
                    │               │       └── N/A
                    │               │
                    │               └── LoF variants not frequent AND exon is present
                    │                       │
                    │                       ├── Variant removes >10% of protein → PVS1_Strong
                    │                       │
                    │                       └── Variant removes <10% of protein → PVS1_Moderate
                    │
                    └── Exon is absent from biologically relevant transcript(s) → N/A
```

#### Canonical Splice Site Variants (GT-AG ±1,2)

Use SpliceAI prediction of the most likely splice effect, then determine the expected protein consequence.

**If exon skipping or cryptic splice site disrupts reading frame and is predicted to undergo NMD:** → PVS1

**If exon skipping or cryptic splice site preserves reading frame:**
- Follow the decision tree for in-frame changes
- In-frame exons (exon skipping not expected to result in NMD): 7, 8, 9, 14, 17, 19, 24, 25, 30, 32, 34, 35, 36, 37, 38, 41, 42, 43, 45, 49, 55

#### Deletion Variants (Single Exon to Full Gene)

**Single/multi-exon deletion disrupting reading frame and predicted to undergo NMD:** → PVS1

**Single/multi-exon deletion preserving reading frame:** → Follow in-frame decision tree

**Full gene deletion:** → PVS1

#### Duplication Variants (≥1 exon, completely contained within gene)

| Scenario | PVS1 Strength |
|----------|---------------|
| Proven in tandem, reading frame disrupted, NMD predicted | PVS1 |
| Proven in tandem, no/unknown impact on reading frame | N/A |
| Presumed in tandem, reading frame disrupted, NMD predicted | PVS1_Strong |
| Proven not in tandem | N/A |

#### Initiation Codon Variants

| Scenario | PVS1 Strength |
|----------|---------------|
| Different functional transcript uses alternative start codon | N/A |
| No known alternative start codon, ≥1 pathogenic variant upstream of closest potential in-frame start codon | PVS1_Moderate |
| No known alternative start codon, no pathogenic variants upstream | PVS1_Supporting |

---

### Appendix B: PM3 Point System and Examples

#### PM3 Point Table (Per Proband)

| Classification/Zygosity of Other Variant | Confirmed in Trans | Phase Unknown |
|------------------------------------------|-------------------|---------------|
| Pathogenic or Likely pathogenic variant | 1.0 | 0.5 (P) / 0.25 (LP) |
| Homozygous occurrence (max 1.0 pt) | 0.5 | N/A |
| Homozygous (downgrade to 0.25 pts for consanguinity) | 0.25 | N/A |
| Uncertain significance variant (max 0.5 pts) | 0.25 | 0 |

#### PM3 Strength Thresholds

| Total Points | Strength Level |
|--------------|----------------|
| 0.5 | PM3_Supporting |
| 1.0 | PM3 (Moderate) |
| 2.0 | PM3_Strong |
| 4.0 | PM3_Very Strong |

#### Important Notes for PM3 Application

1. Author assertions on phase, including based on allele-specific transcript expression, are acceptable.

2. For variants identified in unknown phase, PM3 points should **NOT** be awarded if:
   - The same variants were ever confirmed in cis (e.g., in a different patient in the literature)
   - gnomAD co-occurrence data predict the variants may be part of the same haplotype in at least one genetic ancestry group
   - More than 2 variants are reported in the patient, none of which can be classified as likely benign or benign

3. Any variant awarded points as likely pathogenic or pathogenic must have been classified using the LGMD VCEP specifications.

4. For any variant awarded points as VUS, benign frequency codes (BA1, BS1) cannot be applicable.

#### PM3 Co-Application Examples

**Example 1: PM3 can be awarded to both variants without circularity**

Variants A and B are observed in trans in patient X, who meets the criteria for PP4.

- Variant A is classified as LP independent of patient X observation (e.g., PVS1 + PM2_Supporting)
- Variant B is classified as LP independent of patient X observation (e.g., PS3_Moderate + PP3 + PM2_Supporting + PP4_Moderate (patient Y) + PM3 (variant C in patient Y))

In the curation of variant B: 1.0 PM3 pt can be awarded for the observation in patient X (confirmed in trans with LP variant A). With an additional 1.0 pt, PM3 can be upgraded to PM3_Strong.

In the curation of variant A: 1.0 PM3 pt can also be awarded (confirmed in trans with LP variant B).

*Note: The classification that would be reached WITHOUT counting evidence from co-observation in patient X is used when awarding PM3 points to avoid circularity.*

**Example 2: PM3 cannot be awarded to both variants without circularity**

Variants A and B are observed in trans in patient X.

- Variant A is classified as LP independent of patient X (PVS1 + PM2_Supporting)
- Variant B is classified as VUS independent of patient X (PS3_Moderate + PP3 + PM2_Supporting + PP4 (patient Y))

In the curation of variant B: 1.0 PM3 pt can be awarded (confirmed in trans with LP variant A), upgrading variant B to LP.

In the curation of variant A: PM3 cannot be awarded because variant B was classified as VUS independent of patient X, and 0.25 pts (for being in trans with VUS) is insufficient for PM3 application. However, PP4 can still be applied.

---

### Appendix C: PP4 Phenotype Table

| Criterion | Description | PP4 Supporting | PP4 Strong |
|-----------|-------------|----------------|------------|
| **Clinical¹** | Progressive limb-girdle pattern of muscle weakness observed over ≥6 mo OR clinical suspicion of LGMD | Required (Y) | Required (Y) |
| **Genetic Testing²** | 2 presumed diagnostic³ variants in DYSF, 1 of which is the variant under curation | Required (Y) | Required (Y) |
| **Protein Expression** | Reduced⁴ expression or membrane localization of full-length dysferlin in skeletal muscle (e.g., WB or IHC) or blood monocytes | Not Required (N) | Required (Y) |

**Footnotes:**

¹ May be accompanied by supporting EMG, MRI, muscle histology, elevated CK but not required.

² Screening of all exons and exon/intron boundaries of DYSF required. Screening of additional neuromuscular disease genes (e.g., through a panel) is recommended but not required.

³ If variants have not yet been curated by the LGMD VCEP, confirm they cannot be classified as LB or B (e.g., through application of BA1, BS1, and/or BP4/BP7). If phase is unknown, do not apply if the identified variants were ever confirmed in cis or if [gnomAD co-occurrence data](https://gnomad.broadinstitute.org/variant-cooccurrence) predict the variants may be part of the same haplotype in at least one genetic ancestry group.

⁴ <~30% normal; may be described as "severely" / "drastically" / "strongly" reduced or as "absent", "trace", "barely detectable" or "disease range".

**Important:** When applied together, PP1 and PP4 cannot exceed 5 Bayesian pts (Supporting + Strong or Moderate + Moderate). If PP1_Moderate is applied and the criteria for PP4_Strong are also met, a downgraded PP4_Moderate can be applied.

---

### Appendix D: PS3/BS3 Approved Functional Assays

#### Membrane Localization Assay (Tominaga et al. 2022)

| Parameter | Description |
|-----------|-------------|
| **PMID** | 35028538 |
| **DOI** | 10.1016/j.isci.2021.103667 |
| **Author/Year** | Tominaga, 2022 |
| **Assay Description** | In vitro cell-based assay of membrane localization based on flow cytometry and immunofluorescence |
| **Material** | Patient variants cloned into bicistronic expression vector system and transfected into HEK293T cells |
| **Readout Type** | Quantitative (flow cytometry-based 2A assay); Qualitative (fluorescence immunocytochemistry assay) |
| **Readout Description** | Cell surface expression of variant dysferlin protein relative to wild-type (WT) dysferlin protein, determined via flow cytometry (2A assay); plasma membrane localization of variant dysferlin based on immunofluorescence staining |
| **Biological Replicates** | Met |
| **Technical Replicates** | Met; triplicate |
| **Positive Control** | Met; WT cDNA |
| **Negative Control** | Met; L1341P |
| **Validation Controls (P/LP)** | 3 validated by VCEP |
| **Validation Controls (B/LB)** | 9 validated by VCEP |
| **Threshold for Normal** | Membrane localization functional score ≥0.25 on 2A assay |
| **Threshold for Abnormal** | Membrane localization functional score <0.25 on 2A assay AND concordant immunocytochemistry assay result |
| **Approved Strength** | PS3_Moderate; BS3 not applied |

#### Variant-Specific Animal Models

Animal models may be assessed on a case-by-case basis. Criteria for each strength level:

**PS3 (Strong):** All of the following must be met:
- Signs of myopathy or dystrophy present in skeletal muscle
- Effect on gene or protein function demonstrated (e.g., decreased protein expression, impaired membrane localization, or other functional abnormality)
- Behavioral signs of muscle weakness
- Progression over time

**PS3_Moderate:** The following must be met:
- Signs of myopathy or dystrophy present in skeletal muscle
- Effect on gene or protein function demonstrated

---

### Appendix E: PS1 Splicing Code Weights

**Table: PS1 code weights for variants with same predicted splicing event as a known (likely) pathogenic variant**

| Variant Under Assessment (VUA) | Baseline Computational/Predictive Code Applicable to VUA | Position of Comparison Variant Relative to VUA | PS1 Code with P Comparison Variant | PS1 Code with LP Comparison Variant |
|--------------------------------|----------------------------------------------------------|------------------------------------------------|-----------------------------------|-------------------------------------|
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
- Designated donor and acceptor motif ranges should be based on position weight matrices for intron category (see methods)
- For GT-AG introns: donor motif = last 3 bases of exon and 6 nucleotides of intronic sequence adjacent to the exon; acceptor motif = first base of the exon and 20 nucleotides upstream from the exon boundary
- Consider other motif ranges for non-GT-AG introns
- If relevant, splicing assay data for a pathogenic variant outside a ±1,2 dinucleotide position may be used to update a PVS1 decision tree and hence the applicable PVS1 code for a ±1,2 dinucleotide variant

---

### Appendix F: Experimental Splice Data Decision Tree

#### Overview

Categorization of splicing data need to consider multiple factors, including assay technique, RNA source, and gene-specific knowledge.

#### Decision Flow

1. **RNA/Splicing Data Available?**
   - If NO → No variant-specific observed impact → N/A
   - If YES → Proceed to categorization

2. **Variant Type:**
   - **Silent/Intronic variants:**
     - BP7_S (RNA) applied → Consider splicing predictive data
     - Can the protein impact be ruled out (based on functional and/or clinical data)?
       - YES → BP7_S (RNA) + prediction (PP3/BP4)
       - NO → Document as "BP7_S (RNA) Not Met" to indicate that data was present and reviewed

   - **Other variants:**
     - Assess pathogenicity using protein pathway
     - If variant-specific impact observed (compared to controls) → Follow PVS1 flowchart for OBSERVED RNA impact for your gene
     - PVS1_Strength assigned to at least 1 transcript

3. **Proportion of Alternative Transcripts (inferred to be) Produced by Variant Allele:**
   - If background rate is considered to be at low-moderate levels suggestive of being tolerated, consider reducing PVS1 (RNA) codes by an additional level

   | Proportion | Action |
   |------------|--------|
   | Complete | Keep strength level |
   | Near complete | Reduce strength by 1 level |
   | Incomplete | Do not apply codes |

4. **Final Determination:**
   - Determine PVS1 (RNA) weight from combined analysis (PP3/BP4 not applicable)
   - If PVS1 (RNA) or BP7_S (RNA) not applicable → reconsider PVS1 decision tree as appropriate

---

### Appendix G: Benign Frequency Exceptions

The following variants are defined as exceptions to the benign frequency rules (BA1/BS1):

| Variant | Status | Comment |
|---------|--------|---------|
| NM_003494.3(DYSF):c.2643+1G>A | BS1 exception | Common pathogenic variant |

**Note:** Ongoing updates to this list will be available at the [LGMD VCEP webpage](https://clinicalgenome.org/affiliation/50061/).

---

### Appendix H: Population Frequency Thresholds Summary

| Criterion | Threshold | Strength | Database | Notes |
|-----------|-----------|----------|----------|-------|
| **BA1** | Grpmax FAF >0.003 | Stand Alone | gnomAD | Lower bound of 95% CI |
| **BS1** | Grpmax FAF >0.001 | Strong | gnomAD | Lower bound of 95% CI |
| **PM2** | Grpmax VAF or 95% CI upper bound <0.0001 | Supporting | gnomAD | Use VAF if ≤2 alleles; use 95% CI upper bound if ≥3 alleles |

**Grpmax Notes:**
- Use large, non-bottlenecked genetic ancestry groups
- **Avoid:** Amish, Ashkenazi Jewish, European Finnish, Remaining Individuals groups, and genomes-only Middle Eastern data
- Use the gnomAD version with the largest allele number
- Do not use data that does not pass quality control filters

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 2.0.0 | 7/9/2025 | Bayesian adaptation; Corrections to PVS1 flowchart in-frame exons; Clarifications on experimental RNA/splice data usage; Clarifications on gnomAD population frequency data; Reduced weighting of de novo observation; Updated PM5 guidance |

---

## References

- Richards S, et al. Standards and guidelines for the interpretation of sequence variants. Genet Med. 2015;17(5):405-424. (PMID: 25741868)
- Tavtigian SV, et al. Modeling the ACMG/AMP variant classification guidelines as a Bayesian classification framework. Genet Med. 2018;20(9):1054-1060.
- Brnich SE, et al. Recommendations for application of the functional evidence PS3/BS3 criterion using the ACMG/AMP sequence variant interpretation framework. Genome Med. 2020;12(1):3. (PMID: 31892348)
- Walker LC, et al. Using the ACMG/AMP framework to capture evidence related to predicted and observed impact on splicing: Recommendations from the ClinGen SVI Splicing Subgroup. Am J Hum Genet. 2023;110(7):1046-1067. (PMID: 37352859)
- Tominaga K, et al. A flow cytometric-based functional dysferlin assay for clinical classification of dysferlinopathy. iScience. 2022;25(1):103667. (PMID: 35028538)
- Brogna S, Wen J. Nonsense-mediated mRNA decay (NMD) mechanisms. Nat Struct Mol Biol. 2009;16(2):107-113.

---

*This document was compiled from ClinGen VCEP specifications and ClinGen SVI recommendations. For the most current version, please refer to the [ClinGen website](https://clinicalgenome.org/affiliation/50061/).*
