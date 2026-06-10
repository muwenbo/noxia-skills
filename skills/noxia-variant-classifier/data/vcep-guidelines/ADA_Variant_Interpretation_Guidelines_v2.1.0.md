# Comprehensive Variant Interpretation Guidelines for ADA

## ClinGen SCID VCEP Specifications for ADA-SCID (Version 2.1.0)

**Affiliation:** Severe Combined Immunodeficiency Disease Variant Curation Expert Panel (SCID VCEP)
**Version:** 2.1.0
**Release Date:** October 1, 2025
**Based on:** Richards et al., 2015 - ACMG/AMP Variant Interpretation Guidelines

---

## Table of Contents

1. [Gene and Disease Information](#1-gene-and-disease-information)
2. [Pathogenic Criteria](#2-pathogenic-criteria)
   - [PVS1 - Null Variant](#pvs1---null-variant)
   - [PS1 - Same Amino Acid Change](#ps1---same-amino-acid-change)
   - [PS2 - De Novo (Confirmed)](#ps2---de-novo-confirmed)
   - [PS3 - Functional Studies](#ps3---functional-studies)
   - [PM2 - Absent from Controls](#pm2---absent-from-controls)
   - [PM3 - In Trans with Pathogenic Variant](#pm3---in-trans-with-pathogenic-variant)
   - [PM4 - Protein Length Changes](#pm4---protein-length-changes)
   - [PM5 - Novel Missense at Same Residue](#pm5---novel-missense-at-same-residue)
   - [PM6 - De Novo (Assumed)](#pm6---de-novo-assumed)
   - [PP1 - Co-segregation](#pp1---co-segregation)
   - [PP3 - Computational Evidence](#pp3---computational-evidence)
   - [PP4 - Phenotype Specificity](#pp4---phenotype-specificity)
3. [Benign Criteria](#3-benign-criteria)
   - [BA1 - Stand-Alone Benign](#ba1---stand-alone-benign)
   - [BS1 - Allele Frequency Greater Than Expected](#bs1---allele-frequency-greater-than-expected)
   - [BS2 - Observed in Healthy Adult](#bs2---observed-in-healthy-adult)
   - [BS3 - Functional Studies (Benign)](#bs3---functional-studies-benign)
   - [BS4 - Lack of Segregation](#bs4---lack-of-segregation)
   - [BP7 - Synonymous/Intronic Variants](#bp7---synonymousintronic-variants)
4. [Not Applicable Criteria](#4-not-applicable-criteria)
5. [Rules for Combining Criteria](#5-rules-for-combining-criteria)
6. [Appendices](#6-appendices)

---

## 1. Gene and Disease Information

| Parameter | Value |
|-----------|-------|
| **Gene** | ADA (HGNC:186) |
| **HGNC Name** | Adenosine Deaminase |
| **Reference Transcript** | NM_000022.4 |
| **Disease** | Severe Combined Immunodeficiency, Autosomal Recessive, T cell-negative, B cell-negative, NK cell-negative, due to Adenosine Deaminase Deficiency |
| **MONDO ID** | MONDO:0007064 |
| **Mode of Inheritance** | Autosomal Recessive |
| **Mechanism of Disease** | Loss of Function (LOF) |

### Key Gene Characteristics

- ADA encodes adenosine deaminase, an enzyme critical for purine metabolism
- Loss of ADA function leads to accumulation of toxic metabolites (dATP, dAXP) that impair lymphocyte development
- The gnomAD v2.1.1 missense Z score for ADA (Z = 0.12) suggests this gene is not constrained for missense variation
- Both benign and pathogenic missense variants are present in ADA

---

## 2. Pathogenic Criteria

### PVS1 - Null Variant

**Original ACMG Summary:** Null variant (nonsense, frameshift, canonical ±1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.

**VCEP Specification:** Use ClinGen SVI recommendations for loss of function criterion (Tayoun et al., 2018; PMID: 30192042) with ADA-specific modifications.

#### General Caveats

- Beware of genes where LOF is not a known disease mechanism (e.g., GFAP, MYH7)
- Use caution interpreting LOF variants at the extreme 3' end of a gene
- Use caution with splice variants predicted to lead to exon skipping but leave the remainder of the protein intact
- Use caution in the presence of multiple transcripts

#### Strength Levels

| Strength | Application |
|----------|-------------|
| **PVS1** (Very Strong) | Follow ClinGen SVI flowchart for standard LOF variants predicted to undergo NMD |
| **PVS1_Strong** | Variants not predicted to undergo NMD but removing >10% of protein AND at least one pathogenic variant present downstream |
| **PVS1_Moderate** | Variants not predicted to undergo NMD but removing >10% of protein AND no pathogenic variant present downstream |
| **PVS1_Supporting** | Per ClinGen SVI recommendations |

#### ADA-Specific NMD Considerations

Variants **NOT predicted to undergo NMD** include those with premature stop codon in:
- The last exon (exon 12)
- The last 50 nucleotides of the penultimate exon (after c.1028, codon 343, in exon 11)

#### PVS1 Decision Flowchart Summary

##### Nonsense or Frameshift Variants

| Condition | PVS1 Strength |
|-----------|---------------|
| Predicted to undergo NMD + Exon present in biologically-relevant transcript(s) | **PVS1** |
| Predicted to undergo NMD + Exon absent from biologically-relevant transcript(s) | N/A |
| Not predicted to undergo NMD + Truncated region critical to protein function | **PVS1_Strong** |
| Not predicted to undergo NMD + Role unknown + LoF variants frequent in population | N/A |
| Not predicted to undergo NMD + Role unknown + Variant removes >10% protein + 1+ pathogenic variant downstream | **PVS1_Strong** |
| Not predicted to undergo NMD + Role unknown + Variant removes >10% protein + No pathogenic variant downstream | **PVS1_Moderate** |
| Not predicted to undergo NMD + Role unknown + Variant removes <10% protein | **PVS1_Moderate** |

##### Splice Site Variants (GT-AG ±1,2)

| Condition | PVS1 Strength |
|-----------|---------------|
| Exon skipping disrupts reading frame + predicted NMD + Exon in biologically-relevant transcript | **PVS1** |
| Exon skipping disrupts reading frame + NOT predicted NMD + 1+ pathogenic variant downstream | **PVS1_Strong** |
| Exon skipping disrupts reading frame + NOT predicted NMD + No pathogenic variant downstream | **PVS1_Moderate** |
| Exon skipping preserves reading frame + Variant removes >10% + 1+ pathogenic variant in deleted region | **PVS1_Strong** |
| Exon skipping preserves reading frame + Variant removes >10% + No pathogenic variant in deleted region | **PVS1_Moderate** |

##### Deletions (Single Exon to Full Gene)

| Condition | PVS1 Strength |
|-----------|---------------|
| Full gene deletion | **PVS1** |
| Disrupts reading frame + predicted NMD + Exon present in biologically-relevant transcript | **PVS1** |
| Disrupts reading frame + NOT predicted NMD + 1+ pathogenic variant in deleted region | **PVS1_Strong** |
| Disrupts reading frame + NOT predicted NMD + No pathogenic variant in deleted region | **PVS1_Moderate** |
| Preserves reading frame + Truncated region critical to protein function | **PVS1_Strong** |

##### Duplications (≥1 Exon, Completely Contained Within Gene)

| Condition | PVS1 Strength |
|-----------|---------------|
| Proven in tandem + Reading frame disrupted + NMD predicted | **PVS1** |
| Proven in tandem + No/unknown impact on reading frame | N/A |
| Presumed in tandem + Reading frame presumed disrupted + NMD predicted | **PVS1_Strong** |
| Proven not in tandem | N/A |

##### Initiation Codon Variants

| Condition | PVS1 Strength |
|-----------|---------------|
| No known alternative start codon + ≥1 pathogenic variant upstream of closest potential in-frame start codon | **PVS1_Moderate** |
| No known alternative start codon + No pathogenic variant upstream | **PVS1_Supporting** |
| Different functional transcript uses alternative start codon | N/A |

---

### PS1 - Same Amino Acid Change

**Original ACMG Summary:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.

**Caveat:** Beware of changes that impact splicing rather than at the amino acid/protein level.

#### VCEP Specifications

| Strength | Application |
|----------|-------------|
| **PS1_Strong** | Applicable if previously established variant is classified as **Pathogenic** by SCID VCEP specifications for ADA |
| **PS1_Moderate** | Applicable if previously established variant is classified as **Likely Pathogenic** by SCID VCEP specifications for ADA |

#### Special Application for Splice Variants

PS1 can be applied for splice variants at the same nucleotide with similar impact prediction as previously reported pathogenic variant (if the predicted impact is equal to or greater than the known pathogenic variant per in silico splicing tool SpliceAI).

**Example:** c.105+1G>C is known to be pathogenic → can use PS1 for c.105+1G>T

---

### PS2 - De Novo (Confirmed)

**Original ACMG Summary:** De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.

**Note:** Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.

#### VCEP Specifications

Use ClinGen SVI recommendations for de novo criteria with ADA-specific phenotypic consistency guidelines.

##### Phenotypic Consistency Categories

| Category | Definition for ADA |
|----------|-------------------|
| **Phenotype highly specific for gene** | Proband must meet at least **PP4_Moderate** criteria |
| **Phenotype consistent with gene but not highly specific** | Proband must meet **PP4** criteria |
| **Phenotype consistent with gene but not highly specific and high genetic heterogeneity** | Proband has been asserted to have a SCID phenotype but does not meet PP4 criteria |

**Important:** Reduce points per proband by half if the phase is unconfirmed.

##### Points Awarded per De Novo Occurrence

| Phenotypic Consistency | Confirmed Parental Relationships | Unconfirmed Parental Relationships |
|------------------------|----------------------------------|-----------------------------------|
| Phenotype highly specific for gene | 2 | 1 |
| Phenotype consistent but not highly specific | 1 | 0.5 |
| Consistent but not highly specific + high genetic heterogeneity* | 0.5 | 0.25 |
| Phenotype not consistent with gene | 0 | 0 |

*Maximum allowable value of 1 may contribute to overall score

##### Determining Evidence Strength Level

| Total Points | Evidence Strength |
|--------------|-------------------|
| 0.5 | PS2_Supporting |
| 1 | PS2_Moderate |
| 2 | PS2 (Strong) |
| 4 | PS2_VeryStrong |

##### Additional Considerations

- **Autosomal recessive conditions:** For a de novo occurrence without an additional pathogenic/likely pathogenic variant identified, the strength of evidence should be decreased by one level
- **Mosaicism:** For apparent germline mosaicism (multiple affected siblings with both parents negative), parental relationships must be confirmed for de novo criteria to apply

---

### PS3 - Functional Studies

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.

#### VCEP Specifications

##### PS3_Strong

PS3 may be applied at default strength level of **Strong** for evidence from an **animal model** expressing the variant of interest and recapitulating the ADA-SCID phenotype.

##### PS3_Moderate

Apply when expressed ADA enzyme activity is **≤0.05%** of wild-type activity (Group I per Arredondo-Vega et al., 1998; PMID: 9758612).

**Requirement:** At least one previously observed proband with the expressed ADA variant meeting PP4 is required.

##### PS3_Supporting

Apply when expressed ADA enzyme activity is **0.06-0.6%** of wild-type activity (Groups II and III per Arredondo-Vega et al., 1998).

**Requirement:** At least one previously observed proband with the expressed ADA variant meeting PP4 is required.

#### Approved Functional Assays

| Assay | Reference | Description |
|-------|-----------|-------------|
| Expressed ADA Activity | Akeson...Hutton (1988); PMID: 3182793 | Human fibroblast cell line GM4429 transfected with ADA expression vector |
| Expressed ADA Activity | Arredondo-Vega...Hershfield (1998); PMID: 9758612 | ADA-deleted E. coli transformed with ADA expression vector |

#### Functional Activity Groups (Arredondo-Vega et al., 1998)

| Group | ADA Activity (% of Wild-Type) | Clinical Phenotype | PS3 Strength |
|-------|------------------------------|-------------------|--------------|
| **Group I** | ≤0.05% (~0.012%) | Severe | PS3_Moderate |
| **Group II** | ~0.06-0.15% (~0.11%) | Moderate-Severe | PS3_Supporting |
| **Group III** | ~0.15-0.6% (~0.42%) | Moderate | PS3_Supporting |
| **Group IV** | ≥4.8% | Normal/Benign | BS3_Supporting |

---

### PM2 - Absent from Controls

**Original ACMG Summary:** Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes, or Exome Aggregation Consortium.

**Caveat:** Population data for indels may be poorly called by next generation sequencing.

#### VCEP Specification

| Strength | Threshold |
|----------|-----------|
| **PM2_Supporting** | gnomAD popmax filtering allele frequency **<0.0001742** |

**Additional Requirement:** No homozygotes observed in gnomAD.

---

### PM3 - In Trans with Pathogenic Variant

**Original ACMG Summary:** For recessive disorders, detected in trans with a pathogenic variant.

**Note:** This requires testing of parents (or offspring) to determine phase.

#### VCEP Specifications

Use ClinGen SVI adapted recommendations for in trans criterion with the additional requirement that the **co-occurring variant must be classified using the SCID VCEP specifications for ADA**.

**Caveat:** All variants should be sufficiently rare (meet PM2 specification). The applicability of PM3 to suspected founder variants with allele frequencies exceeding the PM2 threshold will be evaluated on a case-by-case basis by the VCEP.

##### Points Awarded per In Trans Proband

| Classification/Zygosity of Other Variant | Confirmed In Trans | Phase Unknown |
|------------------------------------------|-------------------|---------------|
| Pathogenic or Likely Pathogenic variant | 1.0 | 0.5 (P) / 0.25 (LP) |
| Homozygous (Non-consanguineous) | 1.0 | 1.0 |
| Homozygous (Consanguineous)* | 0.5 | 0.5 |
| Uncertain Significance variant** | 0.25 | 0.0 |

*Maximum 0.5 points per family
**Maximum 0.5 points total

##### Determining Evidence Strength Level

| Total Points | Evidence Strength |
|--------------|-------------------|
| 0.5 | PM3_Supporting |
| 1.0 | PM3 (Moderate) |
| 2.0 | PM3_Strong |
| 4.0 | PM3_VeryStrong |

##### Key Considerations

- **Allele Frequency:** Both variants must meet PM2 threshold
- **Phasing:** If phase unknown, at least two different LP/P variants needed to equal weight of one confirmed in trans
- **Classification:** Avoid circularity - classification of variant on other allele should not use evidence from variant being interrogated
- **Homozygous:** Rare homozygous may be due to consanguinity; max 1.0 points recommended for all homozygous cases

---

### PM4 - Protein Length Changes

**Original ACMG Summary:** Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

#### VCEP Specifications

| Strength | Application |
|----------|-------------|
| **PM4_Moderate** | Deleted region must contain a known **Pathogenic or Likely Pathogenic** variant not predicted/observed to alter splicing |
| **PM4_Supporting** | Deleted region must contain a known **VUS** variant not predicted/observed to alter splicing |

---

### PM5 - Novel Missense at Same Residue

**Original ACMG Summary:** Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.

**Caveat:** Beware of changes that impact splicing rather than at the amino acid/protein level.

#### VCEP Specifications for Missense Variants

| Strength | Application |
|----------|-------------|
| **PM5_Moderate** | Previously established variant is classified as **Pathogenic** |
| **PM5_Supporting** | Previously established variant is classified as **Likely Pathogenic** |

#### VCEP Specifications for Nonsense Variants

A point-based system is used for nonsense variants:

##### Point Table for Nonsense Variants

| VUA Type | Informative Variant | Score |
|----------|---------------------|-------|
| Nonsense predicted to lead to NMD | P/LP variant in exon predicted to lead to NMD | +1 pt |
| Nonsense predicted to lead to NMD | B/LB variant in exon predicted to lead to NMD | -2 pt |
| Nonsense in final exon (no NMD) | P/LP variant resulting in PTC downstream of VUA | +1 pt |
| Nonsense in final exon (no NMD) | B/LB variant resulting in PTC upstream of VUA | -2 pt |

*NMD = nonsense-mediated decay; PTC = premature termination codon; VUA = variant under assessment*

##### Evidence Strength from Points

| Total Points | Evidence Strength | Special Rules |
|--------------|-------------------|---------------|
| 1 point | PM5_Supporting | - |
| 2+ points | PM5_Moderate | Cannot combine with PVS1_VeryStrong (downgrade to PM5_Supporting) |
| 4+ points | PM5_Strong | Downgrade to PM5_Moderate if PVS1 applied at any strength |

##### Important Notes

- Informative variant must be classified by SCID VCEP specifications
- May not be the same variant used to meet "+1 pathogenic variant downstream" on PVS1 flowchart
- If negative points calculated, do not apply PM5 and reconsider PVS1 applicability
- VUA must be sufficiently rare (meet PM2_Supporting)
- If informative variant is frameshift/nonsense, it must reach P/LP classification without PM5 and without only PVS1 + PM2

---

### PM6 - De Novo (Assumed)

**Original ACMG Summary:** Assumed de novo, but without confirmation of paternity and maternity.

#### VCEP Specifications

Use ClinGen SVI recommendations for de novo criteria (same as PS2) with unconfirmed parental relationships.

See [PS2 Section](#ps2---de-novo-confirmed) for phenotypic consistency guidelines and point tables.

| Strength | Application |
|----------|-------------|
| **PM6_Supporting** | 0.5 total points |
| **PM6** (Moderate) | 1 total point |
| **PM6_Strong** | 2 total points |
| **PM6_VeryStrong** | 4 total points |

---

### PP1 - Co-segregation

**Original ACMG Summary:** Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.

**Note:** May be used as stronger evidence with increasing segregation data.

#### VCEP Specifications

Use ClinGen SVI recommendations for co-segregation criterion (PMID: 30311386) with the additional specification that **unaffected individuals contributing to the calculated LOD score must be heterozygous carriers** of one of the variants observed in the affected individuals (i.e., do not count wild-type/wild-type individuals).

##### General Thresholds

| Strength | Likelihood | LOD Score |
|----------|------------|-----------|
| **PP1_Supporting** | 4:1 | 0.6 |
| **PP1_Moderate** | 16:1 | 1.2 |
| **PP1_Strong** | 32:1 | 1.5 |

##### Autosomal Recessive LOD Score Table

Use this table to determine LOD score based on affected and unaffected segregations:

| Affected Segregations | 0 Unaff | 1 Unaff | 2 Unaff | 3 Unaff | 4 Unaff | 5 Unaff |
|----------------------|---------|---------|---------|---------|---------|---------|
| 0 | 0 | 0.12 | 0.25 | 0.37 | 0.5 | 0.62 |
| 1 | 0.6 | 0.73 | 0.85 | 0.98 | 1.1 | 1.23 |
| 2 | 1.2 | 1.33 | 1.45 | 1.58 | 1.7 | 1.83 |
| 3 | 1.81 | 1.93 | 2.06 | 2.18 | 2.31 | 2.43 |
| 4 | 2.41 | 2.53 | 2.66 | 2.78 | 2.91 | 3.03 |
| 5 | 3.01 | 3.14 | 3.26 | 3.39 | 3.51 | 3.63 |

**Color Legend:**
- LOD 0.6-1.19: PP1_Supporting (Green)
- LOD 1.2-1.49: PP1_Moderate (Yellow)
- LOD ≥1.5: PP1_Strong (Orange/Red)

##### Definitions

- **Affected segregations:** Affected family members in whom biallelic compound heterozygous or homozygous variants segregate
- **Unaffected segregations:** Unaffected family members (typically siblings) at risk to inherit the two variants identified in the proband, who are either wild-type for both variants OR heterozygous carrier for a single variant
- **Note:** Unaffected carrier parents DO NOT count as unaffected segregations

---

### PP3 - Computational Evidence

**Original ACMG Summary:** Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).

**Caveat:** As many in silico algorithms use the same or very similar input, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.

#### VCEP Specification

| Strength | Application |
|----------|-------------|
| **PP3_Supporting** | Only applicable to **synonymous or intronic variants** predicted to impact splicing by SpliceAI with a delta score **≥0.2** |

**Important:** Do NOT apply PP3 to missense variants.

---

### PP4 - Phenotype Specificity

**Original ACMG Summary:** Patient's phenotype or family history is highly specific for a disease with a single genetic etiology.

#### VCEP Specifications

PP4 applicability and strength is determined by the **total points accumulated by a single affected individual** according to the evidence table below.

##### Point Thresholds

| Total Points | PP4 Strength |
|--------------|--------------|
| <1 point | PP4 not met |
| 1 to <2 points | **PP4** (Supporting) |
| 2 to <6 points | **PP4_Moderate** |
| ≥6 points | **PP4_Strong**¹ |

¹CNV testing is required for PP4_Strong to certify that the variant in question is causative for the phenotype, and not one CNV event corrected by gene therapy and not identified previously.

##### Evidence Point Table

| Evidence Description | Points |
|---------------------|--------|
| Diagnostic criteria met for SCID (Criteria 1 and 3 or Criterion 4 by itself) or Leaky SCID/Omenn syndrome (excluding Criterion 2)² | 0.5 |
| SCID gene panel or exome/genome sequencing conducted (only applicable if genetic testing did not provide an alternative genetic explanation for SCID/Leaky SCID/Omenn syndrome phenotype) | 1 |
| Family history of SCID (only applicable if SCID gene panel or exome/genome sequencing was conducted on proband and did not provide an alternative genetic explanation for phenotype) | 0.5 |
| Reduced ADA enzyme activity in patient cells (<1-2% of normal ADA catalytic activity) AND/OR increased dAdo nucleotides (dATP or dAXP) in pretreatment or non-transfused erythrocytes above the reference range (PMIDs: 20301656, 39182630) | 5 |
| ADA-SCID phenotype corrected by exogenous ADA supplementation **WITHOUT** CNV testing performed | 4.5 |
| ADA-SCID phenotype corrected by exogenous ADA supplementation **WITH** CNV testing performed | 6 |
| ADA-SCID phenotype corrected by ADA gene therapy **WITHOUT** CNV testing performed | 4.5 |
| ADA-SCID phenotype corrected by ADA gene therapy **WITH** CNV testing performed | 6 |
| T-B-NK- lymphocyte subset profile* | 0.5 |

²The diagnostic criteria should follow the PIDTC 2022 specification.

##### Notes on Lymphocyte Profile

- If NK cells are not noted or are present, criteria may still be applied if SCID gene panel or exome/genome sequencing has ruled out alternative causes
- If maternal T cells are present, the T lymphocyte profile is still considered to be T- (autologous T cells are absent)

---

## 3. Benign Criteria

### BA1 - Stand-Alone Benign

**Original ACMG Summary:** Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes, or Exome Aggregation Consortium.

#### VCEP Specification

| Strength | Threshold |
|----------|-----------|
| **BA1** (Stand Alone) | gnomAD popmax filtering allele frequency **>0.00721** |

##### Calculation Parameters (Whiffin/Ware Calculator)

- Prevalence: 1:5,000
- Allelic heterogeneity: 1
- Genetic heterogeneity: 0.13 (based on ADA contribution to total SCID in PIDTC 6901 cohort: 12.8%)
- Penetrance: 50%

---

### BS1 - Allele Frequency Greater Than Expected

**Original ACMG Summary:** Allele frequency is greater than expected for disorder.

#### VCEP Specification

| Strength | Threshold |
|----------|-----------|
| **BS1_Strong** | gnomAD popmax filtering allele frequency **>0.00161** |

##### Calculation Parameters (Whiffin/Ware Calculator)

- Prevalence: 1:50,000
- Allelic heterogeneity: 1
- Genetic heterogeneity: 0.13
- Penetrance: 100%

**Note:** Consider also bottleneck populations.

---

### BS2 - Observed in Healthy Adult

**Original ACMG Summary:** Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

#### VCEP Specification

| Strength | Application |
|----------|-------------|
| **BS2_Supporting** | Only applicable when the variant is observed in the **homozygous state** in a healthy adult |

---

### BS3 - Functional Studies (Benign)

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

#### VCEP Specification

| Strength | Application |
|----------|-------------|
| **BS3_Supporting** | Expressed ADA enzyme activity **≥4.8%** of wild-type activity (based on Group IV per Arredondo-Vega et al., 1998; PMID: 9758612) |

---

### BS4 - Lack of Segregation

**Original ACMG Summary:** Lack of segregation in affected members of a family.

**Caveat:** The presence of phenocopies for common phenotypes (i.e., cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder.

#### VCEP Specification

| Strength | Application |
|----------|-------------|
| **BS4_Strong** | Can be applied without additional specifications |

---

### BP7 - Synonymous/Intronic Variants

**Original ACMG Summary:** A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.

#### VCEP Specification

| Strength | Application |
|----------|-------------|
| **BP7_Supporting** | Applicable to both synonymous variants and deep intronic variants affecting nucleotides at or beyond the +7 (donor) and -21 (acceptor) positions |

##### Requirements

- Variant should be predicted NOT to impact splicing by at least 2 out of 3 in silico tools
- Freely available tools include: GeneSplicer, MaxEntScan, NNSplice, SpliceAI, Splicing Sequences Finder (SSF), varSEAK

**Note:** Given the potential for poor conservation of genes related to T cell and B cell development among vertebrates, nucleotide conservation is **NOT required** to apply BP7.

---

## 4. Not Applicable Criteria

The following ACMG/AMP criteria are **NOT APPLICABLE** for ADA variant interpretation:

| Criterion | Original Purpose | Reason Not Applicable |
|-----------|-----------------|----------------------|
| **PS4** | Prevalence in affected individuals | Not specified for ADA |
| **PM1** | Mutational hot spot / critical domain | Not specified for ADA |
| **PP2** | Low rate of benign missense | gnomAD missense Z score (0.12) suggests ADA is not constrained; both benign and pathogenic missense variants present |
| **PP5** | Reputable source reports pathogenic | Not recommended by ClinGen SVI VCEP Review Committee (PMID: 29543229) |
| **BP1** | Missense in truncating disease gene | Does not apply |
| **BP2** | In trans with pathogenic for dominant | Not applicable |
| **BP3** | In-frame deletion in repetitive region | Does not apply |
| **BP4** | Computational evidence (benign) | Not specified for ADA |
| **BP5** | Alternate molecular basis | Not applicable |
| **BP6** | Reputable source reports benign | Not recommended by ClinGen SVI VCEP Review Committee (PMID: 29543229) |

---

## 5. Rules for Combining Criteria

### Pathogenic Classification

| Combination | Classification |
|-------------|----------------|
| 1 Very Strong AND ≥1 Strong | **Pathogenic** |
| 1 Very Strong AND ≥2 Moderate | **Pathogenic** |
| 1 Very Strong AND 1 Moderate AND 1 Supporting | **Pathogenic** |
| 1 Very Strong AND ≥2 Supporting | **Pathogenic** |
| ≥2 Strong | **Pathogenic** |
| 1 Strong AND ≥3 Moderate | **Pathogenic** |
| 1 Strong AND 2 Moderate AND ≥2 Supporting | **Pathogenic** |
| 1 Strong AND 1 Moderate AND ≥4 Supporting | **Pathogenic** |

### Likely Pathogenic Classification

| Combination | Classification |
|-------------|----------------|
| 1 Very Strong AND 1 Moderate | **Likely Pathogenic** |
| 1 Strong AND 1 Moderate | **Likely Pathogenic** |
| 1 Strong AND ≥2 Supporting | **Likely Pathogenic** |
| ≥3 Moderate | **Likely Pathogenic** |
| 2 Moderate AND ≥2 Supporting | **Likely Pathogenic** |
| 1 Moderate AND ≥4 Supporting | **Likely Pathogenic** |
| 1 Strong AND 2 Moderate | **Likely Pathogenic** |

### Benign Classification

| Combination | Classification |
|-------------|----------------|
| ≥2 Strong | **Benign** |
| 1 Stand Alone (BA1) | **Benign** |

### Likely Benign Classification

| Combination | Classification |
|-------------|----------------|
| 1 Strong (BS1, BS4) | **Likely Benign** |
| ≥2 Supporting (BS2_Supporting, BS3_Supporting, BP7) | **Likely Benign** |

### Variant of Uncertain Significance (VUS)

- Criteria for benign and pathogenic are contradictory
- No criteria met
- Criteria met do not reach threshold for Likely Benign or Likely Pathogenic

---

## 6. Appendices

### Appendix A: Key References

| Citation | PMID | Topic |
|----------|------|-------|
| Richards et al., 2015 | 25741868 | ACMG/AMP Variant Interpretation Guidelines |
| Tayoun et al., 2018 | 30192042 | ClinGen SVI PVS1 Recommendations |
| Arredondo-Vega et al., 1998 | 9758612 | ADA Enzyme Activity Groups |
| Dvorak et al., 2019 | 30193840 | PIDTC 6901 Cohort Data |
| Oza et al., 2018 | 30311386 | PP1 Segregation Recommendations |
| ClinGen SVI, 2018/2021 | - | De Novo Criteria (PS2/PM6) |
| ClinGen SVI, 2019/2025 | - | In Trans Criterion (PM3) |

### Appendix B: Validated Functional Assay Summary

| Assay Class | PMIDs | Strength Available |
|-------------|-------|-------------------|
| Expressed ADA Activity | 3182793, 9758612 | PS3_Supporting, PS3_Moderate, BS3_Supporting |

### Appendix C: Functional Evidence Validation Controls

| Variant | Protein Change | Classification | ADA Activity (% WT) | Interpretation |
|---------|---------------|----------------|---------------------|----------------|
| c.43C>G | p.His15Asp | Likely Pathogenic | <0.05 | Abnormal |
| c.221G>T | p.Gly74Val | Likely Pathogenic | <0.05 | Abnormal |
| c.301C>T | p.Arg101Trp | Likely Pathogenic | <0.05 | Abnormal |
| c.302G>A | p.Arg101Gln | Likely Pathogenic | <0.05 | Abnormal |
| c.302G>T | p.Arg101Leu | Likely Pathogenic | <0.05 | Abnormal |
| c.320T>C | p.Leu107Pro | Likely Pathogenic | <0.05 | Abnormal |
| c.425G>A | p.Arg142Gln | Benign | >4.8 | Normal |
| c.466C>T | p.Arg156Cys | Likely Pathogenic | <0.05 | Abnormal |
| c.632G>A | p.Arg211His | Pathogenic | <0.05 | Abnormal |
| c.646G>A | p.Gly216Arg | Likely Pathogenic | <0.05 | Abnormal |
| c.872C>T | p.Ser291Leu | Likely Pathogenic | <0.05 | Abnormal |

### Appendix D: SCID Diagnostic Criteria (PIDTC 2022)

The diagnostic criteria for SCID should follow the PIDTC 2022 specification. Key elements include:

- **Criterion 1:** Severely reduced T cells (autologous)
- **Criterion 3:** Evidence of impaired T cell function
- **Criterion 4:** Known SCID-causing genetic mutation

For Leaky SCID/Omenn syndrome, Criterion 2 (restricted T cell repertoire, oligoclonal T cells) is excluded from evaluation.

---

## Document History

| Version | Date | Changes |
|---------|------|---------|
| 2.1.0 | October 1, 2025 | Updated PM5 specifications; PP4 table updates; PP4 instructions harmonized; PM3 criterion table updates; Corrected Likely Benign rules (1 Strong, not 1 Strong + 1 Supporting) |

---

*This document is based on the ClinGen Severe Combined Immunodeficiency Disease Expert Panel Specifications to the ACMG/AMP Variant Interpretation Guidelines for ADA Version 2.1.0*
