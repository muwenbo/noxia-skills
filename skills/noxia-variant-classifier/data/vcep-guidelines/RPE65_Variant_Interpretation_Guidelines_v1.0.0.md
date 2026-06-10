# ClinGen Leber Congenital Amaurosis/early onset Retinal Dystrophy VCEP Variant Interpretation Guidelines for RPE65

**Version:** 1.0.0
**Released:** 10/24/2023
**Affiliation:** Leber Congenital Amaurosis/early onset Retinal Dystrophy VCEP
**Based on:** Richards et al., 2015 ACMG/AMP Guidelines

---

## Gene Information

| Attribute | Value |
|-----------|-------|
| **Gene** | RPE65 (HGNC:10294) |
| **HGNC Name** | retinoid isomerohydrolase RPE65 |
| **Transcript** | NM_000329.3 |
| **Disease** | RPE65-related recessive retinopathy (MONDO:0100368) |
| **Inheritance** | Autosomal recessive inheritance |

---

## Phenotype Requirements

All probands being considered for any pathogenic phenotype codes (PP1, PP4, PM3, PM6, PS2) at any strength **must** have the following phenotype characteristics:

- Absent or severely decreased rod electroretinogram response, **OR**
- Congenital night blindness/nyctalopia, **OR**
- A diagnosis of Leber congenital amaurosis/eoRD

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
- Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7).
- Use caution interpreting LOF variants at the extreme 3' end of a gene.
- Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact.
- Use caution in the presence of multiple transcripts.

**VCEP Specifications:** See RPE65-specific PVS1 Decision Tree, modified from Walker 2023 (PMID: 37352859) and Tayoun 2018 (PMID: 30192042).

**Modification Type:** Gene-specific

#### Strength Levels

| Strength | Criteria |
|----------|----------|
| **Very Strong (PVS1)** | Predicted splice defects at +/- 1,2 in exons 1-14. Single to multi-exon deletions, with or without predicted NMD (all exons are considered critical to protein function). Nonsense or frameshift mutations from p.Ser2 through p.Gly528. Duplications of exons proven in tandem. PVS1(RNA): RNA splicing data with evidence of alternative transcript production at complete levels, relative to normal allele. |
| **Strong (PVS1_Strong)** | Applied to variants in the initiation codon (Met1). The second in-frame methionine is at residue 93, with no known evidence it can serve as a start codon. Nonsense or frameshift mutations from p.Leu529 through p.Ser533. Duplications of exons presumed in tandem. PVS1(RNA)_Strong: RNA splicing data with evidence of alternative transcript production at near complete levels, relative to normal allele. |
| **Moderate** | Not specified for PVS1 at this level by this VCEP. |
| **Supporting** | Not specified for PVS1 at this level by this VCEP. |

#### PVS1 Decision Tree: Nonsense/Frameshift

| Variant Location | PVS1 Strength | Rationale |
|------------------|---------------|-----------|
| Nonsense/frameshift p.Ser2 - p.Pro466 | PVS1 | Transcripts expected to undergo NMD |
| Nonsense/frameshift p.Pro467 - p.Gly528 | PVS1 | Disrupts critical domain/active site at His527/Gly528; transcripts will not undergo NMD but region is critical |
| Nonsense/frameshift p.Leu529 - p.Ser533 | PVS1_Strong | Likely disrupts critical function based on multiple reported variants at p.Phe530 and p.Ser533 |

#### PVS1 Decision Tree: Deletions

| Deletion Type | PVS1 Strength | Rationale |
|---------------|---------------|-----------|
| Full gene deletion | PVS1 | Complete loss of gene |
| Single to multi-exon deletion disrupting reading frame (predicted NMD) | PVS1 | Exon present in NM_000329.3; all exons critical |
| Single to multi-exon deletion disrupting reading frame (NOT predicted NMD) | PVS1 | All exons 1-14 harbor pathogenic variants and are considered critical |
| Single to multi-exon deletion preserving reading frame | PVS1 | All exons 1-14 harbor pathogenic variants and are considered critical |

#### PVS1 Decision Tree: Duplications

| Duplication Type | PVS1 Strength |
|------------------|---------------|
| Proven in tandem, reading frame disrupted + NMD predicted | PVS1 |
| Presumed in tandem, reading frame presumed disrupted + NMD predicted | PVS1_Strong |
| Proven not in tandem | N/A |
| Unknown impact on reading frame/NMD | N/A |

#### PVS1 Decision Tree: Initiation Codon

| Condition | PVS1 Strength |
|-----------|---------------|
| No known alternative start codon; >=1 pathogenic variant(s) upstream of closest in-frame Met (p.Met93) | PVS1_Strong |
| Different functional transcript uses alternative start codon | N/A |

#### PVS1 Decision Tree: Splice Variants (+/- 1,2 Dinucleotide)

| Exon | 3' Acceptor | 5' Donor | Exon Skipping Effect | PVS1 Code |
|------|-------------|----------|---------------------|-----------|
| Exon 1 | — | c.11 | fs/NMD | PVS1 (B) |
| Exon 2 | c.12 | c.94 | fs/NMD | PVS1 (C) |
| Exon 3 | c.95 | c.245 | fs/NMD | PVS1 (C) |
| Exon 4 | c.246 | c.353 | in frame/no NMD | PVS1 (F) |
| Exon 5 | c.354 | c.495 | fs/NMD | PVS1 (C) |
| Exon 6 | c.496 | c.643 | fs/NMD | PVS1 (C) |
| Exon 7 | c.644 | c.725 | fs/NMD | PVS1 (C) |
| Exon 8 | c.726 | c.858 | fs/NMD | PVS1 (C) |
| Exon 9 | c.859 | c.998 | fs/NMD | PVS1 (C) |
| Exon 10 | c.999 | c.1128 | fs/NMD | PVS1 (C) |
| Exon 11 | c.1129 | c.1243 | fs/NMD | PVS1 (C) |
| Exon 12 | c.1244 | c.1338 | fs/NMD | PVS1 (C) |
| Exon 13 | c.1339 | c.1450 | fs but no NMD (new stop in final exon) | PVS1 |
| Exon 14 | c.1451 | — | Not expected to undergo NMD but critical to protein function | PVS1 |

**RPE65-specific notes:**
1. All exons (1-14) harbor pathogenic variants and are considered critical to protein function.
2. The ATG initiation site is in exon 1, so 5' UTR recommendations do not apply.
3. No potential "rescue isoforms" are known.

#### Splicing Variant Evaluation

- For variants at **canonical +/- 1,2 positions**: Use PVS1 rule table above.
- For **non-canonical splice variants**: Use SpliceAI flowchart (part a) from PVS1 Decision Tree.
  - If SpliceAI highest delta score >= 0.2: Apply PP3 (splicing) at Supporting level.
  - If SpliceAI highest delta score < 0.2 and >= 0.1: No PP3 or BP4.
  - If SpliceAI highest delta score <= 0.1: Apply BP4, then consider BP7.
- **RNA splicing data**: Use PVS1(RNA) for evidence of complete impact; PVS1(RNA)_Strong for near complete; BP7_Strong(RNA) for no impact.
- **PS1 for splicing**: Per Walker 2023 Table 2, PS1 can be applied for variants with same predicted splicing impact as known pathogenic variants.

---

### PS1 - Same Amino Acid Change

**Original ACMG Summary:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change. Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:**
- For assessing same amino acid changes, SpliceAI must be used to ensure comparison variant is not causing a splicing defect (score <= 0.1).
- RPE65-specific PVS1 Decision Tree for scoring splicing variants is based on Walker et al. 2023.

**Modification Type:** Gene-specific

| Strength | Criteria |
|----------|----------|
| **Strong (PS1)** | Same amino acid change as a previously established **Pathogenic** variant regardless of nucleotide change. Must have one comparison variant that reaches a Pathogenic classification using this rule specification. SpliceAI scores for both variants should be within 10% of each other. Also applicable for same predicted splicing impact as a previously classified Pathogenic variant: used in conjunction with PP3 for variants outside splice donor/acceptor +/-1,2 with SpliceAI >= 0.2 and a comparable Pathogenic variant at the same position; or with PVS1 for variants at +/-1,2 with a comparable Pathogenic variant within the same +/-1,2 dinucleotide. |
| **Moderate (PS1_Moderate)** | Same amino acid change as a previously established **Likely Pathogenic** variant regardless of nucleotide change. Must have one comparison variant that reaches a Likely Pathogenic classification. SpliceAI scores for both variants should be within 10% of each other. Also applicable for same predicted splicing impact as a previously classified Likely Pathogenic variant: used in conjunction with PP3 for non-canonical variants with SpliceAI >= 0.2 and a comparable LP variant at the same position; or with PVS1_(reduced strength) for +/-1,2 variants with a comparable Pathogenic variant in the same motif but outside the +/-1,2 dinucleotide. |
| **Supporting (PS1_Supporting)** | Used in conjunction with PP3 for variants outside the splice donor/acceptor +/-1,2 with SpliceAI >= 0.2 and a comparable nucleotide variant within the same motif that has been designated Likely Pathogenic. Also used with PVS1 or PVS1_(reduced strength) for +/-1,2 variants with a comparable LP or P variant within the same splice site motif (outside +/-1,2 or at +/-1,2). |

---

### PS2 - De Novo (Confirmed)

**Original ACMG Summary:** De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.

**VCEP Specifications:**
- Use point table from SVI Recommendation for De Novo Criteria (PS2 & PM6) - Version 1.1.
- Individuals must have **2 variants** to consider scoring one for de novo.
- For "Phenotypic consistency" category, use **option 3**: "Phenotype consistent with gene but not highly specific and high genetic heterogeneity" (maximum **0.5 points/proband**).

**Modification Type:** Gene-specific

#### PS2/PM6 Point System (Table 1 - Points per de novo occurrence)

| Phenotypic Consistency | Confirmed de novo (PS2) | Assumed de novo (PM6) |
|------------------------|------------------------|-----------------------|
| Phenotype highly specific for gene | 2 | 1 |
| Phenotype consistent with gene but not highly specific | 1 | 0.5 |
| **Phenotype consistent with gene but not highly specific and high genetic heterogeneity*** | **0.5** | **0.25** |
| Phenotype not consistent with gene | 0 | 0 |

\* **RPE65 uses this row.** Maximum allowable value of 1 may contribute to overall score.

#### PS2/PM6 Evidence Strength Thresholds (Table 2)

| Total Points | Strength Level |
|--------------|----------------|
| 0.50 - 0.75 | Supporting (PS2_Supporting / PM6_Supporting) |
| 1.00 - 1.75 | Moderate (PS2_Moderate / PM6) |
| 2.00 - 3.75 | Strong (PS2 / PM6_Strong) |
| >= 4.00 | Very Strong (PS2_VeryStrong / PM6_VeryStrong) |

---

### PS3 - Functional Studies

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.

**VCEP Specifications:**
- **Strength: Supporting only** (PS3_Supporting). Not applicable for splicing effects (replaced by PVS1_Strength (RNA)).
- For studies reporting isomerohydrolase activity, cutoff is **<= 10% of wild-type control** for abnormal.

**Modification Type:** Gene-specific, Strength

#### Approved Functional Assays

| Assay Type | Description | Readout | Strength | Key PMIDs |
|------------|-------------|---------|----------|-----------|
| **Isomerohydrolase Activity** | Cells transfected with WT or mutant RPE65 plasmids; all-trans retinol added; 11-cis-retinol production measured by HPLC | Quantity of 11cROL produced as percentage of wild-type. Abnormal: <= 10% of WT; Normal: equivalent to WT | PS3_Supporting / BS3_Supporting | Jin 2005 (16096063), Philp 2009 (19431183), Li 2014 (24849605), Li 2015 (25752820), Jin 2016 (26427455), Redmond 2005 (16150724), Lorenz 2008 (18599565), Bereta 2008 (18722466), Takahashi 2006 (16754667), Chen 2006 (16828753), Nikolaeva 2011 (20043869) |
| **Expression (Western Blot)** | Cells transfected with WT or mutant RPE65; protein expression measured by western blot with densitometry | RPE65 signal vs. WT. Abnormal: severely reduced/undetectable (15-20% of WT); Normal: equivalent to WT | PS3_Supporting / BS3_Supporting | Li 2014 (24849605), Li 2015 (25752820), Jin 2016 (26427455) |
| **Localization** | 293T-LC cells transfected with WT or mutant RPE65; membrane fractions isolated; western blot at 30 vs. 37 degrees C | Membrane localization signal normalized to temperature. Abnormal: increased relative to WT at 30°C | PS3_Supporting / BS3_Supporting | Li 2015 (25752820) |
| **Stability (Proteasome Inhibition)** | Cells transfected with WT or mutant RPE65, treated with proteasome inhibitors (MG115, MG132, pepstatin A, UBEI-41); western blot | RPE65 signal with proteasome inhibition vs. WT. Abnormal: increased relative to WT (proteasome-mediated degradation) | PS3_Supporting / BS3_Supporting | Li 2014 (24849605), Li 2015 (25752820) |

---

### PS4 - Prevalence in Affected

**Original ACMG Summary:** The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.

**VCEP Specifications:** *Not Applicable*

---

### PM1 - Mutational Hot Spot

**Original ACMG Summary:** Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.

**VCEP Specifications:**
- Because these sites have been identified based on well-established functional domains rather than a known cluster of pathogenic/likely pathogenic variants, this criterion is **not mutually exclusive with PM5**.
- Missense variants that meet BS1 or BA1 should **not** be eligible to meet this criterion.

**Modification Type:** Gene-specific

| Strength | Criteria |
|----------|----------|
| **Moderate (PM1)** | Met by variants encoding missense substitutions at **His180, His182, His241, His313, Glu417, or His527**, which are required residues located within the active site. Also met by variants encoding missense substitutions between **Ala107 and Gly125**, which are known to mediate localization to the ER membrane. |

---

### PM2 - Absent from Controls

**Original ACMG Summary:** Absent from controls (or at extremely low frequency if recessive) in population databases.

**VCEP Specification (Supporting only):**
- gnomAD PopMax Filtering Allele Frequency (FAF) **<= 2.0 x 10^-4**
- The cutoff value is set between the FAF of the most common pathogenic RPE65 variant (1.6 x 10^-4) and the Whiffin-Ware calculation of 8 x 10^-3 for the maximum credible population allele frequency.
- This rule should **not** be applied if variant would otherwise meet criteria for a benign classification, as rarity should not outweigh other benign evidence.

**Modification Type:** Disease-specific, Strength

---

### PM3 - In Trans with Pathogenic

**Original ACMG Summary:** For recessive disorders, detected in trans with a pathogenic variant.

**VCEP Specifications:**
- Use SVI recommendations for PM3 criterion.
- Both variants must be classified using these rule specifications.
- Each proband is awarded a point value based on phasing (confirmed in trans vs. unknown) and classification of the variant on the other allele (Table 1). Points are summed across probands and compared to Table 2.

**Modification Type:** Disease-specific

#### PM3 Point System (Table 1 - Points per in trans occurrence)

| Classification/Zygosity of Other Variant | Confirmed in Trans | Phase Unknown |
|------------------------------------------|-------------------|---------------|
| Pathogenic or Likely pathogenic variant | 1.0 | 0.5 (P) / 0.25 (LP) |
| Homozygous occurrence (max point 1.0) | 0.5 | N/A |
| Uncertain significance variant on other allele (max point 0.5) | 0.25 | 0.0 |

All variants should be sufficiently rare (meet PM2 specification).

#### PM3 Evidence Strength Thresholds (Table 2)

| Total Points | Strength Level |
|--------------|----------------|
| 0.5 - 0.75 | PM3_Supporting |
| 1.0 - 1.75 | PM3 (Moderate) |
| 2.0 - 3.75 | PM3_Strong |
| >= 4.0 | PM3_VeryStrong |

---

### PM4 - Protein Length Changes

**Original ACMG Summary:** Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

**Modification Type:** Gene-specific

| Strength | Criteria |
|----------|----------|
| **Moderate (PM4)** | Protein length change of **>= 2 amino acids** that leads to loss of at least one conserved residue (PhyloP > 2.0) or insertion of new amino acids adjacent to at least one conserved residue (PhyloP > 2.0). |
| **Supporting (PM4_Supporting)** | Protein length change of **1 amino acid** that leads to loss of at least one conserved residue (PhyloP > 2.0) or insertion of new amino acid adjacent to at least one conserved residue (PhyloP > 2.0). |

---

### PM5 - Novel Missense at Same Residue

**Original ACMG Summary:** Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.

**VCEP Specifications:**
- For assessing same amino acid changes, SpliceAI scores for both variants should be within 10% of each other.

| Strength | Criteria |
|----------|----------|
| **Moderate (PM5)** | Missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before. Must have one comparison variant that reaches a **Pathogenic** classification using this rule specification. |
| **Supporting (PM5_Supporting)** | Missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before. Must have one comparison variant that reaches a **Likely Pathogenic** classification using this rule specification. |

**Modification Type:** Strength (Supporting level)

---

### PM6 - De Novo (Assumed)

**Original ACMG Summary:** Assumed de novo, but without confirmation of paternity and maternity.

**VCEP Specifications:** *Not Applicable*

**Comments:** Use the PS2 code in lieu of using this code for de novo variants. PM6 is incorporated into the PS2/PM6 point system above (see [PS2](#ps2---de-novo-confirmed)).

---

### PP1 - Co-segregation

**Original ACMG Summary:** Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.

**VCEP Specifications:**
- Requires co-segregation with disease in multiple affected family members **and** evidence that this variant and another RPE65 variant are *in trans*.

**Modification Type:** Disease-specific, Strength

| Strength | Criteria |
|----------|----------|
| **Strong (PP1_Strong)** | Segregation in proband plus **>= 3 similarly affected relatives** |
| **Moderate (PP1_Moderate)** | Segregation in proband plus **2 similarly affected relatives** |
| **Supporting (PP1)** | Segregation in proband plus **1 similarly affected relative** |

---

### PP2 - Missense in Constrained Gene

**Original ACMG Summary:** Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.

**VCEP Specifications:** *Not Applicable*

**Comments:** Not applicable for RPE65.

---

### PP3 - Computational Evidence

**Original ACMG Summary:** Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).

**VCEP Specifications:**
- PP3 should **not** be used to evaluate variants at canonical splice sites.
- For non-canonical sites, if SpliceAI score is >= 0.2, apply PP3 (splicing) instead.
- **REVEL** outperformed other in silico prediction models for RPE65 using 161 assumed pathogenic variants, 19 assumed benign variants and 17 different predictors (courtesy of R. Chen Lab at Baylor College of Medicine).
- Score ranges based on SVI Working Group "Calibration of computational tools for missense variant pathogenicity classification and ClinGen recommendations for PP3/BP4 criteria" (Pejaver et al., 2022; PMID: 36413997).

**Modification Type:** Gene-specific, Strength

| Strength | Criteria |
|----------|----------|
| **Moderate (PP3_Moderate)** | For a missense variant: REVEL score **>= 0.774**. Splice variants use PP3 only at Supporting level. |
| **Supporting (PP3)** | For a missense variant: REVEL score **0.644 - 0.773**. For a predicted splicing variant: SpliceAI (max distance 500 bp) highest delta score **>= 0.2**. See RPE65-specific PVS1 Decision Tree part (a) for SpliceAI flowchart. |

---

### PP4 - Phenotype Specificity

**Original ACMG Summary:** Patient's phenotype or family history is highly specific for a disease with a single genetic etiology.

**VCEP Specifications:**
- A point system determines when there is enough phenotype information to use this code.
- A proband must have **two RPE65 variants** to consider applying PP4 (phase is not considered).
- Do not include a proband with a suspected diagnosis of more than one retinal dystrophy.

**Modification Type:** Disease-specific, Strength

#### PP4 Phenotype Point System

**Required for use of PP4 (0.5 points each)** — at least one must be present:

| Finding | Points |
|---------|--------|
| Absent or severely decreased rod electroretinogram (ERG) responses | 0.5 |
| Congenital night blindness/nyctalopia | 0.5 |
| Clinical diagnosis of Leber congenital amaurosis | 0.5 |

**Specific RPE65 Phenotype Findings (2 points each; gene therapy = 8 points):**

| Finding | Points |
|---------|--------|
| Absence or minimal autofluorescence | 2 |
| White/yellow dots on color photography (fundus albipunctatus-type) in the context of severe retinal dysfunction | 2 |
| Previous exome, genome, or 100+ retinal dystrophy gene panel testing that did not provide an alternative explanation for visual impairment | 2 |
| Participation in a gene therapy trial or study with strict inclusion criteria and subsequent positive results | 2 |
| Significant, documented improvement of FST or other measure of dark-adapted vision after treatment with Luxturna or other RPE65 gene therapy (supporting information required from treating clinician if not in published report) | 8 |

**Consistent with RPE65 Phenotype Findings (0.5 or 1 point each):**

| Finding | Points |
|---------|--------|
| Optic disc drusen | 0.5 |
| Optic nerve pallor | 0.5 |
| Pigmentary retinopathy with attenuated vessels | 0.5 |
| Poor pupillary light response | 0.5 |
| Posterior subcapsular cataract | 0.5 |
| RPE mottling | 0.5 |
| Macular atrophy | 0.5 |
| Symptomatic onset between birth and age five years | 1 |
| OCT is preserved with respect to vision loss | 1 |
| Decreased peripheral vision | 1 |
| Abnormal color vision or evidence of cone involvement on ERG | 1 |
| Decreased central visual acuity | 1 |
| Nystagmus | 1 |
| Light staring | 1 |

#### PP4 Strength Thresholds

| Total Points | Strength |
|--------------|----------|
| < 4 | PP4 not met |
| 4 - 7.5 | PP4 (Supporting) |
| >= 8 | PP4_Moderate (must also have at least one **specific** criterion met) |

---

### PP5 - Reputable Source

**Original ACMG Summary:** Reputable source recently reports variant as pathogenic, but the evidence is not available to the laboratory to perform an independent evaluation.

**VCEP Specifications:** *Not Applicable*

This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PMID: 29543229).

---

## Benign Criteria

### BA1 - Allele Frequency >5%

**Original ACMG Summary:** Allele frequency is above 5% in population databases.

**VCEP Specifications:**
- The maximum credible population allele frequency for the disease, based on the Whiffin-Ware calculator, is 8.16 x 10^-3 (assumes population frequency of 1 in 3,000 individuals, genetic heterogeneity = 20%, penetrance = 100%, allele heterogeneity = 1).

**VCEP Specification (Stand Alone):**
- gnomAD PopMax FAF **>= 8 x 10^-3**
- Use large population databases (i.e. gnomAD).

**Modification Type:** Disease-specific

---

### BS1 - Frequency Greater Than Expected

**Original ACMG Summary:** Allele frequency is greater than expected for disorder.

**VCEP Specifications:**
- The BS1 value was derived by decreasing the BA1 cutoff (>= 8.0 x 10^-3) by one order of magnitude.

**VCEP Specification (Strong):**
- gnomAD PopMax FAF between **8 x 10^-4 and 8 x 10^-3**

**Modification Type:** Disease-specific

---

### BS2 - Observed in Healthy Adult

**Original ACMG Summary:** Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

**VCEP Specification (Strong):**
- Variant is present in **>= 3 homozygotes** without any features of the phenotype.
- This rule only applies to individuals found in the **literature** who have been well-phenotyped and are unaffected by age 40.
- Presence in databases such as gnomAD are **not** considered.

**Modification Type:** Disease-specific

---

### BS3 - Functional Studies (No Effect)

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

**VCEP Specifications:**
- **Strength: Supporting only** (BS3_Supporting). Not applicable for splicing effects (replaced by BP7_Strong (RNA)).
- See approved functional assays table above (same assays as PS3).
- For studies reporting isomerohydrolase activity, activity must be **>= 50% of wild-type control** for normal.

**Modification Type:** Gene-specific, Strength

---

### BS4 - Lack of Segregation

**Original ACMG Summary:** Lack of segregation in affected members of a family.

**VCEP Specification (Strong):**
- One or both variants are **absent** in a similarly affected family member.

**Modification Type:** Clarification

---

### BP1-BP7 - Benign Supporting

| Criterion | Status | Specifications |
|-----------|--------|----------------|
| **BP1** | *Not Applicable* | Not applicable for RPE65. |
| **BP2** | Supporting | Observed *in cis* with a Pathogenic variant. Use code if the variant of interest is in cis with a P or LP variant. The other variant must meet LP or P classification using these rule specifications. |
| **BP3** | *Not Applicable* | Not applicable for RPE65. |
| **BP4** | Supporting / Moderate | **Only applicable if both REVEL and SpliceAI scores are below cutoffs.** **Moderate:** Missense variant with REVEL <= 0.183 AND highest SpliceAI delta score < 0.1. **Supporting:** Missense variant with REVEL 0.183 - 0.290 AND highest SpliceAI delta score < 0.1. For silent/intronic variants outside the splice region (+7/-21) and synonymous exonic variants outside the first and last 3 bases of the exon: BP4 met if highest SpliceAI delta score <= 0.1. |
| **BP5** | *Not Applicable* | Due to high genetic heterogeneity and limited phenotypic specificities of retinal dystrophies, this rule should not be used. The presence of this variant could simply represent carrier status. |
| **BP6** | *Not Applicable* | Not for use per ClinGen SVI VCEP Review Committee (PMID: 29543229). |
| **BP7** | Supporting / Strong | **BP4 and BP7 can be added** unless variant is in an excluded region. Evolutionary conservation is not considered informative. **Strong (BP7_Strong (RNA)):** Used to designate capture of splicing data (not BS3). See PVS1 Decision Tree for weighting. **Supporting:** Use for variants outside donor/acceptor +/-1,2. If SpliceAI <= 0.1, apply BP4 then assess BP7. **Positions excluded from BP7:** Synonymous substitutions at the first base of an exon; synonymous substitutions in the last 3 bases of an exon; +1 through +7 of donor sequence; -1 through -21 of acceptor sequence. |

---

## Rules for Combining Criteria

The point system of Tavtigian et al. 2020 (PMID: 32720330) is used for all classifications. For variants where criteria codes for both benign and pathogenic evidence apply, these variants are **not** subjected to a VUS classification. Instead, apply the rule combination point system. If there is a conflict between the point system and the VCI result, the point system classification is applied.

### Tavtigian Point Values (Table 2)

| Evidence Strength | Points (Pathogenic direction) | Points (Benign direction) |
|-------------------|-------------------------------|---------------------------|
| Supporting | 1 | -1 |
| Moderate | 2 | -2 |
| Strong | 4 | -4 |
| Very Strong | 8 | -8 |
| Stand Alone | — | (Benign) |

### Point-Based Classification Thresholds (Table 3)

| Total Points | Classification |
|--------------|----------------|
| >= 10 | Pathogenic |
| 6 to 9 | Likely Pathogenic |
| 0 to 5 | VUS |
| -1 to -6 | Likely Benign |
| <= -7 | Benign |

### Pathogenic Classification (Standard Criteria-Based)

| Criteria Combination |
|---------------------|
| 1 Very Strong *(PVS1, PS2_VeryStrong, PM3_VeryStrong)* **AND** >= 1 Strong *(PVS1_Strong, PS1, PS2, PM3_Strong, PP1_Strong)* |
| 1 Very Strong **AND** >= 2 Moderate *(PS1_Moderate, PS2_Moderate, PM1, PM3, PM4, PM5, PP1_Moderate, PP3_Moderate, PP4_Moderate)* |
| 1 Very Strong **AND** 1 Moderate **AND** 1 Supporting *(PS1_Supporting, PS2_Supporting, PS3_Supporting, PM2_Supporting, PM3_Supporting, PM4_Supporting, PM5_Supporting, PP1, PP3, PP4)* |
| 1 Very Strong **AND** >= 2 Supporting |
| >= 2 Strong *(PVS1_Strong, PS1, PS2, PM3_Strong, PP1_Strong)* |
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
| >= 2 Strong *(BS1, BS2, BS4, BP7_Strong)* |

### Likely Benign Classification

| Criteria Combination |
|---------------------|
| 1 Strong *(BS1, BS2, BS4, BP7_Strong)* **AND** 1 Supporting *(BS3_Supporting, BP2, BP4, BP7)* |
| >= 2 Supporting *(BS3_Supporting, BP2, BP4, BP7)* |

---

## Appendices

### Appendix A: PVS1 Decision Tree Summary

The RPE65-specific PVS1 Decision Tree is based on:
- Tayoun et al. 2018 (PMID: 30192042) - ClinGen SVI PVS1 recommendations
- Walker et al. 2023 (PMID: 37352859) - ClinGen SVI Splicing Subgroup recommendations

**Key RPE65-specific modifications:**
1. All exons (1-14) harbor pathogenic variants and all are considered critical to protein function.
2. ATG initiation site is in exon 1; 5' UTR recommendations do not apply.
3. No potential "rescue isoforms" are known.
4. Second in-frame methionine is at residue 93 (p.Met93); initiation codon variants are PVS1_Strong.

**Three sub-parts:**
- **(a)** SpliceAI Flowchart - calibrated cutoff scores for SpliceAI (based on Walker 2023 Figure 4). Used for PP3 and BP4 assessment of non-canonical splice variants.
- **(b)** Table 2 from Walker 2023 - PS1 code weights for variants with same predicted splicing event as known pathogenic variants.
- **(c)** RPE65-specific PVS1 rule table for +/-1,2 changes and RNA splicing assay results.

### Appendix B: SpliceAI Flowchart Summary (Part a)

| SpliceAI Highest Delta Score | Action |
|-----------------------------|--------|
| >= 0.2 | Apply PP3 (splicing) at Supporting level |
| 0.1 - 0.2 | No PP3 or BP4 |
| <= 0.1 | Apply BP4, then consider BP7 |

**SpliceAI settings:** Max distance = 500 bp.

**Positions excluded from BP7:**
- Synonymous substitutions at the first base of an exon
- Synonymous substitutions in the last 3 bases of an exon
- +1 through +7 of donor sequence
- -1 through -21 of acceptor sequence

### Appendix C: Population Frequency Thresholds Summary

| Criterion | Threshold | Strength |
|-----------|-----------|----------|
| BA1 | >= 8 x 10^-3 (PopMax FAF) | Stand Alone |
| BS1 | 8 x 10^-4 to 8 x 10^-3 (PopMax FAF) | Strong |
| PM2 | <= 2.0 x 10^-4 (PopMax FAF) | Supporting |

**Whiffin-Ware calculator parameters:** Population frequency = 1 in 3,000; genetic heterogeneity = 20%; penetrance = 100%; allele heterogeneity = 1. Maximum credible population allele frequency = 8.16 x 10^-3.

### Appendix D: Computational Prediction Thresholds Summary

| Tool | Pathogenic Threshold | Benign Threshold |
|------|---------------------|------------------|
| **REVEL** (missense) | >= 0.774 (PP3_Moderate), 0.644 - 0.773 (PP3_Supporting) | <= 0.183 (BP4_Moderate), 0.183 - 0.290 (BP4_Supporting) |
| **SpliceAI** (splicing) | >= 0.2 (PP3_Supporting) | <= 0.1 (BP4) |

### Appendix E: Functional Assay Thresholds Summary

| Assay | PS3_Supporting (Abnormal) | BS3_Supporting (Normal) |
|-------|--------------------------|------------------------|
| Isomerohydrolase Activity | <= 10% of wild-type control | >= 50% of wild-type control |
| Expression (Western Blot) | Severely reduced/undetectable (15-20% of WT) | Equivalent to WT (well-expressed) |
| Localization | Enhanced membrane localization at 30°C relative to WT | No enhanced membrane localization |
| Stability | Increased signal with proteasome inhibition relative to WT | Equivalent to WT |

### Appendix F: Reference PMIDs

| # | Citation | PMID |
|---|----------|------|
| 1 | SVI Proposal for De Novo Criteria v1.1 | — |
| 2 | Bereta G, Kiser PD et al. (2008) *Biochemistry* 47(37):9856-65 | 18722466 |
| 3 | Philp AR, Jin M et al. (2009) *Hum Mutat* 30(8):1183-8 | 19431183 |
| 4 | Li S, Izumi T et al. (2014) *J Biol Chem* 289(27):18943-56 | 24849605 |
| 5 | Li S, Hu J et al. (2015) *J Biochem* 158(2):115-25 | 25752820 |
| 6 | Jin M, Li S et al. (2005) *Cell* 122(3):449-59 | 16096063 |
| 7 | Chen Y, Moiseyev G et al. (2006) *FEBS Lett* 580(17):4200-4 | 16828753 |
| 8 | Lorenz B, Poliakov E et al. (2008) *Invest Ophthalmol Vis Sci* 49(12):5235-42 | 18599565 |
| 9 | Nikolaeva O, Takahashi Y et al. (2010) *Biochem Biophys Res Commun* 391(4):1757-61 | 20043869 |
| 10 | Jin M, Li S et al. (2016) *Adv Exp Med Biol* 854:525-32 | 26427455 |
| 11 | Pejaver V, Byrne AB et al. (2022) *Am J Hum Genet* 109(12):2163-2177 | 36413997 |
| 12 | Uppal S, Liu T et al. (2023) *Life Sci Alliance* 6(1) | 36265895 |
| 13 | Lopez-Rodriguez R, Lantero E et al. (2021) *Exp Eye Res* 212:108761 | 34492281 |
| 14 | Chung DC, Bertelsen M et al. (2019) *Am J Ophthalmol* 199:58-70 | 30268864 |
| 15 | Astuti GD, Bertelsen M et al. (2016) *Eur J Hum Genet* 24(7):1071-9 | 26626312 |
| 16 | Abou Tayoun AN, Pesaran T et al. (2018) *Hum Mutat* 39(11):1517-1524 | 30192042 |
| 17 | Walker LC, Hoya M et al. (2023) *Am J Hum Genet* 110(7):1046-1067 | 37352859 |
| 18 | Redmond TM, Poliakov E et al. (2005) *Proc Natl Acad Sci USA* 102(38):13658-63 | 16150724 |
| 19 | Takahashi Y, Chen Y et al. (2006) *J Biol Chem* 281(31):21820-21826 | 16754667 |
| 20 | Tavtigian SV, Harrison SM et al. (2020) *Hum Mutat* 41(10):1734-1737 | 32720330 |

---

## Version History

| Version | Date | Description |
|---------|------|-------------|
| 1.0.0 | 10/24/2023 | Initial release of LCA/eoRD Expert Panel Specifications for RPE65 |

---

*This document was compiled from ClinGen VCEP specifications and ClinGen SVI recommendations. For the most current version, please refer to the ClinGen website.*
