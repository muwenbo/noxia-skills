# ClinGen Potassium Channel Arrhythmia Expert Panel Variant Interpretation Guidelines for KCNQ1

**Version:** 1.0.0
**Released:** 6/25/2025
**Affiliation:** Potassium Channel Arrhythmia VCEP
**Based on:** Tavtigian et al., 2020 - Bayesian adaptation of Richards et al., 2015

---

## Gene Information

| Attribute | Value |
|-----------|-------|
| **Gene** | KCNQ1 (HGNC:6294) |
| **HGNC Name** | potassium voltage-gated channel subfamily Q member 1 |
| **Transcript** | NM_000218.2 |
| **Disease** | long QT syndrome 1 (MONDO:0100316) |
| **Inheritance** | Autosomal dominant inheritance, Autosomal recessive inheritance |

### General Comments

Long QT syndrome 1 and Jervell and Lange-Nielsen syndrome are both caused by loss-of-function variants in KCNQ1. As a result, families with homozygous or compound heterozygous individuals affected with Jervell and Lange-Nielsen syndrome can also have heterozygous family members with long QT syndrome. It is important to note that not all disease-causing variants in KCNQ1 are highly penetrant in the heterozygous state, so it is common to see incomplete penetrance among heterozygous family members. For most KCNQ1 variant curations, a pathogenic or likely pathogenic classification is equally applicable to both inheritance patterns.

On the other hand, a number of hypomorphic KCNQ1 variants that cause Jervell and Lange-Nielsen syndrome (or QTc interval prolongation without hearing loss) in homozygosity or compound heterozygosity are not sufficient to cause long QT syndrome in the heterozygous state. For variants that fit this pattern, the VCEP adds a note to the evidence summary to clarify that the variant has only been observed to cause disease in the homozygous or compound heterozygous state.

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

#### Strength Levels

| Strength | Criteria | Point Value |
|----------|----------|-------------|
| **Very Strong** | For truncating variants affecting codons 1-581, since nonsense-mediated decay is predicted | 8 |
| **Moderate** | For truncating variants between codons 582-620, for which NMD is not predicted. This region includes the subunits assembly domain (SAD) between residues 589-620, which mediates tetramerization, so truncating variants that remove this region are reportedly unable to assemble and are disease-causing (PMID: 10654932) | 2 |
| **Supporting** | For truncating variants between codons 621-676, for which NMD is not predicted and the SAD is retained. These distal variants may still yield functional channels. Note: Although one variant with good evidence of pathogenicity has been found within this region (NM_000218.3(KCNQ1):c.1893del (p.Arg632fs)), it appears to exert a pathogenic effect through a dominant negative (mistrafficking) mechanism rather than true null mechanism (PMID: 22739119) | 1 |

#### PVS1 Decision Tree

```
NONSENSE OR FRAMESHIFT
├── Predicted to undergo NMD
│   ├── Exon present in biologically-relevant transcript(s) AND truncation between codons 1-581
│   │   └── PVS1 (Very Strong)
│   └── Exon absent from biologically-relevant transcript(s)
│       └── N/A
└── Not predicted to undergo NMD
    ├── Truncated/altered region is critical to protein function (codons 582-620)
    │   └── PVS1_Moderate
    ├── Role of region in protein function is unknown (codons 621-676)
    │   └── PVS1_Supporting
    └── LoF variants frequent in general population and/or exon absent from biologically-relevant transcript(s)
        └── N/A

SPLICE VARIANTS (GT-AG, +1/+2 splice sites)
├── Exon skipping or cryptic splice site disrupts reading frame AND predicted to undergo NMD
│   ├── Exon present in biologically-relevant transcript(s) AND truncation between codons 1-581
│   │   └── PVS1 (Very Strong)
│   └── Exon absent → N/A
├── Exon skipping or cryptic splice site disrupts reading frame AND NOT predicted to undergo NMD
│   ├── Truncated/altered region critical (codons 582-620) → PVS1_Moderate
│   ├── Role unknown (codons 621-676) → PVS1_Supporting
│   └── LoF variants frequent/exon absent → N/A
└── Exon skipping preserves reading frame
    ├── Variant removes >10% of protein
    │   ├── LoF variants NOT frequent AND exon present → PVS1_Strong
    │   └── LoF variants frequent/exon absent → N/A
    └── Variant removes <10% of protein
        ├── Truncated/altered region critical → PVS1_Moderate
        └── Role unknown → PVS1_Supporting

DELETIONS (Single exon to full gene)
├── Disrupts reading frame AND predicted to undergo NMD → PVS1
├── Disrupts reading frame AND NOT predicted to undergo NMD
│   ├── Variant removes >10% of protein
│   │   ├── LoF NOT frequent AND exon present → PVS1_Strong
│   │   └── LoF frequent/exon absent → N/A
│   └── Variant removes <10% of protein
│       ├── Truncated/altered region critical → PVS1_Moderate
│       └── Role unknown → PVS1_Supporting
├── Preserves reading frame
│   ├── Truncated/altered region critical → PVS1_Strong
│   └── Role unknown → PVS1_Moderate
└── Full gene deletion → PVS1

DUPLICATIONS (≥1 exon, completely contained within gene)
├── Proven in tandem
│   ├── Reading frame disrupted AND NMD predicted → PVS1
│   └── No/unknown impact on reading frame and NMD → N/A
└── Presumed in tandem
    ├── Reading frame presumed disrupted AND NMD predicted → PVS1_Strong
    └── No/unknown impact → N/A

INITIATION CODON
├── Different functional transcript uses alternative start codon → N/A
└── No known alternative start codon in other transcripts
    ├── ≥1 pathogenic variant(s) upstream of closest potential in-frame start codon → PVS1_Moderate
    └── No pathogenic variant(s) upstream → PVS1_Supporting
```

---

### PS1 - Same Amino Acid Change

**Original ACMG Summary:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.

**Caveat:** Beware of changes that impact splicing rather than at the amino acid/protein level.

#### Strength Levels

| Strength | Criteria | Point Value |
|----------|----------|-------------|
| **Strong** | Same amino acid change as a previously established pathogenic variant. The comparison variant must reach a **Pathogenic** classification using these rule specifications, without the use of PS1. SpliceAI must be used to ensure that the comparison variant is not causing a splicing defect. | 4 |
| **Moderate** | PS1 is met at PS1_Moderate level if the comparison variant reaches a **Likely Pathogenic** classification using these rule specifications, without PS1. **Paralogue-based:** This code can also be met when the corresponding variant in the paralogous KCNQ2 gene meets criteria for Pathogenic classification by the KCNQ Channel Brain Disorders VCEP specifications. The paralogous variant must substitute the same amino acid. Access paralogue data at: https://www.cardiodb.org/paralogue_annotation/gene.php?name=KCNQ1 | 2 |

**Note:** While the paralogue-based strategy has been approved for KCNQ2 only, this criterion may eventually apply to KCNQ3, KCNQ4, and KCNQ5 genes following future specifications by the KCNQ Channel Brain Disorders VCEP.

---

### PS2 - De Novo (Confirmed)

**Original ACMG Summary:** De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.

**Note:** Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.

#### VCEP Specifications

- Both maternity and paternity must be confirmed, with no family history of disease (no evidence of QT-prolongation in parents or family history of sudden, unexplained death under the age of 40 years)
- Cases and parents genotyped by trio whole exome sequencing are considered to have confirmed maternity and paternity
- The *de novo* variant must be coding or flanking
- Strength level depends on clinical phenotype specificity and number of probands

#### Table 1: Points Awarded per De Novo Occurrence

| Phenotypic Consistency | Confirmed de novo | Assumed de novo |
|------------------------|-------------------|-----------------|
| Phenotype highly specific for gene | 2 | 1 |
| Phenotype consistent with gene but not highly specific | 1 | 0.5 |
| Phenotype consistent with gene but not highly specific AND high genetic heterogeneity* | 0.5 | 0.25 |
| Phenotype not consistent with gene | 0 | 0 |

*Maximum allowable value of 1 may contribute to overall score

**Phenotype Guidance:**
- If proband has phenotype sufficient to diagnose LQTS (prolonged QTc interval >480ms), use row "phenotype consistent with gene but not highly specific"
- If proband meets PP4 (KCNQ1-specific LQTS / LQT1), use "phenotype highly specific for gene"
  - Requires: QTc prolongation >480ms AND (swimming-associated events OR treadmill stress test result (PMID: 21699858) OR T-wave morphology characteristic of LQT1 (PMID: 7586261, 29141844))

#### Table 2: Evidence Strength Thresholds for PS2/PM6

| Total Points | Strength Level | Point Value |
|--------------|----------------|-------------|
| 0.5 | PS2_Supporting or PM6_Supporting | 1 |
| 1.0 | PS2_Moderate or PM6 | 2 |
| 2.0 | PS2 or PM6_Strong | 4 |
| 4.0 | PS2_VeryStrong or PM6_VeryStrong | 8 |

---

### PS3 - Functional Studies

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.

**Note:** Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.

#### PS3 Strength Levels

| Strength | Point Value |
|----------|-------------|
| **Strong** | 4 |
| **Moderate** | 2 |
| **Supporting** | 1 |

#### Approved Functional Assays

**Electrophysiology and Experimental/Structural/Functional Simulation assays:**
1. Manual patch-clamp (PMIDs: 21380488, 30571187, 11162126, 19959132, 30591322, 17053194)
2. Automated patch-clamp (PMID: 30571187)
3. Microelectrode array analysis of hIPSC-cardiomyocytes (PMID: 35765105)
4. Experimental/Structural/Functional Simulation (PMIDs: 29021305, 35442947, 32096762)

**RNA or Protein Metabolism assays:**
5. Cell Surface Localization by Flow Cytometry (PMID: 29532034)
6. Mislocalization by Immunofluorescence of KCNQ1 (PMIDs: 21380488, 19114714, 11162126, 17053194) or KCNH2 (PMIDs: 19959132, 30591322)
7. Total Cell Expression by Flow Cytometry (PMID: 29532034)
8. Western Blotting (PMIDs: 21380488, 19114714)
9. RNA Metabolism showing partial/incomplete disruption of splicing (PMIDs: 17292394, 28264985)

#### PS3/BS3 Caveats

1. **Conflicting evidence** from different papers = no points
2. **Same types of evidence** (e.g., RNA and Protein Metabolism) from the same paper = count 1
3. **No more than 2 pieces of evidence** can be counted from the same paper
4. **Same finding in 2 papers** from the same group = count 1
5. **Electrophysiology requirement:** Result can only meet PS3 if the variant is co-expressed with KCNE1 AND the current magnitude is outside the normal range defined by the paper AND is statistically significantly different from the normal control
6. **Experimental/Structural/Functional Simulation** (PMID: 29021305): Only count when results align with an electrophysiology experiment

#### PS3/BS3 Strength Overview Table

| Evidence Type | Points per Instance |
|---------------|---------------------|
| Electrophysiology (patch-clamp, MEA) | Variable based on paper |
| Experimental/Structural/Functional Simulation | Only counted with EP support |
| Cell Surface Localization (Flow Cytometry) | Variable |
| Mislocalization (Immunofluorescence) | Variable |
| Total Cell Expression (Flow Cytometry) | Variable |
| Western Blotting | Variable |
| RNA Metabolism | Variable |

**Strength Determination:**
- **PS3_Supporting (1 point):** 1 piece of evidence
- **PS3_Moderate (2 points):** 2 pieces of evidence
- **PS3 (Strong, 4 points):** Multiple pieces of evidence from different categories

---

### PS4 - Prevalence in Affected

**Original ACMG Summary:** The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.

#### VCEP Specifications

- Variant must **not meet BS1** to be evaluated for this criterion
- Patients must have **QTc measurement ≥460ms** to be counted (diagnosis of LQTS alone is not sufficient)
- This code is **not mutually exclusive with PM3** (variants can meet both for dominant and recessive cases)
- If probands are reported in ≥2 papers with any overlapping authors, count only one case
- If author lists are completely different, count both cases

#### Strength Levels

| Strength | Number of Probands | Point Value |
|----------|-------------------|-------------|
| **Strong** | ≥6 probands | 4 |
| **Moderate** | 3-5 probands | 2 |
| **Supporting** | 2 independent observations | 1 |

---

### PM1 - Mutational Hot Spot

**Original ACMG Summary:** Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.

#### VCEP Specification

| Strength | Criteria | Point Value |
|----------|----------|-------------|
| **Moderate** | Rare variant within the **pore helix (amino acids 300-320)**. This region is known to be a critical region of KCNQ1 and has been confirmed to show an absence of likely benign or benign variants in gnomAD. Variant must meet PM2_Supporting to be considered. | 2 |

---

### PM2 - Absent from Controls

**Original ACMG Summary:** Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

**Caveat:** Population data for indels may be poorly called by next generation sequencing.

#### VCEP Specification (Supporting Level Only)

| Strength | Threshold | Point Value |
|----------|-----------|-------------|
| **Supporting** | Maximum allele frequency in gnomAD (in one of the 5 continental populations: African/African-American, East Asian, European non-Finnish, Latino/Admixed-American, or South Asian) **<0.00001 (0.001%)** | 1 |

---

### PM3 - In Trans with Pathogenic

**Original ACMG Summary:** For recessive disorders, detected in trans with a pathogenic variant.

**Note:** This requires testing of parents (or offspring) to determine phase.

#### VCEP Specifications

- Can be used for variants seen in patients with **Jervell and Lange-Nielsen syndrome**, if phenotype includes both long QT interval and congenital deafness
- **Not mutually exclusive with PS4** (variants can meet both for recessive and dominant cases)
- Use ClinGen SVI recommendations to determine evidence weight
- **Both variants must be classified** using these rule specifications

#### Table 1: Points Awarded per In Trans Occurrence

| Classification/Zygosity of Other Variant | Confirmed in Trans | Phase Unknown |
|------------------------------------------|-------------------|---------------|
| Pathogenic or Likely pathogenic variant | 1.0 | 0.5 (P) / 0.25 (LP) |
| Homozygous occurrence (max 1.0 point) | 0.5 | N/A |
| Uncertain significance variant on other allele (max 0.5 total) | 0.25 | 0.0 |

*All variants should be sufficiently rare (meet PM2 specification)

#### Table 2: PM3 Evidence Strength Thresholds

| Total Points | Strength Level | Point Value |
|--------------|----------------|-------------|
| 0.5 | PM3_Supporting | 1 |
| 1.0 | PM3 (Moderate) | 2 |
| 2.0 | PM3_Strong | 4 |
| 4.0 | PM3_VeryStrong | 8 |

---

### PM4 - Protein Length Changes

**Original ACMG Summary:** Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

#### VCEP Specification

| Strength | Criteria | Point Value |
|----------|----------|-------------|
| **Moderate** | In-frame insertions or deletions of any size meet PM4 at moderate (default) level, due to the greater importance of the location of the variant rather than the size. | 2 |

**Mutual Exclusivity:**
- This code is **mutually exclusive with PVS1** (PMID: 30192042)
- This code is **mutually exclusive with PP3** (to avoid double-counting in silico predictor data)
- This code **can be used together with PM1**

---

### PM5 - Novel Missense at Same Residue

**Original ACMG Summary:** Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.

**Caveat:** Beware of changes that impact splicing rather than at the amino acid/protein level.

#### VCEP Specification

| Strength | Criteria | Point Value |
|----------|----------|-------------|
| **Moderate** | Novel missense change at a highly conserved residue where a different P/LP missense has been seen. **Not used at PM5_Strong level.** | 2 |

**Requirements:**
- Residue must be **highly conserved across all 5 human KCNQ paralogues** (KCNQ1-5)
- Access paralogue data at: https://www.cardiodb.org/paralogue_annotation/gene.php?name=KCNQ1
- **Poor conservation** = 1 or more KCNQs show a different amino acid at the position (ineligible for PM5)
- Comparison variants must be P/LP **without using PM5**
- Variants at any codon where a B/LB variant has been classified are **not eligible**
- **SpliceAI** must be used to examine both variants for similar predicted effect or lack of effect on splicing (SpliceAI Δ score <0.2)

---

### PM6 - De Novo (Assumed)

**Original ACMG Summary:** Assumed de novo, but without confirmation of paternity and maternity.

#### VCEP Specifications

- Maternity and paternity are **not confirmed but assumed**, with no family history of disease
- The *de novo* variant must be coding or flanking
- Use the same point-based system as PS2 (see Tables 1 and 2 under PS2)

| Strength | Point Value |
|----------|-------------|
| **Very Strong** (4 points) | 8 |
| **Strong** (2 points) | 4 |
| **Moderate** (1 point) | 2 |
| **Supporting** (0.5 points) | 1 |

---

### PP1 - Co-segregation

**Original ACMG Summary:** Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.

**Note:** May be used as stronger evidence with increasing segregation data.

#### VCEP Specifications

- Each affected family member must have **Schwartz score (PMID: 36017572, Table 10) >3** OR **QTc ≥480ms** OR **syncope** to be counted
- If any family member is affected but does not harbor the variant, use **BS4 (non-segregation)** instead
- Numbers informed by PMID: 27236918

#### Strength Levels

| Strength | Criteria | Point Value |
|----------|----------|-------------|
| **Strong** | Proband + **7 affected family members** with the variant | 4 |
| **Moderate** | Proband + **5 affected family members** with the variant | 2 |
| **Supporting** | Proband + **3 affected family members** with the variant | 1 |

---

### PP2 - Missense in Constrained Gene

**Original ACMG Summary:** Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.

#### VCEP Specification

| Status | Comment |
|--------|---------|
| **Not Applicable** | Not applicable due to presence of benign variation throughout the KCNQ1 gene (missense constraint Z-score in gnomAD is 1.83, lower than 3) |

---

### PP3 - Computational Evidence

**Original ACMG Summary:** Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).

**Caveat:** As many in silico algorithms use the same or very similar input, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.

#### VCEP Specification (Supporting)

| Strength | Criteria | Point Value |
|----------|----------|-------------|
| **Supporting** | **REVEL and SpliceAI** are the preferred predictors. Apply this code if: | 1 |

**For Missense Variants:**
- REVEL score **≥0.75**

**For Splicing Assessment:**
- SpliceAI delta score for donor gain, donor loss, acceptor gain, or acceptor loss **≥0.2** (PMID: 37352859)

---

### PP4 - Phenotype Specificity

**Original ACMG Summary:** Patient's phenotype or family history is highly specific for a disease with a single genetic etiology.

#### VCEP Specification (Supporting)

| Strength | Criteria | Point Value |
|----------|----------|-------------|
| **Supporting** | QT prolongation **>480ms** AND at least one of: | 1 |

- Swimming-associated events, OR
- Treadmill stress test result (PMID: 21699858), OR
- T-wave morphology characteristic of LQT1 (PMID: 7586261, 29141844)

---

### PP5 - Reputable Source

**Original ACMG Summary:** Reputable source recently reports variant as pathogenic, but the evidence is not available to the laboratory to perform an independent evaluation.

| Status | Comment |
|--------|---------|
| **Not Applicable** | This criterion is not for use as recommended by the ClinGen SVI VCEP Review Committee (PMID: 29543229) |

---

## Benign Criteria

### BA1 - Allele Frequency >5%

**Original ACMG Summary:** Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

#### VCEP Specification (Stand Alone)

| Threshold | Comment |
|-----------|---------|
| Maximum allele frequency in gnomAD (in one of the 5 continental populations: African/African-American, East Asian, European non-Finnish, Latino/Admixed-American, or South Asian) **≥0.004 (0.4%)** | Stand Alone - variant classified as Benign |

---

### BS1 - Frequency Greater Than Expected

**Original ACMG Summary:** Allele frequency is greater than expected for disorder.

#### VCEP Specification (Strong)

| Strength | Threshold | Point Value |
|----------|-----------|-------------|
| **Strong** | Maximum allele frequency in gnomAD (in one of the 5 continental populations) **≥0.0004 (0.04%)** | -4 |

---

### BS2 - Observed in Healthy Adult

**Original ACMG Summary:** Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

#### VCEP Specification

| Status | Comment |
|--------|---------|
| **Not Applicable** | Not applicable due to incomplete penetrance. Please note that hearing loss and other phenotypes are not completely penetrant in homozygotes (PMID: 23392653) |

---

### BS3 - Functional Studies (No Effect)

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

#### BS3 Strength Levels

| Strength | Point Value |
|----------|-------------|
| **Strong** | -4 |
| **Moderate** | -2 |
| **Supporting** | -1 |

#### Approved Assays and Caveats

Same as PS3 (see above), with the following key difference:

**Electrophysiology requirement:** Result can only meet BS3 if the variant is co-expressed with KCNE1 AND the variant current magnitude is **within the normal range** defined by the paper AND is **NOT statistically significantly different** from the normal control.

---

### BS4 - Lack of Segregation

**Original ACMG Summary:** Lack of segregation in affected members of a family.

**Caveat:** The presence of phenocopies for common phenotypes can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder.

#### VCEP Specifications

- Family member must have **QTc ≥480ms** OR **Schwartz score >3** OR **syncope**
- Use European Society of Cardiology guidelines for 2022 (PMID: 36017572, Table 10) to calculate modified Schwartz score

#### Strength Levels

| Strength | Criteria | Point Value |
|----------|----------|-------------|
| **Strong** | Absence of variant in **≥2 affected family members** | -4 |
| **Supporting** | Absence of variant in **1 affected family member** | -1 |

---

### BP1-BP7 - Benign Supporting

| Criterion | Status | Comment | Point Value |
|-----------|--------|---------|-------------|
| **BP1** | Not Applicable | Pathogenic KCNQ1 variants are not limited to truncating variants but can be missense as well | -1 |
| **BP2** | Not Applicable | Not applicable to KCNQ1 due to biallelic cases (Jervell and Lange-Nielsen syndrome) | -1 |
| **BP3** | Not Applicable | Not applicable to KCNQ1 | -1 |
| **BP4** | Applicable | REVEL and SpliceAI are preferred. Apply if: **Missense:** REVEL <0.25 AND SpliceAI Δ <0.1. **Synonymous/Intronic:** SpliceAI Δ <0.1 (PMID: 37352859) | -1 |
| **BP5** | Applicable | Variant found in case with alternate molecular basis. **Caveat:** Not applicable when phenotypes (trigger type, treadmill stress test) indicate KCNQ1 as cause. Only applicable when phenotypes match another form of LQTS (KCNH2, SCN5A, KCNE1) or when phenotype details are not sufficiently specific | -1 |
| **BP6** | Not Applicable | Not for use as recommended by ClinGen SVI VCEP Review Committee (PMID: 29543229) | N/A |
| **BP7** | Applicable | Synonymous or intronic variant with SpliceAI Δ <0.1 AND PhyloP score <2.0. **Exclusions:** Variants in last 3 nucleotides of exon, 1st nucleotide of exon, or positions +1 to +6 or -1 to -20 (PMID: 37352859) | -1 |

---

## Rules for Combining Criteria

The Potassium Channel Arrhythmia VCEP recommends using the **point system** for rule code combining, as proposed by Tavtigian et al., 2020 (PMID: 32720330), rather than the rule combination system described in the original 2015 Variant Curation Guidelines.

**Note:** The ranges for Uncertain and Likely Benign have been modified to classify variants with -1 total points as VUS rather than Likely Benign.

### Point-Based Classification Categories

| Classification | Point Range |
|----------------|-------------|
| **Pathogenic** | ≥10 |
| **Likely Pathogenic** | 6 to 9 |
| **Uncertain Significance (VUS)** | 0 to 5 |
| **Likely Benign** | -6 to -1 |
| **Benign** | ≤-7 |

### Default Point Values Summary

| Criterion | Very Strong | Strong | Moderate | Supporting |
|-----------|-------------|--------|----------|------------|
| **Pathogenic Evidence** | 8 | 4 | 2 | 1 |
| **Benign Evidence** | N/A | -4 | -2 | -1 |

---

## Appendices

### Appendix A: Population Frequency Thresholds Summary

| Criterion | Threshold | Strength | Evidence Direction |
|-----------|-----------|----------|-------------------|
| BA1 | ≥0.004 (0.4%) | Stand Alone | Benign |
| BS1 | ≥0.0004 (0.04%) | Strong | Benign |
| PM2 | <0.00001 (0.001%) | Supporting | Pathogenic |

### Appendix B: Critical Protein Regions

| Region | Amino Acid Range | Clinical Significance |
|--------|------------------|----------------------|
| NMD-predicted region | Codons 1-581 | PVS1 (Very Strong) |
| Subunits Assembly Domain (SAD) | Residues 589-620 | PVS1_Moderate |
| Distal region (function unknown) | Codons 621-676 | PVS1_Supporting |
| Pore helix (critical region) | Amino acids 300-320 | PM1 applicable |

### Appendix C: Approved Functional Studies Reference PMIDs

| PMID | Assay Types |
|------|-------------|
| 21380488 | Manual patch-clamp, Immunofluorescence, Western Blotting |
| 30571187 | Automated patch-clamp, Manual patch-clamp |
| 29532034 | Cell Surface Localization (Flow Cytometry), Total Cell Expression |
| 19114714 | Western Blotting, Immunofluorescence |
| 11162126 | Manual patch-clamp, Immunofluorescence |
| 19959132 | Manual patch-clamp, KCNH2 Immunofluorescence |
| 30591322 | Manual patch-clamp, KCNH2 Immunofluorescence |
| 17053194 | Immunofluorescence, Manual patch-clamp |
| 29021305 | Experimental/Structural/Functional Simulation |
| 35442947 | Experimental/Structural/Functional Simulation |
| 32096762 | Experimental/Structural/Functional Simulation |
| 35765105 | Microelectrode array analysis (hIPSC-cardiomyocytes) |
| 17292394 | RNA Metabolism |
| 28264985 | RNA Metabolism |

### Appendix D: In Silico Predictor Thresholds

| Predictor | Pathogenic Threshold | Benign Threshold |
|-----------|---------------------|------------------|
| REVEL | ≥0.75 (PP3) | <0.25 (BP4) |
| SpliceAI Δ (any of 4 scores) | ≥0.2 (PP3) | <0.1 (BP4/BP7) |
| PhyloP | N/A | <2.0 (BP7) |

### Appendix E: Phenotype Assessment for LQT1

**KCNQ1-specific phenotype (PP4):**
- QTc >480ms AND at least one of:
  - Swimming-associated events (PMIDs: 32882399, 11136691, 18373596)
  - Treadmill stress test result (PMID: 21699858)
  - T-wave morphology characteristic of LQT1 (PMIDs: 7586261, 29141844)

**General LQTS phenotype:**
- QTc ≥460ms for PS4 proband counting
- QTc ≥480ms for PP1 family member counting

**Schwartz Score:**
- Use European Society of Cardiology guidelines 2022 (PMID: 36017572, Table 10)
- Score >3 indicates affected status for PP1/BS4

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 6/25/2025 | Initial release |

---

*This document was compiled from ClinGen Potassium Channel Arrhythmia VCEP specifications. For the most current version, please refer to the ClinGen website.*

*Document generated based on ClinGen VCEP specifications and ClinGen SVI recommendations.*
