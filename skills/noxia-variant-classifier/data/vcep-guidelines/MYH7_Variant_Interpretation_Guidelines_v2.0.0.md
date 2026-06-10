# ClinGen Cardiomyopathy Expert Panel Variant Interpretation Guidelines for MYH7

**Version:** 2.0.0
**Released:** April 22, 2024
**Affiliation:** Cardiomyopathy Variant Curation Expert Panel (CMP-VCEP)
**Based on:** Richards et al., 2015 ACMG/AMP Guidelines

---

## Gene Information

| Attribute | Value |
|-----------|-------|
| **Gene** | MYH7 (HGNC:7577) |
| **HGNC Name** | myosin heavy chain 7 |
| **Transcript** | ENST00000355349 / NM_000257.4 |
| **Disease** | Dilated cardiomyopathy (MONDO:0005021); Hypertrophic cardiomyopathy (MONDO:0005045) |
| **Inheritance** | Autosomal dominant |

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
   - [BA1 - Allele Frequency >0.1%](#ba1---allele-frequency-01)
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

**Caveats:**
- Beware of genes where LOF is not a known disease mechanism (e.g., GFAP, MYH7)
- Use caution interpreting LOF variants at the extreme 3' end of a gene
- Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact
- Use caution in the presence of multiple transcripts

#### VCEP Specification

| Strength | Criteria |
|----------|----------|
| **Not Applicable** | PVS1 is not applicable for MYH7. Loss of function is not a known disease mechanism for this gene. |

**Comments:** Not applicable for MYH7.

---

### PS1 - Same Amino Acid Change

**Original ACMG Summary:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.

**Example:** Val->Leu caused by either G>C or G>T in the same codon.

**Caveat:** Beware of changes that impact splicing rather than at the amino acid/protein level.

#### VCEP Specification

| Strength | Criteria |
|----------|----------|
| **Strong** | No cardiomyopathy-specific modifications. Apply as outlined by Richards et al. 2015. |

**Important Note:** Example of when rule should NOT be applied: NM_000256.3(MYBPC3):c.2308G>A (p.Asp770Asn) has an established impact on splicing leading to nonsense mediated decay (NMD) and should not be used to provide evidence for other variants observed to result in the same amino acid change.

**Modification Type:** No change

---

### PS2 - De Novo (Confirmed)

**Original ACMG Summary:** De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.

**Note:** Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.

#### VCEP Specification

| Strength | Criteria |
|----------|----------|
| **Strong** | Refer to SVI guidance on number/combination of cases required based on phenotype specificity. |

**Phenotype Consistency Recommendation:** For most cardiomyopathies, default to **"Phenotype consistent with gene but not highly specific"**. Clinical judgment is required for shifting to a higher or lower category.

**Requirements for STRONG or VERY STRONG:**
- Ideally parents have been thoroughly clinically evaluated without evidence of cardiomyopathy (using a combination of ECG and echocardiogram or cardiac MRI for maximum sensitivity)

**Family History Consistent with De Novo Inheritance:**
A family history should NOT have any clinical signs or symptoms suggestive of cardiomyopathy in a 1st or 2nd degree relative, including:
1. Sudden death under 60 years of age
2. Heart transplant
3. Implantable cardiac defibrillator (ICD) under 60 years of age
4. Features of cardiomyopathy (e.g., systolic dysfunction, hypertrophy, left ventricular enlargement in an individual without risk factors)
5. Other related/overlapping cardiomyopathies

**Non-suspicious Family History Examples:**
Non-specific clinical features (e.g., palpitations, syncope, borderline/inconclusive echocardiogram findings, heart attack if age appropriate and suspected to result from coronary artery disease), but every attempt should be made to clarify features.

**Important:** Generally, this criterion is only applicable in the ABSENCE of any other possible disease-causing variants. If other pathogenic or likely pathogenic variants are present, consider decreasing points assigned or overall weight.

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

**Modification Type:** Disease-specific

---

### PS3 - Functional Studies

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.

**Note:** Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.

#### VCEP Specifications

**General Guidance:**
- Evaluation of studies/assays is required prior to application of functional evidence at any strength
- Refer to SVI guidance for functional evidence (Brnich et al. 2020)
- In the context of cardiomyopathy, very few functional assays currently meet criteria sufficient for application of this rule at a STRONG level
- Examples of the types of study/assays that MAY be relevant are described, but further definition of cardiomyopathy models/assays is outside the scope of these guidelines

| Strength | Assay Type | Requirements |
|----------|-----------|--------------|
| **Strong** | In vitro splicing assays (e.g., RNA studies) | See detailed criteria below |
| **Moderate** | In vivo models (e.g., variant knock-in animal models) | See detailed criteria below |
| **Supporting** | In vitro assays (e.g., biochemical assays, motility assays, human iPSC-CM) | See detailed criteria below |

#### PS3_Strong: In Vitro Splicing Assays

In vitro splicing assays may be considered as **STRONG** evidence, providing ALL the following criteria are met:
- Prior knowledge of predominant transcripts in cardiac tissue
- Analysis undertaken using RNA extracted from cardiac tissue from the individual with the variant, OR
- Analysis undertaken using RNA extracted from whole blood providing the relevant transcripts (isoforms) are expressed in blood and are at sufficient levels to assess splice disruption
- Assay shows a clear, reproducible and convincing effect on splicing (i.e., a distinct splice product, present at a level comparable to the splice product from the wild-type allele), which is not observed in controls
- Confirmation of abnormal splice product by Sanger sequencing

**NOTE:** Mini-gene assay in non-patient derived cell lines are NOT considered to provide STRONG evidence.

**NOTE:** Whether to activate this rule needs to be reconciled with the variant spectrum and disease mechanism for the gene at hand (i.e., consider whether the effect is likely to lead to LOF or an in-frame alteration and whether this type of effect is expected to be disease causing) (Abou Tayoun et al. 2018).

#### PS3_Moderate: In Vivo Models

Mammalian variant-specific knock-in animal models that produce a phenotype consistent with the clinical phenotype in humans (e.g., structural and/or functional cardiac abnormalities, premature death, arrhythmia) may be considered as **MODERATE** evidence.

**NOTE:** The following assays/models do NOT meet criteria:
1. Assays that are known to be associated with non-specific cardiac phenotypes (e.g., morpholino-induced pericardial edema in zebrafish)
2. In vivo evidence that is not variant specific, such as whole gene alterations (i.e., cDNA or whole gene transgenic mice and whole or partial gene knock-out mice)

#### PS3_Supporting: In Vitro Assays

While some in vitro assays may provide evidence that a variant in a cardiomyopathy gene has an effect on protein and/or myofilament function, at present, there are no validated "gold-standard" assays that are considered to reliably predict the clinical phenotype.

As such, in the cardiomyopathy genes listed in these guidelines, data from individual in vitro studies are unlikely to meet the criteria required to assign this rule at more than **SUPPORTING** level.

**Modification Type:** Disease-specific

---

### PS4 - Prevalence in Affected

**Original ACMG Summary:** The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.

**Note 1:** Relative risk (RR) or odds ratio (OR), as obtained from case-control studies, is >5.0 and the confidence interval around the estimate of RR or OR does not include 1.0.

**Note 2:** In instances of very rare variants where case-control studies may not reach statistical significance, the prior observation of the variant in multiple unrelated patients with the same phenotype, and its absence in controls, may be used as moderate level of evidence.

#### VCEP Specifications

Currently few well-designed case-control studies have been performed for inherited cardiomyopathies. Until such studies become available, comparative analyses can be undertaken using case data (e.g., internal and/or published cohorts) and control data from population-level cohorts (e.g., gnomAD).

#### Cohort Requirements

Cohorts used in these analyses should meet the following criteria:

1. **Cases have clinical diagnosis** of the specified disorder or related phenotype (e.g., all cases have HCM or another relevant phenotype)
   - Consider how likely another potential cause of the phenotype has been excluded
   - Consider the presence of other variants in relevant genes and the extent of testing performed

2. **Controls not enriched** for the specified disorder

3. **Denominator available** (e.g., variant detected in 5 out of 3,500 cases and 1 out of 60,000 controls)

4. **No closely related individuals** (family members not included in case counts)

5. **No overlapping cohorts** (cases not counted more than once)

6. **Population diversity broadly similar** between case and control cohorts

7. **Consider cohort size** — larger cohorts provide more accurate estimates; prefer data from largest available case series (e.g., Walsh et al. 2017, DECIPHER)

#### PS4 Strength Thresholds

| Strength | Lower Bound of 95% CI around OR |
|----------|--------------------------------|
| **Strong** | ≥20 |
| **Moderate** | ≥10 |
| **Supporting** | ≥5 |

**Calculator:** A PS4 calculator is available at www.cardiodb.org

**Multiple Cohorts:** If multiple cohorts are available, the final ORs and associated CIs need to be harmonized across all cohorts to determine the final level (e.g., if 2 large cohorts have an OR of ~6 and a third small cohort has an OR of 11, application at a SUPPORTING level should be considered).

#### Relevant Phenotypes

1. **HCM and RCM** may be combined as they are considered part of the same disease spectrum
2. For the eight genes covered by these guidelines, the combination of probands with other phenotypes should be reviewed by a clinical expert to determine if grouping is appropriate
3. **LVNC Considerations:** Due to debate about whether isolated LVNC represents a true disease entity or variation of typical cardiac morphology, individuals with isolated LVNC should **NOT** be added to proband or segregation counts
4. **HCM vs DCM:** HCM and DCM have distinct mechanisms of disease and pathogenetic variants are not anticipated to cause both primary phenotypes. While occurrence in both phenotypes may initially be considered as evidence against pathogenicity, end-stage HCM can present similarly to DCM. Careful consideration is needed.

**Modification Type:** Disease-specific

---

### PM1 - Mutational Hot Spot

**Original ACMG Summary:** Located in a mutational hot spot and/or critical and well-established functional domain (e.g., active site of an enzyme) without benign variation.

#### VCEP Specification

| Strength | Criteria |
|----------|----------|
| **Moderate** | Applicable to missense variants in MYH7 in the specific regions listed below (Walsh et al. 2019) |

**Applicable Regions:**
- Transcripts: ENST00000355349 & NM_000257.4
- **Codons 167-931** (updated from v1.0)

**Important Notes:**
- Data from HCM case cohorts was used to derive these cluster regions
- This rule should **NOT** be applied when additional evidence supports that the variant causes a phenotype other than HCM (e.g., variant seen in multiple DCM cases)
- Enrichment was not observed for DCM in any genes
- Rule should **NOT** be combined with PM5 because presence of pathogenic variants in the same codon/region were used to determine clustering and would be double-counting evidence

**Modification Type:** Disease-specific, Gene-specific

---

### PM2 - Absent from Controls

**Original ACMG Summary:** Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

**Caveat:** Population data for indels may be poorly called by next generation sequencing.

#### VCEP Specification

| Strength | Criteria |
|----------|----------|
| **Supporting** | Threshold of ≤0.00004 in the subpopulation with the highest frequency when using the upper bound of the 95% CI |

**Threshold Details:**

The values used to calculate the PM2 thresholds were derived from studies in Northern European populations. These thresholds can be applied to any population where:
- Disease prevalence is considered comparable (1/500 or lower)
- The most frequent pathogenic variant accounts for no more than 2% of cases
- The penetrance of a pathogenic variant is expected to be at least 50%

**Equivalents:**
- Variant NOT being observed more than once (≤1 allele) in gnomAD v2.1.1 in one of the non-founder populations
- Absence required from the Other and Ashkenazi Jewish subpopulations

**Allele Count (AC) in Allele Number (AN) equivalents:**
| AC | AN |
|----|-----|
| ≤1 | ≥120,000 |
| ≤2 | ≥160,000 |
| ≤3 | ≥195,000 |
| ≤4 | ≥230,000 |

**gnomAD Considerations:**
- gnomAD is the preferred database but currently only displays the filtering allele frequency (FAF), which is equivalent to a lower bound estimate of the 95% CI, when the upper bound is what is needed
- Use confidence interval tools, such as Confit-de-MAF, to determine the upper bound of the 95% CI

**Cautions:**
- Minor allele frequencies for complex variants (e.g., large indels) may not be accurately represented in population databases
- Use caution when a variant is only identified, or over-represented, in one of the smaller gnomAD populations
- Population databases may contain affected or pre-symptomatic individuals for diseases with reduced penetrance/variable onset

**Modification Type:** Disease-specific

---

### PM3 - In Trans with Pathogenic

**Original ACMG Summary:** For recessive disorders, detected in trans with a pathogenic variant.

**Note:** This requires testing of parents (or offspring) to determine phase.

#### VCEP Specification

| Strength | Criteria |
|----------|----------|
| **Not Applicable** | MYH7-associated cardiomyopathies are autosomal dominant |

**Comments:** It is acknowledged that there is increasing evidence supporting that some of these genes/variants may also be recessive (e.g., MYL2, MYL3), but addressing those edge cases was outside the scope of this current guideline.

---

### PM4 - Protein Length Changes

**Original ACMG Summary:** Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

#### VCEP Specification

| Strength | Criteria |
|----------|----------|
| **Moderate** | Default strength; may require downgrading based on predicted impact |
| **Supporting** | Consider if impact is less severe |

**Guidance:**
- Strength of rule should be carefully considered and may require downgrading to SUPPORTING based on the predicted impact of the variant, including the size of the deletion/insertion, its location, and conservation of the region
- For genes where PVS1 is not applicable (i.e., where there is no evidence that pLOF variants cause disease), consider using this rule at MODERATE or SUPPORTING strength for truncating variants that do NOT undergo nonsense mediated decay (NMD)

**Modification Type:** Disease-specific

---

### PM5 - Novel Missense at Same Residue

**Original ACMG Summary:** Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.

**Example:** Arg156His is pathogenic; now you observe Arg156Cys.

**Caveat:** Beware of changes that impact splicing rather than at the amino acid/protein level.

#### VCEP Specification

| Strength | Criteria |
|----------|----------|
| **Moderate** | Different missense variant at the same codon has been classified as **pathogenic** using these modified guidelines without application of PM5 |
| **Supporting** | Different missense variant at the same codon has been classified as **likely pathogenic** using these modified guidelines without application of PM5 |

**Considerations:**
- The impact of the amino acid change being evaluated needs to be compared to the impact of the amino acid change that is established as pathogenic/likely pathogenic
- Example: A change of Ala to His is less severe than Ala to Cys change
- Consider reducing strength if the predicted impact is not expected to be equivalent or more severe

**Important:** PM5 should **NOT** be combined with PM1. If both are applicable:
- At MODERATE weight: use PM5 (it is variant specific)
- At different strengths: use the one with higher strength
- At SUPPORTING weight: use PM5 (it is variant specific)

**Modification Type:** General recommendation

---

### PM6 - De Novo (Assumed)

**Original ACMG Summary:** Assumed de novo, but without confirmation of paternity and maternity.

#### VCEP Specification

| Strength | Criteria |
|----------|----------|
| **Moderate** | Refer to SVI guidance on number/combination of cases required based on phenotype specificity |

**Guidance:**
- For most cardiomyopathies, it is recommended to default to "phenotype consistent with gene but not highly specific"
- Clinical judgment is required for shifting to a higher or lower phenotypic consistency
- See PS2 for additional considerations and point system

**Modification Type:** Disease-specific

---

### PP1 - Co-segregation

**Original ACMG Summary:** Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.

**Note:** May be used as stronger evidence with increasing segregation data.

#### VCEP Specifications

Due to the genotypic and phenotypic heterogeneity of inherited cardiomyopathies, segregation thresholds have been conservatively set.

| Strength | Standard Threshold | Highly Specific Phenotype |
|----------|-------------------|---------------------------|
| **Strong** | ≥7 segregations (LOD 2.1) | ≥5 segregations (LOD 1.5) |
| **Moderate** | ≥5 segregations (LOD 1.5) | ≥4 segregations (LOD 1.2) |
| **Supporting** | ≥3 segregations (LOD 0.9) | ≥3 segregations (LOD 0.9) |

**Highly Specific Phenotype Example:** Early-onset severe RCM in all affected individuals (rare for inherited cardiomyopathies)

**Counting Segregations:**
- Only **genotype positive/phenotype positive** individuals are counted as segregations
- Can include affected obligate carriers
- Genotype positive/phenotype negative individuals are generally less informative due to variable age at onset and reduced penetrance
- Phenotypes should be clinically confirmed, whenever possible
- Should not include individuals with a suspected diagnosis

**Important Considerations:**
1. Segregation within a single family or haplotype may represent linkage disequilibrium with another undetected variant — consider downgrading if this is a concern
2. Use of segregation criteria should be carefully evaluated if variant frequency meets criteria for BS1
3. Caution is needed when counting segregations in presence of other possible disease-causing variants
4. Caution is needed when distantly related (≥3rd degree) affected individuals are connected by unknown or unaffected relatives (raises possibility of multiple causes of disease)

**Modification Type:** Disease-specific

---

### PP2 - Missense in Constrained Gene

**Original ACMG Summary:** Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.

#### VCEP Specification

| Strength | Criteria |
|----------|----------|
| **Not Applicable** | See comments below |

**Comments:** Application of this rule takes into consideration empirical data quantifying levels of rare missense variant enrichment in HCM referral cohorts compared to population-based cohorts (Walsh et al. 2019 PMID:30696458) rather than the missense constraint score in gnomAD. For MYH7, there is evidence for regional enrichment of rare missense variants (see PM1 specifications).

---

### PP3 - Computational Evidence

**Original ACMG Summary:** Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).

**Caveat:** As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.

#### VCEP Specification

| Strength | Criteria |
|----------|----------|
| **Supporting** | REVEL score ≥0.70 |

**Guidance:**
- As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion
- **Meta-predictors, such as REVEL, are preferred** over multiple individual predictors
- Use of REVEL (Ioannidis et al. 2016) is recommended at thresholds of **≥0.70 for PP3**
- Clinical judgment is needed if any individual algorithms or conservation data are contradictory to REVEL data
- Positive predictive value for benign/no impact predictions is generally higher than for pathogenic/impact predictions
- **SpliceAI** is recommended for evaluation of predicted splice impacts

**Modification Type:** Disease-specific

---

### PP4 - Phenotype Specificity

**Original ACMG Summary:** Patient's phenotype or family history is highly specific for a disease with a single genetic etiology.

#### VCEP Specification

| Strength | Criteria |
|----------|----------|
| **Not Applicable** | Inherited cardiomyopathies have high locus heterogeneity as well as non-genetic etiologies |

---

### PP5 - Reputable Source

**Original ACMG Summary:** Reputable source recently reports variant as pathogenic, but the evidence is not available to the laboratory to perform an independent evaluation.

#### VCEP Specification

| Strength | Criteria |
|----------|----------|
| **Not Applicable** | This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PMID: 29543229) |

---

## Benign Criteria

### BA1 - Allele Frequency >0.1%

**Original ACMG Summary:** Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

#### VCEP Specification

| Strength | Criteria |
|----------|----------|
| **Stand Alone** | Allele frequency is **≥0.001 (0.1%)** based on the filtering allele frequency (FAF) in gnomAD in the subpopulation with the highest frequency (popmax) |

**Threshold Derivation:**
- Values derived from studies in Northern European populations
- Thresholds can be applied to any population where disease prevalence is considered comparable (1/300 or lower)
- Threshold is applicable when assessing variants in the context of autosomal dominant cardiomyopathy

**gnomAD Usage:**
- gnomAD is the preferred database for this calculation
- If a subpopulation specific FAF other than the popmax is needed, this value can be calculated using the AlleleFrequencyApp on the CardioDB website:
  1. Using the Inverse AF tab, enter in the population size and the number of alleles identified
  2. Set confidence to 0.95 (95%)
  3. If the FAF is ≥0.001, this rule can be applied

**Platform Considerations:**
- The FAF by platform (e.g., exome vs. genome; v.2.1.1 vs. v.3.1.1) should be considered
- The larger population is most likely to have the most accurate representation of "true" population allele frequency

**Caution:**
- Use caution when considering any population cohorts that are smaller than the smallest subpopulations within gnomAD v.2.1.1 (e.g., ~5000 individuals or ~10,000 alleles)
- Despite the conservative nature of this threshold, in smaller cohorts, the observed allele frequency may less accurately reflect the true allele frequency
- Traditionally, once a variant is classified as Benign, it is rarely re-evaluated — highest confidence is needed

**Modification Type:** Disease-specific

---

### BS1 - Frequency Greater Than Expected

**Original ACMG Summary:** Allele frequency is greater than expected for disorder.

#### VCEP Specification

| Strength | Criteria |
|----------|----------|
| **Strong** | Allele frequency is **≥0.0001 (0.01%)** for MYH7 based on the filtering allele frequency (FAF) in gnomAD in the subpopulation with the highest frequency (popmax) |

**Important:** Criterion BS1 may only be used as standalone evidence to classify a variant as Likely Benign in the absence of conflicting data. See SVI guidance (Tavtigian et al. 2018; Tavtigian et al. 2020).

See BA1 for additional specifications that also apply to BS1.

**Modification Type:** Disease-specific, Gene-specific

---

### BS2 - Observed in Healthy Adult

**Original ACMG Summary:** Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

#### VCEP Specification

| Strength | Criteria |
|----------|----------|
| **Not Applicable** | Inherited cardiomyopathies generally display reduced penetrance, variable expressivity, and adult-onset |

---

### BS3 - Functional Studies (No Effect)

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

#### VCEP Specifications

**General Guidance:**
- Evaluation of studies/assays is required prior to application of functional evidence at any strength
- Refer to SVI guidance for functional evidence (Brnich et al. 2020)
- In the context of cardiomyopathy, very few functional assays currently meet criteria sufficient for application of this rule at a STRONG level
- Examples of the types of study/assays that MAY be relevant are described, but further definition of cardiomyopathy models/assays is outside the scope of these guidelines

| Strength | Criteria |
|----------|----------|
| **Strong** | See PS3 specifications (reciprocal application) |
| **Moderate** | See PS3 specifications (reciprocal application) |
| **Supporting** | See PS3 specifications (reciprocal application) |

**Modification Type:** Disease-specific

---

### BS4 - Lack of Segregation

**Original ACMG Summary:** Lack of segregation in affected members of a family.

**Caveat:** The presence of phenocopies for common phenotypes (i.e., cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.

#### VCEP Specification

| Strength | Criteria |
|----------|----------|
| **Strong** | Multiple (≥2) non-segregations that are highly unlikely to be phenocopies or due to alternate variants |

**Evaluation Requirements:**
Any non-segregations should be carefully evaluated to rule out a phenocopy or the presence of a second disease-causing variant before considering it as conflicting or benign evidence.

**Phenocopies in Cardiomyopathy:**
- Athlete's heart
- Hypertensive heart disease
- Ischemic cardiomyopathy
- Alcoholic cardiomyopathy
- Diabetic cardiomyopathy

**Multiple Pathogenic Variants:**
Families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent 'non-segregation'.

**Requirements:**
- Multiple (≥2) non-segregations that are highly unlikely to be phenocopies or due to alternate variants are required to apply this rule
- A higher number of non-segregations is necessary for instances where alternative causes are possible (e.g., non-segregation in a sibling with childhood onset cardiomyopathy versus a grandparent with hypertension and HCM)

**Caution:** Careful consideration of the above points is required when using this data as conflicting evidence, especially when overall evidence supports likely pathogenic or pathogenic.

**Modification Type:** Disease-specific

---

### BP1-BP7 - Benign Supporting

| Criterion | Status | Specification |
|-----------|--------|---------------|
| **BP1** | Not Applicable | For the current genes where null variants are a known mechanism, pathogenic missense variants have also been reported |
| **BP2** | Supporting | Other variants must be pathogenic as defined by these specifications. Testing of parents or other informative relatives is often required to determine cis/trans status. If a variant is seen in trans (or as double heterozygous) with another pathogenic variant in ≥2 cases and the phenotype is not more severe than when either of the two variants are seen in isolation, this rule may be applied. <1% of cases of HCM have >1 pathogenic or likely pathogenic variant (0.6%; Alfares et al. 2015). Cannot be applied when variant has only been observed in cis with a pathogenic variant. |
| **BP3** | Not Applicable | Not applicable to the current genes |
| **BP4** | Supporting | Use REVEL score ≤0.40. Meta-predictors preferred. Clinical judgment needed if contradictory. SpliceAI recommended for splice predictions. |
| **BP5** | Not Applicable | Co-occurrence with an established pathogenic or likely pathogenic variant for a non-cardiomyopathy related disease does not reduce the likelihood that a variant is independently disease-causing for cardiomyopathy |
| **BP6** | Not Applicable | This criterion is not for use as recommended by the ClinGen SVI VCEP Review Committee (PMID: 29543229) |
| **BP7** | Supporting | Also applicable to intronic variants outside the splice consensus sequence (-4 and +7 outward) for which splicing prediction algorithms predict no impact to the splice consensus sequence NOR the creation of a new splice site AND the nucleotide is not highly conserved. Rule can be combined with BP4 to make a variant likely benign per Richards et al. 2015. |

---

## Rules for Combining Criteria

### Pathogenic Classification

| Criteria Combination |
|---------------------|
| ≥2 Strong (PS1, PS2, PS3, PS4, PP1_Strong) |
| 1 Strong (PS1, PS2, PS3, PS4, PP1_Strong) **AND** ≥3 Moderate (PS3_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate) |
| 1 Strong (PS1, PS2, PS3, PS4, PP1_Strong) **AND** 2 Moderate (PS3_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate) **AND** ≥2 Supporting (PS3_Supporting, PS4_Supporting, PM2_Supporting, PM5_Supporting, PP1, PP3) |
| 1 Strong (PS1, PS2, PS3, PS4, PP1_Strong) **AND** 1 Moderate (PS3_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate) **AND** ≥4 Supporting (PS3_Supporting, PS4_Supporting, PM2_Supporting, PM5_Supporting, PP1, PP3) |

### Likely Pathogenic Classification

| Criteria Combination |
|---------------------|
| 1 Strong (PS1, PS2, PS3, PS4, PP1_Strong) **AND** 1 Moderate (PS3_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate) |
| 1 Strong (PS1, PS2, PS3, PS4, PP1_Strong) **AND** ≥2 Supporting (PS3_Supporting, PS4_Supporting, PM2_Supporting, PM5_Supporting, PP1, PP3) |
| ≥3 Moderate (PS3_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate) |
| 2 Moderate (PS3_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate) **AND** ≥2 Supporting (PS3_Supporting, PS4_Supporting, PM2_Supporting, PM5_Supporting, PP1, PP3) |
| 1 Moderate (PS3_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate) **AND** ≥4 Supporting (PS3_Supporting, PS4_Supporting, PM2_Supporting, PM5_Supporting, PP1, PP3) |
| 1 Strong (PS1, PS2, PS3, PS4, PP1_Strong) **AND** 2 Moderate (PS3_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate) |

### Benign Classification

| Criteria Combination |
|---------------------|
| ≥2 Strong (BS1, BS3, BS4) |
| 1 Stand Alone (BA1) |

### Likely Benign Classification

| Criteria Combination |
|---------------------|
| 1 Strong (BS1, BS3, BS4) **AND** 1 Supporting (BS3_Supporting, BP2, BP4, BP7) |
| ≥2 Supporting (BS3_Supporting, BP2, BP4, BP7) |

---

## Appendices

### Appendix A: Criteria Summary Table

| Criterion | MYH7 Status | Strength(s) | Key Threshold/Notes |
|-----------|-------------|-------------|---------------------|
| PVS1 | Not Applicable | - | LOF not a disease mechanism |
| PS1 | Applicable | Strong | No modification |
| PS2 | Applicable | Strong/Moderate/Supporting | Point-based system; default "phenotype consistent but not highly specific" |
| PS3 | Applicable | Strong/Moderate/Supporting | Splicing assays (Strong), animal models (Moderate), in vitro assays (Supporting) |
| PS4 | Applicable | Strong/Moderate/Supporting | OR lower 95% CI: ≥20 (Strong), ≥10 (Moderate), ≥5 (Supporting) |
| PM1 | Applicable | Moderate | Codons 167-931 (HCM only); cannot combine with PM5 |
| PM2 | Applicable | Supporting only | ≤0.00004 upper bound 95% CI |
| PM3 | Not Applicable | - | Dominant inheritance |
| PM4 | Applicable | Moderate/Supporting | Consider impact, size, location |
| PM5 | Applicable | Moderate/Supporting | Based on P/LP at same codon; cannot combine with PM1 |
| PM6 | Applicable | Moderate | Use PS2 point system |
| PP1 | Applicable | Strong/Moderate/Supporting | ≥7/≥5/≥3 segregations |
| PP2 | Not Applicable | - | Regional enrichment addressed via PM1 |
| PP3 | Applicable | Supporting | REVEL ≥0.70 |
| PP4 | Not Applicable | - | High locus heterogeneity |
| PP5 | Not Applicable | - | Per SVI recommendations |
| BA1 | Applicable | Stand Alone | FAF ≥0.001 (popmax) |
| BS1 | Applicable | Strong | FAF ≥0.0001 for MYH7 (popmax) |
| BS2 | Not Applicable | - | Reduced penetrance, variable expressivity |
| BS3 | Applicable | Strong/Moderate/Supporting | See PS3 specifications |
| BS4 | Applicable | Strong | ≥2 non-segregations (not phenocopies) |
| BP1 | Not Applicable | - | Missense variants are pathogenic |
| BP2 | Applicable | Supporting | In trans with P variant in ≥2 cases |
| BP3 | Not Applicable | - | No repetitive regions |
| BP4 | Applicable | Supporting | REVEL ≤0.40 |
| BP5 | Not Applicable | - | Does not reduce likelihood |
| BP6 | Not Applicable | - | Per SVI recommendations |
| BP7 | Applicable | Supporting | Synonymous/intronic; combine with BP4 |

### Appendix B: Population Frequency Thresholds Summary

| Criterion | Threshold | Database | Metric | Strength |
|-----------|-----------|----------|--------|----------|
| BA1 | ≥0.001 | gnomAD | FAF (popmax) | Stand Alone |
| BS1 | ≥0.0001 | gnomAD | FAF (popmax) | Strong |
| PM2 | ≤0.00004 | gnomAD | Upper bound 95% CI (popmax) | Supporting |

### Appendix C: PS4 Example Scenarios

#### General Example - Variant A (Strong)

**Scenario:** Variant detected in 22/7,437 clinical lab cases and 13/9,162 literature cases. gnomAD frequency: 1/241,182 alleles.

| Comparison | OR [95% CI] | Rule Strength |
|------------|-------------|---------------|
| Clinical lab vs gnomAD (Total) | 358 [**48**-2,655] | STRONG |
| Literature vs gnomAD (Total) | 171 [**22**-1,310] | STRONG |

**Interpretation:** Both lower bounds of 95% CI are ≥20, therefore PS4 at STRONG.

#### Selecting a Control Cohort - Variant B (Moderate)

**Scenario:** Predominantly European variant. When using gnomAD European data (more appropriate for population matching), lower bound falls into MODERATE range.

| Comparison | OR [95% CI] | Rule Strength |
|------------|-------------|---------------|
| Clinical lab vs gnomAD (Total) | 248 [**32**-1,905] | STRONG |
| Clinical lab vs gnomAD (European) | 128 [**17**-988] | MODERATE |

**Interpretation:** Use the more conservative and appropriate population comparison. Apply PS4 at MODERATE.

#### Comparing Multiple Cohorts - Variant C (STRONG or MODERATE)

**Scenario:** Variant detected in multiple non-overlapping cohorts with consistent DCM phenotype, absent in gnomAD.

**Key Considerations:**
1. Variant not detected in gnomAD (v2.1.1 or v3.1.2)
2. Phenotype consistent across multiple cohorts (all DCM)
3. Variant enriched in three apparently non-overlapping cohorts
4. Criteria for PS4 rule application are intentionally conservative

**Interpretation:** STRONG is acceptable given evidence; MODERATE also appropriate if conservative approach preferred.

### Appendix D: References

1. Richards S, Aziz N, et al. Standards and guidelines for the interpretation of sequence variants: a joint consensus recommendation of the American College of Medical Genetics and Genomics and the Association for Molecular Pathology. *Genet Med* (2015) 17(5):405-24. PMID: 25741868

2. Abou Tayoun AN, Pesaran T, et al. Recommendations for interpreting the loss of function PVS1 ACMG/AMP variant criterion. *Hum Mutat* (2018) 39(11):1517-1524. PMID: 30192042

3. Brnich SE, Abou Tayoun AN, et al. Recommendations for application of the functional evidence PS3/BS3 criterion using the ACMG/AMP sequence variant interpretation framework. *Genome Med* (2019) 12(1):3. PMID: 31892348

4. Walsh R, Thomson KL, et al. Reassessment of Mendelian gene pathogenicity using 7,855 cardiomyopathy cases and 60,706 reference samples. *Genet Med* (2017) 19(2):192-203. PMID: 27532257

5. Walsh R, Mazzarotto F, et al. Quantitative approaches to variant classification increase the yield and precision of genetic testing in Mendelian diseases: the case of hypertrophic cardiomyopathy. *Genome Med* (2019) 11(1):5. PMID: 30696458

6. Kelly MA, Caleshu C, et al. Adaptation and validation of the ACMG/AMP variant classification framework for MYH7-associated inherited cardiomyopathies: recommendations by ClinGen's Inherited Cardiomyopathy Expert Panel. *Genet Med* (2018) 20(3):351-359. PMID: 29300372

7. Jarvik GP, Browning BL. Consideration of Cosegregation in the Pathogenicity Classification of Genomic Variants. *Am J Hum Genet* (2016) 98(6):1077-1081. PMID: 27236918

8. Ioannidis NM, Rothstein JH, et al. REVEL: An Ensemble Method for Predicting the Pathogenicity of Rare Missense Variants. *Am J Hum Genet* (2016) 99(4):877-885. PMID: 27666373

9. Jaganathan K, Kyriazopoulou Panagiotopoulou S, et al. Predicting Splicing from Primary Sequence with Deep Learning. *Cell* (2019) 176(3):535-548.e24. PMID: 30661751

10. Tavtigian SV, Greenblatt MS, et al. Modeling the ACMG/AMP variant classification guidelines as a Bayesian classification framework. *Genet Med* (2018) 20(9):1054-1060. PMID: 29300386

11. Tavtigian SV, Harrison SM, et al. Fitting a naturally scaled point system to the ACMG/AMP variant classification guidelines. *Hum Mutat* (2020) 41(10):1734-1737. PMID: 32720330

12. Alfares AA, Kelly MA, et al. Results of clinical genetic testing of 2,912 probands with hypertrophic cardiomyopathy: expanded panels offer limited additional sensitivity. *Genet Med* (2015) 17(11):880-8. PMID: 25611685

13. Anderson RH, Jensen B, et al. Key Questions Relating to Left Ventricular Noncompaction Cardiomyopathy: Is the Emperor Still Wearing Any Clothes? *Can J Cardiol* (2017) 33(6):747-757. PMID: 28395867

14. Oechslin E, Jenni R. Nosology of Noncompaction Cardiomyopathy: The Emperor Still Wears Clothes! *Can J Cardiol* (2017) 33(6):701-704. PMID: 28545618

15. Hershberger RE, Morales A, et al. Is Left Ventricular Noncompaction a Trait, Phenotype, or Disease? The Evidence Points to Phenotype. *Circ Cardiovasc Genet* (2017) 10(6). PMID: 29212902

16. Ross SB, Jones K, et al. A systematic review and meta-analysis of the prevalence of left ventricular non-compaction in adults. *Eur Heart J* (2020) 41(14):1428-1436. PMID: 31143950

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 2.0.0 | April 22, 2024 | Updated ClinGen Cardiomyopathy Expert Panel Specifications to the ACMG/AMP Variant Interpretation Guidelines for MYH7. PM1 region updated from v1.0. |
| 1.0.0 | 2018 | Initial release (Kelly et al. 2018) |

---

*This document was compiled from ClinGen VCEP specifications and ClinGen SVI recommendations. For the most current version, please refer to the [ClinGen website](https://clinicalgenome.org/).*

*PS4 Calculator available at: [www.cardiodb.org](https://www.cardiodb.org)*

*Confidence interval tools: [Confit-de-MAF](https://github.com/svi-working-group/confit-de-maf)*
