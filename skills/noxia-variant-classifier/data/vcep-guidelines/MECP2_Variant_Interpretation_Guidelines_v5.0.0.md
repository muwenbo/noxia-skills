# ClinGen Rett and Angelman-like Disorders Expert Panel Variant Interpretation Guidelines for MECP2

**Version:** 5.0.0
**Released:** 7/30/2025
**Affiliation:** Rett and Angelman-like Disorders VCEP
**Based on:** Richards et al., 2015 ACMG/AMP Guidelines

---

## Gene Information

| Attribute | Value |
|-----------|-------|
| **Gene** | MECP2 (HGNC:6990) |
| **HGNC Name** | methyl-CpG binding protein 2 |
| **Transcript** | NM_004992.3 |
| **Disease** | Rett syndrome (MONDO:0010726) |
| **Inheritance** | X-linked inheritance |

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

Initiation codon variants are **not applicable** due to the MECP2E1 alternative isoform that excludes exon 1 with an alternate start codon.

For intragenic deletions/duplications that are predicted to result in a product that preserves reading frame:
- For single exon in-frame deletions, assign the same strength (PVS1 or PVS1_Moderate) as for splice site variants that preserve reading frame indicated above.
- For multiple exon in-frame deletions, PVS1 can be assigned to deletions that include single in-frame exons in the PVS1 category listed in the splice site section above OR if the exon contains a functionally important domain as specified in PM1.
- Given the extensive data available for MECP2, classifications for single or multi-exon in-frame deletions are assigned as PVS1 or PVS1_Strong. Refer to PVS1 flowchart for additional guidance.

#### Strength Levels

| Strength | Criteria |
|----------|----------|
| **Very Strong (PVS1)** | Use as defined by ClinGen SVI working group (PMID:30192042). PVS1 is applicable for: <br>- Null variants up to p.E472 <br>- Any frameshift variant that results in a read-through of the stop codon <br>- Canonical splice site variants predicted to result in an out-of-frame product <br>- Canonical splice site variants or single in-frame deletions predicted to preserve the reading frame (exon 3) <br>- A full gene deletion <br><br>PVS1 is **not** applicable for initiation codons. |
| **Strong (PVS1_Strong)** | Canonical splice site variants or deletions (single exon to full gene deletion) resulting in exon skipping or use of a cryptic splice site that disrupts reading frame and is **NOT** predicted to undergo NMD, but the truncated/altered region is critical to protein function (exon 4). |
| **Moderate (PVS1_Moderate)** | Any truncating variant distal of p.E472. |

**Modification Type:** Disease-specific

---

### PS1 - Same Amino Acid Change

**Original ACMG Summary:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.

Example: Val->Leu caused by either G>C or G>T in the same codon.

**Caveat:** Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | Same amino acid change as a previously established pathogenic variant regardless of nucleotide change. |

**Modification Type:** None

---

### PS2 - De Novo (Confirmed)

**Original ACMG Summary:** De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.

**Note:** Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.

**VCEP Specifications:**

Applicable to all genes in affected individuals identified as mosaic for the variant (as the presence of a variant in the mosaic state is confirmatory of the variant being de novo). Because of the very high de novo rate of pathogenic variants in MECP2, de novo observation can be attributed the highest value points per proband (**2 points for confirmed de novo** and **1 point for assumed de novo**) if the patient is known to be affected with a neurodevelopmental phenotype consistent with the gene.

#### Strength Levels

| Strength | Criteria |
|----------|----------|
| **Very Strong** | De novo (maternity and paternity confirmed) in a patient with the disease and no family history. <br>- ≥2 independent occurrences of PS2 <br>- ≥2 independent occurrences of PM6 and one occurrence of PS2 |
| **Strong** | De novo (maternity and paternity confirmed) in a patient with the disease and no family history. <br>- 1 occurrence of PS2 |

**Modification Type:** None

---

### PS3 - Functional Studies

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.

**Note:** Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | Well-established in vitro or in vivo functional studies supportive of a damaging effect. <br>- RNA studies that demonstrate abnormal splicing and an out-of-frame transcript. <br>- Do not use for canonical splice site variants and when PVS1 is used. |
| **Supporting** | Well-established in vitro or in vivo functional studies supportive of a damaging effect. <br>- RNA studies that demonstrate abnormal splicing and an in-frame product (unless it affects an in-frame exon specified in the PVS1 section). <br>- See included table for approved functional studies. |

**Modification Type:** Disease-specific

#### Approved Functional Assay Instances

| Assay Name | Measured Parameter | Expected Deleterious Result (PS3_Supporting) | Expected Benign Result (BS3) | References |
|------------|-------------------|---------------------------------------------|------------------------------|------------|
| **MECP2 chromatin binding assay** | Localization of MECP2 to highly methylated heterochromatic loci by quantitative immunofluorescence assay (MECP2 and DAPI co-localization) | MECP2 is distributed diffusely (no clustering pattern) | Not recommended | PMID: 27929079, 23770565, 29718204 |
| **MECP2 in vitro binding assay** | Association of MECP2 with NCoR/SMRT co-repressors | Abolished interaction by co-immunoprecipitation assay | Not recommended | PMID: 23770565, 29718204 |
| **In vitro transcription repression assay** | Luciferase activity in cell lysates co-expressing target reporters and wt or mutant MECP2 effector proteins | Abolished transcription repression activity in cells transfected with the effector construct expressing mutant MECP2 compared to constructs expressing wild type MECP2 | Not recommended | PMID: 23452848 |

---

### PS4 - Prevalence in Affected

**Original ACMG Summary:** The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.

**Note 1:** Relative risk (RR) or odds ratio (OR), as obtained from case-control studies, is >5.0 and the confidence interval around the estimate of RR or OR does not include 1.0. See manuscript for detailed guidance.

**Note 2:** In instances of very rare variants where case-control studies may not reach statistical significance, the prior observation of the variant in multiple unrelated patients with the same phenotype, and its absence in controls, may be used as moderate level of evidence.

**VCEP Specifications:**

- Detailed phenotype not needed. Need to confirm patient is 'affected with a neurodevelopmental phenotype consistent with the gene' at a minimum.
- Patient can be published OR an internal case OR observed at an outside lab (i.e. via ClinVar) OR described in the reputable databases (RettBASE). However, independent case has to be confirmed to be a different patient than yours (compare gender/age).
- **Do not use this criterion for variants where BS1 is applied or where PM2 does not apply.**

| Strength | Criteria |
|----------|----------|
| **Strong** | The prevalence of the variant in affected individuals is significantly increased compared with the prevalence in controls. <br>- 5+ observations |
| **Moderate** | The prevalence of the variant in affected individuals is significantly increased compared with the prevalence in controls. <br>- 3-4 observations |
| **Supporting** | The prevalence of the variant in affected individuals is significantly increased compared with the prevalence in controls. <br>- Use for 2nd independent occurrence |

**Modification Type:** Strength

---

### PM1 - Mutational Hot Spot

**Original ACMG Summary:** Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Moderate** | Located in a mutational hot spot and/or critical and well-established functional domain: <br>- **Methyl-DNA binding domain (MBD):** aa 90-162 <br>- **Transcriptional repression domain (TRD):** aa 302-306 |

**Modification Type:** Disease-specific

---

### PM2 - Absent from Controls

**Original ACMG Summary:** Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

**Caveat:** Population data for indels may be poorly called by next generation sequencing.

**VCEP Specification (Supporting only):**

| Strength | Criteria |
|----------|----------|
| **Supporting** | Absent/rare from controls in an ethnically-matched cohort population sample. <br>- Use if absent, zero observations in control databases. |

**Modification Type:** Strength

---

### PM3 - In Trans with Pathogenic

**Original ACMG Summary:** For recessive disorders, detected in trans with a pathogenic variant.

**Note:** This requires testing of parents (or offspring) to determine phase.

**VCEP Specifications:**

| Status | Comment |
|--------|---------|
| **Not Applicable** | Not applicable for MECP2. |

---

### PM4 - Protein Length Changes

**Original ACMG Summary:** Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | Protein length changes due to stop-loss variants. <br>- PM4_Strong is applicable to stop-loss variants in *MECP2*, as several stop loss variants in this gene have been described in affected individuals. |
| **Moderate** | Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants. <br>- **Do not use PM4** for in-frame deletions/insertions in the Proline-rich region of gene (p.381-p.405) |
| **Supporting** | Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants. <br>- Smaller in-frame events (< 3 amino acid residues) unless they occur in a functionally important region (see PM1 for functionally important domains for each gene). |

**Modification Type:** Disease-specific, Strength

---

### PM5 - Novel Missense at Same Residue

**Original ACMG Summary:** Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.

Example: Arg156His is pathogenic; now you observe Arg156Cys.

**Caveat:** Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | Missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before. <br>- ≥2 different missense changes affecting the amino acid residue. <br>- **Do not apply PM1 in these situations.** |
| **Moderate** | Missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before. <br>- A Grantham or BLOSUM score comparison can be used to determine if the variant is predicted to be as or more damaging than the established pathogenic variant. |

**Modification Type:** Strength

---

### PM6 - De Novo (Assumed)

**Original ACMG Summary:** Assumed de novo, but without confirmation of paternity and maternity.

**VCEP Specifications:**

Because of the very high de novo rate of pathogenic variants in MECP2, de novo observation can be attributed the highest value points per proband (**2 points for confirmed de novo** and **1 point for assumed de novo**) if the patient is known to be affected with a neurodevelopmental phenotype consistent with the gene.

| Strength | Criteria |
|----------|----------|
| **Very Strong** | Confirmed de novo without confirmation of paternity and maternity. <br>- ≥4 independent occurrences of PM6. <br>- Evidence from literature must be fully evaluated to support independent events. |
| **Strong** | Confirmed de novo without confirmation of paternity and maternity. <br>- ≥2 independent occurrences of PM6. <br>- Evidence from literature must be fully evaluated to support independent events. |
| **Moderate** | Confirmed de novo without confirmation of paternity and maternity. <br>- 1 occurrence of PM6. |

**Modification Type:** Strength

---

### PP1 - Co-segregation

**Original ACMG Summary:** Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.

**Note:** May be used as stronger evidence with increasing segregation data.

**VCEP Specifications:**

**Note:** Individuals must have disease consistent with reported phenotype (even if on the mild end of spectrum of the disease).

| Strength | Criteria |
|----------|----------|
| **Strong** | Co-segregation with disease in multiple affected family members. <br>- ≥5 informative meiosis |
| **Moderate** | Co-segregation with disease in multiple affected family members. <br>- 3-4 informative meiosis |
| **Supporting** | Co-segregation with disease in multiple affected family members. <br>- 2 informative meiosis |

**Modification Type:** Strength

---

### PP2 - Missense in Constrained Gene

**Original ACMG Summary:** Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.

**VCEP Specifications:**

| Status | Comment |
|--------|---------|
| **Not Applicable** | Not applicable for MECP2. |

---

### PP3 - Computational Evidence

**Original ACMG Summary:** Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).

**Caveat:** As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Supporting** | Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.). <br>- For missense variants use **REVEL with a score ≥ 0.644**. <br>- For splice site variants use **SpliceAI with a score ≥ 0.2**. |

**Modification Type:** General recommendation

---

### PP4 - Phenotype Specificity

**Original ACMG Summary:** Patient's phenotype or family history is highly specific for a disease with a single genetic etiology.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Supporting** | Phenotype specific for disease with single genetic etiology. <br>- See gene specific clinical phenotype guidelines below. |

**Modification Type:** Disease-specific

#### MECP2 Clinical Phenotype Guidelines

**Core Phenotype (need to be met for PP4):**
- Regression of developmental progress AND loss of at least 2 of 4 of the following:
  - Loss, partial or complete of fine motor skills (hand use)
  - Loss, partial or complete of spoken communication
  - Abnormal (dyspraxic) or absent gait
  - Stereotypies

**Supportive Criteria** (do not need to be met for PP4; however, in the absence of one core phenotype, two or more supportive phenotypes can be used in its place):
- Periodic breathing (breath-holding/hyperventilation) when awake
- Bruxism when awake
- Impaired sleep pattern
- Abnormal muscle tone
- Peripheral vasomotor disturbances
- Scoliosis/kyphosis
- Growth retardation (small stature)
- Small, cold hands and feet
- Inappropriate laughing/screaming spells
- Diminished response to pain
- Intense eye communication ("eye pointing")

**Additional Notes:** If information is provided such that a phenotype of Rett syndrome is suspected, with specific minimal features used for the diagnosis, then this can be used for PP4 in lieu of the specific clinical features listed.

---

### PP5 - Reputable Source

**Original ACMG Summary:** Reputable source recently reports variant as pathogenic, but the evidence is not available to the laboratory to perform an independent evaluation.

**VCEP Specifications:**

| Status | Comment |
|--------|---------|
| **Not Applicable** | This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee. (PMID: 29543229) |

---

## Benign Criteria

### BA1 - Allele Frequency >5%

**Original ACMG Summary:** Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

**VCEP Specifications:**

The frequency cutoffs are based on MECP2 expected disease allele frequency (1 in 10,000 for the disease prevalence / (1.5 alleles [assumes 50/50 male/female ratio] * 0.8 for 80% penetrance)). MECP2 is the most prevalent of the genes covered in the Rett/Angelman-like working group and was chosen as most conservative number.

| Strength | Criteria |
|----------|----------|
| **Stand Alone** | Use large population databases (i.e. gnomAD). <br>- Use if variant is present at **≥0.000083 (0.0083%)** in any sub-population. <br>- Use if allele frequency is met in any general continental population dataset of at least 2,000 observed alleles. |

**Modification Type:** Disease-specific

---

### BS1 - Frequency Greater Than Expected

**Original ACMG Summary:** Allele frequency is greater than expected for disorder.

**VCEP Specifications:**

The frequency cutoffs are based on MECP2 expected disease allele frequency divided by 10-fold. MECP2 is the most prevalent of the genes covered in the Rett/Angelman-like working group and was chosen as most conservative number.

| Strength | Criteria |
|----------|----------|
| **Strong** | Use large population databases (i.e. gnomAD). <br>- Use if variant is present at **≥0.0000083 (0.00083%)** and **<0.000083 (0.0083%)** in any sub-population. <br>- Use if allele frequency is met in any general continental population dataset of at least 2,000 observed alleles. |

**Modification Type:** Disease-specific

---

### BS2 - Observed in Healthy Adult

**Original ACMG Summary:** Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

**VCEP Specifications:**

- Should be applied in cases where the healthy adult is devoid of neurodevelopmental phenotypes.
- Best to use with internal curated data that includes clinical information or published patients that have been phenotyped.

| Strength | Criteria |
|----------|----------|
| **Strong** | Observed in the heterozygous/hemizygous state in a healthy adult. <br>- 2 unaffected (related or unrelated) heterozygotes or hemizygotes. |
| **Supporting** | Observed in the heterozygous/hemizygous state in a healthy adult. <br>- 1 unaffected (related or unrelated) heterozygote or hemizygote |

**Modification Type:** Strength

---

### BS3 - Functional Studies (No Effect)

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | Well-established in vitro or in vivo functional studies shows no damaging effect on protein function. <br>- RNA functional studies that demonstrate no impact on splicing and transcript composition. It can be downgraded based on quality of data. <br>- **Not applicable for other functional studies.** |

**Modification Type:** Disease-specific

**Note:** As indicated in the functional assay table above, BS3 is "Not recommended" for the approved MECP2 functional assays (chromatin binding, in vitro binding, and transcription repression assays).

---

### BS4 - Lack of Segregation

**Original ACMG Summary:** Lack of segregation in affected members of a family.

**Caveat:** The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.

**VCEP Specifications:**

Need to confirm that the family member is 'affected with a neurodevelopmental phenotype consistent with the gene' at a minimum.

| Strength | Criteria |
|----------|----------|
| **Strong** | Lack of segregation in affected members of a family. <br>- Absent in a similarly affected family member, when seen in two or more families |
| **Supporting** | Lack of segregation in affected members of a family. <br>- Absent in a similarly affected family member |

**Modification Type:** Strength

---

### BP1-BP7 - Benign Supporting

| Criterion | Status | Specifications |
|-----------|--------|----------------|
| **BP1** | Not Applicable | Not applicable for MECP2. |
| **BP2** | Applicable (Supporting) | Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder. <br><br>**VCEP Note:** Knock out of MECP2 results in embryonic lethality/drastic phenotype. |
| **BP3** | Applicable (Supporting) | In-frame deletions/insertions in a repetitive region without a known function. <br><br>BP3 is applicable if there are in-frame deletions/duplications in a repetitive region where other in-frame deletions/duplications have been observed with an overall frequency commensurate with the BA1 threshold for this gene. |
| **BP4** | Applicable (Supporting) | Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc). <br><br>- For missense variants use **REVEL with a score ≤ 0.290**. <br>- For splice site variants use **SpliceAI with a score ≤ 0.1**. |
| **BP5** | Applicable (Supporting to Strong) | Variant found in a case with an alternate molecular basis for disease. <br><br>**VCEP Note:** For example, if a variant in MECP2 is identified in a patient with lissencephaly in whom a pathogenic variant is identified in the PAFAH1B1 gene. **Do not apply if variant is de novo.** <br><br>- **Strong:** ≥3 cases with alternate molecular basis for disease <br>- **Moderate:** 2 cases with alternate molecular basis for disease <br>- **Supporting:** 1 case with alternate molecular basis for disease |
| **BP6** | Not Applicable | This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee. (PMID: 29543229) |
| **BP7** | Applicable (Supporting) | A synonymous (silent) variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved. <br><br>- Defined 'not highly conserved' regions as those with PhastCons score <1 and/or PhyloP score <0.1 and/or the variant is the reference nucleotide in one primate and/or three mammal species. <br>- For splice site variants use **SpliceAI with a score ≤ 0.1**. <br><br>**VCEP Note:** For silent variants BP4 and BP7 can be added. |

---

## Rules for Combining Criteria

### Pathogenic Classification

| Criteria Combination |
|---------------------|
| 1 Very Strong **AND** ≥1 Strong |
| 1 Very Strong **AND** ≥2 Moderate |
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
| ≥2 Strong |
| 1 Stand Alone (BA1) |

### Likely Benign Classification

| Criteria Combination |
|---------------------|
| 1 Strong **AND** 1 Supporting |
| ≥2 Supporting |

---

## Appendices

### Appendix A: PVS1 Decision Tree for MECP2

**Transcript:** NM_004992.3

#### Nonsense or Frameshift Variants

| Condition | Outcome |
|-----------|---------|
| Predicted to undergo NMD, exon is present in biologically-relevant transcript(s) | **PVS1** |
| Predicted to undergo NMD, exon is absent from biologically-relevant transcript(s) | **N/A** |
| Not predicted to undergo NMD, upstream of most distal de novo LOF variant (p.E472) OR a frameshift variant that results in read-through of stop codon | **PVS1** |
| Not predicted to undergo NMD, downstream of most distal de novo LOF variant (p.E472) | **PVS1_Moderate** |

#### Canonical Splice Site Variants (GT--AG at +/-1,2 positions)

| Condition | Outcome |
|-----------|---------|
| Exon skipping or use of cryptic splice site disrupts reading frame and is predicted to undergo NMD, exon is present in biologically-relevant transcript(s) | **PVS1** |
| Exon skipping or use of cryptic splice site disrupts reading frame and is predicted to undergo NMD, exon is absent from biologically-relevant transcript(s) | **N/A** |
| Exon skipping or use of cryptic splice site disrupts reading frame and is NOT predicted to undergo NMD (Exon 4), truncated/altered region is critical to protein function | **PVS1_Strong** |
| Exon skipping or use of cryptic splice site preserves reading frame (Exon 3), truncated/altered region is critical to protein function | **PVS1** |

#### Deletions (Single Exon to Full Gene)

| Condition | Outcome |
|-----------|---------|
| Full gene deletion | **PVS1** |
| Single to multi exon deletion - Disrupts reading frame and is predicted to undergo NMD, exon is present in biologically-relevant transcript(s) | **PVS1** |
| Single to multi exon deletion - Disrupts reading frame and is predicted to undergo NMD, exon is absent from biologically-relevant transcript(s) | **N/A** |
| Single to multi exon deletion - Disrupts reading frame and is NOT predicted to undergo NMD (Exon 4), truncated/altered region is critical to protein function | **PVS1_Strong** |
| Single to multi exon deletion - Preserves reading frame (Exon 3), truncated/altered region is critical to protein function | **PVS1** |

#### Duplications (≥1 exon, completely contained within gene)

| Condition | Outcome |
|-----------|---------|
| Proven in tandem, reading frame disrupted and NMD predicted to occur | **PVS1** |
| Proven in tandem, no or unknown impact on reading frame and NMD | **N/A** |
| Presumed in tandem, reading frame presumed disrupted and NMD predicted to occur | **PVS1_Strong** |
| Proven not in tandem | **N/A** |

#### Initiation Codon Variants

| Condition | Outcome |
|-----------|---------|
| Different functional transcript (MECP2E1) uses alternative start codon | **N/A** |

---

### Appendix B: Population Frequency Thresholds Summary

| Criterion | Threshold | Strength |
|-----------|-----------|----------|
| BA1 | ≥0.000083 (0.0083%) | Stand Alone |
| BS1 | ≥0.0000083 (0.00083%) and <0.000083 (0.0083%) | Strong |
| PM2 | Absent (0 observations) | Supporting |

---

### Appendix C: Computational Prediction Thresholds

| Criterion | Tool | Pathogenic Threshold | Benign Threshold |
|-----------|------|---------------------|------------------|
| PP3/BP4 (Missense) | REVEL | ≥0.644 | ≤0.290 |
| PP3/BP4 (Splice) | SpliceAI | ≥0.2 | ≤0.1 |
| BP7 (Synonymous/Splice) | SpliceAI | - | ≤0.1 |
| BP7 (Conservation) | PhastCons | - | <1 |
| BP7 (Conservation) | PhyloP | - | <0.1 |

---

### Appendix D: Functional Domains

| Domain | Amino Acid Range | Relevant Criteria |
|--------|------------------|-------------------|
| Methyl-DNA binding domain (MBD) | aa 90-162 | PM1 |
| Transcriptional repression domain (TRD) | aa 302-306 | PM1 |
| Proline-rich region (not for PM4) | aa 381-405 | PM4 exclusion zone |
| Region distal to p.E472 | >p.E472 | PVS1_Moderate zone |

---

### Appendix E: Reference PMIDs

| Reference | Citation | Relevant Criteria |
|-----------|----------|-------------------|
| PMID: 30192042 | ClinGen SVI working group PVS1 recommendations | PVS1 |
| PMID: 29543229 | ClinGen SVI recommendations on PP5/BP6 | PP5, BP6 |
| PMID: 11242117 | Guy J, Hendrich B et al. A mouse Mecp2-null mutation causes neurological symptoms that mimic Rett syndrome. Nat Genet (2001) 27(3):322-6 | BP2 |
| PMID: 11469283 | Erlandson A, Hallberg B et al. MECP2 mutation screening in Swedish classical Rett syndrome females. Eur Child Adolesc Psychiatry (2001) 10(2):117-21 | PM4 |
| PMID: 36413997 | Pejaver V, Byrne AB et al. Calibration of computational tools for missense variant pathogenicity classification and ClinGen recommendations for PP3/BP4 criteria. Am J Hum Genet (2022) 109(12):2163-2177 | PP3, BP4 |
| PMID: 27929079 | Functional assay reference | PS3 |
| PMID: 23770565 | Functional assay reference | PS3 |
| PMID: 29718204 | Functional assay reference | PS3 |
| PMID: 23452848 | Functional assay reference | PS3 |

---

### Appendix F: Criteria Summary Table

| Criterion | Default Strength | VCEP Modified Strengths | Status |
|-----------|-----------------|------------------------|--------|
| PVS1 | Very Strong | Very Strong, Strong, Moderate | Applicable |
| PS1 | Strong | Strong | Applicable |
| PS2 | Strong | Very Strong, Strong | Applicable |
| PS3 | Strong | Strong, Supporting | Applicable |
| PS4 | Strong | Strong, Moderate, Supporting | Applicable |
| PM1 | Moderate | Moderate | Applicable |
| PM2 | Moderate | Supporting | Applicable |
| PM3 | Moderate | - | Not Applicable |
| PM4 | Moderate | Strong, Moderate, Supporting | Applicable |
| PM5 | Moderate | Strong, Moderate | Applicable |
| PM6 | Moderate | Very Strong, Strong, Moderate | Applicable |
| PP1 | Supporting | Strong, Moderate, Supporting | Applicable |
| PP2 | Supporting | - | Not Applicable |
| PP3 | Supporting | Supporting | Applicable |
| PP4 | Supporting | Supporting | Applicable |
| PP5 | Supporting | - | Not Applicable |
| BA1 | Stand Alone | Stand Alone | Applicable |
| BS1 | Strong | Strong | Applicable |
| BS2 | Strong | Strong, Supporting | Applicable |
| BS3 | Strong | Strong | Applicable |
| BS4 | Strong | Strong, Supporting | Applicable |
| BP1 | Supporting | - | Not Applicable |
| BP2 | Supporting | Supporting | Applicable |
| BP3 | Supporting | Supporting | Applicable |
| BP4 | Supporting | Supporting | Applicable |
| BP5 | Supporting | Strong, Moderate, Supporting | Applicable |
| BP6 | Supporting | - | Not Applicable |
| BP7 | Supporting | Supporting | Applicable |

---

## Version History

| Version | Date | Description |
|---------|------|-------------|
| 5.0.0 | 7/30/2025 | Modification to the population frequency cutoffs for BA1 and BS1. |

---

*This document was compiled from ClinGen VCEP specifications and ClinGen SVI recommendations. For the most current version, please refer to the ClinGen website.*
