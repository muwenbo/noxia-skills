# ClinGen Leber Congenital Amaurosis/early onset Retinal Dystrophy VCEP Variant Interpretation Guidelines for GUCY2D

**Version:** 1.0.0
**Released:** 1/22/2025
**Affiliation:** Leber Congenital Amaurosis/early onset Retinal Dystrophy VCEP
**Based on:** Richards et al., 2015 ACMG/AMP Guidelines

---

## Gene Information

| Attribute | Value |
|-----------|-------|
| **Gene** | GUCY2D (HGNC:4689) |
| **HGNC Name** | guanylate cyclase 2D, retinal |
| **Transcript** | NM_000180.4 / NP_000171.1 |
| **Disease** | GUCY2D-related recessive retinopathy (MONDO:0100453) |
| **Inheritance** | Autosomal recessive |

**General Comments:** The GUCY2D gene encodes a retina-specific guanylate cyclase, which is a member of the membrane guanylyl cyclase family. Aliases for the protein (NP_000171.1) include RetGC-1, RETGC-1, ROS-GC, ROS-GC1, RetGC, and CG-E.

**Important Note:** The point system of Tavtigian et al. (PMID 32720330) is being used for all classifications, so the standard combining rules are not being utilized.

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
3. [Point-Based Classification System](#point-based-classification-system)
4. [Rules for Combining Criteria](#rules-for-combining-criteria)
5. [Appendices](#appendices)

---

## Pathogenic Criteria

### PVS1 - Null Variant

**Original ACMG Summary:** Null variant (nonsense, frameshift, canonical +/-1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.

**Caveats:**
- Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7)
- Use caution interpreting LOF variants at the extreme 3' end of a gene
- Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact
- Use caution in the presence of multiple transcripts

**VCEP Specifications:** See GUCY2D-specific PVS1 Decision Tree (Appendix A), modified from Walker et al., 2023.

#### Strength Levels

| Strength | Criteria |
|----------|----------|
| **Very Strong (PVS1)** | - Predicted splice defects at +/- 1,2 in exons 2-20<br>- Single to multi-exon deletions, with or without predicted NMD (all exons considered critical)<br>- Variants in the initiation codon (Met1) - second in-frame methionine at residue 218 would eliminate leader sequence<br>- Nonsense or frameshift mutations from p.Thr2 through p.Lys1068<br>- Duplications of exons proven in tandem<br>- PVS1(RNA): RNA splicing data with evidence of alternative transcript production at complete levels |
| **Strong (PVS1_Strong)** | - Nonsense or frameshift mutations from p.Pro1069 through p.Ser1103<br>- Duplications of exons presumed in tandem<br>- PVS1(RNA)_Strong: RNA splicing data with evidence of alternative transcript production at near complete levels |

**Modification Type:** Gene-specific

---

### PS1 - Same Amino Acid Change

**Original ACMG Summary:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.
- Example: Val->Leu caused by either G>C or G>T in the same codon
- Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level

**VCEP Specifications:**
- For assessing same amino acid changes, SpliceAI must be used to ensure comparison variant is not causing a splicing defect (score ≤0.1)
- GUCY2D-specific PVS1 Decision Tree for scoring splicing variants is based on Walker et al. 2023

#### Strength Levels

| Strength | Criteria |
|----------|----------|
| **Strong (PS1)** | Same amino acid change as a previously established **Pathogenic** variant. Must have one comparison variant that reaches a Pathogenic classification using this rule specification. For splice variants: used in conjunction with PP3 for variants outside +/-1,2 positions with SpliceAI ≥0.2 and comparable Pathogenic variant at same position, OR with PVS1 for variants at +/-1,2 positions with comparable Pathogenic variant. |
| **Moderate (PS1_Moderate)** | Same amino acid change as a previously established **Likely Pathogenic** variant. For splice variants: used in conjunction with PP3/PVS1_reduced with comparable Likely Pathogenic or Pathogenic variants within same motif but outside +/-1,2 dinucleotide. |
| **Supporting (PS1_Supporting)** | For variants outside +/-1,2 positions with SpliceAI ≥0.2 and comparable Likely Pathogenic variant within the same motif. For variants at +/-1,2 positions with comparable LP/P variant within same splice site donor/acceptor motif. |

**Modification Type:** Gene-specific, Strength

---

### PS2 - De Novo (Confirmed)

**Original ACMG Summary:** De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.
- Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.

**VCEP Specifications:**
- Use point table from SVI Recommendation for De Novo Criteria (PS2 & PM6) - Version 1.1
- **Individuals must have 2 variants to consider scoring one for de novo**
- For "Phenotypic consistency" category, consider whether the proband meets PP4:
  - Does not meet PP4 → use option 3: "Phenotype consistent with gene but not highly specific and high genetic heterogeneity"
  - Meets PP4 at Supporting level → use option 2: "Phenotype consistent with gene but not highly specific"
  - Meets PP4 at Moderate level → use option 1: "Phenotype highly consistent for gene"

**Required Phenotype Characteristics for all probands:**
- Absent or severely decreased rod electroretinogram response, **OR**
- Congenital night blindness/nyctalopia, **OR**
- Diagnosis of Leber congenital amaurosis/eoRD/cone-rod dystrophy

#### PS2/PM6 Point System (Per Proband)

| Phenotypic Consistency | Confirmed Parental Relationships | Unconfirmed |
|------------------------|----------------------------------|-------------|
| Phenotype highly specific for gene | 2 points | 1 point |
| Phenotype consistent but not highly specific | 1 point | 0.5 points |
| Phenotype consistent + high genetic heterogeneity | 0.5 points | 0.25 points |
| Phenotype not consistent | 0 points | 0 points |

#### Evidence Strength Thresholds

| Points | Strength Level |
|--------|----------------|
| 0.50 - 0.75 | Supporting |
| 1.00 - 1.75 | Moderate |
| 2.00 - 3.75 | Strong |
| ≥4.00 | Very Strong |

**Modification Type:** Gene-specific

---

### PS3 - Functional Studies

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.
- Note: Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.

**VCEP Specifications:** See attached table of approved functional studies.

#### Strength Levels

| Strength | Criteria |
|----------|----------|
| **Strong (PS3)** | Gucy2e−/−Gucy2f−/− knockout mice subretinally injected with AAV-packaged constructs encoding a GUCY2D variant (Boye et al., 2016) or mice with knock-in of a GUCY2D variant. Results should include: flat or nearly flat scotopic and photopic ERG responses vs. wild-type control, absent or near-absent guanylate cyclase activity vs. wild-type control, and/or absent or near-absent GUCY2D expression at protein level despite approximately wild-type RNA expression. |
| **Supporting (PS3_Supporting)** | Well-established in vitro or in vivo functional studies supportive of a damaging effect. Not applicable for splicing effects (replaced by PVS1_Strength (RNA)). For studies reporting guanylate cyclase activity, cutoff is **≤10%** of wild-type control. |

#### Approved Functional Assays

| PMID | Evidence Type | Description |
|------|---------------|-------------|
| 33109612 | Peshenko et al., 2020 | GCAP1/RD3 failure to localize to cell surface; GC activity with GCAP1/2/3 |
| 32255808 | Feng et al., 2020 | GC activity in absence of GCAP1/2/3 |
| 33997691 | Jacobson et al., 2021 | GC activity in presence of GCAP1 |
| 36274938 | Jacobson et al., 2022 | GC activity with GCAP1/2/3; GCAP1 localization |
| 15123990 | Tucker et al., 2004 | GC activity +/- GCAP1 or GCAP2 |
| 23035049 | Jacobson et al., 2013 | GC activity with GCAP1 or GCAP2 |
| 25477517 | Zulliger et al., 2015 | GCAP1/RD3/GUCY2D localization; RD3 binding |
| 26100624 | Peshenko et al., 2015 | GCAP1/2 and RD3 co-localization with GUCY2D |
| 9600905 | Tucker et al., 1998 | GC activity (conversion to adenylyl cyclase) |
| 9888789 | Duda et al., 1999 | GC activity |
| 27881908 | Boye et al., 2016 | In vivo mouse model with AAV delivery |
| 30319355 | Wimberg et al., 2018 | Ca2+-dependent cGMP synthesis |
| 24616660 | Zägel et al., 2014 | GC dysfunction |
| 21463603 | Duda et al., 2011 | Phototransduction switch motif |
| 20050595 | Peshenko et al., 2010 | RetGC1 activation by GCAP1 |
| 36084042 | Daich Varela et al., 2023 | Non-coding variant analysis |

**Modification Type:** Gene-specific, Strength

---

### PS4 - Prevalence in Affected

**Original ACMG Summary:** The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.

**VCEP Specification:** **Not Applicable** for GUCY2D.

---

### PM1 - Mutational Hot Spot

**Original ACMG Summary:** Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.

**VCEP Specifications:**
- These sites have been identified based on well-established functional domains rather than based on a known cluster of pathogenic or likely pathogenic variants
- This criterion is **not mutually exclusive** with PM5
- Missense variants that meet BS1 or BA1 should not be eligible to meet this criterion
- Missense variants at a position where another benign missense variant is identified should not be eligible

#### Strength Levels

| Strength | Criteria |
|----------|----------|
| **Moderate (PM1)** | Active site residues that bind the GTP substrate or the Mg²⁺ ion: **Phe883, Asp885, Thr890, Leu905, Glu925, Ile927, Asp929, Met932, Arg976, Arg995, Cys997, Leu998, Phe999, Gly1000, Val1003, Asn1004, Arg1008, and Glu1010** |
| **Supporting (PM1_Supporting)** | Variants not explicitly listed above encoding missense substitutions between positions **p.873-951** (part of guanylate cyclase catalytic domain with intolerance to missense variation). Also, variants in the 6 bp CRX binding site at position 17:8002593-8002598 (hg38). |

**Modification Type:** Gene-specific

---

### PM2 - Absent from Controls

**Original ACMG Summary:** Absent from controls (or at extremely low frequency if recessive) in population databases.
- Caveat: Population data for indels may be poorly called by next generation sequencing.

**VCEP Specifications:**
- Cutoff value of 4.0x10⁻⁴ is set just above the FAF of the most common pathogenic GUCY2D variant (3.6x10⁻⁴) and below the Whiffin-Ware calculation of 1.6x10⁻³ for the maximum credible population allele frequency
- This rule should not be applied if variant would otherwise meet criteria for a benign classification

#### Strength Level

| Strength | Criteria |
|----------|----------|
| **Supporting (PM2_Supporting)** | gnomAD total allele frequency **≤ 4.0 x 10⁻⁴** |

**Modification Type:** Disease-specific, Strength

---

### PM3 - In Trans with Pathogenic

**Original ACMG Summary:** For recessive disorders, detected in trans with a pathogenic variant.
- Note: This requires testing of parents (or offspring) to determine phase.

**VCEP Specifications:**
- Use SVI recommendations for PM3 criterion
- **Both variants must be classified using these rule specifications**
- All probands must have required phenotype characteristics (see PS2)

#### PM3 Point System (Per Proband)

| Classification/Zygosity of Other Variant | Confirmed in Trans | Phase Unknown |
|------------------------------------------|-------------------|---------------|
| Pathogenic or Likely pathogenic variant | 1.0 | 0.5 (P) / 0.25 (LP) |
| Homozygous occurrence (max point 1.0) | 0.5 | N/A |
| Uncertain significance variant on other allele (max point 0.5) | 0.25 | 0.0 |

#### PM3 Evidence Strength Thresholds

| Total Points | Strength Level |
|--------------|----------------|
| 0.5 - 0.75 | PM3_Supporting |
| 1.0 - 1.75 | PM3 (Moderate) |
| 2.0 - 3.75 | PM3_Strong |
| ≥4.0 | PM3_VeryStrong |

**Modification Type:** Disease-specific

---

### PM4 - Protein Length Changes

**Original ACMG Summary:** Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

#### Strength Levels

| Strength | Criteria |
|----------|----------|
| **Moderate (PM4)** | Protein length change of **≥2 amino acids** that leads to loss of at least one conserved residue (PhyloP>2.0) or insertion of new amino acids adjacent to at least one conserved residue (PhyloP>2.0) |
| **Supporting (PM4_Supporting)** | Protein length change of **1 amino acid** that leads to loss of at least one conserved residue (PhyloP>2.0) or insertion of new amino acid adjacent to at least one conserved residue (PhyloP>2.0) |

**Modification Type:** Gene-specific, Strength

---

### PM5 - Novel Missense at Same Residue

**Original ACMG Summary:** Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.
- Example: Arg156His is pathogenic; now you observe Arg156Cys
- Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level

#### Strength Levels

| Strength | Criteria |
|----------|----------|
| **Moderate (PM5)** | Missense change at residue where different Pathogenic missense exists. Must have comparison variant reaching Pathogenic using this rule specification. SpliceAI scores for both variants should be in the same category (<0.1, 0.1-0.2, >0.2). |
| **Supporting (PM5_Supporting)** | Missense change at residue where different Likely Pathogenic missense exists. Must have comparison variant reaching Likely Pathogenic using this rule specification. SpliceAI scores in same category. |

**Modification Type:** Strength (Supporting level)

---

### PM6 - De Novo (Assumed)

**Original ACMG Summary:** Assumed de novo, but without confirmation of paternity and maternity.

**VCEP Specification:** **Not Applicable** - Use the PS2 code in lieu of using this code for de novo variants.

---

### PP1 - Co-segregation

**Original ACMG Summary:** Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.
- Note: May be used as stronger evidence with increasing segregation data.

**VCEP Specifications:**
- For moderate and strong codes, segregations can be added across multiple families, with each having a proband + at least one affected relative
- All probands must have required phenotype characteristics (see PS2)

#### Strength Levels

| Strength | Criteria |
|----------|----------|
| **Strong (PP1_Strong)** | Co-segregation with evidence that this variant and another GUCY2D variant are in trans. Requires segregation in one proband plus **≥3** similarly affected relatives. |
| **Moderate (PP1_Moderate)** | Co-segregation with evidence that this variant and another GUCY2D variant are in trans. Requires segregation in one proband plus **2** similarly affected relatives. |
| **Supporting (PP1)** | Co-segregation with evidence that this variant and another GUCY2D variant are in trans. Requires segregation in one proband plus **1** similarly affected relative. |

**Modification Type:** Disease-specific, Strength

---

### PP2 - Missense in Constrained Gene

**Original ACMG Summary:** Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.

**VCEP Specification:** **Not Applicable** for GUCY2D.

---

### PP3 - Computational Evidence

**Original ACMG Summary:** Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).
- Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.

**VCEP Specifications:**
- PP3 should **not** be used to evaluate variants at canonical splice sites (apply PVS1(splicing) instead)
- For non-canonical sites, if SpliceAI score is ≥0.2, apply PP3 (splicing)
- Score ranges are based on SVI Working Group publication "Calibration of computational tools for missense variant pathogenicity classification and ClinGen recommendations for PP3/BP4 criteria"

#### Strength Levels

| Strength | Criteria |
|----------|----------|
| **Moderate (PP3_Moderate)** | For missense variants: REVEL score **≥ 0.774**. Splice variants use PP3 only at Supporting level. |
| **Supporting (PP3)** | For missense variants: REVEL score **0.644 - 0.773**. For UTR variants: CADD score **≥ 20.0**. For predicted splicing variants: SpliceAI highest delta score **≥ 0.2** (max distance 500 bp). |

**Modification Type:** Gene-specific, Strength

---

### PP4 - Phenotype Specificity

**Original ACMG Summary:** Patient's phenotype or family history is highly specific for a disease with a single genetic etiology.

**VCEP Specifications:**
- A point system was developed to determine when there is enough information about a proband's phenotype
- This code can be used for a single proband
- **A proband must have two GUCY2D variants to consider applying PP4** (phase is not considered)
- **Caveat:** PP4 should not be applied if variant meets either BA1 or BS1

#### Required for use of PP4 (0.5 points each - must have at least one)
- Absent or severely decreased rod electroretinogram (ERG) responses, **OR**
- Congenital night blindness/nyctalopia, **OR**
- Clinical diagnosis of Leber congenital amaurosis or eoRD or cone-rod dystrophy

#### Specific GUCY2D Phenotype Findings

| Finding | Points |
|---------|--------|
| Previous gene panel testing without alternative explanation | 2 pts |
| Previous exome or genome NGS without alternative explanation | 4 pts |
| Gene therapy trial with strict inclusion criteria and positive results (details not reported) | 2 pts |
| Gene therapy trial with documented "Significant" improvement of FST or other dark-adapted vision measure | 8 pts |

#### Consistent with GUCY2D Phenotype Findings (0.5 or 1 point each)

| Finding | Points |
|---------|--------|
| Optic nerve pallor | 0.5 |
| Attenuated vessels in context of relatively normal fundus | 0.5 |
| Poor pupillary light response | 0.5 |
| RPE mottling | 0.5 |
| Symptomatic onset between birth and age five years | 1 |
| Normal retinal structure (by OCT) preserved with respect to vision loss | 1 |
| Decreased peripheral vision | 1 |
| Abnormal color vision or evidence of cone involvement on ERG | 1 |
| Decreased central visual acuity | 1 |
| Nystagmus | 1 |
| Photophobia | 1 |

#### PP4 Strength Thresholds

| Total Points | Strength |
|--------------|----------|
| <4 | PP4 not met |
| 4 - 7.5 | PP4 (Supporting) |
| ≥8 | PP4_Moderate |

**Note:** For PP4_Moderate, at least one **specific** criterion must also be met. Do not include a proband with a suspected diagnosis of more than one retinal dystrophy.

**Modification Type:** Disease-specific, Strength

---

### PP5 - Reputable Source

**Original ACMG Summary:** Reputable source recently reports variant as pathogenic, but the evidence is not available to the laboratory to perform an independent evaluation.

**VCEP Specification:** **Not Applicable** - This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PMID: 29543229).

---

## Benign Criteria

### BA1 - Allele Frequency >5%

**Original ACMG Summary:** Allele frequency is above 5% in population databases.

**VCEP Specifications:** The BA1 value was derived by increasing the BS1 lower cutoff (>0.0016) by one order of magnitude.

#### Strength Level

| Strength | Criteria |
|----------|----------|
| **Stand Alone (BA1)** | gnomAD Grpmax FAF **>0.016** (>1.6%) |

**Modification Type:** Disease-specific

---

### BS1 - Frequency Greater Than Expected

**Original ACMG Summary:** Allele frequency is greater than expected for disorder.

**VCEP Specifications:** The maximum credible population allele frequency for the disease, based on the Whiffin-Ware calculator, is 1.6 x 10⁻³. This assumes:
- Population frequency: 1 in 2000 individuals
- Genetic heterogeneity: 20%
- Penetrance: 100%
- Allele heterogeneity: 1

#### Strength Level

| Strength | Criteria |
|----------|----------|
| **Strong (BS1)** | gnomAD Grpmax FAF **0.0016 - 0.016** |

**Modification Type:** Disease-specific

---

### BS2 - Observed in Healthy Adult

**Original ACMG Summary:** Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

#### Strength Levels

| Strength | Criteria |
|----------|----------|
| **Strong (BS2)** | Variant is present in **≥3 homozygotes** without any features of the phenotype. Applies to well-phenotyped individuals in literature who are unaffected by age 40. Alternatively, can apply if variant is present in **≥6 homozygotes** in gnomAD v.4.1.0 or later. |
| **Supporting (BS2_Supporting)** | Variant is present in **≥3 homozygotes** in gnomAD v.4.1.0 or later. |

**Modification Type:** Disease-specific, Strength

---

### BS3 - Functional Studies (No Effect)

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

**VCEP Specifications:**
- **Extracellular domain variants (occurring between amino acids 52-462) are known to show no damaging effect in these assays and are excluded from BS3**

#### Strength Level

| Strength | Criteria |
|----------|----------|
| **Supporting (BS3_Supporting)** | Not applicable for splicing effects (replaced by BP7_Strong (RNA)). For studies reporting guanylate cyclase activity, cutoff is **>50%** of wild-type control. |

**Acceptable functional studies include those that report:**
- Failure of GUCY2D to localize to the cell surface (Zulliger et al., 2015)
- Failure of GUCY2D to bind RD3 (Zulliger et al., 2015)
- Failure of GCAP1, GCAP2, or RD3 to co-localize with GUCY2D at the cell surface (Peshenko et al., 2020; Jacobson et al., 2020; Peshenko et al., 2015)

**Modification Type:** Gene-specific, Strength

---

### BS4 - Lack of Segregation

**Original ACMG Summary:** Lack of segregation in affected members of a family.
- Caveat: The presence of phenocopies for common phenotypes can mimic lack of segregation. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder.

#### Strength Level

| Strength | Criteria |
|----------|----------|
| **Strong (BS4)** | Lack of segregation in affected members of a family. One or both variants are absent in a similarly affected family member. |

**Modification Type:** Clarification

---

### BP1-BP7 - Benign Supporting

| Criterion | Status | Comment |
|-----------|--------|---------|
| **BP1** | Not Applicable | Not applicable for GUCY2D |
| **BP2** | Applicable (Supporting) | Observed **in cis** with a Pathogenic variant. The other variant must meet LP or P classification using these rule specifications. |
| **BP3** | Not Applicable | No repetitive regions with unknown function |
| **BP4** | Applicable | Only applicable if **both** REVEL and SpliceAI scores are below cutoffs |
| **BP5** | Not Applicable | Due to high genetic heterogeneity and limited phenotypic specificities of retinal dystrophies. Also, the presence of this variant could simply represent carrier status. |
| **BP6** | Not Applicable | Not for use as recommended by ClinGen SVI VCEP Review Committee (PMID: 29543229) |
| **BP7** | Applicable | BP4 and BP7 can be added unless variant is in an excluded region. Evolutionary conservation is not considered informative. |

#### BP4 Specifications

| Strength | Criteria |
|----------|----------|
| **Moderate (BP4_Moderate)** | For missense variants: REVEL score **≤0.183** AND SpliceAI highest delta score **<0.1** |
| **Supporting (BP4)** | For missense variants: REVEL score **0.183 - 0.290** AND SpliceAI highest delta score **<0.1**. For silent/intronic variants outside designated splice region (at or beyond +7/-21) and synonymous exonic variants outside first/last 3 bases of exon: SpliceAI highest delta score **≤0.1**. |

#### BP7 Specifications

| Strength | Criteria |
|----------|----------|
| **Strong (BP7_Strong)** | BP7_Strong (RNA) - Used to designate capture of splicing data (not BS3). See GUCY2D-specific PVS1 Decision Tree for weighting and combining. |
| **Supporting (BP7)** | Use for synonymous variants and intronic variants outside donor/acceptor +/-1,2 dinucleotide positions. If SpliceAI ≤0.1, apply BP4 followed by assessment of BP7. |

**Positions excluded from BP7:**
- Synonymous substitutions at the first base of an exon
- Synonymous substitutions in the last 3 bases of an exon
- +1 through +7 of donor sequence
- -1 through -21 of acceptor sequence

---

## Point-Based Classification System

For GUCY2D variants where criteria codes for benign and pathogenic evidence apply, these variants are not subjected to a VUS classification. Instead, apply the rule combination point system described by Tavtigian et al. 2020 (PMID: 32720330).

### Point Values for ACMG/AMP Strength of Evidence Categories

| Evidence Strength | Pathogenic Points | Benign Points |
|-------------------|-------------------|---------------|
| Indeterminate | 0 | 0 |
| Supporting | 1 | -1 |
| Moderate | 2 | -2 |
| Strong | 4 | -4 |
| Very Strong | 8 | -8 |

### Point-Based Variant Classification Categories

| Category | Point Range |
|----------|-------------|
| **Pathogenic** | ≥10 |
| **Likely Pathogenic** | 6 to 9 |
| **Uncertain Significance** | 0 to 5 |
| **Likely Benign** | -1 to -6 |
| **Benign** | ≤-7 |

---

## Rules for Combining Criteria

### Pathogenic Classification

| Criteria Combination |
|---------------------|
| 1 Very Strong (PVS1, PS2_Very Strong, PM3_Very Strong) **AND** ≥1 Strong (PVS1_Strong, PS1, PS2, PS3, PM3_Strong, PP1_Strong) |
| 1 Very Strong **AND** ≥2 Moderate (PS1_Moderate, PS2_Moderate, PM1, PM3, PM4, PM5, PP1_Moderate, PP3_Moderate, PP4_Moderate) |
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
| ≥2 Strong (BS1, BS2, BS4, BP7_Strong) |
| 1 Stand Alone (BA1) |

### Likely Benign Classification

| Criteria Combination |
|---------------------|
| 1 Strong (BS1, BS2, BS4, BP7_Strong) **AND** 1 Supporting (BS2_Supporting, BS3_Supporting, BP2, BP4, BP7) |
| ≥2 Supporting (BS2_Supporting, BS3_Supporting, BP2, BP4, BP7) |

---

## Appendices

### Appendix A: GUCY2D-Specific PVS1 Decision Tree

Based on ClinGen SVI Working Group publication (Abou Tayoun et al., 2018; PMID: 30192042) and ClinGen SVI Splicing Subgroup (Walker et al., 2023; PMID: 37352859).

#### Nonsense or Frameshift Variants

| Variant Location | Expected Effect | PVS1 Code |
|------------------|-----------------|-----------|
| Codons 2-1058 | Predicted NMD | PVS1 |
| p.Arg1059-p.Lys1068 | May disrupt RD3 binding site | PVS1 |
| Beyond p.Lys1068 | Likely disrupts critical function | PVS1_Strong |

#### Deletion Variants

| Deletion Type | Effect | PVS1 Code |
|---------------|--------|-----------|
| Full gene deletion | - | PVS1 |
| Single/multi-exon deletion disrupting reading frame + NMD | Exon in NM_000180.4 | PVS1 |
| Single/multi-exon deletion disrupting reading frame, no NMD | Exons 2-19 critical | PVS1 |
| Single/multi-exon deletion preserving reading frame | Exons 2-19 critical | PVS1 |

#### Duplication Variants (≥1 exon, completely contained within gene)

| Duplication Status | Effect | PVS1 Code |
|--------------------|--------|-----------|
| Proven in tandem | Reading frame disrupted + NMD | PVS1 |
| Presumed in tandem | Reading frame presumed disrupted + NMD | PVS1_Strong |
| Proven not in tandem | - | N/A |

#### Initiation Codon Variants

| Status | PVS1 Code |
|--------|-----------|
| No known alternative start codon, ≥1 pathogenic variant(s) upstream of closest potential in-frame start codon (p.Met218) | PVS1 |
| Different functional transcript uses alternative start codon | N/A |

#### GUCY2D Exon Map and PVS1 Codes for Splice Site Variants

| Exon | 3' Acceptor Position | 5' Donor Position | Exon Skipping Effect | PVS1 Code | Domain |
|------|---------------------|-------------------|---------------------|-----------|--------|
| Exon 1 | NA | -10 | NA | PVS1_N/A (A) | NA |
| Exon 2 | -9 | 721 | Truncated protein | PVS1 (B) | LS, ECD |
| Exon 3 | 722 | 1026 | fs/NMD | PVS1 (C) | ECD |
| Exon 4 | 1027 | 1378 | fs/NMD | PVS1 (C) | ECD |
| Exon 5 | 1379 | 1463 | in-frame | PVS1 (F) | ECD, TM |
| Exon 6 | 1464 | 1566 | fs/NMD | PVS1 (C) | JMD |
| Exon 7 | 1567 | 1668 | in-frame | PVS1 (F) | JMD |
| Exon 8 | 1669 | 1749 | in-frame | PVS1 (F) | JMD |
| Exon 9 | 1750 | 1956 | in-frame | PVS1 (F) | JMD, KHD |
| Exon 10 | 1957 | 2113 | fs/NMD | PVS1 (C) | KHD |
| Exon 11 | 2114 | 2263 | in-frame | PVS1 (F) | KHD |
| Exon 12 | 2264 | 2412 | fs/NMD | PVS1 (C) | KHD |
| Exon 13 | 2413 | 2576 | fs/NMD | PVS1 (C) | KHD, DD |
| Exon 14 | 2577 | 2769 | fs/NMD | PVS1 (C) | CCD |
| Exon 15 | 2770 | 2944 | fs/NMD | PVS1 (C) | CCD |
| Exon 16 | 2945 | 3043 | in-frame | PVS1 (F) | CCD |
| Exon 17 | 3044 | 3138 | fs/NMD | PVS1 (C) | CCD |
| Exon 18 | 3139 | 3224 | fs/NMD | PVS1 (H→upgraded) | CCD |
| Exon 19 | 3225 | 3312+24 | fs/NMD | PVS1 (I→upgraded) | CCD |
| Exon 20 | *25 | *237 | NA | NA | NA |

**Domain abbreviations:** LS: leader sequence; ECD: extracellular domain; TM: transmembrane domain; JMD: juxtamembrane domain; KHD: kinase homology domain; DD: dimerization domain; CCD: cyclase catalytic domain

### Appendix B: SpliceAI Flowchart for PP3 and BP4

For variants located **outside** donor/acceptor ±1,2 dinucleotide positions:

| SpliceAI Δ Score | Action |
|------------------|--------|
| ≤0.1 | Apply BP4; consider BP7 based on location |
| >0.1 and <0.2 | PP3 N/A (Splicing); consider missense/indel predictions for exonic variants |
| ≥0.2 | Apply PP3 |

### Appendix C: PS1 Code Weights for Splicing Variants (Table 2 from Walker 2023)

| Variant Under Assessment (VUA) | Baseline Code | Position of Comparison Variant | PS1 with P Comparison | PS1 with LP Comparison |
|--------------------------------|---------------|-------------------------------|----------------------|------------------------|
| Outside splice donor/acceptor ±1,2 | PP3 | Same nucleotide | PS1 | PS1_Moderate |
| Outside splice donor/acceptor ±1,2 | PP3 | Within same splice motif (including ±1,2) | PS1_Moderate | PS1_Supporting |
| Outside splice donor/acceptor ±1,2 | PP3 | Within same splice region | PS1_Supporting | PS1_Supporting |
| At splice donor/acceptor ±1,2 | PVS1 | Within same splice donor/acceptor ±1,2 | PS1_Supporting | N/A |
| At splice donor/acceptor ±1,2 | PVS1 | Within same motif but outside ±1,2 | PS1_Supporting | PS1_Supporting |
| At splice donor/acceptor ±1,2 | PVS1_Strong/Moderate/Supporting | Within same ±1,2 | PS1 | N/A |
| At splice donor/acceptor ±1,2 | PVS1_Strong/Moderate/Supporting | Within same motif but outside ±1,2 | PS1_Moderate | PS1_Supporting |

### Appendix D: Population Frequency Thresholds Summary

| Criterion | Threshold | Strength |
|-----------|-----------|----------|
| BA1 | >0.016 (>1.6%) | Stand Alone |
| BS1 | 0.0016 - 0.016 | Strong |
| PM2 | ≤4.0 x 10⁻⁴ | Supporting |

### Appendix E: Reference PMIDs

| Reference | PMID | Description |
|-----------|------|-------------|
| Peshenko et al., 2020 | 33109612 | GUCY2D mutations in retinal guanylyl cyclase 1 |
| Jacobson et al., 2021 | 33997691 | Gene therapy in childhood blindness |
| Jacobson et al., 2022 | 36274938 | Night vision restored after decades of congenital blindness |
| Tucker et al., 2004 | 15123990 | Functional analyses of mutant recessive GUCY2D alleles |
| Jacobson et al., 2013 | 23035049 | RetGC1 deficiency in human LCA |
| Zulliger et al., 2015 | 25477517 | Impaired association of RD3 with guanylate cyclase |
| Peshenko et al., 2015 | 26100624 | Dimerization domain of RetGC1 |
| Tucker et al., 1998 | 9600905 | RetGC-1 to adenylyl cyclase conversion |
| Duda et al., 1999 | 9888789 | ROS-GC1 gene mutation in LCA |
| Boye et al., 2016 | 27881908 | Functional study via AAV vector in mouse retinas |
| Wimberg et al., 2018 | 30319355 | Ca2+-dependent cyclic GMP synthesis |
| Zägel et al., 2014 | 24616660 | Outer segment guanylate cyclase dysfunction |
| Duda et al., 2011 | 21463603 | Phototransduction switch motif |
| Peshenko et al., 2010 | 20050595 | RetGC1 activation by GCAP1 |
| Daich Varela et al., 2023 | 36084042 | Non-coding variants in inherited retinal dystrophies |
| Abou Tayoun et al., 2018 | 30192042 | Recommendations for PVS1 criterion |
| Walker et al., 2023 | 37352859 | ACMG/AMP framework for splicing |
| Tavtigian et al., 2020 | 32720330 | Point system for ACMG/AMP classification |
| Liu et al., 1997 | 9391039 | Catalytic mechanism of guanylyl cyclases |
| Bouzia et al., 2020 | 31704230 | GUCY2D-Associated LCA natural history |
| ClinGen SVI De Novo Criteria | - | PS2/PM6 Version 1.1 |

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 1/22/2025 | Initial release |

---

*This document was compiled from ClinGen VCEP specifications and ClinGen SVI recommendations. For the most current version, please refer to the [ClinGen website](https://clinicalgenome.org/).*
