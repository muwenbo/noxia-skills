# ClinGen Rett and Angelman-like Disorders VCEP Variant Interpretation Guidelines for TCF4

**Version:** 5.0.0
**Released:** 7/30/2025
**Affiliation:** Rett and Angelman-like Disorders VCEP
**Based on:** Richards et al., 2015 ACMG/AMP Guidelines

**Release Notes:** Modification to the population frequency cutoffs for BA1 and BS1.

---

## Gene Information

| Attribute | Value |
|-----------|-------|
| **Gene** | TCF4 (HGNC:11634) |
| **HGNC Name** | transcription factor 4 |
| **Transcript** | NM_001083962.1 |
| **Disease** | Pitt-Hopkins syndrome (MONDO:0012589) |
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

**VCEP Specifications:**

Refer to PVS1 flow chart (Appendix A) for additional guidance.

For intragenic deletions/duplications that are predicted to result in a product that preserves the reading frame:
- For single exon in-frame deletions, assign the same strength (PVS1) as for splice site variants that preserve reading frame indicated above.
- For multiple exon in-frame deletions, PVS1 can be assigned to deletions that include single in-frame exons in the PVS1 category listed in the splice site section above OR if the exon contains a functionally important domain as specified in PM1.
- Given the extensive data available for TCF4, classifications for single or multi-exon in-frame deletions are assigned as PVS1 or PVS1_Strong. Refer to PVS1 flow chart for additional guidance.

#### Strength Levels

| Strength | Criteria |
|----------|----------|
| **Very Strong** | Null variant in a gene where loss of function is a known mechanism of disease. Use as defined by ClinGen SVI working group (PMID:30192042). PVS1 can be applied for: **1)** Null variants up to p.E643 (the distal most de novo truncating variant in an affected patient reported to date); **2)** Any frameshift variant that results in a read-through of the stop codon; **3)** Canonical splice site variants predicted to result in an out-of-frame product; **4)** Canonical splice site variants or single in-frame deletions predicted to preserve the reading frame (exon 15); **5)** In-frame deletions including the PM1 functional domains (p.E564_V617 (bHLH)); **6)** Deletions and duplications >=1 exon in size (completely contained within the TCF4 gene) where the reading frame is disrupted and NMD is predicted to occur; **7)** Exon skipping or single exon deletion of exon 19 predicted to disrupt the reading frame but is not predicted to undergo NMD; **8)** A full gene deletion. |
| **Strong** | PVS1_Strong is applicable for single to multi exon deletions that preserve the reading frame and the variant removes <10% of the protein. |
| **Moderate** | PVS1_Moderate is applicable for any truncating variant distal of p.E643 and for single exon deletions that involve just non-coding exon 20. |
| **Supporting** | PVS1_Supporting is applicable for initiation codon variants in TCF4. |

#### PVS1 Flowchart Summary

**Nonsense or Frameshift:**
- Predicted to undergo NMD AND exon is present in biologically-relevant transcript(s) → **PVS1**
- Predicted to undergo NMD AND exon is absent from biologically-relevant transcript(s) → **N/A**
- Not predicted to undergo NMD AND downstream of the most distal de novo LOF variant (p.E643) but does not result in a read-through of the stop codon → **PVS1_Moderate**
- Not predicted to undergo NMD AND upstream of most de novo distal LOF variant (p.E643) OR frameshift that results in a read-through of the stop codon → **PVS1**

**Deletion (Single exon to full gene):**
- Single to multi exon deletion disrupts reading frame and is predicted to undergo NMD → **PVS1**
- Single to multi exon deletion disrupts reading frame and is NOT predicted to undergo NMD (Exon 19) → **PVS1**
- Single to multi exon deletion preserves reading frame:
  - Truncated/altered region is critical to protein function (Exon 15 + any in-frame combination that includes the PM1 functional domain p.E564_V617 (bHLH)) → **PVS1**
  - Variant removes >10% of protein → **PVS1**
  - Variant removes <10% of protein → **PVS1_Strong**
  - Role of region in protein function is unknown → **N/A**
  - Exon 19 (truncated/altered region is critical to protein function) → **PVS1**
- Single exon deletion involving non-coding exon 20 → **PVS1_Moderate**
- Full gene deletion → **PVS1**

**Canonical GT-AG +/-1,2 Splice Sites:**
- Exon skipping or use of a cryptic splice site disrupts reading frame and is predicted to undergo NMD AND exon is present in biologically-relevant transcript(s) → **PVS1**
- Exon skipping or use of a cryptic splice site disrupts reading frame and is NOT predicted to undergo NMD (Exon 19) → **PVS1**
- Exon skipping or use of a cryptic splice site preserves reading frame:
  - Truncated/altered region is critical to protein function (Exon 15) → **PVS1**
  - Exon is absent from biologically-relevant transcript(s) → **N/A**

**Duplication (>=1 exon in size, must be completely contained within gene):**
- Proven in tandem → Reading frame presumed disrupted and NMD predicted to occur → **PVS1**
- Presumed in tandem → Reading frame disrupted and NMD predicted to occur → **N/A**
- Proven not in tandem → No or unknown impact on reading frame and NMD → **PVS1_Supporting**

**Initiation Codon:**
- No pathogenic variant(s) upstream of closest potential in-frame start codon AND no known alternative start codon in other medically relevant transcripts → **PVS1_Supporting**

---

### PS1 - Same Amino Acid Change

**Original ACMG Summary:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | Same amino acid change as a previously established pathogenic variant regardless of nucleotide change. *(No modification from original ACMG)* |

> **Caveat:** Beware of changes that impact splicing rather than at the amino acid/protein level.

---

### PS2 - De Novo (Confirmed)

**Original ACMG Summary:** De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.

**VCEP Specifications:**

- Applicable to all genes in affected individuals identified as mosaic for the variant (as the presence of a variant in the mosaic state is confirmatory of the variant being de novo).
- Because of the very high de novo rate of pathogenic variants in TCF4, de novo observation can be attributed the highest value points per proband (**2 points for confirmed de novo** and **1 point for assumed de novo**) if the patient is known to be affected with a neurodevelopmental phenotype consistent with the gene.
- Evidence from literature must be fully evaluated to support independent events.

#### PS2 Strength Levels

| Strength | Criteria |
|----------|----------|
| **Very Strong** | >=2 independent occurrences of PS2; OR >=2 independent occurrences of PM6 and one occurrence of PS2. |
| **Strong** | De novo (maternity and paternity confirmed) in a patient with the disease and no family history. *(No modification from original ACMG)* |

#### PS2/PM6 Point System

| Phenotypic Consistency | Confirmed De Novo (PS2) | Assumed De Novo (PM6) |
|------------------------|------------------------|-----------------------|
| Phenotype highly specific for gene | 2 points | 1 point |
| Phenotype consistent but not highly specific | 1 point | 0.5 points |
| Phenotype consistent + high genetic heterogeneity | 0.5 points | 0.25 points |
| Phenotype not consistent | 0 points | 0 points |

**Note:** For TCF4, because of the very high de novo rate, de novo observation can be attributed the highest value points per proband (2 points for confirmed de novo and 1 point for assumed de novo) if the patient is known to be affected with a neurodevelopmental phenotype consistent with the gene.

#### PS2/PM6 Evidence Strength Thresholds

| Points | Strength Level |
|--------|----------------|
| 0.5 | Supporting |
| 1.0 | Moderate |
| 2.0 | Strong |
| 4.0 | Very Strong |

---

### PS3 - Functional Studies

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | RNA studies that demonstrate abnormal splicing and an **out-of-frame** transcript. Do not use for canonical splice site variants and when PVS1 is used. |
| **Supporting** | RNA studies that demonstrate abnormal splicing and an **in-frame** product (unless it affects an in-frame exon specified in the PVS1 section). See included table for acceptable functional studies. |

#### Approved Assay Instances

| Assay | Measured Parameter | PS3_Supporting (Deleterious Result Range) | BS3 | References |
|-------|-------------------|------------------------------------------|-----|------------|
| **Subcellular localization assay** | Subcellular distribution | Localization different compared to wild type TCF4 (e.g. accumulated in nuclear dots, no nuclear accumulation) | Not recommended | PMID: 22460224, 22777675 |
| **Homogenous time-resolved fluorescence assay (protein-protein interaction)** | Homodimer formation (with itself) and heterodimer formation (with other bHLH transcription factors) | Localization different compared to wild type TCF4 (e.g. accumulated in nuclear dots, no nuclear accumulation) | Not recommended | PMID: 22777675 |
| **Luciferase assay (transcriptional activity)** | Transcriptional activation of E-box containing promoter reporter constructs | p-value <0.05 compared to wild type luciferase activity | Not recommended | PMID: 17436255, 19235238, 22460224, 22777675 |
| **Electrophoretic mobility shift assay (EMSA)** | DNA binding activity of homo- and heterodimers | Comparison to wild type possible however no robust threshold available | Not recommended | PMID: 22460224 |
| **Western blot** | Protein expression and stability | Comparison to wild type possible however no robust threshold available | Not recommended | PMID: 22460224 |
| **Co-fractionation** | Localization to the chromatin | p-value <0.05 compared to wild type TCF4. Localization to the soluble fraction | Not recommended | PMID: 22460224 |

> **Note:** All approved functional assays for TCF4 are applicable at **PS3_Supporting** strength only. BS3 is **not recommended** for any of the approved functional assays.

---

### PS4 - Prevalence in Affected

**Original ACMG Summary:** The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.

**VCEP Specifications:**

- Detailed phenotype not needed. Need to confirm patient is "affected with a neurodevelopmental phenotype consistent with the gene" at a minimum.
- Patient can be published OR an internal case OR observed at an outside lab (i.e. via ClinVar). However, the independent case has to be confirmed to be a different patient than yours (compare gender/age).
- Do not use this criterion for variants where BS1 is applied or where PM2 does not apply.

| Strength | Criteria |
|----------|----------|
| **Strong** | 5+ observations in unrelated affected individuals. |
| **Moderate** | 3-4 observations in unrelated affected individuals. |
| **Supporting** | Use for 2nd independent occurrence. |

---

### PM1 - Mutational Hot Spot

**Original ACMG Summary:** Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Moderate** | Located in the **Basic Helix-Loop-Helix domain (bHLH): amino acids 564-617** |

---

### PM2 - Absent from Controls

**Original ACMG Summary:** Absent from controls (or at extremely low frequency if recessive) in population databases.

**VCEP Specification (Supporting only):**
- Use if **absent (zero observations)** in control databases.
- Applicable at **Supporting** strength only.

---

### PM3 - In Trans with Pathogenic

**Original ACMG Summary:** For recessive disorders, detected in trans with a pathogenic variant.

**VCEP Specifications:** **Not applicable for TCF4** (autosomal dominant disorder).

---

### PM4 - Protein Length Changes

**Original ACMG Summary:** Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Moderate** | Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants. *(No modification from original ACMG)* |
| **Supporting** | Smaller in-frame events (<3 amino acid residues) unless they occur in a functionally important region (see PM1 for functionally important domains). |

---

### PM5 - Novel Missense at Same Residue

**Original ACMG Summary:** Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | >=2 different missense changes affecting the amino acid residue have been determined to be pathogenic. **Do not apply PM1 in these situations.** |
| **Moderate** | A missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before. A Grantham or BLOSUM score comparison can be used to determine if the variant is predicted to be as or more damaging than the established pathogenic variant. *(No modification from original ACMG)* |

> **Caveat:** Beware of changes that impact splicing rather than at the amino acid/protein level.

---

### PM6 - De Novo (Assumed)

**Original ACMG Summary:** Assumed de novo, but without confirmation of paternity and maternity.

**VCEP Specifications:** Same as PS2 - use point-based system above.

- Evidence from literature must be fully evaluated to support independent events.
- Because of the very high de novo rate of pathogenic variants in TCF4, de novo observation can be attributed the highest value points per proband (2 points for confirmed de novo and 1 point for assumed de novo) if the patient is known to be affected with a neurodevelopmental phenotype consistent with the gene.

| Strength | Criteria |
|----------|----------|
| **Very Strong** | >=4 independent occurrences of PM6. |
| **Strong** | >=2 independent occurrences of PM6. |
| **Moderate** | Confirmed de novo without confirmation of paternity and maternity. *(No change from original ACMG)* |

---

### PP1 - Co-segregation

**Original ACMG Summary:** Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.

**VCEP Specifications:**

> **Note:** Individuals must have disease consistent with reported phenotype (even if on the mild end of spectrum of the disease).

| Strength | Informative Meioses | Criteria |
|----------|---------------------|----------|
| **Strong** | >=5 informative meioses | Co-segregation with disease in multiple affected family members. |
| **Moderate** | 3-4 informative meioses | Co-segregation with disease in multiple affected family members. |
| **Supporting** | 2 informative meioses | Co-segregation with disease in multiple affected family members. |

---

### PP2 - Missense in Constrained Gene

**Original ACMG Summary:** Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.

**VCEP Specifications:** **Not applicable for TCF4.**

---

### PP3 - Computational Evidence

**Original ACMG Summary:** Multiple lines of computational evidence support a deleterious effect on the gene or gene product.

**VCEP Specifications:**

| Variant Type | Tool | Threshold for PP3 |
|-------------|------|-------------------|
| Missense | REVEL | Score **>= 0.644** |
| Splice site | SpliceAI | Score **>= 0.2** |

---

### PP4 - Phenotype Specificity

**Original ACMG Summary:** Patient's phenotype or family history is highly specific for a disease with a single genetic etiology.

**VCEP Specifications:** Phenotype specific for disease with single genetic etiology. See gene-specific clinical phenotype guidelines below.

#### TCF4 Clinical Phenotype Guidelines

**Core phenotype** (need to be met for PP4):
- Global developmental delay
- Intellectual disability
- Behavioral problems (anxiety)
- Hand flapping
- Characteristic Facial Features (become more apparent with age):
  - Deeply set eyes with prominent supraorbital ridges
  - Mildly up-slanted palpebral fissures
  - Broad nasal root, wide nasal ridge, and wide nasal base with enlarged nostrils
  - Overhanging or depressed nasal tip, which may be pointed
  - Short philtrum
  - Thick vermilion of the lower lip, which is often everted
  - Widely spaced teeth

**Supportive criteria** (do not need to be met for PP4; however, in the absence of one core phenotype, two or more supportive phenotypes can be used in its place):
- Prominence of the lower face with a well-developed chin; with age the lower face becomes more prominent and facial features may coarsen
- Mildly cupped ears with over-folded helices
- In some individuals, wide mouth with downturned corners and exaggerated Cupid's bow or tented vermilion of the upper lip
- Happy, excitable, frequent smiling, laughter
- Episodic periodic breathing

**Additional notes:** If information is provided such that a phenotype of Pitt-Hopkins syndrome is suspected, with specific minimal features used for the diagnosis, then this can be used for PP4 in lieu of the specific clinical features listed.

---

### PP5 - Reputable Source

**Original ACMG Summary:** Reputable source recently reports variant as pathogenic, but the evidence is not available to the laboratory to perform an independent evaluation.

**VCEP Specifications:** **Not applicable.** This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PMID: 29543229).

---

## Benign Criteria

### BA1 - Allele Frequency >5%

**Original ACMG Summary:** Allele frequency is above 5% in population databases.

**VCEP Specification (Stand Alone):**
- gnomAD allele frequency **>= 0.000083 (0.0083%)** in any sub-population
- Use large population databases (i.e. gnomAD).
- Use if allele frequency is met in any general continental population dataset of at least 2,000 observed alleles.

> **Note:** The frequency cutoffs are based on MECP2 expected disease allele frequency (1 in 10,000 for the disease prevalence / (1.5 alleles [assumes 50/50 male/female ratio] x 0.8 for 80% penetrance)). MECP2 is the most prevalent of the genes covered in the Rett/Angelman-like working group and was chosen as the most conservative number.

---

### BS1 - Frequency Greater Than Expected

**Original ACMG Summary:** Allele frequency is greater than expected for disorder.

**VCEP Specification (Strong):**
- gnomAD allele frequency **>= 0.0000083 (0.00083%)** AND **< 0.000083 (0.0083%)** in any sub-population
- Use large population databases (i.e. gnomAD).
- Use if allele frequency is met in any general continental population dataset of at least 2,000 observed alleles.

> **Note:** The frequency cutoffs are based on MECP2 expected disease allele frequency divided by 10-fold.

---

### BS2 - Observed in Healthy Adult

**Original ACMG Summary:** Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

**VCEP Specifications:**

- Should be applied in cases where the healthy adult is devoid of neurodevelopmental phenotypes.
- Best to use with internal curated data that includes clinical information or published patients that have been phenotyped.

| Strength | Criteria |
|----------|----------|
| **Strong** | 2 unaffected (related or unrelated) heterozygotes observed in the heterozygous state in a healthy adult. |
| **Supporting** | 1 unaffected (related or unrelated) heterozygote observed in the heterozygous state in a healthy adult. |

---

### BS3 - Functional Studies (No Effect)

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | RNA functional studies that demonstrate no impact on splicing and transcript composition. It can be downgraded based on quality of data. Not applicable for other functional studies. |

> **Note:** BS3 is **not recommended** for any of the approved protein-level functional assays (subcellular localization, HTRF, luciferase, EMSA, Western blot, co-fractionation).

---

### BS4 - Lack of Segregation

**Original ACMG Summary:** Lack of segregation in affected members of a family.

**VCEP Specifications:**

- Need to confirm that the family member is "affected with a neurodevelopmental phenotype consistent with the gene" at a minimum.

| Strength | Criteria |
|----------|----------|
| **Strong** | Absent in a similarly affected family member, when seen in two or more families. |
| **Supporting** | Absent in a similarly affected family member. |

---

### BP1-BP7 - Benign Supporting

| Criterion | Status | Strength | Specifications |
|-----------|--------|----------|----------------|
| **BP1** | **Not Applicable** | — | Not applicable for TCF4. |
| **BP2** | Applicable | Supporting | Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder; or observed in cis with a pathogenic variant in any inheritance pattern. Applicable for TCF4 for **in trans state**. Knock out of TCF4 results in embryonic lethality/drastic phenotype. |
| **BP3** | Applicable | Supporting | In-frame deletions/insertions in a repetitive region without a known function. BP3 is applicable if there are in-frame deletions/duplications in a repetitive region where other in-frame deletions/duplications have been observed with an overall frequency commensurate with the BA1 threshold for this gene. |
| **BP4** | Applicable | Supporting | For missense variants use **REVEL with a score <= 0.290**. For splice site variants use **SpliceAI with a score <= 0.1**. |
| **BP5** | Applicable | Supporting–Strong | Variant found in a case with an alternate molecular basis for disease. Do not apply if variant is de novo. **Supporting:** 1 case; **Moderate:** 2 cases; **Strong:** >=3 cases with alternate molecular basis for disease. (e.g. a variant in TCF4 identified in a patient with lissencephaly in whom a pathogenic variant is identified in the PAFAH1B1 gene.) |
| **BP6** | **Not Applicable** | — | Not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PMID: 29543229). |
| **BP7** | Applicable | Supporting | A synonymous (silent) variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved. Defined "not highly conserved" regions as those with PhastCons score <1 and/or PhyloP score <0.1 and/or the variant is the reference nucleotide in one primate and/or three mammal species. For splice site variants use **SpliceAI with a score <= 0.1**. For silent variants **BP4 and BP7 can both be applied**. |

---

## Rules for Combining Criteria

### Pathogenic Classification

| Criteria Combination |
|---------------------|
| 1 Very Strong **AND** >=1 Strong |
| 1 Very Strong **AND** >=2 Moderate |
| 1 Very Strong **AND** 1 Moderate **AND** 1 Supporting |
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
| >=2 Strong |
| 1 Stand Alone (BA1) |

### Likely Benign Classification

| Criteria Combination |
|---------------------|
| 1 Strong **AND** 1 Supporting |
| >=2 Supporting |

---

## Appendices

### Appendix A: PVS1 Flowchart

The PVS1 flowchart for TCF4 (NM_001083962.1) provides decision trees for the following variant types:

#### Nonsense or Frameshift
```
Predicted to undergo NMD?
├── YES → Exon present in biologically-relevant transcript(s)?
│   ├── YES → PVS1
│   └── NO  → N/A
└── NO  → Downstream of most distal de novo LOF variant (p.E643)?
    ├── Does not result in read-through of stop codon → PVS1_Moderate
    └── Upstream of p.E643 OR results in read-through of stop codon → PVS1
```

#### Deletion (Single exon to full gene)
```
Reading frame disrupted?
├── YES, NMD predicted → PVS1
├── YES, NMD NOT predicted (Exon 19) → PVS1
├── Reading frame preserved
│   ├── Critical to protein function (Exon 15, PM1 domain) → PVS1
│   ├── Removes >10% of protein → PVS1
│   ├── Removes <10% of protein → PVS1_Strong
│   ├── Region function unknown → N/A
│   └── Exon 19 critical → PVS1
├── Non-coding exon 20 only → PVS1_Moderate
└── Full gene deletion → PVS1
```

#### Canonical GT-AG +/-1,2 Splice Sites
```
Exon skipping/cryptic splice site outcome?
├── Disrupts reading frame, NMD predicted, exon in relevant transcript → PVS1
├── Disrupts reading frame, NMD NOT predicted (Exon 19) → PVS1
├── Preserves reading frame
│   ├── Critical to protein function (Exon 15) → PVS1
│   └── Exon absent from relevant transcript → N/A
```

#### Duplication (>=1 exon, completely contained within gene)
```
Tandem status?
├── Proven in tandem → Reading frame disrupted, NMD predicted → PVS1
├── Presumed in tandem → N/A
└── Proven not in tandem → PVS1_Supporting
```

#### Initiation Codon
```
No pathogenic variant upstream of closest potential in-frame start codon
AND no known alternative start codon → PVS1_Supporting
```

### Appendix B: Reference PMIDs

| PMID | Reference |
|------|-----------|
| 22045651 | Whalen S, Heron D, et al. Novel comprehensive diagnostic strategy in Pitt-Hopkins syndrome: clinical score and further delineation of the TCF4 mutational spectrum. *Hum Mutat* (2012) 33(1):64-72. |
| 17436254 | Amiel J, Rio M, et al. Mutations in TCF4, encoding a class I basic helix-loop-helix transcription factor, are responsible for Pitt-Hopkins syndrome, a severe epileptic encephalopathy associated with autonomic dysfunction. *Am J Hum Genet* (2007) 80(5):988-93. |
| 17878293 | Flora A, Garcia JJ, et al. The E-protein Tcf4 interacts with Math1 to regulate differentiation of a specific subset of neuronal progenitors. *Proc Natl Acad Sci U S A* (2007) 104(39):15382-7. |
| 29695756 | Mary L, Piton A, et al. Disease-causing variants in TCF4 are a frequent cause of intellectual disability: lessons from large-scale sequencing approaches in diagnosis. *Eur J Hum Genet* (2018) 26(7):996-1006. |
| 36413997 | Pejaver V, Byrne AB, et al. Calibration of computational tools for missense variant pathogenicity classification and ClinGen recommendations for PP3/BP4 criteria. *Am J Hum Genet* (2022) 109(12):2163-2177. |
| 30192042 | ClinGen SVI Working Group. Recommendations for interpreting the loss of function PVS1 ACMG/AMP variant criterion. |
| 29543229 | ClinGen SVI recommendation on PP5/BP6 criteria deprecation. |
| 22460224 | Functional assay reference for subcellular localization, luciferase, EMSA, Western blot, and co-fractionation assays. |
| 22777675 | Functional assay reference for subcellular localization and HTRF protein-protein interaction assays. |
| 17436255 | Functional assay reference for luciferase transcriptional activity assay. |
| 19235238 | Functional assay reference for luciferase transcriptional activity assay. |

### Appendix C: Population Frequency Thresholds Summary

| Criterion | Threshold | Strength |
|-----------|-----------|----------|
| BA1 | >= 0.000083 (0.0083%) in any sub-population | Stand Alone |
| BS1 | >= 0.0000083 (0.00083%) and < 0.000083 (0.0083%) in any sub-population | Strong |
| PM2 | Absent (zero observations) in control databases | Supporting |

> **Note:** Frequency thresholds require a minimum of 2,000 observed alleles in the general continental population dataset. Thresholds are based on MECP2 expected disease allele frequency as the most conservative estimate across the Rett/Angelman-like working group.

### Appendix D: Computational Prediction Thresholds Summary

| Criterion | Variant Type | Tool | Pathogenic Threshold | Benign Threshold |
|-----------|-------------|------|---------------------|------------------|
| PP3 / BP4 | Missense | REVEL | >= 0.644 (PP3) | <= 0.290 (BP4) |
| PP3 / BP4 | Splice site | SpliceAI | >= 0.2 (PP3) | <= 0.1 (BP4/BP7) |

### Appendix E: Criteria Applicability Summary

| Criterion | Applicable? | Max Strength | Modification Type |
|-----------|-------------|-------------|-------------------|
| PVS1 | Yes | Very Strong | Disease-specific |
| PS1 | Yes | Strong | None |
| PS2 | Yes | Very Strong | Strength |
| PS3 | Yes | Strong | Disease-specific |
| PS4 | Yes | Strong | Strength |
| PM1 | Yes | Moderate | Disease-specific |
| PM2 | Yes | Supporting | Strength |
| PM3 | **No** | — | Not applicable (AD disorder) |
| PM4 | Yes | Moderate | Strength (Supporting for small events) |
| PM5 | Yes | Strong | Strength |
| PM6 | Yes | Very Strong | Strength |
| PP1 | Yes | Strong | Strength |
| PP2 | **No** | — | Not applicable |
| PP3 | Yes | Supporting | Clarification |
| PP4 | Yes | Supporting | Disease-specific |
| PP5 | **No** | — | Not recommended (SVI) |
| BA1 | Yes | Stand Alone | Disease-specific |
| BS1 | Yes | Strong | Disease-specific |
| BS2 | Yes | Strong | Strength |
| BS3 | Yes | Strong | Disease-specific |
| BS4 | Yes | Strong | Strength |
| BP1 | **No** | — | Not applicable |
| BP2 | Yes | Supporting | Disease-specific |
| BP3 | Yes | Supporting | None |
| BP4 | Yes | Supporting | General recommendation |
| BP5 | Yes | Strong | Strength |
| BP6 | **No** | — | Not recommended (SVI) |
| BP7 | Yes | Supporting | None |

---

## Version History

| Version | Date | Notes |
|---------|------|-------|
| 5.0.0 | 7/30/2025 | Modification to the population frequency cutoffs for BA1 and BS1. |

---

*This document was compiled from ClinGen Rett and Angelman-like Disorders VCEP specifications for TCF4 (Version 5.0.0). For the most current version, please refer to the [ClinGen website](https://clinicalgenome.org).*
