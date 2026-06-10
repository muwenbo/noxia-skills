# ClinGen Congenital Myopathies VCEP Variant Interpretation Guidelines for RYR1 (Autosomal Recessive)

**Version:** 2.0.0
**Released:** 12/12/2024
**Affiliation:** Congenital Myopathies VCEP
**Based on:** Richards et al., 2015 ACMG/AMP Guidelines

---

## Gene Information

| Attribute | Value |
|-----------|-------|
| **Gene** | RYR1 (HGNC:10483) |
| **HGNC Name** | ryanodine receptor 1 |
| **Transcript** | NM_000540.3 |
| **Disease** | RYR1-related myopathy (MONDO:0100150) |
| **Inheritance** | Autosomal recessive inheritance |

> **General Note on Multiple MOIs:** In general, the easiest way to tell whether a variant is AD or AR is to look at the clinical situation of probands with the variant, along with the family and inheritance. If it's de novo, it's much more likely to be AD and if it's observed with a second variant, it's much more likely to be AR. In general, loss of function variants are almost always associated with AR disease. If two missense variants are identified in trans, individuals are much more likely to have central core or minicore disease. Malignant hyperthermia is only associated with AD variants. However, there have been some examples of a missense MH variant in trans with a LOF variant, causing a blended phenotype of myopathy and MH susceptibility. The AD and AR specifications are listed separately.

> **Release Notes (v2.0.0):** The approved BS1 threshold for AR variant curation was listed incorrectly and has been corrected in this release.

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

Caveats:
- Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7).
- Use caution interpreting LOF variants at the extreme 3' end of a gene.
- Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact.
- Use caution in the presence of multiple transcripts.

**VCEP Specifications:**

RYR1 is associated with both dominant and recessive myopathy. Loss of function is only a mechanism for autosomal recessive (AR) disease and **PVS1 should only be applied for AR variants**.

#### Strength Levels

| Strength | Criteria |
|----------|----------|
| **Very Strong (PVS1)** | Null variant (nonsense, frameshift, canonical +/-1 or 2 splice sites, initiation codon, single or multi-exon deletion) where LOF is a known mechanism — apply per PVS1 flowchart. NMD predicted (up to c.14971, p.4991). |
| **Strong (PVS1_Strong)** | In-frame deletions or in-frame exon-skipping variants in the pore/transmembrane region of RYR1 (amino acids 4800-4950, exons 100-103). Also applies to other scenarios per the PVS1 flowchart. |
| **Moderate (PVS1_Moderate)** | See PVS1 flowchart (Appendix A). |
| **Supporting (PVS1_Supporting)** | See PVS1 flowchart (Appendix A). |

> **Modification Type:** Disease-specific, Gene-specific

---

### PS1 - Same Amino Acid Change

**Original ACMG Summary:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change. Example: Val->Leu caused by either G>C or G>T in the same codon. Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | No change — use as originally described. |
| **Moderate** | No change — use as originally described. |
| **Supporting** | No change — use as originally described. |

> **Modification Type:** No change

---

### PS2 - De Novo (Confirmed)

**Original ACMG Summary:** De novo (both maternity and paternity confirmed) in a patient with the disease and no family history. Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.

**VCEP Specifications:** No change — use as originally described at all strength levels (Very Strong, Strong, Moderate, Supporting).

#### PS2/PM6 Point System

| Phenotypic Consistency | Confirmed Parental Relationships | Unconfirmed |
|------------------------|----------------------------------|-------------|
| Phenotype highly specific for gene | 2 points | 1 point |
| Phenotype consistent but not highly specific | 1 point | 0.5 points |
| Phenotype consistent + high genetic heterogeneity | 0.5 points | 0.25 points |
| Phenotype not consistent | 0 points | 0 points |

#### Evidence Strength Thresholds

| Points | Strength Level |
|--------|----------------|
| 0.5 | Supporting |
| 1.0 | Moderate |
| 2.0 | Strong |
| 4.0 | Very Strong |

> **Modification Type:** No change

---

### PS3 - Functional Studies

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product. Note: Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.

**VCEP Specifications:**

Specified assays are only provided for the AD specifications, which are listed separately. For AR RYR1-related myopathy:

| Strength | Criteria |
|----------|----------|
| **Strong** | May only be considered for **variant-specific mouse models**. Currently, no other assays are applicable at this strength. |
| **Moderate** | Not specified for AR. |
| **Supporting** | There are no specified functional assays for AR RYR1-related myopathy. However, it is acceptable to use PS3_Supporting for other functional analyses if: (1) The assay has been validated by a known pathogenic and benign variant, AND (2) There is plausible reason that the function the assay is testing relates to the phenotype, AND (3) The assay conditions are likely to mimic the physiological environment. |

> **Modification Type:** Disease-specific, Gene-specific

---

### PS4 - Prevalence in Affected

**Original ACMG Summary:** The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.

**VCEP Specifications:** **Not Applicable** for autosomal recessive RYR1 variants. Please use **PM3** for case counting. There are separate specifications for AD RYR1 variants.

> **Modification Type:** Disease-specific, Gene-specific

---

### PM1 - Mutational Hot Spot

**Original ACMG Summary:** Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Moderate** | The pore/transmembrane region of RYR1 is critical for protein function and missense variants that fall within this region (**amino acids 4800-4950**) may apply PM1. |

> **Modification Type:** Disease-specific, Gene-specific

---

### PM2 - Absent from Controls

**Original ACMG Summary:** Absent from controls (or at extremely low frequency if recessive) in population databases. Caveat: Population data for indels may be poorly called by next generation sequencing.

**VCEP Specifications:**

If the mode of inheritance for the variant is unclear (largely with missense variants as loss of function variants are predicted to cause AR disease), use the more conservative AD cutoff and specifications for PM2_Supporting.

**PM2_Supporting (Supporting only):**
- Minor allele frequency in population databases of at least 2,000 alleles is **≤0.00000697** for autosomal recessive

> **Modification Type:** Disease-specific, Gene-specific

---

### PM3 - In Trans with Pathogenic

**Original ACMG Summary:** For recessive disorders, detected in trans with a pathogenic variant. Note: This requires testing of parents (or offspring) to determine phase.

**VCEP Specifications:**

Use the SVI-recommended PM3 chart to count observations. Points for each proband should be summed to get to a final PM3 strength. In order to count case counts for your variant of interest, it should be **rare enough to not meet BS1**.

#### PM3 Point System (Per Proband)

| Classification/Zygosity of Other Variant | Confirmed in Trans | Phase Unknown |
|------------------------------------------|-------------------|---------------|
| Likely Pathogenic / Pathogenic | 1.0 | 0.5 |
| Homozygous occurrence (max 1.0 point) or Rare VUS on other allele | 0.5 | N/A |

#### PM3 Evidence Strength Thresholds

| Total Points | Strength Level |
|--------------|----------------|
| 0.5 | PM3_Supporting |
| 1.0 | PM3 (Moderate) |
| 2.0 | PM3_Strong |
| 4.0 | PM3_VeryStrong |

> **Modification Type:** Disease-specific, Gene-specific

---

### PM4 - Protein Length Changes

**Original ACMG Summary:** Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

**VCEP Specifications:**

Either **PVS1_Strong** or **PM4_Strong**, but not both, should be used for in-frame deletions in the pore region (amino acids 4800-4950) of RYR1.

| Strength | Criteria |
|----------|----------|
| **Strong** | No change — use as originally described. |
| **Moderate** | No change — use as originally described. |
| **Supporting** | No change — use as originally described. |

> **Note:** For in-frame deletions in the pore/transmembrane region (AAs 4800-4950), choose either PVS1_Strong or PM4_Strong, not both.

> **Modification Type:** No change (with gene-specific caveat for pore region)

---

### PM5 - Novel Missense at Same Residue

**Original ACMG Summary:** Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before. Example: Arg156His is pathogenic; now you observe Arg156Cys. Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | No change — use as originally described. |
| **Moderate** | No change — use as originally described. |
| **Supporting** | No change — use as originally described. |

> **Modification Type:** No change

---

### PM6 - De Novo (Assumed)

**Original ACMG Summary:** Assumed de novo, but without confirmation of paternity and maternity.

**VCEP Specifications:** No change — use as originally described. Same point-based system as PS2 (see PS2/PM6 Point System above).

| Strength | Criteria |
|----------|----------|
| **Strong** | No change — use as originally described. |
| **Moderate** | No change — use as originally described. |
| **Supporting** | No change — use as originally described. |

> **Modification Type:** No change

---

### PP1 - Co-segregation

**Original ACMG Summary:** Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease. Note: May be used as stronger evidence with increasing segregation data.

**VCEP Specifications:**

The segregation chart (adopted from Oza et al 2018, PMID:30311386) should be used to determine the strength level of the total number of affected and unaffected segregations. In order to count unaffected segregations, the unaffected individuals can be heterozygous carriers or WT, but should have the same risk of inheriting the variant as the affected individuals (e.g. siblings in the same generation).

| Strength | Criteria |
|----------|----------|
| **Strong** | See segregation chart (Oza et al 2018, PMID:30311386) |
| **Moderate** | See segregation chart |
| **Supporting** | See segregation chart |

#### PP1 Thresholds (General SVI Recommendation)

| Strength | Likelihood | LOD Score |
|----------|------------|-----------|
| Supporting | 4:1 | 0.6 |
| Moderate | 16:1 | 1.2 |
| Strong | 32:1 | 1.5 |

> **Modification Type:** General recommendation

---

### PP2 - Missense in Constrained Gene

**Original ACMG Summary:** Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.

**VCEP Specifications:** **Not Applicable.** RYR1 is not a gene that is constrained for missense variation. Hence PP2 is not applicable.

---

### PP3 - Computational Evidence

**Original ACMG Summary:** Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.). Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.

**VCEP Specifications (Supporting):**

PP3 is met if:
- **REVEL score ≥ 0.7**, OR
- The variant is predicted to impact splicing using **SpliceAI score ≥ 0.5**

> **Modification Type:** General recommendation

---

### PP4 - Phenotype Specificity

**Original ACMG Summary:** Patient's phenotype or family history is highly specific for a disease with a single genetic etiology.

**VCEP Specifications (Supporting):**

To meet PP4, a congenital myopathy testing panel should be performed without identification of other causative variants **AND AT LEAST TWO** of these features should be present:

1. Presence on muscle biopsy of: **mini cores or central cores** (histology or electron microscopy)
2. **Exercise, heat, or anesthetic induced rhabdomyolysis**
3. **Ophthalmoplegia**
4. **Characteristic muscle imaging** (see Figure 8, Saade et al 2019, PMID:31060725)

> **Modification Type:** Disease-specific, Gene-specific

---

### PP5 - Reputable Source

**Original ACMG Summary:** Reputable source recently reports variant as pathogenic, but the evidence is not available to the laboratory to perform an independent evaluation.

**VCEP Specifications:** **Not Applicable.** This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PMID:29543229).

---

## Benign Criteria

### BA1 - Allele Frequency >5%

**Original ACMG Summary:** Allele frequency is above 5% in population databases.

**VCEP Specification (Stand Alone):**

- The minor allele frequency using the filtering allele frequency of either exomes or genomes of continental populations in gnomAD is **≥0.00697** for AR variants
- All populations used should have at least **2,000 alleles** and **>1 observation**

If the mode of inheritance for the variant is unclear (this largely applies to missense variants as loss of function variants are suspected to cause AR disease), use the more conservative AR cutoff and specifications for BA1.

**BA1 Exclusion Variants** (well-known pathogenic variants that are above the specified BA1 or BS1 threshold):
- NM_000540.3:c.6721C>T (p.Arg2241Ter)
- NM_000540.3:c.10348-6C>G

> **Modification Type:** Disease-specific, Gene-specific

---

### BS1 - Frequency Greater Than Expected

**Original ACMG Summary:** Allele frequency is greater than expected for disorder.

**VCEP Specification (Strong):**

- The minor allele frequency using the filtering allele frequency of either exomes or genomes of continental populations in gnomAD is **≥0.000697** for AR variants
- All populations used should have at least **2,000 alleles** and **>1 observation**

If the mode of inheritance for the variant is unclear (this largely applies to missense variants as loss of function variants are suspected to cause AR disease), use the more conservative AR cutoff and specifications for BS1.

**BA1/BS1 Exclusion Variants:**
- NM_000540.3:c.6721C>T (p.Arg2241Ter)
- NM_000540.3:c.10348-6C>G

> **Modification Type:** Disease-specific, Gene-specific

---

### BS2 - Observed in Healthy Adult

**Original ACMG Summary:** Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | No change — use as originally described. |
| **Moderate** | No change — use as originally described. |
| **Supporting** | No change — use as originally described. |

> **Modification Type:** No change

---

### BS3 - Functional Studies (No Effect)

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

**VCEP Specifications:** **Not Applicable.** The VCEP has decided that lack of demonstrated effect in a functional assay should not count against the pathogenicity of an RYR1 variant because of the numerous possible functions of the ryanodine receptor; therefore all specified functional assays will only be used as evidence for pathogenicity.

---

### BS4 - Lack of Segregation

**Original ACMG Summary:** Lack of segregation in affected members of a family. Caveat: The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | No change — use as originally described. |
| **Moderate** | No change — use as originally described. |
| **Supporting** | No change — use as originally described. |

> **Modification Type:** No change

---

### BP1-BP7 - Benign Supporting

| Criterion | Status | Comment |
|-----------|--------|---------|
| **BP1** | **Not Applicable** | Both missense and truncating variants in RYR1 are disease-causing. |
| **BP2** | Applicable (no change) | Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder or observed in cis with a pathogenic variant in any inheritance pattern. Available at Supporting, Moderate, and Strong. |
| **BP3** | **Not Applicable** | There are no regions in RYR1 where BP3 would apply. |
| **BP4** | Applicable (modified) | BP4 is met if **REVEL score ≤ 0.15** or if the variant is **not predicted to impact splicing using SpliceAI**. |
| **BP5** | Applicable (no change) | Variant found in a case with an alternate molecular basis for disease. Available at Supporting, Moderate, and Strong. |
| **BP6** | **Not Applicable** | This criterion is not for use as recommended by the ClinGen SVI VCEP Review Committee (PMID:29543229). |
| **BP7** | Applicable (modified) | A synonymous variant for which **SpliceAI** predicts no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved. |

---

## Rules for Combining Criteria

### Pathogenic Classification

| Criteria Combination |
|---------------------|
| 1 Very Strong (PVS1, PS2_VeryStrong, PM3_VeryStrong) **AND** ≥1 Strong (PVS1_Strong, PS1, PS2, PS3, PM3_Strong, PM4_Strong, PM5_Strong, PM6_Strong, PP1_Strong) |
| 1 Very Strong **AND** ≥2 Moderate (PVS1_Moderate, PS1_Moderate, PS2_Moderate, PM1, PM3, PM4, PM5, PM6, PP1_Moderate) |
| 1 Very Strong **AND** 1 Moderate **AND** 1 Supporting (PVS1_Supporting, PS1_Supporting, PS2_Supporting, PS3_Supporting, PM2_Supporting, PM3_Supporting, PM4_Supporting, PM5_Supporting, PM6_Supporting, PP1, PP3, PP4) |
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
| ≥2 Strong (BS1, BS2, BS4, BP2_Strong, BP5_Strong) |
| 1 Stand Alone (BA1) |

### Likely Benign Classification

| Criteria Combination |
|---------------------|
| 1 Strong (BS1, BS2, BS4, BP2_Strong, BP5_Strong) **AND** 1 Supporting (BS2_Supporting, BS4_Supporting, BP2, BP4, BP5, BP7) |
| ≥2 Supporting (BS2_Supporting, BS4_Supporting, BP2, BP4, BP5, BP7) |

---

## Appendices

### Appendix A: PVS1 Decision Tree for RYR1

The following flowchart describes PVS1 strength assignment for different variant types in RYR1:

#### Nonsense or Frameshift Variants

```
Nonsense or Frameshift
├── Predicted to undergo NMD (up to c.14971, p.4991)
│   └── PVS1
│
└── NOT predicted to undergo NMD
    ├── Truncated/altered region is critical to protein function
    │   (AAs 4800-4950, Exons 100-103)
    │   └── PVS1_Strong
    │
    └── Role of region in protein function is unknown
        ├── LoF variants in this exon are frequent in general population
        │   and/or exon is absent from biologically-relevant transcript(s)
        │   └── N/A
        │
        └── LoF variants NOT frequent and exon present in
            biologically-relevant transcript(s)
            ├── Variant removes >10% of protein → PVS1_Strong
            └── Variant removes <10% of protein → PVS1_Moderate
```

#### Canonical Splice Site Variants (GT-AG, +/-1,2)

```
Splice Site (GT-AG, ±1,2)
├── Exon skipping or cryptic splice site DISRUPTS reading frame
│   AND predicted to undergo NMD
│   └── PVS1
│
├── Exon skipping or cryptic splice site DISRUPTS reading frame
│   AND NOT predicted to undergo NMD
│   ├── Truncated/altered region critical (AAs 4800-4950, Exons 100-103)
│   │   └── PVS1_Strong
│   └── Role of region unknown
│       ├── LoF variants frequent / exon absent → N/A
│       └── LoF variants not frequent / exon present
│           ├── Removes >10% of protein → PVS1_Strong
│           └── Removes <10% of protein → PVS1_Moderate
│
└── Exon skipping or cryptic splice site PRESERVES reading frame
    In-frame exons: 1-4, 9, 11, 15, 23, 32, 36, 38, 50, 53, 54, 66,
                    70-73, 78, 83, 84, 86, 87, 90, 91, 94, 95, 100, 101, 106
    ├── Exon present in biologically-relevant transcript(s)
    │   ├── Truncated/altered region critical (AAs 4800-4950, Exons 100-103)
    │   │   └── PVS1_Strong
    │   └── Role of region unknown
    │       ├── LoF variants frequent / exon absent → N/A
    │       └── LoF variants not frequent / exon present
    │           ├── Removes >10% of protein → PVS1_Strong
    │           └── Removes <10% of protein → PVS1_Moderate
    └── Exon absent from biologically-relevant transcript(s)
        └── N/A
```

#### Deletion Variants (Single Exon to Full Gene)

```
Deletion
├── Single to multi exon – DISRUPTS reading frame, predicted NMD
│   └── PVS1
│
├── Single to multi exon – DISRUPTS reading frame, NOT predicted NMD
│   ├── Truncated/altered region critical → PVS1_Strong
│   └── Role of region unknown
│       ├── LoF variants frequent / exon absent → N/A
│       └── LoF variants not frequent / exon present
│           ├── Removes >10% of protein → PVS1_Strong
│           └── Removes <10% of protein → PVS1_Moderate
│
├── Single to multi exon – PRESERVES reading frame
│   ├── Truncated/altered region critical (AAs 4800-4950, Exons 100-103)
│   │   └── PVS1_Strong
│   └── Role of region unknown
│       ├── LoF variants frequent / exon absent → N/A
│       └── LoF variants not frequent / exon present
│           ├── Removes >10% of protein → PVS1_Strong
│           └── Removes <10% of protein → PVS1_Moderate
│
└── Full gene deletion
    └── PVS1
```

#### Duplication Variants (≥1 Exon, Completely Contained Within Gene)

```
Duplication (≥1 exon)
├── Proven in tandem
│   ├── Reading frame disrupted and NMD predicted → PVS1
│   └── No or unknown impact on reading frame and NMD → N/A
│
├── Presumed in tandem
│   └── Reading frame presumed disrupted and NMD predicted → PVS1_Strong
│
└── Proven not in tandem → N/A
```

#### Initiation Codon Variants

```
Initiation Codon
├── Different functional transcript uses alternative start codon
│   └── N/A
│
└── No known alternative start codon in other transcripts
    ├── ≥1 pathogenic variant(s) upstream of closest potential
    │   in-frame start codon → PVS1_Moderate
    │
    └── No pathogenic variant(s) upstream of closest potential
        in-frame start codon → PVS1_Supporting
```

---

### Appendix B: Criteria Applicability Summary

| Criterion | Applicability | Key Modification |
|-----------|---------------|------------------|
| PVS1 | Applicable (AR only) | LOF only for AR; use flowchart for strength |
| PS1 | Applicable | No change |
| PS2 | Applicable | No change; use SVI point system |
| PS3 | Applicable (limited) | Strong: variant-specific mouse models only; Supporting: validated assays with conditions |
| PS4 | **Not Applicable** | Use PM3 for case counting (AR) |
| PM1 | Applicable | Pore/transmembrane region AAs 4800-4950 |
| PM2 | Supporting only | FAF ≤0.00000697 (AR) |
| PM3 | Applicable | Point-based system; variant must not meet BS1 |
| PM4 | Applicable | Pore region: use either PVS1_Strong or PM4_Strong, not both |
| PM5 | Applicable | No change |
| PM6 | Applicable | No change; use PS2/PM6 point system |
| PP1 | Applicable | Segregation chart (Oza et al 2018) |
| PP2 | **Not Applicable** | RYR1 not constrained for missense |
| PP3 | Supporting only | REVEL ≥0.7 or SpliceAI ≥0.5 |
| PP4 | Supporting only | Myopathy panel negative + ≥2 specific features |
| PP5 | **Not Applicable** | Per ClinGen SVI recommendation |
| BA1 | Applicable | FAF ≥0.00697 (AR); 2 exclusion variants |
| BS1 | Applicable | FAF ≥0.000697 (AR); 2 exclusion variants |
| BS2 | Applicable | No change |
| BS3 | **Not Applicable** | Lack of effect does not count against pathogenicity for RYR1 |
| BS4 | Applicable | No change |
| BP1 | **Not Applicable** | Both missense and truncating variants cause disease |
| BP2 | Applicable | No change |
| BP3 | **Not Applicable** | No applicable regions in RYR1 |
| BP4 | Applicable | REVEL ≤0.15 or SpliceAI no impact |
| BP5 | Applicable | No change |
| BP6 | **Not Applicable** | Per ClinGen SVI recommendation |
| BP7 | Applicable | SpliceAI no impact + not highly conserved |

---

### Appendix C: Population Frequency Thresholds Summary

| Criterion | Threshold | Strength | Notes |
|-----------|-----------|----------|-------|
| BA1 | ≥0.00697 | Stand Alone | AR; FAF from gnomAD exomes or genomes; ≥2,000 alleles and >1 observation |
| BS1 | ≥0.000697 | Strong | AR; FAF from gnomAD exomes or genomes; ≥2,000 alleles and >1 observation |
| PM2 | ≤0.00000697 | Supporting | AR; population databases with ≥2,000 alleles |

**BA1/BS1 Exclusion Variants:**
- NM_000540.3:c.6721C>T (p.Arg2241Ter)
- NM_000540.3:c.10348-6C>G

---

### Appendix D: Reference PMIDs

| PMID | Reference |
|------|-----------|
| 30311386 | Oza AM, DiStefano MT et al. Expert specification of the ACMG/AMP variant interpretation guidelines for genetic hearing loss. *Hum Mutat* (2018) 39(11):1593-1613. |
| 31060725 | Saade DN, Neuhaus SB et al. The Use of Muscle Ultrasound in the Diagnosis and Differential Diagnosis of Congenital Disorders of Muscle in the Age of Next Generation Genetics. *Semin Pediatr Neurol* (2019) 29:44-54. |
| 9334205 | Tong J, Oyamada H et al. Caffeine and halothane sensitivity of intracellular Ca2+ release is altered by 15 calcium release channel (ryanodine receptor) mutations associated with malignant hyperthermia and/or central core disease. *J Biol Chem* (1997) 272(42):26332-9. |
| 32236737 | Kushnir A, Todd JJ et al. Intracellular calcium leak as a therapeutic target for RYR1-related myopathies. *Acta Neuropathol* (2020) 139(6):1089-1104. |
| 16958053 | Lyfenko AD, Ducreux S et al. Two central core disease (CCD) deletions in the C-terminal region of RYR1 alter muscle excitation-contraction (EC) coupling by distinct mechanisms. *Hum Mutat* (2007) 28(1):61-8. |
| 12704193 | Avila G, Lee EH et al. FKBP12 binding to RyR1 modulates excitation-contraction coupling in mouse skeletal myotubes. *J Biol Chem* (2003) 278(25):22600-8. |
| 16940308 | Zhou H, Yamaguchi N et al. Characterization of recessive RYR1 mutations in core myopathies. *Hum Mol Genet* (2006) 15(18):2791-803. |
| 29543229 | Biesecker LG, Harrison SM et al. ClinGen Sequence Variant Interpretation Working Group recommendations for ACMG/AMP guideline criteria PP5 and BP6. (2018) |

---

## Version History

| Version | Date | Notes |
|---------|------|-------|
| 2.0.0 | 12/12/2024 | Corrected BS1 threshold for AR variant curation. |

---

*This document was compiled from ClinGen VCEP specifications and ClinGen SVI recommendations. For the most current version, please refer to the ClinGen website.*
