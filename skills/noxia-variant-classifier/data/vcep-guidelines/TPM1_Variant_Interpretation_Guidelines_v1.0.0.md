# ClinGen Cardiomyopathy Expert Panel Variant Interpretation Guidelines for TPM1

**Version:** 1.0.0
**Released:** 4/22/2024
**Affiliation:** Cardiomyopathy VCEP
**Based on:** Richards et al., 2015 ACMG/AMP Guidelines

---

## Gene Information

| Attribute | Value |
|-----------|-------|
| **Gene** | TPM1 (HGNC:12010) |
| **HGNC Name** | tropomyosin 1 |
| **Transcript** | NM_001018005.2 |
| **Disease** | hypertrophic cardiomyopathy (MONDO:0005045) |
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

**VCEP Specification:** ***Not Applicable***

**Comments:** Not currently applicable to TPM1. See PM4 for truncating variants that do NOT undergo NMD.

---

### PS1 - Same Amino Acid Change

**Original ACMG Summary:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change. Example: Val->Leu caused by either G>C or G>T in the same codon. Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specification:**

| Strength | Criteria |
|----------|----------|
| **Strong** | No cardiomyopathy specifications. Apply as outlined by Richards et al. 2015. |

**Example of when rule should NOT be applied:** NM_000256.3(*MYBPC3*): c.2308G>A (p.Asp770Asn) has an established impact on splicing leading to nonsense mediated decay (NMD) and should not be used to provide evidence for other variants observed to result in the same amino acid change.

**Modification Type:** No change

---

### PS2 - De Novo (Confirmed)

**Original ACMG Summary:** De novo (both maternity and paternity confirmed) in a patient with the disease and no family history. Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.

**VCEP Specifications:**

Refer to SVI guidance on number/combination of cases required based on phenotype specificity.

For most cardiomyopathies, it is recommended to default to **Phenotype consistency: "Phenotype consistent with gene but not highly specific"**. Clinical judgment is required for shifting to a higher or lower category.

For use as a **STRONG** or **VERY STRONG** criterion, ideally parents have been thoroughly clinically evaluated without evidence of cardiomyopathy (ideally using a combination of ECG and echocardiogram or cardiac MRI for maximum sensitivity).

A family history consistent with *de novo* inheritance should not have any clinical signs or symptoms suggestive of cardiomyopathy in a 1st or 2nd degree relative, for example:
1. Sudden death under 60 years of age
2. Heart transplant
3. Implantable cardiac defibrillator (ICD) under 60 years of age
4. Features of cardiomyopathy (e.g., systolic dysfunction, hypertrophy, left ventricular enlargement in an individual without risk factors)
5. Other related/overlapping cardiomyopathies

Examples of non-suspicious family history may include non-specific clinical features (e.g., palpitations, syncope, borderline/inconclusive echocardiogram findings, heart attack if age appropriate and suspected to result from coronary artery disease), but every attempt should be made to clarify features.

Generally, this criterion is only applicable in the **ABSENCE** of any other possible disease-causing variants. If other pathogenic or likely pathogenic variants are present, consider decreasing points assigned or overall weight.

#### PS2/PM6 Point System

| Phenotypic Consistency | Confirmed Parental Relationships | Unconfirmed |
|------------------------|----------------------------------|-------------|
| Phenotype highly specific for gene | 2 points | 1 point |
| Phenotype consistent but not highly specific | 1 point | 0.5 points |
| Phenotype consistent + high genetic heterogeneity | 0.5 points | 0.25 points |
| Phenotype not consistent | 0 points | 0 points |

**Default for cardiomyopathies:** "Phenotype consistent with gene but not highly specific" (1 point confirmed / 0.5 points unconfirmed)

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

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product. Note: Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.

**VCEP Specifications:**

Evaluation of studies/assays is required prior to application of functional evidence at any strength. Refer to SVI guidance for functional evidence (Brnich *et al.* 2020). In the context of cardiomyopathy, very few functional assays currently meet criteria sufficient for application of this rule at a STRONG level. Examples of the types of study/assays that MAY be relevant are described, but further definition of cardiomyopathy models/assays is outside the scope of these guidelines.

| Strength | Criteria |
|----------|----------|
| **Strong** | **In vitro splicing assays (e.g., RNA studies)** — see detailed requirements below |
| **Moderate** | **In vivo models (e.g., variant knock-in animal models)** — see detailed requirements below |
| **Supporting** | **In vitro assays (e.g., biochemical assays of myofilament function, motility assays, human iPSC-CM)** |

#### Strong — In Vitro Splicing Assays

*In vitro* splicing assays may be considered as **STRONG** evidence, providing the following criteria are met:
- Prior knowledge of predominant transcripts in cardiac tissue
- Analysis undertaken using RNA extracted from cardiac tissue from the individual with the variant
- Analysis undertaken using RNA extracted from whole blood providing the relevant transcripts (isoforms) are expressed in blood and are at sufficient levels to assess splice disruption
- Assay shows a clear, reproducible and convincing effect on splicing (i.e. a distinct splice product, present at a level comparable to the splice product from the wild-type allele), which is not observed in controls
- Confirmation of abnormal splice product by Sanger sequencing

**NOTE:** Mini-gene assay in non-patient derived cell lines are NOT considered to provide STRONG evidence.

**NOTE:** Whether to activate this rule needs to be reconciled with the variant spectrum and disease mechanism for the gene at hand (i.e., consider whether the effect is likely to lead to LOF or an in-frame alteration and whether this type of effect is expected to be disease causing) (Abou Tayoun *et al.* 2018).

#### Moderate — In Vivo Models

Mammalian variant-specific knock-in animal models that produce a phenotype consistent with the clinical phenotype in humans (e.g., structural and/or functional cardiac abnormalities, premature death, arrhythmia) may be considered as **MODERATE** evidence.

**NOTE:** The following assays/models do NOT meet criteria:
1. Assays that are known to be associated with non-specific cardiac phenotypes (e.g., morpholino-induced pericardial edema in zebrafish)
2. *In vivo* evidence that is not variant specific, such as whole gene alterations (i.e., cDNA or whole gene transgenic mice and whole or partial gene knock-out mice)

#### Supporting — In Vitro Assays

While some *in vitro* assays may provide evidence that a variant in a cardiomyopathy gene has an effect on protein and/or myofilament function, at present, there are no validated "gold-standard" assays that are considered to reliably predict the clinical phenotype. As such, in the cardiomyopathy genes listed in these guidelines, data from individual *in vitro* studies are unlikely to meet the criteria required to assign this rule at more than SUPPORTING level.

**Modification Type:** Disease-specific

---

### PS4 - Prevalence in Affected

**Original ACMG Summary:** The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.

**VCEP Specifications:**

Currently few well-designed case-control studies have been performed for inherited cardiomyopathies. Until such studies become available, comparative analyses can be undertaken using case data (e.g., internal and/or published cohorts) and control data from population-level cohorts (e.g., gnomAD).

#### Cohort Criteria

Cohorts used in these analyses should meet the following criteria:
1. The cases have a clinical diagnosis of the specified disorder or related phenotype (e.g., all cases have HCM or another relevant phenotype*)
   - When assessing cases, consider how likely another potential cause of the phenotype has been excluded, including the presence of other variants in relevant genes and the extent of testing performed
2. The controls should not be derived from study populations that might be enriched for the specified disorder
3. The denominator of the cohorts must be available (e.g., variant detected in 5 out of 3,500 cases and 1 out of 60,000 controls)
4. The cohorts do not include closely related individuals (i.e., family members are not included in the case counts)
5. The cohorts do not overlap with other cohorts being used in the analysis (i.e., cases are not being counted more than once)
6. The population diversity of the case and control cohorts are broadly similar
7. Consider the size of the case cohort — larger cohorts are likely to provide more accurate estimates of variant frequency; prefer data from the largest available case series (e.g., Walsh *et al.* 2017, DECIPHER)

#### Strength Levels

| Strength | OR Threshold (Lower Bound of 95% CI) |
|----------|---------------------------------------|
| **Strong** | Lower bound of 95% CI of OR **≥20** |
| **Moderate** | Lower bound of 95% CI of OR **≥10** |
| **Supporting** | Lower bound of 95% CI of OR **≥5** |

A PS4 calculator is available at www.cardiodb.org.

If multiple cohorts are available, the final ORs and associated CIs need to be harmonized across all cohorts to determine the final level (e.g., if 2 large cohorts have an OR of ~6 and a third small cohort has an OR of 11, application at a SUPPORTING level should be considered).

#### *Relevant Phenotypes

1. Cases of HCM and RCM may be combined as they are considered part of the same disease spectrum
2. For the eight genes covered by these guidelines, the combination of probands with other phenotypes should be reviewed by a clinical expert to determine if grouping is appropriate
3. Additional considerations for LVNC and end-stage HCM:
   - Due to the current debate about whether isolated LVNC represents a true disease entity or variation of typical cardiac morphology, individuals with isolated LVNC should **NOT** be added to proband or segregation counts (including individuals with isolated LVNC in a family with other cardiomyopathies)
4. HCM and DCM have distinct mechanisms of disease and therefore pathogenetic variants are not anticipated to cause both primary phenotypes. While occurrence in both phenotypes may initially be considered as evidence against pathogenicity, end-stage HCM can present similarly to DCM. Careful consideration is needed before including DCM or related phenotypes in case or segregation data for primarily HCM variants.

#### PS4 Example Scenarios

**Variant A (General Example):**
Variant A detected in clinical lab (22/7,437 HCM cases) and literature (13/9,162 HCM cases). gnomAD total frequency: 1/241,182 alleles. Both case vs. gnomAD analyses yield lower 95% CI of OR ≥20 → **PS4 STRONG**.

| Comparison | OR [95% CI] | Strength |
|------------|-------------|----------|
| Clinical lab (22/7,437) vs gnomAD Total (1/120,591) | 358 [**48**-2,655] | STRONG |
| Literature (13/9,162) vs gnomAD Total (1/120,591) | 171 [**22**-1,310] | STRONG |

**Variant B (Selecting a Control Cohort):**
A predominantly European variant. gnomAD Total yields STRONG, but gnomAD European (more conservative) yields MODERATE → **PS4 MODERATE** recommended.

| Comparison | OR [95% CI] | Strength |
|------------|-------------|----------|
| Clinical lab (12/5,792) vs gnomAD Total | 248 [**32**-1,905] | STRONG |
| Literature (15/7,873) vs gnomAD Total | 227 [**30**-1,724] | STRONG |
| Clinical lab (12/5,792) vs gnomAD European | 128 [**17**-988] | MODERATE |
| Literature (15/7,873) vs gnomAD European | 118 [**16**-894] | MODERATE |

**Variant C (Comparing Cohort and Available Data):**
Multiple non-overlapping DCM cohorts, variant absent from gnomAD. Results range from MODERATE to STRONG. Acceptable to apply PS4 at STRONG given consistency, but MODERATE is also appropriate with a more conservative approach.

| Comparison | OR [95% CI] | Strength |
|------------|-------------|----------|
| Clinical lab A (4/2,481) vs gnomAD Total (0/116,190) | 422 [**23**-7,841] | STRONG |
| Clinical lab B (8/5,953) vs gnomAD Total (0/116,190) | 332 [**19**-5,757] | MODERATE |
| Literature (6/5,154) vs gnomAD Total (0/116,190) | 293 [**16**-5,208] | MODERATE |

**Modification Type:** Disease-specific

---

### PM1 - Mutational Hot Spot

**Original ACMG Summary:** Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.

**VCEP Specification:** ***Not Applicable***

**Comments:** Application of this rule takes into consideration empirical data quantifying levels of rare missense variant enrichment in HCM referral cohorts compared to population-based cohorts (Walsh *et al.* 2019, PMID:30696458). For TPM1, there is evidence for gene-level enrichment of rare missense variants (see PP2 specifications).

---

### PM2 - Absent from Controls

**Original ACMG Summary:** Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium. Caveat: Population data for indels may be poorly called by next generation sequencing.

**VCEP Specification (Supporting only):**

A threshold of **≤0.00004** in the subpopulation with the highest frequency when using the upper bound of the 95% CI activates this rule.

1. Alternatively, this is equivalent to the variant NOT being observed more than once (≤1 allele) in gnomAD v.2.1.1 in one of the non-founder populations (e.g., absence required from the Other and Ashkenazi Jewish subpopulations).
2. Applying a threshold of ≤0.00004 (upper bound of 95% CI of the allele frequency in gnomAD) is equivalent to the variant being seen in a single subpopulation meeting any of the following:

| Allele Count (AC) | Allele Number (AN) |
|--------------------|--------------------|
| ≤1 | ≥120,000 |
| ≤2 | ≥160,000 |
| ≤3 | ≥195,000 |
| ≤4 | ≥230,000 |

gnomAD is the preferred database for this calculation, but currently only displays the filtering allele frequency (FAF), which is equivalent to a lower bound estimate of the 95% CI, when the upper bound is what is needed. Confidence interval tools, such as Confit-de-MAF, can be used to determine the upper bound of the 95% CI of the observed allele frequency.

**Additional Notes:**
- Due to current technical limitations of next generation sequencing technologies, minor allele frequencies for complex variants (e.g., large indels) may not be accurately represented in population databases
- Caution should be used when a variant is only identified, or over-represented, in one of the smaller gnomAD populations, as the gnomAD allele frequencies may not accurately represent the true population frequency
- Population databases may contain affected or pre-symptomatic individuals for diseases with reduced penetrance/variable onset

**Derivation Notes:** The values used to calculate the PM2 thresholds were derived from studies in Northern European populations that have been relatively well-characterized with regards to disease prevalence and variant spectrum. These thresholds can be applied to any population where disease prevalence is considered comparable (1/500 or lower), where the most frequent pathogenic variant accounts for no more than 2% of cases (e.g., has an allele frequency of ≤0.02 in cases based on the upper bound of 95% CI), and where the penetrance of a pathogenic variant is expected to be at least 50% (Kelly *et al.* 2018).

**Modification Type:** Disease-specific

---

### PM3 - In Trans with Pathogenic

**Original ACMG Summary:** For recessive disorders, detected in trans with a pathogenic variant. Note: This requires testing of parents (or offspring) to determine phase.

**VCEP Specification:** ***Not Applicable***

**Comments:** While compound heterozygosity leading to a more severe phenotype has been documented, this rule was designed for traditional recessive inheritance. It is acknowledged that there is increasing evidence supporting that some of these genes/variants may also be recessive (e.g., MYL2, MYL3), but addressing those edge cases was outside the scope of this current guideline.

---

### PM4 - Protein Length Changes

**Original ACMG Summary:** Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Moderate** | Strength of rule should be carefully considered and may require downgrading to SUPPORTING based on the predicted impact of the variant, including the size of the deletion/insertion, its location, and conservation of the region. For genes where PVS1 is not applicable (i.e., where there is no evidence that pLOF variants cause disease), consider using this rule at MODERATE or SUPPORTING strength for **truncating variants that do NOT undergo nonsense mediated decay (NMD)**. |
| **Supporting** | May be downgraded from Moderate based on predicted impact assessment. |

**Modification Type:** General recommendation

---

### PM5 - Novel Missense at Same Residue

**Original ACMG Summary:** Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before. Example: Arg156His is pathogenic; now you observe Arg156Cys. Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Moderate** | Can be used at MODERATE if a different missense variant at the same codon has been classified as *pathogenic* using these modified guidelines without application of PM5. The impact of the amino acid change being evaluated needs to be compared to the impact of the established pathogenic change (e.g., a change of Ala to His is less severe than Ala to Cys). Consider reducing to SUPPORTING if the predicted impact is not expected to be equivalent or more severe. |
| **Supporting** | Can be considered at SUPPORTING if a different missense variant at the same codon has been classified as *likely pathogenic* using these modified guidelines without application of PM5. Consider reducing to NOT APPLICABLE if the predicted impact is not expected to be equivalent or more severe. |

**Important:** PM5 should **not** be combined with PM1. If both are applicable at MODERATE weight, use of PM5 is most appropriate since it is variant specific. If both are applicable at SUPPORTING weight, PM5 should be preferred. If they are applicable at different strengths, the one with the higher strength should be applied.

**Modification Type:** General recommendation

---

### PM6 - De Novo (Assumed)

**Original ACMG Summary:** Assumed de novo, but without confirmation of paternity and maternity.

**VCEP Specifications:**

Refer to SVI guidance on number/combination of cases required based on phenotype specificity. For most cardiomyopathies, it is recommended to default to "phenotype consistent with gene but not highly specific". Clinical judgment is required for shifting to a higher or lower phenotypic consistency.

See [PS2](#ps2---de-novo-confirmed) for the point-based system and additional considerations.

**Modification Type:** Disease-specific

---

### PP1 - Co-segregation

**Original ACMG Summary:** Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease. Note: May be used as stronger evidence with increasing segregation data.

**VCEP Specifications:**

| Strength | Segregation Threshold (Conservative) | Highly Specific Phenotype (Jarvik & Browning 2016) |
|----------|---------------------------------------|----------------------------------------------------|
| **Strong** | ≥7 segregations (LOD 2.1) | ≥5 segregations (LOD 1.5) |
| **Moderate** | ≥5 segregations (LOD 1.5) | ≥4 segregations (LOD 1.2) |
| **Supporting** | ≥3 segregations (LOD 0.9) | ≥3 segregations (LOD 0.9) |

**Counting Segregations:**
- Only genotype positive/phenotype positive individuals are counted as segregations, which can include affected obligate carriers
- Genotype positive/phenotype negative individuals are generally less informative for cardiomyopathy genes due to variable age at onset and reduced penetrance
- Phenotypes should be clinically confirmed, whenever possible, and should not include individuals with a suspected diagnosis

**Important Considerations:**
1. Segregation of a variant within a single family or haplotype has the potential to represent linkage disequilibrium with another undetected variant. If linkage disequilibrium is a concern, consider downgrading strength of segregation.
2. Use of segregation criteria should be carefully evaluated if variant frequency meets criteria for BS1.
3. Caution is needed when counting segregations in presence of other possible disease-causing variants, as both variants may be contributing to the phenotype.
4. Caution is needed when distantly related (≥3rd degree) affected individuals are connected by unknown or unaffected relatives (raises possibility of multiple causes of disease).

**Note:** Although rare for inherited cardiomyopathies, when the phenotype/presentation of a variant within and across families is highly specific (e.g., early-onset severe RCM in all affected individuals), the lower Jarvik and Browning thresholds can be considered.

**Modification Type:** Disease-specific

---

### PP2 - Missense in Constrained Gene

**Original ACMG Summary:** Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.

**VCEP Specification (Supporting):**

Application of this rule takes into consideration empirical data quantifying levels of rare missense variant enrichment in HCM referral cohorts compared to population-based cohorts (Walsh *et al.* 2019, PMID:30696458) rather than the missense constraint score in gnomAD.

On the basis of data from Walsh *et al.* 2019, **PP2 is currently only applicable to TPM1 for HCM** (transcripts ENST00000403994 and NM_001018005.2).

**Important Notes:**
- Data from HCM case cohorts was used to derive these cluster regions. Therefore, this rule should **NOT** be applied when additional evidence for the variant supports that the variant causes a phenotype other than HCM (e.g., variant seen in multiple DCM cases).
- Enrichment was not observed for DCM in any genes.

**Modification Type:** Disease-specific, Gene-specific

---

### PP3 - Computational Evidence

**Original ACMG Summary:** Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.). Caveat: As many *in silico* algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.

**VCEP Specification (Supporting):**

- As many *in silico* algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. Meta-predictors, such as REVEL, are preferred over multiple individual predictors.
- Use of **REVEL** (Ioannidis *et al.* 2016) is recommended at thresholds of **≥0.70 for PP3**
- Clinical judgment is needed if any individual algorithms or conservation data are contradictory to REVEL data
- Positive predictive value for benign/no impact predictions is generally higher than for pathogenic/impact predictions
- **SpliceAI** is recommended for evaluation of predicted splice impacts

**Modification Type:** Disease-specific

---

### PP4 - Phenotype Specificity

**Original ACMG Summary:** Patient's phenotype or family history is highly specific for a disease with a single genetic etiology.

**VCEP Specification:** ***Not Applicable***

**Comments:** Inherited cardiomyopathies have high locus heterogeneity as well as non-genetic etiologies.

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

Allele frequency is **≥0.001** based on the **filtering allele frequency (FAF)** in **gnomAD** in the subpopulation with the highest frequency (popmax).

**Additional Specifications:**
- The values used to calculate the BA1 threshold were derived from studies in Northern European populations that have been relatively well-characterized with regards to disease prevalence and variant spectrum. These thresholds can be applied to any population where disease prevalence is considered comparable (1/300 or lower).
- The threshold is applicable when assessing variants in the context of autosomal dominant cardiomyopathy.
- gnomAD is the preferred database for this calculation. If a subpopulation specific FAF other than the popmax is needed, this value can be calculated using the AlleleFrequencyApp on the CardioDB website:
  1. Using the Inverse AF tab, enter in the population size and the number of alleles identified and it will calculate the FAF
  2. Set confidence to 0.95 (95%)
  3. If the FAF is ≥0.001, this rule can be applied
- The FAF by platform (e.g., exome vs. genome; v.2.1.1 vs. v.3.1.1) should be considered; the larger population is most likely to have the most accurate representation of "true" population allele frequency
- Caution is needed when considering any population cohorts that are smaller than the smallest subpopulations within gnomAD v.2.1.1 (e.g., ~5,000 individuals or ~10,000 alleles). Despite the conservative nature of this threshold and approach, in smaller cohorts, the observed allele frequency may less accurately reflect the true allele frequency.

**Modification Type:** Disease-specific

---

### BS1 - Frequency Greater Than Expected

**Original ACMG Summary:** Allele frequency is greater than expected for disorder.

**VCEP Specification (Strong):**

Allele frequency is **≥0.0001** for TPM1 based on the **filtering allele frequency (FAF)** in **gnomAD** in the subpopulation with the highest frequency (popmax).

- Criterion BS1 may only be used as standalone evidence to classify a variant as Likely Benign in the absence of conflicting data. See SVI guidance (Tavtigian *et al.* 2018; Tavtigian *et al.* 2020).
- See BA1 for additional specifications that also apply to BS1.

**Modification Type:** Disease-specific, Gene-specific

---

### BS2 - Observed in Healthy Adult

**Original ACMG Summary:** Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

**VCEP Specification:** ***Not Applicable***

**Comments:** Inherited cardiomyopathies generally display reduced penetrance, variable expressivity, and adult-onset.

---

### BS3 - Functional Studies (No Effect)

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

**VCEP Specifications:**

Evaluation of studies/assays is required prior to application of functional evidence at any strength. Refer to SVI guidance for functional evidence (Brnich *et al.* 2020). In the context of cardiomyopathy, very few functional assays currently meet criteria sufficient for application of this rule at a STRONG level.

| Strength | Criteria |
|----------|----------|
| **Strong** | See PS3 specifications (in vitro splicing assays showing no effect) |
| **Moderate** | See PS3 specifications (in vivo models showing no effect) |
| **Supporting** | See PS3 specifications (in vitro assays showing no effect) |

**Modification Type:** Disease-specific

---

### BS4 - Lack of Segregation

**Original ACMG Summary:** Lack of segregation in affected members of a family. Caveat: The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.

**VCEP Specification (Strong):**

Any non-segregations should be carefully evaluated to rule out a phenocopy or the presence of a second disease-causing variant before considering it as conflicting or benign evidence.

1. The presence of "phenocopies" (e.g., athlete's heart, hypertensive heart disease, ischemic cardiomyopathy, alcoholic cardiomyopathy, diabetic cardiomyopathy) can mimic non-segregation (i.e., lack of segregation) among affected individuals.
2. Families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent 'non-segregation'.

Because of these possibilities, **multiple (≥2) non-segregations** that are highly unlikely to be phenocopies or due to alternate variants (e.g., those without a possible alternate cause) **are required to apply this rule**. A higher number of non-segregations is necessary for instances where alternative causes are possible (e.g., non-segregation in a sibling with childhood onset cardiomyopathy versus a grandparent with hypertension and HCM).

Careful consideration of the above points is required when using this data as conflicting evidence, especially when overall evidence supports likely pathogenic or pathogenic.

**Modification Type:** Disease-specific

---

### BP1-BP7 - Benign Supporting

| Criterion | Status | Comment |
|-----------|--------|---------|
| **BP1** | Not Applicable | For the current genes where null variants are a known mechanism, pathogenic missense variants have also been reported. |
| **BP2** | Supporting | Other variants must be pathogenic as defined by these specifications. Testing of parents or other informative relatives is often required to determine *cis/trans* status. If a variant is seen in *trans* (or as double heterozygous) with another pathogenic variant in ≥2 cases and the phenotype is not more severe, this rule may be applied. <1% of cases of HCM have >1 P/LP variant (0.6%; Alfares *et al.* 2015). Cannot be applied when variant has only been observed in *cis* with a pathogenic variant. Caution is needed if using as primary evidence for LB/B classification. |
| **BP3** | Not Applicable | Not applicable to the current genes. |
| **BP4** | Supporting | Use of **REVEL** (Ioannidis *et al.* 2016) is recommended at thresholds of **≤0.40 for BP4**. Meta-predictors preferred over multiple individual predictors. Clinical judgment needed if individual algorithms or conservation data are contradictory to REVEL data. **SpliceAI** recommended for evaluation of predicted splice impacts. |
| **BP5** | Not Applicable | Co-occurrence with an established P/LP variant for a non-cardiomyopathy related disease does not reduce the likelihood that a variant is independently disease-causing for cardiomyopathy. |
| **BP6** | Not Applicable | This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PMID: 29543229). |
| **BP7** | Supporting | Also applicable to **intronic variants outside the splice consensus sequence (-4 and +7 outward)** for which splicing prediction algorithms predict no impact to the splice consensus sequence NOR the creation of a new splice site AND the nucleotide is not highly conserved. Rule can be combined with BP4 to make a variant Likely Benign per Richards *et al.* 2015. |

---

## Rules for Combining Criteria

### Pathogenic Classification

| Criteria Combination |
|---------------------|
| ≥2 Strong *(PS1, PS2, PS3, PS4, PP1_Strong)* |
| 1 Strong *(PS1, PS2, PS3, PS4, PP1_Strong)* **AND** ≥3 Moderate *(PS3_Moderate, PS4_Moderate, PM4, PM5, PM6, PP1_Moderate)* |
| 1 Strong *(PS1, PS2, PS3, PS4, PP1_Strong)* **AND** 2 Moderate *(PS3_Moderate, PS4_Moderate, PM4, PM5, PM6, PP1_Moderate)* **AND** ≥2 Supporting *(PS3_Supporting, PS4_Supporting, PM2_Supporting, PM5_Supporting, PP1, PP2, PP3)* |
| 1 Strong *(PS1, PS2, PS3, PS4, PP1_Strong)* **AND** 1 Moderate *(PS3_Moderate, PS4_Moderate, PM4, PM5, PM6, PP1_Moderate)* **AND** ≥4 Supporting *(PS3_Supporting, PS4_Supporting, PM2_Supporting, PM5_Supporting, PP1, PP2, PP3)* |

### Likely Pathogenic Classification

| Criteria Combination |
|---------------------|
| 1 Strong *(PS1, PS2, PS3, PS4, PP1_Strong)* **AND** 1 Moderate *(PS3_Moderate, PS4_Moderate, PM4, PM5, PM6, PP1_Moderate)* |
| 1 Strong *(PS1, PS2, PS3, PS4, PP1_Strong)* **AND** ≥2 Supporting *(PS3_Supporting, PS4_Supporting, PM2_Supporting, PM5_Supporting, PP1, PP2, PP3)* |
| ≥3 Moderate *(PS3_Moderate, PS4_Moderate, PM4, PM5, PM6, PP1_Moderate)* |
| 2 Moderate *(PS3_Moderate, PS4_Moderate, PM4, PM5, PM6, PP1_Moderate)* **AND** ≥2 Supporting *(PS3_Supporting, PS4_Supporting, PM2_Supporting, PM5_Supporting, PP1, PP2, PP3)* |
| 1 Moderate *(PS3_Moderate, PS4_Moderate, PM4, PM5, PM6, PP1_Moderate)* **AND** ≥4 Supporting *(PS3_Supporting, PS4_Supporting, PM2_Supporting, PM5_Supporting, PP1, PP2, PP3)* |
| 1 Strong *(PS1, PS2, PS3, PS4, PP1_Strong)* **AND** 2 Moderate *(PS3_Moderate, PS4_Moderate, PM4, PM5, PM6, PP1_Moderate)* |

### Benign Classification

| Criteria Combination |
|---------------------|
| ≥2 Strong *(BS1, BS3, BS4)* |
| 1 Stand Alone *(BA1)* |

### Likely Benign Classification

| Criteria Combination |
|---------------------|
| 1 Strong *(BS1, BS3, BS4)* **AND** 1 Supporting *(BS3_Supporting, BP2, BP4, BP7)* |
| ≥2 Supporting *(BS3_Supporting, BP2, BP4, BP7)* |

---

## Appendices

### Appendix A: Criteria Applicability Summary for TPM1

| Criterion | Applicability | Max Strength | Modification Type |
|-----------|--------------|--------------|-------------------|
| PVS1 | Not Applicable | — | — |
| PS1 | Applicable | Strong | No change |
| PS2 | Applicable | Very Strong (point-based) | Disease-specific |
| PS3 | Applicable | Strong (splicing assays) | Disease-specific |
| PS4 | Applicable | Strong (OR-based) | Disease-specific |
| PM1 | Not Applicable | — | — |
| PM2 | Applicable | Supporting only | Disease-specific |
| PM3 | Not Applicable | — | — |
| PM4 | Applicable | Moderate | General recommendation |
| PM5 | Applicable | Moderate | General recommendation |
| PM6 | Applicable | See PS2 point system | Disease-specific |
| PP1 | Applicable | Strong | Disease-specific |
| PP2 | Applicable (HCM only) | Supporting | Disease-specific, Gene-specific |
| PP3 | Applicable | Supporting | Disease-specific |
| PP4 | Not Applicable | — | — |
| PP5 | Not Applicable | — | — |
| BA1 | Applicable | Stand Alone | Disease-specific |
| BS1 | Applicable | Strong | Disease-specific, Gene-specific |
| BS2 | Not Applicable | — | — |
| BS3 | Applicable | Strong (see PS3) | Disease-specific |
| BS4 | Applicable | Strong | Disease-specific |
| BP1 | Not Applicable | — | — |
| BP2 | Applicable | Supporting | Disease-specific |
| BP3 | Not Applicable | — | — |
| BP4 | Applicable | Supporting | Disease-specific |
| BP5 | Not Applicable | — | — |
| BP6 | Not Applicable | — | — |
| BP7 | Applicable | Supporting | General recommendation |

### Appendix B: Population Frequency Thresholds Summary

| Criterion | Threshold | Database | Strength |
|-----------|-----------|----------|----------|
| BA1 | FAF ≥0.001 (popmax) | gnomAD | Stand Alone |
| BS1 | FAF ≥0.0001 (popmax) | gnomAD | Strong |
| PM2 | Upper bound 95% CI ≤0.00004 (popmax) | gnomAD | Supporting |

### Appendix C: Computational Predictor Thresholds

| Criterion | Tool | Threshold | Direction |
|-----------|------|-----------|-----------|
| PP3 | REVEL | ≥0.70 | Pathogenic (Supporting) |
| BP4 | REVEL | ≤0.40 | Benign (Supporting) |
| PP3/BP4 | SpliceAI | Per tool recommendations | Splice impact evaluation |

### Appendix D: Reference PMIDs

| # | Citation | PMID |
|---|----------|------|
| 1 | Richards S, Aziz N *et al.* Standards and guidelines for the interpretation of sequence variants. *Genet Med* (2015) 17(5):405-24. | 25741868 |
| 2 | ClinGen SVI Working Group | — |
| 3 | Abou Tayoun AN, Pesaran T *et al.* Recommendations for interpreting the loss of function PVS1 ACMG/AMP variant criterion. *Hum Mutat* (2018) 39(11):1517-1524. | 30192042 |
| 4 | Brnich SE, Abou Tayoun AN *et al.* Recommendations for application of the functional evidence PS3/BS3 criterion. *Genome Med* (2019) 12(1):3. | 31892348 |
| 5 | Walsh R, Thomson KL *et al.* Reassessment of Mendelian gene pathogenicity using 7,855 cardiomyopathy cases and 60,706 reference samples. *Genet Med* (2017) 19(2):192-203. | 27532257 |
| 6 | Anderson RH, Jensen B *et al.* Key Questions Relating to Left Ventricular Noncompaction Cardiomyopathy. *Can J Cardiol* (2017) 33(6):747-757. | 28395867 |
| 7 | Oechslin E, Jenni R. Nosology of Noncompaction Cardiomyopathy. *Can J Cardiol* (2017) 33(6):701-704. | 28545618 |
| 8 | Hershberger RE, Morales A *et al.* Is Left Ventricular Noncompaction a Trait, Phenotype, or Disease? *Circ Cardiovasc Genet* (2017) 10(6). | 29212902 |
| 9 | Ross SB, Jones K *et al.* A systematic review and meta-analysis of the prevalence of left ventricular non-compaction in adults. *Eur Heart J* (2020) 41(14):1428-1436. | 31143950 |
| 10 | Kelly MA, Caleshu C *et al.* Adaptation and validation of the ACMG/AMP variant classification framework for MYH7-associated inherited cardiomyopathies. *Genet Med* (2018) 20(3):351-359. | 29300372 |
| 11 | Jarvik GP, Browning BL. Consideration of Cosegregation in the Pathogenicity Classification of Genomic Variants. *Am J Hum Genet* (2016) 98(6):1077-1081. | 27236918 |
| 12 | Walsh R, Mazzarotto F *et al.* Quantitative approaches to variant classification increase the yield and precision of genetic testing in Mendelian diseases: the case of hypertrophic cardiomyopathy. *Genome Med* (2019) 11(1):5. | 30696458 |
| 13 | Ioannidis NM, Rothstein JH *et al.* REVEL: An Ensemble Method for Predicting the Pathogenicity of Rare Missense Variants. *Am J Hum Genet* (2016) 99(4):877-885. | 27666373 |
| 14 | Jaganathan K, Kyriazopoulou Panagiotopoulou S *et al.* Predicting Splicing from Primary Sequence with Deep Learning. *Cell* (2019) 176(3):535-548.e24. | 30661751 |
| 15 | Tavtigian SV, Greenblatt MS *et al.* Modeling the ACMG/AMP variant classification guidelines as a Bayesian classification framework. *Genet Med* (2018) 20(9):1054-1060. | 29300386 |
| 16 | Tavtigian SV, Harrison SM *et al.* Fitting a naturally scaled point system to the ACMG/AMP variant classification guidelines. *Hum Mutat* (2020) 41(10):1734-1737. | 32720330 |
| 17 | Alfares AA, Kelly MA *et al.* Results of clinical genetic testing of 2,912 probands with hypertrophic cardiomyopathy. *Genet Med* (2015) 17(11):880-8. | 25611685 |

---

## Version History

| Version | Date | Notes |
|---------|------|-------|
| 1.0.0 | 4/22/2024 | Initial release. PS4 calculator link added. |

---

*This document was compiled from ClinGen Cardiomyopathy VCEP specifications for TPM1 and ClinGen SVI recommendations. For the most current version, please refer to the [ClinGen website](https://clinicalgenome.org).*
