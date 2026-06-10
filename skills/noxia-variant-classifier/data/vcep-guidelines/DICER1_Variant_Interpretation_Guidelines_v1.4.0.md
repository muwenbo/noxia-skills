# ClinGen DICER1 and miRNA-Processing Gene Expert Panel Variant Interpretation Guidelines for DICER1

**Version:** 1.4.0
**Released:** 7/8/2025
**Affiliation:** DICER1 and miRNA-Processing Gene VCEP
**Type:** Tavtigian et al., 2020 - Bayesian adaptation of Richards et al., 2015
**Publication:** https://www.hindawi.com/journals/humu/2023/9537832/

---

## Gene Information

| Attribute | Value |
|-----------|-------|
| **Gene** | DICER1 (HGNC:17098) |
| **HGNC Name** | dicer 1, ribonuclease III |
| **Transcript** | NM_177438.2 |
| **Disease** | DICER1-related tumor predisposition (MONDO:0100216) |
| **Inheritance** | Autosomal dominant |

---

## Table of Contents

1. [Point-Based Classification System](#point-based-classification-system)
2. [Pathogenic Criteria](#pathogenic-criteria)
   - [PVS1 - Null Variant](#pvs1---null-variant)
   - [PS1 - Same Amino Acid Change](#ps1---same-amino-acid-change)
   - [PS2 - De Novo](#ps2---de-novo)
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
4. [Phenotype Tables](#phenotype-tables)
5. [Appendices](#appendices)

---

## Point-Based Classification System

This VCEP uses the Tavtigian et al. (2020) Bayesian point-based system for variant classification.

### Evidence Point Values

| Evidence Type | Supporting | Moderate | Strong | Very Strong |
|---------------|------------|----------|--------|-------------|
| **Pathogenic** | +1 | +2 | +4 | +8 |
| **Benign** | -1 | -2 | -4 | -8 |

### Classification Thresholds

| Category | Point Range |
|----------|-------------|
| **Pathogenic** | ≥10 |
| **Likely Pathogenic** | 6 to 9 |
| **Uncertain Significance** | 0 to 5 |
| **Uncertain with caveat*** | -1 |
| **Likely Benign** | -2 to -6 |
| **Benign** | ≤-7 |

> *A final point value of -1 may be overridden to Likely Benign in cases where at least 2 benign evidence codes are applied AND PM2_Supporting is the only pathogenic code applied.

---

## Pathogenic Criteria

### PVS1 - Null Variant

**Original ACMG Summary:** Null variant (nonsense, frameshift, canonical ±1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.

**Caveats:**
- Beware of genes where LOF is not a known disease mechanism (e.g., GFAP, MYH7)
- Use caution interpreting LOF variants at the extreme 3' end of a gene
- Use caution with splice variants predicted to lead to exon skipping but leave the remainder of the protein intact
- Use caution in the presence of multiple transcripts

**VCEP Specifications:**

Follow SVI guidance using DICER1-specific information per the PVS1 workflow guidance provided in Tayoun et al. 2018.

#### Nonsense or Frameshift Variants

| Condition | Strength | Points |
|-----------|----------|--------|
| Predicted to undergo NMD (stop codon 5' of p.Pro1850) | **PVS1** | 8 |
| Not predicted to undergo NMD (stop codon 3' of p.Pro1850) | **PVS1_Moderate** | 2 |

#### Canonical Splice Variants (±1,2 intronic positions)

| Condition | Strength | Points |
|-----------|----------|--------|
| Exon skipping disrupts reading frame + NMD predicted (stop 5' of p.Pro1850) | **PVS1** | 8 |
| Exon skipping disrupts reading frame, NOT predicted to undergo NMD, variant removes >10% protein (≥193 AAs) | **PVS1_Strong** | 4 |
| Exon skipping disrupts reading frame, NOT predicted to undergo NMD, variant removes <10% protein (exon 27 SAS - final exon) | **PVS1_Moderate** | 2 |
| Exon 10 SDS/SAS (in-frame but exon includes >10% protein) | **PVS1_Strong** | 4 |
| Exons 5, 15, 18, 22 SDS/SAS (in-frame and each <10% of protein) | **PVS1_Moderate** | 2 |
| Exon 27 SAS (final exon) | **PVS1_Moderate** | 2 |
| Exon 1 (non-coding) | **N/A** | - |

#### Deletions (Single Exon to Full Gene)

| Condition | Strength | Points |
|-----------|----------|--------|
| Full gene deletion | **PVS1** | 8 |
| Single to multi exon deletion - disrupts reading frame + NMD predicted (stop 5' of p.Pro1850) | **PVS1** | 8 |
| Single to multi exon deletion - disrupts reading frame, NOT predicted to undergo NMD, truncated region includes PM1 residue | **PVS1_Strong** | 4 |
| Single to multi exon deletion - disrupts reading frame, NOT predicted to undergo NMD, removes ≥193 AAs | **PVS1_Strong** | 4 |
| Single to multi exon deletion - disrupts reading frame, NOT predicted to undergo NMD, removes <193 AAs | **PVS1_Moderate** | 2 |
| Single to multi exon deletion - preserves reading frame, truncated region includes PM1 residue | **PVS1_Strong** | 4 |

#### Duplications (≥1 exon, completely contained within gene)

| Condition | Strength | Points |
|-----------|----------|--------|
| Proven in tandem - reading frame disrupted + NMD predicted (stop 5' of p.Pro1850) | **PVS1** | 8 |
| Proven in tandem - no or unknown impact on reading frame and NMD | **N/A** | - |
| Presumed in tandem - reading frame presumed disrupted + NMD predicted | **PVS1_Strong** | 4 |
| Proven not in tandem | **N/A** | - |

#### Initiation Codon Variants (p.M1?)

**Not Applicable** - p.M1 is not highly conserved, there are three in-frame possible alternate start codons (p.Met11, p.Met17, p.Met24), and multiple lab cases of p.Met1? without DICER1 phenotype.

> **Note:** Do not apply PS3 at any strength if PVS1 is applied at full strength. If PP3 is applicable to canonical splice variants, it should not be used in combination with PVS1.

---

### PS1 - Same Amino Acid Change

**Original ACMG Summary:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.

**Example:** Val->Leu caused by either G>C or G>T in the same codon.

**Caveat:** Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:**

All variants should be assessed by MaxEntScan (MES) and SpliceAI for predicting de novo and cryptic splice sites. However, for predicting impact to consensus splice sites, SpliceAI scores alone should be considered for variants outside the MES validation threshold, as MES is not capable of predicting native splice site impact for such variants.

**MES Validation Threshold:**
- Donor sites: last 3 nucleotides of exon through intronic position +6
- Acceptor sites: intronic position -20 through first 3 nucleotides of exon

| Strength | Criteria | Points |
|----------|----------|--------|
| **Strong** | For same AA change, must confirm there is no difference in splicing using RNA data or in-silico modeling data (concordance of MaxEntScan and SpliceAI). For non-canonical intronic splicing variants at same nucleotide should have equal or worse splicing impact. **This rule code can only be used to compare variants asserted as pathogenic by the ClinGen DICER1 VCEP. Likely pathogenic changes do not apply.** | 4 |

---

### PS2 - De Novo

**Original ACMG Summary:** De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.

**Note:** Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.

**VCEP Specifications:**

De novo points should be tallied using the simplified table for tallying proband points and used to determine the applied strength of PS2, consistent with SVI guidance. **To avoid redundancy and increase consistency, the EP has opted to drop PM6 and exclusively use PS2 for de novo evidence.**

#### PS2 Point Thresholds

| Strength | Points Required | Default Point Value |
|----------|-----------------|---------------------|
| **Very Strong** | ≥4 de novo points | 8 |
| **Strong** | ≥2 but <4 de novo points | 4 |
| **Moderate** | ≥1 but <2 de novo points | 2 |
| **Supporting** | ≥0.5 but <1 de novo points | 1 |

#### Simplified Table for Tallying Proband Points (PS2 and PS4)

| Phenotypic Consistency | PS2 Confirmed | PS2 Assumed | PS4 | Proband Phenotype (use Phenotype Table) |
|------------------------|---------------|-------------|-----|----------------------------------------|
| Phenotype highly specific for gene | 2 | 1 | 1 | I. ≥1 High OR<br>II. ≥2 Moderate OR<br>III. 1 Moderate **AND**<br>&nbsp;&nbsp;&nbsp;A. 1-2 Low **OR**<br>&nbsp;&nbsp;&nbsp;B. High or Moderate in 1st or 2nd-degree relative (unless known not to carry variant)* |
| Phenotype consistent with gene but not highly specific | 1 | 0.5 | 0.5 | IV. 1 Moderate |
| Phenotype consistent with gene but not highly specific and high genetic heterogeneity** | 0.5 | 0.25 | 0 | V. ≥1 Low |

> \* If PP1 is applied and the proband's family contributed to the PP1 meiosis count, use IV (1 Moderate) instead of III.B to avoid double counting family history.
>
> \*\* Maximum allowable value of 1 may contribute to overall PS2 score to avoid counting multiple probands with only low-specificity phenotypes.

#### Code Strength Summary

| PS2 | PS4 | Total Points |
|-----|-----|--------------|
| Very Strong | Strong | ≥4 |
| Strong | Moderate | 2 to <4 |
| Moderate | Supporting | 1 to <2 |
| Supporting | N/A | 0.5 to <1 |

---

### PS3 - Functional Studies

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.

**Note:** Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.

**VCEP Specifications:**

This rule should be used and weighted appropriately for variants with functional evidence of a splicing impact and/or reduced DICER1 ability to cleave pre-miRNA. Follow SVI guidance regarding control numbers for functional studies. **Do not apply PS3 at any strength if PVS1 is applied at full strength.**

| Strength | Criteria | Points |
|----------|----------|--------|
| **Strong** | RNA assay shows splicing impact that is out-of-frame, in-frame ≥193 residues, or in-frame with RNase IIIb disruption. (PS3_Moderate if PVS1_Strong is applied) | 4 |
| **Moderate** | RNA assay shows in-frame splicing impact with change in protein length <193 residues AND RNase IIIb domain not disrupted | 2 |
| **Supporting** | In vitro cleavage assay shows failure or severely reduced capacity to produce either 5p or 3p microRNAs from a pre-miRNA (positive and negative controls also performed) | 1 |

---

### PS4 - Prevalence in Affected

**Original ACMG Summary:** The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.

**VCEP Specifications:**

Unrelated probands may contribute up to 1 point each based on phenotype (see Phenotype Table and Proband Points Table).

**Caveats:**
- Do not apply PS4 if variant meets BA1/BS1 criteria
- Do not apply points for a phenotype in an individual with a likely pathogenic germline variant in a second gene that could have reasonably contributed to the phenotype (e.g., Wilms tumor in an individual with a P/LP WT1 variant)
- Do not apply points for a proband whose tumor sequencing is consistent with a likely sporadic event (i.e., sequencing reveals a somatic, VCEP-curated, non-hotspot, likely pathogenic DICER1 variant in addition to a somatic hotspot variant and the germline variant under assessment)

**Exception:** DICER1 tumors that consistently or occasionally follow a classical 2-hit hypothesis (i.e., LOF of both alleles) are exempt from this caveat. For example, identification of a somatic pathogenic non-hotspot DICER1 variant in pineoblastoma, pituitary blastoma, and lung cysts or cystic nephroma lacking mesenchymal cells should not exclude the proband from PS4.

| Strength | Criteria | Points |
|----------|----------|--------|
| **Strong** | ≥4 phenotype points | 4 |
| **Moderate** | 2 – 3.5 phenotype points | 2 |
| **Supporting** | 1 – 1.5 phenotype points | 1 |

---

### PM1 - Mutational Hot Spot

**Original ACMG Summary:** Located in a mutational hot spot and/or critical and well-established functional domain (e.g., active site of an enzyme) without benign variation.

**VCEP Specifications:**

| Strength | Criteria | Points |
|----------|----------|--------|
| **Moderate** | Putative missense variants at residues affecting metal ion-binding: codons **p.S1344, p.E1705, p.D1709, p.D1713, p.G1809, p.D1810, p.E1813** | 2 |
| **Supporting** | Putative missense variants at residues in the RNase IIIb domain (p.Y1682 – p.S1846), besides the metal ion-binding residues (see PM1) | 1 |

---

### PM2 - Absent from Controls

**Original ACMG Summary:** Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

**Caveat:** Population data for indels may be poorly called by next generation sequencing.

**VCEP Specifications:**

In general, the most recent/most comprehensive gnomAD version should be used.

| Strength | Criteria | Points |
|----------|----------|--------|
| **Supporting** | Allele frequency <0.000005 across gnomAD with no more than one allele in any subpopulation and at least 20x coverage | 1 |

---

### PM3 - In Trans with Pathogenic

**Original ACMG Summary:** For recessive disorders, detected in trans with a pathogenic variant.

**VCEP Specifications:** **Not Applicable** - Autosomal dominant inheritance.

---

### PM4 - Protein Length Changes

**Original ACMG Summary:** Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

**VCEP Specifications:**

| Strength | Criteria | Points |
|----------|----------|--------|
| **Moderate** | In-frame indels with a residue within the RNase IIIb domain (p.Y1682 – p.S1846) | 2 |
| **Supporting** | In-frame indels outside of the RNase IIIb domain (p.Y1682 – p.S1846) and repeat regions (p.D606-p.D609; p.E1418-p.E1420; p.E1422-p.E1425) | 1 |

---

### PM5 - Novel Missense at Same Residue

**Original ACMG Summary:** Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.

**Example:** Arg156His is pathogenic; now you observe Arg156Cys.

**Caveat:** Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:**

All variants should be assessed by MaxEntScan (MES) and SpliceAI for predicting de novo and cryptic splice sites. See PS1 for MES validation threshold details.

| Strength | Criteria | Points |
|----------|----------|--------|
| **Moderate** | Missense variant under evaluation should have equal or worse Grantham score. Splicing should be ruled out with either RNA data or agreement in splicing predictors (MaxEntScan and SpliceAI) that show no splicing effects. The other variant must be interpreted as pathogenic by the ClinGen DICER1 VCEP. Likely pathogenic changes do not apply. **This rule cannot be applied in combination with PM1 or PS1.** | 2 |

---

### PM6 - De Novo (Assumed)

**Original ACMG Summary:** Assumed de novo, but without confirmation of paternity and maternity.

**VCEP Specifications:** **Not Applicable** - Combined with PS2. Use PS2 instead of PM6.

---

### PP1 - Co-segregation

**Original ACMG Summary:** Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.

**Note:** May be used as stronger evidence with increasing segregation data.

**VCEP Specifications:**

Phenotype-positive individuals should have high, moderate, or low-specificity phenotypes (see phenotype table).

**Caveat:** Segregation with a single low-specificity phenotype across multiple individuals (e.g., familial Wilms tumor) does not fulfill PP1. Do not apply PP1 if variant meets BA1/BS1 criteria.

| Strength | Criteria | Points |
|----------|----------|--------|
| **Strong** | ≥7 meioses across ≥2 families | 4 |
| **Moderate** | 5 – 6 meioses across ≥1 family | 2 |
| **Supporting** | 3 – 4 meioses across ≥1 family | 1 |

---

### PP2 - Missense in Constrained Gene

**Original ACMG Summary:** Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.

**VCEP Specifications:** **Not Applicable**

While DICER1 does meet recommended cutoff for missense constraint z score of ≥3.09 established by the SVI (4.23 on gnomAD), the VCEP recommends this rule not be used for DICER1 due to the presence of various missense variants throughout the gene that are clinically interpreted as benign (9) or likely benign (30) in ClinVar.

---

### PP3 - Computational Evidence

**Original ACMG Summary:** Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).

**Caveat:** As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.

**VCEP Specifications:**

All variants should be assessed by MaxEntScan (MES) and SpliceAI for predicting de novo and cryptic splice sites. See PS1 for MES validation threshold details.

| Strength | Criteria | Points |
|----------|----------|--------|
| **Supporting** | For missense variants: REVEL score ≥0.750 **OR** agreement in splicing predictors predict splicing effects. For splicing variants: concordance of MaxEntScan and SpliceAI. | 1 |

---

### PP4 - Phenotype Specificity

**Original ACMG Summary:** Patient's phenotype or family history is highly specific for a disease with a single genetic etiology.

**VCEP Specifications:**

Somatic tumor testing identifies somatic hotspot second hit and no additional somatic LOF variants. Tumor testing of a neoplasm with known DICER1 association in a proband who carries the germline variant under evaluation reveals the following:

| Strength | Criteria | Points |
|----------|----------|--------|
| **Supporting** | A previously reported somatic second hit of DICER1 in an RNase IIIb-disrupting "hotspot" codon (p.S1344, p.E1705, p.D1709, p.D1713, p.G1809, p.D1810, or p.E1813) **AND** Retention of the germline DICER1 variant under evaluation | 1 |

**PP4 is NOT applicable if:**
- The germline variant is a missense variant in one of the seven RNase IIIb "hotspot" codons (see PM1), **OR**
- Somatic sequencing reveals additional DICER1 non-hotspot variants (could be consistent with sporadic tumorigenesis)

#### PP4 Flowchart Decision Logic

```
Is germline variant a missense in one of the seven DICER1 hotspot codons
(p.S1344, p.E1705, p.D1709, p.D1713, p.G1809, p.D1810, or p.E1813)?
│
├── YES → PP4 Not Applicable
│
└── NO → Does somatic sequencing of DICER1-associated neoplasm show
          retention of germline variant AND acquisition of a previously
          reported somatic second hit in one of the DICER1 hotspot codons?
          │
          ├── NO → PP4 Not Applicable
          │
          └── YES → Does somatic sequencing reveal additional DICER1
                    non-hotspot variants besides the germline variant?
                    │
                    ├── YES → PP4 Not Applicable (possibly sporadic tumorigenesis)
                    │
                    └── NO → PP4 Applicable
```

#### Previously Reported Somatic Second Hits

(PMIDs: 31342592; 23620094; 28825729)

| Codon | Wild-Type | Reported Alternate Amino Acids |
|-------|-----------|-------------------------------|
| **1344** | Ser (S) | Leu (L) |
| **1705** | Glu (E) | Asp (D), Gln (Q), Lys (K), Val (V) |
| **1709** | Asp (D) | Asn (N), Glu (E), Gly (G), Tyr (Y), Val (V) |
| **1713** | Asp (D) | Val (V) |
| **1809** | Gly (G) | Arg (R), Glu (E), Trp (W) |
| **1810** | Asp (D) | Asn (N), Gly (G), His (H), Tyr (Y), Val (V) |
| **1813** | Glu (E) | Ala (A), Asp (D), Gln (Q), Gly (G), Lys (K), Val (V) |

---

### PP5 - Reputable Source

**Original ACMG Summary:** Reputable source recently reports variant as pathogenic, but the evidence is not available to the laboratory to perform an independent evaluation.

**VCEP Specifications:** **Not Applicable**

This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee. (PubMed: 29543229)

---

## Benign Criteria

### BA1 - Allele Frequency >0.3%

**Original ACMG Summary:** Allele frequency is above 5% in population databases.

**VCEP Specifications:**

In general, the most recent/most comprehensive gnomAD version should be used.

| Strength | Criteria | Points |
|----------|----------|--------|
| **Stand Alone** | Frequency >0.003 (0.3%) in gnomAD subpopulations. Subpopulations must have >2,000 alleles tested and a minimum of 5 alleles present. | N/A (Stand Alone) |

---

### BS1 - Frequency Greater Than Expected

**Original ACMG Summary:** Allele frequency is greater than expected for disorder.

**VCEP Specifications:**

In general, the most recent/most comprehensive gnomAD version should be used.

| Strength | Criteria | Points |
|----------|----------|--------|
| **Strong** | Frequency >0.0003 (0.03%) in gnomAD subpopulations. Subpopulations must have >2,000 alleles tested and a minimum of 5 alleles present. | -4 |

---

### BS2 - Observed in Healthy Adult

**Original ACMG Summary:** Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

**VCEP Specifications:**

| Strength | Criteria | Points |
|----------|----------|--------|
| **Strong** | 40+ unrelated females from a single source are tumor-free through age 50 (caveat: ratio of BS2-eligible females to PS4-eligible probands must be ≥40:1) **OR** 2+ observations of homozygosity in healthy individuals **OR** 1+ observation(s) of homozygosity in a healthy individual with status confirmed by parental testing | -4 |
| **Supporting** | 10+ unrelated females from a single source are tumor-free through age 50 (caveat: ratio of BS2-eligible females to PS4-eligible probands must be ≥10:1) **OR** 2+ observations of homozygosity in individuals lacking clinical information | -1 |

---

### BS3 - Functional Studies (No Effect)

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

**VCEP Specifications:**

This rule should be used and weighted appropriately for variants with functional evidence of no splicing impact and/or no reduced DICER1 ability to cleave pre-miRNA. Follow SVI guidance regarding control numbers for functional studies.

| Strength | Criteria | Points |
|----------|----------|--------|
| **Strong** | For intronic or synonymous variants, no splicing impact observed via RNA assay. (Should be observed more than once.) | -4 |
| **Supporting** | An in vitro cleavage assay must demonstrate the variant produces both 5p and 3p microRNAs from a pre-miRNA (positive and negative controls also performed). An example of an appropriate assay to which criteria could be applied is Wu et al. 2018. | -1 |

---

### BS4 - Lack of Segregation

**Original ACMG Summary:** Lack of segregation in affected members of a family.

**Caveat:** The presence of phenocopies for common phenotypes (i.e., cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.

**VCEP Specifications:**

| Strength | Criteria | Points |
|----------|----------|--------|
| **Strong** | Family members should be phenotype-positive (must be high- or moderate-specificity phenotype; see phenotype table), genotype-negative 1st, 2nd, or 3rd degree relatives of the proband. | -4 |

---

### BP1-BP7 - Benign Supporting

| Criterion | Status | Specification | Points |
|-----------|--------|---------------|--------|
| **BP1** | Not Applicable | This rule code does not apply to this gene, as truncating variants account for only a portion of disease-causing variants. | - |
| **BP2** | Supporting | ≥1 observation in trans with P/LP DICER1 variant **OR** ≥3 observations in cis or phase unknown with 2+ different P/LP DICER1 variants. | -1 |
| **BP3** | Not Applicable | Not applicable at this time. | - |
| **BP4** | Supporting | For missense variants: REVEL score <0.500 and agreement in splicing predictors that no splicing effects are predicted. For synonymous/intronic/non-coding variants: concordance of MaxEntScan and SpliceAI. | -1 |
| **BP5** | Not Applicable | Given the broad spectrum of DICER1-related neoplasms and the lack of evidence of other high-penetrance germline variants that could account for such neoplasms (except perhaps for some already low-specificity phenotypes such as Wilms tumor), this rule should not be used at this time. | - |
| **BP6** | Not Applicable | This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee. (PubMed: 29543229) | - |
| **BP7** | Supporting | Silent variant **OR** Intronic variant at or beyond +7 to -21 positions **OR** Other intronic or non-coding variant if the variant is the reference nucleotide in ≥1 primate and/or ≥4 mammalian species. **Caveat:** Variant must meet BP4 to apply BP7 | -1 |

---

## Phenotype Tables

### DICER1 Phenotype Specificity Table

*For use with PS4, PS2, PP1, PP4, BS4*

| Specificity | Phenotypes |
|-------------|------------|
| **High-specificity** *(much more likely than not to have germline P/LP DICER1)* | PPB (Including Type 1r)<br>Pituitary Blastoma<br>Anaplastic renal sarcoma<br>Ciliary body medulloepithelioma<br>Cystic nephroma (<18 yrs)<br>Embryonal rhabdomyosarcoma (Ovarian)<br>Embryonal rhabdomyosarcoma (Cervix) |
| **Moderate-specificity** *(more likely than not to have germline P/LP DICER1)* | Differentiated thyroid cancer and/or Multinodular goiter (<18 years)<br>Nasal chondromesenchymal hamartoma<br>Ovarian Sertoli-Leydig cell tumors<br>Ovarian sex-cord stromal tumor of mixed type (specifically, gynandroblastoma) |
| **Low-specificity** *(less likely to have DICER1)* | Non-parasitic liver cysts (childhood)<br>Wilms tumor<br>Pineoblastoma<br>Cerebral sarcoma<br>Lung cysts (<18 yrs) |
| **For PP4 use ONLY** *(Additional neoplasms of very low or undetermined specificity)* | Thyroid neoplasms (any age)<br>Sarcomas<br>Juvenile hamartomatous polyps<br>Primitive neuroectodermal/neuroepithelial neoplasms<br>Infantile cerebellar embryonal tumors<br>Fetal lung adenocarcinoma |

---

## Appendices

### Appendix A: PVS1 Decision Tree

The DICER1-specific PVS1 decision tree follows the Tayoun et al. 2018 framework with the following key parameters:

**Key Parameters:**
- **NMD Cutoff:** p.Pro1850
- **Biologically-relevant transcript:** NM_177438.2
- **10% protein threshold:** ≥193 amino acids
- **Critical functional residues (PM1):** p.S1344, p.E1705, p.D1709, p.D1713, p.G1809, p.D1810, p.E1813

**In-frame exons:** 5, 10, 15, 18, 22

### Appendix B: Population Frequency Thresholds Summary

| Criterion | Threshold | Strength | Points |
|-----------|-----------|----------|--------|
| **BA1** | >0.003 (0.3%) | Stand Alone | N/A |
| **BS1** | >0.0003 (0.03%) | Strong | -4 |
| **PM2** | <0.000005 (0.0005%) | Supporting | 1 |

**Requirements for BA1/BS1:**
- Subpopulations must have >2,000 alleles tested
- Minimum of 5 alleles present

**Requirements for PM2:**
- No more than one allele in any subpopulation
- At least 20x coverage

### Appendix C: Computational Prediction Tools

| Tool | Use Case | Threshold |
|------|----------|-----------|
| **REVEL** | Missense variant pathogenicity | ≥0.750 for PP3; <0.500 for BP4 |
| **MaxEntScan (MES)** | Splicing prediction | Used in combination with SpliceAI |
| **SpliceAI** | Splicing prediction | Used for all splice site predictions |

**MES Validation Threshold:**
- Donor sites: last 3 nucleotides of exon through intronic position +6
- Acceptor sites: intronic position -20 through first 3 nucleotides of exon

> **Note:** For predicting impact to consensus splice sites, SpliceAI scores alone should be considered for variants outside the MES validation threshold, as MES is not capable of predicting native splice site impact for such variants.

### Appendix D: RNase IIIb Domain

- **Domain boundaries:** p.Y1682 – p.S1846
- **Metal ion-binding residues:** p.S1344, p.E1705, p.D1709, p.D1713, p.G1809, p.D1810, p.E1813

### Appendix E: Repeat Regions (Excluded from PM4_Supporting)

- p.D606-p.D609
- p.E1418-p.E1420
- p.E1422-p.E1425

---

## References

1. Abou Tayoun AN, Pesaran T, et al. *Recommendations for interpreting the loss of function PVS1 ACMG/AMP variant criterion.* **Hum Mutat** (2018) 39(11):1517-1524. PMID: 30192042

2. de Kock L, Sabbaghian N, et al. *Germ-line and somatic DICER1 mutations in pineoblastoma.* **Acta Neuropathol** (2014) 128(4):583-95. PMID: 25022261

3. de Kock L, Sabbaghian N, et al. *Pituitary blastoma: a pathognomonic feature of germ-line DICER1 mutations.* **Acta Neuropathol** (2014) 128(1):111-22. PMID: 24839956

4. Wagh PK, Gardner MA, et al. *Cell- and developmental stage-specific Dicer1 ablation in the lung epithelium models cystic pleuropulmonary blastoma.* **J Pathol** (2015) 236(1):41-52. PMID: 25500911

5. Yin Y, Castro AM, et al. *Fibroblast Growth Factor 9 Regulation by MicroRNAs Controls Lung Development and Links DICER1 Loss to the Pathogenesis of Pleuropulmonary Blastoma.* **PLoS Genet** (2015) 11(5):e1005242. PMID: 25978641

6. Walsh MF, Ritter DI, et al. *Integrating somatic variant data and biomarkers for germline variant classification in cancer predisposition genes.* **Hum Mutat** (2018) 39(11):1542-1552. PMID: 30311369

7. Wu MK, Vujanic GM, et al. *Anaplastic sarcomas of the kidney are characterized by DICER1 mutations.* **Mod Pathol** (2018) 31(1):169-178. PMID: 28862265

8. de Kock L, Wu MK, et al. *Ten years of DICER1 mutations: Provenance, distribution, and associated phenotypes.* **Hum Mutat** (2019) 40(11):1939-1953. PMID: 31342592

9. Wu MK, Sabbaghian N, et al. *Biallelic DICER1 mutations occur in Wilms tumours.* **J Pathol** (2013) 230(2):154-64. PMID: 23620094

10. Gadd S, Huff V, et al. *A Children's Oncology Group and TARGET initiative exploring the genetic landscape of Wilms tumor.* **Nat Genet** (2017) 49(10):1487-1494. PMID: 28825729

11. Tavtigian SV, Harrison SM, et al. *Fitting a naturally scaled point system to the ACMG/AMP variant classification guidelines.* **Hum Mutat** (2020) 41(10):1734-1737. PMID: 32720330

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.4.0 | 7/8/2025 | 1. Updated C Spec specifications type to Tavtigian points based system as allowed in the latest C Spec release in order to appropriately reflect the classification schema the VCEP has used from the start and to remove the irrelevant criteria combinations at the bottom of the page.<br>2. PP3/BP4: Changed REVEL cutoffs to 3 decimal points to avoid ambiguity regarding rounding. |
| 1.3.0 | Previous | 1. BA1/BS1/PM2 Clarification: In light of the recent release of gnomAD v4.0.0 without a (non-cancer) filter, removed the (non-cancer) text and added the following clarifying instruction: "In general, the most recent/most comprehensive gnomAD version should be used."<br>2. Criteria Combination Clarification: Added a general comment to the C Spec asking users to disregard the "Rules for Combining Criteria" section and instead use the "Evidence Criteria Combinations" table. |

---

*This document was compiled from ClinGen DICER1 and miRNA-Processing Gene VCEP specifications. For the most current version, please refer to the [ClinGen website](https://clingen.org).*
