# ClinGen Limb Girdle Muscular Dystrophy VCEP Variant Interpretation Guidelines for ANO5

**Version:** 2.0.0
**Released:** 7/9/2025
**Affiliation:** Limb Girdle Muscular Dystrophy VCEP
**Type:** Tavtigian et al., 2020 - Bayesian adaptation of Richards et al., 2015

---

## Gene Information

| Attribute | Value |
|-----------|-------|
| **Gene** | ANO5 (HGNC:27337) |
| **HGNC Name** | anoctamin 5 |
| **Transcript** | NM_213599.3 |
| **Disease** | Autosomal recessive limb-girdle muscular dystrophy (MONDO:0015152) |
| **Inheritance** | Autosomal recessive inheritance |

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
- Beware of genes where LOF is not a known disease mechanism (e.g., GFAP, MYH7)
- Use caution interpreting LOF variants at the extreme 3' end of a gene
- Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact
- Use caution in the presence of multiple transcripts

**VCEP Specifications:**

Please see attached ANO5 PVS1 flowchart (Appendix A). In addition, for any variant with RNA/splicing data, follow the SVI Working Group's recommendations (Walker et al. 2023; PMID: 37352859). See Appendix B for experimental splice data guidance.

#### Strength Levels

| Strength | Default Points | Criteria |
|----------|---------------|----------|
| **Very Strong** | 8 | Follow ANO5 PVS1 flowchart for null variants predicted to undergo NMD |
| **Strong** | 4 | Follow ANO5 PVS1 flowchart for variants meeting Strong criteria |
| **Moderate** | 2 | Follow ANO5 PVS1 flowchart for variants meeting Moderate criteria |
| **Supporting** | 1 | Follow ANO5 PVS1 flowchart for variants meeting Supporting criteria |

#### PVS1 Decision Tree for ANO5

**Nonsense or Frameshift:**
- **Predicted to undergo NMD** (Premature truncation in codons 35-840): **PVS1**
- **Not predicted to undergo NMD:**
  - Premature truncation within the first 100 bp (codons 1-34): **PVS1_Moderate**
  - Exon present in biologically relevant transcript(s) (NM_213599.3):
    - Truncated/altered region is critical to protein function: **PVS1_Strong**
    - Role of region in protein function is unknown:
      - Variant removes >10% of protein: **PVS1_Strong**
      - Variant removes <10% of protein: **PVS1_Moderate**
  - LoF variants in this exon are frequent in the general population and/or exon is absent from biologically relevant transcript(s): **N/A**

**Canonical Splice Sites (GT-AG +1,2 positions):**

Use SpliceAI prediction of the most likely splice effect and determine expected protein consequence (https://spliceailookup.broadinstitute.org)

- **Exon skipping or cryptic splice site disrupts reading frame and is predicted to undergo NMD:**
  - Exon present in biologically relevant transcript(s): **PVS1**
  - Exon absent from biologically relevant transcript(s): **N/A**

- **Exon skipping or cryptic splice site preserves reading frame:**
  - In-frame exons where skipping is not expected to result in NMD: 3, 4, 5, 6, 7, 8, 10, 14, 22
  - Truncated/altered region is critical to protein function: **PVS1_Strong**
  - Role of region in protein function is unknown:
    - LoF variants in this exon are frequent in the general population and/or exon is absent: **N/A**
    - LoF variants not frequent and exon present in biologically relevant transcript(s):
      - Variant removes >10% of protein: **PVS1_Strong**
      - Variant removes <10% of protein: **PVS1_Moderate**

- **Exon skipping or cryptic splice site disrupts reading frame and is NOT predicted to undergo NMD:** Follow same logic as above for protein impact assessment

**Deletion (Single exon to full gene):**
- **Single to multi exon deletion - Disrupts reading frame and predicted to undergo NMD:**
  - Exon present in biologically relevant transcript(s): **PVS1**
  - Exon absent: **N/A**
- **Single to multi exon deletion - Preserves reading frame:** Follow same criteria as splice variants
- **Single to multi exon deletion - Disrupts reading frame and NOT predicted to undergo NMD:** Follow criteria based on protein impact
- **Full gene deletion:** **PVS1**

**Duplication (>=1 exon in size, must be completely contained within gene):**
- **Proven in tandem:**
  - Reading frame disrupted and NMD predicted to occur: **PVS1**
  - No or unknown impact on reading frame and NMD predicted to occur: **N/A**
- **Presumed in tandem:**
  - Reading frame presumed disrupted and NMD predicted to occur: **PVS1_Strong**
- **Proven not in tandem:** **N/A**

**Initiation Codon:**
- Different functional transcript uses alternative start codon: **N/A**
- No known alternative start codon in other transcripts:
  - >=1 pathogenic variant(s) upstream of closest potential in-frame start codon: **PVS1_Moderate**
  - No pathogenic variant(s) upstream of closest potential in-frame start codon: **PVS1_Supporting**

---

### PS1 - Same Amino Acid Change

**Original ACMG Summary:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.

**Caveat:** Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:**

#### For Missense Variants (amino acid change is the expected mechanism):

| Strength | Default Points | Criteria |
|----------|---------------|----------|
| **Strong** | 4 | Apply for 1 pathogenic OR 2 likely pathogenic variants resulting in the same amino acid change |
| **Moderate** | 2 | Apply for 1 likely pathogenic variant resulting in the same amino acid change |

**Requirements:**
- The likely pathogenic or pathogenic variant(s) must have been classified using LGMD VCEP specifications
- Potential splice effects must be excluded for the missense variant under curation AND the variant(s) resulting in the same amino acid change (SpliceAI score <=0.10 or experimental evidence of normal splicing)
- PS1 can potentially be applied to multiple nucleotide changes at the same residue as long as the variant classification that determines the strength level does not depend on PS1 application
- For missense variants encoded by the first or last 3 nucleotides of an exon, PS1 should be considered only in the context of altered splicing (see below), unless a splice effect has been experimentally ruled out

#### For Variants with Altered Splicing as Expected Mechanism:

Follow SVI Working Group recommendations (Walker et al. 2023; PMID: 37352859), as outlined in Appendix C (PS1 splicing).

| Strength | Default Points | Criteria |
|----------|---------------|----------|
| **Strong** | 4 | See PS1 splicing table |
| **Moderate** | 2 | See PS1 splicing table |
| **Supporting** | 1 | See PS1 splicing table |

---

### PS2 - De Novo (Confirmed)

**Original ACMG Summary:** De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.

**Note:** Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.

**VCEP Specifications:**

| Strength | Default Points | Criteria |
|----------|---------------|----------|
| **Supporting** | 1 | Apply for confirmed de novo occurrence in a proband meeting the criteria for PP4 (Supporting). Maternity and paternity should be confirmed by trio WES/WGS or other testing. |

---

### PS3 - Functional Studies

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.

**Note:** Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.

**VCEP Specifications:**

| Strength | Default Points | Criteria |
|----------|---------------|----------|
| **Strong** | 4 | Variant-specific animal model meeting ALL conditions: signs of myopathy or dystrophy in skeletal muscle; effect on gene/protein function demonstrated; behavioral signs of muscle weakness; progression over time |
| **Moderate** | 2 | Variant-specific animal model meeting ALL conditions: signs of myopathy or dystrophy in skeletal muscle; effect on gene/protein function demonstrated |
| **Supporting** | 1 | Not applicable for in vitro assays at this time |

**Important Notes:**
- For ANO5, functional studies in heterologous systems are hard to conduct and rare in the literature. Therefore, PS3 is **not applicable** at this time for *in vitro* assays for variants in ANO5
- For any variant type, experimental evidence for altered splicing should be scored under PVS1 in accordance with the decision tree for RNA splicing assay results outlined in Walker et al. 2023 (PMID: 37352859)
- Apply PS3 only once, for the piece of evidence that meets the highest possible strength level

---

### PS4 - Prevalence in Affected

**Original ACMG Summary:** The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.

**Note 1:** Relative risk (RR) or odds ratio (OR), as obtained from case-control studies, is >5.0 and the confidence interval around the estimate of RR or OR does not include 1.0.

**Note 2:** In instances of very rare variants where case-control studies may not reach statistical significance, the prior observation of the variant in multiple unrelated patients with the same phenotype, and its absence in controls, may be used as moderate level of evidence.

**VCEP Specifications:**

| Strength | Default Points | Criteria |
|----------|---------------|----------|
| **Strong** | 4 | Use without disease-specific modification if case-control studies are available |

**Notes:**
- While case-control studies could potentially be considered for a few pathogenic variants with high minor allele frequency, the VCEP is unaware of any such studies being conducted for ANO5
- Any case-control study would require careful selection of an appropriate control population given the potential for late onset and mild disease

---

### PM1 - Mutational Hot Spot

**Original ACMG Summary:** Located in a mutational hot spot and/or critical and well-established functional domain (e.g., active site of an enzyme) without benign variation.

**VCEP Specifications:** **Not Applicable** at this time.

---

### PM2 - Absent from Controls

**Original ACMG Summary:** Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

**Caveat:** Population data for indels may be poorly called by next generation sequencing.

**VCEP Specification (Supporting only):**

| Strength | Default Points | Criteria |
|----------|---------------|----------|
| **Supporting** | 1 | Apply if the Grpmax variant allele frequency / upper bound of the 95% CI of the Grpmax variant allele frequency in gnomAD is **<0.0001** |

**Requirements:**
- Do not use data for which the variant does not pass quality control filters
- If only 1 or 2 variant alleles are present in the Grpmax population, use the Grpmax variant allele frequency
- If at least 3 variant alleles are present in the Grpmax population, use the upper bound of the 95% confidence interval (95% CI) of the Grpmax variant allele frequency
- Grpmax refers to the gnomAD subpopulation with the highest variant allele frequency
- **Avoid using:** Amish, Ashkenazi Jewish, European Finnish, and Remaining Individuals groups as well as the genomes-only data for the Middle Eastern group
- The upper bound of the 95% CI must be calculated using variant allele numbers and counts from gnomAD. Confidence interval tools, such as Confit-de-MAF (https://www.genecalculators.net/confit-de-maf.html), can be used
- Use the gnomAD version with the largest allele number
- For larger deletions or duplications that may not be well represented in gnomAD (e.g., single- or multi-exon events), also confirm the variant is not common in gnomAD SVs, gnomAD CNVs, or the Database of Genomic Variants (DGV) (https://dgv.tcag.ca/dgv/app/home)

---

### PM3 - In Trans with Pathogenic

**Original ACMG Summary:** For recessive disorders, detected in trans with a pathogenic variant.

**Note:** This requires testing of parents (or offspring) to determine phase.

**VCEP Specifications:**

Use the SVI Working Group's recommended point system to determine PM3 strength.

#### PM3 Point System (Per Proband)

| Classification/Zygosity of Other Variant | Confirmed in Trans | Phase Unknown |
|------------------------------------------|-------------------|---------------|
| Pathogenic or Likely pathogenic variant | 1.0 | 0.5 (P) / 0.25 (LP) |
| Homozygous occurrence (Max 1.0 pt; Downgrade to 0.25 pts for consanguinity) | 0.5 | N/A |
| Uncertain significance variant (Max 0.5 pts) | 0.25 | 0 |

#### PM3 Evidence Strength Thresholds

| Total Points | Strength Level | Default Points |
|--------------|----------------|----------------|
| >=0.5 but <1 | PM3_Supporting | 1 |
| >=1 but <2 | PM3 (Moderate) | 2 |
| >=2 but <4 | PM3_Strong | 4 |
| >=4 | PM3_Very Strong | 8 |

#### PM3 Footnotes

1. Author assertions on phase, including based on allele-specific transcript expression, are acceptable
2. For variants identified in unknown phase, PM3 points should **NOT** be awarded under the following circumstances:
   - The same variants were ever confirmed in cis (e.g., in a different patient in the literature)
   - gnomAD co-occurrence data (https://gnomad.broadinstitute.org/variant-cooccurrence) predict the variants may be part of the same haplotype in at least one genetic ancestry group
   - More than 2 variants are reported in the patient, none of which can be classified as likely benign or benign
3. Any variant awarded points as likely pathogenic or pathogenic must have been classified using the LGMD VCEP specifications
4. For any variant awarded points as VUS, benign frequency codes (BA1, BS1) cannot be applicable

**Note:** It is possible to award PM3 points to both variants identified in an individual as long as the evidence related to their co-observation in that individual does not contribute to the variant classification that determines the number of points applied. This excludes all evidence derived from the co-observation, including inter-dependent PM3 points (pathogenicity of variant in trans/unknown phase), PP1 (genotype-phenotype co-segregation), and PP4 (phenotype specificity). See Appendix D for examples.

---

### PM4 - Protein Length Changes

**Original ACMG Summary:** Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

**VCEP Specifications:**

| Strength | Default Points | Criteria |
|----------|---------------|----------|
| **Moderate** | 2 | Use as is, regardless of the length of the in-frame insertion or deletion |

---

### PM5 - Novel Missense at Same Residue

**Original ACMG Summary:** Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.

**Caveat:** Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:**

| Strength | Default Points | Criteria |
|----------|---------------|----------|
| **Strong** | 4 | 2 pathogenic OR 3 likely pathogenic variants resulting in different amino acid changes at the same residue |
| **Moderate** | 2 | 1 pathogenic OR 2 likely pathogenic variants resulting in different amino acid changes at the same residue |
| **Supporting** | 1 | 1 likely pathogenic variant resulting in a different amino acid change at the same residue |

**Requirements:**
- Apply only for missense variants for which the amino acid change is the expected mechanism of disease
- For the missense variant under curation and the variant(s) resulting in a different amino acid change, exclude likely splice effects (SpliceAI score <0.5 or experimental evidence of normal splicing)
- The REVEL score for the missense variant under curation should be >0.7
- Missense changes at the same residue must be classified according to LGMD VCEP specifications
- No benign missense variation should be present at the residue
- Do not apply for missense variants encoded by the first or last 3 nucleotides of an exon unless a splice effect has been ruled out for the variant under curation and the variant(s) resulting in the same amino acid change
- PM5 can potentially be applied to multiple amino acid changes at the same residue as long as the variant classification that determines the strength level does not depend on PM5 application

---

### PM6 - De Novo (Assumed)

**Original ACMG Summary:** Assumed de novo, but without confirmation of paternity and maternity.

**VCEP Specifications:** **Not Applicable.** See PS2.

---

### PP1 - Co-segregation

**Original ACMG Summary:** Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.

**Note:** May be used as stronger evidence with increasing segregation data.

**VCEP Specifications:**

Segregations should be counted across families, with the total number of segregations determining the strength level.

| Strength | Default Points | Criteria |
|----------|---------------|----------|
| **Strong** | 4 | 3 affected segregations (in addition to proband) across >=2 families |
| **Moderate** | 2 | 2 affected segregations (in addition to proband; may be from a single family) |
| **Supporting** | 1 | 1 affected segregation (in addition to proband) |

**Important:** When applied together, PP1 and PP4 cannot exceed 5 Bayesian pts (Supporting + Strong or Moderate + Moderate).

---

### PP2 - Missense in Constrained Gene

**Original ACMG Summary:** Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.

**VCEP Specifications:** **Not Applicable.** ANO5 is not constrained for missense variation (Z-score <3).

---

### PP3 - Computational Evidence

**Original ACMG Summary:** Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).

**Caveat:** As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.

**VCEP Specifications:**

| Strength | Default Points | Criteria |
|----------|---------------|----------|
| **Supporting** | 1 | For missense variants: REVEL score >=0.7. For variants that may affect splicing: SpliceAI score >=0.5 |

**Note:** For any variant with RNA or other experimental data indicating an impact on splicing, follow the SVI Working Group's recommendations (Walker et al. 2023; PMID: 37352859). See Appendix B for experimental splice data guidance.

---

### PP4 - Phenotype Specificity

**Original ACMG Summary:** Patient's phenotype or family history is highly specific for a disease with a single genetic etiology.

**VCEP Specifications:**

| Strength | Default Points | Criteria |
|----------|---------------|----------|
| **Supporting** | 1 | Apply for a proband meeting BOTH criteria below |

**Criteria for PP4 (Supporting):**

1. Progressive limb-girdle pattern of muscle weakness observed over >=6 months OR clinical suspicion of LGMD
   - May be accompanied by supporting EMG, MRI, muscle histology, elevated CK but not required

2. 2 presumed diagnostic variants in ANO5, 1 of which is the variant under curation
   - Screening of all exons and exon/intron boundaries of ANO5 required
   - Screening of additional neuromuscular disease genes (e.g., through a panel) is recommended but not required
   - If variants have not yet been curated by the LGMD VCEP, confirm they cannot be classified as LB or B (e.g., through application of BA1, BS1, and/or BP4/BP7)
   - If phase is unknown, do not apply if the identified variants were ever confirmed in cis or if gnomAD co-occurrence data (https://gnomad.broadinstitute.org/variant-cooccurrence) predict the variants may be part of the same haplotype in at least one genetic ancestry group

---

### PP5 - Reputable Source

**Original ACMG Summary:** Reputable source recently reports variant as pathogenic, but the evidence is not available to the laboratory to perform an independent evaluation.

**VCEP Specifications:** **Not Applicable.** This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee. (PMID: 29543229)

---

## Benign Criteria

### BA1 - Allele Frequency >5%

**Original ACMG Summary:** Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

**VCEP Specification (Stand Alone):**

Apply if the variant **Grpmax FAF** (the lower bound of the 95% confidence interval of the maximum credible genetic ancestry group allele frequency) is **>0.003**.

- This value can be taken directly from gnomAD
- Do not use data for which the variant does not pass quality control filters
- See Appendix E for a list of variants defined as exceptions to the benign frequency rules
- Ongoing updates to this list will be available at the LGMD VCEP webpage: https://clinicalgenome.org/affiliation/50061/
- Variants whose frequency may not be reliable (e.g., variants that may reflect a sequencing artifact) should be critically evaluated and brought to the attention of the LGMD VCEP

---

### BS1 - Frequency Greater Than Expected

**Original ACMG Summary:** Allele frequency is greater than expected for disorder.

**VCEP Specification (Strong):**

| Strength | Default Points | Criteria |
|----------|---------------|----------|
| **Strong** | -4 | Apply if the variant Grpmax FAF is **>0.001** |

- This value can be taken directly from gnomAD
- Do not use data for which the variant does not pass quality control filters
- See Appendix E for a list of variants defined as exceptions to the benign frequency rules

---

### BS2 - Observed in Healthy Adult

**Original ACMG Summary:** Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

**VCEP Specifications:** **Not Applicable.** LGMD is characterized by variable expressivity and late-onset LGMD is not uncommon.

---

### BS3 - Functional Studies (No Effect)

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

**VCEP Specifications:** **Not Applicable.** Since the muscle disease mechanisms are complex, it is not feasible at this time to exclude all pathogenic functional abnormalities through available assays.

---

### BS4 - Lack of Segregation

**Original ACMG Summary:** Lack of segregation in affected members of a family.

**Caveat:** The presence of phenocopies for common phenotypes (i.e., cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.

**VCEP Specifications:**

| Strength | Default Points | Criteria |
|----------|---------------|----------|
| **Strong** | -4 | Use as is. One affected individual (genotype-, phenotype+) is sufficient for BS4. Do not apply for genotype+, phenotype- individuals, as LGMD is characterized by variable expressivity and late onset is not uncommon. |

---

### BP1-BP7 - Benign Supporting

| Criterion | Status | Default Points | Specification |
|-----------|--------|----------------|---------------|
| **BP1** | Not Applicable | N/A | Not applicable as missense variants are also known to cause disease |
| **BP2** | Applicable | -1 | Use when variant is found *in cis* with a variant classified as pathogenic or likely pathogenic using the LGMD VCEP specifications |
| **BP3** | Not Applicable | N/A | Repetitive regions without a known function are not well described in ANO5 |
| **BP4** | Applicable | -1 | For missense variants: REVEL score <=0.1 **AND** SpliceAI score <=0.05. For variants that may affect splicing: SpliceAI score <=0.05 |
| **BP5** | Not Applicable | N/A | Not applicable |
| **BP6** | Not Applicable | N/A | Not for use as recommended by ClinGen SVI VCEP Review Committee (PMID: 29543229) |
| **BP7** | Applicable (Supporting & Strong) | -1 or -4 | See below |

#### BP7 Specifications

| Strength | Default Points | Criteria |
|----------|---------------|----------|
| **Strong** | -4 | For any variant experimentally shown to have no splice impact, follow SVI Working Group's recommendations (Walker et al. 2023; PMID: 37352859). Apply BP7_Strong if a splicing assay shows no effect on splicing and a protein impact can be ruled out |
| **Supporting** | -1 | For splice predictions: SpliceAI score <=0.05. BP7 may be co-applied with BP4 for synonymous, UTR, and intronic variants located outside the splice donor/acceptor regions designated in Walker et al. 2023 (+6/-3 for donor; +1/-20 for acceptor) |

---

## Rules for Combining Criteria

### Point-Based Classification System

| Category | Point Range |
|----------|-------------|
| Pathogenic | >=10 |
| Likely Pathogenic | 6 - 9 |
| Uncertain Significance | 0 - 5 |
| Likely Benign | -6 to -1 |
| Benign | <=-7 OR BA1 applies |

**Additional Note:** A Benign classification can also be assigned when BA1 applies.

### Default Point Values Summary

| Criterion | Supporting | Moderate | Strong | Very Strong | Stand Alone |
|-----------|------------|----------|--------|-------------|-------------|
| PVS1 | 1 | 2 | 4 | 8 | - |
| PS1 | 1 | 2 | 4 | - | - |
| PS2 | 1 | - | - | - | - |
| PS3 | 1 | 2 | 4 | - | - |
| PS4 | - | - | 4 | - | - |
| PM1 | N/A | N/A | N/A | N/A | N/A |
| PM2 | 1 | - | - | - | - |
| PM3 | 1 | 2 | 4 | 8 | - |
| PM4 | - | 2 | - | - | - |
| PM5 | 1 | 2 | 4 | - | - |
| PM6 | N/A | N/A | N/A | N/A | N/A |
| PP1 | 1 | 2 | 4 | - | - |
| PP2 | N/A | N/A | N/A | N/A | N/A |
| PP3 | 1 | - | - | - | - |
| PP4 | 1 | - | - | - | - |
| PP5 | N/A | N/A | N/A | N/A | N/A |
| BA1 | - | - | - | - | Yes |
| BS1 | - | - | -4 | - | - |
| BS2 | N/A | N/A | N/A | N/A | N/A |
| BS3 | N/A | N/A | N/A | N/A | N/A |
| BS4 | - | - | -4 | - | - |
| BP1 | N/A | N/A | N/A | N/A | N/A |
| BP2 | -1 | - | - | - | - |
| BP3 | N/A | N/A | N/A | N/A | N/A |
| BP4 | -1 | - | - | - | - |
| BP5 | N/A | N/A | N/A | N/A | N/A |
| BP6 | N/A | N/A | N/A | N/A | N/A |
| BP7 | -1 | - | -4 | - | - |

---

## Appendices

### Appendix A: PVS1 Flowchart for ANO5

The PVS1 decision tree for ANO5 follows the general structure outlined in the Criteria Specifications section above. Key gene-specific considerations:

**Biologically Relevant Transcript:** NM_213599.3

**In-frame Exons (where exon skipping is not expected to result in NMD):** 3, 4, 5, 6, 7, 8, 10, 14, 22

**NMD Prediction:**
- Premature truncation in codons 35-840: Predicted to undergo NMD
- Premature truncation in codons 1-34 (first 100 bp): Not predicted to undergo NMD

**Critical Regions:** None specified

---

### Appendix B: Experimental Splice Data Guidance

For any variant with RNA/splicing data, follow the SVI Working Group's recommendations (Walker et al. 2023; PMID: 37352859).

**Categorization of splicing data needs to consider multiple factors, including assay/technique, RNA source, and gene-specific knowledge.**

**Decision Pathway:**

1. **No variant-specific observed impact (Silent/Intronic):** BP7_S (RNA) applied
2. **Other variants with no variant-specific observed impact:** Assess pathogenicity using protein pathway
3. **Variant-specific impact (compared to controls):** Follow PVS1 flowchart for observed RNA impact for your gene

**When RNA Data Shows Impact:**

| Proportion of alternative transcript(s) (inferred to be) produced by variant allele | Strength Adjustment |
|-----------------------------------------------------------------------------------|---------------------|
| Complete | Keep strength level |
| Near complete | Reduce strength by 1 level |
| Incomplete | Do not apply codes |

*If background rate is considered to be at low/moderate levels suggestive of being tolerated, consider reducing PVS1 (RNA) codes by an additional level.*

**After RNA Analysis:**
- Determine PVS1 (RNA) weight from combined analysis (PP3/BP4 not applicable)
- Consider splicing predictive data for final determination
- If protein impact can be ruled out (based on functional and/or clinical data): BP7_S (RNA) + prediction (PP3/BP4)
- If protein impact cannot be ruled out: Document as "BP7_S (RNA)? Not Met to indicate that data was present and reviewed"

---

### Appendix C: PS1 Splicing Code Weights

**Table: PS1 code weights for variants with same predicted splicing event as a known (likely) pathogenic variant**

| Variant under assessment (VUA) | Baseline computational/predictive code applicable to VUA | Position of comparison variant relative to VUA | PS1 code with P comparison variant | PS1 code with LP comparison variant |
|--------------------------------|----------------------------------------------------------|------------------------------------------------|-----------------------------------|-------------------------------------|
| Located outside splice donor/acceptor +/-1,2 dinucleotide positions | PP3 | same nucleotide | PS1 | PS1_Moderate |
| Located outside splice donor/acceptor +/-1,2 dinucleotide positions | PP3 | within same splice donor/acceptor motif (including at +/-1,2 positions) | PS1_Moderate | PS1_Supporting |
| Located at splice donor/acceptor +/-1,2 dinucleotide positions | PVS1 | within same splice donor/acceptor +/-1,2 dinucleotide | PS1_Supporting | N/A |
| Located at splice donor/acceptor +/-1,2 dinucleotide positions | PVS1 | within same splice donor/acceptor region, but outside +/-1,2 dinucleotide | PS1_Supporting | PS1_Supporting |
| Located at splice donor/acceptor +/-1,2 dinucleotide positions | PVS1_Strong, PVS1_Moderate, or PVS1_Supporting | within same splice donor/acceptor +/-1,2 dinucleotide | PS1 | N/A |
| Located at splice donor/acceptor +/-1,2 dinucleotide positions | PVS1_Strong, PVS1_Moderate, or PVS1_Supporting | within same splice donor/acceptor motif, but outside +/-1,2 dinucleotide | PS1_Moderate | PS1_Supporting |

**Prerequisites:**
- The predicted event of the VUA must precisely match the predicted event of the comparison (likely) pathogenic variant (e.g., both predicted to lead to exon skipping, or both to lead to enhanced use of a cryptic splice motif)
- The strength of the prediction for the VUA must be of similar or higher strength than the strength of the prediction for the comparison [likely] pathogenic variant
- For an exonic variant, predicted or proven functional effect of missense substitution(s) encoded by the VUA and (likely) pathogenic variant should also be considered before application of this code
- Dinucleotide positions refer to donor and acceptor dinucleotides in reference transcript(s) used for curation
- Designated donor and acceptor motif ranges should be based on position weight matrices for intron category. For GT-AG introns these are defined as follows: the donor motif, last 3 bases of the exon and 6 nucleotides of intronic sequence adjacent to the exon; acceptor motif, first base of the exon and 20 nucleotides upstream from the exon boundary. Consider other motif ranges for non-GT-AG introns.

*If relevant, splicing assay data for a pathogenic variant outside a +/-1,2 dinucleotide position may be used to update a PVS1 decision tree and hence the applicable PVS1 code for a +/-1,2 dinucleotide variant.*

---

### Appendix D: PM3 Co-application Examples

**It is possible to award PM3 points to both variants identified in an individual as long as the evidence related to their co-observation in that individual does not contribute to the variant classification that determines the number of points applied.** This excludes all evidence derived from the co-observation, including inter-dependent PM3 points (pathogenicity of variant in trans/unknown phase), PP1 (genotype-phenotype co-segregation), and PP4 (phenotype specificity).

#### Example 1: PM3 can be awarded to both variants in a pair without circularity

Variants A and B are observed in trans in patient X, who meets the criteria for PP4. Variant A has not been observed in any other patients. Variant B has also been observed in patient Y, where it was confirmed in trans with a pathogenic variant (variant C, 1.0 PM3 pt) in an individual meeting the criteria for PP4_Moderate.

- **Variant A** is classified as LP independent of the observation in patient X (e.g., PVS1 + PM2_Supporting)
- **Variant B** is also classified as LP independent of the observation in patient X (e.g., PS3_Moderate + PP3 + PM2_Supporting + PP4_Moderate (for patient Y) + PM3 (for variant C in patient Y))

**In the curation of variant B:** 1.0 PM3 pt can be awarded for the observation in patient X, since variant B was confirmed in trans with an LP* variant, variant A. With an additional 1.0 pt from its observation with variant A in patient X, PM3 can be upgraded to PM3_Strong, resulting in a final classification of P for variant B (PS3_Moderate + PP3 + PM2_Supporting + PP4_Moderate (patient Y) + PM3_Strong (patients X + Y)).

**In the curation of variant A:** 1.0 PM3 pt can be awarded for the observation in patient X as well, since variant A was also confirmed in trans with an LP* variant, variant B. With 1.0 pt, PM3 can be applied to variant A, resulting in a final classification of P for variant A (PVS1 + PM2_Supporting + PM3 (patient X) + PP4 (patient X)).

*While the final classification of variants A and B is P, the classification that would be reached without counting the evidence from their co-observation in patient X (in this case, PM3 points and PP4) is used when awarding PM3 points for the observation in patient X. This avoids circularity and double counting of evidence.

#### Example 2: PM3 cannot be awarded to both variants in a pair without circularity

Variants A and B are observed in trans in patient X, who meets the criteria for PP4. Variant A has not been observed in any other patients. Variant B has also been observed in patient Y, where it was observed in unknown phase with a VUS variant (variant C, 0 PM3 pts) in an individual meeting the criteria for PP4.

- **Variant A** is classified as LP independent of the observation in patient X (PVS1 + PM2_Supporting)
- **Variant B** is classified as VUS independent of the observation in patient X (e.g., PS3_Moderate + PP3 + PM2_Supporting + PP4 (for patient Y))

**In the curation of variant B:** PM3 can be awarded for the observation in patient X, since variant B was confirmed in trans with an LP* variant, variant A (1.0 PM3 pt). With the addition of PM3, variant B can be classified as LP (PS3_Moderate + PP3 + PM2_Supporting + PP4 (patient Y) + PM3 (patient X)).

**In the curation of variant A:** PM3 **cannot** be awarded for the observation in patient X, since variant B was classified as VUS independent of the observation in patient X**, and the 0.25 PM3 pts awarded for being confirmed in trans with a VUS are not sufficient for PM3 to be applied at any strength level. While PM3 cannot be applied to variant A for the observation in patient X, PP4 can, resulting in a final classification of P for variant A (PVS1 + PM2_Supporting + PP4 (patient X)).

*While the final classification of variant A is P, the classification that would be reached without counting the evidence from their co-observation in patient X is used when awarding PM3 points for the observation in patient X. This avoids circularity and double counting of evidence.

**While the final classification of variant B is LP, the classification that would be reached without counting the evidence from their co-observation in patient X is used when awarding PM3 points for the observation in patient X. This avoids circularity and double counting of evidence.

---

### Appendix E: Benign Frequency Exceptions

The following variants are defined as exceptions to the benign frequency rules (BA1, BS1):

| Variant Information | Status | Comment |
|---------------------|--------|---------|
| NM_213599.3(ANO5):c.191dup (p.Asn64LysfsTer15) | BS1 exception | Common pathogenic variant |

**Note:** Ongoing updates to this list will be available at the LGMD VCEP webpage: https://clinicalgenome.org/affiliation/50061/

---

### Appendix F: Population Frequency Thresholds Summary

| Criterion | Threshold | Strength | Notes |
|-----------|-----------|----------|-------|
| BA1 | Grpmax FAF >0.003 | Stand Alone | Use gnomAD FAF directly |
| BS1 | Grpmax FAF >0.001 | Strong | Use gnomAD FAF directly |
| PM2 | Grpmax AF or 95% CI upper bound <0.0001 | Supporting | Use Grpmax AF if <=2 alleles; use 95% CI upper bound if >=3 alleles |

**Excluded Populations for Grpmax:** Amish, Ashkenazi Jewish, European Finnish, Remaining Individuals, and genomes-only Middle Eastern data

---

### Appendix G: Computational Predictor Thresholds Summary

| Criterion | Predictor | Threshold | Direction |
|-----------|-----------|-----------|-----------|
| PP3 (missense) | REVEL | >=0.7 | Pathogenic |
| PP3 (splicing) | SpliceAI | >=0.5 | Pathogenic |
| BP4 (missense) | REVEL | <=0.1 | Benign |
| BP4 (missense) | SpliceAI | <=0.05 | Benign (required with REVEL) |
| BP4 (splicing) | SpliceAI | <=0.05 | Benign |
| BP7 | SpliceAI | <=0.05 | Benign |
| PS1/PM5 splice exclusion | SpliceAI | <=0.10 | Normal splicing |
| PM5 splice exclusion | SpliceAI | <0.5 | Normal splicing |

---

### Appendix H: Reference PMIDs

| Reference | PMID | Description |
|-----------|------|-------------|
| Richards et al., 2015 | 25741868 | ACMG/AMP Standards and Guidelines |
| Tavtigian et al., 2020 | 32720330 | Bayesian adaptation of ACMG/AMP Guidelines |
| Walker et al., 2023 | 37352859 | SVI Working Group recommendations for RNA splicing assays |
| ClinGen SVI Review | 29543229 | Recommendations on PP5/BP6 criteria |
| NMD boundary reference | 27618451 | Premature truncation within first 100 bp |

---

## Version History

| Version | Release Date | Notes |
|---------|--------------|-------|
| 2.0.0 | 7/9/2025 | Bayesian adaptation; PVS1 flowchart corrections; clarifications on RNA/splice data, gnomAD population frequency, de novo weighting, PM5 guidance |

---

*This document was compiled from ClinGen VCEP specifications for the Limb Girdle Muscular Dystrophy VCEP. For the most current version, please refer to the ClinGen website: https://clinicalgenome.org/affiliation/50061/*
