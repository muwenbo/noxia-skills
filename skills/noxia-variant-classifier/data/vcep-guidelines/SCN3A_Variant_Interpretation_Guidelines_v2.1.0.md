# ClinGen Epilepsy Sodium Channel VCEP Variant Interpretation Guidelines for SCN3A

**Version:** 2.1.0
**Released:** 4/28/2025
**Affiliation:** Epilepsy Sodium Channel VCEP
**Based on:** Richards et al., 2015 ACMG/AMP Guidelines

> **Important:** For combining criteria, use the points-based system described in [Rules for Combining Criteria](#rules-for-combining-criteria), not the standard ACMG combining rules table on the ClinGen specification page.

---

## Gene Information

| Attribute | Value |
|-----------|-------|
| **Gene** | SCN3A (HGNC:10590) |
| **HGNC Name** | Sodium voltage-gated channel alpha subunit 3 |
| **Transcript** | NM_006922.3 (MANE Select: NM_006922.4) |
| **Disease** | Developmental and epileptic encephalopathy (MONDO:0100062) |
| **Inheritance** | Autosomal dominant inheritance |

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
   - [BA1 - Allele Frequency >0.01%](#ba1---allele-frequency-001)
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

**VCEP Specifications:**
- Most terminal codon expected to undergo NMD: **p.Thr1586**
- For splice site variants, PVS1 should **not** be applied in combination with PP3
- For a full gene deletion, a **Pathogenic** classification is warranted
- Follow SVI guidance per workflow in Tayoun et al (2018) — see [Appendix A: PVS1 Decision Tree](#appendix-a-pvs1-decision-tree)

#### Strength Levels

| Strength | Criteria |
|----------|----------|
| **Very Strong** | Follow SVI PVS1 decision tree. Nonsense/frameshift predicted to undergo NMD (stop codon 5' of p.Thr1586) in biologically-relevant transcript (NM_006922.4), where exon is present and region is critical to protein function. Canonical ±1,2 splice sites where exon skipping disrupts reading frame and triggers NMD. Single/multi-exon deletion disrupting reading frame with NMD. Full gene deletion. |
| **Strong** | Nonsense/frameshift not predicted to undergo NMD but truncated region is critical to protein function OR variant removes ≥10% of protein (≥200 aa). Splice variants where exon skipping preserves reading frame but truncated/altered region is critical to protein function. In-tandem presumed duplication disrupting reading frame with NMD predicted. |
| **Moderate** | Nonsense/frameshift not predicted to undergo NMD, role of region in protein function is unknown, and variant removes ≥10% of protein (≥200 aa). Initiation codon variant with no known alternative start codon and ≥1 pathogenic variant upstream of closest potential in-frame start codon. |
| **Supporting** | Initiation codon variant where a different functional transcript uses an alternative start codon. |

---

### PS1 - Same Amino Acid Change

**Original ACMG Summary:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.

**VCEP Specifications:**

The paralogous sodium channel genes associated with neurodevelopmental disorders (SCN1A, SCN2A, SCN3A, SCN8A) share >77% sequence identity (PMID:33531663). The four homologous domains with voltage sensor and pore region remain largely preserved across the channels. When terminal regions and cytoplasmic loops are excluded, homology increases to >90% (PMID:33531663; PMID:16382098).

As such, **Pathogenic and Likely Pathogenic variants in paralogous genes can be considered for PS1.** See [Appendix D: Paralogous Gene Table](#appendix-d-paralogous-gene-table).

PS1 can also be applied for **splice variants** at varying strengths, in conjunction with either PP3 or PVS1. See [Appendix E: PS1 Splice Variant Table](#appendix-e-ps1-splice-variant-table).

| Strength | Criteria |
|----------|----------|
| **Strong** | Same amino acid change as a previously established **Pathogenic** variant regardless of nucleotide change. **OR** >1 identical amino acid change in paralogous gene (SCN1A, SCN2A, SCN3A, SCN8A) previously established as Pathogenic or Likely Pathogenic. **OR** Same predicted impact on splicing as previously classified Pathogenic variant (per Walker et al, 2023 Table 2). |
| **Moderate** | Same amino acid change as a previously established **Likely Pathogenic** variant regardless of nucleotide change. **OR** Same predicted impact on splicing as previously classified variant (per Walker et al, 2023 Table 2). |
| **Supporting** | A single identical amino acid change in a paralogous gene (SCN1A, SCN2A, SCN3A, SCN8A) previously established as Pathogenic or Likely Pathogenic. **OR** Same predicted impact on splicing as previously classified variant (per Walker et al, 2023 Table 2). |

> **Caveat:** Beware of changes that impact splicing rather than at the amino acid/protein level.

---

### PS2 - De Novo (Confirmed)

**Original ACMG Summary:** De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.

**VCEP Specifications:** Points-based system for each unrelated proband, determined by phenotypic specificity. Both maternity and paternity must be confirmed.

> **Note:** Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.

#### PS2 Point System (Per Confirmed De Novo Proband)

| Phenotype | Points per Proband |
|-----------|-------------------|
| Developmental and Epileptic Encephalopathy | **1 point** |
| Other phenotypes not consistent with neurodevelopmental disorder | **0 points** |

#### PS2 Evidence Strength Thresholds

| Total Points | Strength Level |
|--------------|----------------|
| ≥0.5 | PS2_Supporting |
| ≥1.0 | PS2_Moderate |
| ≥2.0 | PS2_Strong |
| ≥4.0 | PS2_Very Strong |

---

### PS3 - Functional Studies

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.

**VCEP Specifications:**
- If a variant shows differences from wildtype at **multiple strength levels** (e.g., strong-level evidence in peak current and moderate-level evidence in persistent current), use the **highest** level of evidence (capping at Strong).
- If a variant has been studied in **multiple publications**, use the strongest level of evidence available.

| Strength | Criteria |
|----------|----------|
| **Strong** | **Patch clamping:** Peak current ≤72.7% of wildtype, **OR** persistent current ≥135% of wildtype, **OR** voltage dependence of activation shifted by ≥2.2 mV (absolute value), **OR** voltage dependence of inactivation shifted by ≥4.1 mV (absolute value). **Mouse model:** Knock-in displays spontaneous seizures. |
| **Moderate** | **Patch clamping:** Peak current ≤80.6% of wildtype, **OR** persistent current ≥125% of wildtype, **OR** voltage dependence of activation shifted by ≥2.1 mV (absolute value), **OR** voltage dependence of inactivation shifted by ≥3.0 mV (absolute value). **Mouse model:** Knock-in displays induced seizures. **Zebrafish model:** Knock-in displays spontaneous seizures evidenced by hyperexcitability through electrophysiology or calcium imaging. |
| **Supporting** | **Zebrafish model:** Knock-in displays induced seizures evidenced by hyperexcitability through electrophysiology or calcium imaging. |

#### PS3 Functional Assay Thresholds Summary

| Assay Parameter | Strong (PS3) | Moderate (PS3_Moderate) |
|-----------------|-------------|------------------------|
| Peak current (% of WT) | ≤72.7% | ≤80.6% |
| Persistent current (% of WT) | ≥135% | ≥125% |
| V½ activation shift (mV, absolute) | ≥2.2 | ≥2.1 |
| V½ inactivation shift (mV, absolute) | ≥4.1 | ≥3.0 |

> All electrophysiology parameters are as defined by the FENICS ontology (https://bioportal.bioontology.org/ontologies/FENICS).

---

### PS4 - Prevalence in Affected

**Original ACMG Summary:** The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.

**VCEP Specifications:** Points-based system for each unrelated proband, determined by phenotypic specificity.

| Phenotype | Points per Proband |
|-----------|-------------------|
| Developmental and Epileptic Encephalopathy | **1 point** |
| Other phenotypes not consistent with neurodevelopmental disorder | **0 points** |

#### PS4 Evidence Strength Thresholds

| Total Points | Strength Level |
|--------------|----------------|
| 1–1.5 | PS4_Supporting |
| 2–3.5 | PS4_Moderate |
| 4–15.5 | PS4_Strong |
| ≥16 | PS4_Very Strong |

---

### PM1 - Mutational Hot Spot

**Original ACMG Summary:** Located in a mutational hot spot and/or critical and well-established functional domain without benign variation.

**VCEP Specifications:**

Pathogenic Enriched Regions (PERs) are regions enriched for Pathogenic variants (ClinVar/HGMD) across gene families and lacking population (gnomAD) variants (Pérez-Palma, 2020 PMID:31871067; Lal et al, 2020 PMID:32183904).

| Strength | Criteria |
|----------|----------|
| **Moderate** | Variant is located within a Pathogenic Enriched Region. See PM1 Table below. |

> **Rule Combining Stipulation:**
> - PP3 + PM1 combined can reach **no higher than Strong**
> - When PM5_Strong is reached, do **not** combine PM1 with PM5

#### PM1 Pathogenic Enriched Regions (SCN3A)

| PER # | SCN3A Residues | # Residues |
|-------|---------------|------------|
| 1 | 212–230 | 19 |
| 2 | 247–255 | 9 |
| 3 | 412–425 | 14 |
| 4 | 851–859 | 9 |
| 5 | 871–879 | 9 |
| 6 | 881–894 | 14 |
| 7 | 896–904 | 9 |
| 8 | 923–931 | 9 |
| 9 | 971–989 | 19 |
| 10 | 1309–1352 | 44 |
| 11 | 1453–1461 | 9 |
| 12 | 1463–1476 | 14 |
| 13 | 1478–1496 | 19 |
| 14 | 1616–1634 | 19 |
| 15 | 1641–1659 | 19 |
| 16 | 1756–1769 | 14 |

> See attached "PM1 Table" for corresponding residue positions in paralogous genes (SCN1A, SCN2A, SCN8A).

---

### PM2 - Absent from Controls

**Original ACMG Summary:** Absent from controls (or at extremely low frequency if recessive) in population databases.

**VCEP Specification (Supporting only):**
- **≤1 allele** in population databases (e.g., gnomAD), if a minimum of 10,000 alleles assessed
- Caveat: Population data for indels may be poorly called by next generation sequencing

---

### PM3 - In Trans with Pathogenic

**Original ACMG Summary:** For recessive disorders, detected in trans with a pathogenic variant.

**VCEP Specifications:** **Not Applicable** — SCN3A is associated with autosomal dominant inheritance.

---

### PM4 - Protein Length Changes

**Original ACMG Summary:** Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

| Strength | Criteria |
|----------|----------|
| **Moderate** | Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants. (No change from original ACMG.) |

---

### PM5 - Novel Missense at Same Residue

**Original ACMG Summary:** Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.

**VCEP Specifications:**

The paralogous sodium channel genes (SCN1A, SCN2A, SCN3A, SCN8A) share >77% sequence identity. Pathogenic and Likely Pathogenic variants in paralogous genes can be considered for PM5. See [Appendix D: Paralogous Gene Table](#appendix-d-paralogous-gene-table).

> **Rule Combining Stipulation:** If PM5_Strong is reached, and the variant falls within a PM1 region, then do **not** add PM1 with PM5_Strong.

| Strength | Criteria |
|----------|----------|
| **Strong** | ≥2 known Pathogenic variants at the same site as the novel change (within the same gene). |
| **Moderate** | Novel missense change at an amino acid residue where a different missense change determined to be **Pathogenic** has been seen before. |
| **Supporting** | Novel missense change at an amino acid residue where a different missense change determined to be **Likely Pathogenic** has been seen before. **OR** >1 non-identical amino acid change in paralogous gene(s) (SCN1A, SCN2A, SCN3A, SCN8A) where a different missense change determined to be Pathogenic or Likely Pathogenic. |

> **Caveat:** Beware of changes that impact splicing rather than at the amino acid/protein level.

---

### PM6 - De Novo (Assumed)

**Original ACMG Summary:** Assumed de novo, but without confirmation of paternity and maternity.

**VCEP Specifications:** Points-based system (same structure as PS2 but with half points since parental relationships are unconfirmed).

#### PM6 Point System (Per Assumed De Novo Proband)

| Phenotype | Points per Proband |
|-----------|-------------------|
| Developmental and Epileptic Encephalopathy | **0.5 points** |
| Other phenotypes not consistent with neurodevelopmental disorder | **0 points** |

#### PM6 Evidence Strength Thresholds

| Total Points | Strength Level |
|--------------|----------------|
| ≥0.5 | PM6_Supporting |
| ≥1.0 | PM6_Moderate |
| ≥2.0 | PM6_Strong |
| ≥4.0 | PM6_Very Strong |

> **Note:** PS2 and PM6 points can be summed together to reach the appropriate strength level.

---

### PP1 - Co-segregation

**Original ACMG Summary:** Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.

**VCEP Specifications:**

| Strength | Meioses Required |
|----------|-----------------|
| **Supporting** | 3–4 independent meioses |
| **Moderate** | 5–6 independent meioses |
| **Strong** | ≥7 independent meioses |

---

### PP2 - Missense in Constrained Gene

**Original ACMG Summary:** Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.

**VCEP Specifications:** **Not Applicable** — Benign missense variants are common.

---

### PP3 - Computational Evidence

**Original ACMG Summary:** Multiple lines of computational evidence support a deleterious effect on the gene or gene product.

**VCEP Specifications:**

Follow ClinGen's recommendations (PMID:36413997), using **REVEL** as the computational tool.

| Strength | Criteria |
|----------|----------|
| **Moderate** | REVEL score meets the moderate threshold per ClinGen SVI recommendations (PMID:36413997). |
| **Supporting** | REVEL score meets the supporting threshold per ClinGen SVI recommendations (PMID:36413997). |

> **Stipulations:**
> 1. Strength should be **capped at Moderate**
> 2. Limit the combination of PP3 and PM1 to reach **no higher than Strong**
> 3. For splice site variants, PP3 should **not** be combined with PVS1

---

### PP4 - Phenotype Specificity

**Original ACMG Summary:** Patient's phenotype or family history is highly specific for a disease with a single genetic etiology.

**VCEP Specifications:** **Not Applicable** — Phenotypic specificity is incorporated into PS2, PM6, and PS4 point systems.

---

### PP5 - Reputable Source

**Original ACMG Summary:** Reputable source recently reports variant as pathogenic, but the evidence is not available to the laboratory to perform an independent evaluation.

**VCEP Specifications:** **Not Applicable** — This criterion is not for use as recommended by the ClinGen SVI VCEP Review Committee (PMID:29543229).

---

## Benign Criteria

### BA1 - Allele Frequency >0.01%

**Original ACMG Summary:** Allele frequency is above 5% in population databases.

**VCEP Specification (Stand Alone):**
- Allele frequency is above **0.01%** (0.0001) in gnomAD or other large population databases
- Must be ≥5 alleles if a minimum of 10,000 alleles was assessed

---

### BS1 - Frequency Greater Than Expected

**Original ACMG Summary:** Allele frequency is greater than expected for disorder.

**VCEP Specification (Strong):**
- Allele frequency is above **0.0002%** (0.000002) in gnomAD or other large population databases
- Must be ≥5 alleles if a minimum of 10,000 alleles was assessed

---

### BS2 - Observed in Healthy Adult

**Original ACMG Summary:** Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

**VCEP Specification (Strong):**
- Observed in a healthy adult individual. (No change from original ACMG.)

---

### BS3 - Functional Studies (No Effect)

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

**VCEP Specifications:** **Not Applicable**

> **Rationale:**
> - **Cellular electrophysiology (voltage clamp recording):** Values indicating "no impact on channel function" have not been sufficiently characterized to date. Additionally, one cannot exclude non-electrophysiological defects such as mis-localization in a neuron based solely on heterologous expression studies. This can be re-assessed over time as benign variants are functionally characterized.
> - **Animal models:** Lack of an epilepsy phenotype in an animal model is insufficient to support benignity. Some non-epilepsy co-morbidities (behavioral characteristics mimicking intellectual disability and/or autism spectrum disorder) are still being established and could support pathogenicity. This can be re-assessed over time.

---

### BS4 - Lack of Segregation

**Original ACMG Summary:** Lack of segregation in affected members of a family.

**VCEP Specifications:** **Not Applicable** — Reduced penetrance and phenocopies preclude the use of this criterion.

---

### BP1-BP7 - Benign Supporting

| Criterion | Status | Comment |
|-----------|--------|---------|
| **BP1** | Not Applicable | Missense variants are a common cause of disease |
| **BP2** | Applicable (Supporting) | Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder or observed in cis with a pathogenic variant in any inheritance pattern. No change. |
| **BP3** | Applicable (Supporting) | In-frame deletions/insertions in a repetitive region without a known function. No change. |
| **BP4** | Applicable (Supporting/Moderate) | Follow ClinGen's recommendations (PMID:36413997) using REVEL as the computational tool. |
| **BP5** | Applicable (Supporting) | Variant found in a case with an alternate molecular basis for disease. No change. |
| **BP6** | Not Applicable | Not for use per ClinGen SVI VCEP Review Committee (PMID:29543229) |
| **BP7** | Applicable (Supporting) | A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved. No change. |

---

## Rules for Combining Criteria

> **This VCEP uses a points-based system** based on Tavtigian et al, 2018 in conjunction with forthcoming points-based guidance.

### Points per Criterion

| Evidence Category | Points |
|-------------------|--------|
| Pathogenic Very Strong | **8** |
| Pathogenic Strong | **4** |
| Pathogenic Moderate | **2** |
| Pathogenic Supporting | **1** |
| Benign Supporting | **-1** |
| Benign Strong | **-4** |

### Classification Based on Total Points

| Total Points | Classification | Posterior Probability |
|--------------|----------------|---------------------|
| ≥10 | **Pathogenic** | ≥0.99 |
| 6–9 | **Likely Pathogenic** | ≥0.9 to <0.99 |
| 0–5 | **VUS** | ≥0.10 to <0.9 |
| -6 to -1 | **Likely Benign** | ≥0.001 to <0.1 |
| ≤-7 | **Benign** | <0.001 |

### Benign Stand-Alone

BA1 is applied as a **stand-alone** criterion — if BA1 is met, the variant is classified as **Benign** regardless of other criteria.

### Additional Combining Caveats

- **PP3 + PM1** combined can reach **no higher than Strong**
- When **PM5_Strong** is reached, do **not** combine PM1 with PM5

### Applicable Criteria at Each Strength Level

| Strength | Applicable Criteria |
|----------|-------------------|
| **Very Strong (8 pts)** | PVS1, PS2_VeryStrong, PS4_VeryStrong |
| **Strong (4 pts)** | PVS1_Strong, PS1, PS2, PS3, PS4, PM5_Strong, PM6_Strong, PP1_Strong, PP3_Strong |
| **Moderate (2 pts)** | PVS1_Moderate, PS1_Moderate, PS2_Moderate, PS3_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate, PP3_Moderate |
| **Supporting (1 pt)** | PVS1_Supporting, PS2_Supporting, PS3_Supporting, PS4_Supporting, PM2_Supporting, PM5_Supporting, PM6_Supporting, PP1, PP3 |
| **B-Supporting (-1 pt)** | BP2, BP3, BP4, BP5, BP7 |
| **B-Strong (-4 pts)** | BS1, BS2 |
| **Stand Alone** | BA1 |

---

## Appendices

### Appendix A: PVS1 Decision Tree

The PVS1 decision tree follows SVI guidance per Tayoun et al (2018), with SCN3A-specific parameters:

- **Biologically-relevant transcript:** NM_006922.4 (MANE Select)
- **Most terminal codon for NMD:** p.Thr1586
- **Truncated/altered region critical to protein function** defined as:
  - (a) Presence of non-truncating pathogenic (per these criteria) variants, OR
  - (b) Located within a Pathogenic Enriched Region defined by PM1

#### Variant Types and PVS1 Strength

**Nonsense or Frameshift:**
- Predicted to undergo NMD (stop codon 5' of p.Thr1586) → **PVS1**
- Not predicted to undergo NMD (stop codon 3' of p.Thr1586):
  - Truncated region is critical to protein function → **PVS1_Strong**
  - Role of region unknown + removes ≥10% protein (≥200 aa) → **PVS1_Strong**
  - Role of region unknown + removes <10% protein (<200 aa) → **PVS1_Moderate**

**Canonical ±1,2 Splice Sites** (if applied, PP3 not to be used in combination):
- Exon skipping disrupts reading frame + NMD predicted → **PVS1**
- Exon skipping disrupts reading frame + NMD NOT predicted:
  - Truncated region is critical → **PVS1_Strong**
  - Removes ≥10% protein → **PVS1_Strong**
  - Removes <10% protein → **PVS1_Moderate**
- Exon skipping preserves reading frame:
  - Truncated/altered region is critical → **PVS1_Strong**
  - Removes ≥10% protein → **PVS1_Strong**
  - Removes <10% protein → **PVS1_Moderate**
- LoF variants in exon frequent in general population / exon absent from biologically-relevant transcript → **N/A**

**Deletion (Single exon to full gene):**
- Full gene deletion → **PVS1** (Pathogenic classification warranted)
- Disrupts reading frame + NMD predicted → **PVS1**
- Disrupts reading frame + NMD NOT predicted → same as nonsense/frameshift rules above
- Preserves reading frame:
  - Truncated/altered region is critical → **PVS1_Strong**
  - Removes ≥10% protein → **PVS1_Strong**
  - Removes <10% protein → **PVS1_Moderate**

**Duplication (≥1 exon, completely contained within gene):**
- Proven in tandem + reading frame disrupted + NMD predicted → **PVS1**
- Proven in tandem + no/unknown impact on reading frame → **N/A**
- Presumed in tandem + reading frame presumed disrupted + NMD predicted → **PVS1_Strong**
- Proven NOT in tandem → **N/A**

**Initiation Codon:**
- Different functional transcript uses alternative start codon → **PVS1_Supporting**
- No known alternative start codon:
  - ≥1 pathogenic variant upstream of closest potential in-frame start codon → **PVS1_Moderate**
  - No pathogenic variant upstream → **N/A**

#### Exon Frame Information (SCN3A, NM_006922.4)

| Exon | Coding Exon | Start Phase | Stop Phase | Frame |
|------|------------|-------------|------------|-------|
| 1 | - | untranslated | | |
| 2 | - | untranslated | | |
| 3 | 1 | 0 | 0 | IN |
| 4 | 2 | 0 | 2 | OUT |
| 5 | 3 | 2 | 2 | IN |
| 6 | 4 | 2 | 2 | IN |
| 7 | 5 | 2 | 1 | OUT |
| 8 | 6 | 1 | 1 | IN |
| 9 | 7 | 1 | 2 | OUT |
| 10 | 8 | 2 | 0 | OUT |
| 11 | 9 | 0 | 0 | IN |
| 12 | 10 | 0 | 0 | IN |
| 13 | 11 | 0 | 0 | IN |
| 14 | 12 | 0 | 1 | OUT |
| 15 | 13 | 1 | 0 | OUT |
| 16 | 14 | 0 | 0 | IN |
| 17 | 15 | 0 | 0 | IN |
| 18 | 16 | 0 | 0 | IN |
| 19 | 17 | 0 | 1 | OUT |
| 20 | 18 | 1 | 0 | OUT |
| 21 | 19 | 0 | 0 | IN |
| 22 | 20 | 0 | 0 | IN |
| 23 | 21 | 0 | 0 | IN |
| 24 | 22 | 0 | 0 | IN |
| 25 | 23 | 0 | 0 | IN |
| 26 | 24 | 0 | 0 | IN |
| 27 | 25 | 0 | 1 | OUT |
| 28 | 26 | 1 | X | OUT |

- **In-frame coding exons:** 1, 3, 4, 6, 9, 10, 11, 14, 15, 16, 19, 20, 21, 22, 23, 24
- **Out-of-frame coding exons:** 2, 5, 7, 8, 12, 13, 17, 18, 25, 26

---

### Appendix B: Reference PMIDs

| PMID | Reference |
|------|-----------|
| 33531663 | Paralogous sodium channel gene sequence identity (SCN1A/2A/3A/8A) |
| 16382098 | Sodium channel gene homology analysis |
| 31871067 | Pérez-Palma et al, 2020 — Pathogenic Enriched Regions (PERs) |
| 32183904 | Lal et al, 2020 — PERs across gene families |
| 37352859 | Walker et al, 2023 — PS1 splice variant guidance (Table 2) |
| 36413997 | ClinGen SVI computational tool recommendations (REVEL) |
| 29543229 | ClinGen SVI — PP5/BP6 not for use recommendation |

---

### Appendix C: Population Frequency Thresholds Summary

| Criterion | Threshold | Strength | Additional Requirement |
|-----------|-----------|----------|----------------------|
| BA1 | >0.01% (0.0001) | Stand Alone | ≥5 alleles if ≥10,000 alleles assessed |
| BS1 | >0.0002% (0.000002) | Strong | ≥5 alleles if ≥10,000 alleles assessed |
| PM2 | ≤1 allele | Supporting | Minimum of 10,000 alleles assessed |

---

### Appendix D: Paralogous Gene Table

Corresponding amino acid positions across paralogous sodium channel genes (SCN1A, SCN2A, SCN3A, SCN8A). Used for PS1 and PM5 criteria.

<details>
<summary>Click to expand PM1 PER residue mapping across paralogous genes</summary>

| PER # | SCN1A | SCN2A | SCN3A | SCN8A |
|-------|-------|-------|-------|-------|
| 1 | 212–230 | 213–231 | 212–230 | 216–234 |
| 2 | 247–255 | 248–256 | 247–255 | 251–259 |
| 3 | 411–424 | 413–426 | 412–425 | 399–412 |
| 4 | 859–867 | 850–858 | 851–859 | 844–852 |
| 5 | 879–887 | 870–878 | 871–879 | 864–872 |
| 6 | 889–902 | 880–893 | 881–894 | 874–887 |
| 7 | 904–912 | 895–903 | 896–904 | 889–897 |
| 8 | 931–939 | 922–930 | 923–931 | 916–924 |
| 9 | 979–997 | 970–988 | 971–989 | 964–982 |
| 10 | 1321–1364 | 1311–1354 | 1309–1352 | 1301–1344 |
| 11 | 1468–1476 | 1458–1466 | 1453–1461 | 1449–1457 |
| 12 | 1478–1491 | 1468–1481 | 1463–1476 | 1459–1472 |
| 13 | 1493–1511 | 1483–1501 | 1478–1496 | 1474–1492 |
| 14 | 1631–1649 | 1621–1639 | 1616–1634 | 1612–1630 |
| 15 | 1656–1674 | 1646–1664 | 1641–1659 | 1637–1655 |
| 16 | 1771–1784 | 1761–1774 | 1756–1769 | 1751–1764 |

</details>

> The full Paralogous Gene Table with amino acid-level mapping for the entire protein is available as a supplementary Excel file.

---

### Appendix E: PS1 Splice Variant Table

PS1 code weights for variants with the same predicted splicing event as a known (likely) pathogenic variant. From Walker et al, 2023 (PMID:37352859), Table 2.

| Variant Under Assessment (VUA) Location | Baseline Code | Comparison Variant Position | PS1 with P Comparison | PS1 with LP Comparison |
|---|---|---|---|---|
| Outside splice ±1,2 dinucleotide | PP3 | Same nucleotide | PS1 | PS1_Moderate |
| Outside splice ±1,2 dinucleotide | PP3 | Within same splice motif (including ±1,2) | PS1_Moderate | PS1_Supporting |
| At splice ±1,2 dinucleotide | PVS1 | Within same splice ±1,2 dinucleotide | PS1_Supporting | N/A |
| At splice ±1,2 dinucleotide | PVS1 | Within same splice motif, outside ±1,2 | PS1_Supporting | PS1_Supporting |
| At splice (PVS1_Strong/Mod/Supp) | PVS1_Strong/Mod/Supp | Within same splice ±1,2 dinucleotide | PS1 | N/A |
| At splice (PVS1_Strong/Mod/Supp) | PVS1_Strong/Mod/Supp | Within same splice motif, outside ±1,2 | PS1_Moderate | PS1_Supporting |

---

### Appendix F: Criteria Summary Table

| Criterion | Status | Max Strength | Modification Type |
|-----------|--------|-------------|-------------------|
| PVS1 | Applicable | Very Strong | General recommendation |
| PS1 | Applicable | Strong | Gene-specific |
| PS2 | Applicable | Very Strong | Disease-specific, Strength |
| PS3 | Applicable | Strong | Disease-specific, Gene-specific |
| PS4 | Applicable | Very Strong | Disease-specific, Gene-specific, Strength |
| PM1 | Applicable | Moderate | Gene-specific |
| PM2 | Applicable | Supporting | General recommendation |
| PM3 | **Not Applicable** | — | AD inheritance |
| PM4 | Applicable | Moderate | No change |
| PM5 | Applicable | Strong | Disease-specific, Gene-specific, Strength |
| PM6 | Applicable | Very Strong | Disease-specific, Strength |
| PP1 | Applicable | Strong | Strength |
| PP2 | **Not Applicable** | — | Benign missense variants are common |
| PP3 | Applicable | Moderate | General recommendation, Strength |
| PP4 | **Not Applicable** | — | Incorporated into PS2/PM6/PS4 |
| PP5 | **Not Applicable** | — | Not for use per ClinGen SVI |
| BA1 | Applicable | Stand Alone | Disease-specific |
| BS1 | Applicable | Strong | Disease-specific |
| BS2 | Applicable | Strong | No change |
| BS3 | **Not Applicable** | — | Insufficient characterization |
| BS4 | **Not Applicable** | — | Reduced penetrance/phenocopies |
| BP1 | **Not Applicable** | — | Missense common cause of disease |
| BP2 | Applicable | Supporting | No change |
| BP3 | Applicable | Supporting | No change |
| BP4 | Applicable | Moderate | General recommendation |
| BP5 | Applicable | Supporting | No change |
| BP6 | **Not Applicable** | — | Not for use per ClinGen SVI |
| BP7 | Applicable | Supporting | No change |

---

## Version History

| Version | Date | Notes |
|---------|------|-------|
| 2.1.0 | 4/28/2025 | Making PVS1 flowchart available |

---

*This document was compiled from ClinGen Epilepsy Sodium Channel VCEP specifications (Version 2.1.0) and ClinGen SVI recommendations. For the most current version, please refer to the [ClinGen website](https://clinicalgenome.org).*
