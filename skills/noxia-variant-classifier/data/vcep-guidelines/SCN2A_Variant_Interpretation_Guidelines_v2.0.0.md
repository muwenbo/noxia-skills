# ClinGen Epilepsy Sodium Channel VCEP Variant Interpretation Guidelines for SCN2A

**Version:** 2.0.0
**Released:** 1/7/2025
**Affiliation:** Epilepsy Sodium Channel VCEP
**Based on:** Richards et al., 2015 ACMG/AMP Guidelines

**Release Notes:** Release contains updates to transcript information and exon numbering. The PM1 table has been revised, slightly altering the amino acid positions that are applicable.

**General Comments:** The "Rules for combining criteria" section in the main specification has been superseded by the points-based system described in the "Combining Rules" attachment.

---

## Gene Information

| Attribute | Value |
|-----------|-------|
| **Gene** | SCN2A (HGNC:10588) |
| **HGNC Name** | sodium voltage-gated channel alpha subunit 2 |
| **Transcripts** | NM_001040142.2 (Adult isoform; MANE Select), NM_001371246.1 (Neonatal isoform; MANE Plus Clinical) |
| **Disease** | Complex neurodevelopmental disorder (MONDO:0100038) |
| **Inheritance** | Autosomal dominant inheritance |

> **Note on Disease:** Complex Neurodevelopmental Disorder (MONDO:0100038), as further described by Helbig et al, 2018 (PMID: 30311377), represents the broad and overlapping clinical spectrum that can include epilepsy, developmental delay, intellectual disability and autism spectrum disorder.

> **Note on Transcripts:** SCN2A has two developmentally-regulated isoforms: neonatal and adult, which differ by the alternatively spliced coding exon 5A/5N. Exons 5A/5N differ by a single amino acid at position 209 (Asn in the neonatal isoform and Asp in the adult).

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

- Most terminal codon expected to undergo nonsense-mediated decay: **p.Thr1591**
- For splice sites, this criterion should **not** be applied with PP3
- For a full gene deletion, a pathogenic classification is warranted
- Follow SVI guidance per workflow in Tayoun et al (2018), included as the "PVS1 Decision Tree" (see [Appendix A](#appendix-a-pvs1-decision-tree))

#### Strength Levels

| Strength | Criteria |
|----------|----------|
| **Very Strong** | Follow SVI guidance per PVS1 Decision Tree (Tayoun et al, 2018). Nonsense/frameshift predicted to undergo NMD (stop codon 5' of p.Thr1591) in biologically-relevant transcripts; full gene deletion; canonical ±1,2 splice sites where exon skipping disrupts reading frame and triggers NMD. |
| **Strong** | Follow SVI guidance per PVS1 Decision Tree. Applicable when: truncated/altered region is critical to protein function (non-NMD variants); reading frame disrupted in tandem duplications; canonical splice variants where exon skipping preserves reading frame but truncated region is critical; variant removes >10% of protein (≥201 aa). |
| **Moderate** | Follow SVI guidance per PVS1 Decision Tree. Applicable when: role of truncated region in protein function is unknown; variant removes <10% of protein (<201 aa); initiation codon variants with pathogenic variant(s) upstream of closest potential in-frame start codon. |
| **Supporting** | Follow SVI guidance per PVS1 Decision Tree. Applicable for initiation codon variants where a different functional transcript uses an alternative start codon. |

#### PVS1 Key Notes

- **Biologically-relevant transcripts:** NM_001040142.2 (adult isoform; MANE Select) and NM_001371246.1 (neonatal isoform; MANE Plus Clinical)
- **Truncated/altered region critical to protein function** is defined as either:
  - (a) Presence of non-truncating, pathogenic (per these criteria) variants, OR
  - (b) Located within a Pathogenic Enriched Region defined by PM1
- **In-frame coding exons:** 1, 3, 4, 6, 9, 10, 11, 14, 15, 16, 19, 20, 21, 22, 23, 24
- **Out-of-frame coding exons:** 2, 5A/5N, 7, 8, 12, 13, 17, 18, 25, 26

---

### PS1 - Same Amino Acid Change

**Original ACMG Summary:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.

**VCEP Specifications:**

The paralogous sodium channel genes associated with neurodevelopmental disorders (SCN1A, SCN2A, SCN3A, SCN8A) share >77% sequence identity (PMID: 33531663). The four homologous domains with voltage sensor and pore region remain largely preserved across the channels. Differences lie within the terminal regions and cytoplasmic loops. When these regions are excluded from analysis, homology increases to >90% (PMID: 33531663; PMID: 16382098). As such, Pathogenic and Likely Pathogenic variants in paralogous genes can be considered for PS1.

PS1 can be applied at varying strengths for splice variants, in conjunction with either PP3 or PVS1. PS1 strength depends on the location of the variant under assessment (within or outside the ±1,2 dinucleotide positions) and the location of the previously classified variant (within or outside the ±1,2 dinucleotide position). See [Appendix B](#appendix-b-ps1-splice-variant-table) for specific combinations.

| Strength | Criteria |
|----------|----------|
| **Strong** | Same/identical amino acid change as a previously established **Pathogenic** variant regardless of nucleotide change. **OR** >1 identical amino acid change in paralogous gene (SCN1A, SCN2A, SCN3A, SCN8A) previously established as Pathogenic or Likely Pathogenic (see Paralogous Gene Table). **OR** Same predicted impact on splicing as a previously classified variant (per Table 2 in Walker et al, 2023; PMID: 37352859). |
| **Moderate** | Same/identical amino acid change as a previously established **Likely Pathogenic** variant regardless of nucleotide change. **OR** Same predicted impact on splicing as a previously classified variant (per Table 2 in Walker et al, 2023). |
| **Supporting** | A single identical amino acid change in a paralogous gene (SCN1A, SCN2A, SCN3A, SCN8A) previously established as Pathogenic or Likely Pathogenic. **OR** Same predicted impact on splicing as a previously classified variant (per Table 2 in Walker et al, 2023). |

**Caveat:** Beware of changes that impact splicing rather than at the amino acid/protein level.

---

### PS2 - De Novo (Confirmed)

**Original ACMG Summary:** De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.

**VCEP Specifications:** Points-based system for each unrelated proband determined by phenotypic specificity.

#### PS2/PM6 Point System

| Phenotypic Consistency | PS2 (Confirmed Parental Relationships) | PM6 (Unconfirmed) |
|------------------------|-----------------------------------------|--------------------|
| Complex Neurodevelopmental Disorder | 1 point | 0.5 points |
| Other phenotypes not consistent w/neurodevelopmental disorder | 0 points | 0 points |

#### Evidence Strength Thresholds

| Total Points | Strength Level |
|--------------|----------------|
| 0.5 | Supporting |
| 1.0 | Moderate |
| 2.0 | Strong |
| 4.0 | Very Strong |

**Note:** Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.

---

### PS3 - Functional Studies

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.

**VCEP Specifications:**

If a variant is found to have differences from wildtype of multiple levels of strength (e.g., strong level of evidence in peak current and moderate level of evidence in persistent current), use the **highest** level of evidence (capping at strong). If a variant has been studied in multiple publications, use the strongest level of evidence available.

| Strength | Criteria |
|----------|----------|
| **Strong** | Patch clamping: **Peak current** ≤72.7% of wildtype. **OR** Patch clamping: **Persistent current** ≥135% of wildtype. **OR** Patch clamping: **Voltage dependence of activation** shifted by ≥2.2 mV (absolute value). **OR** Patch clamping: **Voltage dependence of inactivation** shifted by ≥4.1 mV (absolute value). **OR** Mouse knock-in model displays spontaneous seizures. |
| **Moderate** | Patch clamping: **Peak current** ≤80.6% of wildtype. **OR** Patch clamping: **Persistent current** ≥125% of wildtype. **OR** Patch clamping: **Voltage dependence of activation** shifted by ≥2.1 mV (absolute value). **OR** Patch clamping: **Voltage dependence of inactivation** shifted by ≥3.0 mV (absolute value). **OR** Zebrafish knock-in model displays spontaneous seizures, evidenced by hyperexcitability through electrophysiology or calcium imaging-based studies. |
| **Supporting** | Zebrafish knock-in model displays induced seizures, evidenced by hyperexcitability through electrophysiology or calcium imaging-based studies. |

#### PS3 Functional Assay Thresholds Summary

| Assay Parameter | Strong | Moderate |
|----------------|--------|----------|
| Peak current (% of wildtype) | ≤72.7% | ≤80.6% |
| Persistent current (% of wildtype) | ≥135% | ≥125% |
| Voltage dependence of activation (mV shift) | ≥2.2 | ≥2.1 |
| Voltage dependence of inactivation (mV shift) | ≥4.1 | ≥3.0 |
| Mouse knock-in (spontaneous seizures) | Strong | — |
| Zebrafish knock-in (spontaneous seizures) | — | Moderate |
| Zebrafish knock-in (induced seizures) | — | Supporting |

> **Note:** All patch clamping parameters are as defined by the FENICS ontology (https://bioportal.bioontology.org/ontologies/FENICS).

---

### PS4 - Prevalence in Affected

**Original ACMG Summary:** The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.

**VCEP Specifications:** Points-based system for each unrelated proband determined by phenotypic specificity. The variant must be present in multiple unrelated patients with consistent phenotypes and absent in controls.

| Strength | Total Points |
|----------|-------------|
| **Very Strong** | ≥16 points |
| **Strong** | 4–15.5 points |
| **Moderate** | 2–3.5 points |
| **Supporting** | 1–1.5 points |

#### PS4 Point Values Per Proband

| Phenotypic Consistency | Points |
|------------------------|--------|
| Complex Neurodevelopmental Disorder | 1 point |
| Other phenotypes not consistent w/neurodevelopmental disorder | 0 points |

---

### PM1 - Mutational Hot Spot

**Original ACMG Summary:** Located in a mutational hot spot and/or critical and well-established functional domain without benign variation.

**VCEP Specifications:**

Variant is located within a **Pathogenic Enriched Region (PER)**: Regions enriched for Pathogenic variants (ClinVar/HGMD) across gene families that lack population (gnomAD) variants. Based on Pérez-Palma, 2020 (PMID: 31871067) and Lal et al, 2020 (PMID: 32183904).

| Strength | Criteria |
|----------|----------|
| **Moderate** | Variant is located within a Pathogenic Enriched Region (see PM1 Table below). |

#### PM1 Table — Pathogenic Enriched Regions for SCN2A

| PER # | SCN2A Amino Acid Range | Number of Residues | SCN1A Equivalent | SCN3A Equivalent | SCN8A Equivalent |
|-------|------------------------|-------------------|------------------|------------------|------------------|
| 1 | 213–231 | 19 | 212–230 | 212–230 | 216–234 |
| 2 | 248–256 | 9 | 247–255 | 247–255 | 251–259 |
| 3 | 413–426 | 14 | 411–424 | 412–425 | 399–412 |
| 4 | 850–858 | 9 | 859–867 | 851–859 | 844–852 |
| 5 | 870–878 | 9 | 879–887 | 871–879 | 864–872 |
| 6 | 880–893 | 14 | 889–902 | 881–894 | 874–887 |
| 7 | 895–903 | 9 | 904–912 | 896–904 | 889–897 |
| 8 | 922–930 | 9 | 931–939 | 923–931 | 916–924 |
| 9 | 970–988 | 19 | 979–997 | 971–989 | 964–982 |
| 10 | 1311–1354 | 44 | 1321–1364 | 1309–1352 | 1301–1344 |
| 11 | 1458–1466 | 9 | 1468–1476 | 1453–1461 | 1449–1457 |
| 12 | 1468–1481 | 14 | 1478–1491 | 1463–1476 | 1459–1472 |
| 13 | 1483–1501 | 19 | 1493–1511 | 1478–1496 | 1474–1492 |
| 14 | 1621–1639 | 19 | 1631–1649 | 1616–1634 | 1612–1630 |
| 15 | 1646–1664 | 19 | 1656–1674 | 1641–1659 | 1637–1655 |
| 16 | 1761–1774 | 14 | 1771–1784 | 1756–1769 | 1751–1764 |

**Combining Caveat:** PP3 + PM1 combined can reach no higher than Strong.

---

### PM2 - Absent from Controls

**Original ACMG Summary:** Absent from controls (or at extremely low frequency if recessive) in population databases.

**VCEP Specification (Supporting only):**

| Strength | Criteria |
|----------|----------|
| **Supporting** | One or fewer alleles, if a minimum of 10,000 alleles assessed in population databases such as gnomAD. |

**Caveat:** Population data for indels may be poorly called by next generation sequencing.

---

### PM3 - In Trans with Pathogenic

**Original ACMG Summary:** For recessive disorders, detected in trans with a pathogenic variant.

**VCEP Specifications:** **Not Applicable** — SCN2A is associated with autosomal dominant inheritance.

---

### PM4 - Protein Length Changes

**Original ACMG Summary:** Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

| Strength | Criteria |
|----------|----------|
| **Moderate** | Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants. No change from original ACMG criteria. |

---

### PM5 - Novel Missense at Same Residue

**Original ACMG Summary:** Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.

**VCEP Specifications:**

The paralogous sodium channel genes associated with neurodevelopmental disorders (SCN1A, SCN2A, SCN3A, SCN8A) share >77% sequence identity (PMID: 33531663). As such, Pathogenic and Likely Pathogenic variants in paralogous genes can be considered for PM5.

**Rule Combining Stipulation:** If PM5_Strong is reached and the variant falls within a PM1 region, then **do not** add PM1 with PM5_Strong.

| Strength | Criteria |
|----------|----------|
| **Strong** | ≥2 known pathogenic variants at the same site as the novel change (within the same gene). Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level. |
| **Moderate** | Novel missense change at an amino acid residue where a different missense change determined to be **Pathogenic** has been seen before. |
| **Supporting** | Novel missense change at an amino acid residue where a different missense change determined to be **Likely Pathogenic** has been seen before. **OR** >1 non-identical amino acid change in paralogous gene(s) (SCN1A, SCN2A, SCN3A, SCN8A) where a different missense change determined to be Pathogenic or Likely Pathogenic. |

---

### PM6 - De Novo (Assumed)

**Original ACMG Summary:** Assumed de novo, but without confirmation of paternity and maternity.

**VCEP Specifications:** Uses the same points-based system as PS2 (see [PS2 section](#ps2---de-novo-confirmed)).

#### PM6 Point Values

| Phenotypic Consistency | Points per Proband |
|------------------------|--------------------|
| Complex Neurodevelopmental Disorder | 0.5 points |
| Other phenotypes not consistent w/neurodevelopmental disorder | 0 points |

#### PM6 Evidence Strength Thresholds

| Total Points | Strength Level |
|--------------|----------------|
| 0.5 | Supporting |
| 1.0 | Moderate |
| 2.0 | Strong |
| 4.0 | Very Strong |

---

### PP1 - Co-segregation

**Original ACMG Summary:** Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.

| Strength | Criteria |
|----------|----------|
| **Strong** | ≥7 independent meioses |
| **Moderate** | 5–6 independent meioses |
| **Supporting** | 3–4 independent meioses |

---

### PP2 - Missense in Constrained Gene

**Original ACMG Summary:** Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.

**VCEP Specifications:** **Not Applicable** — Benign missense variants are common.

---

### PP3 - Computational Evidence

**Original ACMG Summary:** Multiple lines of computational evidence support a deleterious effect on the gene or gene product.

**VCEP Specifications:** Follow ClinGen's recommendations (PMID: 36413997), using **REVEL** as the computational tool.

| Strength | Criteria |
|----------|----------|
| **Moderate** | REVEL score meets moderate threshold per ClinGen recommendations (PMID: 36413997). |
| **Supporting** | REVEL score meets supporting threshold per ClinGen recommendations (PMID: 36413997). |

**Stipulations:**
1. Strength should be capped at **Moderate**
2. Limit the combination of PP3 and PM1 to reach no higher than **Strong**

---

### PP4 - Phenotype Specificity

**Original ACMG Summary:** Patient's phenotype or family history is highly specific for a disease with a single genetic etiology.

**VCEP Specifications:** **Not Applicable** — Phenotypic specificity is incorporated into PS2, PM6, and PS4.

---

### PP5 - Reputable Source

**Original ACMG Summary:** Reputable source recently reports variant as pathogenic, but the evidence is not available to the laboratory to perform an independent evaluation.

**VCEP Specifications:** **Not Applicable** — This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PMID: 29543229).

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

| Strength | Criteria |
|----------|----------|
| **Strong** | Observed in a healthy adult individual with full penetrance expected at an early age. No change from original ACMG criteria. |

---

### BS3 - Functional Studies (No Effect)

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

**VCEP Specifications:** **Not Applicable**

**Rationale:**
- **Cellular electrophysiology (voltage clamp recording):** Values indicating "no impact on channel function" have not been sufficiently characterized to date. Additionally, one cannot exclude non-electrophysiological defects such as mis-localization in a neuron based solely on heterologous expression studies. This can be re-assessed by the EP over time as benign variants are functionally characterized in the future.
- **Animal Models:** Lack of an epilepsy phenotype in an animal model is insufficient to support benignity of a variant. Additionally, some non-epilepsy co-morbidities, such as behavioral characteristics that may mimic ID/ASD, are still being established and could support pathogenicity. This can be re-assessed by the EP over time.

---

### BS4 - Lack of Segregation

**Original ACMG Summary:** Lack of segregation in affected members of a family.

**VCEP Specifications:** **Not Applicable** — Reduced penetrance and phenocopies preclude use.

---

### BP1-BP7 - Benign Supporting

| Criterion | Status | Comment |
|-----------|--------|---------|
| **BP1** | Not Applicable | Missense variants are a common cause of disease. |
| **BP2** | Applicable (Supporting) | Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder or observed in cis with a pathogenic variant in any inheritance pattern. No change from ACMG. |
| **BP3** | Applicable (Supporting) | In-frame deletions/insertions in a repetitive region without a known function. No change from ACMG. |
| **BP4** | Applicable (Supporting/Moderate) | Follow ClinGen's recommendations (PMID: 36413997) using REVEL as the computational tool. Moderate and Supporting strengths available. |
| **BP5** | Applicable (Supporting) | Variant found in a case with an alternate molecular basis for disease. No change from ACMG. |
| **BP6** | Not Applicable | Not for use per ClinGen SVI VCEP Review Committee (PMID: 29543229). |
| **BP7** | Applicable (Supporting) | A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved. No change from ACMG. |

---

## Rules for Combining Criteria

This VCEP uses the **Bayesian points-based classification framework** (Tavtigian et al, 2018) in conjunction with forthcoming points-based guidance.

### Points Per Criterion

| Criterion Strength | Points |
|-------------------|--------|
| Pathogenic - Very Strong | 8 |
| Pathogenic - Strong | 4 |
| Pathogenic - Moderate | 2 |
| Pathogenic - Supporting | 1 |
| Benign - Supporting | -1 |
| Benign - Strong | -4 |

### Classification Thresholds

| Total Points | Classification | Posterior Probability |
|-------------|----------------|---------------------|
| ≥10 | **Pathogenic** | ≥0.99 |
| 6–9 | **Likely Pathogenic** | ≥0.9 to <0.99 |
| 0–5 | **VUS** | ≥0.10 to <0.9 |
| −6 to −1 | **Likely Benign** | ≥0.001 to <0.1 |
| ≤−7 | **Benign** | <0.001 |

### Additional Caveats

- PP3 + PM1 combined can reach no higher than **Strong**
- When PM5_Strong is reached, do **not** combine PM1 with PM5

---

## Appendices

### Appendix A: PVS1 Decision Tree

The PVS1 Decision Tree follows SVI guidance per Tayoun et al (2018), adapted for SCN2A:

#### Nonsense or Frameshift

```
Predicted to undergo NMD (stop codon 5' of p.Thr1591)?
├── YES → Exon in biologically-relevant transcript(s)?
│   ├── YES → PVS1
│   └── NO → N/A
└── NO (stop codon 3' of p.Thr1591)
    ├── Truncated/altered region critical to protein function? → PVS1_Strong
    ├── Role of region unknown → PVS1_Moderate
    └── LoF variants frequent in general population / exon absent from
        biologically-relevant transcripts → N/A
```

#### Canonical ±1,2 Splice Sites

```
(If applied, PP3 not to be used in combination)

Exon skipping or cryptic splice site disrupts reading frame AND predicted NMD
(stop codon 5' of p.Thr1591)?
├── YES → Exon in biologically-relevant transcript(s)?
│   ├── YES → PVS1
│   └── NO → N/A
├── Preserves reading frame?
│   ├── Truncated/altered region critical? → PVS1_Strong
│   ├── Region unknown?
│   │   ├── Removes >10% protein (≥201 aa) → PVS1_Strong
│   │   └── Removes <10% protein (<201 aa) → PVS1_Moderate
│   └── LoF frequent / exon absent → N/A
└── Disrupts reading frame but NOT predicted NMD (stop 3' of p.Thr1591)?
    ├── Truncated/altered region critical? → PVS1_Strong
    ├── LoF not frequent, exon present
    │   ├── Removes >10% protein (≥201 aa) → PVS1_Strong
    │   └── Removes <10% protein (<201 aa) → PVS1_Moderate
    └── LoF frequent / exon absent → N/A
```

#### Deletion (Single Exon to Full Gene)

```
Full gene deletion → Pathogenic classification warranted

Single/multi-exon deletion disrupts reading frame AND NMD predicted
(stop 5' of p.Thr1591)?
├── YES → Exon in biologically-relevant transcript(s)?
│   ├── YES → PVS1
│   └── NO → N/A
├── Preserves reading frame?
│   ├── Truncated/altered region critical? → PVS1_Strong
│   ├── Role unknown
│   │   ├── Removes >10% protein → PVS1_Strong
│   │   └── Removes <10% protein → PVS1_Moderate
│   └── LoF frequent / exon absent → N/A
└── Disrupts reading frame, NOT predicted NMD (stop 3' of p.Thr1591)?
    ├── Truncated/altered region critical? → PVS1_Strong
    ├── LoF not frequent, exon present
    │   ├── Removes >10% protein → PVS1_Strong
    │   └── Removes <10% protein → PVS1_Moderate
    └── LoF frequent / exon absent → N/A
```

#### Duplication (≥1 Exon, Completely Contained Within Gene)

```
Proven in tandem → Reading frame disrupted and NMD predicted?
├── YES → PVS1
└── NO / Unknown impact → N/A

Presumed in tandem → Reading frame presumed disrupted and NMD predicted?
├── YES → PVS1_Strong
└── NO → N/A

Proven not in tandem → N/A
```

#### Initiation Codon

```
Different functional transcript uses alternative start codon?
├── YES → PVS1_Supporting
└── NO → ≥1 pathogenic variant(s) upstream of closest potential in-frame start codon?
    ├── YES → PVS1_Moderate
    └── NO → N/A
```

---

### Appendix B: PS1 Splice Variant Table

PS1 code weights for variants with same predicted splicing event as a known (likely) pathogenic variant (from Walker et al, 2023; PMID: 37352859):

| Variant Under Assessment (VUA) Location | Baseline Computational Code | Position of Comparison Variant | PS1 with P Comparison Variant | PS1 with LP Comparison Variant |
|----------------------------------------|----------------------------|-------------------------------|-------------------------------|-------------------------------|
| Outside splice donor/acceptor ±1,2 dinucleotide | PP3 | Same nucleotide | PS1 | PS1_Moderate |
| Outside splice donor/acceptor ±1,2 dinucleotide | PP3 | Within same splice donor/acceptor motif (including ±1,2) | PS1_Moderate | PS1_Supporting |
| At splice donor/acceptor ±1,2 dinucleotide | PVS1 | Within same splice donor/acceptor ±1,2 dinucleotide | PS1_Supporting | N/A |
| At splice donor/acceptor ±1,2 dinucleotide | PVS1 | Within same splice donor/acceptor region, but outside ±1,2 dinucleotide | PS1_Supporting | PS1_Supporting |
| PVS1_Strong, PVS1_Moderate, or PVS1_Supporting | — | Within same splice donor/acceptor ±1,2 dinucleotide | PS1 | N/A |
| PVS1_Strong, PVS1_Moderate, or PVS1_Supporting | — | Within same splice donor/acceptor motif, but outside ±1,2 dinucleotide | PS1_Moderate | PS1_Supporting |

---

### Appendix C: PVS1 Alternate Transcripts & Exon Numbering (SCN2A)

| Exon | Coding Exon | Start Phase | Stop Phase | Frame |
|------|-------------|-------------|------------|-------|
| 1 | — | untranslated | — | — |
| 2 | 1 | 0 | 0 | IN |
| 3 | 2 | 0 | 2 | OUT |
| 4 | 3 | 2 | 2 | IN |
| 5 | 4 | 2 | 2 | IN |
| 6N | 5N | 2 | 1 | OUT |
| 6A | 5A | 2 | 1 | OUT |
| 7 | 6 | 1 | 1 | IN |
| 8 | 7 | 1 | 2 | OUT |
| 9 | 8 | 2 | 0 | OUT |
| 10 | 9 | 0 | 0 | IN |
| 11 | 10 | 0 | 0 | IN |
| 12 | 11 | 0 | 0 | IN |
| 13 | 12 | 0 | 1 | OUT |
| 14 | 13 | 1 | 0 | OUT |
| 15 | 14 | 0 | 0 | IN |
| 16 | 15 | 0 | 0 | IN |
| 17 | 16 | 0 | 0 | IN |
| 18 | 17 | 0 | 1 | OUT |
| 19 | 18 | 1 | 0 | OUT |
| 20 | 19 | 0 | 0 | IN |
| 21 | 20 | 0 | 0 | IN |
| 22 | 21 | 0 | 0 | IN |
| 23 | 22 | 0 | 0 | IN |
| 24 | 23 | 0 | 0 | IN |
| 25 | 24 | 0 | 0 | IN |
| 26 | 25 | 0 | 1 | OUT |
| 27 | 26 | 1 | X | OUT |

> SCN2A has two developmentally-regulated isoforms; neonatal and adult, which differ by the alternatively spliced exon 5.

---

### Appendix D: Population Frequency Thresholds Summary

| Criterion | Threshold | Strength |
|-----------|-----------|----------|
| BA1 | >0.01% (≥5 alleles in ≥10,000 alleles assessed) | Stand Alone |
| BS1 | >0.0002% (≥5 alleles in ≥10,000 alleles assessed) | Strong |
| PM2 | ≤1 allele (in ≥10,000 alleles assessed) | Supporting |

---

### Appendix E: Criteria Applicability Summary

| Criterion | Applicable | Max Strength | Modification Type |
|-----------|-----------|-------------|-------------------|
| PVS1 | Yes | Very Strong | No change |
| PS1 | Yes | Strong | Gene-specific (paralogs) |
| PS2 | Yes | Very Strong | Disease-specific, Points-based |
| PS3 | Yes | Strong | Disease/Gene-specific |
| PS4 | Yes | Very Strong | Disease/Gene-specific, Points-based |
| PM1 | Yes | Moderate | Gene-specific (PER table) |
| PM2 | Yes | Supporting | Other (SVI recommendation) |
| PM3 | **No** | — | AD inheritance |
| PM4 | Yes | Moderate | No change |
| PM5 | Yes | Strong | Disease/Gene-specific (paralogs) |
| PM6 | Yes | Very Strong | Disease/Gene-specific, Points-based |
| PP1 | Yes | Strong | Strength modification |
| PP2 | **No** | — | Benign missense common |
| PP3 | Yes | Moderate | REVEL-based |
| PP4 | **No** | — | Incorporated into PS2/PM6/PS4 |
| PP5 | **No** | — | ClinGen SVI recommendation |
| BA1 | Yes | Stand Alone | Disease-specific threshold |
| BS1 | Yes | Strong | Disease/Gene-specific threshold |
| BS2 | Yes | Strong | No change |
| BS3 | **No** | — | Insufficient characterization |
| BS4 | **No** | — | Reduced penetrance/phenocopies |
| BP1 | **No** | — | Missense common cause |
| BP2 | Yes | Supporting | No change |
| BP3 | Yes | Supporting | No change |
| BP4 | Yes | Moderate | REVEL-based |
| BP5 | Yes | Supporting | No change |
| BP6 | **No** | — | ClinGen SVI recommendation |
| BP7 | Yes | Supporting | No change |

---

### Appendix F: Key References

| PMID | Reference |
|------|-----------|
| 30311377 | Helbig et al, 2018 — Complex Neurodevelopmental Disorder phenotype description |
| 33531663 | Paralogous sodium channel sequence identity analysis |
| 16382098 | Sodium channel homology analysis |
| 37352859 | Walker et al, 2023 — PS1 splice variant framework |
| 31871067 | Pérez-Palma, 2020 — Pathogenic Enriched Regions |
| 32183904 | Lal et al, 2020 — Pathogenic Enriched Regions |
| 36413997 | ClinGen computational evidence recommendations (REVEL) |
| 29543229 | ClinGen SVI recommendation (PP5/BP6 not for use) |

---

## Version History

| Version | Date | Notes |
|---------|------|-------|
| 2.0.0 | 1/7/2025 | Updates to transcript information and exon numbering. Revised PM1 table with slightly altered amino acid positions. Points-based combining rules incorporated. |

---

*This document was compiled from ClinGen Epilepsy Sodium Channel VCEP specifications and ClinGen SVI recommendations. For the most current version, please refer to the ClinGen website.*
