# ClinGen Rett and Angelman-like Disorders Expert Panel Variant Interpretation Guidelines for UBE3A

**Version:** 6.0.0
**Released:** 7/30/2025
**Affiliation:** Rett and Angelman-like Disorders VCEP
**Based on:** Richards et al., 2015 ACMG/AMP Guidelines

**Release Notes:** Modification to the population frequency cutoffs for BA1 and BS1.

---

## Gene Information

| Attribute | Value |
|-----------|-------|
| **Gene** | UBE3A (HGNC:12496) |
| **HGNC Name** | ubiquitin protein ligase E3A |
| **Transcript** | NM_130838.2 |
| **Disease** | Angelman syndrome (MONDO:0007113) |
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

Caveats:
- Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7).
- Use caution interpreting LOF variants at the extreme 3' end of a gene.
- Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact.
- Use caution in the presence of multiple transcripts.

**VCEP Specifications:**

Refer to PVS1 flow chart for additional guidance.

For intragenic deletions/duplications that are predicted to result in a product that preserves reading frame:
- For single exon in-frame deletions assign the same strength (PVS1, PVS1_Strong, or PVS1_Moderate) as for splice site variants that preserve reading frame indicated above.
- For multiple exon in-frame deletions PVS1 can be assigned to deletions that include single in-frame exons in the PVS1 category (listed above) OR if the exon contains a functionally important domain as specified in PM1.
- Given the extensive data available for *UBE3A*, classifications for single or multi-exon in-frame deletions are assigned as PVS1 or PVS1_Strong. Refer to PVS1 flow chart for additional guidance.

#### Strength Levels

| Strength | Criteria |
|----------|----------|
| **Very Strong** | PVS1 is applicable for: Any truncating variant up to p.K841; Any frameshift variant that results in a read-through of the stop codon; Initiation codon variants; Canonical splice site variants predicted to result in an out-of-frame product; Intragenic deletions/duplications predicted to result in an out-of-frame product; Full gene deletion. Use as defined by ClinGen SVI working group (PMID:30192042). |
| **Strong** | PVS1_Strong is applicable for: Any truncating variant from p.A842 to p.G850; Canonical splice site variants that flank exons 7, 8 (in-frame exons). |
| **Moderate** | PVS1_Moderate is applicable for any truncating variant distal of p.G850. |

---

### PS1 - Same Amino Acid Change

**Original ACMG Summary:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change. Example: Val->Leu caused by either G>C or G>T in the same codon.

Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

| Strength | Criteria |
|----------|----------|
| **Strong** | Same amino acid change as a previously established pathogenic variant regardless of nucleotide change. No modification from original ACMG criteria. |

---

### PS2 - De Novo (Confirmed)

**Original ACMG Summary:** De novo (both maternity and paternity confirmed) in a patient with the disease and no family history. Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.

**VCEP Specifications:**
- Applicable to all genes in affected individuals identified as mosaic for the variant (as the presence of a variant in the mosaic state is confirmatory of the variant being de novo).
- Because of the very high de novo rate of pathogenic variants in UBE3A, de novo observation can be attributed the highest value points per proband (2 points for confirmed de novo and 1 point for assumed de novo) if the patient is known to be affected with a neurodevelopmental phenotype consistent with the gene.

#### PS2/PM6 Strength Levels

| Strength | Criteria |
|----------|----------|
| **Very Strong** | ≥2 independent occurrences of PS2; OR ≥2 independent occurrences of PM6 and one occurrence of PS2. Evidence from literature must be fully evaluated to support independent events. |
| **Strong** | 1 occurrence of PS2. |

#### PS2/PM6 Point System

| Phenotypic Consistency | Confirmed De Novo (PS2) | Assumed De Novo (PM6) |
|------------------------|------------------------|-----------------------|
| Neurodevelopmental phenotype consistent with gene | 2 points | 1 point |

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
| **Strong** | RNA studies that demonstrate abnormal splicing and an out-of-frame transcript. Do not use for canonical splice site variants and when PVS1 is used. |
| **Supporting** | RNA studies that demonstrate abnormal splicing and an in-frame product (unless it affects an in-frame exon specified in the PVS1 section). See included table for acceptable functional studies. |

#### Approved Assay Instances

| Assay Name | Measured Parameter | Expected Deleterious Result (PS3_Supporting) | Expected Benign Result (BS3) | References |
|------------|-------------------|----------------------------------------------|------------------------------|------------|
| E3 ubiquitin ligase activity | E3 ubiquitin ligase activity | Loss of substrate ubiquitination | Not recommended | PMID: 15263005; 26255772 |
| UBE3A protein expression | Protein levels monitored to reflect either protein stability or levels of self degradation | Comparison to WT possible however no robust thresholds available | Not recommended | PMID: 26255772 |
| UBE3A nuclear localization | UBE3A subcellular localization | Cytoplasmic localization | Not recommended | PMID: 31235931, 33607653 |

---

### PS4 - Prevalence in Affected

**Original ACMG Summary:** The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.

**VCEP Specifications:**
- Detailed phenotype not needed. Need to confirm patient is 'affected with a neurodevelopmental phenotype consistent with the gene' at a minimum.
- Patient can be published OR an internal case OR observed at an outside lab (i.e. via ClinVar) OR described in the reputable databases (LOVD). However, the independent case has to be confirmed to be a different patient than yours (compare gender/age).
- Do not use this criterion for variants where BS1 is applied or where PM2 does not apply.

| Strength | Criteria |
|----------|----------|
| **Strong** | 5+ observations. |
| **Moderate** | 3-4 observations. |
| **Supporting** | Use for 2nd independent occurrence. |

---

### PM1 - Mutational Hot Spot

**Original ACMG Summary:** Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Moderate** | 3' cysteine binding site: aa 820 (p.C820). |

---

### PM2 - Absent from Controls

**Original ACMG Summary:** Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium. Caveat: Population data for indels may be poorly called by next generation sequencing.

**VCEP Specification (Supporting only):**
- Use if absent, zero observations in control databases.

---

### PM3 - In Trans with Pathogenic

**Original ACMG Summary:** For recessive disorders, detected in trans with a pathogenic variant. Note: This requires testing of parents (or offspring) to determine phase.

**VCEP Specifications:** ***Not Applicable*** - Not applicable for UBE3A (autosomal dominant disorder).

---

### PM4 - Protein Length Changes

**Original ACMG Summary:** Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | PM4_Strong is applicable to stop-loss variants in UBE3A, as several stop loss variants in this gene have been described in affected individuals. |
| **Moderate** | Protein length changes due to in-frame deletions/insertions in a non-repeat region. |
| **Supporting** | Smaller in-frame events (< 3 amino acid residues) unless they occur in a functionally important region (see PM1 for functionally important domain for this gene). |

---

### PM5 - Novel Missense at Same Residue

**Original ACMG Summary:** Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before. Example: Arg156His is pathogenic; now you observe Arg156Cys.

Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | ≥2 different missense changes affecting the amino acid residue. Do not apply PM1 in these situations. |
| **Moderate** | A Grantham or BLOSUM score comparison can be used to determine if the variant is predicted to be as or more damaging than the established pathogenic variant. |

---

### PM6 - De Novo (Assumed)

**Original ACMG Summary:** Assumed de novo, but without confirmation of paternity and maternity.

**VCEP Specifications:**
- Because of the very high de novo rate of pathogenic variants in *UBE3A*, de novo observation can be attributed the highest value points per proband (2 points for confirmed de novo and 1 point for assumed de novo) if the patient is known to be affected with a neurodevelopmental phenotype consistent with the gene.
- See PS2 section for the combined PS2/PM6 point system.

| Strength | Criteria |
|----------|----------|
| **Very Strong** | ≥4 independent occurrences of PM6. Evidence from literature must be fully evaluated to support independent events. |
| **Strong** | ≥2 independent occurrences of PM6. Evidence from literature must be fully evaluated to support independent events. |
| **Moderate** | 1 occurrence of PM6. |

---

### PP1 - Co-segregation

**Original ACMG Summary:** Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease. Note: May be used as stronger evidence with increasing segregation data.

**VCEP Specifications:**
- Note: individuals must have disease consistent with reported phenotype (even if on the mild end of spectrum of the disease).

| Strength | Informative Meioses |
|----------|---------------------|
| **Strong** | ≥5 informative meioses |
| **Moderate** | 3-4 informative meioses |
| **Supporting** | 2 informative meioses |

---

### PP2 - Missense in Constrained Gene

**Original ACMG Summary:** Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.

**VCEP Specifications:** ***Not Applicable*** - Not applicable for UBE3A.

---

### PP3 - Computational Evidence

**Original ACMG Summary:** Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.). Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Supporting** | For missense variants use REVEL with a score ≥ 0.644. For splice site variants use SpliceAI with a score ≥ 0.2. |

---

### PP4 - Phenotype Specificity

**Original ACMG Summary:** Patient's phenotype or family history is highly specific for a disease with a single genetic etiology.

**VCEP Specifications:**
- See gene specific clinical phenotype guidelines.

| Strength | Criteria |
|----------|----------|
| **Supporting** | Phenotype specific for disease with single genetic etiology. See clinical phenotype guidelines below. |

#### UBE3A Clinical Phenotype Guidelines (for PP4)

**Mandatory criterion:**
- Severe ID (if 5 years of age or older) or global developmental delay (if <5 years of age)

**In addition, the patient has to satisfy at least 4/5 of the following:**
1. Ataxia/jerky movements
2. Characteristic EEG
3. Seizures
4. Absent speech or less than 5 words (if at least 4 years of age)
5. Frequent smiling

**Additional notes:** If information is provided such that a phenotype of Angelman syndrome is suspected, with specific minimal features used for the diagnosis, then this can be used for PP4 in lieu of the specific clinical features listed.

---

### PP5 - Reputable Source

**Original ACMG Summary:** Reputable source recently reports variant as pathogenic, but the evidence is not available to the laboratory to perform an independent evaluation.

**VCEP Specifications:** ***Not Applicable*** - This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PMID: 29543229).

---

## Benign Criteria

### BA1 - Allele Frequency >5%

**Original ACMG Summary:** Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

**VCEP Specifications:**
- The frequency cutoffs are based on MECP2 expected disease allele frequency (1 in 10,000 for the disease prevalence / (1.5 alleles [assumes 50/50 male/female ratio] * 0.8 for 80% penetrance)). MECP2 is the most prevalent of the genes covered in the Rett/Angelman-like working group and was chosen as most conservative number.

**VCEP Specification (Stand Alone):**
- Use large population databases (i.e. gnomAD).
- Use if variant is present at **≥0.000083 (0.0083%)** in any sub-population.
- Use if allele frequency is met in any general continental population dataset of at least 2,000 observed alleles.

---

### BS1 - Frequency Greater Than Expected

**Original ACMG Summary:** Allele frequency is greater than expected for disorder.

**VCEP Specifications:**
- The frequency cutoffs are based on MECP2 expected disease allele frequency divided by 10-fold. MECP2 is the most prevalent of the genes covered in the Rett/Angelman-like working group and was chosen as most conservative number.

**VCEP Specification (Strong):**
- Use large population databases (i.e. gnomAD).
- Use if variant is present at **≥0.0000083 (0.00083%) and <0.000083 (0.0083%)** in any sub-population.
- Use if allele frequency is met in any general continental population dataset of at least 2,000 observed alleles.

---

### BS2 - Observed in Healthy Adult

**Original ACMG Summary:** Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

**VCEP Specifications:**
- Should be applied in cases where the healthy adult is devoid of neurodevelopmental phenotypes.
- Best to use with internal curated data that includes clinical information or published patients that have been phenotyped.

| Strength | Criteria |
|----------|----------|
| **Strong** | 4 unaffected (related and maternally inherited or unrelated) heterozygotes. |
| **Moderate** | 3 unaffected (related and maternally inherited or unrelated) heterozygotes. |
| **Supporting** | 2 unaffected (related and maternally inherited or unrelated) heterozygotes. |

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

**VCEP Specifications:**
- Need to confirm that the family member is 'affected with a neurodevelopmental phenotype consistent with the gene' at a minimum.

| Strength | Criteria |
|----------|----------|
| **Strong** | Absent in a similarly affected family member, when seen in two or more families. |
| **Supporting** | Absent in a similarly affected family member. |

---

### BP1-BP7 - Benign Supporting

| Criterion | Status | Comment |
|-----------|--------|---------|
| **BP1** | Not Applicable | Not applicable for UBE3A. |
| **BP2** | Applicable (Supporting, *in cis* only) | Knock out of *UBE3A* results in disease but viable phenotype. BP2 is not applicable for UBE3A in *trans* state. Only applicable when observed *in cis* with a pathogenic variant. |
| **BP3** | Applicable (Supporting) | In-frame deletions/insertions in a repetitive region without a known function. BP3 is applicable if there are in-frame deletions/duplications in a repetitive region where other in-frame deletions/duplications have been observed with an overall frequency commensurate with the BA1 threshold for this gene. |
| **BP4** | Applicable (Supporting) | For missense variants use REVEL with a score ≤ 0.290. For splice site variants use SpliceAI with a score ≤ 0.1. |
| **BP5** | Applicable (Supporting to Strong) | Variant found in a case with an alternate molecular basis for disease. Variant should also be maternally inherited in the case with an alternate molecular basis for disease for this criteria to be used. Do not apply if variant is de novo. **Strong:** ≥3 cases. **Moderate:** 2 cases. **Supporting:** 1 case. Example: variant in UBE3A identified in a patient with lissencephaly in whom a pathogenic variant is identified in the PAFAH1B1 gene. |
| **BP6** | Not Applicable | This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PMID: 29543229). |
| **BP7** | Applicable (Supporting) | A synonymous (silent) variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved. Defined 'not highly conserved' regions as those with PhastCons score <1 and/or PhyloP score <0.1 and/or the variant is the reference nucleotide in one primate and/or three mammal species. For splice site variants use SpliceAI with a score ≤ 0.1. For silent variants BP4 and BP7 can be added together. |

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

### Appendix A: PVS1 Flowchart

**Transcript:** NM_130838.2

#### Nonsense or Frameshift

| Condition | Outcome | Strength |
|-----------|---------|----------|
| Predicted to undergo NMD → Exon present in biologically-relevant transcript(s) | Applicable | PVS1 |
| Predicted to undergo NMD → Exon absent from biologically-relevant transcript(s) | Not applicable | N/A |
| Not predicted to undergo NMD → Upstream of the most distal de novo LOF variant (p.K841); Frameshift that results in a read-through of the stop codon | Applicable | PVS1 |
| Not predicted to undergo NMD → Downstream of the most distal de novo LOF variant (p.K841) but does not result in a read-through of the stop codon | Applicable | PVS1_Strong |
| Not predicted to undergo NMD → Downstream of the most distal de novo non-truncating variant (p.G850) but does not result in a read-through of the stop codon | Applicable | PVS1_Moderate |

#### GT--AG 1,2 Splice Sites

| Condition | Outcome | Strength |
|-----------|---------|----------|
| Exon skipping/cryptic splice site disrupts reading frame and is predicted to undergo NMD → Exon present in biologically-relevant transcript(s) | Applicable | PVS1 |
| Exon skipping/cryptic splice site disrupts reading frame and is predicted to undergo NMD → Exon absent from biologically-relevant transcript(s) | Not applicable | N/A |
| Exon skipping/cryptic splice site disrupts reading frame and is NOT predicted to undergo NMD → Truncated/altered region is critical to protein function (Exon 11) | Applicable | PVS1 |
| Exon skipping/cryptic splice site preserves reading frame → Exons 7, 8 (LoF variants not frequent in general population and exon present in biologically-relevant transcripts) | Applicable | PVS1_Strong |

#### Deletion (Single Exon to Full Gene)

| Condition | Outcome | Strength |
|-----------|---------|----------|
| Full gene deletion | Applicable | PVS1 |
| Disrupts reading frame and is predicted to undergo NMD → Exon present in biologically-relevant transcript(s) | Applicable | PVS1 |
| Disrupts reading frame and is predicted to undergo NMD → Exon absent from biologically-relevant transcript(s) | Not applicable | N/A |
| Disrupts reading frame and is NOT predicted to undergo NMD (Exon 11) → Truncated/altered region is critical to protein function | Applicable | PVS1 |
| Preserves reading frame (Single exon 7 or 8 deletion; Other in-frame combinations) → Role of region in protein function is unknown; LoF variants not frequent; Variant removes >10% of protein | Applicable | PVS1 |
| Preserves reading frame → Role of region in protein function is unknown; LoF variants not frequent; Variant removes <10% of protein (Exon 7) | Applicable | PVS1_Strong |
| Preserves reading frame → Truncated/altered region is critical to protein function (Exon 8 + any in-frame combination that includes the PM1 functional domain p.C820) | Applicable | PVS1 |

#### Duplication (≥1 Exon in Size, Must Be Completely Contained Within Gene)

| Condition | Outcome | Strength |
|-----------|---------|----------|
| Proven in tandem → Reading frame disrupted and NMD predicted to occur | Applicable | PVS1 |
| Proven in tandem → No or unknown impact on reading frame and NMD | Not applicable | N/A |
| Presumed in tandem → Reading frame presumed disrupted and NMD predicted to occur | Applicable | PVS1_Strong |
| Proven not in tandem | Not applicable | N/A |

#### Initiation Codon

| Condition | Outcome | Strength |
|-----------|---------|----------|
| No known alternative start codon in other medically relevant transcripts → Initiation codon variant described in at least one affected individual with Angelman syndrome | Applicable | PVS1 |

### Appendix B: Reference PMIDs

| # | Reference |
|---|-----------|
| 1 | Bienvenu T, Carrié A, et al. *MECP2 mutations account for most cases of typical forms of Rett syndrome.* **Hum Mol Genet** (2000) 9(9):1377-84. PMID: 10814719 |
| 2 | Erlandson A, Hallberg B, et al. *MECP2 mutation screening in Swedish classical Rett syndrome females.* **Eur Child Adolesc Psychiatry** (2001) 10(2):117-21. PMID: 11469283 |
| 3 | Fang P, Lev-Lehman E, et al. *The spectrum of mutations in UBE3A causing Angelman syndrome.* **Hum Mol Genet** (1999) 8(1):129-35. PMID: 9887341 |
| 4 | Sadikovic B, Fernandes P, et al. *Mutation Update for UBE3A variants in Angelman syndrome.* **Hum Mutat** (2014) 35(12):1407-17. PMID: 25212744 |
| 5 | Jiang YH, Armstrong D, et al. *Mutation of the Angelman ubiquitin ligase in mice causes increased cytoplasmic p53 and deficits of contextual learning and long-term potentiation.* **Neuron** (1998) 21(4):799-811. PMID: 9808466 |
| 6 | Pejaver V, Byrne AB, et al. *Calibration of computational tools for missense variant pathogenicity classification and ClinGen recommendations for PP3/BP4 criteria.* **Am J Hum Genet** (2022) 109(12):2163-2177. PMID: 36413997 |

### Appendix C: Population Frequency Thresholds Summary

| Criterion | Threshold | Strength |
|-----------|-----------|----------|
| BA1 | ≥0.000083 (0.0083%) in any sub-population | Stand Alone |
| BS1 | ≥0.0000083 (0.00083%) and <0.000083 (0.0083%) in any sub-population | Strong |
| PM2 | Absent (zero observations) in control databases | Supporting |

**Note:** Allele frequency must be met in any general continental population dataset of at least 2,000 observed alleles. Frequency cutoffs are based on MECP2 expected disease allele frequency (most conservative across Rett/Angelman-like working group genes).

### Appendix D: Functional Assays Summary

| Assay | Measured Parameter | PS3_Supporting Threshold | BS3 Applicability | References |
|-------|-------------------|--------------------------|-------------------|------------|
| E3 ubiquitin ligase activity | E3 ubiquitin ligase activity | Loss of substrate ubiquitination | Not recommended | PMID: 15263005; 26255772 |
| UBE3A protein expression | Protein levels (stability or self-degradation) | Comparison to WT possible; no robust thresholds available | Not recommended | PMID: 26255772 |
| UBE3A nuclear localization | UBE3A subcellular localization | Cytoplasmic localization | Not recommended | PMID: 31235931, 33607653 |

### Appendix E: Criteria Applicability Summary

| Criterion | Status | Max Strength | Modification Type |
|-----------|--------|-------------|-------------------|
| PVS1 | Applicable | Very Strong | Disease-specific |
| PS1 | Applicable | Strong | None |
| PS2 | Applicable | Very Strong | None |
| PS3 | Applicable | Strong | Disease-specific |
| PS4 | Applicable | Strong | Strength |
| PM1 | Applicable | Moderate | Disease-specific |
| PM2 | Applicable | Supporting | Strength |
| PM3 | **Not Applicable** | — | — |
| PM4 | Applicable | Strong | Disease-specific |
| PM5 | Applicable | Strong | Strength |
| PM6 | Applicable | Very Strong | Strength |
| PP1 | Applicable | Strong | Strength |
| PP2 | **Not Applicable** | — | — |
| PP3 | Applicable | Supporting | General recommendation |
| PP4 | Applicable | Supporting | Disease-specific |
| PP5 | **Not Applicable** | — | — |
| BA1 | Applicable | Stand Alone | Disease-specific |
| BS1 | Applicable | Strong | Disease-specific |
| BS2 | Applicable | Strong | Strength |
| BS3 | Applicable | Strong | Disease-specific |
| BS4 | Applicable | Strong | Strength |
| BP1 | **Not Applicable** | — | — |
| BP2 | Applicable (*in cis* only) | Supporting | Disease-specific |
| BP3 | Applicable | Supporting | None |
| BP4 | Applicable | Supporting | None |
| BP5 | Applicable | Strong | Strength/Disease-specific |
| BP6 | **Not Applicable** | — | — |
| BP7 | Applicable | Supporting | None |

---

## Version History

| Version | Date | Notes |
|---------|------|-------|
| 6.0.0 | 7/30/2025 | Modification to the population frequency cutoffs for BA1 and BS1. |

---

*This document was compiled from ClinGen Rett and Angelman-like Disorders VCEP specifications and ClinGen SVI recommendations. For the most current version, please refer to the ClinGen website.*
