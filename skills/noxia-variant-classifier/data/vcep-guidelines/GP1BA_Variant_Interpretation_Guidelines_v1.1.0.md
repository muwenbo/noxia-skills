# ClinGen Platelet Disorders Expert Panel Variant Interpretation Guidelines for GP1BA

**Version:** 1.1.0
**Released:** 9/29/2025
**Affiliation:** Platelet Disorders VCEP
**Based on:** Richards et al., 2015 ACMG/AMP Guidelines

---

## Gene Information

| Attribute | Value |
|-----------|-------|
| **Gene** | GP1BA (HGNC:4439) |
| **HGNC Name** | Glycoprotein Ib platelet subunit alpha |
| **Transcript** | NM_000173.7 |
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
- Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7)
- Use caution interpreting LOF variants at the extreme 3' end of a gene
- Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact
- Use caution in the presence of multiple transcripts

**VCEP Specifications:** See GP1BA modified decision tree below. GP1BA has a single coding exon which is not considered subject to NMD.

#### Strength Levels

| Strength | Criteria |
|----------|----------|
| **Very Strong** | Use GP1BA modified decision tree as per SVI WG |
| **Strong** | Use GP1BA modified decision tree as per SVI WG |
| **Moderate** | Use GP1BA modified decision tree as per SVI WG |
| **Supporting** | Use GP1BA modified decision tree as per SVI WG |

#### PVS1 Decision Tree for GP1BA

**Nonsense or Frameshift:**
- GP1BA has a single coding exon which is NOT subject to NMD
- The transmembrane domain (amino acids 532-553) is critical to protein function
- If truncated/altered region is critical to protein function: **PVS1_Strong**
- If role of region in protein function is unknown: *Refer to specific guidelines*

**Canonical GT-AG +/-1,2 Splice Sites:**
- If exon skipping or use of cryptic splice site disrupts reading frame and is predicted to undergo NMD: **PVS1** (if exon present in biologically-relevant transcripts)
- If exon skipping or use of cryptic splice site preserves reading frame: Evaluate if exon is present in biologically-relevant transcripts

**Deletions (Single exon to full gene):**
- Full gene deletion: **PVS1**
- Single to multi exon deletion disrupting reading frame predicted to undergo NMD: **PVS1** (if exon present in biologically-relevant transcripts)

**Duplications (>=1 exon, completely contained within gene):**
- Proven in tandem with reading frame disrupted and NMD predicted: **PVS1**
- Presumed in tandem with reading frame presumed disrupted and NMD predicted: **PVS1_Strong**

**Initiation Codon:**
- No known alternative start codon in other transcripts
- If >=1 pathogenic variant(s) upstream of closest potential in-frame start codon at Met68: **PVS1_Supporting**
- If no pathogenic variant(s) upstream of closest potential in-frame start codon at Met68: **PVS1_Moderate**

**Note:** Terminal most PTV: NM_000173.7:c.1846_1852del (p.Asn616Valfs*5) - ClinVar 1703858 (Pathogenic, 1 star)

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

| Phenotypic Consistency | Confirmed Parental Relationships | Unconfirmed |
|------------------------|----------------------------------|-------------|
| Phenotype highly specific for gene (all 3 BSS genes sequenced) | 2 points | 1 point |
| Phenotype consistent but not highly specific (1-2 genes sequenced) | 1 point | 0.5 points |

#### Evidence Strength Thresholds

| Points | Strength Level |
|--------|----------------|
| 0.5 | PS2_Supporting |
| 1.0 | PS2_Moderate |
| 2.0 | PS2_Strong |
| 4.0 | PS2_VeryStrong |

---

### PS3 - Functional Studies

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.

**Note:** Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | In a transgenic animal model, must demonstrate minimal to no function |
| **Supporting** | Functional assays measuring quantity of GP1ba expression on cell surface measured by flow cytometry analysis of GPIb and GPIX when there is absent or near absent expression, >75% reduction |

#### Approved Assay Instances for GP1BA (PS3_Supporting)

| PMID | Year | Author | Assay Description | Threshold |
|------|------|--------|-------------------|-----------|
| 7579348 | 1995 | Li C | Transient transfection of mutant GPIba into mouse L-cell line stably expressing GPIbb and GPIX, measured by flow cytometry | >75% reduction from WT |
| 9326229 | 1997 | Kenny D | Transient transfection of mutant GPIba into 293T cells | >75% reduction from WT |
| 11054083 | 2001 | Afshar-Kharghan V | Mutant cDNAs expressed in CHOβIX cells (Chinese hamster ovary cells stably expressing GP Ibβ and GP IX) | >75% reduction from WT |
| 10928479 | 2000 | Ulsemer P | Wild type and mutated GPIba transfected into CHO cells expressing GPIbb and GPIX | >75% reduction from WT |
| 11776304 | 2001 | Gonzalez-Manchon C | CHOIBb-IX cells transiently transfected with pcDNA3 plasmid containing normal or mutant GPIb-cDNA | >75% reduction from WT |
| 17083647 | 2007 | Rosenberg N | BHK cells transfected with normal GPIbβ and GPIX cDNAs and either normal or mutant GPIbα | >75% reduction from WT |

**Readout:** Quantity of GP1ba expression on the cell surface, measured by flow cytometry

**Controls Required:**
- Positive control: wild-type GPIBA
- Negative control: empty vector/plasmid or untransfected cells

---

### PS4 - Prevalence in Affected

**Original ACMG Summary:** The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.

**VCEP Specifications:**
According to Bragadottir, et al, individuals heterozygous for Bernard-Soulier syndrome variants are considered informative due to measurable, quantitative abnormalities relevant to the disease (PMID: 25370924).

**Caveats:**
1. The variant must be sufficiently rare, meeting PM2_supporting
2. There must be an assumed unrelated biallelic BSS patient, meeting PP4, before heterozygotes are considered
3. A single proband of a family can be included in either PM3 (biallelic proband) or PS4 (monoallelic proband), not both
4. Any additional family members are not included in PS4; they may be considered for segregation in PP1

#### PS4 Scoring for Heterozygous Individuals

| Evidence Type | Points |
|---------------|--------|
| Significantly reduced surface expression of GP1b measured by flow cytometry | 0.5 pt |
| Giant platelets (MPD >7 microns) OR macrothrombocytopenia (MPV >12 fL AND platelet count <150x10^9/L) | 0.25 pt |

#### PS4 Evidence Strength Thresholds

| Total Points | Strength Level |
|--------------|----------------|
| 1-1.75 | PS4_Supporting |
| 2+ | PS4_Moderate |

---

### PM1 - Mutational Hot Spot

**Original ACMG Summary:** Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Moderate** | Disulfide bonds in GPIb are well-established as critical to function, both for interaction with GPIX (PMID: 12036872) and receptor binding to von Willebrand factor (PMID: 18647229). PM1 can be applied when the following cysteine residues (at which there are no known benign variants) are altered: **20, 33, 225, 227, 264, 280, 526, 527** |

---

### PM2 - Absent from Controls

**Original ACMG Summary:** Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

**Caveat:** Population data for indels may be poorly called by next generation sequencing.

**VCEP Specification (Supporting only):**
- gnomAD MAF **<= 0.0001114**

---

### PM3 - In Trans with Pathogenic

**Original ACMG Summary:** For recessive disorders, detected in trans with a pathogenic variant.

**Note:** This requires testing of parents (or offspring) to determine phase.

**VCEP Specifications:**
- In trans variants classified as a variant of uncertain significance (per GP1BA rule specifications) must meet PM2_supporting to be scored
- In trans variants that meet P/LP classification using GP1BA rule specifications do not have to meet PM2_supporting criteria; however, they cannot meet BS1 or BA1 criteria
- Both variants must be classified using these rule specifications

#### PM3 Point System (Per Proband)

| Classification/Zygosity of Other Variant | Confirmed in Trans | Phase Unknown |
|------------------------------------------|-------------------|---------------|
| Pathogenic variant | 1.0 | 0.5 |
| Likely pathogenic variant | 1.0 | 0.25 |
| Homozygous (non-consanguineous) | 1.0 | 1.0 |
| Homozygous (consanguineous, max 0.5/family) | 0.5 | 0.5 |
| VUS (max 0.5 total) | 0.25 | 0.0 |

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

**VCEP Specifications:** *Not Applicable*

**Comments:** Use PS2 for de novo cases in lieu of this rule code.

---

### PP1 - Co-segregation

**Original ACMG Summary:** Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.

**Note:** May be used as stronger evidence with increasing segregation data.

**VCEP Specifications:**
For Bernard-Soulier syndrome (BSS), segregation of the variant in a pedigree is considered informative in both:
- Additional relatives with BSS
- Heterozygous relatives with measurable, quantitative abnormalities relevant to the disease

**Caveats:**
- There must be a biallelic BSS patient, meeting PP4, before segregation points are awarded
- Heterozygotes used for PP1 cannot be applied to PS4

#### PP1 Segregation Scoring

| Evidence Type | Points |
|---------------|--------|
| Proband | 0 pt (proband should be accounted for in PP4 or PS4) |
| BSS affected relative with the same biallelic variant(s) identified in the proband | 1 pt |
| Relative heterozygous for the variant with significantly reduced surface expression of GP1b (flow cytometry) | 0.5 pt |
| Relative heterozygous for the variant with giant platelets (MPD >7 microns) OR macrothrombocytopenia (MPV >12 fL AND platelet count <150x10^9/L) | 0.25 pt |

**Note:** Only score one parent of a homozygous proband in a consanguineous pedigree.

#### PP1 Evidence Strength Thresholds

| Total Segregation Score | Strength Level |
|------------------------|----------------|
| 1-1.75 | PP1_Supporting |
| 2-2.75 | PP1_Moderate |
| 3+ | PP1_Strong |

---

### PP2 - Missense in Constrained Gene

**Original ACMG Summary:** Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.

**VCEP Specifications:** *Not Applicable*

**Comments:** This rule does not apply because BSS is a rare disease and this gene is not constrained for missense variation (gnomAD).

---

### PP3 - Computational Evidence

**Original ACMG Summary:** Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).

**Caveat:** As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Moderate** | REVEL score **>= 0.773** based on recommendations of Pejaver et al., 2022 (PMID: 36413997) |
| **Supporting** | REVEL score **>= 0.644** (to <0.773), based on recommendations of Pejaver et al., 2022 (PMID: 36413997) **OR** suggested splicing effect using SpliceAI **>= 0.5** |

---

### PP4 - Phenotype Specificity

**Original ACMG Summary:** Patient's phenotype or family history is highly specific for a disease with a single genetic etiology.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Moderate** | Must meet BOTH criteria: (1) Proband with platelet aggregation study absent for ristocetin and present for all other agonists OR flow cytometry or Western blot less than 10% expression of GPIba AND (2) Proband must have full sequencing of all three BSS genes (GP1BA, GP1BB and GP9) and deletion/duplication analysis |
| **Supporting** | Proband with platelet aggregation study absent for ristocetin and present for all other agonists **OR** flow cytometry or Western blot less than 10% expression of GPIba |

---

### PP5 - Reputable Source

**Original ACMG Summary:** Reputable source recently reports variant as pathogenic, but the evidence is not available to the laboratory to perform an independent evaluation.

**VCEP Specifications:** *Not Applicable*

This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PMID: 29543229).

---

## Benign Criteria

### BA1 - Allele Frequency >5%

**Original ACMG Summary:** Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

**VCEP Specification (Stand Alone):**
- gnomAD MAF **>= 0.001** (or 0.1%)

---

### BS1 - Frequency Greater Than Expected

**Original ACMG Summary:** Allele frequency is greater than expected for disorder.

**VCEP Specification (Strong):**
- gnomAD MAF **>= 0.0005** but **< 0.001**

---

### BS2 - Observed in Healthy Adult

**Original ACMG Summary:** Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | Use this rule with 1 or more homozygotes who are unaffected (proven with aggregometry OR flow cytometry AND normal platelet count AND normal platelet size) |

---

### BS3 - Functional Studies (No Effect)

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | Must demonstrate normal aggregometry in a transgenic mouse model |
| **Supporting** | In a heterologous cell line, must demonstrate BOTH normal expression and normal protein function as compared to wildtype |

---

### BS4 - Lack of Segregation

**Original ACMG Summary:** Lack of segregation in affected members of a family.

**Caveat:** The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | Variant not tracking in an affected family member |

---

### BP1-BP7 - Benign Supporting

| Criterion | Status | Specification |
|-----------|--------|---------------|
| **BP1** | *Not Applicable* | Rule does not apply as truncating variants do not predominate and missense variants are a known cause of disease |
| **BP2** | Supporting | Use as written for recessive variants (i.e., variant must be observed in cis with a pathogenic variant) |
| **BP3** | Supporting | Use with no specification |
| **BP4** | Supporting | For a missense variant: apply when REVEL score **<= 0.290** (PMID: 36413997) AND SpliceAI score is zero. For a synonymous or intronic variant: apply when SpliceAI score is zero. **Note:** Determine REVEL and SpliceAI cutoff before applying this code. Do not use if PP3 is met. |
| **BP5** | *Not Applicable* | Do not use this rule as an individual can be a carrier of an unrelated pathogenic variant for a recessive disorder |
| **BP6** | *Not Applicable* | This criterion is not for use as recommended by the ClinGen SVI VCEP Review Committee (PMID: 29543229) |
| **BP7** | Supporting | Use SpliceAI to rule out possible splicing defect (score **<= 0.2**) and reference PhyloP (score **<= 1.5**) to assess conservation. Can be used for intronic variants. Can be used in combination with BP4. |

---

## Rules for Combining Criteria

### Pathogenic Classification

| Criteria Combination |
|---------------------|
| 1 Very Strong **AND** >= 1 Strong |
| 1 Very Strong **AND** >= 2 Moderate |
| 1 Very Strong **AND** 1 Moderate **AND** 1 Supporting |
| 1 Very Strong **AND** >= 2 Supporting |
| >= 2 Strong |
| 1 Strong **AND** >= 3 Moderate |
| 1 Strong **AND** 2 Moderate **AND** >= 2 Supporting |
| 1 Strong **AND** 1 Moderate **AND** >= 4 Supporting |

### Likely Pathogenic Classification

| Criteria Combination |
|---------------------|
| 1 Very Strong **AND** 1 Moderate |
| 1 Strong **AND** 1 Moderate |
| 1 Strong **AND** >= 2 Supporting |
| >= 3 Moderate |
| 2 Moderate **AND** >= 2 Supporting |
| 1 Moderate **AND** >= 4 Supporting |
| 1 Strong **AND** 2 Moderate |

### Benign Classification

| Criteria Combination |
|---------------------|
| >= 2 Strong |
| 1 Stand Alone (BA1) |

### Likely Benign Classification

| Criteria Combination |
|---------------------|
| 1 Strong **AND** 1 Supporting |
| >= 2 Supporting |

### Combining Pathogenic and Benign Evidence

For GP1BA variants where criteria codes for both benign and pathogenic evidence apply, these variants are NOT subjected to an automatic VUS classification. Instead, apply the rule combination point system described by Tavtigian et al. 2020 (PMID: 32720330).

#### Evidence Point Values (Tavtigian et al. Table 2)

| Evidence Strength | Points |
|-------------------|--------|
| Very Strong | 8 |
| Strong | 4 |
| Moderate | 2 |
| Supporting | 1 |

**For benign evidence, use negative values:**
| Evidence Strength | Points |
|-------------------|--------|
| Strong Benign | -4 |
| Supporting Benign | -1 |
| Stand Alone (BA1) | -8 |

#### Classification Thresholds (Tavtigian et al. Table 3)

| Point Sum | Classification |
|-----------|---------------|
| >= 10 | Pathogenic |
| 6 to 9 | Likely Pathogenic |
| 0 to 5 | VUS |
| -1 to -6 | Likely Benign |
| <= -7 | Benign |

---

## Appendices

### Appendix A: Population Frequency Thresholds Summary

| Criterion | Threshold | Strength |
|-----------|-----------|----------|
| BA1 | >= 0.001 (0.1%) | Stand Alone |
| BS1 | >= 0.0005 to < 0.001 | Strong |
| PM2 | <= 0.0001114 | Supporting |

### Appendix B: Computational Predictor Thresholds Summary

| Predictor | PP3_Moderate | PP3_Supporting | BP4 |
|-----------|--------------|----------------|-----|
| REVEL | >= 0.773 | >= 0.644 to < 0.773 | <= 0.290 |
| SpliceAI | - | >= 0.5 | = 0 |

**For BP7:**
- SpliceAI: <= 0.2
- PhyloP: <= 1.5

### Appendix C: Critical Cysteine Residues for PM1

The following cysteine residues form disulfide bonds critical for protein function and can be used for PM1_Moderate when altered:

**Cysteine positions:** 20, 33, 225, 227, 264, 280, 526, 527

### Appendix D: Key Functional Domains

| Domain | Amino Acid Position | Significance |
|--------|---------------------|--------------|
| Transmembrane domain | 532-553 | Critical to protein function (relevant for PVS1 assessment) |

### Appendix E: Reference PMIDs

| PMID | Reference |
|------|-----------|
| 21173099 | Savoia A, Pastore A, et al. Clinical and genetic aspects of Bernard-Soulier syndrome: searching for genotype/phenotype correlations. Haematologica (2011) 96(3):417-23 |
| 25370924 | Bragadottir G, et al. (Heterozygote evidence for PS4) |
| 12036872 | Disulfide bonds - GPIX interaction |
| 18647229 | Disulfide bonds - VWF binding |
| 36413997 | Pejaver V, et al. 2022 (REVEL thresholds) |
| 29543229 | ClinGen SVI recommendations on PP5/BP6 |
| 32720330 | Tavtigian SV, et al. 2020 (Point-based combining rules) |

---

## Version History

| Version | Date | Notes |
|---------|------|-------|
| 1.1.0 | 9/29/2025 | BP4 rule was corrected to include less than "or equal to" |
| 1.0.0 | Initial release | Original specifications |

---

*This document was compiled from ClinGen VCEP specifications. For the most current version, please refer to the ClinGen website.*
