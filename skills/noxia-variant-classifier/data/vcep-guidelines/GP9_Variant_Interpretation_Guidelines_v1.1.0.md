# ClinGen Platelet Disorders Expert Panel Variant Interpretation Guidelines for GP9

**Version:** 1.1.0
**Released:** 9/29/2025
**Affiliation:** Platelet Disorders VCEP
**Based on:** Richards et al., 2015 ACMG/AMP Guidelines

**Release Notes:** The BP4 rule was corrected to include less than "or equal to".

---

## Gene Information

| Attribute | Value |
|-----------|-------|
| **Gene** | GP9 (HGNC:4444) |
| **HGNC Name** | glycoprotein IX platelet |
| **Transcript** | NM_000174.5 |
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
   - [BA1 - Allele Frequency Stand Alone](#ba1---allele-frequency-stand-alone)
   - [BS1 - Frequency Greater Than Expected](#bs1---frequency-greater-than-expected)
   - [BS2 - Observed in Healthy Adult](#bs2---observed-in-healthy-adult)
   - [BS3 - Functional Studies (No Effect)](#bs3---functional-studies-no-effect)
   - [BS4 - Lack of Segregation](#bs4---lack-of-segregation)
   - [BP1-BP7 - Benign Supporting](#bp1-bp7---benign-supporting)
3. [Rules for Combining Criteria](#rules-for-combining-criteria)
4. [Guidance for Combining Conflicting Criteria](#guidance-for-combining-conflicting-criteria)
5. [Appendices](#appendices)

---

## Pathogenic Criteria

### PVS1 - Null Variant

**Original ACMG Summary:** Null variant (nonsense, frameshift, canonical +/-1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.

**Caveats:**
- Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7).
- Use caution interpreting LOF variants at the extreme 3' end of a gene.
- Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact.
- Use caution in the presence of multiple transcripts.

**VCEP Specifications:** Use GP9 modified decision tree as per SVI WG.

#### Strength Levels

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Very Strong** | Use GP9 modified decision tree as per SVI WG | Gene-specific |
| **Strong** | Use GP9 modified decision tree as per SVI WG | Gene-specific |
| **Moderate** | Use GP9 modified decision tree as per SVI WG | Gene-specific |
| **Supporting** | Use GP9 modified decision tree as per SVI WG | Gene-specific |

#### PVS1 Decision Tree for GP9

**Important Notes for GP9:**
- GP9 has a single coding exon which is not considered subject to NMD
- The transmembrane domain (amino acids 148-169) is considered critical to protein function
- Terminal-most PTV: NM_000174.5:c.450G>A (p.Trp150Ter) - Xu et al., 2010 (PMID: 20497174)

| Variant Type | Criteria | Outcome |
|--------------|----------|---------|
| **Nonsense or Frameshift** | Not predicted to undergo NMD (single coding exon); Exon is present in biologically-relevant transcript(s) | See below |
| - Truncated/altered region is critical to protein function (transmembrane domain aa 148-169) | | PVS1 |
| - Role of region in protein function is unknown | | PVS1_Strong |
| **GT-AG +/-1,2 splice sites** | Exon skipping or use of cryptic splice site disrupts reading frame and is predicted to undergo NMD; Exon is present in biologically-relevant transcript(s) | PVS1 |
| - Exon skipping or use of cryptic splice site preserves reading frame; Exon is present in biologically-relevant transcript(s) | | PVS1_Strong |
| - Exon is absent from biologically-relevant transcript(s) | | N/A |
| **Deletion (Single exon to full gene)** | Single to multi exon deletion - disrupts reading frame and is predicted to undergo NMD; Exon is present in biologically-relevant transcript(s) | PVS1 |
| - Single to multi exon deletion - preserves reading frame; Exon is present in biologically-relevant transcript(s) | | PVS1_Strong |
| - Full gene deletion | | PVS1 |
| - Exon is absent from biologically-relevant transcript(s) | | N/A |
| **Duplication (>=1 exon, completely contained within gene)** | Proven in tandem; Reading frame disrupted and NMD predicted to occur | PVS1 |
| - Presumed in tandem; Reading frame presumed disrupted and NMD predicted to occur | | PVS1_Strong |
| - Proven not in tandem; No or unknown impact on reading frame and NMD | | N/A |
| **Initiation Codon** | No known alternative start codon in other transcripts | See below |
| - >=1 pathogenic variant(s) upstream of closest potential in-frame start codon at Met32 (NM_000174.5(GP9):c.70T>C (p.Cys24Arg) - ClinVar 13533, Pathogenic, 2 stars) | | PVS1_Moderate |
| - No pathogenic variant(s) upstream of closest potential in-frame start codon at Met32 | | PVS1_Supp |
| - Different functional transcript uses alternative start codon | | N/A |

---

### PS1 - Same Amino Acid Change

**Original ACMG Summary:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.

**Example:** Val->Leu caused by either G>C or G>T in the same codon.

**Caveat:** Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:**

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Strong** | Use as originally specified, but the comparison variant must reach a **pathogenic** classification using these rule specifications in order to apply code. | General recommendation |
| **Moderate** | Use as originally specified, but the comparison variant must reach a **likely pathogenic** classification using these rule specifications in order to apply code. | General recommendation |

---

### PS2 - De Novo (Confirmed)

**Original ACMG Summary:** De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.

**Note:** Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.

**VCEP Specifications:**
- Only applicable when proband has a known pathogenic or likely pathogenic variant according to the BSS rule specifications along with the de novo variant.
- Only use "highly specific phenotype" scoring if all three BSS genes (GP1BA, GP1BB, GP9) were sequenced. Otherwise use the "consistent but not highly specific" scoring.

#### PS2/PM6 Point System

| Phenotypic Consistency | Confirmed Parental Relationships (Maternity AND Paternity) | Unconfirmed Parental Relationships |
|------------------------|-----------------------------------------------------------|-----------------------------------|
| Phenotype highly specific for gene (use when all 3 BSS genes sequenced) | 2 points | 1 point |
| Phenotype consistent with gene but not highly specific (use when only 1-2 BSS genes sequenced) | 1 point | 0.5 points |

#### Evidence Strength Thresholds

| Total Points | Strength Level | Modification Type |
|--------------|----------------|-------------------|
| 0.5 | PS2_Supporting | Disease-specific |
| 1.0 | PS2_Moderate | Disease-specific |
| 2.0 | PS2_Strong | Disease-specific |
| 4.0 | PS2_VeryStrong | Disease-specific |

---

### PS3 - Functional Studies

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.

**Note:** Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.

**VCEP Specifications:**

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Strong** | In a transgenic animal model, must demonstrate minimal to no function. | Disease-specific |
| **Supporting** | Functional assays measuring quantity of GP9 expression on cell surface measured by flow cytometry analysis of GPIb and GPIX when there is absent or near absent expression, >75% reduction (see approved assay spreadsheet for more detail). | Disease-specific |

#### Approved Functional Assays for GP9 (PS3_Supporting)

All approved assays measure quantity of GP1b/GPIX expression on the cell surface by flow cytometry.

| PMID | First Author | Year | Cell System | Material | Threshold |
|------|--------------|------|-------------|----------|-----------|
| 8608225 | Garunee Sae-Tung | 1996 | CHO cells (either CHO-alpbeta or wild-type CHO cotransfected with GPIb-alpha and GPIb-beta) | Site-directed mutagenesis on pDX (Asp21Gly, Asn45Ser - legacy nomenclature) | >75% reduction from WT |
| 10527407 | Keijiroh Suzuki | 1999 | CHO-K1 cells cotransfected with GPIb-alpha and GPIb-beta | Site-directed mutagenesis on pcDNA3.1 (Phe71Ser - legacy nomenclature) | >75% reduction from WT |
| 10583255 | Shinji Kunishima | 2001 | CHO DUK- cells cotransfected with GPIb-alpha and GPIb-beta | Site-directed mutagenesis on pDX (Cys97Tyr, Cys73Tyr - legacy nomenclature) | >75% reduction from WT |
| 12100158 | Francois Lanza | 2002 | CHO K1- cells cotransfected with GPIb-alpha and GPIb-beta | Site-directed mutagenesis on pDX (Leu7Pro - legacy nomenclature) | >75% reduction from WT |
| 8972003 | Masaaki Noda | 1996 | 293 cells co-transfected with GPIb-beta | Site-directed mutagenesis cloned into pBK-EF (C73Y - legacy nomenclature) | >75% reduction from WT |

**Controls Used:**
- Positive control: wild-type GPIX
- Negative control: empty vector (in most studies)

---

### PS4 - Prevalence in Affected

**Original ACMG Summary:** The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.

**Note 1:** Relative risk (RR) or odds ratio (OR), as obtained from case-control studies, is >5.0 and the confidence interval around the estimate of RR or OR does not include 1.0.

**Note 2:** In instances of very rare variants where case-control studies may not reach statistical significance, the prior observation of the variant in multiple unrelated patients with the same phenotype, and its absence in controls, may be used as moderate level of evidence.

**VCEP Specifications:**

According to Bragadottir, et al, individuals heterozygous for Bernard-Soulier syndrome variants are considered informative due to measurable, quantitative abnormalities relevant to the disease (PMID: 25370924).

**Caveats:**
1. The variant must be sufficiently rare, meeting PM2_supporting
2. There must be an assumed unrelated biallelic BSS patient, meeting PP4, before heterozygotes are considered
3. A single proband of a family can be included in either PM3 (biallelic proband) or PS4 (monoallelic proband), not both
4. Any additional family members are not included in PS4, they may be considered for segregation in PP1

#### PS4 Scoring for Heterozygous Individuals

| Evidence Type | Points |
|---------------|--------|
| Significantly reduced surface expression of GP1b measured by flow cytometry | 0.5 pt |
| **OR** Giant platelets (MPD >7 microns) or macrothrombocytopenia (MPV >12 fL and platelet count <150x10^9/L) | 0.25 pt |

#### PS4 Evidence Strength Thresholds

| Total Points | Strength Level | Modification Type |
|--------------|----------------|-------------------|
| 1-1.75 | PS4_Supporting | Disease-specific |
| 2+ | PS4_Moderate | Disease-specific |

---

### PM1 - Mutational Hot Spot

**Original ACMG Summary:** Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.

**VCEP Specifications:** **Not Applicable**

**Comments:** Rule does not apply due to gene being polymorphic.

---

### PM2 - Absent from Controls

**Original ACMG Summary:** Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

**Caveat:** Population data for indels may be poorly called by next generation sequencing.

**VCEP Specification (Supporting only):**

| Strength | Threshold | Modification Type |
|----------|-----------|-------------------|
| **Supporting** | gnomAD MAF of less than or equal to **0.0000329** | Disease-specific, Gene-specific |

---

### PM3 - In Trans with Pathogenic

**Original ACMG Summary:** For recessive disorders, detected in trans with a pathogenic variant.

**Note:** This requires testing of parents (or offspring) to determine phase.

**VCEP Specifications:**
- *In trans* variants classified as variants of uncertain significance, as per the GP9 rule specifications, must meet PM2_supporting to be scored.
- Conversely, *in trans* variants that meet a pathogenic or likely pathogenic classification using the GP9 rule specifications do not have to meet PM2_supporting criteria; however, they cannot meet BS1 or BA1 criteria.

#### PM3 Point System (Per Proband)

| Classification/Zygosity of Other Variant | Confirmed in Trans | Phase Unknown |
|------------------------------------------|-------------------|---------------|
| Pathogenic variant | 1.0 | 0.5 |
| Likely pathogenic variant | 1.0 | 0.5 |
| Homozygous occurrence (non-consanguineous) | 0.5 | N/A |
| Homozygous occurrence (consanguineous or unknown) | 0.5 | N/A |
| VUS (must meet PM2_supporting; max total 0.5) | 0.25 | 0 |

#### PM3 Evidence Strength Thresholds

| Total Points | Strength Level | Modification Type |
|--------------|----------------|-------------------|
| 0.5 | PM3_Supporting | Disease-specific |
| 1.0 | PM3 (Moderate) | Disease-specific |
| 2.0 | PM3_Strong | Disease-specific |
| 4.0 | PM3_VeryStrong | Disease-specific |

---

### PM4 - Protein Length Changes

**Original ACMG Summary:** Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

**VCEP Specifications:**

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Moderate** | Use with no specification | No change |

---

### PM5 - Novel Missense at Same Residue

**Original ACMG Summary:** Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.

**Example:** Arg156His is pathogenic; now you observe Arg156Cys.

**Caveat:** Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:**

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Moderate** | Use as originally specified, but the comparison variant must reach a **pathogenic** classification using these rule specifications in order to apply code. | General recommendation |
| **Supporting** | Use as originally specified, but the comparison variant must reach a **likely pathogenic** classification using these rule specifications in order to apply code. | General recommendation |

---

### PM6 - De Novo (Assumed)

**Original ACMG Summary:** Assumed de novo, but without confirmation of paternity and maternity.

**VCEP Specifications:** **Not Applicable**

**Comments:** Use PS2 for de novo cases in lieu of this rule code.

---

### PP1 - Co-segregation

**Original ACMG Summary:** Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.

**Note:** May be used as stronger evidence with increasing segregation data.

**VCEP Specifications:**

For Bernard-Soulier syndrome (BSS), segregation of the variant in a pedigree is considered informative in the case of both additional relatives with BSS and in heterozygous relatives with measurable, quantitative abnormalities relevant to the disease.

**Caveat:** There must be a biallelic BSS patient, meeting PP4, before segregation points are awarded. Additionally, heterozygous relatives counted for PP1 must not be counted for PS4.

#### PP1 Segregation Scoring System

| Family Member Type | Points |
|-------------------|--------|
| (1) Proband | 0 points (proband should be accounted for in PP4 or PS4) |
| (2) BSS affected relative with the same biallelic variant(s) identified in the proband | 1 pt |
| (3) Relative heterozygous for the variant under assessment with a relevant measurable, quantitative abnormality | See below |
| - 3a. Significantly reduced surface expression of GP1b measured by flow cytometry | 0.5 pt |
| - **OR** 3b. Giant platelets (MPD >7 microns) or macrothrombocytopenia (MPV >12 fL and platelet count <150x10^9/L) | 0.25 pt |

**Note:** Only score one parent of a homozygous proband in a consanguineous pedigree.

#### PP1 Evidence Strength Thresholds

| Total Segregation Score | Strength Level | Modification Type |
|------------------------|----------------|-------------------|
| 1-1.75 points | PP1_Supporting | Disease-specific |
| 2-2.75 points | PP1_Moderate | Disease-specific |
| 3+ points | PP1_Strong | Disease-specific |

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

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Moderate** | REVEL score of **>=0.773** based on recommendations of Pejaver et al., 2022 (PMID: 36413997). | Gene-specific |
| **Supporting** | REVEL score of **>=0.644** (to <0.773), based on recommendations of Pejaver et al., 2022 (PMID: 36413997), **OR** suggested splicing effect using SpliceAI **>=0.5**. | Gene-specific |

---

### PP4 - Phenotype Specificity

**Original ACMG Summary:** Patient's phenotype or family history is highly specific for a disease with a single genetic etiology.

**VCEP Specifications:**

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Moderate** | Must meet **BOTH** criteria: (1) Proband with platelet aggregation study absent for ristocetin and present for all other agonists OR flow cytometry or Western blot less than 10% expression of GPIb-alpha; AND (2) Proband must have full sequencing of all three BSS genes (GP1BA, GP1BB and GP9) and deletion/duplication analysis. | Disease-specific |
| **Supporting** | Proband with platelet aggregation study absent for ristocetin and present for all other agonists, **OR** Flow cytometry or Western blot less than 10% expression of GPIb-alpha. | Disease-specific |

---

### PP5 - Reputable Source

**Original ACMG Summary:** Reputable source recently reports variant as pathogenic, but the evidence is not available to the laboratory to perform an independent evaluation.

**VCEP Specifications:** **Not Applicable**

This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PMID: 29543229).

---

## Benign Criteria

### BA1 - Allele Frequency Stand Alone

**Original ACMG Summary:** Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

**VCEP Specification (Stand Alone):**

| Strength | Threshold | Modification Type |
|----------|-----------|-------------------|
| **Stand Alone** | gnomAD MAF of greater than or equal to **0.001** (or 0.1%) | Gene-specific |

---

### BS1 - Frequency Greater Than Expected

**Original ACMG Summary:** Allele frequency is greater than expected for disorder.

**VCEP Specification:**

| Strength | Threshold | Modification Type |
|----------|-----------|-------------------|
| **Strong** | gnomAD MAF of greater than or equal to **0.0007** but less than **0.001** | Gene-specific |

---

### BS2 - Observed in Healthy Adult

**Original ACMG Summary:** Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

**VCEP Specifications:**

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Strong** | Use this rule with 1 or more homozygotes who are unaffected (proven with aggregometry OR flow cytometry AND normal platelet count AND normal platelet size). | Disease-specific |

---

### BS3 - Functional Studies (No Effect)

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

**VCEP Specifications:**

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Strong** | Must demonstrate normal aggregometry in a transgenic mouse model | Disease-specific |
| **Supporting** | In a heterologous cell line, must demonstrate BOTH normal expression and normal protein function as compared to wildtype. | Disease-specific |

---

### BS4 - Lack of Segregation

**Original ACMG Summary:** Lack of segregation in affected members of a family.

**Caveat:** The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.

**VCEP Specifications:**

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Strong** | Variant not tracking in an affected family member. | Disease-specific |

---

### BP1-BP7 - Benign Supporting

| Criterion | Status | Specification | Modification Type |
|-----------|--------|---------------|-------------------|
| **BP1** | Not Applicable | Rule does not apply as truncating variants do not predominate and missense variants are a known cause of disease. | N/A |
| **BP2** | Supporting | Use as written for recessive variants (i.e. - variant must be observed in cis with a pathogenic variant) | Disease-specific |
| **BP3** | Supporting | Use with no specification | None |
| **BP4** | Supporting | For a missense variant apply when REVEL score is **<=0.290**, based on recommendations of Pejaver et al., 2022 (PMID: 36413997) **AND** SpliceAI score is zero. **OR** for a synonymous or intronic variant apply when SpliceAI score is zero. Do not use if PP3 is applicable. | Gene-specific |
| **BP5** | Not Applicable | Do not use this rule as an individual can be a carrier of an unrelated pathogenic variant for a recessive disorder. | N/A |
| **BP6** | Not Applicable | This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PMID: 29543229). | N/A |
| **BP7** | Supporting | Use SpliceAI to rule out possible splicing defect (score = 0.2 or less) and reference PhyloP (score = 1.5 or less) to assess conservation. Can be used for intronic variants. Can be used along with BP4. | Gene-specific |

---

## Rules for Combining Criteria

### Pathogenic Classification

| Criteria Combination |
|---------------------|
| 1 Very Strong **AND** >=1 Strong |
| 1 Very Strong **AND** >=2 Moderate |
| 1 Very Strong **AND** 1 Moderate **AND** 1 Supporting |
| 1 Very Strong **AND** >=2 Supporting |
| >=2 Strong |
| 1 Strong **AND** >=3 Moderate |
| 1 Strong **AND** 2 Moderate **AND** >=2 Supporting |
| 1 Strong **AND** 1 Moderate **AND** >=4 Supporting |

### Likely Pathogenic Classification

| Criteria Combination |
|---------------------|
| 1 Very Strong **AND** 1 Moderate |
| 1 Strong **AND** 1 Moderate |
| 1 Strong **AND** >=2 Supporting |
| >=3 Moderate |
| 2 Moderate **AND** >=2 Supporting |
| 1 Moderate **AND** >=4 Supporting |
| 1 Strong **AND** 2 Moderate |

### Benign Classification

| Criteria Combination |
|---------------------|
| >=2 Strong |
| 1 Stand Alone (BA1) |

### Likely Benign Classification

| Criteria Combination |
|---------------------|
| 1 Strong **AND** 1 Supporting |
| >=2 Supporting |

---

## Guidance for Combining Conflicting Criteria

For GP9 variants where criteria codes for benign and pathogenic evidence apply, these variants are not subjected to an automatic variant of uncertain significance (VUS) classification. Instead, the VCEP recommends application of the rule combination point system described by Tavtigian et al., 2020 (PMID: 32720330).

### Evidence Code Point Values (Tavtigian et al., Table 2)

| Evidence Strength | Pathogenic Points | Benign Points |
|-------------------|-------------------|---------------|
| Very Strong | 8 | N/A |
| Strong | 4 | -4 |
| Moderate | 2 | N/A |
| Supporting | 1 | -1 |
| Stand Alone | N/A | -8 |

### Classification Based on Point Total (Tavtigian et al., Table 3)

| Point Total | Classification |
|-------------|----------------|
| >=10 | Pathogenic |
| 6-9 | Likely Pathogenic |
| 0-5 | VUS |
| -1 to -6 | Likely Benign |
| <=-7 | Benign |

**Instructions:**
1. Use the evidence code point values table to determine how many points each applied evidence code is worth
2. Sum all point values (pathogenic codes contribute positive points, benign codes contribute negative points)
3. Use the classification table to determine which variant classification corresponds to the summed point value

---

## Appendices

### Appendix A: PVS1 Flowchart Summary for GP9

```
GP9 PVS1 Decision Tree Key Points:
==================================

1. GP9 has a SINGLE CODING EXON - NOT subject to NMD

2. Critical Functional Region:
   - Transmembrane domain: amino acids 148-169

3. Reference Pathogenic Variant:
   - Terminal-most PTV: NM_000174.5:c.450G>A (p.Trp150Ter)
   - Source: Xu et al., 2010 (PMID: 20497174)

4. Initiation Codon Variants:
   - Closest potential in-frame start codon: Met32
   - Known pathogenic upstream variant: NM_000174.5(GP9):c.70T>C (p.Cys24Arg)
     ClinVar ID: 13533 (Pathogenic, 2 stars)

5. Strength Assignments:
   - Nonsense/Frameshift in critical region (aa 148-169): PVS1
   - Nonsense/Frameshift in region of unknown function: PVS1_Strong
   - Splice variants with confirmed reading frame disruption: PVS1
   - Full gene deletion: PVS1
   - Initiation codon with upstream P/LP variant: PVS1_Moderate
   - Initiation codon without upstream P/LP variant: PVS1_Supporting
```

### Appendix B: Population Frequency Thresholds Summary

| Criterion | Threshold | Strength | Direction |
|-----------|-----------|----------|-----------|
| BA1 | >=0.001 (0.1%) | Stand Alone | Benign |
| BS1 | >=0.0007 to <0.001 | Strong | Benign |
| PM2 | <=0.0000329 | Supporting | Pathogenic |

### Appendix C: Computational Prediction Thresholds Summary

| Tool | Pathogenic Threshold | Benign Threshold |
|------|---------------------|------------------|
| REVEL (missense) | >=0.773 (PP3_Moderate), >=0.644 (PP3_Supporting) | <=0.290 (BP4) |
| SpliceAI | >=0.5 (PP3_Supporting) | =0 (BP4), <=0.2 (BP7) |
| PhyloP | N/A | <=1.5 (BP7) |

### Appendix D: Point-Based Scoring Systems Summary

#### De Novo (PS2/PM6) Points

| Scenario | Points |
|----------|--------|
| Highly specific phenotype (all 3 BSS genes sequenced) + confirmed parentage | 2 |
| Highly specific phenotype + unconfirmed parentage | 1 |
| Consistent phenotype (1-2 BSS genes sequenced) + confirmed parentage | 1 |
| Consistent phenotype + unconfirmed parentage | 0.5 |

#### PM3 (In Trans) Points

| Scenario | Points |
|----------|--------|
| Confirmed in trans with P/LP | 1.0 |
| Phase unknown with P/LP | 0.5 |
| Homozygous (non-consanguineous) | 0.5 |
| Homozygous (consanguineous) | 0.5 |
| Confirmed in trans with VUS | 0.25 |

#### PS4/PP1 Segregation Points

| Evidence | Points |
|----------|--------|
| BSS-affected relative with same biallelic variants | 1.0 |
| Heterozygous relative with reduced GP1b by flow cytometry | 0.5 |
| Heterozygous relative with giant platelets/macrothrombocytopenia | 0.25 |

### Appendix E: Criteria Applicability Summary

| Criterion | Status | Notes |
|-----------|--------|-------|
| PVS1 | Applicable (with modifications) | Use GP9-specific decision tree |
| PS1 | Applicable | Requires P/LP comparison variant per these specs |
| PS2 | Applicable (point-based) | Use with PP4; requires BSS phenotype |
| PS3 | Applicable | Strong for animal models; Supporting for flow cytometry |
| PS4 | Applicable (point-based) | For heterozygous individuals only |
| PM1 | **Not Applicable** | Gene is polymorphic |
| PM2 | Applicable (Supporting only) | MAF <=0.0000329 |
| PM3 | Applicable (point-based) | For biallelic probands |
| PM4 | Applicable | No modification |
| PM5 | Applicable | Requires P/LP comparison variant per these specs |
| PM6 | **Not Applicable** | Use PS2 instead |
| PP1 | Applicable (point-based) | Requires PP4-meeting proband |
| PP2 | **Not Applicable** | Gene not constrained |
| PP3 | Applicable | REVEL and SpliceAI thresholds |
| PP4 | Applicable | Phenotype-based criteria |
| PP5 | **Not Applicable** | Per SVI recommendation |
| BA1 | Applicable | MAF >=0.001 |
| BS1 | Applicable | MAF >=0.0007 to <0.001 |
| BS2 | Applicable | Homozygotes only |
| BS3 | Applicable | Strong for animal models; Supporting for cell lines |
| BS4 | Applicable | Non-segregation in affected |
| BP1 | **Not Applicable** | Missense variants cause disease |
| BP2 | Applicable | In cis with pathogenic only |
| BP3 | Applicable | No modification |
| BP4 | Applicable | REVEL <=0.290 AND SpliceAI=0 |
| BP5 | **Not Applicable** | Carrier status possible |
| BP6 | **Not Applicable** | Per SVI recommendation |
| BP7 | Applicable | SpliceAI <=0.2 AND PhyloP <=1.5 |

### Appendix F: References

1. Savoia A, Pastore A et al. *Clinical and genetic aspects of Bernard-Soulier syndrome: searching for genotype/phenotype correlations.* **Haematologica** (2011) 96(3):417-23. DOI: 10.3324/haematol.2010.032631. PMID: 21173099

2. Bragadottir G et al. (2015) PMID: 25370924 - Heterozygous BSS carriers with measurable phenotypic abnormalities

3. Tavtigian SV et al. (2020) *Modeling the ACMG/AMP variant classification guidelines as a Bayesian classification framework.* PMID: 32720330

4. Pejaver V et al. (2022) *Calibration of computational tools for missense variant pathogenicity classification and ClinGen recommendations for PP3/BP4 criteria.* PMID: 36413997

5. ClinGen SVI Recommendation on PP5/BP6 (2018) PMID: 29543229

6. Xu L et al. (2010) PMID: 20497174 - Terminal PTV reference for GP9

**Functional Assay References (PS3_Supporting):**
- PMID: 8608225 (Sae-Tung, 1996)
- PMID: 10527407 (Suzuki, 1999)
- PMID: 10583255 (Kunishima, 2001)
- PMID: 12100158 (Lanza, 2002)
- PMID: 8972003 (Noda, 1996)

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.1.0 | 9/29/2025 | BP4 rule corrected to include less than "or equal to" |
| 1.0.0 | Initial | Initial release |

---

*This document was compiled from ClinGen Platelet Disorders VCEP specifications. For the most current version, please refer to the [ClinGen website](https://clinicalgenome.org/).*
