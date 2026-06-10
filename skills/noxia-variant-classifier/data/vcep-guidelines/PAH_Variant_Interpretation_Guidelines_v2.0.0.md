# ClinGen Phenylketonuria Expert Panel Variant Interpretation Guidelines for PAH

**Version:** 2.0.0
**Released:** 7/16/2024
**Affiliation:** Phenylketonuria VCEP
**Based on:** Richards et al., 2015 ACMG/AMP Guidelines

---

## Gene Information

| Attribute | Value |
|-----------|-------|
| **Gene** | PAH (HGNC:8582) |
| **HGNC Name** | phenylalanine hydroxylase |
| **Transcript** | NM_000277.3 |
| **Disease** | Phenylketonuria (MONDO:0009861) |
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

**Original ACMG Summary:** Null variant (nonsense, frameshift, canonical ±1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.

**Caveats:**
- Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7).
- Use caution interpreting LOF variants at the extreme 3' end of a gene.
- Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact.
- Use caution in the presence of multiple transcripts.

**VCEP Specifications:**

Use the PAH-specific PVS1 decision tree (see [Appendix A](#appendix-a-pvs1-decision-tree)) to determine code strength. Applicable as described in Tayoun et al. 2018 and Walker et al. (PMID: 36865205).

#### Strength Levels

| Strength | Criteria |
|----------|----------|
| **Very Strong (PVS1)** | Any nonsense or frameshift variant occurring upstream of c.1285; Any canonical splice site predicted to disrupt reading frame and undergo nonsense mediated decay |
| **Strong (PVS1_Strong)** | Any nonsense or frameshift variant occurring downstream of c.1285; Any canonical splice site predicted to preserve reading frame (skipping of exons 1, 9, 10) or affect the last exon (exon 13); Initiator codon variant |
| **Moderate (PVS1_Moderate)** | Per decision tree: variants in regions where role in protein function is unknown, exon is present in biologically-relevant transcripts, LoF variants not frequent in general population, and variant removes <10% of protein |
| **N/A** | Exon absent from biologically-relevant transcripts; LoF variants in the exon are frequent in the general population |

**PVS1 (RNA):** Splicing assay data — assays demonstrating a variant leads to an aberrant splicing profile that can be categorized against the PVS1 decision tree to determine code strength.

#### PAH-Specific PVS1 Decision Tree Details

**Nonsense or Frameshift:**
- Predicted to undergo NMD (upstream of c.1285) → Exon present in biologically-relevant transcript (NM_000277.3) → **PVS1**
- Not predicted to undergo NMD:
  - Truncated/altered region is critical to protein function (oligomerization domain, aa 411–452) → **PVS1_Strong**
  - Role of region unknown + LoF variants not frequent + exon present → Variant removes >10% protein → **PVS1_Strong**
  - Role of region unknown + LoF variants not frequent + exon present → Variant removes <10% protein → **PVS1_Moderate**

**Canonical (GT-AG) ±1,2 Splice Sites:**
- Exon skipping or cryptic splice site disrupts reading frame + predicted NMD → Exon present → **PVS1**
- Exon skipping or cryptic splice site disrupts reading frame + NOT predicted NMD (exon 13):
  - Truncated/altered region critical (oligomerization domain, aa 411–452) → **PVS1_Strong**
  - Role unknown + LoF not frequent + exon present → >10% removed → **PVS1_Strong**; <10% removed → **PVS1_Moderate**
- Exon skipping or cryptic splice site preserves reading frame (exons 1, 9, 10):
  - Truncated/altered region critical (autoregulatory sequence, aa 1–33; PAH catalytic domain, aa 143–410) → **PVS1_Strong**
  - Role unknown + LoF not frequent + exon present → >10% removed → **PVS1_Strong**; <10% removed → **PVS1_Moderate**

**Deletions (Single exon to full gene):**
- Full gene deletion → **PVS1**
- Disrupts reading frame + predicted NMD → Exon present → **PVS1**
- Disrupts reading frame + NOT predicted NMD:
  - Truncated/altered region critical (autoregulatory sequence, aa 1–33; PAH catalytic domain, aa 143–410; oligomerization domain, aa 411–452) → **PVS1_Strong**
  - Role unknown + LoF not frequent + exon present → >10% removed → **PVS1_Strong**; <10% removed → **PVS1_Moderate**
- Preserves reading frame:
  - Truncated/altered region critical (autoregulatory sequence, aa 1–33; PAH catalytic domain, aa 143–410; oligomerization domain, aa 411–452) → **PVS1_Strong**
  - Role unknown + LoF not frequent + exon present → >10% removed → **PVS1_Strong**; <10% removed → **PVS1_Moderate**

**Duplications (≥1 exon, completely contained within gene):**
- Proven in tandem → Reading frame disrupted + NMD predicted → **PVS1**
- Proven in tandem → No or unknown impact on reading frame and NMD → **N/A**
- Presumed in tandem → Reading frame presumed disrupted + NMD predicted → **PVS1_Strong**
- Proven not in tandem → **N/A**

**Initiation Codon:**
- No known alternative start codon in other transcripts + ≥1 pathogenic variant(s) upstream of closest potential in-frame start codon (p.Met180) → **PVS1_Strong**

---

### PS1 - Same Amino Acid Change

**Original ACMG Summary:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change. Example: Val->Leu caused by either G>C or G>T in the same codon. Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | Same predicted splicing impact as a previously classified (likely) pathogenic variant. Applicable as described in Walker et al. (PMID: 36865205). |

**Modification Type:** Disease-specific

---

### PS2 - De Novo (Confirmed)

**Original ACMG Summary:** De novo (both maternity and paternity confirmed) in a patient with the disease and no family history. Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity. **Only applicable when proband has a known pathogenic variant in trans with the de novo variant.** |

**Modification Type:** Disease-specific

> **Note:** Because PAH is an autosomal recessive disorder, de novo occurrence must be demonstrated in the context of a known pathogenic variant in trans. A single de novo variant in a recessive gene is not independently sufficient for pathogenicity.

---

### PS3 - Functional Studies

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product. Note: Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.

**VCEP Specifications:**

Functional studies with sufficient analyses to calculate OddsPath reaching strong have not been identified. Therefore, the strength of this criterion is modified to PS3_moderate or PS3_supporting for future or existing studies.

| Strength | Criteria |
|----------|----------|
| **Moderate** | In vitro enzyme activity <50% compared to wild type controls. Expression systems placing the mutant (and wild-type) cDNAs into plasmid vectors and introducing these into human or other mammalian host cells (e.g., COS cells) (Trunzo et al. Gene. 2016. 594:138-143. PMID: 27620137). With **≥11** benign/pathogenic variant controls used in assay. |
| **Supporting** | In vitro enzyme activity **≤50%** compared to wild type controls with **≤10** benign/pathogenic variant controls used in assay. |

**Notes:**
- No papers meeting PS3_Moderate criteria have been identified by the PAH VCEP at the time of this specification update. However, there may be future studies that meet the above criteria where a moderate level of evidence can be applied.
- PS3 at Strong level is not currently applicable for PAH.

#### Approved Assay Instances

The following tyrosine formation assays have been approved for use at PS3_supporting level:

| PMID | Author | Year | Expression System | Proposed Strength |
|------|--------|------|-------------------|-------------------|
| 18477464 | Li, J | 2008 | E. coli (C41(DE3)) | PS3_supporting |
| 14999516 | Zoidakis, J | 2004 | E. coli | PS3_supporting |
| 15917086 | Miranda, FF | 2005 | E. coli (pMAL vectors) | PS3_supporting |
| 11368310 | Jennings, Cotton | 2000 | E. coli (pGEX-2T, DH10b) | PS3_supporting |
| 12733906 | Kemsley, JN | 2003 | E. coli BL21(DE3) | PS3_supporting |

**Assay Description:** In vitro expression of cDNA constructs in E. coli followed by assay of tyrosine formation from phenylalanine. A coupled assay with dihydropteridine reductase and NADH was used to measure tetrahydropterin oxidation.

---

### PS4 - Prevalence in Affected

**Original ACMG Summary:** The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.

**VCEP Specifications:** ***Not Applicable***

This criterion is not applicable for PAH. For proband counting, use the PM3 criterion.

---

### PM1 - Mutational Hot Spot

**Original ACMG Summary:** Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Moderate** | Variant located in one of the following critical residue/domain sets (see below). **Do not apply if PP3_Strong applies.** |

**Active site residues in PAH:**
- Tyr138, Arg158, Val245, Tyr268, Thr278, Pro279, Glu289, Ala300, Asp315, Phe331, Ala345, Gly346, Ser349, Tyr377

**Substrate binding residues in PAH:**
- Residues 46–48, 63–69

**Cofactor binding residues in PAH:**
- His285, His290, Glu330, residues 246–266, 280–283, 322–326, 377–379

**Modification Type:** Gene-specific

> **Important:** PP3 + PM1 combined should not exceed Strong level evidence.

---

### PM2 - Absent from Controls

**Original ACMG Summary:** Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium. Caveat: Population data for indels may be poorly called by next generation sequencing.

**VCEP Specification (Supporting only):**
- gnomAD popmax filtering allele frequency **<0.0002 (0.02%)**

**Rationale:** The 0.0002 cutoff is based on disease frequency of 1:12,000 and the most common PAH pathogenic variant, R408W (ExAC MAF: 0.001109, 74/66718 European Non-Finnish; gnomAD overall: 0.0009056, gnomAD MAF: 0.001728, 219/126,700 European Non-Finnish).

**Modification Type:** Strength

---

### PM3 - In Trans with Pathogenic

**Original ACMG Summary:** For recessive disorders, detected in trans with a pathogenic variant. Note: This requires testing of parents (or offspring) to determine phase.

**VCEP Specifications:** Applicable as described in SVI recommendations for in trans criterion at all strength levels.

#### PM3 Point System (Per Proband)

| Classification/Zygosity of Other Variant | Confirmed in Trans | Phase Unknown |
|------------------------------------------|-------------------|---------------|
| Pathogenic or Likely pathogenic variant | 1.0 | 0.5 (P) / 0.25 (LP) |
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

**Modification Type:** Strength

---

### PM4 - Protein Length Changes

**Original ACMG Summary:** Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Moderate** | Applicable as described (no change from original ACMG). |

**Modification Type:** No change

---

### PM5 - Novel Missense at Same Residue

**Original ACMG Summary:** Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before. Example: Arg156His is pathogenic; now you observe Arg156Cys. Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Moderate** | Applicable as described (no change). |
| **Supporting** | Applicable when the different missense change is **likely pathogenic** (rather than pathogenic). |

**Modification Type:** No change (Moderate); Strength (Supporting)

---

### PM6 - De Novo (Assumed)

**Original ACMG Summary:** Assumed de novo, but without confirmation of paternity and maternity.

**VCEP Specifications:** ***Not Applicable***

---

### PP1 - Co-segregation

**Original ACMG Summary:** Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease. Note: May be used as stronger evidence with increasing segregation data.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | 3 affected segregations + 0 unaffected segregations **OR** 2 affected segregations + 3 unaffected segregations |
| **Moderate** | 2 affected segregations + 0 unaffected segregations |
| **Supporting** | 1 affected family member + 3 unaffected segregations |

**Modification Type:** Strength

---

### PP2 - Missense in Constrained Gene

**Original ACMG Summary:** Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.

**VCEP Specifications:** ***Not Applicable***

---

### PP3 - Computational Evidence

**Original ACMG Summary:** Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.). Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.

**VCEP Specifications:**
- Per SVI recommendations (PMID: 36865205), PP3 should **not** be used for variants with experimental evidence of altered splicing.
- For variants without experimental evidence of altered splicing, PP3 can be used for variants that have a SpliceAI delta score of ≥0.2.

| Strength | Criteria |
|----------|----------|
| **Strong** | REVEL score **≥0.932** for missense variants (per Pejaver et al., PMID: 36413997). PP3 + PM1 should not exceed Strong. |
| **Moderate** | REVEL score **0.773–0.932** for missense variants (per Pejaver et al., PMID: 36413997). |
| **Supporting** | REVEL score **0.644–0.733** for missense variants (per Pejaver et al., PMID: 36413997); **OR** In-frame deletion or insertion predicted deleterious by 2 out of 3 tools (PROVEAN, MutationTaster, MutPred-InDel); **OR** Predicted impact on splicing by SpliceAI (score >0.5). |

**Modification Type:** Strength

> **Important:** PP3 + PM1 combined should not exceed Strong level evidence. If PP3_Strong applies, do not also apply PM1.

#### PP3 REVEL Data Summary

There are 304 PAH variants submitted to ClinVar that have a REVEL score:
- 151 variants have REVEL ≥0.932 (32 P, 70 LP, 49 VUS)
- 91 variants have REVEL 0.773–0.932 (26 P, 41 LP, 24 VUS)
- 30 variants have REVEL 0.644–0.773 (2 P, 12 LP, 16 VUS) — only 5 variants have PP3 applied
- 30 variants have REVEL <0.644 (8 P, 7 LP, 14 VUS, 1 LB) — only 2 variants have PP3 applied, 5 VUS with BP4 applied

---

### PP4 - Phenotype Specificity

**Original ACMG Summary:** Patient's phenotype or family history is highly specific for a disease with a single genetic etiology.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Moderate** | Plasma phenylalanine concentration persistently above 120 µmol/L (2 mg/dL), **AND** either normal urine pterins and normal DHPR activity, **OR** sequencing of genes in the BH4 cofactor metabolism pathway to exclude a defect of BH4 cofactor metabolism. |
| **Supporting** | A plasma phenylalanine concentration persistently above 120 µmol/L (2 mg/dL) **without** analysis of urine pterins, DHPR activity, or sequencing to exclude defects of BH4 cofactor metabolism. |

**Modification Type:** Disease-specific, Strength

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
- gnomAD popmax filtering allele frequency **≥0.015 (1.5%)**

**Rationale:** Calculated with genetic heterogeneity of 90% to account for defects of BH4 metabolism, and penetrance of 80% to account for individuals who come to attention after becoming clinically symptomatic.

**Modification Type:** Disease-specific

---

### BS1 - Frequency Greater Than Expected

**Original ACMG Summary:** Allele frequency is greater than expected for disorder.

**VCEP Specification (Strong):**
- gnomAD popmax filtering allele frequency **≥0.002 (0.2%)**

**Modification Type:** Disease-specific

---

### BS2 - Observed in Healthy Adult

**Original ACMG Summary:** Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | Only to be used when variant is observed in the **homozygous state** in a healthy adult. |

**Modification Type:** None

---

### BS3 - Functional Studies (No Effect)

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Supporting** | In vitro enzyme activity **>85%** compared to wild type. Expression systems: placing the mutant (and wildtype) cDNA into plasmid vectors and introducing these into host cells. Transiently transfected human or other mammalian host cells are the closest available approximation to the in vivo situation (e.g., COS cells) (Trunzo et al. Gene. 2016. 594:138-143). |

**Modification Type:** Disease-specific, Strength

---

### BS4 - Lack of Segregation

**Original ACMG Summary:** Lack of segregation in affected members of a family. Caveat: The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | Applicable as described (no change). |

**Modification Type:** None

---

### BP1-BP7 - Benign Supporting

| Criterion | Status | Comment |
|-----------|--------|---------|
| **BP1** | Not Applicable | Missense variant in a gene for which primarily truncating variants are known to cause disease. |
| **BP2** | Not Applicable | Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder or observed in cis with a pathogenic variant in any inheritance pattern. |
| **BP3** | Not Applicable | In-frame deletions/insertions in a repetitive region without a known function. |
| **BP4** | Applicable (Supporting through Very Strong) | See BP4 details below. |
| **BP5** | Applicable (Supporting) | Variant found in a case with an alternate molecular basis for disease. Applicable as described. |
| **BP6** | Not Applicable | Not for use as recommended by the ClinGen SVI VCEP Review Committee (PMID: 29543229). |
| **BP7** | Applicable (Supporting and Strong) | See BP7 details below. |

#### BP4 - Computational Evidence (Benign)

**Original ACMG Summary:** Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc). BP4 can be used only once in any evaluation of a variant.

**VCEP Specifications:** BP4_very strong: applicable as described in Pejaver et al.

| Strength | Criteria |
|----------|----------|
| **Very Strong** | Applicable as described in Pejaver et al. (PMID: 36413997) |
| **Strong** | Applicable as described in Pejaver et al. |
| **Moderate** | Applicable as described in Pejaver et al. |
| **Supporting** | REVEL score **0.183–0.290** for missense variants; **OR** In-frame deletion or insertion predicted benign by PROVEAN, MutationTaster, and MutPred-InDel; **OR** No predicted impact on splicing by SpliceAI (score <0.1). |

**Modification Type:** Gene-specific

#### BP7 - Synonymous Variant

**Original ACMG Summary:** A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.

| Strength | Criteria |
|----------|----------|
| **Strong** | Applicable as described by Walker et al. (PMID: 36865205). For variants with experimental evidence supporting that they do not alter splicing, use BP7_strong (RNA). |
| **Supporting** | Per SVI recommendations (PMID: 36865205), use BP7 only if BP4 is met. Intronic variants must be outside +7/−21 nt. Exonic variants must be outside first and last 3 bases of exon. |

**Modification Type:** Gene-specific, Strength

---

## Rules for Combining Criteria

### Pathogenic Classification

| Criteria Combination |
|---------------------|
| 1 Very Strong *(PVS1, PM3_VeryStrong)* **AND** ≥1 Strong *(PVS1_Strong, PS1, PS2, PM3_Strong, PP1_Strong, PP3_Strong)* |
| 1 Very Strong *(PVS1, PM3_VeryStrong)* **AND** ≥2 Moderate *(PS3_Moderate, PM1, PM3, PM4, PM5, PP1_Moderate, PP3_Moderate, PP4_Moderate)* |
| 1 Very Strong *(PVS1, PM3_VeryStrong)* **AND** 1 Moderate *(PS3_Moderate, PM1, PM3, PM4, PM5, PP1_Moderate, PP3_Moderate, PP4_Moderate)* **AND** 1 Supporting *(PS3_Supporting, PM2_Supporting, PM3_Supporting, PM5_Supporting, PP1, PP3, PP4)* |
| 1 Very Strong *(PVS1, PM3_VeryStrong)* **AND** ≥2 Supporting *(PS3_Supporting, PM2_Supporting, PM3_Supporting, PM5_Supporting, PP1, PP3, PP4)* |
| ≥2 Strong *(PVS1_Strong, PS1, PS2, PM3_Strong, PP1_Strong, PP3_Strong)* |
| 1 Strong *(PVS1_Strong, PS1, PS2, PM3_Strong, PP1_Strong, PP3_Strong)* **AND** ≥3 Moderate *(PS3_Moderate, PM1, PM3, PM4, PM5, PP1_Moderate, PP3_Moderate, PP4_Moderate)* |
| 1 Strong *(PVS1_Strong, PS1, PS2, PM3_Strong, PP1_Strong, PP3_Strong)* **AND** 2 Moderate *(PS3_Moderate, PM1, PM3, PM4, PM5, PP1_Moderate, PP3_Moderate, PP4_Moderate)* **AND** ≥2 Supporting *(PS3_Supporting, PM2_Supporting, PM3_Supporting, PM5_Supporting, PP1, PP3, PP4)* |
| 1 Strong *(PVS1_Strong, PS1, PS2, PM3_Strong, PP1_Strong, PP3_Strong)* **AND** 1 Moderate *(PS3_Moderate, PM1, PM3, PM4, PM5, PP1_Moderate, PP3_Moderate, PP4_Moderate)* **AND** ≥4 Supporting *(PS3_Supporting, PM2_Supporting, PM3_Supporting, PM5_Supporting, PP1, PP3, PP4)* |

### Likely Pathogenic Classification

| Criteria Combination |
|---------------------|
| 1 Very Strong *(PVS1, PM3_VeryStrong)* **AND** 1 Moderate *(PS3_Moderate, PM1, PM3, PM4, PM5, PP1_Moderate, PP3_Moderate, PP4_Moderate)* |
| 1 Strong *(PVS1_Strong, PS1, PS2, PM3_Strong, PP1_Strong, PP3_Strong)* **AND** 1 Moderate *(PS3_Moderate, PM1, PM3, PM4, PM5, PP1_Moderate, PP3_Moderate, PP4_Moderate)* |
| 1 Strong *(PVS1_Strong, PS1, PS2, PM3_Strong, PP1_Strong, PP3_Strong)* **AND** ≥2 Supporting *(PS3_Supporting, PM2_Supporting, PM3_Supporting, PM5_Supporting, PP1, PP3, PP4)* |
| ≥3 Moderate *(PS3_Moderate, PM1, PM3, PM4, PM5, PP1_Moderate, PP3_Moderate, PP4_Moderate)* |
| 2 Moderate *(PS3_Moderate, PM1, PM3, PM4, PM5, PP1_Moderate, PP3_Moderate, PP4_Moderate)* **AND** ≥2 Supporting *(PS3_Supporting, PM2_Supporting, PM3_Supporting, PM5_Supporting, PP1, PP3, PP4)* |
| 1 Moderate *(PS3_Moderate, PM1, PM3, PM4, PM5, PP1_Moderate, PP3_Moderate, PP4_Moderate)* **AND** ≥4 Supporting *(PS3_Supporting, PM2_Supporting, PM3_Supporting, PM5_Supporting, PP1, PP3, PP4)* |
| 1 Strong *(PVS1_Strong, PS1, PS2, PM3_Strong, PP1_Strong, PP3_Strong)* **AND** 2 Moderate *(PS3_Moderate, PM1, PM3, PM4, PM5, PP1_Moderate, PP3_Moderate, PP4_Moderate)* |

### Benign Classification

| Criteria Combination |
|---------------------|
| ≥2 Strong *(BS1, BS2, BS4, BP4_Strong, BP7_Strong)* |
| 1 Stand Alone *(BA1)* |

### Likely Benign Classification

| Criteria Combination |
|---------------------|
| 1 Strong *(BS1, BS2, BS4, BP4_Strong, BP7_Strong)* **AND** 1 Supporting *(BS3_Supporting, BP4, BP5, BP7)* |
| ≥2 Supporting *(BS3_Supporting, BP4, BP5, BP7)* |

---

## Appendices

### Appendix A: PVS1 Decision Tree

The PAH PVS1 decision tree provides gene-specific guidance for classifying null variants. Key parameters:

**Critical Protein Regions:**
- **Autoregulatory sequence:** amino acid residues 1–33
- **PAH catalytic domain:** amino acid residues 143–410
- **Oligomerization domain:** amino acid residues 411–452

**NMD Boundary:** c.1285 (variants upstream are predicted to undergo NMD)

**Biologically-relevant transcript:** NM_000277.3

**Reading frame-preserving exon skipping:** Exons 1, 9, 10

**Last exon:** Exon 13 (splice variants affecting this exon — reading frame disrupted but NOT predicted to undergo NMD)

**Initiation codon:** Closest potential in-frame alternative start codon at p.Met180

### Appendix B: Criteria Applicability Summary

| Criterion | Max Strength | Status |
|-----------|-------------|--------|
| PVS1 | Very Strong | Applicable (use decision tree) |
| PS1 | Strong | Applicable (disease-specific) |
| PS2 | Strong | Applicable (requires P variant in trans) |
| PS3 | Moderate | Applicable (modified strength) |
| PS4 | — | **Not Applicable** (use PM3) |
| PM1 | Moderate | Applicable (gene-specific residues) |
| PM2 | Supporting | Applicable (<0.0002) |
| PM3 | Very Strong | Applicable (SVI point system) |
| PM4 | Moderate | Applicable (no change) |
| PM5 | Moderate / Supporting | Applicable |
| PM6 | — | **Not Applicable** |
| PP1 | Strong | Applicable (segregation thresholds) |
| PP2 | — | **Not Applicable** |
| PP3 | Strong | Applicable (REVEL thresholds) |
| PP4 | Moderate | Applicable (Phe >120 µmol/L) |
| PP5 | — | **Not Applicable** |
| BA1 | Stand Alone | Applicable (≥0.015) |
| BS1 | Strong | Applicable (≥0.002) |
| BS2 | Strong | Applicable (homozygous in healthy adult) |
| BS3 | Supporting | Applicable (enzyme activity >85%) |
| BS4 | Strong | Applicable (no change) |
| BP1 | — | **Not Applicable** |
| BP2 | — | **Not Applicable** |
| BP3 | — | **Not Applicable** |
| BP4 | Very Strong | Applicable (Pejaver et al. thresholds) |
| BP5 | Supporting | Applicable (no change) |
| BP6 | — | **Not Applicable** |
| BP7 | Strong | Applicable (Walker et al.) |

### Appendix C: Population Frequency Thresholds Summary

| Criterion | Threshold | Strength |
|-----------|-----------|----------|
| BA1 | ≥0.015 (1.5%) | Stand Alone |
| BS1 | ≥0.002 (0.2%) | Strong |
| PM2 | <0.0002 (0.02%) | Supporting |

### Appendix D: PS3/BS3 Functional Evidence Thresholds

| Enzyme Activity | Evidence Direction | Criterion | Strength |
|----------------|-------------------|-----------|----------|
| <50% of WT (≥11 controls) | Pathogenic | PS3 | Moderate |
| ≤50% of WT (≤10 controls) | Pathogenic | PS3 | Supporting |
| >85% of WT | Benign | BS3 | Supporting |
| 50–85% of WT | Indeterminate | — | Not applicable |

### Appendix E: PP3/BP4 Computational Evidence Thresholds (REVEL)

| REVEL Score Range | Criterion | Strength |
|-------------------|-----------|----------|
| ≥0.932 | PP3 | Strong |
| 0.773–0.932 | PP3 | Moderate |
| 0.644–0.733 | PP3 | Supporting |
| 0.291–0.643 | — | Indeterminate |
| 0.183–0.290 | BP4 | Supporting |
| <0.183 | BP4 | Moderate to Very Strong (per Pejaver et al.) |

### Appendix F: Reference PMIDs

| PMID | Reference |
|------|-----------|
| 29543229 | ClinGen SVI recommendation on PP5/BP6 removal |
| 36865205 | Walker et al. — SVI splicing recommendations |
| 36413997 | Pejaver et al. — Calibration of computational tools |
| 27620137 | Trunzo et al. — PAH expression system for functional assays |
| 18477464 | Li, J — Tyrosine formation assay (E. coli) |
| 14999516 | Zoidakis, J — Y179F/Y179A characterization |
| 15917086 | Miranda, FF — Y325 mutant characterization |
| 11368310 | Jennings, Cotton — Active site mutagenesis |
| 12733906 | Kemsley, JN — R158Q/E280K kinetics and spectroscopy |

---

## Version History

| Version | Date | Notes |
|---------|------|-------|
| 2.0.0 | 7/16/2024 | Major update with many changes. Response to SVI comments in PM1 and PP3, with attachments for PVS1 and PS3. |
| 1.0.0 | — | Initial VCEP specification (prior version). |

---

*This document was compiled from ClinGen Phenylketonuria VCEP specifications and ClinGen SVI recommendations. For the most current version, please refer to the ClinGen website.*
