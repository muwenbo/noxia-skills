# ClinGen Congenital Myopathies Expert Panel Variant Interpretation Guidelines for NEB

**Version:** 1.0.0
**Released:** 8/7/2024
**Affiliation:** Congenital Myopathies VCEP
**Based on:** Richards et al., 2015 ACMG/AMP Guidelines

---

## Gene Information

| Attribute | Value |
|-----------|-------|
| **Gene** | NEB (HGNC:7720) |
| **HGNC Name** | nebulin |
| **Transcripts** | NM_001164507.1, NM_001164508.2 |
| **Disease** | Nemaline myopathy (MONDO:0018958) |
| **Inheritance** | Autosomal recessive inheritance |

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

**VCEP Specifications:** See PVS1 flowchart (Appendix A). Specified critical regions in NEB that should also receive PVS1 are listed below and in the PVS1 flowchart.

**Gene-Specific Notes:**
- In-frame deletions due to the repetitive nature of NEB, particularly in exon 55, are deleterious and pathogenic (Anderson 2004 PMID:15221447, Lehtokari 2009 PMID:19232495).
- Exons 161-183 are critical functional regions (Pelin 1999 PMID:10051637).
- NMD boundary: c.25354, p.8452.
- In-frame exons: 3-180, 182.
- Biologically-relevant transcripts: NM_001164508.2, NM_001164507.2.

#### Strength Levels

| Strength | Criteria |
|----------|----------|
| **Very Strong** | Null variant predicted to undergo NMD in biologically-relevant transcript(s); OR truncated/altered region is critical to protein function (exons 55, 161-183); OR full gene deletion. See PVS1 flowchart for complete decision tree. |
| **Strong** | In-frame deletions due to the repetitive nature of NEB, particularly in exon 55 (Anderson 2004, Lehtokari 2009). The majority of NEB exons are in frame (exons 3-180, 182); thus, skipping of in-frame exons should be scored at PVS1_Strong. Also applies when variant removes >10% of protein and LoF variants in the exon are not frequent in the general population. |
| **Moderate** | See PVS1 flowchart. Applies when role of region in protein function is unknown and variant removes <10% of protein, or other scenarios per flowchart. |
| **Supporting** | See PVS1 flowchart. Applies to initiation codon variants with no pathogenic variant(s) upstream of closest potential in-frame start codon. |

#### PVS1 Decision Tree Summary

**Nonsense or Frameshift:**
- Predicted to undergo NMD (before c.25354) AND exon present in biologically-relevant transcript(s) → **PVS1**
- Not predicted to undergo NMD:
  - Truncated region critical (exons 55, 161-183) → **PVS1**
  - Region unknown + removes >10% protein → **PVS1_Strong**
  - Region unknown + removes <10% protein → **PVS1_Moderate**
  - LoF variants frequent in exon / exon absent from biologically-relevant transcripts → **N/A**

**Canonical Splice Variants (GT-AG, +/-1,2):**
- Exon skipping disrupts reading frame + predicted NMD → **PVS1**
- Exon skipping preserves reading frame (in-frame exons: 3-180, 182):
  - Truncated region critical (exons 55, 161-183) → **PVS1**
  - Region unknown + removes >10% protein → **PVS1_Strong**
  - Region unknown + removes <10% protein → **PVS1_Moderate**
  - LoF variants frequent / exon absent → **N/A**
- Exon skipping disrupts frame + NOT predicted NMD: same logic as above for critical regions and protein removal percentage

**Deletions (single exon to full gene):**
- Full gene deletion → **PVS1**
- Disrupts reading frame + NMD predicted → **PVS1**
- Preserves reading frame:
  - Truncated region critical (exons 55, 161-183) → **PVS1**
  - Region unknown + removes >10% protein → **PVS1_Strong**
  - Region unknown + removes <10% protein → **PVS1_Moderate**
- Disrupts frame + NOT predicted NMD: same logic as above

**Duplications (>=1 exon, completely within gene):**
- Proven in tandem + reading frame disrupted + NMD predicted → **PVS1**
- Proven in tandem + no/unknown impact on reading frame → **N/A**
- Presumed in tandem + reading frame presumed disrupted + NMD predicted → **PVS1_Strong**
- Proven not in tandem → **N/A**

**Initiation Codon:**
- Different functional transcript uses alternative start codon → **N/A**
- No known alternative start codon:
  - >=1 pathogenic variant(s) upstream of closest potential in-frame start codon → **PVS1_Moderate**
  - No pathogenic variant(s) upstream → **PVS1_Supporting**

---

### PS1 - Same Amino Acid Change

**Original ACMG Summary:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change. Example: Val->Leu caused by either G>C or G>T in the same codon. Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:** No change from original ACMG guidelines.

| Strength | Criteria |
|----------|----------|
| **Strong** | Same amino acid change as a previously established pathogenic variant regardless of nucleotide change. Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level. |
| **Moderate** | No change - use as originally described |
| **Supporting** | No change - use as originally described |

---

### PS2 - De Novo (Confirmed)

**Original ACMG Summary:** De novo (both maternity and paternity confirmed) in a patient with the disease and no family history. Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.

**VCEP Specifications:** No change from original ACMG guidelines. Use the SVI-recommended point-based system.

| Strength | Criteria |
|----------|----------|
| **Strong** | De novo (both maternity and paternity confirmed) in a patient with the disease and no family history. |
| **Moderate** | No change - use as originally described |
| **Supporting** | No change - use as originally described |

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

---

### PS3 - Functional Studies

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product. Note: Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | Strong may only be considered for variant-specific mouse models. Currently, no other assays are applicable at this strength. *(Modification: Disease-specific)* |
| **Moderate** | The two assays from PS3_Supporting may be stacked to reach Moderate strength. *(Modification: Gene-specific)* |
| **Supporting** | Two specific assays are currently suggested to be applied at Supporting: (1) **Thin filament structure** - an abnormal readout consists of a significant difference in intensity reflections of X-ray diffraction patterns generated by muscle fibers from patient biopsies compared to WT; (2) **In vitro motility** - an abnormal readout consists of a significant difference in speed of single fibers derived from patient muscle compared to WT. If not listed above, it is acceptable to use PS3_Supporting for other functional analyses if: the assay has been validated by a known pathogenic and benign variant AND there is plausible reason that the function the assay is testing relates to the phenotype AND the assay conditions are likely to mimic the physiological environment. *(Modification: Gene-specific)* |

#### Approved Assay Instances

**Assay 1: In Vitro Motility**

| Attribute | Details |
|-----------|---------|
| **PMID** | 21350120 |
| **Author** | Ochala...Larsson (2011) |
| **DOI** | 10.1096/fj.10-176727 |
| **Description** | The in vitro motility of single fibers derived from patient and control muscle in the presence of rhodamine-phalloidin-labeled actin filaments was measured. |
| **Material** | Single muscle fiber preparations from biopsies from nemaline myopathy patient and healthy subjects |
| **Readout** | Quantitative - in vitro motility speed |
| **Normal threshold** | No statistically significant difference in speed compared to wild type |
| **Abnormal threshold** | Statistically significant difference in speed compared to wild type |
| **Approved** | Yes |
| **Proposed strength** | Supporting |
| **Variants evaluated** | c.36+2dupT; c.2106+3A>C |
| **Notes** | Patient-derived muscle fibers; compound heterozygous splice variants associated with reduced levels of intact nebulin (~30% reduction vs controls) |

**Assay 2: Thin Filament Structure (Instance 1 - Patient Biopsies)**

| Attribute | Details |
|-----------|---------|
| **PMID** | 21350120 |
| **Author** | Ochala...Larsson (2011) |
| **DOI** | 10.1096/fj.10-176727 |
| **Description** | The X-ray diffraction pattern of arrays of ~30 single fibers derived from patient and control muscle were recorded in two buffer conditions (preactivating and activating with pCa 4.5). |
| **Material** | Single muscle fiber preparations from biopsies from nemaline myopathy patient and healthy subjects |
| **Readout** | Quantitative - reflection intensities at the second, sixth, and seventh actin layer lines (ALLs) normalized to total intensity of sixth ALL in absence of calcium |
| **Normal threshold** | No statistically significant difference in intensity reflections compared to wild type |
| **Abnormal threshold** | Statistically significant difference in intensity reflections compared to wild type |
| **Approved** | Yes |
| **Proposed strength** | Supporting |
| **Variants evaluated** | c.36+2dupT; c.2106+3A>C |
| **Notes** | Patient-derived muscle fibers; compound heterozygous splice variants associated with reduced levels of intact nebulin (~30% reduction vs controls) |

**Assay 3: Thin Filament Structure (Instance 2 - Mouse Model)**

| Attribute | Details |
|-----------|---------|
| **PMID** | 32483185 |
| **Author** | Lindqvist...Granzier (2020) |
| **DOI** | 10.1038/s41467-020-16526-9 |
| **Description** | The X-ray diffraction pattern of intact extensor digitorum longus muscles derived from wild type mice and the compound heterozygous variant mouse model were recorded at rest and after activation. |
| **Material** | Intact muscle fibers isolated from wild type mice and the compound heterozygous NebS6366I/DeltaExon55 mouse model |
| **Readout** | Quantitative - spacing of 27A meridional reflection (thin filament stiffness), sixth and seventh ALLs spacing, actin radius, second ALL intensity, meridional third-order troponin intensity ratio, thin-thick filament spacing |
| **Normal threshold** | No statistically significant difference in intensity reflections compared to wild type |
| **Abnormal threshold** | Statistically significant difference in reflection measurements compared to wild type |
| **Approved** | Yes |
| **Proposed strength** | Supporting |
| **Variants evaluated** | c.19097G>T (p.Ser6366Ile) (homozygous or compound heterozygous with exon 55 deletion) |

---

### PS4 - Prevalence in Affected

**Original ACMG Summary:** The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls. Note 1: Relative risk (RR) or odds ratio (OR), as obtained from case-control studies, is >5.0 and the confidence interval around the estimate of RR or OR does not include 1.0. Note 2: In instances of very rare variants where case-control studies may not reach statistical significance, the prior observation of the variant in multiple unrelated patients with the same phenotype, and its absence in controls, may be used as moderate level of evidence.

**VCEP Specifications:** NEB is associated with Autosomal Recessive disease; PS4 can only be used for case-control studies and not proband counting. Please use PM3 for individual case observations.

| Strength | Criteria |
|----------|----------|
| **Strong** | Case-control studies only. RR or OR >5.0, CI does not include 1.0. Not for proband counting - use PM3 instead. *(Modification: Disease-specific, Gene-specific)* |
| **Moderate** | Same restriction - case-control studies only, not proband counting. Use PM3 for individual cases. *(Modification: Gene-specific)* |
| **Supporting** | Same restriction - case-control studies only, not proband counting. Use PM3 for individual cases. *(Modification: Gene-specific)* |

---

### PM1 - Mutational Hot Spot

**Original ACMG Summary:** Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.

**VCEP Specifications:** ***Not Applicable***

> There are no defined hotspots or critical functional domains in NEB at this time.

---

### PM2 - Absent from Controls

**Original ACMG Summary:** Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium. Caveat: Population data for indels may be poorly called by next generation sequencing.

**VCEP Specification (Supporting only):**
- PM2_Supporting may be applied if the minor allele frequency in population databases of at least 2,000 alleles is **<=0.0000559**
- 1 allele is allowed

*(Modification: Disease-specific, Gene-specific)*

---

### PM3 - In Trans with Pathogenic

**Original ACMG Summary:** For recessive disorders, detected in trans with a pathogenic variant. Note: This requires testing of parents (or offspring) to determine phase.

**VCEP Specifications:** Please use the SVI-recommended PM3 chart to count observations. Points for each proband should be summed to get to a final PM3 strength. In order to count case counts for your variant of interest, it should be rare enough to not meet BS1.

#### PM3 Point System (Per Proband)

| Classification/Zygosity of Other Variant | Confirmed in Trans | Phase Unknown |
|------------------------------------------|-------------------|---------------|
| Pathogenic or Likely pathogenic variant | 1.0 | 0.5 (P) / 0.25 (LP) |
| Homozygous (non-consanguineous) | 1.0 | 1.0 |
| Homozygous (consanguineous, max 0.5/family) | 0.5 | 0.5 |
| VUS (max 0.5 total) | 0.25 | 0.0 |

#### PM3 Evidence Strength Thresholds

| Total Points | Strength Level |
|--------------|----------------|
| 0.5 | PM3_Supporting |
| 1.0 | PM3 (Moderate) |
| 2.0 | PM3_Strong |
| 4.0 | PM3_VeryStrong |

*(Modification: Disease-specific)*

---

### PM4 - Protein Length Changes

**Original ACMG Summary:** Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

**VCEP Specifications:** Either PVS1_Strong or PM4_Strong, but not both, should be used for in-frame deletions in NEB.

| Strength | Criteria |
|----------|----------|
| **Strong** | In-frame deletions due to the repetitive nature of NEB, particularly in exon 55, are deleterious and pathogenic (Anderson 2004 PMID:15221447, Lehtokari 2009 PMID:19232495). *(Modification: Gene-specific)* |
| **Moderate** | Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants. No change from original. |
| **Supporting** | No change - use as originally described |

> **Important:** Either PVS1_Strong or PM4_Strong should be applied for in-frame deletions in NEB, but not both simultaneously.

---

### PM5 - Novel Missense at Same Residue

**Original ACMG Summary:** Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before. Example: Arg156His is pathogenic; now you observe Arg156Cys. Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:** No change from original ACMG guidelines.

| Strength | Criteria |
|----------|----------|
| **Strong** | No change - use as originally described |
| **Moderate** | Novel missense change at an amino acid residue where a different pathogenic missense change has been seen before. Caveat: Beware of changes that impact splicing. |
| **Supporting** | No change - use as originally described |

---

### PM6 - De Novo (Assumed)

**Original ACMG Summary:** Assumed de novo, but without confirmation of paternity and maternity.

**VCEP Specifications:** No change from original ACMG guidelines. Use the same PS2/PM6 point-based system described above.

| Strength | Criteria |
|----------|----------|
| **Strong** | No change - use as originally described |
| **Moderate** | No change - use as originally described |
| **Supporting** | No change - use as originally described |

---

### PP1 - Co-segregation

**Original ACMG Summary:** Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease. Note: May be used as stronger evidence with increasing segregation data.

**VCEP Specifications:** The segregation chart (adopted from Oza et al 2018 PMID:30311386) should be used to determine the strength level of the total number of affected and unaffected segregations. In order to count unaffected segregations, the unaffected individuals can be heterozygous carriers or WT, but should have the same risk of inheriting the variant as the affected individuals (e.g. siblings in the same generation).

#### PP1 General Thresholds

| | Supporting | Moderate | Strong |
|---|---|---|---|
| **Likelihood** | 4:1 | 16:1 | 32:1 |
| **LOD Score** | 0.6 | 1.2 | 1.5 |
| **Autosomal dominant threshold** | 2 affected segregations | 4 affected segregations | 5 affected segregations |
| **Autosomal recessive threshold** | See Table 5 | See Table 5 | See Table 5 |

#### Segregation Table for Autosomal Recessive (LOD Scores)

*General recommendations (phenocopy not an issue). Rows = affected segregations, Columns = unaffected recessive segregations.*

| Affected \ Unaffected | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **0** | 0 | 0.12 | 0.25 | 0.37 | 0.5 | 0.62 | 0.75 | 0.87 | 1 | 1.12 | 1.25 |
| **1** | 0.6 | 0.73 | 0.85 | 0.98 | 1.1 | 1.23 | 1.35 | 1.48 | 1.6 | 1.73 | 1.85 |
| **2** | 1.2 | 1.33 | 1.45 | 1.58 | 1.7 | 1.83 | 1.95 | 2.08 | 2.2 | 2.33 | 2.45 |
| **3** | 1.81 | 1.93 | 2.06 | 2.18 | 2.31 | 2.43 | 2.56 | 2.68 | 2.81 | 2.93 | 3.06 |
| **4** | 2.41 | 2.53 | 2.66 | 2.78 | 2.91 | 3.03 | 3.16 | 3.28 | 3.41 | 3.53 | 3.66 |
| **5** | 3.01 | 3.14 | 3.26 | 3.39 | 3.51 | 3.63 | 3.76 | 3.88 | 4.01 | 4.13 | 4.26 |
| **6** | 3.61 | 3.74 | 3.86 | 3.99 | 4.11 | 4.24 | 4.36 | 4.49 | 4.61 | 4.74 | 4.86 |
| **7** | 4.21 | 4.34 | 4.46 | 4.59 | 4.71 | 4.84 | 4.96 | 5.09 | 5.21 | 5.34 | 5.46 |
| **8** | 4.82 | 4.94 | 5.07 | 5.19 | 5.32 | 5.44 | 5.57 | 5.69 | 5.82 | 5.94 | 6.07 |
| **9** | 5.42 | 5.54 | 5.67 | 5.79 | 5.92 | 6.04 | 6.17 | 6.29 | 6.42 | 6.54 | 6.67 |
| **10** | 6.02 | 6.15 | 6.27 | 6.4 | 6.52 | 6.65 | 6.77 | 6.9 | 7.02 | 7.15 | 7.27 |

*Color coding: LOD <0.6 = not met; 0.6-<1.2 = Supporting (PP1); 1.2-<1.5 = Moderate (PP1_Moderate); >=1.5 = Strong (PP1_Strong)*

---

### PP2 - Missense in Constrained Gene

**Original ACMG Summary:** Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.

**VCEP Specifications:** ***Not Applicable***

> NEB is not a gene that is constrained for missense variation. Hence PP2 is not applicable.

---

### PP3 - Computational Evidence

**Original ACMG Summary:** Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.). Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.

**VCEP Specifications (Supporting only):**

PP3 is met if:
- **REVEL score >=0.7**, OR
- The variant is predicted to impact splicing using **SpliceAI score >=0.5**

*(Modification: General recommendation)*

---

### PP4 - Phenotype Specificity

**Original ACMG Summary:** Patient's phenotype or family history is highly specific for a disease with a single genetic etiology.

**VCEP Specifications (Supporting):**

PP4 is met with the presence of any of these features:

**Presence on Muscle Biopsy of:**
- Nemaline rods
- Shorter thin filaments

**Functional assays performed upon patient muscle biopsy indicate:**
- Significantly altered calcium sensitivity
- Significantly altered muscle mechanics (altered force-sarcomere length or reduced contractile strength and force generation)

*(Modification: Disease-specific, Gene-specific)*

---

### PP5 - Reputable Source

**Original ACMG Summary:** Reputable source recently reports variant as pathogenic, but the evidence is not available to the laboratory to perform an independent evaluation.

**VCEP Specifications:** ***Not Applicable***

> This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PMID: 29543229).

---

## Benign Criteria

### BA1 - Allele Frequency >5%

**Original ACMG Summary:** Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

**VCEP Specification (Stand Alone):**
- The minor allele frequency using the filtering allele frequency of either exomes or genomes in gnomAD is **>=0.00559**
- All populations used should have at least 2,000 alleles and >1 observation
- The Ashkenazi Jewish, European Finnish, and Other populations in gnomAD will **not** be used for BA1 application

**BA1 Exclusion Variants** (well-known pathogenic variants that are above the specified BA1 threshold):
1. Exon 55 deletion common in the AJ population (NM_001271208.2:c.7431+1919_7536+374del)
2. NM_001271208.2:c.19097G>T (p.Ser6366Ile)
3. NM_001271208.2:c.22249A>C (p.Thr7417Pro)

*(Modification: Disease-specific, Gene-specific)*

---

### BS1 - Frequency Greater Than Expected

**Original ACMG Summary:** Allele frequency is greater than expected for disorder.

**VCEP Specification (Strong):**
- The minor allele frequency using the filtering allele frequency of either exomes or genomes in gnomAD is **>=0.000237** in continental populations
- All populations used should have at least 2,000 alleles and >1 observation

*(Modification: Disease-specific, Gene-specific)*

---

### BS2 - Observed in Healthy Adult

**Original ACMG Summary:** Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

**VCEP Specifications:** No change from original ACMG guidelines.

| Strength | Criteria |
|----------|----------|
| **Strong** | Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age. |
| **Moderate** | No change - use as originally described |
| **Supporting** | No change - use as originally described |

---

### BS3 - Functional Studies (No Effect)

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Moderate** | The two assays from BS3_Supporting may be stacked to reach Moderate strength. *(Modification: Gene-specific)* |
| **Supporting** | Two specific assays are currently suggested to be applied at Supporting: (1) **Thin filament structure** - a normal readout consists of no significant difference in intensity reflections of X-ray diffraction patterns generated by muscle fibers from patient biopsies compared to WT; (2) **In vitro motility** - a normal readout consists of no significant difference in speed of single fibers derived from patient muscle compared to WT. *(Modification: Gene-specific)* |

---

### BS4 - Lack of Segregation

**Original ACMG Summary:** Lack of segregation in affected members of a family. Caveat: The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.

**VCEP Specifications:** No change from original ACMG guidelines.

| Strength | Criteria |
|----------|----------|
| **Strong** | Lack of segregation in affected members of a family. Caveat applies regarding phenocopies. |
| **Moderate** | No change - use as originally described |
| **Supporting** | No change - use as originally described |

---

### BP1-BP7 - Benign Supporting

| Criterion | Status | Comment |
|-----------|--------|---------|
| **BP1** | *Not Applicable* | Both missense and truncating variants in NEB are disease-causing. |
| **BP2** | Applicable (no change) | Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder or observed in cis with a pathogenic variant in any inheritance pattern. Available at Supporting, Moderate, and Strong. |
| **BP3** | *Not Applicable* | There are no regions in NEB where BP3 would apply. |
| **BP4** | Applicable (Supporting) | BP4 is met if the REVEL score <=0.15 or if the variant is not predicted to impact splicing using SpliceAI. *(General recommendation)* |
| **BP5** | Applicable (no change) | Variant found in a case with an alternate molecular basis for disease. Available at Supporting, Moderate, and Strong. |
| **BP6** | *Not Applicable* | This criterion is not for use as recommended by the ClinGen SVI VCEP Review Committee (PMID: 29543229). |
| **BP7** | Applicable (Supporting) | A synonymous variant for which SpliceAI predicts no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved. *(General recommendation)* |

---

## Rules for Combining Criteria

### Pathogenic Classification

| Criteria Combination |
|---------------------|
| 1 Very Strong *(PVS1, PS2_VeryStrong, PS3_VeryStrong, PS4_VeryStrong, PM3_VeryStrong)* **AND** >=1 Strong *(PVS1_Strong, PS1, PS2, PS3, PS4, PM3_Strong, PM4_Strong, PM5_Strong, PM6_Strong, PP1_Strong, PP3_Strong, PP4_Strong)* |
| 1 Very Strong **AND** >=2 Moderate *(PVS1_Moderate, PS1_Moderate, PS2_Moderate, PS3_Moderate, PS4_Moderate, PM3, PM4, PM5, PM6, PP1_Moderate, PP3_Moderate, PP4_Moderate)* |
| 1 Very Strong **AND** 1 Moderate **AND** 1 Supporting *(PVS1_Supporting, PS1_Supporting, PS2_Supporting, PS3_Supporting, PS4_Supporting, PM2_Supporting, PM3_Supporting, PM4_Supporting, PM5_Supporting, PM6_Supporting, PP1, PP3, PP4)* |
| 1 Very Strong **AND** >=2 Supporting |
| >=2 Strong |
| 1 Strong **AND** >=3 Moderate |
| 1 Strong **AND** 2 Moderate **AND** >=2 Supporting |
| 1 Strong **AND** 1 Moderate **AND** >=4 Supporting |

### Likely Pathogenic Classification

| Criteria Combination |
|---------------------|
| 1 Very Strong **AND** 1 Moderate |
| 1 Strong **AND** 1 Moderate |
| 1 Strong **AND** >=2 Supporting |
| >=3 Moderate |
| 2 Moderate **AND** >=2 Supporting |
| 1 Moderate **AND** >=4 Supporting |
| 1 Strong **AND** 2 Moderate |

### Benign Classification

| Criteria Combination |
|---------------------|
| >=2 Strong *(BS1, BS2, BS4, BP2_Strong, BP5_Strong, BP7_Strong)* |
| 1 Stand Alone *(BA1)* |

### Likely Benign Classification

| Criteria Combination |
|---------------------|
| 1 Strong *(BS1, BS2, BS4, BP2_Strong, BP5_Strong, BP7_Strong)* **AND** 1 Supporting *(BS2_Supporting, BS3_Supporting, BS4_Supporting, BP2, BP4, BP5, BP7)* |
| >=2 Supporting *(BS2_Supporting, BS3_Supporting, BS4_Supporting, BP2, BP4, BP5, BP7)* |

---

## Appendices

### Appendix A: PVS1 Flowchart

The PVS1 decision tree for NEB follows the ClinGen SVI PVS1 flowchart framework with the following NEB-specific annotations:

- **Biologically-relevant transcripts:** NM_001164508.2, NM_001164507.2
- **NMD boundary:** c.25354 (p.8452)
- **In-frame exons:** 3-180, 182
- **Critical functional regions:** Exons 55, 161-183
- **Key references:**
  - Anderson 2004 (PMID:15221447) - Exon 55 deletion
  - Lehtokari 2009 (PMID:19232495) - Exon 55 deletion worldwide
  - Pelin 1999 (PMID:10051637) - Exons 161-183

See the separate PVS1 decision tree document for the full flowchart.

### Appendix B: Reference PMIDs

| PMID | Reference |
|------|-----------|
| 15221447 | Anderson SL, Ekstein J et al. *Nemaline myopathy in the Ashkenazi Jewish population is caused by a deletion in the nebulin gene.* **Hum Genet** (2004) 115(3):185-90. DOI: 10.1007/s00439-004-1140-8 |
| 19232495 | Lehtokari VL, Greenleaf RS et al. *The exon 55 deletion in the nebulin gene--one single founder mutation with world-wide occurrence.* **Neuromuscul Disord** (2009) 19(3):179-81. DOI: 10.1016/j.nmd.2008.12.001 |
| 10051637 | Pelin K, Hilpela P et al. *Mutations in the nebulin gene associated with autosomal recessive nemaline myopathy.* **Proc Natl Acad Sci U S A** (1999) 96(5):2305-10. DOI: 10.1073/pnas.96.5.2305 |
| 30311386 | Oza AM, DiStefano MT et al. *Expert specification of the ACMG/AMP variant interpretation guidelines for genetic hearing loss.* **Hum Mutat** (2018) 39(11):1593-1613. DOI: 10.1002/humu.23630 |
| 29543229 | Biesecker LG, Harrison SM et al. *ClinGen Sequence Variant Interpretation Working Group recommendations for ACMG/AMP guideline criteria PP5 and BP6.* (2018) |
| 21350120 | Ochala J...Larsson L. *Thin filament structure functional assay.* **FASEB J** (2011). DOI: 10.1096/fj.10-176727 |
| 32483185 | Lindqvist J...Granzier H. *Thin filament X-ray diffraction in compound heterozygous mouse model.* **Nat Commun** (2020). DOI: 10.1038/s41467-020-16526-9 |

### Appendix C: Population Frequency Thresholds Summary

| Criterion | Threshold | Strength | Notes |
|-----------|-----------|----------|-------|
| BA1 | >=0.00559 | Stand Alone | Filtering AF in gnomAD exomes or genomes; >=2,000 alleles and >1 observation required; exclude AJ, European Finnish, and Other populations. 3 BA1 exclusion variants defined. |
| BS1 | >=0.000237 | Strong | Filtering AF in gnomAD exomes or genomes in continental populations; >=2,000 alleles and >1 observation required. |
| PM2 | <=0.0000559 | Supporting | In population databases of >=2,000 alleles; 1 allele allowed. |

### Appendix D: Criteria Applicability Summary

| Criterion | Status | Max Strength | Modification Type |
|-----------|--------|--------------|-------------------|
| PVS1 | Applicable | Very Strong | Gene-specific |
| PS1 | Applicable | Strong | No change |
| PS2 | Applicable | Strong | No change |
| PS3 | Applicable | Strong | Disease-specific / Gene-specific |
| PS4 | Applicable (case-control only) | Strong | Disease-specific / Gene-specific |
| PM1 | **Not Applicable** | - | - |
| PM2 | Applicable (Supporting only) | Supporting | Disease-specific / Gene-specific |
| PM3 | Applicable | Very Strong | Disease-specific |
| PM4 | Applicable | Strong | Gene-specific |
| PM5 | Applicable | Strong | No change |
| PM6 | Applicable | Strong | No change |
| PP1 | Applicable | Strong | General recommendation |
| PP2 | **Not Applicable** | - | - |
| PP3 | Applicable (Supporting only) | Supporting | General recommendation |
| PP4 | Applicable (Supporting only) | Supporting | Disease-specific / Gene-specific |
| PP5 | **Not Applicable** | - | - |
| BA1 | Applicable | Stand Alone | Disease-specific / Gene-specific |
| BS1 | Applicable | Strong | Disease-specific / Gene-specific |
| BS2 | Applicable | Strong | No change |
| BS3 | Applicable | Moderate | Gene-specific |
| BS4 | Applicable | Strong | No change |
| BP1 | **Not Applicable** | - | - |
| BP2 | Applicable | Strong | No change |
| BP3 | **Not Applicable** | - | - |
| BP4 | Applicable (Supporting only) | Supporting | General recommendation |
| BP5 | Applicable | Strong | No change |
| BP6 | **Not Applicable** | - | - |
| BP7 | Applicable (Supporting only) | Supporting | General recommendation |

---

## Version History

| Version | Date | Description |
|---------|------|-------------|
| 1.0.0 | 8/7/2024 | Initial release of NEB-specific ACMG/AMP criteria specifications by the Congenital Myopathies VCEP |

---

*This document was compiled from ClinGen VCEP specifications and ClinGen SVI recommendations. For the most current version, please refer to the ClinGen website.*
