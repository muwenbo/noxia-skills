# ClinGen Epilepsy Sodium Channel VCEP Variant Interpretation Guidelines for SCN8A

**Version:** 2.0.0
**Released:** 1/7/2025
**Affiliation:** Epilepsy Sodium Channel VCEP
**Based on:** Richards et al., 2015 ACMG/AMP Guidelines

**Release Notes:** Release contains updates to transcript information and exon numbering. The PM1 table has been revised, which has altered some of the regions that are applicable from the previous version.

**General Comments:** This specification uses the **points-based combining system** (Tavtigian et al., 2018) rather than the standard ACMG/AMP combining rules. Refer to the [Rules for Combining Criteria](#rules-for-combining-criteria) section.

---

## Gene Information

| Attribute | Value |
|-----------|-------|
| **Gene** | SCN8A (HGNC:10596) |
| **HGNC Name** | sodium voltage-gated channel alpha subunit 8 |
| **Transcripts** | NM_001330260.2 (MANE Select; adult isoform), NM_014191.4 (MANE Plus Clinical; neonatal isoform) |
| **Disease** | Complex neurodevelopmental disorder (MONDO:0100038) |
| **Inheritance** | Autosomal dominant |

> **Transcript Note:** SCN8A has two developmentally-regulated isoforms (neonatal and adult) that differ by the alternatively spliced coding exon 5A/5N. Exons 5A/5N differ by a single amino acid at position 213 (Asn in the neonatal isoform and Asp in the adult isoform).

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

**VCEP Specifications:**

- Most terminal codon expected to undergo nonsense-mediated decay: **p.Thr1582**
- For splice sites, this criterion should **not** be applied with PP3.
- For a **full gene deletion**, a pathogenic classification is warranted.
- Follow SVI guidance per workflow in Tayoun et al (2018), included as the "PVS1 Decision Tree" (see [Appendix A](#appendix-a-pvs1-decision-tree)).

#### Strength Levels

| Strength | Criteria |
|----------|----------|
| **Very Strong** | Follow SVI PVS1 Decision Tree (Tayoun et al, 2018) |
| **Strong** | Follow SVI PVS1 Decision Tree (Tayoun et al, 2018) |
| **Moderate** | Follow SVI PVS1 Decision Tree (Tayoun et al, 2018) |
| **Supporting** | Follow SVI PVS1 Decision Tree (Tayoun et al, 2018) |

#### PVS1 Decision Tree Summary

**Nonsense or Frameshift:**

| Scenario | NMD Predicted (stop 5' of p.Thr1582) | NMD Not Predicted (stop 3' of p.Thr1582) |
|----------|--------------------------------------|------------------------------------------|
| Exon present in biologically-relevant transcript(s) | **PVS1** | See below |
| LoF variants frequent in general population and/or exon absent from biologically-relevant transcript(s) | **N/A** | **N/A** |

For nonsense/frameshift **not predicted to undergo NMD** (stop codon 3' of p.Thr1582):
- Truncated/altered region is critical to protein function → **PVS1_Strong**
- Role of region in protein function is unknown:
  - LoF variants not frequent in general population AND exon present in biologically-relevant transcript(s):
    - Variant removes ≥10% of protein (≥198 aa) → **PVS1_Strong**
    - Variant removes <10% of protein (<198 aa) → **PVS1_Moderate**
  - LoF variants frequent in general population and/or exon absent → **N/A**

**Splice Site Variants (GT-AG, +/-1,2 splice sites):**

*If applied, PP3 is not to be used in combination.*

| Exon Skipping/Cryptic Splice | Reading Frame | NMD Status | Strength |
|------------------------------|---------------|------------|----------|
| Disrupts reading frame | NMD predicted (stop 5' of p.Thr1582) | Exon in biologically-relevant transcript(s) | **PVS1** |
| Disrupts reading frame | NMD not predicted (stop 3' of p.Thr1582) | Truncated region critical to protein function | **PVS1_Strong** |
| Preserves reading frame | — | Truncated/altered region critical to protein function | **PVS1_Strong** |
| Preserves reading frame | — | Role unknown, variant removes ≥10% protein (≥198 aa) | **PVS1_Strong** |
| Preserves reading frame | — | Role unknown, variant removes <10% protein (<198 aa) | **PVS1_Moderate** |

**Deletions (Single Exon to Full Gene):**

| Deletion Type | Strength |
|---------------|----------|
| Full gene deletion | **PVS1** |
| Disrupts reading frame, NMD predicted, exon in biologically-relevant transcript(s) | **PVS1** |
| Disrupts reading frame, NMD not predicted, truncated region critical | **PVS1_Strong** |
| Preserves reading frame, truncated/altered region critical | **PVS1_Strong** |
| Disrupts reading frame, NMD not predicted, removes ≥10% protein | **PVS1_Strong** |
| Disrupts reading frame, NMD not predicted, removes <10% protein | **PVS1_Moderate** |

**Duplications (≥1 exon, completely contained within gene):**

| Scenario | Strength |
|----------|----------|
| Proven in tandem, reading frame disrupted, NMD predicted | **PVS1** |
| Proven in tandem, no/unknown impact on reading frame/NMD | **N/A** |
| Presumed in tandem, reading frame presumed disrupted, NMD predicted | **PVS1_Strong** |
| Proven not in tandem | **N/A** |

**Initiation Codon:**

| Scenario | Strength |
|----------|----------|
| Different functional transcript uses alternative start codon | **N/A** |
| No known alternative start codon, ≥1 pathogenic variant(s) upstream of closest potential in-frame start codon | **PVS1_Moderate** |
| No known alternative start codon, no pathogenic variant(s) upstream | **PVS1_Supporting** |

#### Key PVS1 Definitions

1. **Biologically-relevant transcripts:** NM_001330260.2 (adult isoform; MANE Select) and NM_014191.4 (neonatal isoform; MANE Plus Clinical). These isoforms are developmentally regulated and differ by the alternatively spliced coding exon 5A/5N.
2. **Truncated/altered region critical to protein function:** Defined as either (a) presence of non-truncating, pathogenic (per these criteria) variants, or (b) located within a Pathogenic Enriched Region defined by PM1.
3. **In-frame coding exons:** 1, 3, 4, 6, 9, 10, 11, 14, 15, 16, 19, 20, 21, 22, 23, 24
4. **Out-of-frame coding exons:** 2, 5A/5N, 7, 8, 12, 13, 17, 18, 25, 26

---

### PS1 - Same Amino Acid Change

**Original ACMG Summary:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change. Example: Val->Leu caused by either G>C or G>T in the same codon. Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:**

The paralogous sodium channel genes associated with neurodevelopmental disorders (SCN1A, SCN2A, SCN3A, SCN8A) share >77% sequence identity (PMID:33531663). The four homologous domains with voltage sensor and pore region remain largely preserved across the channels. Differences lie within the terminal regions and cytoplasmic loops. When these regions are excluded from analysis, homology increases to >90% (PMID:33531663; PMID:16382098).

As such, **Pathogenic and Likely Pathogenic variants in paralogous genes can be considered for PS1.**

#### Strength Levels (Amino Acid Changes)

| Strength | Criteria |
|----------|----------|
| **Strong** | Same amino acid change as a previously established **Pathogenic** variant regardless of nucleotide change. **OR** >1 identical amino acid change in paralogous gene previously established as **Pathogenic or Likely Pathogenic** (SCN1A, SCN2A, SCN3A, SCN8A). See Paralogous Gene Table for corresponding amino acid positions. |
| **Moderate** | Same amino acid change as a previously established **Likely Pathogenic** variant regardless of nucleotide change. |
| **Supporting** | A **single** identical amino acid change in a paralogous gene previously established as **Pathogenic or Likely Pathogenic** (SCN1A, SCN2A, SCN3A, SCN8A). |

#### PS1 for Splice Variants

PS1 can be applied at varying strengths for splice variants, in conjunction with either PP3 or PVS1. PS1 strength depends on:
1. Location of the variant under assessment (within or outside the +/-1,2 dinucleotide positions)
2. Location of the previously classified variant (within or outside the +/-1,2 dinucleotide positions)

Specific combinations are outlined in Table 2 from Walker et al (2023) PMID: 37352859:

| VUA Location | Baseline Code | Comparison Variant Position | PS1 with P variant | PS1 with LP variant |
|---|---|---|---|---|
| Outside splice donor/acceptor +/-1,2 | PP3 | Same nucleotide | PS1 (Strong) | PS1_Moderate |
| Outside splice donor/acceptor +/-1,2 | PP3 | Within same splice donor/acceptor motif (including at +/-1,2) | PS1_Moderate | PS1_Supporting |
| At splice donor/acceptor +/-1,2 | PVS1 | Within same splice donor/acceptor +/-1,2 dinucleotide | PS1_Supporting | N/A |
| At splice donor/acceptor +/-1,2 | PVS1 | Within same splice donor/acceptor region, but outside +/-1,2 | PS1_Supporting | PS1_Supporting |
| At splice donor/acceptor +/-1,2 | PVS1_Strong/Moderate/Supporting | Within same splice donor/acceptor +/-1,2 dinucleotide | PS1 (Strong) | N/A |
| At splice donor/acceptor +/-1,2 | PVS1_Strong/Moderate/Supporting | Within same splice donor/acceptor motif, but outside +/-1,2 | PS1_Moderate | PS1_Supporting |

---

### PS2 - De Novo (Confirmed)

**Original ACMG Summary:** De novo (both maternity and paternity confirmed) in a patient with the disease and no family history. Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.

**VCEP Specifications:**

Complex Neurodevelopmental Disorder (MONDO:0100038), as further described in Helbig et al, 2018 (PMID: 30311377), represents the broad and overlapping clinical spectrum that can include epilepsy, developmental delay, intellectual disability and autism spectrum disorder.

Uses a **points-based system** for each unrelated proband determined by phenotypic specificity.

#### PS2 Point System (Per Proband, Confirmed Parentage)

| Phenotype | Points per Proband |
|-----------|--------------------|
| Complex Neurodevelopmental Disorder | 1 point |
| Other phenotypes not consistent w/neurodevelopmental disorder | 0 points |

#### PS2 Evidence Strength Thresholds

| Total Points | Strength Level |
|--------------|----------------|
| 0.5 | Supporting |
| 1 | Moderate |
| 2 | Strong |
| 4 | Very Strong |

---

### PM6 - De Novo (Assumed)

**Original ACMG Summary:** Assumed de novo, but without confirmation of paternity and maternity.

**VCEP Specifications:**

Uses the same points-based system as PS2, but with **0.5 points per proband** (unconfirmed parentage).

#### PM6 Point System (Per Proband, Unconfirmed Parentage)

| Phenotype | Points per Proband |
|-----------|--------------------|
| Complex Neurodevelopmental Disorder | 0.5 points |
| Other phenotypes not consistent w/neurodevelopmental disorder | 0 points |

#### PM6 Evidence Strength Thresholds

| Total Points | Strength Level |
|--------------|----------------|
| 0.5 | Supporting |
| 1 | Moderate |
| 2 | Strong |
| 4 | Very Strong |

> **Note:** PS2 and PM6 points can be combined across probands. For example, 1 confirmed de novo (1 pt) + 2 assumed de novo (0.5 pt each) = 2 pts total = Strong.

---

### PS3 - Functional Studies

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product. Note: Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.

**VCEP Specifications:**

If a variant is found to have differences from wildtype of multiple levels of strength (example: strong level of evidence in peak current and moderate level of evidence in persistent current), use the **highest level of evidence** (capping at strong). If a variant has been studied in multiple publications, use the **strongest level of evidence** available.

#### Strength Levels

| Strength | Criteria |
|----------|----------|
| **Strong** | **Patch clamping:** Peak current ≤72.7% of WT; Persistent current ≥135% of WT; V½ activation shift ≥2.2 mV (absolute); V½ inactivation shift ≥4.1 mV (absolute). **Mouse model:** Knock-in displays spontaneous seizures. |
| **Moderate** | **Patch clamping:** Peak current ≤80.6% of WT; Persistent current ≥125% of WT; V½ activation shift ≥2.1 mV (absolute); V½ inactivation shift ≥3.0 mV (absolute). **Mouse model:** Knock-in displays induced seizures. **Zebrafish model:** Knock-in displays spontaneous seizures (evidenced by hyperexcitability through electrophysiology or calcium imaging). |
| **Supporting** | **Zebrafish model:** Knock-in displays induced seizures (evidenced by hyperexcitability through electrophysiology or calcium imaging). |

#### Approved Functional Assay Summary

| Assay | Parameter | Strong Threshold | Moderate Threshold |
|-------|-----------|------------------|--------------------|
| Patch clamping | Peak current (FENICS) | ≤72.7% of WT | ≤80.6% of WT |
| Patch clamping | Persistent current (FENICS) | ≥135% of WT | ≥125% of WT |
| Patch clamping | V½ activation (FENICS) | ≥2.2 mV shift (absolute) | ≥2.1 mV shift (absolute) |
| Patch clamping | V½ inactivation (FENICS) | ≥4.1 mV shift (absolute) | ≥3.0 mV shift (absolute) |
| Mouse knock-in | Seizure phenotype | Spontaneous seizures | Induced seizures |
| Zebrafish knock-in | Seizure phenotype | — | Spontaneous seizures (Supporting: Induced seizures) |

---

### PS4 - Prevalence in Affected

**Original ACMG Summary:** The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.

**VCEP Specifications:**

Present in multiple unrelated patients with consistent phenotypes and absent in controls. Uses a **points-based system** for each unrelated proband determined by phenotypic specificity.

| Phenotype | Points per Proband |
|-----------|--------------------|
| Complex Neurodevelopmental Disorder | 1 point |
| Other phenotypes not consistent w/neurodevelopmental disorder | 0 points |

#### PS4 Evidence Strength Thresholds

| Total Points | Strength Level |
|--------------|----------------|
| 1 - 1.5 | Supporting |
| 2 - 3.5 | Moderate |
| 4 - 15.5 | Strong |
| ≥16 | Very Strong |

---

### PM1 - Mutational Hot Spot

**Original ACMG Summary:** Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.

**VCEP Specifications:**

Pathogenic Enriched Regions (PERs): Regions that are enriched for Pathogenic variants (ClinVar/HGMD) across gene families, lack population (gnomAD) variants. (Perez-Palma, 2020 PMID: 31871067 & Lal et al, 2020 PMID: 32183904)

| Strength | Criteria |
|----------|----------|
| **Moderate** | Variant is located within a Pathogenic Enriched Region (PER). See PM1 Table for specific amino acid residues. |

#### PM1 Pathogenic Enriched Regions (SCN8A Amino Acid Positions)

| PER # | SCN8A Residues | SCN1A Residues | SCN2A Residues | SCN3A Residues |
|-------|---------------|---------------|---------------|---------------|
| 1 | 216-234 | 212-230 | 213-231 | 212-230 |
| 2 | 251-259 | 247-255 | 248-256 | 247-255 |
| 3 | 399-412 | 411-424 | 413-426 | 412-425 |
| 4 | 844-852 | 859-867 | 850-858 | 851-859 |
| 5 | 864-872 | 879-887 | 870-878 | 871-879 |
| 6 | 874-887 | 889-902 | 880-893 | 881-894 |
| 7 | 889-897 | 904-912 | 895-903 | 896-904 |
| 8 | 916-924 | 931-939 | 922-930 | 923-931 |
| 9 | 964-982 | 979-997 | 970-988 | 971-989 |
| 10 | 1301-1344 | 1321-1364 | 1311-1354 | 1309-1352 |
| 11 | 1449-1457 | 1468-1476 | 1458-1466 | 1453-1461 |
| 12 | 1459-1472 | 1478-1491 | 1468-1481 | 1463-1476 |
| 13 | 1474-1492 | 1493-1511 | 1483-1501 | 1478-1496 |
| 14 | 1612-1630 | 1631-1649 | 1621-1639 | 1616-1634 |
| 15 | 1637-1655 | 1656-1674 | 1646-1664 | 1641-1659 |
| 16 | 1751-1764 | 1771-1784 | 1761-1774 | 1756-1769 |

---

### PM2 - Absent from Controls

**Original ACMG Summary:** Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium. Caveat: Population data for indels may be poorly called by next generation sequencing.

**VCEP Specification (Supporting only):**

| Strength | Criteria |
|----------|----------|
| **Supporting** | One or fewer alleles, if a minimum of 10,000 alleles assessed in population databases, such as the Genome Aggregation Database (gnomAD). |

---

### PM3 - In Trans with Pathogenic

**Original ACMG Summary:** For recessive disorders, detected in trans with a pathogenic variant. Note: This requires testing of parents (or offspring) to determine phase.

**VCEP Specification:** ***Not Applicable***

SCN8A is associated with autosomal dominant inheritance.

---

### PM4 - Protein Length Changes

**Original ACMG Summary:** Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Moderate** | Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants. (No change from original ACMG.) |

---

### PM5 - Novel Missense at Same Residue

**Original ACMG Summary:** Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before. Example: Arg156His is pathogenic; now you observe Arg156Cys. Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:**

The paralogous sodium channel genes associated with neurodevelopmental disorders (SCN1A, SCN2A, SCN3A, SCN8A) share >77% sequence identity (PMID:33531663). Pathogenic and Likely Pathogenic variants in paralogous genes can be considered for PM5.

**Rule Combining Stipulation:** If PM5_Strong is reached, and the variant falls within a PM1 region, then **do not add PM1 with PM5_Strong.**

#### Strength Levels

| Strength | Criteria |
|----------|----------|
| **Strong** | ≥2 known pathogenic variants at same site as novel change (within the same gene). |
| **Moderate** | Novel missense change at an amino acid residue where a different missense change determined to be **Pathogenic** has been seen before. |
| **Supporting** | Novel missense change at an amino acid residue where a different missense change determined to be **Likely Pathogenic** has been seen before. **OR** >1 non-identical amino acid change in paralogous gene(s) where a different missense change determined to be **Pathogenic or Likely Pathogenic** (SCN1A, SCN2A, SCN3A, SCN8A). |

---

### PP1 - Co-segregation

**Original ACMG Summary:** Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease. Note: May be used as stronger evidence with increasing segregation data.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | ≥7 independent meioses |
| **Moderate** | 5-6 independent meioses |
| **Supporting** | 3-4 independent meioses |

---

### PP2 - Missense in Constrained Gene

**Original ACMG Summary:** Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.

**VCEP Specification:** ***Not Applicable***

Benign missense variants are common.

---

### PP3 - Computational Evidence

**Original ACMG Summary:** Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.). Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.

**VCEP Specifications:**

Follow ClinGen's recommendations (PMID: 36413997), using **REVEL** as the computational tool, with the following stipulations:

1. Strength should be **capped at Moderate**
2. Limit the combination of **PP3 and PM1 to reach no higher than Strong**

| Strength | Criteria |
|----------|----------|
| **Moderate** | Follow ClinGen SVI recommendations using REVEL (capped at Moderate) |
| **Supporting** | Follow ClinGen SVI recommendations using REVEL |

---

### PP4 - Phenotype Specificity

**Original ACMG Summary:** Patient's phenotype or family history is highly specific for a disease with a single genetic etiology.

**VCEP Specification:** ***Not Applicable***

Phenotypic specificity has been incorporated into PS2, PM6, and PS4.

---

### PP5 - Reputable Source

**Original ACMG Summary:** Reputable source recently reports variant as pathogenic, but the evidence is not available to the laboratory to perform an independent evaluation.

**VCEP Specification:** ***Not Applicable***

This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PMID: 29543229).

---

## Benign Criteria

### BA1 - Allele Frequency >5%

**Original ACMG Summary:** Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

**VCEP Specification (Stand Alone):**

- Allele frequency is above **0.02%** in gnomAD or other large population database.

| Strength | Threshold |
|----------|-----------|
| **Stand Alone** | Allele frequency >**0.01%** in gnomAD or other large population databases, must be ≥5 alleles if a minimum of 10,000 alleles was assessed. |

> **Note:** The VCEP specifications list BA1 at 0.02% in the general description and 0.01% at the Stand Alone level. The Stand Alone threshold of **0.01%** (0.0001) with ≥5 alleles is the applicable threshold.

---

### BS1 - Frequency Greater Than Expected

**Original ACMG Summary:** Allele frequency is greater than expected for disorder.

**VCEP Specification (Strong):**

- Allele frequency is above **0.0002%** in gnomAD or other large population database, must be ≥5 alleles if a minimum of 10,000 alleles was assessed.

---

### BS2 - Observed in Healthy Adult

**Original ACMG Summary:** Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

**VCEP Specification (Strong):**

- Observed in a healthy adult individual with full penetrance expected at an early age. (No change from original ACMG.)

---

### BS3 - Functional Studies (No Effect)

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

**VCEP Specification:** ***Not Applicable***

**Rationale:**
- **Cellular electrophysiology (voltage clamp recording):** Values indicating "no impact on channel function" have not been sufficiently characterized to date. Additionally, one cannot exclude non-electrophysiological defects such as mis-localization in a neuron based solely on heterologous expression studies. This can be re-assessed by the EP over time and as benign variants are functionally characterized in the future.
- **Animal Models:** Lack of an epilepsy phenotype in an animal model is insufficient to support benignity of a variant. Additionally, some non-epilepsy co-morbidities, such as behavioral characteristics that may mimic intellectual disability and/or autism spectrum disorder, are still being established and could support pathogenicity. This can be re-assessed by the EP over time.

---

### BS4 - Lack of Segregation

**Original ACMG Summary:** Lack of segregation in affected members of a family. Caveat: The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.

**VCEP Specification:** ***Not Applicable***

Reduced penetrance and phenocopies.

---

### BP1-BP7 - Benign Supporting

| Criterion | Status | Strength | Comment |
|-----------|--------|----------|---------|
| **BP1** | Not Applicable | — | Missense variants are common cause of disease. |
| **BP2** | Applicable | Supporting | Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder or observed in cis with a pathogenic variant in any inheritance pattern. (No change.) |
| **BP3** | Applicable | Supporting | In-frame deletions/insertions in a repetitive region without a known function. (No change.) |
| **BP4** | Applicable | Moderate / Supporting | Follow ClinGen's recommendations (PMID: 36413997), using REVEL as the computational tool. |
| **BP5** | Applicable | Supporting | Variant found in a case with an alternate molecular basis for disease. (No change.) |
| **BP6** | Not Applicable | — | Not for use as recommended by the ClinGen SVI VCEP Review Committee (PMID: 29543229). |
| **BP7** | Applicable | Supporting | A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved. (No change.) |

---

## Rules for Combining Criteria

This VCEP uses the **points-based combining system** (Tavtigian et al, 2018) in conjunction with forthcoming points-based guidance.

### Points per Criterion

| Criterion Strength | Points |
|--------------------|--------|
| P - Very Strong | 8 |
| P - Strong | 4 |
| P - Moderate | 2 |
| P - Supporting | 1 |
| B - Supporting | -1 |
| B - Strong | -4 |

### Classification of Variant

| Total Points | Classification | Posterior Probability |
|--------------|---------------|---------------------|
| ≥10 | **Pathogenic** | ≥0.99 |
| 6-9 | **Likely Pathogenic** | ≥0.9 to <0.99 |
| 0-5 | **VUS** | ≥0.10 to <0.9 |
| -6 to -1 | **Likely Benign** | ≥0.001, <0.1 |
| -7 and below | **Benign** | <0.001 |

### Additional Caveats

- **PP3 + PM1** combined can reach **no higher than Strong** (max 4 points combined)
- When **PM5_Strong** is reached, **do not combine PM1** with PM5_Strong

### Pathogenic Classification (≥10 points)

| Criteria Combination | Example Point Calculation |
|---------------------|--------------------------|
| 1 Very Strong AND ≥1 Strong | 8 + 4 = 12 |
| 1 Very Strong AND ≥2 Moderate | 8 + 2 + 2 = 12 |
| 1 Very Strong AND 1 Moderate AND 1 Supporting | 8 + 2 + 1 = 11 |
| 1 Very Strong AND ≥2 Supporting | 8 + 1 + 1 = 10 |
| ≥2 Strong | 4 + 4 + ... = ≥10 (requires ≥3 strong, or 2 strong + moderate/supporting) |
| 1 Strong AND ≥3 Moderate | 4 + 2 + 2 + 2 = 10 |
| 1 Strong AND 2 Moderate AND ≥2 Supporting | 4 + 2 + 2 + 1 + 1 = 10 |
| 1 Strong AND 1 Moderate AND ≥4 Supporting | 4 + 2 + 1 + 1 + 1 + 1 = 10 |

### Likely Pathogenic Classification (6-9 points)

| Criteria Combination | Example Point Calculation |
|---------------------|--------------------------|
| 1 Very Strong AND 1 Moderate | 8 + 2 = 10 (borderline; note: ≥10 = Pathogenic) |
| 1 Strong AND 1 Moderate | 4 + 2 = 6 |
| 1 Strong AND ≥2 Supporting | 4 + 1 + 1 = 6 |
| ≥3 Moderate | 2 + 2 + 2 = 6 |
| 2 Moderate AND ≥2 Supporting | 2 + 2 + 1 + 1 = 6 |

### Benign Classification (≤-7 points)

| Criteria Combination |
|---------------------|
| ≥2 Strong (BS1, BS2): -4 + -4 = -8 |
| 1 Stand Alone (BA1) |

### Likely Benign Classification (-6 to -1 points)

| Criteria Combination |
|---------------------|
| 1 Strong (BS1, BS2) AND 1 Supporting (BP2, BP3, BP5, BP7): -4 + -1 = -5 |
| ≥2 Supporting (BP2, BP3, BP5, BP7): -1 + -1 = -2 |

### Applicable Criteria by Strength Level

| Strength | Pathogenic Criteria | Benign Criteria |
|----------|-------------------|-----------------|
| **Very Strong (8 pts)** | PVS1, PS2_VeryStrong, PS4_VeryStrong | — |
| **Strong (4 pts)** | PVS1_Strong, PS1, PS2, PS3, PS4, PM5_Strong, PM6_Strong, PP1_Strong, PP3_Strong | BS1, BS2 |
| **Moderate (2 pts)** | PVS1_Moderate, PS1_Moderate, PS2_Moderate, PS3_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate, PP3_Moderate | — |
| **Supporting (1 pt / -1 pt)** | PVS1_Supporting, PS2_Supporting, PS3_Supporting, PS4_Supporting, PM2_Supporting, PM5_Supporting, PM6_Supporting, PP1, PP3 | BP2, BP3, BP5, BP7 |
| **Stand Alone** | — | BA1 |

---

## Appendices

### Appendix A: PVS1 Decision Tree

The PVS1 Decision Tree follows the SVI guidance per Tayoun et al (2018), with the following SCN8A-specific parameters:

- **NMD boundary:** p.Thr1582 (stop codons 5' of this position are predicted to undergo NMD)
- **Biologically-relevant transcripts:**
  - NM_001330260.2 (adult isoform; MANE Select)
  - NM_014191.4 (neonatal isoform; MANE Plus Clinical)
- **10% of protein:** ≥198 amino acids
- **Critical region definition:** Presence of non-truncating pathogenic variants OR located within a Pathogenic Enriched Region (PM1)
- **In-frame coding exons:** 1, 3, 4, 6, 9, 10, 11, 14, 15, 16, 19, 20, 21, 22, 23, 24
- **Out-of-frame coding exons:** 2, 5A/5N, 7, 8, 12, 13, 17, 18, 25, 26

### Appendix B: SCN8A Exon Numbering and Frame Status

| Exon (Genomic) | Coding Exon | Start Phase | Stop Phase | Frame |
|-------|-------------|-------------|------------|-------|
| 1 | — | Untranslated | — | — |
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
| 27 | 26 | 1 | — | OUT |

### Appendix C: Population Frequency Thresholds Summary

| Criterion | Threshold | Strength | Additional Requirements |
|-----------|-----------|----------|------------------------|
| BA1 | >0.01% | Stand Alone | ≥5 alleles if minimum 10,000 alleles assessed |
| BS1 | >0.0002% | Strong | ≥5 alleles if minimum 10,000 alleles assessed |
| PM2 | ≤1 allele | Supporting | Minimum 10,000 alleles assessed in gnomAD |

### Appendix D: Not Applicable Criteria Summary

| Criterion | Reason |
|-----------|--------|
| PM3 | SCN8A is associated with autosomal dominant inheritance |
| PP2 | Benign missense variants are common |
| PP4 | Phenotypic specificity incorporated into PS2, PM6, PS4 |
| PP5 | Not for use per ClinGen SVI VCEP Review Committee (PMID: 29543229) |
| BS3 | Functional "no impact" values not sufficiently characterized; cannot exclude non-electrophysiological defects |
| BS4 | Reduced penetrance and phenocopies |
| BP1 | Missense variants are common cause of disease |
| BP6 | Not for use per ClinGen SVI VCEP Review Committee (PMID: 29543229) |

### Appendix E: Reference PMIDs

| PMID | Reference |
|------|-----------|
| 33531663 | Paralogous sodium channel sequence identity analysis |
| 16382098 | Sodium channel homology analysis |
| 30311377 | Helbig et al, 2018 - Complex Neurodevelopmental Disorder phenotype description |
| 37352859 | Walker et al, 2023 - PS1 for splice variants (Table 2) |
| 31871067 | Perez-Palma, 2020 - Pathogenic Enriched Regions |
| 32183904 | Lal et al, 2020 - Pathogenic Enriched Regions |
| 36413997 | ClinGen SVI recommendations for computational tools (REVEL) |
| 29543229 | ClinGen SVI VCEP Review Committee - PP5/BP6 not recommended |

---

## Version History

| Version | Date | Notes |
|---------|------|-------|
| 2.0.0 | 1/7/2025 | Updates to transcript information and exon numbering. Revised PM1 table with altered applicable regions. Implemented points-based combining system. |

---

*This document was compiled from ClinGen Epilepsy Sodium Channel VCEP specifications and ClinGen SVI recommendations. For the most current version, please refer to the ClinGen website.*
