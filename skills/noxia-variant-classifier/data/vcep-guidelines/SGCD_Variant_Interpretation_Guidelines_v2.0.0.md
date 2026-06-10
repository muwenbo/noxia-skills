# ClinGen Limb Girdle Muscular Dystrophy VCEP Variant Interpretation Guidelines for SGCD

**Version:** 2.0.0
**Released:** 7/9/2025
**Affiliation:** Limb Girdle Muscular Dystrophy VCEP
**Based on:** Tavtigian et al., 2020 - Bayesian adaptation of Richards et al., 2015
**Specification Type:** Bayesian adaptation

### Release Notes (v2.0.0)
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
| **Gene** | SGCD (HGNC:10807) |
| **HGNC Name** | sarcoglycan delta |
| **Transcript** | NM_000337.6 |
| **Disease** | Autosomal recessive limb-girdle muscular dystrophy (MONDO:0015152) |
| **Inheritance** | Autosomal recessive inheritance |

---

## Point-Based Variant Classification Categories

| Category | Point Ranges |
|----------|-------------|
| Pathogenic | ≥10 |
| Likely Pathogenic | 6 – 9 |
| Uncertain Significance | 0 – 5 |
| Likely Benign | -6 – -1 |
| Benign | ≤-7 |

**Additional Notes:** A Benign classification can also be assigned when BA1 applies.

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
   - [BP1–BP7 - Benign Supporting](#bp1bp7---benign-supporting)
3. [Rules for Combining Criteria](#rules-for-combining-criteria)
4. [Appendices](#appendices)

---

## Pathogenic Criteria

### PVS1 - Null Variant

**Original ACMG Summary:** Null variant (nonsense, frameshift, canonical ±1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.

**Caveats:**
- Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7).
- Use caution interpreting LOF variants at the extreme 3' end of a gene.
- Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact.
- Use caution in the presence of multiple transcripts.

**VCEP Specifications:** Please see the attached SGCD PVS1 flowchart (Appendix A). In addition, for any variant with RNA/splicing data, follow the SVI Working Group's recommendations (Walker et al. 2023; PMID: 37352859). See supplementary file "experimental splice data".

#### Strength Levels

| Strength | Default Points | Criteria |
|----------|---------------|----------|
| **Very Strong** | 8 | See SGCD PVS1 decision tree (Appendix A) |
| **Strong** | 4 | See SGCD PVS1 decision tree (Appendix A) |
| **Moderate** | 2 | See SGCD PVS1 decision tree (Appendix A) |
| **Supporting** | 1 | See SGCD PVS1 decision tree (Appendix A) |

#### PVS1 Decision Tree for SGCD

##### Nonsense or Frameshift

1. **Predicted to undergo NMD** (premature truncation in codons 35–214):
   - → **PVS1** (Very Strong, 8 pts)

2. **Not predicted to undergo NMD:**
   - Exon is present in biologically relevant transcript(s) (NM_000337.6):
     - Truncated/altered region is critical to protein function (none specified) → **PVS1_Strong** (4 pts)
     - Role of region in protein function is unknown → **N/A**
   - Exon is absent from biologically relevant transcript(s) → **N/A**

3. **Premature truncation within the first 100 bp** (codons 1–34; PMID: 27618451):
   - → **PVS1_Supporting** (1 pt)

##### Canonical (GT-AG) ±1,2 Splice Sites

Use the SpliceAI prediction of the most likely splice effect and then determine the expected protein consequence. (https://spliceailookup.broadinstitute.org)

1. **Exon skipping or use of a cryptic splice site disrupts reading frame and is predicted to undergo NMD:**
   - → **PVS1** (Very Strong, 8 pts)

2. **Exon skipping or use of a cryptic splice site preserves reading frame:**
   - In-frame exons for which exon skipping is not expected to result in NMD: 2, 3, 4, 6, 9
   - Exon is present in biologically relevant transcript(s) (NM_000337.6):
     - Truncated/altered region is critical to protein function (none specified) → **PVS1_Strong** (4 pts)
     - Role of region in protein function is unknown:
       - LoF variants in this exon are frequent in the general population and/or exon is absent from biologically relevant transcript(s) → **N/A**
       - LoF variants in this exon are NOT frequent in the general population and exon IS present in biologically relevant transcript(s):
         - Variant removes >10% of protein → **PVS1_Strong** (4 pts)
         - Variant removes <10% of protein → **PVS1_Moderate** (2 pts)
   - Exon is absent from biologically relevant transcript(s) → **N/A**

3. **Exon skipping or use of a cryptic splice site disrupts reading frame and is NOT predicted to undergo NMD:**
   - Exon is present in biologically relevant transcript(s) (NM_000337.6):
     - Truncated/altered region is critical to protein function (none specified) → **PVS1_Strong** (4 pts)
     - Role of region in protein function is unknown:
       - LoF variants in this exon are frequent in the general population and/or exon is absent from biologically relevant transcript(s) → **N/A**
       - LoF variants in this exon are NOT frequent in the general population and exon IS present:
         - Variant removes >10% of protein → **PVS1_Strong** (4 pts)
         - Variant removes <10% of protein → **PVS1_Moderate** (2 pts)

##### Deletion (Single Exon to Full Gene)

1. **Single to multi-exon deletion — disrupts reading frame and is predicted to undergo NMD:**
   - → **PVS1** (Very Strong, 8 pts)

2. **Single to multi-exon deletion — preserves reading frame:**
   - Exon is present in biologically relevant transcript(s) (NM_000337.6):
     - Truncated/altered region is critical to protein function (none specified) → **PVS1_Strong** (4 pts)
     - Role of region in protein function is unknown:
       - LoF variants in this exon are frequent in the general population and/or exon is absent from biologically relevant transcript(s) → **N/A**
       - LoF variants in this exon are NOT frequent and exon IS present:
         - Variant removes >10% of protein → **PVS1_Strong** (4 pts)
         - Variant removes <10% of protein → **PVS1_Moderate** (2 pts)
   - Exon is absent from biologically relevant transcript(s) → **N/A**

3. **Single to multi-exon deletion — disrupts reading frame and is NOT predicted to undergo NMD:**
   - Same logic as frame-preserving deletions above (uses exon presence, functional region criticality, and variant size thresholds)

4. **Full gene deletion:**
   - → **PVS1** (Very Strong, 8 pts)

##### Duplication (≥1 Exon, Completely Contained Within Gene)

1. **Proven in tandem — reading frame disrupted and NMD predicted:**
   - → **PVS1** (Very Strong, 8 pts)

2. **Proven in tandem — no or unknown impact on reading frame and NMD predicted:**
   - → **N/A**

3. **Presumed in tandem — reading frame presumed disrupted and NMD predicted:**
   - → **PVS1_Strong** (4 pts)

4. **Proven not in tandem:**
   - → **N/A**

##### Initiation Codon Variants

1. Different functional transcript uses alternative start codon → **N/A**
2. No known alternative start codon in other transcripts:
   - ≥1 pathogenic variant(s) upstream of closest potential in-frame start codon → **PVS1_Moderate** (2 pts)
   - No pathogenic variant(s) upstream of closest potential in-frame start codon → **PVS1_Supporting** (1 pt)

---

### PS1 - Same Amino Acid Change

**Original ACMG Summary:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.

**Caveat:** Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:**

#### Strong (4 pts)

For missense variants for which the amino acid change is the expected mechanism of disease, apply at Strong for 1 pathogenic or 2 likely pathogenic variants resulting in the same amino acid change. The likely pathogenic or pathogenic variant(s) must have been classified using LGMD VCEP specifications, and potential splice effects must be excluded for the missense variant under curation and the variant(s) resulting in the same amino acid change (SpliceAI score ≤0.10 or experimental evidence of normal splicing). PS1 can potentially be applied to multiple nucleotide changes at the same residue as long as the variant classification that determines the strength level does not depend on PS1 application.

For missense variants encoded by the first or last 3 nucleotides of an exon, PS1 should be considered only in the context of altered splicing (see below), unless a splice effect has been experimentally ruled out for the variant under curation and the variant(s) resulting in the same amino acid change.

For variants for which the nucleotide change is the expected mechanism of disease (altered splicing), follow SVI Working Group recommendations (Walker et al. 2023; PMID: 37352859), as outlined in supplementary file "PS1 splicing".

#### Moderate (2 pts)

For missense variants for which the amino acid change is the expected mechanism of disease, apply at Moderate for 1 likely pathogenic variant resulting in the same amino acid change. The likely pathogenic variant must have been classified using LGMD VCEP specifications, and potential splice effects must be excluded for the missense variant under curation and the variant resulting in the same amino acid change (SpliceAI score ≤0.10 or experimental evidence of normal splicing). PS1 can potentially be applied to multiple nucleotide changes at the same residue as long as the variant classification that determines the strength level does not depend on PS1 application.

For missense variants encoded by the first or last 3 nucleotides of an exon, PS1 should be considered only in the context of altered splicing (see below), unless a splice effect has been experimentally ruled out for the variant under curation and the variant(s) resulting in the same amino acid change.

For variants for which the nucleotide change is the expected mechanism of disease (altered splicing), follow SVI Working Group recommendations (Walker et al. 2023; PMID: 37352859), as outlined in supplementary file "PS1 splicing".

#### Supporting (1 pt)

For variants for which the nucleotide change is the expected mechanism of disease (altered splicing), follow SVI Working Group recommendations (Walker et al. 2023; PMID: 37352859), as outlined in supplementary file "PS1 splicing".

#### PS1 Splicing Code Weights

**Table 2: PS1 code weights for variants with same predicted splicing event as a known (likely) pathogenic variant**

| Variant Under Assessment (VUA) | Baseline Computational/Predictive Code Applicable to VUA | Position of Comparison Variant Relative to VUA | PS1 Code with P Comparison Variant | PS1 Code with LP Comparison Variant |
|---|---|---|---|---|
| Located outside splice donor/acceptor ±1,2 dinucleotide positions | PP3 | same nucleotide | PS1 | PS1_Moderate |
| Located outside splice donor/acceptor ±1,2 dinucleotide positions | PP3 | within same splice donor/acceptor motif (including at ±1,2 positions) | PS1_Moderate | PS1_Supporting |
| Located at splice donor/acceptor ±1,2 dinucleotide positions | PVS1 | within same splice donor/acceptor ±1,2 dinucleotide | PS1_Supporting | N/A |
| Located at splice donor/acceptor ±1,2 dinucleotide positions | PP3 | within same splice donor/acceptor region, but outside ±1,2 dinucleotide* | PS1_Supporting | PS1_Supporting |
| Located at splice donor/acceptor ±1,2 dinucleotide positions | PVS1_Strong, PVS1_Moderate, or PVS1_Supporting | within same splice donor/acceptor ±1,2 dinucleotide | PS1 | N/A |
| Located at splice donor/acceptor ±1,2 dinucleotide positions | PVS1_Strong, PVS1_Moderate, or PVS1_Supporting | within same splice donor/acceptor motif, but outside ±1,2 dinucleotide* | PS1_Moderate | PS1_Supporting |

**Prerequisites:** For all: the predicted event of the VUA must precisely match the predicted event of the comparison (likely) pathogenic variant (e.g., both predicted to lead to exon skipping, or both to lead to enhanced use of a cryptic splice motif), AND the strength of the prediction for the VUA must be of similar or higher strength than the strength of the prediction for the comparison (likely) pathogenic variant. For an exonic variant, predicted or proven functional effect of missense substitution(s) encoded by the VUA and (likely) pathogenic variant should also be considered before application of this code. Dinucleotide positions refer to donor and acceptor dinucleotides in reference transcript(s) used for curation. Designated donor and acceptor motif ranges should be based on position weight matrices for intron category (see methods). For GT-AG introns these are defined as follows: the donor motif, last 3 bases of the exon and 6 nucleotides of intronic sequence adjacent to the exon; acceptor motif, first base of the exon and 20 nucleotides upstream from the exon boundary. Consider other motif ranges for non-GT-AG introns.

*If relevant, splicing assay data for a pathogenic variant outside a ±1,2 dinucleotide position may be used to update a PVS1 decision tree and hence the applicable PVS1 code for a ±1,2 dinucleotide variant.

---

### PS2 - De Novo (Confirmed)

**Original ACMG Summary:** De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.

**Note:** Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.

**VCEP Specifications:**

#### Supporting (1 pt)

Apply for confirmed *de novo* occurrence in a proband meeting the criteria for PP4 (Supporting). Maternity and paternity should be confirmed by trio WES/WGS or other testing.

> **Note:** PS2 is applied at Supporting only for SGCD due to autosomal recessive inheritance. PM6 is not applicable — see PS2.

---

### PS3 - Functional Studies

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.

**Note:** Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.

**VCEP Specifications:**

#### Strong (4 pts)

Variant-specific animal models are rare but may be assessed on a case-by-case basis and PS3 applied at a strength level that reflects how well the model recapitulates features observed in human patients. Apply PS3 at Strong for a variant-specific animal model that meets all of the following conditions, regardless of species:
- Signs of myopathy or dystrophy are present in skeletal muscle
- An effect on gene or protein function is demonstrated (e.g., decreased protein expression, impaired membrane localization, or other functional abnormality)
- Behavioral signs of muscle weakness
- Progression over time

For any variant type, experimental evidence for altered splicing should be scored under PVS1 in accordance with the decision tree for RNA splicing assay results outlined in Walker et al. 2023 (PMID: 37352859).

Apply PS3 only once, for the piece of evidence that meets the highest possible strength level.

#### Moderate (2 pts)

Variant-specific animal models are rare but may be assessed on a case-by-case basis and PS3 applied at a strength level that reflects how well the model recapitulates features observed in human patients. Apply PS3_Moderate for a variant-specific animal model that meets all of the following conditions, regardless of species:
- Signs of myopathy or dystrophy are present in skeletal muscle
- An effect on gene or protein function is demonstrated (e.g., decreased protein expression, impaired membrane localization, or other functional abnormality)

PS3_Moderate may be applied for sarcoglycan complex membrane localization assays that have been clinically validated with ≥11 control variants that meet criteria specified in Brnich et al. 2020 (PMID: 31892348) for the number of pathogenic and benign control variants. See supplementary file "PS3 assays SGCD".

For any variant type, experimental evidence for altered splicing should be scored under PVS1 in accordance with the decision tree for RNA splicing assay results outlined in Walker et al. 2023 (PMID: 37352859).

Apply PS3 only once, for the piece of evidence that meets the highest possible strength level.

#### Supporting (1 pt)

PS3_Supporting may be applied if the variant is expressed in heterologous cell lines/model organisms and shows absent membrane localization of the sarcoglycan protein complex and fewer than 11 control variants were used, in accordance with Brnich et al. 2020 (PMID: 31892348). See supplementary file "PS3 assays SGCD".

For any variant type, experimental evidence for altered splicing should be scored under PVS1 in accordance with the decision tree for RNA splicing assay results outlined in Walker et al. 2023 (PMID: 37352859).

Apply PS3 only once, for the piece of evidence that meets the highest possible strength level.

#### Approved Assay Instances

| Field | Details |
|-------|---------|
| **PMID** | 22095924 |
| **DOI** | 10.1002/humu.21659 |
| **Author** | Soheili |
| **Year** | 2012 |
| **Assay** | Membrane localization of sarcoglycan complex |
| **Material** | Vectors expressing the SGCD variant of interest transfected into HER-911 cells expressing the three other sarcoglycans |
| **Readout type** | Qualitative |
| **Readout description** | Membrane localization assessed via confocal immunofluorescence analysis of nonpermeabilized cells |
| **Biological replicates** | Not described |
| **Technical replicates** | Not described |
| **Positive control** | Met; WT |
| **Negative control** | Met; expression of α-sarcoglycan alone |
| **Validation controls P/LP** | 3; 0 validated by VCEP |
| **Validation controls B/LB** | 0 |
| **Threshold for normal** | Membrane localized |
| **Threshold for abnormal** | Absent at membrane |
| **Approved assay** | Yes |
| **Proposed strength** | PS3_Supporting; BS3 not applied |

---

### PS4 - Prevalence in Affected

**Original ACMG Summary:** The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.

**Note 1:** Relative risk (RR) or odds ratio (OR), as obtained from case-control studies, is >5.0 and the confidence interval around the estimate of RR or OR does not include 1.0.

**Note 2:** In instances of very rare variants where case-control studies may not reach statistical significance, the prior observation of the variant in multiple unrelated patients with the same phenotype, and its absence in controls, may be used as moderate level of evidence.

**VCEP Specifications:**

#### Strong (4 pts)

Use without disease-specific modification if case-control studies are available. While case-control studies could potentially be considered for a few pathogenic variants with high minor allele frequency, the VCEP is unaware of any such studies being conducted for *SGCD*. Any case-control study would require careful selection of an appropriate control population given the potential for late onset and mild disease.

---

### PM1 - Mutational Hot Spot

**Original ACMG Summary:** Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.

**VCEP Specifications:** ***Not Applicable.*** Not applicable at this time.

---

### PM2 - Absent from Controls

**Original ACMG Summary:** Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

**Caveat:** Population data for indels may be poorly called by next generation sequencing.

**VCEP Specification (Supporting only, 1 pt):**

Apply if the Grpmax variant allele frequency / upper bound of the 95% confidence interval (95% CI) of the Grpmax variant allele frequency in gnomAD is **<0.00009**. Do not use data for which the variant does not pass quality control filters.

**Detailed rules:**
- If only 1 or 2 variant alleles are present in the Grpmax population, use the Grpmax variant allele frequency
- If at least 3 variant alleles are present in the Grpmax population, use the upper bound of the 95% confidence interval (95% CI) of the Grpmax variant allele frequency

**Grpmax** refers to the gnomAD subpopulation with the highest variant allele frequency. Use large, non-bottlenecked genetic ancestry groups for the Grpmax; avoid using the Amish, Ashkenazi Jewish, European Finnish, and Remaining Individuals groups as well as the genomes-only data for the Middle Eastern group.

The upper bound of the 95% CI must be calculated using variant allele numbers and counts from gnomAD. Confidence interval tools, such as Confit-de-MAF (https://www.genecalculators.net/confit-de-maf.html), can be used.

Use the gnomAD version with the largest allele number.

For larger deletions or duplications that may not be well represented in gnomAD (e.g., single- or multi-exon events), also confirm the variant is not common in gnomAD SVs, gnomAD CNVs, or the Database of Genomic Variants (DGV) (https://dgv.tcag.ca/dgv/app/home).

---

### PM3 - In Trans with Pathogenic

**Original ACMG Summary:** For recessive disorders, detected in trans with a pathogenic variant.

**Note:** This requires testing of parents (or offspring) to determine phase.

**VCEP Specifications:** Use the SVI Working Group's recommended point system to determine PM3 strength (see supplementary file "PM3 table").

#### PM3 Strength Thresholds

| Total Points | Strength Level | Default Points |
|-------------|----------------|---------------|
| ≥0.5 but <1.0 | PM3_Supporting | 1 |
| ≥1.0 but <2.0 | PM3 (Moderate) | 2 |
| ≥2.0 but <4.0 | PM3_Strong | 4 |
| ≥4.0 | PM3_Very Strong | 8 |

#### PM3 Point System (Per Proband)

| Classification/Zygosity of Other Variant | Confirmed in Trans¹ | Phase Unknown² |
|------------------------------------------|---------------------|----------------|
| Pathogenic or Likely Pathogenic variant³ | 1.0 | 0.5 (P) / 0.25 (LP) |
| Homozygous occurrence (max 1.0 pt; downgrade to 0.25 pts for consanguinity) | 0.5 | N/A |
| Uncertain significance variant⁴ (max 0.5 pts) | 0.25 | 0 |

#### PM3 Footnotes

1. Author assertions on phase, including based on allele-specific transcript expression, are acceptable.
2. For variants identified in unknown phase, PM3 points should not be awarded under the following circumstances:
   - The same variants were ever confirmed in cis (e.g., in a different patient in the literature)
   - gnomAD co-occurrence data (https://gnomad.broadinstitute.org/variant-cooccurrence) predict the variants may be part of the same haplotype in at least one genetic ancestry group
   - More than 2 variants are reported in the patient, none of which can be classified as likely benign or benign
3. Any variant awarded points as likely pathogenic or pathogenic must have been classified using the LGMD VCEP specifications.
4. For any variant awarded points as VUS, benign frequency codes (BA1, BS1) cannot be applicable.

#### PM3 Co-Application Rules

It is possible to award PM3 points to both variants identified in an individual as long as the evidence related to their co-observation in that individual does not contribute to the variant classification that determines the number of points applied. This excludes all evidence derived from the co-observation, including inter-dependent PM3 points (pathogenicity of variant in trans/unknown phase), PP1 (genotype-phenotype co-segregation), and PP4 (phenotype specificity). Please see examples in supplementary file "PM3 co-application examples".

##### Example 1: PM3 can be awarded to both variants in a pair without circularity

Variants A and B are observed in trans in patient X, who meets the criteria for PP4. Variant A has not been observed in any other patients. Variant B has also been observed in patient Y, where it was confirmed in trans with a pathogenic variant (variant C, 1.0 PM3 pt) in an individual meeting the criteria for PP4_Moderate.

- **Variant A** is classified as LP independent of the observation in patient X (e.g., PVS1 + PM2_Supporting).
- **Variant B** is also classified as LP independent of the observation in patient X (e.g., PS3_Moderate + PP3 + PM2_Supporting + PP4_Moderate (for patient Y) + PM3 (for variant C in patient Y)).
- In the curation of **variant B**, 1.0 PM3 pt can be awarded for the observation in patient X, since variant B was confirmed in trans with an LP* variant (variant A). With an additional 1.0 pt from patient X, PM3 can be upgraded to PM3_Strong, resulting in a final classification of **P** for variant B.
- In the curation of **variant A**, 1.0 PM3 pt can be awarded for the observation in patient X as well, since variant A was also confirmed in trans with an LP* variant (variant B). With 1.0 pt, PM3 can be applied, resulting in a final classification of **P** for variant A (PVS1 + PM2_Supporting + PM3 + PP4).

*While the final classification of variants A and B is P, the classification that would be reached without counting the evidence from their co-observation in patient X is used when awarding PM3 points for that observation. This avoids circularity and double counting of evidence.

##### Example 2: PM3 cannot be awarded to both variants in a pair without circularity

Variants A and B are observed in trans in patient X, who meets the criteria for PP4. Variant A has not been observed in any other patients. Variant B has also been observed in patient Y, where it was observed in unknown phase with a VUS variant (variant C, 0 PM3 pts) in an individual meeting the criteria for PP4.

- **Variant A** is classified as LP independent of the observation in patient X (PVS1 + PM2_Supporting).
- **Variant B** is classified as VUS independent of the observation in patient X (e.g., PS3_Moderate + PP3 + PM2_Supporting + PP4 (for patient Y)).
- In the curation of **variant B**, PM3 can be awarded for the observation in patient X, since variant B was confirmed in trans with an LP* variant (variant A, 1.0 PM3 pt). With PM3, variant B can be classified as LP.
- In the curation of **variant A**, PM3 **cannot** be awarded for the observation in patient X, since variant B was classified as VUS independent of the observation in patient X, and the 0.25 PM3 pts awarded for being confirmed in trans with a VUS are not sufficient for PM3 to be applied at any strength level. However, PP4 can be applied, resulting in a final classification of **P** for variant A (PVS1 + PM2_Supporting + PP4).

---

### PM4 - Protein Length Changes

**Original ACMG Summary:** Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

**VCEP Specifications:**

#### Moderate (2 pts)

Use as is, regardless of the length of the in-frame insertion or deletion.

---

### PM5 - Novel Missense at Same Residue

**Original ACMG Summary:** Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.

**Example:** Arg156His is pathogenic; now you observe Arg156Cys.

**Caveat:** Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:**

#### Strong (4 pts)

Apply only for missense variants for which the amino acid change is the expected mechanism of disease. For the missense variant under curation and the variant(s) resulting in a different amino acid change, exclude likely splice effects (SpliceAI score <0.5 or experimental evidence of normal splicing). The REVEL score for the missense variant under curation should be >0.7. Missense changes at the same residue must be classified according to LGMD VCEP specifications, and no benign missense variation should be present at the residue. Do not apply for missense variants encoded by the first or last 3 nucleotides of an exon unless a splice effect has been ruled out for the variant under curation and the variant(s) resulting in the same amino acid change. Apply at Strong for 2 pathogenic or 3 likely pathogenic variants resulting in different amino acid changes at the same residue as the variant under curation.

PM5 can potentially be applied to multiple amino acid changes at the same residue as long as the variant classification that determines the strength level does not depend on PM5 application.

#### Moderate (2 pts)

Apply only for missense variants for which the amino acid change is the expected mechanism of disease. For the missense variant under curation and the variant(s) resulting in a different amino acid change, exclude likely splice effects (SpliceAI score <0.5 or experimental evidence of normal splicing). The REVEL score for the missense variant under curation should be >0.7. Missense changes at the same residue must be classified according to LGMD VCEP specifications, and no benign missense variation should be present at the residue. Do not apply for missense variants encoded by the first or last 3 nucleotides of an exon unless a splice effect has been ruled out for the variant under curation and the variant(s) resulting in the same amino acid change. Apply at Moderate for 1 pathogenic or 2 likely pathogenic variants resulting in different amino acid changes at the same residue as the variant under curation.

PM5 can potentially be applied to multiple amino acid changes at the same residue as long as the variant classification that determines the strength level does not depend on PM5 application.

#### Supporting (1 pt)

Apply only for missense variants for which the amino acid change is the expected mechanism of disease. For the missense variant under curation and the variant(s) resulting in a different amino acid change, exclude likely splice effects (SpliceAI score <0.5 or experimental evidence of normal splicing). The REVEL score for the missense variant under curation should be >0.7. Missense changes at the same residue must be classified according to LGMD VCEP specifications, and no benign missense variation should be present at the residue. Do not apply for missense variants encoded by the first or last 3 nucleotides of an exon unless a splice effect has been ruled out for the variant under curation and the variant(s) resulting in the same amino acid change. Apply at Supporting for 1 likely pathogenic variant resulting in a different amino acid change at the same residue as the variant under curation.

PM5 can potentially be applied to multiple amino acid changes at the same residue as long as the variant classification that determines the strength level does not depend on PM5 application.

---

### PM6 - De Novo (Assumed)

**Original ACMG Summary:** Assumed de novo, but without confirmation of paternity and maternity.

**VCEP Specifications:** ***Not Applicable.*** Not applicable. See PS2.

---

### PP1 - Co-segregation

**Original ACMG Summary:** Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.

**Note:** May be used as stronger evidence with increasing segregation data.

**VCEP Specifications:**

Segregations should be counted across families, with the total number of segregations determining the strength level. When applied together, PP1 and PP4 cannot exceed 5 Bayesian pts (Supporting + Strong or Moderate + Moderate).

#### PP1 Strength Thresholds

| Strength | Criteria | Default Points |
|----------|----------|---------------|
| **Supporting** | 1 affected segregation (in addition to proband) | 1 |
| **Moderate** | 2 affected segregations (in addition to proband; may be from a single family) | 2 |
| **Strong** | 3 affected segregations (in addition to proband) across ≥2 families | 4 |

---

### PP2 - Missense in Constrained Gene

**Original ACMG Summary:** Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.

**VCEP Specifications:** ***Not Applicable.*** SGCD is not constrained for missense variation (Z-score <3).

---

### PP3 - Computational Evidence

**Original ACMG Summary:** Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).

**Caveat:** As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.

**VCEP Specifications:**

#### Supporting (1 pt)

- For **missense variants**, use REVEL with a score **≥0.7**.
- For **variants that may affect splicing**, use SpliceAI with a score **≥0.5**.
- For any variant with RNA or other experimental data indicating an impact on splicing, follow the SVI Working Group's recommendations (Walker et al. 2023; PMID: 37352859). See supplementary file "experimental splice data".

---

### PP4 - Phenotype Specificity

**Original ACMG Summary:** Patient's phenotype or family history is highly specific for a disease with a single genetic etiology.

**VCEP Specifications:**

Use the PP4 table (see supplementary file "PP4 table SGCD") to determine the appropriate PP4 strength level. Apply PP4 only once, for a patient meeting the highest possible strength level. When applied together, PP1 and PP4 cannot exceed 5 Bayesian pts (Supporting + Strong or Moderate + Moderate). If PP1_Moderate is applied and the criteria for PP4_Strong are also met, a downgraded PP4_Moderate can be applied.

#### PP4 Strength Thresholds

| Strength | Default Points |
|----------|---------------|
| **Supporting** | 1 |
| **Moderate** | 2 |
| **Strong** | 4 |

#### PP4 Requirements Table

| Requirement | | PP4_Supporting | PP4_Moderate | PP4_Strong |
|---|---|:---:|:---:|:---:|
| **Clinical¹** | Progressive limb-girdle pattern of muscle weakness observed over ≥6 months OR clinical suspicion of LGMD | Y | Y | Y |
| **Genetic testing²** | 2 presumed diagnostic³ variants in SGCD, 1 of which is the variant under curation | Y | Y | Y |
| **Protein expression in patient tissue** | Severely reduced⁴ or absent⁵ expression of full-length protein in skeletal muscle (e.g., WB or IHC) | N | A | B |

**Key:** Y = Required; N = Not required; A = severely reduced⁴; B = absent⁵

#### PP4 Footnotes

1. May be accompanied by supporting EMG, MRI, muscle histology, elevated CK but not required.
2. Screening of all exons and exon/intron boundaries of SGCD required for Supporting. To apply at Moderate or Strong, screening of SGCA, SGCB, and SGCG also required. Do not apply if 2 presumed diagnostic variants also identified in SGCA, SGCB, or SGCG. Screening of additional neuromuscular disease genes (e.g., through a panel) is recommended but not required.
3. If variants have not yet been curated by the LGMD VCEP, confirm they cannot be classified as LB or B (e.g., through application of BA1, BS1, and/or BP4/BP7). If phase is unknown, do not apply if the identified variants were ever confirmed in cis or if gnomAD co-occurrence data (https://gnomad.broadinstitute.org/variant-cooccurrence) predict the variants may be part of the same haplotype in at least one genetic ancestry group.
4. <~30% normal; may also be described as "severely"/"drastically"/"strongly" reduced.
5. May also be described as "trace" or "barely detectable."

---

### PP5 - Reputable Source

**Original ACMG Summary:** Reputable source recently reports variant as pathogenic, but the evidence is not available to the laboratory to perform an independent evaluation.

**VCEP Specifications:** ***Not Applicable.*** This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee. (PubMed: 29543229)

---

## Benign Criteria

### BA1 - Allele Frequency >5%

**Original ACMG Summary:** Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

**VCEP Specification (Stand Alone):**

Apply if the variant Grpmax FAF (the lower bound of the 95% confidence interval of the maximum credible genetic ancestry group allele frequency) is **>0.002**. This value can be taken directly from gnomAD, but do not use data for which the variant does not pass quality control filters. See supplementary file "benign frequency exceptions" for a list of variants defined as exceptions to the benign frequency rules. Ongoing updates to this list will be available at the LGMD VCEP webpage: https://clinicalgenome.org/affiliation/50061/.

Variants whose frequency may not be reliable (e.g., variants that may reflect a sequencing artifact) should be critically evaluated and brought to the attention of the LGMD VCEP.

---

### BS1 - Frequency Greater Than Expected

**Original ACMG Summary:** Allele frequency is greater than expected for disorder.

**VCEP Specification (Strong, -4 pts):**

Apply if the variant Grpmax FAF (the lower bound of the 95% confidence interval of the maximum credible genetic ancestry group allele frequency) is **>0.0009**. This value can be taken directly from gnomAD, but do not use data for which the variant does not pass quality control filters. See supplementary file "benign frequency exceptions" for a list of variants defined as exceptions to the benign frequency rules. Ongoing updates to this list will be available at the LGMD VCEP webpage: https://clinicalgenome.org/affiliation/50061/.

Variants whose frequency may not be reliable (e.g., variants that may reflect a sequencing artifact) should be critically evaluated and brought to the attention of the LGMD VCEP.

#### Benign Frequency Exceptions (BS1)

| Variant Information | Status | Comment |
|---------------------|--------|---------|
| NM_003494.3(DYSF):c.2643+1G>A | BS1 exception | Common pathogenic variant |
| NM_213599.3(ANO5):c.191dup (p.Asn64LysfsTer15) | BS1 exception | Common pathogenic variant |
| NM_000070.3(CAPN3):c.1746-20C>G | BS1 exception | Proposed hypomorph |
| NM_000070.3(CAPN3):c.2120A>G (p.Asp707Gly) | BS1 exception | Likely founder in East Asian population |

> **Note:** These exceptions are for the broader LGMD VCEP panel; no SGCD-specific exceptions are currently listed.

---

### BS2 - Observed in Healthy Adult

**Original ACMG Summary:** Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

**VCEP Specifications:** ***Not Applicable.*** Not applicable as LGMD is characterized by variable expressivity and late-onset LGMD is not uncommon.

---

### BS3 - Functional Studies (No Effect)

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

**VCEP Specifications:** ***Not Applicable.*** Not applicable. Since muscle disease mechanisms are complex, it is not feasible at this time to exclude all pathogenic functional abnormalities through available assays.

---

### BS4 - Lack of Segregation

**Original ACMG Summary:** Lack of segregation in affected members of a family.

**Caveat:** The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.

**VCEP Specifications:**

#### Strong (-4 pts)

Use as is. One affected individual (genotype-, phenotype+) is sufficient for BS4. Do not apply for genotype+, phenotype- individuals, as LGMD is characterized by variable expressivity and late onset is not uncommon.

---

### BP1–BP7 - Benign Supporting

| Criterion | Status | Comment |
|-----------|--------|---------|
| **BP1** | ***Not Applicable*** | Not applicable as missense variants are also known to cause disease. |
| **BP2** | **Supporting (-1 pt)** | Use when variant is found *in cis* with a variant classified as pathogenic or likely pathogenic using the LGMD VCEP specifications. |
| **BP3** | ***Not Applicable*** | Not applicable. Repetitive regions without a known function are not well described in SGCD. |
| **BP4** | **Supporting (-1 pt)** | For missense variants, use REVEL with a score ≤0.1 AND SpliceAI with a score ≤0.05. For variants that may affect splicing, use SpliceAI with a score ≤0.05. Splice AI scores can be calculated here: https://spliceailookup.broadinstitute.org/. For any variant with RNA or other experimental data indicating no impact on splicing, follow the SVI Working Group's recommendations (Walker et al. 2023; PMID: 37352859). See supplementary file "experimental splice data". |
| **BP5** | ***Not Applicable*** | Not applicable. |
| **BP6** | ***Not Applicable*** | This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee. (PubMed: 29543229) |
| **BP7** | **Strong (-4 pts) or Supporting (-1 pt)** | **Strong:** For any variant that has been experimentally shown to have no splice impact, follow the SVI Working Group's recommendations (Walker et al. 2023; PMID: 37352859). See supplementary file "Experimental splice data". Apply BP7_Strong if a splicing assay shows no effect on splicing and a protein impact can be ruled out. **Supporting:** For splice predictions, use SpliceAI with a score ≤0.05. BP7 may be co-applied with BP4 for synonymous, UTR, and intronic variants located outside the splice donor/acceptor regions designated in Walker et al. 2023 (+6/-3 for donor; +1/-20 for acceptor). |

---

## Rules for Combining Criteria

This VCEP uses the **Bayesian point-based framework** (Tavtigian et al., 2020) for combining criteria.

### Point-Based Classification Thresholds

| Category | Point Ranges |
|----------|-------------|
| **Pathogenic** | ≥10 |
| **Likely Pathogenic** | 6 – 9 |
| **Uncertain Significance** | 0 – 5 |
| **Likely Benign** | -6 – -1 |
| **Benign** | ≤-7 |

**Additional Notes:** A Benign classification can also be assigned when BA1 applies.

### Default Point Values Summary

| Strength Level | Pathogenic Points | Benign Points |
|---------------|------------------|---------------|
| Very Strong | 8 | — |
| Strong | 4 | -4 |
| Moderate | 2 | — |
| Supporting | 1 | -1 |
| Stand Alone | — | BA1 (Benign) |

### Special Combination Rules

- **PP1 + PP4 cap:** When applied together, PP1 and PP4 cannot exceed 5 Bayesian points (Supporting + Strong or Moderate + Moderate). If PP1_Moderate is applied and the criteria for PP4_Strong are also met, a downgraded PP4_Moderate can be applied.
- **PS2/PM6:** For autosomal recessive SGCD, PS2 is applied at Supporting only. PM6 is not applicable.
- **PS3:** Apply only once, for the piece of evidence that meets the highest possible strength level.
- **PM3 co-application:** PM3 points may be awarded to both variants in a pair if neither variant's independent classification relies on co-observation evidence.

---

## Appendices

### Appendix A: PVS1 Flowchart

The PVS1 decision tree for SGCD is provided as a supplementary file ("PVS1 flowchart SGCD"). Key parameters:

- **Biologically relevant transcript:** NM_000337.6
- **NMD boundary:** Codons 35–214 (premature truncation predicted to undergo NMD)
- **First 100 bp exception:** Codons 1–34 (PMID: 27618451) → PVS1_Supporting
- **In-frame exons** (exon skipping not expected to result in NMD): 2, 3, 4, 6, 9
- **Critical protein regions:** None specified
- **Initiation codon guidance:** Use standard PVS1 initiation codon decision path

### Appendix B: Experimental Splice Data Decision Tree

For any variant with RNA or other experimental data:

1. **Silent/Intronic variants:** If RNA/splicing is observed, categorize the specific impact; note that multiple factors including technique, RNA source, and gene-specific knowledge need consideration.
2. **Variant-specific changes compared to control:** Follow PVS1 flowchart for observed RNA impact for your gene.
3. **Consider splicing predictive data:**
   - If BP7_S (RNA) is applied → consider splicing predictive data
   - BP7_S (RNA) + prediction → may inform strength level
   - If BP7_S (RNA) + prediction aligns → document as "BP7_S (RNA)"; note: do not include data that was present and reviewed
4. **Proportion of alternative transcript(s) (inferred to be) produced by mutant allele:**
   - If independent evidence at transcriptomic or protein levels suggests loss of function:
     - **Complete** → Keep strength level
     - **Near complete** → Reduce strength by 1 level
     - **Incomplete** → Do not apply codes
5. **Determine PVS1 (RNA) weight from combined analyses** (PVS1/BP4 not applicable if incomplete)
6. **PVS1 (RNA) or BP7_S (RNA) — use appropriate decision tree as applicable**

### Appendix C: PS1 Splicing Reference Table

See [PS1 - Same Amino Acid Change](#ps1---same-amino-acid-change) section for the full PS1 splicing code weights table (Table 2).

### Appendix D: Population Frequency Thresholds Summary

| Criterion | Threshold | Strength | Notes |
|-----------|-----------|----------|-------|
| BA1 | Grpmax FAF >0.002 | Stand Alone (Benign) | Lower bound of 95% CI of maximum credible genetic ancestry group allele frequency |
| BS1 | Grpmax FAF >0.0009 | Strong (-4 pts) | Lower bound of 95% CI of maximum credible genetic ancestry group allele frequency |
| PM2 | Grpmax VAF / upper bound 95% CI <0.00009 | Supporting (1 pt) | Use Grpmax VAF for ≤2 alleles; use upper bound 95% CI for ≥3 alleles |

### Appendix E: Criteria Summary Table

| Criterion | VCEP Status | Max Strength | Default Points | Modification Type |
|-----------|-------------|-------------|---------------|-------------------|
| PVS1 | Applied | Very Strong | 8 | Gene-specific |
| PS1 | Applied | Strong | 4 | Disease-specific, General recommendation |
| PS2 | Applied | Supporting | 1 | Disease-specific, General recommendation |
| PS3 | Applied | Strong | 4 | Disease-specific, General recommendation |
| PS4 | Applied | Strong | 4 | Clarification |
| PM1 | Not Applicable | — | — | — |
| PM2 | Applied (Supporting only) | Supporting | 1 | Disease-specific |
| PM3 | Applied | Very Strong | 8 | Disease-specific, General recommendation |
| PM4 | Applied | Moderate | 2 | No change |
| PM5 | Applied | Strong | 4 | Disease-specific |
| PM6 | Not Applicable | — | — | See PS2 |
| PP1 | Applied | Strong | 4 | Disease-specific |
| PP2 | Not Applicable | — | — | — |
| PP3 | Applied | Supporting | 1 | Disease-specific |
| PP4 | Applied | Strong | 4 | Disease-specific, Gene-specific |
| PP5 | Not Applicable | — | — | — |
| BA1 | Applied | Stand Alone | Benign | Disease-specific |
| BS1 | Applied | Strong | -4 | Disease-specific |
| BS2 | Not Applicable | — | — | — |
| BS3 | Not Applicable | — | — | — |
| BS4 | Applied | Strong | -4 | Clarification |
| BP1 | Not Applicable | — | — | — |
| BP2 | Applied | Supporting | -1 | Disease-specific |
| BP3 | Not Applicable | — | — | — |
| BP4 | Applied | Supporting | -1 | Disease-specific |
| BP5 | Not Applicable | — | — | — |
| BP6 | Not Applicable | — | — | — |
| BP7 | Applied | Strong | -4 / -1 | Disease-specific, Clarification |

---

## Key References

- Richards et al., 2015 — ACMG/AMP Standards and Guidelines (PMID: 25741868)
- Tavtigian et al., 2020 — Bayesian framework for variant classification (calibrated point system)
- Brnich et al., 2020 — PS3/BS3 functional evidence recommendations (PMID: 31892348)
- Walker et al., 2023 — SVI Working Group RNA/splice data recommendations (PMID: 37352859)
- ClinGen SVI recommendation against PP5/BP6 (PMID: 29543229)
- Soheili et al., 2012 — Sarcoglycan complex membrane localization assay (PMID: 22095924)
- Abou Tayoun et al., 2018 — PVS1 first 100 bp (PMID: 27618451)

---

*This document was compiled from ClinGen LGMD VCEP specifications for SGCD v2.0.0. For the most current version, please refer to the ClinGen website: https://clinicalgenome.org/affiliation/50061/*
