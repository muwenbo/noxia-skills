# ClinGen Cerebral Creatine Deficiency Syndromes Expert Panel Variant Interpretation Guidelines for GAMT

**Version:** 2.0.0
**Released:** 5/23/2024
**Affiliation:** Cerebral Creatine Deficiency Syndromes VCEP
**Based on:** Richards et al., 2015 ACMG/AMP Guidelines

---

## Gene Information

| Attribute | Value |
|-----------|-------|
| **Gene** | GAMT (HGNC:4136) |
| **HGNC Name** | guanidinoacetate N-methyltransferase |
| **Transcript** | NM_000156.6 |
| **Disease** | Guanidinoacetate methyltransferase deficiency (MONDO:0012999) |
| **Inheritance** | Autosomal Recessive |

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

**VCEP Specifications:**

Loss of function (LOF) of GAMT is a known mechanism of disease for guanidinoacetate methyltransferase deficiency (GAMT-D). There are examples of various LOF variants, including nonsense and frameshift, in GAMT in individuals with GAMT-D. The specifications are based on the PVS1 decision tree (Figure 1, Abou Tayoun et al, 2018, PMID 30192042).

**Important:** For all splice site variants (+1, +2, -1, -2), follow the guidance from the ClinGen SVI Splicing Subgroup (Walker et al, 2023, PMID: 37352859). Follow the decision tree outlined in Figure 5. If PVS1 is applied at any strength, PP3 should not be applied. Experimental evidence, such as RT-PCR, is used to determine the weight of PVS1; PS3 is not applied if PVS1 is applied; instead PVS1_Strength (RNA) is used. PS1 may also be applied for splice variants (see Table 3 in PMID: 37352859).

#### Strength Levels

| Strength | Criteria |
|----------|----------|
| **Very Strong (PVS1)** | Nonsense-mediated decay predicted for nonsense/frameshift variants; splice site variants leading to out-of-frame exon skipping with NMD; full gene deletion; single/multi-exon deletion disrupting reading frame with NMD predicted |
| **Strong (PVS1_Strong)** | Single exon or larger deletion resulting in loss of >10% of the protein; nonsense/frameshift variants with PTC not predicted to undergo NMD and >10% protein lost; splice site variants with out-of-frame consequence not predicted to undergo NMD and >10% protein altered; in-frame exon skipping (Exons 5, 6); duplications presumed in tandem with reading frame disrupted |
| **Moderate (PVS1_Moderate)** | Single exon or larger deletion resulting in loss of <10% of the protein; nonsense/frameshift variants with PTC not predicted to undergo NMD and <10% protein lost; initiator codon variants; splice site variants with in-frame loss of <10% of protein |

#### NMD Prediction Rules for GAMT

- NMD is **not predicted** if the premature termination codon (PTC) is in:
  - The last exon (exon 6), OR
  - The last 50 nucleotides of the penultimate exon (exon 5, 3' to c.520)

#### Nonsense and Frameshift Variants

All nonsense and frameshift variants will meet **PVS1** unless a PTC is predicted to be missed by NMD:
- If PTC in exon 6 or last 50 bases of exon 5 (c.520):
  - **PVS1_Strong** if >10% of the protein is lost
  - **PVS1_Moderate** if <10% of the protein is lost

#### Splice Site Variants (+1, +2, -1, -2)

- All canonical splice site pairs in GAMT are GT-AG
- For any canonical splice site variant, the exon immediately adjacent to the variant is predicted to be skipped:
  - Upstream exon skipped for canonical donor splice site variants
  - Downstream exon skipped for canonical acceptor splice site variants
- Use SpliceAI to look for nearby (+/- 20 nucleotides) strong consensus splice sequence that may reconstitute in-frame splicing
- If this criterion is applied, PP3 should not be used
- Non-canonical splice variants (e.g., +3 or -3) will not meet PVS1, but could meet PS3 and/or PP3 criteria

#### Initiator Codon Variants

All initiator codon variants will meet **PVS1_Moderate**. The next in-frame methionine is at amino acid position 42 (based on NP_000147.1).

#### Deletions (Single or Multi-Exon)

| Consequence | NMD Predicted | Protein Impact | PVS1 Strength |
|-------------|---------------|----------------|---------------|
| Out of frame | Yes | - | PVS1 |
| Out of frame | No | >10% removed | PVS1_Strong |
| Out of frame | No | <10% removed | PVS1_Moderate |
| In frame (≥1 exon) | - | >10% removed | PVS1_Strong |
| In frame (≥1 exon) | - | <10% removed | PVS1_Moderate |
| In frame (<1 exon) | - | - | PVS1 not applicable; consider PM4 |

#### Duplications

Use the PVS1 decision tree (Figure 1, Abou Tayoun et al, 2018, PMID 30192042) to assess the impact of duplications.

| Duplication Type | Reading Frame | PVS1 Strength |
|------------------|---------------|---------------|
| Proven in tandem | Disrupted, NMD predicted | PVS1 |
| Presumed in tandem | Presumed disrupted, NMD predicted | PVS1_Strong |
| Proven not in tandem | - | Do not apply PVS1 |

---

### PS1 - Same Amino Acid Change

**Original ACMG Summary:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.

**Caveat:** Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:**

Any additional variants used to support the classification of the variant under assessment MUST have been previously classified by the CCDS VCEP, using these criteria, and the classification MUST be approved.

| Strength | Criteria |
|----------|----------|
| **Strong (PS1)** | Variant resulting in the same amino acid change as a variant previously established as **pathogenic** by the CCDS VCEP. If the variant is in the last 3 nucleotides of an exon, further analysis using splicing site prediction algorithms (see PP3) and data from the literature (if available) is required. PS1 may also be applied for splicing variants under specific circumstances (see Table 3 in PMID: 37352859). |
| **Moderate (PS1_Moderate)** | Variant resulting in the same amino acid change as a variant previously established as **likely pathogenic** by the CCDS VCEP. If the variant is in the last 3 nucleotides of an exon, further analysis using splicing site prediction algorithms is required. PS1_Moderate may also be applied for splicing variants under specific circumstances (see Table 3 in PMID: 37352859). |
| **Supporting (PS1_Supporting)** | May be applied for splicing variants under specific circumstances (see Table 3 in PMID: 37352859). |

---

### PS2 - De Novo (Confirmed)

**Original ACMG Summary:** De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.

***Not Applicable***

**Comments:** De novo variants have not been reported in patients with GAMT deficiency, to our knowledge. Furthermore, the observation that a variant in GAMT has arisen de novo does not support its causality because GAMT deficiency is an autosomal recessive disorder. The occurrence of de novo variants is more supportive in autosomal dominant and X-linked disorders. Any de novo variants in GAMT, should they be observed, will be assessed based on the variant type, functional evidence, and in trans data as described.

---

### PS3 - Functional Studies

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.

**Note:** Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.

**VCEP Specifications:**

Splicing assays (e.g., RT-PCR) are now included under PVS1; PS3 is not applied if PVS1 is applied.

| Strength | Criteria |
|----------|----------|
| **Supporting (PS3_Supporting)** | Variant expressed in GAMT-deficient fibroblasts or HeLa cells with **<15% of control value** for enzyme activity, as published in: Mercimek-Mahmutoglu et al, 2014 (PMID 24415674); Mercimek-Mahmutoglu et al, 2016 (PMID 26319512); or DesRoches et al, 2015 (PMID 26003046). |

#### Approved Functional Assay Details

| Parameter | PMID 24415674 | PMID 26003046 | PMID 26319512 |
|-----------|---------------|---------------|---------------|
| **Author** | Mercimek-Mahmutoglu | Desroches | Mercimek-Mahmutoglu |
| **Year** | 2014 | 2015 | 2016 |
| **Assay Description** | In vitro expression of cDNA constructs in GAMT-deficient cell line followed by assay of GAMT activity and Western blot | In vitro expression of cDNA constructs in HeLa cells followed by assay of GAMT activity and Western blot | In vitro expression of cDNA constructs in GAMT-deficient cell line followed by assay of GAMT activity and Western blot |
| **Material Used** | Missense variants introduced into pGAMT-EGFP plasmid by site-directed mutagenesis and expressed in primary GAMT-deficient human fibroblast cell line | Missense variants introduced into pGAMT-EGFP plasmid by site-directed mutagenesis and expressed in HeLa cells | Same method as PMID 24415674 |
| **Readout Type** | Quantitative (enzyme assay), qualitative (Western blot) | Quantitative for variants with deficient activity, qualitative for others | Qualitative |
| **Biological Replicates** | Met (triplicate transfections) | Met (triplicate transfections) | Met (triplicate transfections) |
| **Positive Control** | Wild type pGAMT-EGFPN1; GFP signal indicates successful transfection | Wild type pGAMT-EGFPN1; GFP signal indicates successful transfection | Wild type pGAMT-EGFPN1; GFP signal indicates successful transfection |
| **Negative Control** | pEGFPN1 empty vector; untransfected cells | pEGFPN1 empty vector; untransfected cells | pEGFPN1 empty vector; untransfected cells |
| **Approved** | Yes | Yes | Yes |
| **Proposed Strength** | Supporting | Supporting | Supporting |

---

### PS4 - Prevalence in Affected

**Original ACMG Summary:** The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.

***Not Applicable***

**Comments:** This rule is typically used for autosomal dominant disorders, with PM3 used as a case-counting mechanism for autosomal recessive conditions.

---

### PM1 - Mutational Hot Spot

**Original ACMG Summary:** Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.

***Not Applicable***

**Comments:** Located in a mutational hot spot and/or critical and well-established functional domain (e.g., active site of an enzyme) without benign variation.

---

### PM2 - Absent from Controls

**Original ACMG Summary:** Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

**Caveat:** Population data for indels may be poorly called by next generation sequencing.

**VCEP Specifications:**

PM2 will **NOT** be used at moderate strength; PM2 will only be applied as a **Supporting** criterion based on ClinGen SVI recommendations.

| Strength | Criteria |
|----------|----------|
| **Supporting (PM2_Supporting)** | Allele frequency **<0.0004 (<0.04%)** in all populations in gnomAD v4.0 |

**GAMT-Specific Notes:**
- All subpopulations in gnomAD v4.0 must have a maximum allele frequency less than 0.0004 (the highest population minor allele frequency of the most common pathogenic GAMT variant, c.327G>A, in gnomAD)
- It is acceptable for a GAMT variant to be present in controls, if heterozygous, because GAMT-D is a recessive disorder
- Homozygotes should not be seen in a population database such as gnomAD because penetrance of this condition in individuals with biallelic pathogenic variants is expected to be 100% and the condition presents with severe symptoms early in life
- If homozygotes are observed, or variant is confirmed in trans with a known pathogenic variant, the variant will meet BS2 (assuming 100% penetrance)

---

### PM3 - In Trans with Pathogenic

**Original ACMG Summary:** For recessive disorders, detected in trans with a pathogenic variant.

**Note:** This requires testing of parents (or offspring) to determine phase.

**VCEP Specifications:**

Any additional variants used to support the classification of the variant under assessment MUST have been previously classified by the CCDS VCEP, using these criteria, and the classification MUST be approved. Circularity must be avoided: Variant A can support the classification of Variant B, or vice versa, but NOT both.

Follow SVI guidance for PM3. Parental testing, or another appropriate molecular method (such as cloning each allele separately followed by sequencing), must have been performed to confirm that the variants are in trans if the patient is compound heterozygous.

#### PM3 Point System (Per Proband)

| Classification of Other Variant | Confirmed in Trans | Phase Unknown |
|--------------------------------|-------------------|---------------|
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
| **Moderate (PM4)** | Stop loss variants; in-frame deletions and insertions of **2 or more amino acids** |
| **Supporting (PM4_Supporting)** | Single amino acid deletions and insertions |

---

### PM5 - Novel Missense at Same Residue

**Original ACMG Summary:** Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.

**Caveat:** Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:**

Any additional variants used to support the classification of the variant under assessment MUST have been previously classified by the CCDS VCEP, using these criteria, and the classification MUST be approved.

| Strength | Criteria |
|----------|----------|
| **Moderate (PM5)** | Variant resulting in a different amino acid change, at the same amino acid position, as a variant previously established as **pathogenic** by the CCDS VCEP. If the variant is in the last 3 nucleotides of an exon, further analysis using splicing site prediction algorithms is required. |
| **Supporting (PM5_Supporting)** | Variant resulting in a different amino acid change, at the same amino acid position, as a variant previously established as **likely pathogenic** by the CCDS VCEP. If the variant is in the last 3 nucleotides of an exon, further analysis using splicing site prediction algorithms is required. |

---

### PM6 - De Novo (Assumed)

**Original ACMG Summary:** Assumed de novo, but without confirmation of paternity and maternity.

***Not Applicable***

**Comments:** De novo variants have not been reported in patients with GAMT deficiency. The observation that a variant in GAMT has arisen de novo does not support its causality because GAMT deficiency is an autosomal recessive disorder. Any de novo variants in GAMT, should they be observed, will be assessed based on the variant type, functional evidence, and in trans data as described.

---

### PP1 - Co-segregation

**Original ACMG Summary:** Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.

***Not Applicable***

**Comments:** Sibships large enough to meet this criterion are extremely rare. In addition, because GAMT is the only gene involved in GAMT-D, ALL patients are expected to be bi-allelic, regardless of whether the pathogenic variants can be, or have been, detected. A variant under assessment may not be the true pathogenic variant but instead in linkage disequilibrium with an unidentified pathogenic variant. For this reason, this criterion does not facilitate assessment of pathogenicity.

---

### PP2 - Missense in Constrained Gene

**Original ACMG Summary:** Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.

***Not Applicable***

**Comments:** Does not apply; there are benign and pathogenic missense variants in GAMT.

---

### PP3 - Computational Evidence

**Original ACMG Summary:** Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).

**Caveat:** As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.

**VCEP Specifications:**

**Important:** Do not apply PP3 if PVS1 has been applied at any strength.

#### For Missense Variants (REVEL Score)

| Strength | REVEL Score |
|----------|-------------|
| **Strong (PP3_Strong)** | ≥0.932 |
| **Moderate (PP3_Moderate)** | 0.773 - <0.932 |
| **Supporting (PP3)** | 0.644 - <0.773 |

*Based on guidance from Pejaver et al, 2022, PMID: 36413997*

#### For In-Frame Deletions/Insertions

- Predicted deleterious by **PROVEAN** and **MutationTaster**
- Results must be consistent to count
- Strength: **Supporting (PP3)**

#### For Non-Canonical Splice Site Variants (e.g., +3, -3)

- Use SpliceAI (https://spliceailookup.broadinstitute.org/)
- Apply **PP3 (Supporting)** for a score **≥0.2** (as indicated in PMID: 37352859, Table 1 and Figure 4)
- Assess the possibility of activation of cryptic splice sites

---

### PP4 - Phenotype Specificity

**Original ACMG Summary:** Patient's phenotype or family history is highly specific for a disease with a single genetic etiology.

**VCEP Specifications:**

**Important:** Variant must meet PM2_Supporting for PP4 to apply at any strength.

#### PP4 Point System

| Phenotypic Feature | Points |
|--------------------|--------|
| Elevated urine guanidinoacetate with or without low or low normal creatine | 1 point |
| Elevated plasma guanidinoacetate with or without low or low normal creatine | 2 points |
| Significantly decreased creatine peak in brain magnetic resonance spectroscopy with or without visible guanidinoacetate peak | 3 points |
| GAMT enzyme activity <5% of normal | 3 points |

#### PP4 Strength Thresholds

| Total Points | Strength | Additional Requirements |
|--------------|----------|------------------------|
| <1 | PP4 not met | - |
| 1-2 | PP4 (Supporting) | Based on urine and/or plasma guanidinoacetate |
| 3 | PP4_Moderate | Two or more data types recommended |
| ≥4 | PP4_Strong | Two or more data types required; for PP4_Strong, full GAMT gene sequencing (all coding exons and intron/exon boundaries) must have been carried out. If not, consider downgrading. |

---

### PP5 - Reputable Source

**Original ACMG Summary:** Reputable source recently reports variant as pathogenic, but the evidence is not available to the laboratory to perform an independent evaluation.

***Not Applicable***

This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PMID: 29543229).

---

## Benign Criteria

### BA1 - Allele Frequency >5%

**Original ACMG Summary:** Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

**VCEP Specification (Stand Alone):**

| Strength | Criteria |
|----------|----------|
| **Stand Alone (BA1)** | Allele frequency **>0.003 (0.3%)** in gnomAD v4.0 in any continental population with >2000 alleles |

**Calculation Basis:**
- Estimated prevalence: 1 in 114,000 (PMID 24071436)
- Max allelic contribution = 100%
- Max genetic contribution = 100%
- Use the highest population minor allele frequency (MAF) in any given continental population with >2,000 alleles (European non-Finnish, African, East Asian, South Asian, Latino) (PMID 30311383)

---

### BS1 - Frequency Greater Than Expected

**Original ACMG Summary:** Allele frequency is greater than expected for disorder.

**VCEP Specification (Strong):**

| Strength | Criteria |
|----------|----------|
| **Strong (BS1)** | Allele frequency **>0.001 (0.1%)** in gnomAD v4.0 in any continental population with >2000 alleles |

**Calculation Basis:**
- Estimated prevalence: 1 in 114,000 (PMID: 24071436)
- Max allelic contribution = 40%
- Max genetic contribution = 100%
- Use the highest population MAF in any given continental population with >2,000 alleles (PMID 30311383)

---

### BS2 - Observed in Healthy Adult

**Original ACMG Summary:** Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong (BS2)** | Observed in the **homozygous state** in a healthy adult, OR confirmed in trans with a variant that has been classified as **pathogenic** by the CCDS VCEP using these criteria |

---

### BS3 - Functional Studies (No Effect)

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Supporting (BS3_Supporting)** | In vitro assays in which a variant is expressed in GAMT-deficient cultured cells (e.g., GAMT-deficient fibroblasts) or in-fusion High-Fidelity cloning of GAMT transcript and site directed mutagenesis to generate missense variant overexpressed in HeLa cells, with measurement of GAMT activity showing **≥30% of normal**. Applicable for values in: Mercimek-Mahmutoglu et al, 2014 (PMID 24415674); Mercimek-Mahmutoglu et al, 2016 (PMID 26319512); DesRoches et al, 2015 (PMID 26003046). |

---

### BS4 - Lack of Segregation

**Original ACMG Summary:** Lack of segregation in affected members of a family.

**Caveat:** The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals.

***Not Applicable***

**Comments:** Lack of segregation in a family. Caveat: The presence of phenocopies for common phenotypes.

---

### BP1-BP7 - Benign Supporting

| Criterion | Status | Specifications |
|-----------|--------|----------------|
| **BP1** | Not Applicable | Does not apply. All types of variants cause GAMT-D. |
| **BP2** | Supporting | Observed in cis with a pathogenic variant (to take AR inheritance into account). |
| **BP3** | Not Applicable | There are no known repetitive regions without known function in GAMT. |
| **BP4** | Supporting | REVEL score <0.29 for missense variants (PMID: 36413997); In-frame deletion/insertion predicted benign by PROVEAN and MutationTaster; No predicted impact on splicing by SpliceAI (score <0.1, per PMID: 37352859). |
| **BP5** | Not Applicable | An individual could be a carrier of a pathogenic variant in GAMT and have another disorder. |
| **BP6** | Not Applicable | This criterion is not for use as recommended by the ClinGen SVI VCEP Review Committee (PMID: 29543229). |
| **BP7** | Supporting | A synonymous (silent) variant OR an intronic variant at or beyond positions +7 and -21, for which SpliceAI predicts no impact on splicing (score <0.1). |
| **BP7_Strong** | Strong | Experimental evidence, such as RT-PCR, shows no impact on splicing. Follow the decision tree in Figure 5, Walker et al, 2023 (PMID: 37352859). Note: splicing may appear normal in compound heterozygous patients if the splicing defect generates a transcript degraded by NMD. |

---

## Rules for Combining Criteria

### Pathogenic Classification

| Criteria Combination |
|---------------------|
| 1 Very Strong (PVS1, PM3_VeryStrong) **AND** ≥1 Strong (PVS1_Strong, PS1, PS3, PM3_Strong, PP4_Strong) |
| 1 Very Strong (PVS1, PM3_VeryStrong) **AND** ≥2 Moderate (PVS1_Moderate, PM3, PM4, PM5, PP3_Moderate, PP4_Moderate) |
| 1 Very Strong (PVS1, PM3_VeryStrong) **AND** 1 Moderate (PVS1_Moderate, PM3, PM4, PM5, PP3_Moderate, PP4_Moderate) **AND** 1 Supporting (PS3_Supporting, PM2_Supporting, PM3_Supporting, PM4_Supporting, PM5_Supporting, PP3, PP4) |
| 1 Very Strong (PVS1, PM3_VeryStrong) **AND** ≥2 Supporting (PS3_Supporting, PM2_Supporting, PM3_Supporting, PM4_Supporting, PM5_Supporting, PP3, PP4) |
| ≥2 Strong (PVS1_Strong, PS1, PS3, PM3_Strong, PP4_Strong) |
| 1 Strong (PVS1_Strong, PS1, PS3, PM3_Strong, PP4_Strong) **AND** ≥3 Moderate (PVS1_Moderate, PM3, PM4, PM5, PP3_Moderate, PP4_Moderate) |
| 1 Strong (PVS1_Strong, PS1, PS3, PM3_Strong, PP4_Strong) **AND** 2 Moderate (PVS1_Moderate, PM3, PM4, PM5, PP3_Moderate, PP4_Moderate) **AND** ≥2 Supporting (PS3_Supporting, PM2_Supporting, PM3_Supporting, PM4_Supporting, PM5_Supporting, PP3, PP4) |
| 1 Strong (PVS1_Strong, PS1, PS3, PM3_Strong, PP4_Strong) **AND** 1 Moderate (PVS1_Moderate, PM3, PM4, PM5, PP3_Moderate, PP4_Moderate) **AND** ≥4 Supporting (PS3_Supporting, PM2_Supporting, PM3_Supporting, PM4_Supporting, PM5_Supporting, PP3, PP4) |

### Likely Pathogenic Classification

| Criteria Combination |
|---------------------|
| 1 Very Strong (PVS1, PM3_VeryStrong) **AND** 1 Moderate (PVS1_Moderate, PM3, PM4, PM5, PP3_Moderate, PP4_Moderate) |
| 1 Strong (PVS1_Strong, PS1, PM3_Strong, PP3_Strong, PP4_Strong) **AND** ≥1 Moderate (PVS1_Moderate, PS1_Moderate, PM3, PM4, PM5, PP3_Moderate, PP4_Moderate) |
| 1 Strong (PVS1_Strong, PS1, PM3_Strong, PP3_Strong, PP4_Strong) **AND** ≥2 Supporting (PS1_Supporting, PS3_Supporting, PM2_Supporting, PM3_Supporting, PM4_Supporting, PM5_Supporting, PP3, PP4) |
| ≥3 Moderate (PVS1_Moderate, PS1_Moderate, PM3, PM4, PM5, PP3_Moderate, PP4_Moderate) |
| 2 Moderate (PVS1_Moderate, PS1_Moderate, PM3, PM4, PM5, PP3_Moderate, PP4_Moderate) **AND** ≥2 Supporting (PS1_Supporting, PS3_Supporting, PM2_Supporting, PM3_Supporting, PM4_Supporting, PM5_Supporting, PP3, PP4) |
| 1 Moderate (PVS1_Moderate, PS1_Moderate, PM3, PM4, PM5, PP3_Moderate, PP4_Moderate) **AND** ≥4 Supporting (PS1_Supporting, PS3_Supporting, PM2_Supporting, PM3_Supporting, PM4_Supporting, PM5_Supporting, PP3, PP4) |
| 1 Very Strong (PVS1) **AND** 1 Supporting (PM2_Supporting) |

### Benign Classification

| Criteria Combination |
|---------------------|
| 1 Stand Alone (BA1) |
| ≥2 Strong (BS1, BS2) |

### Likely Benign Classification

| Criteria Combination |
|---------------------|
| 1 Strong (BS1, BS2) **AND** 1 Supporting (BS3_Supporting, BP2, BP4, BP7) |
| ≥2 Supporting (BS3_Supporting, BP2, BP4, BP7) |

---

## Appendices

### Appendix A: PVS1 Flowchart for GAMT

Based on Figure 1, Abou Tayoun et al, 2018 (PMID 30192042)

| Type of Variant | Molecular Consequence | Additional Criteria | PVS1 Strength |
|-----------------|----------------------|---------------------|---------------|
| **Nonsense** | Predicted to undergo NMD | - | PVS1 |
| | Not predicted to undergo NMD | >10% of protein lost | PVS1_Strong |
| | Not predicted to undergo NMD | <10% of protein lost | PVS1_Moderate |
| **Frameshift** | Predicted to undergo NMD | - | PVS1 |
| | Not predicted to undergo NMD | >10% of protein altered | PVS1_Strong |
| | Not predicted to undergo NMD | <10% of protein altered | PVS1_Moderate |
| **GT-AG +/-1,2 splice sites** | Exon skipping disrupts reading frame, NMD predicted | Exons 1-4 | PVS1 |
| | Exon skipping disrupts reading frame, NMD not predicted | >10% altered | PVS1_Strong |
| | Exon skipping disrupts reading frame, NMD not predicted | <10% altered | PVS1_Moderate |
| | Exon skipping preserves reading frame | Exons 5, 6 | PVS1_Strong |
| **Initiation codon** | - | - | PVS1_Moderate |
| **Deletion** | Full gene deletion | - | PVS1 |
| | Single/multi-exon, out of frame, NMD predicted | - | PVS1 |
| | Single/multi-exon, out of frame, NMD not predicted | >10% altered | PVS1_Strong |
| | Single/multi-exon, out of frame, NMD not predicted | <10% altered | PVS1_Moderate |
| | Single/multi-exon preserves reading frame | Consult Appendix B | Apply highest possible strength |
| **Duplication** | Proven in tandem, reading frame disrupted, NMD predicted | - | PVS1 |
| | Presumed in tandem, reading frame disrupted, NMD predicted | - | PVS1_Strong |

**Footnotes:**
- In GAMT, all exons are biologically relevant; there is no significant alternative splicing.
- NMD is not predicted if the PTC is in the last exon (exon 6) or in the last 50 nucleotides of the penultimate exon (exon 5, 3' to c.520).
- All donor/acceptor splice sites in GAMT follow the GT/AG rule. Use SpliceAI to assess all splice site variants for creation of a cryptic splice site.

---

### Appendix B: Exon Deletion Consequences for PVS1

| Exon | First Nucleotide | Last Nucleotide | Length (coding nt) | Predicted Impact | PVS1 Strength | Critical Residues/Domains | ClinVar P/LP Missense Variants |
|------|------------------|-----------------|-------------------|------------------|---------------|--------------------------|-------------------------------|
| **Exon 1** | -66 | 181 | 181 | Out of frame → NMD | **Very Strong** | Trp20 and Met50 bind SAM; Glu45 important in catalytic mechanism and active site | p.Trp20Ser, p.Trp45Arg, p.Met50Leu |
| **Exon 2** | 182 | 327 | 146 | Out of frame → NMD | **Very Strong** | SAM binding (Gly70, Met71, Ile73, Ala74, Glu90) | p.Glu90Lys, p.Gln106Pro |
| **Exon 3** | 328 | 391 | 64 | Out of frame → NMD | **Very Strong** | SAM binding (Trp117, Glu118) | p.Val110Phe |
| **Exon 4** | 392 | 459 | 68 | Out of frame → NMD | **Very Strong** | Asp135 forms part of active site; binds GAA; Tyr136 important to structure | p.Thr136Met, p.Tyr137Ser |
| **Exon 5** | 460 | 570 | 111 | In frame, deletes 37 aa (15.5%) | **Strong** | GAA-binding residues Leu171, Thr172 | p.Gly164Asp, p.Tyr168Ser, p.Cys169Tyr |
| **Exon 6** | 571 | 711* | 141 | In frame, deletes 47 aa (19.9%) | **Strong** | GAA-binding residue Tyr222, important in active site structure | - |

*Last nucleotide of stop codon = 711

**Total:** 711 nucleotides (including stop codon); 236 amino acids

**References:**
- https://www.uniprot.org/uniprot/Q14353
- Komoto et al, 2004, "Catalytic Mechanism of Guanidinoacetate Methyltransferase" PMID 15533043
- Komoto et al, 2002, "Crystal Structure of Guanidinoacetate Methyltransferase from Rat Liver" PMID 12079381

*Note: Amino acid numbering in Komoto papers is one less compared to current protein sequences.*

---

### Appendix C: Population Frequency Thresholds Summary

| Criterion | Threshold | Strength | Notes |
|-----------|-----------|----------|-------|
| **BA1** | >0.003 (0.3%) | Stand Alone | Based on prevalence 1 in 114,000; max allelic contribution = 100% |
| **BS1** | >0.001 (0.1%) | Strong | Based on prevalence 1 in 114,000; max allelic contribution = 40% |
| **PM2** | <0.0004 (0.04%) | Supporting | Highest population MAF of most common pathogenic variant c.327G>A |

**Population Database:** gnomAD v4.0

**Qualifying Populations:** Continental populations with >2,000 alleles (European non-Finnish, African, East Asian, South Asian, Latino)

**Prevalence Estimates Used:**

| Publication | Method | Prevalence |
|-------------|--------|------------|
| Viau et al, 2013 | Utah newborn population | 1 in 114,072 |
| Mercimek-Mahmutoglu et al, 2016 | Sequenced GAMT in 500 newborns from Netherlands | 1 in 250,000 |
| Des Roches et al, 2015 | Searched ExAC for damaging missense and LOF variants | 1 in 550,000 |
| Des Roches et al, 2015 | Reviewed EVS, measured GAMT activity | 1 in 2,640,000 |

**Maximum Allelic Contribution:**
- ~40% of alleles are c.327G>A (most common pathogenic variant)
- c.59G>C (p.W20S) occurs exclusively in Portuguese families
- Remaining mutations occur in <3 alleles (~4%)

---

### Appendix D: In Silico Prediction Thresholds

#### REVEL Scores for Missense Variants

| Score Range | PP3 Strength | BP4 Applicability |
|-------------|--------------|-------------------|
| ≥0.932 | Strong (PP3_Strong) | - |
| 0.773 - <0.932 | Moderate (PP3_Moderate) | - |
| 0.644 - <0.773 | Supporting (PP3) | - |
| <0.29 | - | Supporting (BP4) |

*Based on Pejaver et al, 2022, PMID: 36413997*

#### SpliceAI Scores

| Score | Application |
|-------|-------------|
| ≥0.2 | PP3 (Supporting) for non-canonical splice variants |
| <0.1 | BP4 (Supporting) - no predicted impact on splicing |
| <0.1 | BP7 (Supporting) for synonymous or intronic variants at/beyond +7/-21 |

*Based on Walker et al, 2023, PMID: 37352859*

---

### Appendix E: Reference PMIDs

| PMID | Reference | Topic |
|------|-----------|-------|
| 30192042 | Abou Tayoun et al, 2018 | PVS1 decision tree |
| 37352859 | Walker et al, 2023 | SVI Splicing Subgroup guidance |
| 36413997 | Pejaver et al, 2022 | In silico prediction thresholds |
| 29543229 | ClinGen SVI, 2018 | PP5/BP6 not recommended |
| 24415674 | Mercimek-Mahmutoglu et al, 2014 | Functional assay |
| 26319512 | Mercimek-Mahmutoglu et al, 2016 | Functional assay |
| 26003046 | DesRoches et al, 2015 | Functional assay |
| 24071436 | Viau et al, 2013 | Prevalence data |
| 30311383 | Whiffin et al, 2018 | Population frequency filtering |
| 15533043 | Komoto et al, 2004 | GAMT catalytic mechanism |
| 12079381 | Komoto et al, 2002 | GAMT crystal structure |
| 23031365 | Mercimek-Mahmutoglu et al, 2012 | Carrier frequency |
| 17336114 | Almeida et al, 2007 | Portuguese founder variant |
| 19027335 | Dhar et al, 2009 | Maximum allelic contribution |
| 24268530 | Stockler-Ipsiroglu et al, 2016 | Known alleles |

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 2.0.0 | 5/23/2024 | Updated to include SVI guidance on splicing variants (PMID: 37352859) and in silico predictions (PMID: 36413997); Added PS1_Moderate and PS1_Supporting for splicing variants; Removed splicing assays from PS3 (now under PVS1); Added PP3_Strong and PP3_Moderate; Updated BP4 with new REVEL and SpliceAI thresholds; Updated BP7 for intronic variants; Added BP7_Strong; Added additional Likely Pathogenic combinations including PVS1 + PM2_Supporting |

---

*This document was compiled from ClinGen Cerebral Creatine Deficiency Syndromes VCEP specifications and ClinGen SVI recommendations. For the most current version, please refer to the ClinGen website.*
