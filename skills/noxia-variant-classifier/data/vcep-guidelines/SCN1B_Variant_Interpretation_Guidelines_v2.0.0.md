# ClinGen Epilepsy Sodium Channel VCEP Variant Interpretation Guidelines for SCN1B

**Version:** 2.0.0
**Released:** 1/7/2025
**Affiliation:** Epilepsy Sodium Channel VCEP
**Based on:** Richards et al., 2015 ACMG/AMP Guidelines

> **General Comments:** Please disregard the "Rules for Combining Criteria" section in the main specification PDF. Instead, refer to the points-based combining rules system described below.

> **Release Notes:** Release contains updates to transcript information and exon numbering.

---

## Gene Information

| Attribute | Value |
|-----------|-------|
| **Gene** | SCN1B (HGNC:10586) |
| **HGNC Name** | sodium voltage-gated channel beta subunit 1 |
| **Transcript** | NM_001037.4 |
| **Disease** | Generalized epilepsy with febrile seizures plus (GEFS+) (MONDO:0018214) — Autosomal dominant inheritance |
| **Disease** | Developmental and epileptic encephalopathy (DEE) (MONDO:0100062) — Autosomal recessive inheritance |

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
   - [BA1 - Allele Frequency >0.3%](#ba1---allele-frequency-03)
   - [BS1 - Frequency Greater Than Expected](#bs1---frequency-greater-than-expected)
   - [BS2 - Observed in Healthy Adult](#bs2---observed-in-healthy-adult)
   - [BS3 - Functional Studies (No Effect)](#bs3---functional-studies-no-effect)
   - [BS4 - Lack of Segregation](#bs4---lack-of-segregation)
   - [BP1-BP7 - Benign Supporting](#bp1-bp7---benign-supporting)
3. [Rules for Combining Criteria (Points-Based System)](#rules-for-combining-criteria-points-based-system)
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

**VCEP Specifications:**
- Most terminal codon expected to undergo NMD: **p.Thr204**
- For splice sites, this criterion should **not** be applied with PP3.
- For a full gene deletion, a pathogenic classification is warranted.
- Follow SVI guidance per workflow in Tayoun et al (2018), included as "PVS1 Decision Tree" (see [Appendix A](#appendix-a-pvs1-decision-tree)).

#### Strength Levels

| Strength | Criteria |
|----------|----------|
| **Very Strong** | Follow SVI guidance per PVS1 Decision Tree |
| **Strong** | Follow SVI guidance per PVS1 Decision Tree |
| **Moderate** | Follow SVI guidance per PVS1 Decision Tree |
| **Supporting** | Follow SVI guidance per PVS1 Decision Tree |

#### PVS1 Decision Tree Summary

**Nonsense or Frameshift:**

| Scenario | NMD Predicted (stop 5' of p.Thr204) | NMD NOT Predicted (stop 3' of p.Thr204) |
|----------|--------------------------------------|------------------------------------------|
| Exon present in biologically-relevant transcript (NM_001037.5) | PVS1 | — |
| Truncated/altered region critical to protein function | — | PVS1_Strong |
| Role of region unknown | — | PVS1_Moderate |
| LoF variants frequent in general population / exon absent | N/A | N/A |

**Splice Sites (GT-AG +/-1,2):**
- If PVS1 is applied for splice sites, PP3 should **not** be used in combination.

| Scenario | Strength |
|----------|----------|
| Exon skipping disrupts reading frame AND predicted NMD (stop 5' of p.Thr204) | PVS1 |
| Exon skipping disrupts reading frame AND NOT predicted NMD (stop 3' of p.Thr204), truncated/altered region critical | PVS1_Strong |
| Exon skipping disrupts reading frame AND NOT predicted NMD, role of region unknown, removes ≥10% protein (≥200 aa) | PVS1_Strong |
| Exon skipping disrupts reading frame AND NOT predicted NMD, role of region unknown, removes <10% protein (<200 aa) | PVS1_Moderate |
| Exon skipping preserves reading frame, exon present in biologically-relevant transcript, truncated/altered region critical | PVS1_Strong |
| Exon skipping preserves reading frame, exon present, removes ≥10% protein (≥200 aa) | PVS1_Strong |
| Exon skipping preserves reading frame, exon present, removes <10% protein (<200 aa) | PVS1_Moderate |

**Deletions (Single exon to full gene):**

| Scenario | Strength |
|----------|----------|
| Full gene deletion | PVS1 |
| Disrupts reading frame AND predicted NMD (stop 5' of p.Thr204) | PVS1 |
| Disrupts reading frame AND NOT predicted NMD, truncated/altered region critical | PVS1_Strong |
| Disrupts reading frame AND NOT predicted NMD, role unknown, removes ≥10% protein | PVS1_Strong |
| Disrupts reading frame AND NOT predicted NMD, role unknown, removes <10% protein | PVS1_Moderate |
| Preserves reading frame, truncated/altered region critical | PVS1_Strong |
| Preserves reading frame, removes ≥10% protein (≥200 aa) | PVS1_Strong |
| Preserves reading frame, removes <10% protein (<200 aa) | PVS1_Moderate |

**Duplications (≥1 exon, completely contained within gene):**

| Scenario | Strength |
|----------|----------|
| Proven in tandem, reading frame disrupted AND NMD predicted | PVS1 |
| Proven in tandem, no or unknown impact on reading frame/NMD | N/A |
| Presumed in tandem, reading frame presumed disrupted AND NMD predicted | PVS1_Strong |
| Proven NOT in tandem | N/A |

**Initiation Codon:**

| Scenario | Strength |
|----------|----------|
| Different functional transcript uses alternative start codon | PVS1_Supporting |
| No known alternative start codon, ≥1 P variant upstream of closest potential in-frame start codon | PVS1_Moderate |
| No known alternative start codon, no P variants upstream | N/A |

> **Notes:**
> - Biologically-relevant transcript: NM_001037.5 (MANE Select)
> - Truncated/altered region critical to protein function is defined as the presence of non-truncating, pathogenic (per these criteria) variants
> - All exons are out of frame

---

### PS1 - Same Amino Acid Change

**Original ACMG Summary:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change. Example: Val->Leu caused by either G>C or G>T in the same codon. Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | Same amino acid change as a previously established **Pathogenic** variant regardless of nucleotide change. Also applies to splice variants: same predicted impact on splicing as previously classified variant (see PS1 Splice Table below). |
| **Moderate** | Same amino acid change as a previously established **Likely Pathogenic** variant regardless of nucleotide change. Also applies to splice variants with same predicted splicing impact. |
| **Supporting** | Same predicted impact on splicing as previously classified variant (see PS1 Splice Table below). |

#### PS1 Splice Variant Table (Walker et al, 2023; PMID: 37352859)

PS1 can be applied at varying strengths for splice variants, in conjunction with either PP3 or PVS1. PS1 strength depends on location of the variant under assessment (VUA) relative to the +/-1,2 dinucleotide positions and the location of the previously classified variant.

| VUA Location | Baseline Code | Comparison Variant Position | PS1 with P Comparison | PS1 with LP Comparison |
|---|---|---|---|---|
| **Outside** splice donor/acceptor +/-1,2 | PP3 | Same nucleotide | PS1 | PS1_Moderate |
| **Outside** splice donor/acceptor +/-1,2 | PP3 | Within same splice donor/acceptor motif (including +/-1,2) | PS1_Moderate | PS1_Supporting |
| **At** splice donor/acceptor +/-1,2 | PVS1 | Within same splice donor/acceptor +/-1,2 dinucleotide | PS1_Supporting | N/A |
| **At** splice donor/acceptor +/-1,2 | PVS1 | Within same splice donor/acceptor region, but outside +/-1,2 | PS1_Supporting | PS1_Supporting |
| **At** splice donor/acceptor +/-1,2 | PVS1_Strong/Moderate/Supporting | Within same splice donor/acceptor +/-1,2 dinucleotide | PS1 | N/A |
| **At** splice donor/acceptor +/-1,2 | PVS1_Strong/Moderate/Supporting | Within same splice donor/acceptor motif, but outside +/-1,2 | PS1_Moderate | PS1_Supporting |

---

### PS2 - De Novo (Confirmed)

**Original ACMG Summary:** De novo (both maternity and paternity confirmed) in a patient with the disease and no family history. Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.

**VCEP Specifications:** Points-based system for each unrelated proband determined by phenotypic specificity. Points are summed across all unrelated probands.

#### PS2 Points Per Proband (Confirmed Parentage)

| Phenotype | Points per Proband |
|-----------|-------------------|
| Genetic Epilepsy with Febrile Seizures Plus (GEFS+) | 1 point |
| Other epilepsy types or syndromes, with or without associated neurodevelopmental features | 0.5 points |

#### PS2 Evidence Strength Thresholds

| Total Points | Strength Level |
|--------------|----------------|
| ≥ 0.5 | PS2_Supporting |
| ≥ 1.0 | PS2_Moderate |
| ≥ 2.0 | PS2 (Strong) |
| ≥ 4.0 | PS2_Very Strong |

---

### PS3 - Functional Studies

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product. Note: Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | Mouse knock-in model displays **spontaneous** seizures |
| **Moderate** | Heterologous expression with voltage clamping shows statistically significant difference over wildtype in at least one parameter (FENICS ontology); **OR** Mouse knock-in model displays **induced** seizures; **OR** Zebrafish knock-in model displays **spontaneous** seizures, evidenced by hyperexcitability through electrophysiology or calcium imaging-based studies |
| **Supporting** | Zebrafish knock-in model displays **induced** seizures, evidenced by hyperexcitability through electrophysiology or calcium imaging-based studies |

---

### PS4 - Prevalence in Affected

**Original ACMG Summary:** The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.

**VCEP Specifications:** Points-based system. Present in multiple unrelated patients with consistent phenotype. Points assigned per unrelated proband determined by phenotypic specificity.

#### PS4 Points Per Proband

| Phenotype | Points per Proband |
|-----------|-------------------|
| Genetic Epilepsy with Febrile Seizures Plus (GEFS+) | 1 point |
| Other epilepsy types or syndromes, with or without associated neurodevelopmental features | 0.5 points |

#### PS4 Evidence Strength Thresholds

| Total Points | Strength Level |
|--------------|----------------|
| 1–1.5 | PS4_Supporting |
| 2–3.5 | PS4_Moderate |
| 4–15.5 | PS4 (Strong) |
| ≥ 16 | PS4_Very Strong |

---

### PM1 - Mutational Hot Spot

**Original ACMG Summary:** Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.

**VCEP Specification:** ***Not Applicable***

> **Comments:** Currently, insufficient numbers of pathogenic variants have been reported in SCN1B to calculate "mutational hotspots". SCN1B does not belong to a gene family to utilize PERs.

---

### PM2 - Absent from Controls

**Original ACMG Summary:** Absent from controls (or at extremely low frequency if recessive) in population databases. Caveat: Population data for indels may be poorly called by next generation sequencing.

**VCEP Specification (Supporting only):**
- **≤1 allele** in population databases such as the Genome Aggregation Database (gnomAD), if a minimum of 10,000 alleles assessed.

---

### PM3 - In Trans with Pathogenic

**Original ACMG Summary:** For recessive disorders, detected in trans with a pathogenic variant. Note: This requires testing of parents (or offspring) to determine phase.

**VCEP Specifications:** Points-based system based on confirmation of phase and classification of other variant.

#### PM3 Point System (Per Proband)

| Classification/Zygosity of Other Variant | Confirmed in Trans | Phase Unknown |
|------------------------------------------|-------------------|---------------|
| Pathogenic variant | 1.0 | 0.5 |
| Likely Pathogenic variant | 1.0 | 0.25 |
| Homozygous occurrence (max 1.0 point) | 0.5 | 0.5 |
| VUS (confirmed in trans only) | 0.25 | 0 |

#### PM3 Evidence Strength Thresholds

| Total Points | Strength Level |
|--------------|----------------|
| 0.5 | PM3_Supporting |
| 1.0 | PM3 (Moderate) |
| 2.0 | PM3_Strong |
| 4.0 | PM3_Very Strong |

---

### PM4 - Protein Length Changes

**Original ACMG Summary:** Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Moderate** | Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants. (No change from ACMG) |

---

### PM5 - Novel Missense at Same Residue

**Original ACMG Summary:** Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before. Example: Arg156His is pathogenic; now you observe Arg156Cys. Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | ≥2 known **Pathogenic** variants at the same residue as the novel change |
| **Moderate** | Novel missense change at a residue where a different missense change determined to be **Pathogenic** has been seen before |
| **Supporting** | Novel missense change at a residue where a different missense change determined to be **Likely Pathogenic** has been seen before |

---

### PM6 - De Novo (Assumed)

**Original ACMG Summary:** Assumed de novo, but without confirmation of paternity and maternity.

**VCEP Specifications:** Points-based system for each unrelated proband determined by phenotypic specificity (same structure as PS2 but with halved point values reflecting unconfirmed parentage).

#### PM6 Points Per Proband (Unconfirmed Parentage)

| Phenotype | Points per Proband |
|-----------|-------------------|
| Genetic Epilepsy with Febrile Seizures Plus (GEFS+) | 0.5 points |
| Other epilepsy types or syndromes, with or without associated neurodevelopmental features | 0.25 points |

#### PM6 Evidence Strength Thresholds

| Total Points | Strength Level |
|--------------|----------------|
| ≥ 0.5 | PM6_Supporting |
| ≥ 1.0 | PM6_Moderate |
| ≥ 2.0 | PM6 (Strong) |
| ≥ 4.0 | PM6_Very Strong |

---

### PP1 - Co-segregation

**Original ACMG Summary:** Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease. Note: May be used as stronger evidence with increasing segregation data.

**VCEP Specifications:**

| Strength | AD (Autosomal Dominant) | AR (Autosomal Recessive) |
|----------|------------------------|--------------------------|
| **Supporting** | 3–4 independent meioses | 1 affected segregation |
| **Moderate** | 5–6 independent meioses | 2 affected segregations |
| **Strong** | ≥7 independent meioses | ≥3 affected segregations |

---

### PP2 - Missense in Constrained Gene

**Original ACMG Summary:** Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.

**VCEP Specification:** ***Not Applicable***

> **Comments:** Benign missense variants are common.

---

### PP3 - Computational Evidence

**Original ACMG Summary:** Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.). Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Moderate** | Follow ClinGen's recommendations (PMID: 36413997), using **REVEL** as the computational tool. Strength capped at Moderate. Limit the combination of PP3 and PM1 to reach no higher than Strong. |
| **Supporting** | Follow ClinGen's recommendations (PMID: 36413997), using **REVEL** as the computational tool. Strength capped at Moderate. Limit the combination of PP3 and PM1 to reach no higher than Strong. |

> **Note:** For splice site variants where PVS1 is applied, PP3 should **not** be used in combination.

---

### PP4 - Phenotype Specificity

**Original ACMG Summary:** Patient's phenotype or family history is highly specific for a disease with a single genetic etiology.

**VCEP Specification:** ***Not Applicable***

> **Comments:** Phenotypic specificity is incorporated into PS2, PM6, and PS4.

---

### PP5 - Reputable Source

**Original ACMG Summary:** Reputable source recently reports variant as pathogenic, but the evidence is not available to the laboratory to perform an independent evaluation.

**VCEP Specification:** ***Not Applicable***

> This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PMID: 29543229).

---

## Benign Criteria

### BA1 - Allele Frequency >0.3%

**Original ACMG Summary:** Allele frequency is above 5% in population databases.

**VCEP Specification (Stand Alone):**
- Allele frequency is above **0.3%** in gnomAD or other large population database
- Must be ≥5 alleles if a minimum of 10,000 alleles was assessed

---

### BS1 - Frequency Greater Than Expected

**Original ACMG Summary:** Allele frequency is greater than expected for disorder.

**VCEP Specification (Strong):**
- Allele frequency is above **0.01%** in gnomAD or other large population database
- Must be ≥5 alleles if a minimum of 10,000 alleles was assessed

---

### BS2 - Observed in Healthy Adult

**Original ACMG Summary:** Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

**VCEP Specification (Strong):**
- Observed in a healthy adult individual. (No change from ACMG)

---

### BS3 - Functional Studies (No Effect)

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

**VCEP Specification:** ***Not Applicable***

> **Comments:**
> - **Cellular electrophysiology (voltage clamp recording):** Values indicating "no impact on channel function" have not been sufficiently characterized to date. Additionally, one cannot exclude non-electrophysiological defects such as mis-localization in a neuron based solely on heterologous expression studies. This can be re-assessed by the EP over time and as benign variants are functionally characterized in the future.
> - **Animal Models:** Lack of an epilepsy phenotype in an animal model is insufficient to support benignity of a variant. Additionally, some non-epilepsy co-morbidities, such as behavioral characteristics that may mimic intellectual disability and/or autism spectrum disorder, are still being established and could support pathogenicity. This can be re-assessed by the EP over time.

---

### BS4 - Lack of Segregation

**Original ACMG Summary:** Lack of segregation in affected members of a family. Caveat: The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.

**VCEP Specification:** ***Not Applicable***

> **Comments:** Reduced penetrance, variable expressivity and phenocopies.

---

### BP1-BP7 - Benign Supporting

| Criterion | Status | Strength | Comment |
|-----------|--------|----------|---------|
| **BP1** | Not Applicable | — | Missense variants are a common cause of disease |
| **BP2** | Applicable | Supporting | Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder or observed in cis with a pathogenic variant in any inheritance pattern. (No change) |
| **BP3** | Applicable | Supporting | In-frame deletions/insertions in a repetitive region without a known function. (No change) |
| **BP4** | Applicable | Moderate / Supporting | Follow ClinGen's recommendations (PMID: 36413997), using REVEL as the computational tool |
| **BP5** | Applicable | Supporting | Variant found in a case with an alternate molecular basis for disease. (No change) |
| **BP6** | Not Applicable | — | Not for use per ClinGen SVI VCEP Review Committee (PMID: 29543229) |
| **BP7** | Applicable | Supporting | A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved. (No change) |

---

## Rules for Combining Criteria (Points-Based System)

This VCEP uses a **points-based combining system** based on Tavtigian et al, 2018, in conjunction with forthcoming points-based guidance.

### Points Per Criterion Strength

| Criterion Strength | Points |
|-------------------|--------|
| P – Very Strong | 8 |
| P – Strong | 4 |
| P – Moderate | 2 |
| P – Supporting | 1 |
| B – Supporting | -1 |
| B – Strong | -4 |

### Classification Thresholds

| Total Points | Classification | Posterior Probability |
|--------------|---------------|---------------------|
| ≥ 10 | **Pathogenic** | ≥ 0.99 |
| 6–9 | **Likely Pathogenic** | ≥ 0.9 to < 0.99 |
| 0–5 | **VUS** | ≥ 0.10 to < 0.9 |
| -6 to -1 | **Likely Benign** | ≥ 0.001, < 0.1 |
| ≤ -7 | **Benign** | < 0.001 |

### Additional Caveats

- PP3 + PM1 combined can reach **no higher than Strong**
- When PM5_Strong is reached, **do not combine PM1 to PM5**

### Legacy Combining Rules (for reference)

#### Pathogenic Classification

| Criteria Combination | Applicable Criteria |
|---------------------|-------------------|
| 1 Very Strong **AND** ≥1 Strong | Very Strong: PVS1, PS2_VeryStrong, PS4_VeryStrong, PM3_VeryStrong; Strong: PVS1_Strong, PS1, PS2, PS3, PS4, PM3_Strong, PM5_Strong, PM6_Strong, PP1_Strong, PP3_Strong |
| 1 Very Strong **AND** ≥2 Moderate | Moderate: PVS1_Moderate, PS1_Moderate, PS2_Moderate, PS3_Moderate, PS4_Moderate, PM3, PM4, PM5, PM6, PP1_Moderate, PP3_Moderate |
| 1 Very Strong **AND** 1 Moderate **AND** 1 Supporting | Supporting: PVS1_Supporting, PS2_Supporting, PS3_Supporting, PS4_Supporting, PM2_Supporting, PM3_Supporting, PM5_Supporting, PM6_Supporting, PP1, PP3 |
| 1 Very Strong **AND** ≥2 Supporting | — |
| ≥2 Strong | — |
| 1 Strong **AND** ≥3 Moderate | — |
| 1 Strong **AND** 2 Moderate **AND** ≥2 Supporting | — |
| 1 Strong **AND** 1 Moderate **AND** ≥4 Supporting | — |

#### Likely Pathogenic Classification

| Criteria Combination |
|---------------------|
| 1 Very Strong **AND** 1 Moderate |

#### Benign Classification

| Criteria Combination |
|---------------------|
| ≥2 Strong (BS1, BS2) |
| 1 Stand Alone (BA1) |

#### Likely Benign Classification

| Criteria Combination |
|---------------------|
| 1 Strong (BS1, BS2) **AND** 1 Supporting (BP2, BP3, BP5, BP7) |
| ≥2 Supporting (BP2, BP3, BP5, BP7) |

---

## Appendices

### Appendix A: PVS1 Decision Tree

The PVS1 decision tree for SCN1B follows the SVI guidance per Tayoun et al (2018) with the following gene-specific parameters:

- **Biologically-relevant transcript:** NM_001037.5 (MANE Select)
- **Most terminal codon expected to undergo NMD:** p.Thr204
- **Truncated/altered region critical to protein function** is defined as the presence of non-truncating, pathogenic (per these criteria) variants
- **All exons are out of frame**

#### Variant Types Covered:
1. Nonsense or Frameshift
2. Splice site variants (GT-AG +/-1,2)
3. Deletions (single exon to full gene)
4. Duplications (≥1 exon, completely contained within gene)
5. Initiation codon variants

See the detailed decision tree tables in the [PVS1 section](#pvs1---null-variant) above.

---

### Appendix B: SCN1B Exon Numbering (NM_001037.5)

| Exon | Coding Exon | Start Phase | Stop Phase | Frame |
|------|-------------|-------------|------------|-------|
| 1 | 1 | 1 | 0 | OUT |
| 2 | 2 | 1 | 0 | OUT |
| 3 | 3 | 0 | 1 | OUT |
| 4 | 4 | 1 | 2 | OUT |
| 5 | 5 | 2 | -1 | OUT |
| 6 | — | untranslated | — | — |

> **Note:** All coding exons are out of frame.

---

### Appendix C: Population Frequency Thresholds Summary

| Criterion | Threshold | Strength | Additional Requirement |
|-----------|-----------|----------|----------------------|
| BA1 | >0.3% | Stand Alone | ≥5 alleles, minimum 10,000 alleles assessed |
| BS1 | >0.01% | Strong | ≥5 alleles, minimum 10,000 alleles assessed |
| PM2 | ≤1 allele | Supporting | Minimum 10,000 alleles assessed |

---

### Appendix D: Criteria Applicability Summary

| Criterion | Status | Max Strength | Modification Type |
|-----------|--------|-------------|-------------------|
| PVS1 | Applicable | Very Strong | General recommendation |
| PS1 | Applicable | Strong | Gene-specific |
| PS2 | Applicable | Very Strong | Disease-specific, Strength |
| PS3 | Applicable | Strong | Disease-specific, Gene-specific |
| PS4 | Applicable | Very Strong | Disease-specific, Gene-specific, Strength |
| PM1 | **Not Applicable** | — | — |
| PM2 | Applicable | Supporting | General recommendation |
| PM3 | Applicable | Very Strong | General recommendation |
| PM4 | Applicable | Moderate | No change |
| PM5 | Applicable | Strong | Disease-specific, Gene-specific, Strength |
| PM6 | Applicable | Very Strong | Disease-specific, Strength |
| PP1 | Applicable | Strong | Strength |
| PP2 | **Not Applicable** | — | — |
| PP3 | Applicable | Moderate | General recommendation, Strength |
| PP4 | **Not Applicable** | — | Incorporated into PS2, PM6, PS4 |
| PP5 | **Not Applicable** | — | Per ClinGen SVI (PMID: 29543229) |
| BA1 | Applicable | Stand Alone | Disease-specific |
| BS1 | Applicable | Strong | Disease-specific |
| BS2 | Applicable | Strong | No change |
| BS3 | **Not Applicable** | — | — |
| BS4 | **Not Applicable** | — | — |
| BP1 | **Not Applicable** | — | — |
| BP2 | Applicable | Supporting | No change |
| BP3 | Applicable | Supporting | No change |
| BP4 | Applicable | Moderate | General recommendation |
| BP5 | Applicable | Supporting | No change |
| BP6 | **Not Applicable** | — | Per ClinGen SVI (PMID: 29543229) |
| BP7 | Applicable | Supporting | No change |

---

### Appendix E: Reference PMIDs

| PMID | Reference |
|------|-----------|
| 29543229 | ClinGen SVI recommendation against use of PP5/BP6 |
| 36413997 | ClinGen recommendations for computational evidence (PP3/BP4) using REVEL |
| 37352859 | Walker et al, 2023. PS1 code weights for variants impacting splicing |
| — | Tayoun et al, 2018. PVS1 Decision Tree / SVI guidance |
| — | Tavtigian et al, 2018. Points-based combining rules |

---

## Version History

| Version | Date | Notes |
|---------|------|-------|
| 2.0.0 | 1/7/2025 | Release contains updates to transcript information and exon numbering. Points-based combining rules system incorporated. |

---

*This document was compiled from ClinGen Epilepsy Sodium Channel VCEP specifications for SCN1B v2.0.0 and ClinGen SVI recommendations. For the most current version, please refer to the ClinGen website.*
