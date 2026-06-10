# ClinGen Leber Congenital Amaurosis/early onset Retinal Dystrophy VCEP Variant Interpretation Guidelines for AIPL1

**Version:** 1.0.0
**Released:** 9/26/2025
**Affiliation:** Leber Congenital Amaurosis/early onset Retinal Dystrophy VCEP
**Type:** Tavtigian et al., 2020 - Bayesian adaptation of Richards et al., 2015

---

## Gene Information

| Attribute | Value |
|-----------|-------|
| **Gene** | AIPL1 (HGNC:359) |
| **HGNC Name** | aryl hydrocarbon receptor interacting protein like 1 |
| **Transcript** | NM_014336.5 |
| **Disease** | AIPL1-related retinopathy (MONDO:0100438) |
| **Inheritance** | Autosomal recessive inheritance |

---

## General Comments

The point system of Tavtigian et al. (PMID:32720330) is being used for all classifications, so the traditional combining rules are not being utilized. Refer to the [Rules for Combining Criteria](#rules-for-combining-criteria) section for the point-based classification system.

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
   - [BP1 - Missense in Truncating Gene](#bp1---missense-in-truncating-gene)
   - [BP2 - In Cis or Trans with Pathogenic](#bp2---in-cis-or-trans-with-pathogenic)
   - [BP3 - In-Frame in Repeat Region](#bp3---in-frame-in-repeat-region)
   - [BP4 - Computational Evidence (No Effect)](#bp4---computational-evidence-no-effect)
   - [BP5 - Alternate Molecular Basis](#bp5---alternate-molecular-basis)
   - [BP6 - Reputable Source (Benign)](#bp6---reputable-source-benign)
   - [BP7 - Synonymous Variant](#bp7---synonymous-variant)
3. [Rules for Combining Criteria](#rules-for-combining-criteria)
4. [Appendices](#appendices)
   - [Appendix A: PVS1 Decision Tree](#appendix-a-pvs1-decision-tree)
   - [Appendix B: SpliceAI Flowchart](#appendix-b-spliceai-flowchart)
   - [Appendix C: PS1 Splice Code Weights](#appendix-c-ps1-splice-code-weights)
   - [Appendix D: PS3 Approved Functional Assays](#appendix-d-ps3-approved-functional-assays)
   - [Appendix E: PP4 Phenotype Point System](#appendix-e-pp4-phenotype-point-system)
   - [Appendix F: References](#appendix-f-references)

---

## Pathogenic Criteria

### PVS1 - Null Variant

**Original ACMG Summary:** Null variant (nonsense, frameshift, canonical ±1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.

**Caveats:**
- Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7)
- Use caution interpreting LOF variants at the extreme 3' end of a gene
- Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact
- Use caution in the presence of multiple transcripts

**VCEP Specifications:**

Use as defined by ClinGen SVI working group (Abou Tayoun et al., 2018) and as updated by the ClinGen SVI Splicing Subgroup (Walker et al., 2023). Refer to the AIPL1-specific PVS1 Decision Tree in [Appendix A](#appendix-a-pvs1-decision-tree).

#### Strength Levels

| Strength | Default Points | Criteria |
|----------|---------------|----------|
| **Very Strong (PVS1)** | 8 | See detailed specifications below |
| **Strong (PVS1_Strong)** | 4 | See detailed specifications below |
| **Moderate (PVS1_Moderate)** | 2 | See detailed specifications below |

#### Very Strong (PVS1)

- **Predicted splice defects at ±1,2 in exons 1-6**
- **Single to multi-exon deletions**, with or without predicted NMD. All exons are considered critical to protein function.
- **Initiation codon variants**: The second in-frame methionine is located at residue 40 in exon 2. There is no known study indicating that this methionine in AIPL1 can be used as start codon. Multiple variants located upstream of p.Met40 have been reported as pathogenic in HGMD and ClinVar, evidence that this entire region of the protein is functionally important.
- **Nonsense variants from p.Thr2 through p.Ser328**
- **Frameshift variants from p.Thr2 through p.Glu337** (The presence of extensive long ORFs may lead to significant additional protein length after frameshift.)
- **Duplications of exons proven in tandem**
- **PVS1(RNA)**: RNA splicing data with evidence of alternative transcript production at **complete levels**, relative to normal allele

#### Strong (PVS1_Strong)

- **Nonsense variants from p.Glu329 through p.Ser346** (significant truncation of the proline-rich domain (PRD))
- **Frameshift variants from p.Pro338 through p.His384** (likely to disrupt critical function)
- **Duplications of exons presumed in tandem**
- **PVS1(RNA)_Strong**: RNA splicing data with evidence of alternative transcript production at **near complete levels**, relative to normal allele

#### Moderate (PVS1_Moderate)

- **Nonsense variants from p.Ser347 through p.His384** (~10% truncation of the proline-rich domain (PRD))

---

### PS1 - Same Amino Acid Change

**Original ACMG Summary:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change. Example: Val->Leu caused by either G>C or G>T in the same codon.

**Caveat:** Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:**

- For assessing **same amino acid changes**, SpliceAI must be used to ensure comparison variant is not causing a splicing defect (score ≤0.1 indicates no likely defect)
- For assessing **splicing impact**, refer to the AIPL1-specific PVS1 Decision Tree. Part (b) defines PS1 code weights for variants with the same predicted splicing event as a known pathogenic/likely pathogenic variant.
- For sites to be considered "comparable", they should have similar SpliceAI-predicted effects (gain vs loss, site of effect)

| Strength | Default Points | Criteria |
|----------|---------------|----------|
| **Strong** | 4 | Same amino acid change as a previously established **Pathogenic** variant (must reach Pathogenic classification using this rule specification). Same predicted splicing impact as a previously classified P variant. |
| **Moderate** | 2 | Same amino acid change as a previously established **Likely Pathogenic** variant (must reach LP classification using this rule specification). Same predicted splicing impact as a previously classified LP variant. |
| **Supporting** | 1 | Same predicted splicing impact as previously classified variant (per Walker 2023 Table 2). |

See [Appendix C](#appendix-c-ps1-splice-code-weights) for PS1 code weights table for splicing variants.

---

### PS2 - De Novo (Confirmed)

**Original ACMG Summary:** De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.

**Note:** Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.

**VCEP Specifications:**

Use point table from SVI Recommendation for De Novo Criteria (PS2 & PM6) - Version 1.1.

**Important:** Individuals must have 2 variants to consider scoring one for de novo.

To determine the appropriate strength level:
1. Each proband with a de novo variant is awarded a point value based upon phenotypic consistency and confirmed or assumed parental relationships (Table 1)
2. The combined point value of all de novo occurrences is compared to Table 2 to determine the applicable evidence strength level

**Phenotypic consistency mapping to PP4:**
- Does not meet PP4 → use option 3: "Phenotype consistent with gene but not highly specific and high genetic heterogeneity"
- Meets PP4 at Supporting level → use option 2: "Phenotype consistent with gene but not highly specific"
- Meets PP4 at Moderate level → use option 1: "Phenotype highly consistent for gene"

**Required phenotype for all probands:**
- Absent or severely decreased rod electroretinogram response **OR**
- Congenital night blindness/nyctalopia **OR**
- A diagnosis of Leber congenital amaurosis/early-onset retinal dystrophy (eoRD)/cone-rod dystrophy

#### Table 1: Points Awarded Per De Novo Occurrence

| Phenotypic Consistency | Confirmed de novo | Assumed de novo |
|------------------------|-------------------|-----------------|
| Phenotype highly specific for gene | 2 | 1 |
| Phenotype consistent with gene but not highly specific | 1 | 0.5 |
| Phenotype consistent with gene but not highly specific and high genetic heterogeneity* | 0.5 | 0.25 |
| Phenotype not consistent with gene | 0 | 0 |

*Maximum allowable value of 1 may contribute to overall score

#### Table 2: Evidence Strength Thresholds for PS2

| Points | Strength Level | Default Points |
|--------|----------------|---------------|
| 0.50 - 0.75 | Supporting | 1 |
| 1.00 - 1.75 | Moderate | 2 |
| 2.00 - 3.75 | Strong | 4 |
| ≥4.00 | Very Strong | 8 |

---

### PS3 - Functional Studies

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.

**Note:** Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.

**VCEP Specifications:**

Not applicable for splicing effects (replaced by PVS1_Strength (RNA)).

See [Appendix D](#appendix-d-ps3-approved-functional-assays) for the complete list of approved functional assays.

| Strength | Default Points | Criteria |
|----------|---------------|----------|
| **Supporting** | 1 | Well-established in vitro or in vivo functional studies supportive of a damaging effect. See attached table for acceptable functional studies. |

**Approved Studies:**
- Bellingham et al. 2015 (PMID: 26650897) - Splicing assays
- Gopalakrishna et al. 2016 (PMID: 27268253) - cGMP hydrolysis, localization
- Hidalgo-de-Quintana et al. 2008 (PMID: 18408180) - Protein-protein interaction, chaperone activity
- Sacristán-Reviriego et al. 2017 (PMID: 28973376) - Localization, protein interaction, cGMP hydrolysis
- Sacristán-Reviriego et al. 2020 (PMID: 33067476) - Localization, protein interaction, cGMP hydrolysis

---

### PS4 - Prevalence in Affected

**Original ACMG Summary:** The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.

**VCEP Specifications:** **Not Applicable**

---

### PM1 - Mutational Hot Spot

**Original ACMG Summary:** Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.

**VCEP Specifications:** **Not Applicable**

**Comments:** Functional domains have not been definitively identified.

---

### PM2 - Absent from Controls

**Original ACMG Summary:** Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

**Caveat:** Population data for indels may be poorly called by next generation sequencing.

**VCEP Specifications:**

| Strength | Default Points | Criteria |
|----------|---------------|----------|
| **Supporting** | 1 | gnomAD total allele frequency ≤ **4.0 × 10⁻⁴** |

**Cutoff rationale:**
- Set just above the FAF of the most common pathogenic AIPL1 variant (p.Trp278Ter, 0.00035)
- Below the Whiffin-Ware calculation of 5.7 × 10⁻³ for the maximum credible population allele frequency

**Important:** This rule should **not** be applied if variant would otherwise meet criteria for a benign classification, as rarity of the variant should not outweigh other types of benign evidence.

---

### PM3 - In Trans with Pathogenic

**Original ACMG Summary:** For recessive disorders, detected in trans with a pathogenic variant.

**Note:** This requires testing of parents (or offspring) to determine phase.

**VCEP Specifications:**

Use SVI recommendations for PM3 criterion.

**Requirements:**
- Both variants must be classified using these rule specifications
- All probands must have required phenotype characteristics (see PS2)

#### Table 1: Points Awarded Per In Trans Occurrence

| Classification/Zygosity of Other Variant | Confirmed in Trans | Phase Unknown |
|------------------------------------------|-------------------|---------------|
| Pathogenic or Likely pathogenic variant | 1.0 | 0.5 (P) / 0.25 (LP) |
| Homozygous occurrence (max 1.0) | 0.5 | N/A |
| Uncertain significance variant on other allele (max 0.5) | 0.25 | 0.0 |

*All variants should be sufficiently rare (meet PM2 specification)

#### Table 2: Evidence Strength Thresholds for PM3

| Total Points | Strength Level | Default Points |
|--------------|----------------|---------------|
| 0.5 - 0.75 | PM3_Supporting | 1 |
| 1.0 - 1.75 | PM3 (Moderate) | 2 |
| 2.0 - 3.75 | PM3_Strong | 4 |
| ≥4.0 | PM3_VeryStrong | 8 |

---

### PM4 - Protein Length Changes

**Original ACMG Summary:** Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

**VCEP Specifications:**

**Do not apply** to the region from p.Ser328 to p.His384 unless the indel is ≥5 amino acids.

| Strength | Default Points | Criteria |
|----------|---------------|----------|
| **Moderate** | 2 | Protein length change of ≥2 amino acids that leads to loss of at least one conserved residue (PhyloP>2.0) or insertion of new amino acids adjacent to at least one conserved residue (PhyloP>2.0) |
| **Supporting** | 1 | Protein length change of 1 amino acid that leads to loss of at least one conserved residue (PhyloP>2.0) or insertion of new amino acid adjacent to at least one conserved residue (PhyloP>2.0) |

---

### PM5 - Novel Missense at Same Residue

**Original ACMG Summary:** Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.

**Caveat:** Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:**

Apply only for missense variants for which the amino acid change is the expected mechanism of disease. For the missense variant under curation and the variant(s) resulting in a different amino acid change:
- Exclude potential splice effects (SpliceAI scores should be <0.20)
- Confirm the applicability of PP3

| Strength | Default Points | Criteria |
|----------|---------------|----------|
| **Moderate** | 2 | Must have one comparison variant that reaches a **Pathogenic** classification using this rule specification |
| **Supporting** | 1 | Must have one comparison variant that reaches a **Likely Pathogenic** classification using this rule specification |

---

### PM6 - De Novo (Assumed)

**Original ACMG Summary:** Assumed de novo, but without confirmation of paternity and maternity.

**VCEP Specifications:** **Not Applicable**

**Comments:** Use the PS2 code in lieu of using this code for de novo variants. Points from assumed de novo are incorporated into the PS2 point system.

---

### PP1 - Co-segregation

**Original ACMG Summary:** Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.

**Note:** May be used as stronger evidence with increasing segregation data.

**VCEP Specifications:**

For moderate and strong codes, segregations can be added across multiple families, with each having a proband + at least one affected relative.

**Required phenotype for all probands:**
- Absent or severely decreased rod electroretinogram response **OR**
- Congenital night blindness/nyctalopia **OR**
- A diagnosis of Leber congenital amaurosis/early-onset retinal dystrophy (eoRD)/cone-rod dystrophy

| Strength | Default Points | Criteria |
|----------|---------------|----------|
| **Strong** | 4 | Co-segregation with disease in multiple affected family members and evidence that this variant and another AIPL1 variant are in trans. Requires segregation in one proband plus **≥3 similarly affected relatives** |
| **Moderate** | 2 | Co-segregation with disease in multiple affected family members and evidence that this variant and another AIPL1 variant are in trans. Requires segregation in one proband plus **2 similarly affected relatives** |
| **Supporting** | 1 | Co-segregation with disease in multiple affected family members and evidence that this variant and another AIPL1 variant are in trans. Requires segregation in one proband plus **1 similarly affected relative** |

---

### PP2 - Missense in Constrained Gene

**Original ACMG Summary:** Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.

**VCEP Specifications:** **Not Applicable**

**Comments:** Not applicable for AIPL1.

---

### PP3 - Computational Evidence

**Original ACMG Summary:** Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).

**Caveat:** As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.

**VCEP Specifications:**

- PP3 should **not** be used to evaluate variants at canonical splice sites. For canonical splice sites, apply PVS1(splicing).
- For non-canonical sites, if SpliceAI score is ≥0.2, apply PP3 (splicing) instead.
- Score ranges are based on calculations from the SVI Working Group publication "Calibration of computational tools for missense variant pathogenicity classification and ClinGen recommendations for PP3/BP4 criteria"
- PM1 is not applicable to AIPL1 so PP3_Strong is allowed and will not break the rule that PM1+PP3 should not exceed 4 pts.

| Strength | Default Points | Criteria |
|----------|---------------|----------|
| **Strong** | 4 | For missense variants: REVEL score ≥**0.932**. Splice variants use PP3 only at Supporting level. |
| **Moderate** | 2 | For missense variants: REVEL score **0.773 - 0.932**. Splice variants use PP3 only at Supporting level. |
| **Supporting** | 1 | For missense variants: REVEL score **0.644 - 0.773**. For UTR variants: CADD score ≥20.0. For predicted splicing variants: SpliceAI max distance 500 bp, highest delta score ≥0.2. |

See [Appendix B](#appendix-b-spliceai-flowchart) for SpliceAI flowchart.

---

### PP4 - Phenotype Specificity

**Original ACMG Summary:** Patient's phenotype or family history is highly specific for a disease with a single genetic etiology.

**VCEP Specifications:**

A point system was developed to determine when there is enough information about a proband's phenotype to qualify for use of this code.

**Requirements:**
- A proband must have two AIPL1 variants to consider applying PP4 (phase is not considered)
- PP4 should **not** be applied if variant meets either BA1 or BS1

**Caveat:** Do not include a proband with a suspected diagnosis of more than one retinal dystrophy.

| Strength | Default Points | Criteria |
|----------|---------------|----------|
| **Moderate** | 2 | ≥8 phenotype points required. Additionally, at least one **specific** criterion must be met. |
| **Supporting** | 1 | 4-7.5 phenotype points required. |

See [Appendix E](#appendix-e-pp4-phenotype-point-system) for the complete PP4 point system.

---

### PP5 - Reputable Source

**Original ACMG Summary:** Reputable source recently reports variant as pathogenic, but the evidence is not available to the laboratory to perform an independent evaluation.

**VCEP Specifications:** **Not Applicable**

This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PMID: 29543229).

---

## Benign Criteria

### BA1 - Allele Frequency Stand Alone

**Original ACMG Summary:** Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

**VCEP Specifications:**

The BA1 value was derived by increasing the BS1 lower cutoff (> 0.00057) by one order of magnitude.

| Strength | Default Points | Criteria |
|----------|---------------|----------|
| **Stand Alone** | N/A | gnomAD Grpmax FAF ≥**0.0057** (0.57%) |

Use large population databases (i.e. gnomAD).

---

### BS1 - Frequency Greater Than Expected

**Original ACMG Summary:** Allele frequency is greater than expected for disorder.

**VCEP Specifications:**

The maximum credible population allele frequency for the disease, based on the Whiffin-Ware calculator, is **5.7 × 10⁻³**. This assumes:
- Population frequency of 1 in 6000 individuals
- Genetic heterogeneity = 20%
- Penetrance of 100%
- Allele heterogeneity of 1

| Strength | Default Points | Criteria |
|----------|---------------|----------|
| **Strong** | -4 | gnomAD Grpmax FAF: **0.00057 - 0.00569** |

---

### BS2 - Observed in Healthy Adult

**Original ACMG Summary:** Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

**VCEP Specifications:**

| Strength | Default Points | Criteria |
|----------|---------------|----------|
| **Strong** | -4 | Variant is present in ≥3 homozygotes without any features of the phenotype. This rule applies to individuals found in the literature who have been well-phenotyped and are unaffected by age 40. **Alternatively**, this strength can be applied if the variant is present in ≥6 homozygotes in gnomAD v.4.1.0 or later. |
| **Supporting** | -1 | Variant is present in ≥3 homozygotes in gnomAD v.4.1.0 or later. |

---

### BS3 - Functional Studies (No Effect)

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

**VCEP Specifications:** **Not Applicable**

**Comments:** Not applicable for splicing effects (replaced by BP7_Strong (RNA)).

---

### BS4 - Lack of Segregation

**Original ACMG Summary:** Lack of segregation in affected members of a family.

**Caveat:** The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.

**VCEP Specifications:**

| Strength | Default Points | Criteria |
|----------|---------------|----------|
| **Strong** | -4 | Lack of segregation in affected members of a family. One or both variants are absent in a similarly affected family member. |

---

### BP1 - Missense in Truncating Gene

**Original ACMG Summary:** Missense variant in a gene for which primarily truncating variants are known to cause disease.

**VCEP Specifications:** **Not Applicable**

**Comments:** Not applicable for AIPL1.

---

### BP2 - In Cis or Trans with Pathogenic

**Original ACMG Summary:** Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder or observed in cis with a pathogenic variant in any inheritance pattern.

**VCEP Specifications:**

| Strength | Default Points | Criteria |
|----------|---------------|----------|
| **Supporting** | -1 | Observed **in cis** with a Pathogenic variant. Use code if the variant of interest is in cis with a Pathogenic or Likely Pathogenic variant. The other variant must meet a Likely Pathogenic or Pathogenic classification using these rule specifications. |

---

### BP3 - In-Frame in Repeat Region

**Original ACMG Summary:** In frame-deletions/insertions in a repetitive region without a known function.

**VCEP Specifications:** **Not Applicable**

**Comments:** No repetitive regions with unknown function.

---

### BP4 - Computational Evidence (No Effect)

**Original ACMG Summary:** Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc).

**Caveat:** As many in silico algorithms use the same or very similar input for their predictions each algorithm cannot be counted as an independent criterion. BP4 can be used only once in any evaluation of a variant.

**VCEP Specifications:**

**Only applicable if both the REVEL and SpliceAI scores are below cutoffs.**

| Strength | Default Points | Criteria |
|----------|---------------|----------|
| **Moderate** | -2 | For missense variants: REVEL score ≤**0.183**. In addition, highest SpliceAI delta score should also be below cutoff of 0.1. |
| **Supporting** | -1 | For missense variants: REVEL score **0.183 - 0.290**. In addition, highest SpliceAI delta score should also be below cutoff of 0.1. For silent/intronic variants outside the designated splice region (conservatively at or beyond positions +7/-21) and synonymous exonic variants located outside of the first and the last 3 bases of the exon: BP4 can be met if the highest SpliceAI delta score is ≤0.1. |

**Note:** BP7 can be met as well for synonymous/intronic variants.

See [Appendix B](#appendix-b-spliceai-flowchart) for SpliceAI flowchart.

---

### BP5 - Alternate Molecular Basis

**Original ACMG Summary:** Variant found in a case with an alternate molecular basis for disease.

**VCEP Specifications:** **Not Applicable**

**Comments:** Due to the high genetic heterogeneity and limited phenotypic specificities of retinal dystrophies, this rule should not be used. Additionally, the presence of this variant could simply represent carrier status.

---

### BP6 - Reputable Source (Benign)

**Original ACMG Summary:** Reputable source recently reports variant as benign, but the evidence is not available to the laboratory to perform an independent evaluation.

**VCEP Specifications:** **Not Applicable**

This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PMID: 29543229).

---

### BP7 - Synonymous Variant

**Original ACMG Summary:** A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.

**VCEP Specifications:**

BP4 and BP7 can be added unless variant is in an excluded region. Evolutionary conservation is not considered informative for application of this code.

| Strength | Default Points | Criteria |
|----------|---------------|----------|
| **Strong** | -4 | **BP7_Strong (RNA)**: Used to designate capture of splicing data (not BS3). See AIPL1-specific PVS1 Decision Tree for weighting and combining with other codes. |
| **Supporting** | -1 | Use not only for synonymous variants but also for intronic variants located outside of the donor/acceptor ±1,2 dinucleotide positions. If SpliceAI score ≤0.1, apply BP4 followed by assessment of BP7. |

**Positions excluded from BP7:**
- Synonymous substitutions at the first base of an exon
- Synonymous substitutions in the last 3 bases of an exon
- +1 through +7 of donor sequence
- -1 through -21 of acceptor sequence

---

## Rules for Combining Criteria

For AIPL1 variants where criteria codes for benign and pathogenic evidence apply, these variants are not subjected to a variant of uncertain significance (VUS) classification. Instead, the rule combination point system described by Tavtigian et al. 2020 (PMID: 32720330) is applied.

### Point Values for ACMG/AMP Strength of Evidence Categories

| Evidence Strength | Pathogenic | Benign |
|-------------------|------------|--------|
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
| **Uncertain Significance (VUS)** | 0 to 5 |
| **Likely Benign** | -1 to -6 |
| **Benign** | ≤-7 |

**Note:** BA1 (Stand Alone) automatically classifies a variant as Benign when met.

---

## Appendices

### Appendix A: PVS1 Decision Tree

#### Nonsense or Frameshift Variants

| Variant Position | Predicted NMD | PVS1 Code |
|------------------|---------------|-----------|
| Nonsense/frameshift terminating at codons 2-244 | Expected NMD | PVS1 |
| Nonsense from p.Glu245 through p.Ser328 | No NMD (truncation in critical functional region) | PVS1 |
| Nonsense from p.Glu329 through p.Ser346 | No NMD (significant truncation of PRD) | PVS1_Strong |
| Nonsense from p.Ser347 through p.His384 | No NMD (~10% truncation of PRD) | PVS1_Moderate |
| Frameshift from p.Glu245 through p.Glu337 | No NMD (likely to disrupt critical function) | PVS1 |
| Frameshift from p.Pro338 through p.His384 | No NMD (likely to disrupt critical function) | PVS1_Strong |

#### Deletions (Single Exon to Full Gene)

| Deletion Type | Condition | PVS1 Code |
|---------------|-----------|-----------|
| Full gene deletion | - | PVS1 |
| Single to multi-exon deletion | Disrupts reading frame, predicted NMD, exon(s) present in NM_014336.5 | PVS1 |
| Single to multi-exon deletion | Disrupts reading frame, predicted NMD, exon(s) absent from NM_014336.5 | N/A |
| Single to multi-exon deletion | Disrupts reading frame, NOT predicted NMD | PVS1 (exons 2-6 all critical) |
| Single to multi-exon deletion | Preserves reading frame | PVS1 (exons 2-6 all critical) |

#### Duplications (≥1 Exon, Completely Contained Within Gene)

| Duplication Status | Condition | PVS1 Code |
|--------------------|-----------|-----------|
| Proven in tandem | Reading frame disrupted and NMD predicted | PVS1 |
| Proven in tandem | No or unknown impact on reading frame and NMD | N/A |
| Presumed in tandem | Reading frame presumed disrupted and NMD predicted | PVS1_Strong |
| Proven not in tandem | - | N/A |

#### Initiation Codon

| Condition | PVS1 Code |
|-----------|-----------|
| No known alternative start codon in other transcripts, ≥1 pathogenic variant(s) upstream of closest potential in-frame start codon (closest in-frame Met is p.Met40) | PVS1 |
| Different functional transcript uses alternative start codon | N/A |

#### AIPL1 Exon Map and PVS1 Rule Table for Splice Sites

| Exon | 3' Acceptor Position | 5' Donor Position | Exon Skipping Effect | PVS1 Code | Critical Domain |
|------|---------------------|-------------------|---------------------|-----------|-----------------|
| Exon 1 | N/A | 96 | in frame/no NMD | PVS1 | FKBP |
| Exon 2 | 97 | 276 | in frame/no NMD | PVS1 | FKBP |
| Exon 3 | 277 | 465 | in frame/no NMD | PVS1 | FKBP |
| Exon 4 | 466 | 642 | in frame/no NMD | PVS1 | TPR |
| Exon 5 | 643 | 784 | fs/no NMD | PVS1 | TPR |
| Exon 6 | 785 | *1721 | N/A | PVS1 | TPR, PRD |

**Functional Domains:**
- **FKBP** (FK506-binding protein-like domain): amino acids 29-155
- **TPR** (Tetratricopeptide repeat domain): amino acids 178-297
- **PRD** (Proline-rich domain): amino acids 328-384

---

### Appendix B: SpliceAI Flowchart

For variants located **outside** donor/acceptor ±1,2 dinucleotide positions:

```
SpliceAI Δ score ≤0.1 → BP4
    └─ Synonymous/intronic variants outside splice regions → BP7

SpliceAI Δ score >0.1 and <0.2 → PP3 N/A (Splicing)
    └─ Consider missense/indel predictions for exonic variants

SpliceAI Δ score ≥0.2 → PP3 (Splicing)
```

**Positions excluded from BP7:**
- Synonymous substitutions at the first base of an exon
- Synonymous substitutions in the last 3 bases of an exon
- +1 through +7 of donor sequence
- -1 through -21 of acceptor sequence

---

### Appendix C: PS1 Splice Code Weights

**Table 2 from Walker et al. 2023: PS1 code weights for variants with same predicted splicing event as a known (likely) pathogenic variant**

| Variant Under Assessment (VUA) | Baseline Code Applicable to VUA | Position of Comparison Variant Relative to VUA | PS1 Code with P Comparison Variant | PS1 Code with LP Comparison Variant |
|-------------------------------|--------------------------------|-----------------------------------------------|-----------------------------------|-------------------------------------|
| Located outside splice donor/acceptor ±1,2 dinucleotide positions | PP3 | same nucleotide | PS1 | PS1_Moderate |
| Located outside splice donor/acceptor ±1,2 dinucleotide positions | PP3 | within same splice donor/acceptor motif (including at ±1,2 positions) | PS1_Moderate | PS1_Supporting |
| Located at splice donor/acceptor ±1,2 dinucleotide positions | PVS1 | within same splice donor/acceptor ±1,2 dinucleotide | PS1_Supporting | N/A |
| Located at splice donor/acceptor ±1,2 dinucleotide positions | PVS1 | within same splice donor/acceptor region, but outside ±1,2 dinucleotide | PS1_Supporting | PS1_Supporting |
| Located at splice donor/acceptor ±1,2 dinucleotide positions | PVS1_Strong, PVS1_Moderate, or PVS1_Supporting | within same splice donor/acceptor ±1,2 dinucleotide | PS1 | N/A |
| Located at splice donor/acceptor ±1,2 dinucleotide positions | PVS1_Strong, PVS1_Moderate, or PVS1_Supporting | within same splice donor/acceptor motif, but outside ±1,2 dinucleotide | PS1_Moderate | PS1_Supporting |

**Prerequisites for all:**
- The predicted event of the VUA must precisely match the predicted event of the comparison (likely) pathogenic variant
- The strength of prediction for VUA must be of similar or higher strength than the prediction for the comparison variant
- For exonic variants, predicted or proven functional effect of missense substitution(s) encoded by the VUA and (likely) pathogenic variant should also be considered before application of this code

---

### Appendix D: PS3 Approved Functional Assays

#### Table of Contents

| PMID | Assay 1 | Assay 2 | Assay 3 |
|------|---------|---------|---------|
| PMID: 27268253 | cGMP hydrolysis | disrupted cellular localization and aggregation | |
| PMID: 33067476 | Subcellular localization by immunofluorescent confocal microscopy and western blotting | Protein-protein interaction with recombinant HSP90α and HSP90β (ELISA) | cGMP hydrolysis (activity of co-expressed PDE6) |
| PMID: 18408180 | yeast two-hybrid assay testing for interaction with Hsp70 and HSP90α | enhancement of Hsp70 chaperone activity (Figure 7D) | |
| PMID: 15347646 | disrupted cellular localization and aggregation | | |
| PMID: 26650897 | splicing | | |
| PMID: 28973376 | disrupted cellular localization and aggregation | yeast two-hybrid assay testing for interaction with HSP90 | cGMP hydrolysis (PDE6 activity) |

#### Assay Categories

**1. Protein-Protein Interaction Assays**
- ELISA-based interaction with HSP90α and HSP90β
- Yeast two-hybrid assays testing interaction with Hsp70, HSP90α
- GST/FLAG tag-based pull-down assays

**2. cGMP Hydrolysis Assays**
- Measurement of PDE6 activity in co-transfected cells
- ELISA-based measurement of cellular cGMP levels

**3. Localization/Aggregation Assays**
- Immunofluorescent confocal microscopy
- Western blotting for subcellular localization
- Assessment of inclusion body formation

**4. Chaperone Activity Assays**
- HSP70 chaperone activity enhancement assays

**5. Splicing Assays**
- Minigene assays in HEK293 cells with PCR-based readout (PMID: 26650897)

---

### Appendix E: PP4 Phenotype Point System

#### Required for Use of PP4 (0.5 points each)

One of the following is **required**:
- Absent or severely decreased rod electroretinogram (ERG) responses **OR**
- Congenital night blindness/nyctalopia **OR**
- Clinical diagnosis of Leber congenital amaurosis or early-onset retinal dystrophy (eoRD) or cone-rod dystrophy

#### Specific AIPL1 Phenotype Findings List

| Finding | Points |
|---------|--------|
| **Previous exome, genome or retinal dystrophy gene panel testing** that did not provide an alternative explanation for visual impairment | |
| - Gene panel only | 2 |
| - Exome or genome NGS | 4 |
| **Participation in a gene therapy trial** | |
| - Study with strict inclusion criteria and subsequent positive results, details not reported | 2 |
| - Study with strict inclusion criteria and documented "Significant" improvement of FST or other measure of dark-adapted vision after treatment with AIPL1 gene therapy* | 8 |

*Supporting information required from treating clinician if sufficient detail is not included in published report

#### Consistent with AIPL1 Phenotype Findings List

| Finding | Points |
|---------|--------|
| Pigmentary retinopathy with attenuated vessels | 1 |
| Optic disc/nerve pallor | 0.5 |
| Optic disc drusen | 0.5 |
| Poor pupillary light response | 0.5 |
| RPE mottling | 0.5 |
| Symptomatic onset between birth and age ten years | 1 |
| Decreased peripheral vision | 1 |
| Abnormal color vision or evidence of cone involvement on ERG | 1 |
| Decreased central visual acuity | 1 |
| Nystagmus | 1 |
| Photophobia or photoattraction | 1 |
| Oculodigital reflex (eye poking) | 0.5 |
| Corneal abnormality/keratoconus | 0.5 |
| Macular atrophy/maculopathy | 0.5 |
| Posterior subcapsular cataract | 0.5 |

#### Strength Level Requirements

| Strength | Points Required | Additional Requirements |
|----------|-----------------|------------------------|
| **PP4_Moderate** | ≥8 points | At least one **specific** criterion must be met |
| **PP4_Supporting** | 4-7.5 points | None |

---

### Appendix F: References

1. Abou Tayoun AN, Pesaran T et al. *Recommendations for interpreting the loss of function PVS1 ACMG/AMP variant criterion.* **Hum Mutat** (2018) 39(11):1517-1524. DOI: 10.1002/humu.23626 PMID: 30192042

2. Walker LC, Hoya M et al. *Using the ACMG/AMP framework to capture evidence related to predicted and observed impact on splicing: Recommendations from the ClinGen SVI Splicing Subgroup.* **Am J Hum Genet** (2023) 110(7):1046-1067. DOI: 10.1016/j.ajhg.2023.06.002 PMID: 37352859

3. Tavtigian SV, Harrison SM et al. *Fitting a naturally scaled point system to the ACMG/AMP variant classification guidelines.* **Hum Mutat** (2020) 41(10):1734-1737. DOI: 10.1002/humu.24088 PMID: 32720330

4. ClinGen SVI Proposal for De Novo Criteria (PS2 & PM6) - Version 1.1. https://clinicalgenome.org/site/assets/files/3461/svi_proposal_for_de_novo_criteria_v1_1.pdf

5. Bellingham J, Davidson AE et al. *Investigation of Aberrant Splicing Induced by AIPL1 Variations as a Cause of Leber Congenital Amaurosis.* **Invest Ophthalmol Vis Sci** (2015) 56(13):7784-7793. DOI: 10.1167/iovs.15-18092 PMID: 26650897

6. Sacristán-Reviriego A, Le HM et al. *Clinical and functional analyses of AIPL1 variants reveal mechanisms of pathogenicity linked to different forms of retinal degeneration.* **Sci Rep** (2020) 10(1):17520. DOI: 10.1038/s41598-020-74516-9 PMID: 33067476

7. Sohocki MM, Bowne SJ et al. *Mutations in a new photoreceptor-pineal gene on 17p cause Leber congenital amaurosis.* **Nat Genet** (2000) 24(1):79-83. DOI: 10.1038/71732 PMID: 10615133

8. Gopalakrishna KN, Boyd K et al. *Aryl Hydrocarbon Receptor-interacting Protein-like 1 Is an Obligate Chaperone of Phosphodiesterase 6 and Is Assisted by the γ-Subunit of Its Client.* **J Biol Chem** (2016) 291(31):16282-91. DOI: 10.1074/jbc.M116.737593 PMID: 27268253

9. Sacristán-Reviriego A, Bellingham J et al. *The integrity and organization of the human AIPL1 functional domains is critical for its role as a HSP90-dependent co-chaperone for rod PDE6.* **Hum Mol Genet** (2017) 26(22):4465-4480. DOI: 10.1093/hmg/ddx334 PMID: 28973376

10. Hidalgo-de-Quintana J, Evans RJ et al. *The Leber congenital amaurosis protein AIPL1 functions as part of a chaperone heterocomplex.* **Invest Ophthalmol Vis Sci** (2008) 49(7):2878-87. DOI: 10.1167/iovs.07-1576 PMID: 18408180

11. van der Spuy J, Cheetham ME et al. *The Leber congenital amaurosis gene product AIPL1 is localized exclusively in rod photoreceptors of the adult human retina.* **J Biol Chem** (2004) 279(34):35534-40. DOI: 10.1074/jbc.M407871200 PMID: 15347646

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 9/26/2025 | Initial release |

---

*This document was compiled from ClinGen VCEP specifications for AIPL1 (Version 1.0.0) and ClinGen SVI recommendations. For the most current version, please refer to the ClinGen website.*
