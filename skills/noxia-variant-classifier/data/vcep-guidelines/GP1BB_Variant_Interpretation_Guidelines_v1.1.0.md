# ClinGen Platelet Disorders VCEP Variant Interpretation Guidelines for GP1BB

**Version:** 1.1.0
**Released:** 9/29/2025
**Affiliation:** Platelet Disorders VCEP
**Based on:** Richards et al., 2015 ACMG/AMP Guidelines

---

## Gene Information

| Attribute | Value |
|-----------|-------|
| **Gene** | GP1BB (HGNC:4440) |
| **HGNC Name** | glycoprotein Ib platelet subunit beta |
| **Transcript** | NM_000407.5 |
| **Disease** | Bernard-Soulier syndrome (MONDO:0009276) |
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
   - [BA1 - Allele Frequency >0.1%](#ba1---allele-frequency-01)
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

**VCEP Specifications:** Use GP1BB modified decision tree below.

#### Strength Levels

| Strength | Criteria |
|----------|----------|
| **Very Strong** | Use GP1BB modified decision tree as per SVI WG |
| **Strong** | Use GP1BB modified decision tree as per SVI WG |
| **Moderate** | Use GP1BB modified decision tree as per SVI WG |
| **Supporting** | Use GP1BB modified decision tree as per SVI WG |

#### PVS1 Decision Tree for GP1BB

**Nonsense or Frameshift:**
- **Predicted to undergo NMD:**
  - GP1BB coding sequence begins in the last 50 nucleotides of the penultimate exon (1 of 2) which is not considered subject to NMD
- **Not predicted to undergo NMD:**
  - Exon is present in biologically-relevant transcript(s):
    - Truncated/altered region is critical to protein function (transmembrane domain, amino acids 148-173) → **PVS1_Strong**
    - Role of region in protein function is unknown → See decision tree
  - Exon is absent from biologically-relevant transcript(s) → **N/A**

**Canonical Splice Sites (GT-AG, +/-1,2):**
- Exon skipping or use of cryptic splice site disrupts reading frame and predicted to undergo NMD:
  - Exon present in biologically-relevant transcript(s) → **PVS1**
  - Exon absent from biologically-relevant transcript(s) → **N/A**
- Exon skipping or use of cryptic splice site preserves reading frame → See full decision tree
- Exon skipping disrupts reading frame and NOT predicted to undergo NMD → See full decision tree

**Deletion (Single exon to full gene):**
- Single to multi exon deletion disrupts reading frame and predicted to undergo NMD:
  - Exon present in biologically-relevant transcript(s) → **PVS1**
  - Exon absent from biologically-relevant transcript(s) → **N/A**
- Single to multi exon deletion preserves reading frame → See full decision tree
- Full gene deletion → **PVS1**

**Duplication (≥1 exon, completely contained within gene):**
- Proven in tandem:
  - Reading frame disrupted and NMD predicted → **PVS1**
  - No or unknown impact on reading frame and NMD → **N/A**
- Presumed in tandem:
  - Reading frame presumed disrupted and NMD predicted → **PVS1_Strong**
- Proven not in tandem → **N/A**

**Initiation Codon:**
- Different functional transcript uses alternative start codon → See decision tree
- No known alternative start codon in other transcripts:
  - ≥1 pathogenic variant(s) upstream of closest potential in-frame start codon → **PVS1**
  - No pathogenic variant(s) upstream of closest potential in-frame start codon → **PVS1_Supporting**
- **Note:** GP1BB does not have another potential in-frame start codon

**Terminal-most PTV:** NM_000407.5:c.448del (Ala150Argfs*43) - ClinVar 627075 (Likely Pathogenic)

---

### PS1 - Same Amino Acid Change

**Original ACMG Summary:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.

**Example:** Val->Leu caused by either G>C or G>T in the same codon.

**Caveat:** Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | Use as originally specified, but the comparison variant must reach a **pathogenic** classification using these rule specifications in order to apply code |
| **Moderate** | Use as originally specified, but the comparison variant must reach a **likely pathogenic** classification using these rule specifications in order to apply code |

---

### PS2 - De Novo (Confirmed)

**Original ACMG Summary:** De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.

**Note:** Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.

**VCEP Specifications:**
- Only applicable when proband has a known pathogenic or likely pathogenic variant according to the BSS rule specifications along with the de novo variant
- Only use "highly specific phenotype" scoring if all three BSS genes (GP1BA, GP1BB, GP9) were sequenced
- Otherwise use the "consistent but not highly specific" scoring

#### PS2/PM6 Point System

| Phenotype Consistency | Confirmed Parental Relationships | Unconfirmed |
|-----------------------|----------------------------------|-------------|
| Phenotype highly specific for gene (all 3 BSS genes sequenced) | 2 points | 1 point |
| Phenotype consistent but not highly specific (1-2 genes sequenced) | 1 point | 0.5 points |
| Phenotype consistent + high genetic heterogeneity | 0.5 points | 0.25 points |
| Phenotype not consistent | 0 points | 0 points |

#### Evidence Strength Thresholds

| Total Points | Strength Level |
|--------------|----------------|
| 0.5 | Supporting |
| 1.0 | Moderate (PS2_Moderate) |
| 2.0 | Strong (PS2) |
| 4.0 | Very Strong (PS2_VeryStrong) |

---

### PS3 - Functional Studies

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.

**Note:** Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | In a transgenic animal model, must demonstrate minimal to no function |
| **Supporting** | Functional assays measuring quantity of GP1ba and/or GPIX expression on cell surface measured by flow cytometry (see approved assays below) |

#### Approved Functional Assays for PS3_Supporting (GP1BB)

| PMID | Year | First Author | Assay Description | Cell Line | Threshold for Abnormal |
|------|------|--------------|-------------------|-----------|------------------------|
| 10216092 | 1999 | Kenny D | Transient transfection of mutant GPIbb with wild-type GPIba and GPIX into 293T cells, measured by flow cytometry | 293T | Absent or near absent expression, >75% reduction from WT |
| 10928480 | 2000 | Kunishima S | 293T cells transiently cotransfected with wild-type or mutant GPIbb with wild-type GPIba and GPIX, measured by flow cytometry | 293T | Absent or near absent expression, >75% reduction from WT |
| 12958615 | 2003 | González-Manchón C | CHO cells transiently cotransfected with normal GPIba and GPIX cDNAs, and either normal or mutant GPIbb cDNAs, measured by flow cytometry | CHO | Absent or near absent expression, >75% reduction from WT |
| 16409472 | 2006 | Strassel C | CHO cells expressing GPIba and GPIX subunits, transfected with wild-type or mutant GPIbb, measured by flow cytometry | CHO | Absent or near absent expression, >75% reduction from WT |

**Controls Required:**
- Basic positive control: wild-type GPIBB
- Basic negative control: mock transfection or empty vector
- Readout: Quantity of GP1ba and/or GPIX expression on the cell surface

---

### PS4 - Prevalence in Affected

**Original ACMG Summary:** The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.

**Note 1:** Relative risk (RR) or odds ratio (OR), as obtained from case-control studies, is >5.0 and the confidence interval around the estimate of RR or OR does not include 1.0.

**Note 2:** In instances of very rare variants where case-control studies may not reach statistical significance, the prior observation of the variant in multiple unrelated patients with the same phenotype, and its absence in controls, may be used as moderate level of evidence.

**VCEP Specifications:**
According to Bragadottir et al. (PMID: 25370924), individuals heterozygous for Bernard-Soulier syndrome variants are considered informative due to measurable, quantitative abnormalities relevant to the disease.

**Caveats:**
1. The variant must be sufficiently rare, meeting PM2_supporting
2. There must be an assumed unrelated biallelic BSS patient, meeting PP4, before heterozygotes are considered
3. A single proband of a family can be included in either PM3 (biallelic proband) or PS4 (monoallelic proband), not both
4. Any additional family members are not included in PS4; they may be considered for segregation in PP1

#### PS4 Scoring for Heterozygous Individuals

| Evidence Type | Points |
|---------------|--------|
| Significantly reduced surface expression of GP1b measured by flow cytometry | 0.5 points |
| Giant platelets (MPD >7 microns) OR macrothrombocytopenia (MPV >12 fL and platelet count <150x10^9/L) | 0.25 points |

#### PS4 Strength Thresholds

| Total Points | Strength Level |
|--------------|----------------|
| 1.0 - 1.75 | PS4_Supporting |
| 2.0+ | PS4_Moderate |

---

### PM1 - Mutational Hot Spot

**Original ACMG Summary:** Located in a mutational hot spot and/or critical and well-established functional domain (e.g., active site of an enzyme) without benign variation.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Moderate** | Disulfide bonds in GPIb are well-established as critical to function, both for interaction with GPIX (PMID: 12036872) and receptor binding to von Willebrand factor (PMID: 18647229). PM1 can be applied when the following cysteine residues (at which there are no known benign variants) are altered: **93, 95, 118, 141, and 147** |

---

### PM2 - Absent from Controls

**Original ACMG Summary:** Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

**Caveat:** Population data for indels may be poorly called by next generation sequencing.

**VCEP Specification (Supporting only):**

| Strength | Criteria |
|----------|----------|
| **Supporting** | gnomAD MAF ≤ 0.00006517 |

---

### PM3 - In Trans with Pathogenic

**Original ACMG Summary:** For recessive disorders, detected in trans with a pathogenic variant.

**Note:** This requires testing of parents (or offspring) to determine phase.

**VCEP Specifications:**
- *In trans* variants classified as VUS, per the GP1BB rule specifications, must meet PM2_supporting to be scored
- *In trans* variants that meet a pathogenic or likely pathogenic classification using the GP1BB rule specifications do not have to meet PM2_supporting criteria; however, they cannot meet BS1 or BA1 criteria
- A 22q11.2 deletion in trans (https://www.ncbi.nlm.nih.gov/books/NBK1523/) may be automatically scored 1 point with confirmation that the deletion includes the GP1BB gene

#### PM3 Point System (Per Proband)

| Classification of Other Variant | Phase Confirmed (in trans) | Phase Unknown |
|---------------------------------|---------------------------|---------------|
| Pathogenic variant | 1.0 point | 0.5 point |
| Likely pathogenic variant | 1.0 point | 0.25 point |
| Homozygous (non-consanguineous) | 1.0 point | 1.0 point |
| Homozygous (consanguineous, max 0.5/family) | 0.5 point | 0.5 point |
| VUS (max 0.5 total) | 0.25 point | 0.0 point |
| 22q11.2 deletion (confirmed to include GP1BB) | 1.0 point | 1.0 point |

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

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Moderate** | Use with no specification |

---

### PM5 - Novel Missense at Same Residue

**Original ACMG Summary:** Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.

**Example:** Arg156His is pathogenic; now you observe Arg156Cys.

**Caveat:** Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Moderate** | Use as originally specified, but the comparison variant must reach a **pathogenic** classification using these rule specifications in order to apply code |
| **Supporting** | Use as originally specified, but the comparison variant must reach a **likely pathogenic** classification using these rule specifications in order to apply code |

---

### PM6 - De Novo (Assumed)

**Original ACMG Summary:** Assumed de novo, but without confirmation of paternity and maternity.

**VCEP Specifications:** **Not Applicable**

**Comments:** Use PS2 for de novo cases in lieu of this rule code. The PS2/PM6 point system incorporates both confirmed and unconfirmed de novo cases.

---

### PP1 - Co-segregation

**Original ACMG Summary:** Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.

**Note:** May be used as stronger evidence with increasing segregation data.

**VCEP Specifications:**
For Bernard-Soulier syndrome (BSS), segregation of the variant in a pedigree is considered informative in the case of both:
- Additional relatives with BSS
- Heterozygous relatives with measurable, quantitative abnormalities relevant to the disease

**Caveats:**
- There must be a biallelic BSS patient, meeting PP4, before segregation points are awarded
- Heterozygotes used for PP1 cannot be applied to PS4

#### PP1 Segregation Scoring

| Evidence Type | Points |
|---------------|--------|
| Proband | 0 points (proband should be accounted for in PP4 or PS4) |
| BSS affected relative with the same biallelic variant(s) identified in the proband | 1.0 point |
| Relative heterozygous for the variant with significantly reduced surface expression of GP1b measured by flow cytometry | 0.5 points |
| Relative heterozygous for the variant with giant platelets (MPD >7 microns) OR macrothrombocytopenia (MPV >12 fL and platelet count <150x10^9/L) | 0.25 points |

**Note:** Only score one parent of a homozygous proband in a consanguineous pedigree.

#### PP1 Strength Thresholds

| Total Segregation Score | Strength Level |
|------------------------|----------------|
| 1.0 - 1.75 | PP1_Supporting |
| 2.0 - 2.75 | PP1_Moderate |
| 3.0+ | PP1_Strong |

---

### PP2 - Missense in Constrained Gene

**Original ACMG Summary:** Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.

**VCEP Specifications:** **Not Applicable**

**Comments:** This rule does not apply because BSS is a rare disease and this gene is not constrained for missense variation (gnomAD).

---

### PP3 - Computational Evidence

**Original ACMG Summary:** Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).

**Caveat:** As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Moderate** | REVEL score ≥ 0.773 (based on Pejaver et al., 2022; PMID: 36413997) |
| **Supporting** | REVEL score ≥ 0.644 (to < 0.773) (based on Pejaver et al., 2022; PMID: 36413997) **OR** SpliceAI score ≥ 0.5 for suggested splicing effect |

---

### PP4 - Phenotype Specificity

**Original ACMG Summary:** Patient's phenotype or family history is highly specific for a disease with a single genetic etiology.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Moderate** | Must meet **BOTH** criteria: (1) Proband with platelet aggregation study absent for ristocetin and present for all other agonists **OR** flow cytometry or Western blot less than 10% expression of GPIba; **AND** (2) Proband must have full sequencing of all three BSS genes (GP1BA, GP1BB and GP9) and deletion/duplication analysis |
| **Supporting** | Proband with platelet aggregation study absent for ristocetin and present for all other agonists **OR** flow cytometry or Western blot less than 10% expression of GPIba |

---

### PP5 - Reputable Source

**Original ACMG Summary:** Reputable source recently reports variant as pathogenic, but the evidence is not available to the laboratory to perform an independent evaluation.

**VCEP Specifications:** **Not Applicable**

This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PMID: 29543229).

---

## Benign Criteria

### BA1 - Allele Frequency >0.1%

**Original ACMG Summary:** Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

**VCEP Specification (Stand Alone):**

| Strength | Criteria |
|----------|----------|
| **Stand Alone** | gnomAD MAF ≥ 0.001 (0.1%) |

---

### BS1 - Frequency Greater Than Expected

**Original ACMG Summary:** Allele frequency is greater than expected for disorder.

**VCEP Specification (Strong):**

| Strength | Criteria |
|----------|----------|
| **Strong** | gnomAD MAF ≥ 0.0005 but < 0.001 (0.05% to <0.1%) |

---

### BS2 - Observed in Healthy Adult

**Original ACMG Summary:** Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | Use this rule with 1 or more homozygotes who are unaffected (proven with aggregometry **OR** flow cytometry **AND** normal platelet count **AND** normal platelet size) |

---

### BS3 - Functional Studies (No Effect)

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | Must demonstrate normal aggregometry in a transgenic mouse model |
| **Supporting** | In a heterologous cell line, must demonstrate **BOTH** normal expression **AND** normal protein function as compared to wildtype |

---

### BS4 - Lack of Segregation

**Original ACMG Summary:** Lack of segregation in affected members of a family.

**Caveat:** The presence of phenocopies for common phenotypes (i.e., cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | Variant not tracking in an affected family member |

---

### BP1-BP7 - Benign Supporting

| Criterion | Status | Specification |
|-----------|--------|---------------|
| **BP1** | Not Applicable | Rule does not apply as truncating variants do not predominate and missense variants are a known cause of disease |
| **BP2** | Supporting | Use as written for recessive variants (i.e., variant must be observed in cis with a pathogenic variant) |
| **BP3** | Supporting | Use with no specification (in-frame deletions/insertions in a repetitive region without a known function) |
| **BP4** | Supporting | For a missense variant: apply when REVEL score ≤ 0.290 (based on Pejaver et al., 2022; PMID: 36413997) **AND** SpliceAI score = 0. **OR** for a synonymous or intronic variant: apply when SpliceAI score = 0. **Note:** Determine REVEL and SpliceAI cutoff before applying this code. Do not use if PP3 is applicable. |
| **BP5** | Not Applicable | Do not use this rule as an individual can be a carrier of an unrelated pathogenic variant for a recessive disorder |
| **BP6** | Not Applicable | This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PMID: 29543229) |
| **BP7** | Supporting | Use SpliceAI to rule out possible splicing defect (score ≤ 0.2) and reference PhyloP (score ≤ 1.5) to assess conservation. Can be used for intronic variants. Can be used in combination with BP4. |

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

### Combining Pathogenic and Benign Criteria (Point-Based System)

For GP1BB variants where criteria codes for both benign and pathogenic evidence apply, these variants are not subjected to an automatic VUS classification. Instead, apply the rule combination point system described by Tavtigian et al., 2020 (PMID: 32720330).

#### Point Values per Evidence Strength (Tavtigian et al., Table 2)

| Evidence Strength | Points |
|-------------------|--------|
| Very Strong (Pathogenic) | 8 |
| Strong (Pathogenic) | 4 |
| Moderate (Pathogenic) | 2 |
| Supporting (Pathogenic) | 1 |
| Supporting (Benign) | -1 |
| Strong (Benign) | -4 |
| Stand Alone (Benign) | -8 |

#### Classification Thresholds (Tavtigian et al., Table 3)

| Point Total | Classification |
|-------------|----------------|
| ≥10 | Pathogenic |
| 6-9 | Likely Pathogenic |
| 0-5 | VUS |
| -1 to -6 | Likely Benign |
| ≤-7 | Benign |

---

## Appendices

### Appendix A: Population Frequency Thresholds Summary

| Criterion | Threshold | Strength |
|-----------|-----------|----------|
| BA1 | ≥0.001 (0.1%) | Stand Alone |
| BS1 | ≥0.0005 to <0.001 (0.05% to <0.1%) | Strong |
| PM2 | ≤0.00006517 | Supporting |

### Appendix B: Computational Prediction Thresholds

| Tool | PP3_Moderate | PP3_Supporting | BP4 |
|------|--------------|----------------|-----|
| REVEL | ≥0.773 | ≥0.644 to <0.773 | ≤0.290 |
| SpliceAI | N/A | ≥0.5 | 0 |
| PhyloP (for BP7) | N/A | N/A | ≤1.5 |

### Appendix C: Critical Cysteine Residues for PM1

The following cysteine residues are critical for disulfide bond formation and can be used for PM1:
- **Cys93**
- **Cys95**
- **Cys118**
- **Cys141**
- **Cys147**

These residues are critical for:
- Interaction with GPIX (PMID: 12036872)
- Receptor binding to von Willebrand factor (PMID: 18647229)

### Appendix D: Reference PMIDs

| PMID | Description |
|------|-------------|
| 21173099 | Savoia A et al. Clinical and genetic aspects of Bernard-Soulier syndrome: searching for genotype/phenotype correlations. Haematologica (2011) |
| 25370924 | Bragadottir et al. Heterozygous BSS carrier phenotype |
| 36413997 | Pejaver et al. REVEL score recommendations (2022) |
| 29543229 | ClinGen SVI recommendations on PP5/BP6 |
| 32720330 | Tavtigian et al. Point-based classification system (2020) |
| 12036872 | Disulfide bond interaction with GPIX |
| 18647229 | Disulfide bond receptor binding to von Willebrand factor |

### Appendix E: Bernard-Soulier Syndrome Associated Genes

| Gene | HGNC ID | Protein |
|------|---------|---------|
| GP1BA | HGNC:4439 | Glycoprotein Ib platelet subunit alpha |
| GP1BB | HGNC:4440 | Glycoprotein Ib platelet subunit beta |
| GP9 | HGNC:4444 | Glycoprotein IX platelet |

---

## Version History

| Version | Date | Notes |
|---------|------|-------|
| 1.1.0 | 9/29/2025 | The BP4 rule was corrected to include less than "or equal to" |
| 1.0.0 | Initial | Initial release |

---

*This document was compiled from ClinGen VCEP specifications and ClinGen SVI recommendations. For the most current version, please refer to the ClinGen website.*
