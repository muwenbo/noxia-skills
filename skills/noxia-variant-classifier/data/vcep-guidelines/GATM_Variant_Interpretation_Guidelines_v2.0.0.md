# ClinGen Cerebral Creatine Deficiency Syndromes VCEP Variant Interpretation Guidelines for GATM

**Version:** 2.0.0
**Released:** December 3, 2024
**Affiliation:** Cerebral Creatine Deficiency Syndromes Variant Curation Expert Panel (CCDS VCEP)
**Based on:** Richards et al., 2015 ACMG/AMP Guidelines

---

## Gene Information

| Attribute | Value |
|-----------|-------|
| **Gene** | GATM (HGNC:4175) |
| **HGNC Name** | glycine amidinotransferase |
| **Transcript** | NM_001482.3 |
| **Protein** | NP_001473 (423 amino acids) |
| **Disease** | AGAT deficiency (MONDO:0012996) |
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

Loss of function (LOF) of GATM is a known mechanism of disease for arginine:glycine amidinotransferase deficiency (AGAT-D). There are examples of various LOF variants, including nonsense and frameshift, in GATM in individuals with AGAT-D.

For all splice site variants (+1, +2, -1, -2), follow the guidance from the ClinGen SVI Splicing Subgroup (Walker et al, 2023, PMID: 37352859). Follow the decision tree outlined in Figure 5. As shown:
- If PVS1 is applied at any strength, PP3 should not be applied
- Experimental evidence, such as RT-PCR, is used to determine the weight of PVS1; this may be denoted as "PVS1_Strength (RNA)"
- PS1 may also be applied for splice variants (see Table 3 in PMID: 37352859)

**Note on compound heterozygotes:** In patients who are compound heterozygotes for a splicing variant and another variant type that does not disrupt splicing (such as a missense variant), evidence of normal splicing is expected. Therefore, the presence of normal splice products could complicate the assessment of the impact of the splice variant.

#### Strength Levels

| Strength | Criteria |
|----------|----------|
| **Very Strong** | Nonsense-mediated decay predicted |
| **Strong** | In-frame loss of >10% of the protein |
| **Moderate** | Single exon or larger deletion resulting in loss of <10% of the protein, and initiator codon variants |

#### Nonsense and Frameshift Variants

All nonsense and frameshift variants will meet PVS1 unless a premature termination codon is predicted to be missed by nonsense-mediated decay (NMD) because it is located in:
- The last exon (exon 9), OR
- The last 50 bases of the penultimate exon (exon 8, 3' of c.1109)

In those cases, refer to the PVS1 flowchart (Appendix A) for guidance on PVS1 weight.

#### Splice Site Variants (+1, +2, -1, -2)

- All canonical splice site pairs in GATM are GT-AG
- For any canonical splice site variant (+1, +2, -1, -2), the exon immediately adjacent to the variant is predicted to be skipped:
  - Upstream exon skipped for canonical donor splice site variants
  - Downstream exon skipped for canonical acceptor splice site variants
- To apply PVS1 at the very strong level, splice site variants must have no detectable nearby (+/- 20 nucleotides) strong consensus splice sequence that may reconstitute in-frame splicing, as predicted by SpliceAI. Otherwise, the PVS1 strength should be reduced accordingly.
- If this criterion is applied, PP3 (in silico splice site prediction tools) should not be used
- Non-canonical splice variants, such as +3 or -3, may also meet PVS1 - refer to Walker et al, PMID: 37352859

#### Deletions (Single or Multi-Exon)

- If a single or multi-exon deletion results in an out-of-frame consequence, use PVS1 at the very strong level unless not predicted to undergo NMD
- If not predicted to undergo NMD, refer to Appendix A (PVS1 flowchart) and Appendix B (predicted impact of exon loss)
- If the consequence is in-frame, the deletion must encompass one or more exons for PVS1 to apply
- If the in-frame deletion is smaller than one exon, PVS1 does not apply; consider using PM4

#### Duplications

To assess the impact of duplications, see Appendix A (PVS1 flowchart) and Appendix B (predicted impact of exon loss).

#### Initiator Codon Variants

All initiator codon variants will meet PVS1_Moderate. The next in-frame methionine is at amino acid position 130 (based on NP_001473).

---

### PS1 - Same Amino Acid Change

**Original ACMG Summary:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.

**Example:** Val->Leu caused by either G>C or G>T in the same codon.

**Caveat:** Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | Variant resulting in the same amino acid change as a previously established **pathogenic** variant regardless of nucleotide change. If the variant is in the last 3 nucleotides of an exon, further analysis using splicing site prediction algorithms (see PP3) and data from the literature (if available) is required to investigate the impact on splicing. PS1 may also be applied for splicing variants under specific circumstances (see Table 3 in PMID: 37352859). |
| **Moderate** | Variant resulting in the same amino acid change as a previously established **likely pathogenic** variant regardless of nucleotide change. If the variant is in the last 3 nucleotides of an exon, further analysis using splicing site prediction algorithms (see PP3) and data from the literature (if available) is required to investigate the impact on splicing. PS1_Moderate may also be applied for splicing variants under specific circumstances (see Table 3 in PMID: 37352859). |
| **Supporting** | PS1_Supporting may be applied for splicing variants under specific circumstances (see Table 3 in PMID: 37352859). |

---

### PS2 - De Novo (Confirmed)

**Original ACMG Summary:** De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.

**Note:** Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.

**VCEP Specifications:** ***Not Applicable***

**CCDS VCEP Notes:** De novo variants have not been reported in patients with AGAT deficiency, to our knowledge. Furthermore, the observation that a variant in GATM has arisen de novo does not support its causality because AGAT deficiency is an autosomal recessive disorder. The occurrence of de novo variants is more supportive in autosomal dominant and X-linked disorders. Any de novo variants in GATM, should they be observed, will be assessed based on the variant type, functional evidence, and in trans data as described.

---

### PS3 - Functional Studies

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.

**Note:** Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | Not applicable |
| **Moderate** | Not applicable |
| **Supporting** | AGAT activity data from an in vitro assay in which GATM variants were overexpressed in HeLa cells (DesRoches et al, 2016; PMID 27233232). Any variant with AGAT activity **at or below 15% of normal** meets PS3_Supporting. See Appendix C for further details on AGAT functional assays. |

#### Approved Functional Assay

| Parameter | Details |
|-----------|---------|
| **Reference** | DesRoches et al, 2016 (PMID: 27233232) |
| **Assay Description** | In vitro expression of cDNA constructs in HeLa cells followed by assay of AGAT activity |
| **Material** | Missense variants introduced into pTracer-GATM plasmid by site-directed mutagenesis, expressed in HeLa cells |
| **Readout** | % of recombinant wild-type AGAT activity |
| **Controls** | Wild type pTracer-GATM (positive); pTracer empty vector and untransfected cells (negative) |
| **Validation** | 1 LP variant, 2 benign variants (meet BA1) |
| **PS3_Supporting Threshold** | AGAT activity ≤15% of normal |
| **BS3_Supporting Threshold** | AGAT activity ≥30% of normal |

**Note:** Details on splicing assays (e.g., RT-PCR) have been removed from PS3 because this data is now included under PVS1 (PMID: 37352859).

---

### PS4 - Prevalence in Affected

**Original ACMG Summary:** The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.

**VCEP Specifications:** ***Not Applicable***

**CCDS VCEP Notes:** This rule is typically used for autosomal dominant disorders, with PM3 used as a case-counting mechanism for autosomal recessive conditions.

---

### PM1 - Mutational Hot Spot

**Original ACMG Summary:** Located in a mutational hot spot and/or critical and well-established functional domain (e.g., active site of an enzyme) without benign variation.

**VCEP Specifications:** ***Not Applicable***

---

### PM2 - Absent from Controls

**Original ACMG Summary:** Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

**Caveat:** Population data for indels may be poorly called by next generation sequencing.

**VCEP Specification (Supporting only):**

| Strength | Criteria |
|----------|----------|
| **Supporting** | Allele frequency **<0.000055 (<0.0055%)** in all populations in gnomAD |

**GATM Specifications:**
- All subpopulations in gnomAD must have a maximum allele frequency less than 0.000055 (based on the prevalence of the most common suspected pathogenic variants, c.484+1G>T and p.Arg169Ter)
- Use the current version recommended by SVI; version number will be stated in classification summary
- **PM2 will NOT be used at moderate strength; PM2 will only be applied as a Supporting criterion**
- If homozygotes are observed, the variant will meet BS2 (assuming 100% penetrance for an individual with 2 pathogenic variants in trans)

**CCDS VCEP Notes:** It is acceptable for a GATM variant to be present in controls, if heterozygous, because AGAT-D is a recessive disorder. Homozygotes should not be seen in a population database, such as gnomAD, because the penetrance of this condition in individuals with biallelic pathogenic variants is expected to be 100%.

---

### PM3 - In Trans with Pathogenic

**Original ACMG Summary:** For recessive disorders, detected in trans with a pathogenic variant.

**Note:** This requires testing of parents (or offspring) to determine phase.

**VCEP Specifications:** Follow SVI guidance for PM3.

Parental testing, or another appropriate molecular method (such as cloning each allele separately followed by sequencing), must have been performed in order to confirm that the variants are in trans if the patient is compound heterozygous.

#### PM3 Point System

| Classification of Other Allele | Points (Confirmed in Trans) | Points (Phase Unknown) |
|--------------------------------|----------------------------|------------------------|
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
| **Moderate** | In-frame deletions and insertions of **2 or more amino acids** |
| **Supporting** | In-frame deletion/insertion of a **single amino acid** |

**CCDS VCEP Notes:** Stop loss variants in GATM have not been reported, as far as we are aware.

---

### PM5 - Novel Missense at Same Residue

**Original ACMG Summary:** Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.

**Example:** Arg156His is pathogenic; now you observe Arg156Cys.

**Caveat:** Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Moderate** | Missense change at an amino acid residue where a different missense change determined to be **pathogenic** has been seen before. If the pathogenicity of another missense change at the same amino acid residue is unknown, determine its pathogenicity using these specifications in order to determine if this criterion can be used. |
| **Supporting** | Missense change at an amino acid residue where a different missense change determined to be **likely pathogenic** has been seen before. |

---

### PM6 - De Novo (Assumed)

**Original ACMG Summary:** Assumed de novo, but without confirmation of paternity and maternity.

**VCEP Specifications:** ***Not Applicable***

**CCDS VCEP Notes:** See PS2 notes. De novo variants have not been reported in patients with AGAT deficiency, and the observation that a variant in GATM has arisen de novo does not support its causality because AGAT deficiency is an autosomal recessive disorder.

---

### PP1 - Co-segregation

**Original ACMG Summary:** Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.

**Note:** May be used as stronger evidence with increasing segregation data.

**VCEP Specifications:** ***Not Applicable***

**CCDS VCEP Notes:** Sibships large enough to meet this criterion are extremely rare. In addition, because GATM is the only gene involved in AGAT-D, ALL patients are expected to be bi-allelic, regardless of whether the pathogenic variants can be, or have been, detected. A variant under assessment may not be the true pathogenic variant but instead in linkage disequilibrium with an unidentified pathogenic variant. For this reason, this criterion does not facilitate assessment of pathogenicity.

---

### PP2 - Missense in Constrained Gene

**Original ACMG Summary:** Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.

**VCEP Specifications:** ***Not Applicable***

**CCDS VCEP Notes:** Does not apply; there are benign and pathogenic missense variants in GATM.

---

### PP3 - Computational Evidence

**Original ACMG Summary:** Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).

**Caveat:** As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.

**VCEP Specifications:**

**Important:** Do not apply PP3 if PVS1 has been applied at any strength. PP3 is not applied at strong strength due to insufficient data.

| Strength | Criteria |
|----------|----------|
| **Strong** | Not applicable (insufficient data) |
| **Moderate** | Missense variant with a **REVEL score >0.773** (based on guidance from Pejaver et al, 2022, PMID: 36413997) |
| **Supporting** | **Missense variants:** REVEL score **0.644-0.773** (based on guidance from Pejaver et al, 2022, PMID: 36413997). **In-frame deletions/insertions:** Predicted deleterious by PROVEAN and MutationTaster (results must be consistent to count). **Non-canonical splice site variants (e.g., +3, -3):** SpliceAI score **≥0.2** (as indicated in PMID: 37352859, Table 1 and Figure 4). Assess the possibility of activation of cryptic splice sites. |

---

### PP4 - Phenotype Specificity

**Original ACMG Summary:** Patient's phenotype or family history is highly specific for a disease with a single genetic etiology.

**VCEP Specifications:**

**Important:** Variant must meet PM2_Supporting for PP4 to apply at any strength.

#### PP4 Point System

| Phenotypic Feature | Points |
|-------------------|--------|
| Low urine guanidinoacetate with or without low or low normal creatine | 1 point |
| Low plasma guanidinoacetate with or without low or low normal creatine | 2 points |
| Significantly decreased creatine peak in brain magnetic resonance spectroscopy | 3 points |
| AGAT enzyme activity <5% of normal | 3 points |

#### PP4 Strength Thresholds

| Total Points | Strength | Additional Requirements |
|--------------|----------|------------------------|
| 1-2 points | PP4 (Supporting) | Based on urine and/or plasma guanidinoacetate only |
| 3 points | PP4_Moderate | Two or more data types recommended |
| ≥4 points | PP4_Strong | Two or more data types required. Full GATM gene sequencing (all coding exons and intron/exon boundaries) must have been carried out. If not, consider downgrading. |

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

| Strength | Threshold |
|----------|-----------|
| **Stand Alone** | GrpMax (lower bound 95%ile) **>0.0005 (0.05%)** in gnomAD |

**Calculation basis:**
- Max allelic contribution = 100%
- Max genetic contribution = 100%
- Estimated prevalence = 1 in 3,450,000 (PMID: 27233232)
- Penetrance = 100%
- Reference: PMID 30311383

Use the current version recommended by SVI; version number will be stated in classification summary.

---

### BS1 - Frequency Greater Than Expected

**Original ACMG Summary:** Allele frequency is greater than expected for disorder.

**VCEP Specification (Strong):**

| Strength | Threshold |
|----------|-----------|
| **Strong** | GrpMax (lower bound 95%ile) **>0.0001 (0.01%)** in gnomAD |

**Calculation basis:**
- Max allelic contribution = 25%
- Max genetic contribution = 100%
- Estimated prevalence = 1 in 3,450,000 (PMID: 27233232)
- Penetrance = 100%
- Reference: PMID 30311383

Use the current version recommended by SVI; version number will be stated in classification summary.

---

### BS2 - Observed in Healthy Adult

**Original ACMG Summary:** Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

**VCEP Specification (Strong):**

| Strength | Criteria |
|----------|----------|
| **Strong** | Observed in the **homozygous state** in a healthy adult |

---

### BS3 - Functional Studies (No Effect)

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

**VCEP Specification (Supporting):**

| Strength | Criteria |
|----------|----------|
| **Supporting** | In vitro assays in which a variant is expressed in AGAT-deficient cultured cells (e.g., AGAT-deficient fibroblasts) or In-Fusion High-Fidelity cloning of GATM transcript and site-directed mutagenesis to generate missense variant overexpressed in HeLa cells with measurement of AGAT activity. Any variant with enzyme activity **at or above 30% of normal** in DesRoches et al, 2016 (PMID: 27233232) meets BS3_Supporting. |

---

### BS4 - Lack of Segregation

**Original ACMG Summary:** Lack of segregation in affected members of a family.

**Caveat:** The presence of phenocopies for common phenotypes (i.e., cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.

**VCEP Specifications:** ***Not Applicable***

---

### BP1-BP7 - Benign Supporting

| Criterion | Status | Specification |
|-----------|--------|---------------|
| **BP1** | Not Applicable | Missense variant in a gene for which primarily truncating variants are known to cause disease. |
| **BP2** | Supporting | Observed **in cis** with a pathogenic variant (to take AR inheritance for AGAT deficiency into account). |
| **BP3** | Not Applicable | In-frame deletions/insertions in a repetitive region without a known function. |
| **BP4** | Supporting | **Missense variants:** REVEL score **<0.29** (based on guidance from Pejaver et al, 2022, PMID: 36413997). **In-frame deletions/insertions:** Predicted benign by MutPredIndel and MutationTaster. **Splicing:** No predicted impact on splicing by SpliceAI, based on a score **<0.1** (as indicated in PMID: 37352859, Table 1 and Figure 4). |
| **BP5** | Not Applicable | Variant found in a case with an alternate molecular basis for disease. An individual could be a carrier of a pathogenic variant in GATM and have another disorder. |
| **BP6** | Not Applicable | This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PMID: 29543229). |
| **BP7** | Supporting | A synonymous (silent) variant OR an intronic variant at or beyond positions +7 and -21, for which SpliceAI predicts no impact on splicing (score **<0.1**) (see Walker et al, 2023, PMID: 37352859). |
| **BP7_Strong** | Strong | Experimental evidence, such as RT-PCR, shows no impact on splicing. Follow the decision tree outlined in Figure 5, Walker et al, 2023, PMID: 37352859. **Caution:** Splicing may appear normal in compound heterozygous patients with one allele that is degraded by nonsense-mediated decay as the result of a frameshift and premature termination codon due to splicing defect. |

---

## Rules for Combining Criteria

### Pathogenic Classification

| Criteria Combination |
|---------------------|
| 1 Very Strong *(PVS1, PM3_VeryStrong)* **AND** ≥1 Strong *(PVS1_Strong, PS1, PS3, PM3_Strong, PP4_Strong)* |
| 1 Very Strong *(PVS1, PM3_VeryStrong)* **AND** ≥2 Moderate *(PVS1_Moderate, PM3, PM4, PM5, PP3_Moderate, PP4_Moderate)* |
| 1 Very Strong *(PVS1, PM3_VeryStrong)* **AND** 1 Moderate *(PVS1_Moderate, PM3, PM4, PM5, PP3_Moderate, PP4_Moderate)* **AND** 1 Supporting *(PS3_Supporting, PM2_Supporting, PM3_Supporting, PM4_Supporting, PM5_Supporting, PP3, PP4)* |
| 1 Very Strong *(PVS1, PM3_VeryStrong)* **AND** ≥2 Supporting *(PS3_Supporting, PM2_Supporting, PM3_Supporting, PM4_Supporting, PM5_Supporting, PP3, PP4)* |
| ≥2 Strong *(PVS1_Strong, PS1, PS3, PM3_Strong, PP4_Strong)* |
| 1 Strong *(PVS1_Strong, PS1, PS3, PM3_Strong, PP4_Strong)* **AND** ≥3 Moderate *(PVS1_Moderate, PM3, PM4, PM5, PP3_Moderate, PP4_Moderate)* |
| 1 Strong *(PVS1_Strong, PS1, PS3, PM3_Strong, PP4_Strong)* **AND** 2 Moderate *(PVS1_Moderate, PM3, PM4, PM5, PP3_Moderate, PP4_Moderate)* **AND** ≥2 Supporting *(PS3_Supporting, PM2_Supporting, PM3_Supporting, PM4_Supporting, PM5_Supporting, PP3, PP4)* |
| 1 Strong *(PVS1_Strong, PS1, PS3, PM3_Strong, PP4_Strong)* **AND** 1 Moderate *(PVS1_Moderate, PM3, PM4, PM5, PP3_Moderate, PP4_Moderate)* **AND** ≥4 Supporting *(PS3_Supporting, PM2_Supporting, PM3_Supporting, PM4_Supporting, PM5_Supporting, PP3, PP4)* |

### Likely Pathogenic Classification

| Criteria Combination |
|---------------------|
| 1 Very Strong *(PVS1, PM3_VeryStrong)* **AND** 1 Moderate *(PVS1_Moderate, PM3, PM4, PM5, PP3_Moderate, PP4_Moderate)* |
| 1 Very Strong *(PVS1)* **AND** 1 Supporting *(PM2_Supporting)* |

### Benign Classification

| Criteria Combination |
|---------------------|
| ≥2 Strong *(BS1, BS2)* |
| 1 Stand Alone *(BA1)* |

### Likely Benign Classification

| Criteria Combination |
|---------------------|
| 1 Strong *(BS1, BS2)* **AND** 1 Supporting *(BS3_Supporting, BP2, BP4, BP7)* |
| ≥2 Supporting *(BS3_Supporting, BP2, BP4, BP7)* |

---

## Appendices

### Appendix A: PVS1 Decision Tree Summary

The PVS1 decision tree for GATM follows the ClinGen SVI recommendations (Abou Tayoun et al, 2018, PMID: 30192042) with gene-specific modifications.

#### Nonsense/Frameshift Pathway

```
Nonsense or Frameshift
    |
    +-- Predicted to undergo NMD (nucleotide is 5' of c.1109)
    |       --> PVS1
    |
    +-- Not predicted to undergo NMD (last exon or last 50bp of exon 8)
            |
            +-- Truncated region includes Cys407 (critical active site)
            |       --> PVS1_Strong
            |
            +-- Role of truncated region unknown
                    --> PVS1_Moderate
```

#### Splice Site Pathway

```
Canonical Splice Site (+1, +2, -1, -2)
    |
    +-- Exon skipping disrupts reading frame + NMD predicted
    |       --> PVS1
    |
    +-- Exon skipping preserves reading frame
    |       |
    |       +-- Removes >10% protein OR includes active site residue
    |       |       --> PVS1_Strong
    |       |
    |       +-- Removes <10% protein, no critical residues
    |               --> PVS1_Moderate
    |
    +-- Exon skipping disrupts reading frame, no NMD
            --> See flowchart for specific guidance
```

#### Critical Residues by Exon

| Exon | Critical Residues | Notes |
|------|-------------------|-------|
| 5 | Asp254 | Active site, hydrogen bonded to His303 |
| 6 | His303, Asp305, Met302, Arg322 | Active site and substrate binding |
| 9 | Cys407, Gly402 | Active site (Cys407) and substrate binding |

---

### Appendix B: Exon Information and Predicted Impact of Deletion

| Exon | First Nucleotide | Last Nucleotide | Length (coding bp) | Predicted Impact of Deletion | PVS1 Strength | Critical Residues |
|------|------------------|-----------------|-------------------|------------------------------|---------------|-------------------|
| 1 | -91 | 69 | 69 | In-frame, deletes 23 aa (5.4%) | Strong | Mitochondrial transit peptide (aa 1-37) |
| 2 | 70 | 288 | 219 | Out-of-frame → NMD | Very Strong | - |
| 3 | 289 | 484 | 196 | Out-of-frame → NMD | Very Strong | Asn98 (water binding) |
| 4 | 485 | 675 | 191 | Out-of-frame → NMD | Very Strong | Asp170 (substrate binding), Tyr203 |
| 5 | 676 | 813 | 138 | In-frame, deletes 46 aa (10.9%) | Strong | **Asp254** (active site) |
| 6 | 814 | 978 | 165 | In-frame, deletes 55 aa (13.0%) | Strong | **His303** (active site), Met302, Asp305, Arg322 |
| 7 | 979 | 1042 | 64 | Out-of-frame → NMD | Very Strong | - |
| 8 | 1043 | 1159 | 117 | In-frame, deletes 39 aa (9.2%) | Moderate | Ser354, Ser355 (substrate binding) |
| 9 | 1160 | 1272 (stop) | 113 | Missing last 36 aa + stop | Moderate (Strong if Cys407 missing) | **Cys407** (active site), Gly402 |

**Total:** 1272 nucleotides (including stop codon), 423 amino acids

---

### Appendix C: Functional Assay Details

#### Approved Assay: In Vitro AGAT Enzyme Activity (DesRoches et al, 2016)

| Component | Details |
|-----------|---------|
| **PMID** | 27233232 |
| **DOI** | 10.1002/humu.23018 |
| **Method** | In vitro expression of cDNA constructs in HeLa cells followed by assay of AGAT activity |
| **Material** | Missense variants introduced into pTracer-GATM plasmid by site-directed mutagenesis |
| **Readout** | % of recombinant wild-type AGAT activity (quantitative) |
| **Replicates** | Biological: Yes (duplicate transfections); Technical: Limited |
| **Positive Control** | Wild type pTracer-GATM; GFP signal indicates successful transfection |
| **Negative Control** | (1) pTracer empty vector, (2) untransfected cells |
| **Validation** | 1 LP variant, 2 benign variants (meet BA1) |

#### Evidence Thresholds

| Classification | AGAT Activity Threshold |
|----------------|------------------------|
| PS3_Supporting (Abnormal) | ≤15% of normal |
| Indeterminate | 16-29% of normal |
| BS3_Supporting (Normal) | ≥30% of normal |

---

### Appendix D: Population Frequency Thresholds Summary

| Criterion | Threshold | Strength | Calculation Basis |
|-----------|-----------|----------|-------------------|
| BA1 | GrpMax >0.0005 (0.05%) | Stand Alone | Max AC=100%, Max GC=100%, Prevalence=1:3,450,000, Penetrance=100% |
| BS1 | GrpMax >0.0001 (0.01%) | Strong | Max AC=25%, Max GC=100%, Prevalence=1:3,450,000, Penetrance=100% |
| PM2 | All pops <0.000055 (0.0055%) | Supporting | Based on highest MAF of suspected pathogenic LOF variants (c.484+1G>T, p.Arg169Ter) |

**Note:** Use gnomAD GrpMax (lower bound 95th percentile). Version will be stated in classification summary.

---

### Appendix E: Reference PMIDs

| PMID | Citation | Relevance |
|------|----------|-----------|
| 27233232 | DesRoches et al, 2016 | Functional assay data, prevalence estimates |
| 29543229 | Biesecker & Harrison, 2018 | ClinGen SVI recommendations (PP5/BP6 not for use) |
| 30192042 | Abou Tayoun et al, 2018 | PVS1 decision tree framework |
| 30311383 | Whiffin et al, 2018 | Allele frequency threshold calculations |
| 36413997 | Pejaver et al, 2022 | REVEL thresholds for PP3/BP4 |
| 37352859 | Walker et al, 2023 | SVI Splicing Subgroup guidance |
| 9148748 | Humm et al, 1997 | AGAT active site identification |
| 9218780 | Humm et al, 1997 | AGAT crystal structure |
| 9266688 | Fritsche et al, 1997 | AGAT substrate binding and catalysis |

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 2.0.0 | December 3, 2024 | Updated to include SVI guidance on splicing variants (Walker et al, 2023, PMID: 37352859) and in silico data (Pejaver et al, 2022, PMID: 36413997), as well as new gnomAD version. Added PS1_Moderate, PS1_Supporting for splicing variants. Removed splicing assays from PS3 (now under PVS1). Added PP3_Moderate. Updated BP4 and BP7 with new SpliceAI cutoffs. Added additional Likely Pathogenic combinations including PVS1 + PM2_Supporting. |
| 1.0.0 | Initial release | Original VCEP specifications |

---

*This document was compiled from ClinGen Cerebral Creatine Deficiency Syndromes VCEP specifications and ClinGen SVI recommendations. For the most current version, please refer to the [ClinGen website](https://clinicalgenome.org/).*
