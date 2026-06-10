# ClinGen Rett and Angelman-like Disorders Expert Panel Variant Interpretation Guidelines for SLC9A6

**Version:** 5.0.0
**Released:** 7/30/2025
**Affiliation:** Rett and Angelman-like Disorders VCEP
**Based on:** Richards et al., 2015 ACMG/AMP Guidelines

**Release Notes:** Modification to the population frequency cutoffs for BA1 and BS1.

---

## Gene Information

| Attribute | Value |
|-----------|-------|
| **Gene** | SLC9A6 (HGNC:11079) |
| **HGNC Name** | solute carrier family 9 member A6 |
| **Transcript** | NM_006359.2 |
| **Disease** | Christianson syndrome (MONDO:0010278) |
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

Caveats:
- Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7).
- Use caution interpreting LOF variants at the extreme 3' end of a gene.
- Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact.
- Use caution in the presence of multiple transcripts.

**VCEP Specifications:**

Refer to PVS1 flowchart for additional guidance.

For intragenic deletions/duplications that are predicted to result in a product that preserves reading frame:
- For single exon in-frame deletions assign the same strength (PVS1, PVS1_Strong, or PVS1_Moderate) as for splice site variants that preserve reading frame indicated above.
- For multiple exon in-frame deletions, PVS1 can be assigned to deletions that include single in-frame exons in the PVS1 category above (exon 3 or exon 10).

#### Strength Levels

| Strength | Criteria |
|----------|----------|
| **Very Strong** | Use as defined by ClinGen SVI working group (PMID:30192042). PVS1 is applicable for: **Null variants up to p.A563**; Canonical splice site variants predicted to result in an out-of-frame product; Canonical splice site variants predicted to preserve the reading frame (exon 10); Multiple in-frame exon deletions that include exon 10; Single exon 3 or 10 in-frame deletion that preserves the reading frame (Note: This gene has no PM1 functional domains); Deletions and duplications >=1 exon in size (completely contained within the *SLC9A6* gene) where the reading frame is disrupted and NMD is predicted to occur; A full gene deletion. |
| **Strong** | PVS1_Strong is applicable for: Any truncating variant from **p.C564 to p.T601**; Canonical splice site variants that flank **exon 3** (in-frame exon). |
| **Moderate** | PVS1_Moderate is applicable for: Any truncating variant between **p.Y602 to p.A669**; Any frameshift variant that results in a read-through of the stop codon. |
| **Supporting** | PVS1_Supporting is applicable for **initiation codon variants** in *SLC9A6*. |

#### PVS1 Flowchart Decision Tree

**Nonsense or Frameshift:**
- Predicted to undergo NMD:
  - Exon is present in biologically-relevant transcript(s) → **PVS1**
  - Exon is absent from biologically-relevant transcript(s) → N/A
- Not predicted to undergo NMD (role of region in protein function is unknown):
  - Variant removes >10% of protein (occurs between p.C564-p.T601) → **PVS1_Strong**
  - Variant removes <10% of protein (occurs between p.Y602-p.A669); Frameshift that results in a read-through of the stop codon → **PVS1_Moderate**

**GT--AG 1,2 Splice Sites:**
- Exon skipping or use of a cryptic splice site disrupts reading frame and is predicted to undergo NMD:
  - Exon is present in biologically-relevant transcript(s) → **PVS1**
  - Exon is absent from biologically-relevant transcript(s) → N/A
- Exon skipping or use of a cryptic splice site disrupts reading frame and is NOT predicted to undergo NMD:
  - Role of region in protein function is unknown; LoF variants in this exon are not frequent in the general population and exon is present in biologically-relevant transcript(s); Variant removes >10% of protein → **PVS1_Strong**
- Exon skipping or use of a cryptic splice site preserves reading frame (Exons 3, 10):
  - Exon 3: Role of region in protein function is unknown; LoF variants in this exon are not frequent in the general population and exon is present in biologically-relevant transcript(s) → **PVS1_Strong**
  - Exon 10: Truncated/altered region is critical to protein function → **PVS1**

**Deletion (Single exon to full gene):**
- Full gene deletion → **PVS1**
- Single to multi exon deletion — Disrupts reading frame and is predicted to undergo NMD:
  - Exon is present in biologically-relevant transcript(s) → **PVS1**
  - Exon is absent from biologically-relevant transcript(s) → N/A
- Single to multi exon deletion — Disrupts reading frame and is NOT predicted to undergo NMD:
  - Role of region in protein function is unknown; LoF variants in this exon are not frequent in the general population and exon is present in biologically-relevant transcript(s):
    - Variant removes >10% of protein → **PVS1_Strong**
    - Variant removes <10% of protein → **PVS1_Moderate**
- Single to multi exon deletion — Preserves reading frame:
  - Single exon 3 or 10 deletion; Other in-frame combinations:
    - Truncated/altered region is critical to protein function — Exon 3 or exon 10 (Note: This gene has no PM1 functional domains) → **PVS1**

**Duplication (>=1 exon in size and must be completely contained within gene):**
- Proven in tandem:
  - Reading frame disrupted and NMD predicted to occur → **PVS1**
  - No or unknown impact on reading frame and NMD → N/A
- Presumed in tandem:
  - Reading frame presumed disrupted and NMD predicted to occur → **PVS1_Strong**
- Proven not in tandem → N/A

**Initiation Codon:**
- No known alternative start codon in other medically relevant transcripts → No pathogenic variant(s) upstream of closest potential in-frame start codon → **PVS1_Supporting**

---

### PS1 - Same Amino Acid Change

**Original ACMG Summary:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change. Example: Val->Leu caused by either G>C or G>T in the same codon. Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:** No disease-specific modifications.

| Strength | Criteria |
|----------|----------|
| **Strong** | Same amino acid change as a previously established pathogenic variant regardless of nucleotide change. |

---

### PS2 - De Novo (Confirmed)

**Original ACMG Summary:** De novo (both maternity and paternity confirmed) in a patient with the disease and no family history. Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.

**VCEP Specifications:**

- Applicable to all genes in affected individuals identified as mosaic for the variant (as the presence of a variant in the mosaic state is confirmatory of the variant being de novo).
- Because of the very high de novo rate of pathogenic variants in *SLC9A6*, de novo observation can be attributed the highest value points per proband (**2 points for confirmed de novo** and **1 point for assumed de novo**) if the patient is known to be affected with a neurodevelopmental phenotype consistent with the gene.

| Strength | Criteria |
|----------|----------|
| **Very Strong** | >=2 independent occurrences of PS2; OR >=2 independent occurrences of PM6 and one occurrence of PS2. Evidence from literature must be fully evaluated to support independent events. |
| **Strong** | 1 occurrence of PS2. |

---

### PS3 - Functional Studies

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product. Note: Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | RNA studies that demonstrate abnormal splicing and an **out-of-frame transcript**. Do not use for canonical splice site variants and when PVS1 is used. |
| **Supporting** | RNA studies that demonstrate abnormal splicing and an **in-frame product** (unless it affects an in-frame exon specified in the PVS1 section). |

---

### PS4 - Prevalence in Affected

**Original ACMG Summary:** The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls. Note 1: Relative risk (RR) or odds ratio (OR), as obtained from case-control studies, is >5.0 and the confidence interval around the estimate of RR or OR does not include 1.0. Note 2: In instances of very rare variants where case-control studies may not reach statistical significance, the prior observation of the variant in multiple unrelated patients with the same phenotype, and its absence in controls, may be used as moderate level of evidence.

**VCEP Specifications:**

- Detailed phenotype not needed. Need to confirm patient is 'affected with a neurodevelopmental phenotype consistent with the gene' at a minimum.
- Patient can be published OR an internal case OR observed at an outside lab (i.e. via ClinVar) OR described in the reputable databases. However independent case has to be confirmed to be a different patient than yours (compare gender/age).
- Do not use this criterion for variants where BS1 is applied or where PM2 does not apply.

| Strength | Criteria |
|----------|----------|
| **Strong** | 5+ observations. |
| **Moderate** | 3-4 observations. |
| **Supporting** | Use for 2nd independent occurrence. |

---

### PM1 - Mutational Hot Spot

**Original ACMG Summary:** Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.

**VCEP Specifications:** ***Not Applicable*** for SLC9A6.

---

### PM2 - Absent from Controls

**Original ACMG Summary:** Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium. Caveat: Population data for indels may be poorly called by next generation sequencing.

**VCEP Specification (Supporting only):**
- Use if **absent, zero observations** in control databases.

---

### PM3 - In Trans with Pathogenic

**Original ACMG Summary:** For recessive disorders, detected in trans with a pathogenic variant. Note: This requires testing of parents (or offspring) to determine phase.

**VCEP Specifications:** ***Not Applicable*** for SLC9A6. (X-linked inheritance — not a recessive disorder requiring compound heterozygosity.)

---

### PM4 - Protein Length Changes

**Original ACMG Summary:** Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Moderate** | Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants. |
| **Supporting** | Smaller in-frame events (< 3 amino acid residues). |

---

### PM5 - Novel Missense at Same Residue

**Original ACMG Summary:** Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before. Example: Arg156His is pathogenic; now you observe Arg156Cys. Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | >=2 different missense changes affecting the amino acid residue. Do not apply PM1 in these situations. |
| **Moderate** | A Grantham or BLOSUM score comparison can be used to determine if the variant is predicted to be as or more damaging than the established pathogenic variant. |

---

### PM6 - De Novo (Assumed)

**Original ACMG Summary:** Assumed de novo, but without confirmation of paternity and maternity.

**VCEP Specifications:**

Because of the very high de novo rate of pathogenic variants in *SLC9A6*, de novo observation can be attributed the highest value points per proband (**2 points for confirmed de novo** and **1 point for assumed de novo**) if the patient is known to be affected with a neurodevelopmental phenotype consistent with the gene.

| Strength | Criteria |
|----------|----------|
| **Very Strong** | >=4 independent occurrences of PM6. Evidence from literature must be fully evaluated to support independent events. |
| **Strong** | >=2 independent occurrences of PM6. Evidence from literature must be fully evaluated to support independent events. |
| **Moderate** | 1 occurrence of PM6. |

---

### PP1 - Co-segregation

**Original ACMG Summary:** Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease. Note: May be used as stronger evidence with increasing segregation data.

**VCEP Specifications:** Individuals must have disease consistent with reported phenotype (even if on the mild end of spectrum of the disease).

| Strength | Criteria |
|----------|----------|
| **Strong** | >=5 informative meiosis |
| **Moderate** | 3-4 informative meiosis |
| **Supporting** | 2 informative meiosis |

---

### PP2 - Missense in Constrained Gene

**Original ACMG Summary:** Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.

**VCEP Specifications:** ***Not Applicable*** for SLC9A6.

---

### PP3 - Computational Evidence

**Original ACMG Summary:** Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.). Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.

**VCEP Specifications (Supporting only):**

- For missense variants use **REVEL** with a score **>= 0.664**.
- For splice site variants use **SpliceAI** with a score **>= 0.2**.

---

### PP4 - Phenotype Specificity

**Original ACMG Summary:** Patient's phenotype or family history is highly specific for a disease with a single genetic etiology.

**VCEP Specifications (Supporting only):** See gene-specific clinical phenotype guidelines below.

#### SLC9A6 Clinical Phenotype Guidelines

**Core phenotype (need to be met for PP4):**

- Global developmental delay
- Intellectual disability
- Epilepsy
- Autistic spectrum disorder
- Ataxia
- Craniofacial dysmorphism

**Supportive criteria (do not need to be met for PP4, however in the absence of one core phenotype, two or more supportive phenotypes can be used in its place):**

- Happy, excitable, frequent smiling, laughter
- Angelman-like features
- Microcephaly

---

### PP5 - Reputable Source

**Original ACMG Summary:** Reputable source recently reports variant as pathogenic, but the evidence is not available to the laboratory to perform an independent evaluation.

**VCEP Specifications:** ***Not Applicable.*** This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PMID: 29543229).

---

## Benign Criteria

### BA1 - Allele Frequency >5%

**Original ACMG Summary:** Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

**VCEP Specifications:** The frequency cutoffs are based on MECP2 expected disease allele frequency (1 in 10,000 for the disease prevalence / (1.5 alleles [assumes 50/50 male/female ratio] * 0.8 for 80% penetrance)). MECP2 is the most prevalent of the genes covered in the Rett/Angelman-like working group and was chosen as the most conservative number.

**VCEP Specification (Stand Alone):**
- Use large population databases (i.e. gnomAD).
- Use if variant is present at **>=0.000083 (0.0083%)** in any sub-population.
- Use if allele frequency is met in any general continental population dataset of at least 2,000 observed alleles.

---

### BS1 - Frequency Greater Than Expected

**Original ACMG Summary:** Allele frequency is greater than expected for disorder.

**VCEP Specifications:** The frequency cutoffs are based on MECP2 expected disease allele frequency divided by 10 fold. MECP2 is the most prevalent of the genes covered in the Rett/Angelman-like working group and was chosen as the most conservative number.

**VCEP Specification (Strong):**
- Use large population databases (i.e. gnomAD).
- Use if variant is present at **>=0.0000083 (0.00083%)** and **<0.000083 (0.0083%)** in any sub-population.
- Use if allele frequency is met in any general continental population dataset of at least 2,000 observed alleles.

---

### BS2 - Observed in Healthy Adult

**Original ACMG Summary:** Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

**VCEP Specifications:**
- Should be applied in cases where the healthy adult is devoid of neurodevelopmental phenotypes.
- Best to use with internal curated data that includes clinical information or published patients that have been phenotyped.

| Strength | Criteria |
|----------|----------|
| **Strong** | 2 unaffected (related or unrelated) hemizygotes. |
| **Supporting** | 1 unaffected (related or unrelated) hemizygote. |

---

### BS3 - Functional Studies (No Effect)

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | RNA functional studies that demonstrate no impact on splicing and transcript composition. It can be downgraded based on quality of data. Not applicable for other functional studies. |

---

### BS4 - Lack of Segregation

**Original ACMG Summary:** Lack of segregation in affected members of a family. Caveat: The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.

**VCEP Specifications:** Need to confirm that the family member is 'affected with a neurodevelopmental phenotype consistent with the gene' at a minimum.

| Strength | Criteria |
|----------|----------|
| **Strong** | Absent in a similarly affected family member, when seen in two or more families. |
| **Supporting** | Absent in a similarly affected family member. |

---

### BP1-BP7 - Benign Supporting

| Criterion | Status | Specification |
|-----------|--------|---------------|
| **BP1** | *Not Applicable* | Not applicable for SLC9A6. |
| **BP2** | Supporting | Observed in *cis* with a pathogenic variant in any inheritance pattern. BP2 is **not applicable** for SLC9A6 for *in trans* state. Note: Knock out of *SLC9A6* results in disease but viable phenotype. |
| **BP3** | Supporting | In-frame deletions/insertions in a repetitive region without a known function. BP3 is applicable if there are in-frame deletions/duplications in a repetitive region where other in-frame deletions/duplications have been observed with an overall frequency commensurate with the BA1 threshold for this gene. |
| **BP4** | Supporting | For missense variants use **REVEL** with a score **<= 0.290**. For splice site variants use **SpliceAI** with a score **<= 0.1**. |
| **BP5** | Supporting / Moderate / Strong | Variant found in a case with an alternate molecular basis for disease. The variant should be in the hemizygous state. Do not apply if variant is de novo. **Supporting:** 1 case. **Moderate:** 2 cases. **Strong:** >=3 cases with alternate molecular basis for disease. |
| **BP6** | *Not Applicable* | Not for use as recommended by the ClinGen SVI VCEP Review Committee (PMID: 29543229). |
| **BP7** | Supporting | A synonymous (silent) variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved. Defined 'not highly conserved' as PhastCons score <1 and/or PhyloP score <0.1 and/or the variant is the reference nucleotide in one primate and/or three mammal species. For splice site variants use SpliceAI with a score <= 0.1. Note: For silent variants BP4 and BP7 can be added. |

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

### Appendix A: PVS1 Flowchart Summary

The PVS1 flowchart for *SLC9A6* (NM_006359.2) provides decision paths for the following variant types:

1. **Nonsense or Frameshift** — Assess NMD prediction, exon presence in biologically-relevant transcripts, and protein removal percentage to assign PVS1 through PVS1_Moderate.
2. **GT--AG 1,2 Splice Sites** — Evaluate reading frame disruption, NMD prediction, and exon identity (exons 3 and 10 are key in-frame exons) to assign PVS1 through PVS1_Strong.
3. **Deletion (Single exon to full gene)** — Full gene deletion receives PVS1; other deletions assessed by reading frame disruption, NMD prediction, and protein removal percentage.
4. **Duplication (>=1 exon, completely within gene)** — Proven in tandem with reading frame disruption and NMD → PVS1; Presumed in tandem → PVS1_Strong.
5. **Initiation Codon** — No known alternative start codon → PVS1_Supporting.

**Key position thresholds:**
- Null variants up to **p.A563** → PVS1 (Very Strong)
- Truncating variants **p.C564 to p.T601** → PVS1_Strong (removes >10% of protein)
- Truncating variants **p.Y602 to p.A669** → PVS1_Moderate (removes <10% of protein)

**Key exon notes:**
- **Exon 3** — In-frame exon; splice site variants flanking exon 3 → PVS1_Strong
- **Exon 10** — Truncated/altered region is critical to protein function; splice site variants preserving reading frame → PVS1
- This gene has **no PM1 functional domains**

### Appendix B: PP4 Clinical Phenotype Guidelines for SLC9A6

**Core phenotype (all need to be met for PP4):**

| # | Phenotype |
|---|-----------|
| 1 | Global developmental delay |
| 2 | Intellectual disability |
| 3 | Epilepsy |
| 4 | Autistic spectrum disorder |
| 5 | Ataxia |
| 6 | Craniofacial dysmorphism |

**Supportive criteria (do not need to be met for PP4; however in the absence of one core phenotype, two or more supportive phenotypes can be used in its place):**

| # | Phenotype |
|---|-----------|
| 1 | Happy, excitable, frequent smiling, laughter |
| 2 | Angelman-like features |
| 3 | Microcephaly |

### Appendix C: Population Frequency Thresholds Summary

| Criterion | Threshold | Strength |
|-----------|-----------|----------|
| BA1 | >=0.000083 (0.0083%) in any sub-population | Stand Alone |
| BS1 | >=0.0000083 (0.00083%) and <0.000083 (0.0083%) in any sub-population | Strong |
| PM2 | Absent (zero observations) in control databases | Supporting |

**Note:** Allele frequency must be met in any general continental population dataset of at least 2,000 observed alleles.

**Frequency cutoff rationale:** Based on MECP2 expected disease allele frequency (1 in 10,000 for the disease prevalence / (1.5 alleles [assumes 50/50 male/female ratio] * 0.8 for 80% penetrance)). MECP2 is the most prevalent of the genes covered in the Rett/Angelman-like working group and was chosen as the most conservative number. BS1 is BA1 divided by 10 fold.

### Appendix D: Computational Prediction Thresholds

| Tool | Pathogenic (PP3) | Benign (BP4) | Variant Type |
|------|-----------------|--------------|--------------|
| REVEL | >= 0.664 | <= 0.290 | Missense |
| SpliceAI | >= 0.2 | <= 0.1 | Splice site |

**Note:** For synonymous variants, BP4 and BP7 can both be applied.

### Appendix E: Criteria Applicability Summary

| Criterion | Applicable? | Max Strength | Notes |
|-----------|-------------|--------------|-------|
| PVS1 | Yes | Very Strong | Disease-specific modifications |
| PS1 | Yes | Strong | No modification |
| PS2 | Yes | Very Strong | High de novo rate; 2 pts confirmed |
| PS3 | Yes | Strong | RNA studies only |
| PS4 | Yes | Strong | Proband counting |
| PM1 | **No** | — | Not applicable for SLC9A6 |
| PM2 | Yes | Supporting only | Zero observations required |
| PM3 | **No** | — | Not applicable (X-linked) |
| PM4 | Yes | Moderate | Supporting for <3 AA events |
| PM5 | Yes | Strong | >=2 different missense changes |
| PM6 | Yes | Very Strong | High de novo rate; 1 pt assumed |
| PP1 | Yes | Strong | Informative meiosis counting |
| PP2 | **No** | — | Not applicable for SLC9A6 |
| PP3 | Yes | Supporting only | REVEL/SpliceAI |
| PP4 | Yes | Supporting only | Gene-specific phenotype guidelines |
| PP5 | **No** | — | Not for use (ClinGen SVI) |
| BA1 | Yes | Stand Alone | >=0.0083% in any sub-population |
| BS1 | Yes | Strong | >=0.00083% to <0.0083% |
| BS2 | Yes | Strong | Hemizygote observation |
| BS3 | Yes | Strong | RNA studies only |
| BS4 | Yes | Strong | Segregation in affected family |
| BP1 | **No** | — | Not applicable for SLC9A6 |
| BP2 | Yes | Supporting | *In cis* only; not *in trans* |
| BP3 | Yes | Supporting | Repetitive region, BA1-level freq |
| BP4 | Yes | Supporting only | REVEL/SpliceAI |
| BP5 | Yes | Strong | Alternate molecular basis |
| BP6 | **No** | — | Not for use (ClinGen SVI) |
| BP7 | Yes | Supporting | Synonymous + not conserved |

### Appendix F: Reference PMIDs

| # | Reference | PMID |
|---|-----------|------|
| 1 | Stromme P, Dobrenis K et al. *X-linked Angelman-like syndrome caused by Slc9a6 knockout in mice exhibits evidence of endosomal-lysosomal dysfunction.* Brain (2011) 134 (Pt 11) p. 3369-83. | 21964919 |
| 2 | Tarpey PS, Smith R et al. *A systematic, large-scale resequencing screen of X-chromosome coding exons in mental retardation.* Nat Genet (2009) 41 (5) p. 535-43. | 19377476 |
| 3 | Masurel-Paulet A, Piton A et al. *A new family with an SLC9A6 mutation expanding the phenotypic spectrum of Christianson syndrome.* Am J Med Genet A (2016) 170 (8) p. 2103-10. | 27256868 |
| 4 | Gilfillan GD, Selmer KK et al. *SLC9A6 mutations cause X-linked mental retardation, microcephaly, epilepsy, and ataxia, a phenotype mimicking Angelman syndrome.* Am J Hum Genet (2008) 82 (4) p. 1003-10. | 18342287 |
| 5 | Pejaver V, Byrne AB et al. *Calibration of computational tools for missense variant pathogenicity classification and ClinGen recommendations for PP3/BP4 criteria.* Am J Hum Genet (2022) 109 (12) p. 2163-2177. | 36413997 |
| 6 | Richards S et al. *Standards and guidelines for the interpretation of sequence variants: a joint consensus recommendation of ACMG and AMP.* Genet Med (2015). | 25741868 |
| 7 | Brnich SE et al. *Recommendations for application of the functional evidence PS3/BS3 criterion using the ACMG/AMP sequence variant interpretation framework.* Genome Med (2019). | 31892348 |
| 8 | Abou Tayoun AN et al. *Recommendations for interpreting the loss of function PVS1 ACMG/AMP variant criterion.* Hum Mutat (2018). | 30192042 |
| 9 | Biesecker LG, Harrison SM. *The ACMG/AMP reputable source criterion for the interpretation of sequence variants.* Genet Med (2018). | 29543229 |

---

## Version History

| Version | Date | Notes |
|---------|------|-------|
| 5.0.0 | 7/30/2025 | Modification to the population frequency cutoffs for BA1 and BS1. |

---

*This document was compiled from ClinGen VCEP specifications and ClinGen SVI recommendations. For the most current version, please refer to the ClinGen website.*
