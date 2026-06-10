# ClinGen Cardiomyopathy Expert Panel Variant Interpretation Guidelines for MYBPC3

**Version:** 1.0.0
**Released:** 4/22/2024
**Affiliation:** Cardiomyopathy VCEP
**Based on:** Richards et al., 2015 ACMG/AMP Guidelines

---

## Gene Information

| Attribute | Value |
|-----------|-------|
| **Gene** | MYBPC3 (HGNC:7551) |
| **HGNC Name** | myosin binding protein C3 |
| **Transcript** | NM_000256.3 |
| **Disease** | Hypertrophic cardiomyopathy (MONDO:0005045) |
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

**VCEP Specifications:**

Currently only applicable to *MYBPC3* where LOF is an established disease mechanism. Refer to SVI guidance for the interpretation of this criterion (Abou Tayoun *et al.* 2018). SpliceAI is recommended for evaluation of predicted splice impacts.

**Modification Type:** Gene-specific

#### Key Considerations for MYBPC3

1. **NMD Escape Region:** Codon p.1254 is located 50 nucleotides upstream of the most 3' exon-exon junction (exon 33:34) in MYBPC3. Nonsense variants introducing a premature termination codon after this point may escape nonsense mediated decay (NMD) and consequently not result in protein haploinsufficiency.

2. **Micro-exons:** When assessing variants predicted to affect splicing of micro-exons (exons 10, 11, and 14), be aware that *in silico* splice site predictions may be less reliable in this setting and the consequences of variants affecting splice sites at these exons less predictable.

3. **In-frame exons:** When assessing variants affecting splice sites of in-frame exons (exons 2-4, 8-11, 14, 20, 22, 24-27), be aware that although most of these exons encode domains that have been shown to play critical roles in protein function, and/or harbor functionally important residues, in general, the consequences of in-frame deletions are less predictable.

#### PVS1 Strength Levels by Variant Type

##### Nonsense or Frameshift Variants

| Scenario | Strength |
|----------|----------|
| Predicted to undergo NMD (prior to p.1254), exon present in biologically-relevant transcript(s) | **PVS1** |
| Not predicted to undergo NMD (after p.1254), truncated/altered region is critical to protein function | **PVS1_Strong** |
| Not predicted to undergo NMD (after p.1254), role of region unknown, LoF variants not frequent in general population, exon present in biologically-relevant transcript(s), variant removes <10% of protein | **PVS1_Moderate** |

##### Canonical Splice Site Variants (GT--AG ±1,2)

| Scenario | Strength |
|----------|----------|
| Exon skipping or use of cryptic splice site disrupts reading frame and is predicted to undergo NMD, exon present in biologically-relevant transcript(s) | **PVS1** |
| Exon skipping or use of cryptic splice site disrupts reading frame and is NOT predicted to undergo NMD, truncated/altered region is critical to protein function | **PVS1_Strong** |
| Exon skipping or use of cryptic splice site disrupts reading frame and is NOT predicted to undergo NMD, role of region unknown, LoF variants not frequent, exon present in biologically-relevant transcript(s), variant removes >10% of protein | **PVS1_Strong** |
| Exon skipping or use of cryptic splice site disrupts reading frame and is NOT predicted to undergo NMD, role of region unknown, LoF variants not frequent, exon present in biologically-relevant transcript(s), variant removes <10% of protein | **PVS1_Moderate** |
| Exon skipping or use of cryptic splice site preserves reading frame (exons 2-4, 8-11, 14, 20, 22, 24-27), truncated/altered region is critical to protein function | **PVS1_Strong** |

##### Deletion Variants (Single Exon to Full Gene)

| Scenario | Strength |
|----------|----------|
| Full gene deletion | **PVS1** |
| Single to multi exon deletion – disrupts reading frame and predicted to undergo NMD, exon present in biologically-relevant transcript(s) | **PVS1** |
| Single to multi exon deletion – disrupts reading frame and NOT predicted to undergo NMD, truncated/altered region is critical to protein function | **PVS1_Strong** |
| Single to multi exon deletion – disrupts reading frame and NOT predicted to undergo NMD, role of region unknown, LoF variants not frequent, exon present in biologically-relevant transcript(s), variant removes >10% of protein | **PVS1_Strong** |
| Single to multi exon deletion – disrupts reading frame and NOT predicted to undergo NMD, role of region unknown, LoF variants not frequent, exon present in biologically-relevant transcript(s), variant removes <10% of protein | **PVS1_Moderate** |
| Single to multi exon deletion – preserves reading frame, truncated/altered region is critical to protein function | **PVS1_Strong** |

##### Duplication Variants (≥1 exon, completely contained within gene)

| Scenario | Strength |
|----------|----------|
| Proven in tandem, reading frame disrupted and NMD predicted to occur | **PVS1** |
| Proven in tandem, no or unknown impact on reading frame and NMD | **N/A** |
| Presumed in tandem, reading frame presumed disrupted and NMD predicted to occur | **PVS1_Strong** |
| Proven not in tandem | **N/A** |

##### Initiation Codon Variants

| Scenario | Strength |
|----------|----------|
| No known alternative start codon in other transcripts, ≥1 pathogenic variant(s) upstream of closest potential in-frame start codon (p.103) | **PVS1_Moderate** |
| No known alternative start codon in other transcripts, no pathogenic variant(s) upstream of closest potential in-frame start codon | **PVS1_Supporting** |

**Note:** Investigations are ongoing to definitively establish the regions/domains of MYBPC3 that are critical to protein function and therefore have not been pre-defined. Functional and genetic evidence should be evaluated periodically for most accurate application of this rule.

---

### PS1 - Same Amino Acid Change

**Original ACMG Summary:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.

**Example:** Val->Leu caused by either G>C or G>T in the same codon.

**Caveat:** Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | No cardiomyopathy specifications. Apply as outlined by Richards *et al.* 2015. |

**Example of when rule should NOT be applied:** NM_000256.3(MYBPC3): c.2308G>A (p.Asp770Asn) has an established impact on splicing leading to nonsense mediated decay (NMD) and should not be used to provide evidence for other variants observed to result in the same amino acid change.

For canonical splice site variants where other canonical splice variants have been reported, application of the PS1 rule may be considered if the other variant affecting the same splice site is:
1. Predicted to have a similar or more deleterious effect, AND
2. Has been classified as pathogenic according to these modified guidelines without use of PS1 for other splice variants

**Modification Type:** No change

---

### PS2 - De Novo (Confirmed)

**Original ACMG Summary:** De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.

**Note:** Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | Refer to SVI guidance on number/combination of cases required based on phenotype specificity. |

**Key Points:**
- For most cardiomyopathies, default to **"Phenotype consistent with gene but not highly specific"**
- Clinical judgment is required for shifting to a higher or lower category
- For use as a STRONG or VERY STRONG criterion, ideally parents have been thoroughly clinically evaluated without evidence of cardiomyopathy (ideally using a combination of ECG and echocardiogram or cardiac MRI for maximum sensitivity)

**Family History Consistent with De Novo Inheritance Should NOT Have:**
1. Sudden death under 60 years of age
2. Heart transplant
3. Implantable cardiac defibrillator (ICD) under 60 years of age
4. Features of cardiomyopathy (e.g., systolic dysfunction, hypertrophy, left ventricular enlargement in an individual without risk factors)
5. Other related/overlapping cardiomyopathies

**Examples of Non-suspicious Family History:** Non-specific clinical features (e.g., palpitations, syncope, borderline/inconclusive echocardiogram findings, heart attack if age appropriate and suspected to result from coronary artery disease), but every attempt should be made to clarify features.

**Important:** This criterion is only applicable in the ABSENCE of any other possible disease-causing variants. If other pathogenic or likely pathogenic variants are present, consider decreasing points assigned or overall weight.

**Modification Type:** Disease-specific

---

### PS3 - Functional Studies

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.

**Note:** Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.

**VCEP Specifications:**

Evaluation of studies/assays is required prior to application of functional evidence at any strength. Refer to SVI guidance for functional evidence (Brnich *et al.* 2020).

In the context of cardiomyopathy, very few functional assays currently meet criteria sufficient for application of this rule at a STRONG level.

#### Strength Levels

| Strength | Assay Type | Criteria |
|----------|------------|----------|
| **Strong** | In vitro splicing assays (e.g., RNA studies) | See detailed criteria below |
| **Moderate** | In vivo models (e.g., variant knock-in animal models) | See detailed criteria below |
| **Supporting** | In vitro assays (e.g., biochemical assays of myofilament function, motility assays, human iPSC-CM) | See detailed criteria below |

#### PS3_Strong: In Vitro Splicing Assays

*In vitro* splicing assays may be considered as **STRONG** evidence, providing the following criteria are met:
- Prior knowledge of predominant transcripts in cardiac tissue
- Analysis undertaken using RNA extracted from cardiac tissue from the individual with the variant, OR
- Analysis undertaken using RNA extracted from whole blood providing the relevant transcripts (isoforms) are expressed in blood and are at sufficient levels to assess splice disruption
- Assay shows a clear, reproducible and convincing effect on splicing (i.e., a distinct splice product, present at a level comparable to the splice product from the wild-type allele), which is not observed in controls
- Confirmation of abnormal splice product by Sanger sequencing

**NOTE:** Mini-gene assay in non-patient derived cell lines are NOT considered to provide STRONG evidence.

**NOTE:** Whether to activate this rule needs to be reconciled with the variant spectrum and disease mechanism for the gene at hand (i.e., consider whether the effect is likely to lead to LOF or an in-frame alteration and whether this type of effect is expected to be disease causing).

#### PS3_Moderate: In Vivo Models

Mammalian variant-specific knock-in animal models that produce a phenotype consistent with the clinical phenotype in humans (e.g., structural and/or functional cardiac abnormalities, premature death, arrhythmia) may be considered as **MODERATE** evidence.

**The following assays/models do NOT meet criteria:**
1. Assays that are known to be associated with non-specific cardiac phenotypes (e.g., morpholino-induced pericardial edema in zebrafish)
2. In vivo evidence that is not variant specific, such as whole gene alterations (i.e., cDNA or whole gene transgenic mice and whole or partial gene knock-out mice)

#### PS3_Supporting: In Vitro Assays

While some *in vitro* assays may provide evidence that a variant in a cardiomyopathy gene has an effect on protein and/or myofilament function, at present, there are no validated "gold-standard" assays that are considered to reliably predict the clinical phenotype.

As such, data from individual *in vitro* studies are unlikely to meet the criteria required to assign this rule at more than **SUPPORTING** level.

**Modification Type:** Disease-specific

---

### PS4 - Prevalence in Affected

**Original ACMG Summary:** The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.

**Note 1:** Relative risk (RR) or odds ratio (OR), as obtained from case-control studies, is >5.0 and the confidence interval around the estimate of RR or OR does not include 1.0.

**Note 2:** In instances of very rare variants where case-control studies may not reach statistical significance, the prior observation of the variant in multiple unrelated patients with the same phenotype, and its absence in controls, may be used as moderate level of evidence.

**VCEP Specifications:**

Currently few well-designed case-control studies have been performed for inherited cardiomyopathies. Until such studies become available, comparative analyses can be undertaken using case data (e.g., internal and/or published cohorts) and control data from population-level cohorts (e.g., gnomAD).

#### Cohort Criteria

1. Cases have a clinical diagnosis of the specified disorder or related phenotype (e.g., all cases have HCM or another relevant phenotype)
   - Consider how likely another potential cause of the phenotype has been excluded
   - Consider the presence of other variants in relevant genes
   - Consider the extent of testing performed
2. Controls should not be derived from study populations that might be enriched for the specified disorder
3. Denominator of the cohorts must be available
4. Cohorts do not include closely related individuals (i.e., family members are not included in the case counts)
5. Cohorts do not overlap with other cohorts being used in the analysis
6. Population diversity of the case and control cohorts are broadly similar
7. Consider the size of the case cohort — larger cohorts provide more accurate estimates

#### Strength Thresholds (Based on Lower Bound of 95% CI of Odds Ratio)

| Strength | OR Lower 95% CI Threshold |
|----------|---------------------------|
| **Strong** | ≥20 |
| **Moderate** | ≥10 |
| **Supporting** | ≥5 |

**PS4 Calculator:** Available at www.cardiodb.org

**Note:** If multiple cohorts are available, the final ORs and associated CIs need to be harmonized across all cohorts to determine the final level.

#### Relevant Phenotypes

1. Cases of HCM and RCM may be combined as they are considered part of the same disease spectrum
2. Combination of probands with other phenotypes should be reviewed by a clinical expert
3. **LVNC Considerations:** Due to the current debate about whether isolated LVNC represents a true disease entity or variation of typical cardiac morphology, individuals with isolated LVNC should NOT be added to proband or segregation counts
4. **HCM/DCM Considerations:** HCM and DCM have distinct mechanisms of disease and therefore pathogenetic variants are not anticipated to cause both primary phenotypes. End-stage HCM can present similarly to DCM, so careful consideration is needed before including DCM or related phenotypes.

**Modification Type:** Disease-specific

---

### PM1 - Mutational Hot Spot

**Original ACMG Summary:** Located in a mutational hot spot and/or critical and well-established functional domain (e.g., active site of an enzyme) without benign variation.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Moderate** | Applicable to missense variants in MYBPC3 in the specific regions listed below |

**Cluster Regions (Walsh *et al.* 2019):**
- Transcripts: ENST00000545968 and NM_000256.3
- **Codons 485-502**
- **Codons 1248-1266**

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

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Supporting** | gnomAD popmax filtering allele frequency upper bound of 95% CI **≤0.00004** |

**Threshold Equivalents:**
- Variant NOT being observed more than once (≤1 allele) in gnomAD v.2.1.1 in one of the non-founder populations (absence required from the Other and Ashkenazi Jewish subpopulations)
- Variant being seen in a single subpopulation meeting:
  - AC ≤1 in AN ≥120,000
  - AC ≤2 in AN ≥160,000
  - AC ≤3 in AN ≥195,000
  - AC ≤4 in AN ≥230,000

**Notes:**
- gnomAD is the preferred database for this calculation
- Confidence interval tools, such as Confit-de-MAF, can be used to determine the upper bound of the 95% CI
- Due to technical limitations of NGS, minor allele frequencies for complex variants (e.g., large indels) may not be accurately represented
- Caution should be used when a variant is only identified, or over-represented, in one of the smaller gnomAD populations
- Population databases may contain affected or pre-symptomatic individuals for diseases with reduced penetrance/variable onset

**Modification Type:** Disease-specific

---

### PM3 - In Trans with Pathogenic

**Original ACMG Summary:** For recessive disorders, detected in trans with a pathogenic variant.

**Note:** This requires testing of parents (or offspring) to determine phase.

**VCEP Specifications:**

| Status | Comment |
|--------|---------|
| **Not Applicable** | While compound heterozygosity leading to a more severe phenotype has been documented, this rule was designed for traditional recessive inheritance. It is acknowledged that there is increasing evidence supporting that some of these genes/variants may also be recessive (e.g., MYL2, MYL3), but addressing those edge cases was outside the scope of this current guideline. |

---

### PM4 - Protein Length Changes

**Original ACMG Summary:** Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Moderate** | Default strength; carefully consider predicted impact |
| **Supporting** | May require downgrading based on size, location, and conservation of region |

**Notes:**
- Strength of rule should be carefully considered and may require downgrading to SUPPORTING based on the predicted impact of the variant, including the size of the deletion/insertion, its location, and conservation of the region
- For genes where PVS1 is not applicable (i.e., where there is no evidence that pLOF variants cause disease), consider using this rule at MODERATE or SUPPORTING strength for truncating variants that do NOT undergo nonsense mediated decay (NMD)

**Modification Type:** General recommendation

---

### PM5 - Novel Missense at Same Residue

**Original ACMG Summary:** Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.

**Example:** Arg156His is pathogenic; now you observe Arg156Cys.

**Caveat:** Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Moderate** | A different missense variant at the same codon has been classified as **pathogenic** using these modified guidelines without application of PM5 |
| **Supporting** | A different missense variant at the same codon has been classified as **likely pathogenic** using these modified guidelines without application of PM5 |

**Notes:**
- The impact of the amino acid change being evaluated needs to be compared to the impact of the amino acid change that is established as pathogenic/likely pathogenic
- Consider reducing the strength if the predicted impact is not expected to be equivalent or more severe
- **PM5 should not be combined with PM1.** If both are applicable at MODERATE weight, use of PM5 is most appropriate since it is variant specific. If both applicable at different strengths, apply the one with higher strength.

**Modification Type:** General recommendation

---

### PM6 - De Novo (Assumed)

**Original ACMG Summary:** Assumed de novo, but without confirmation of paternity and maternity.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Moderate** | Refer to SVI guidance on number/combination of cases required based on phenotype specificity |

- For most cardiomyopathies, default to "phenotype consistent with gene but not highly specific"
- Clinical judgment is required for shifting to a higher or lower phenotypic consistency
- See PS2 for additional considerations

**Modification Type:** Disease-specific

---

### PP1 - Co-segregation

**Original ACMG Summary:** Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.

**Note:** May be used as stronger evidence with increasing segregation data.

**VCEP Specifications:**

Due to the genotypic and phenotypic heterogeneity of inherited cardiomyopathies, segregation thresholds have been conservatively set.

#### Standard Thresholds

| Strength | Segregations Required | LOD Score |
|----------|----------------------|-----------|
| **Strong** | ≥7 | 2.1 |
| **Moderate** | ≥5 | 1.5 |
| **Supporting** | ≥3 | 0.9 |

#### When Phenotype is Highly Specific (e.g., early-onset severe RCM in all affected individuals)

| Strength | Segregations Required | LOD Score |
|----------|----------------------|-----------|
| **Strong** | ≥5 | 1.5 |
| **Moderate** | ≥4 | 1.2 |
| **Supporting** | ≥3 | 0.9 |

**Counting Segregations:**
- Only genotype positive/phenotype positive individuals are counted as segregations
- Can include affected obligate carriers
- Genotype positive/phenotype negative individuals are generally less informative due to variable age at onset and reduced penetrance
- Phenotypes should be clinically confirmed, whenever possible, and should not include individuals with a suspected diagnosis

**Important Considerations:**
1. Segregation within a single family or haplotype has the potential to represent linkage disequilibrium with another undetected variant. If linkage disequilibrium is a concern, consider downgrading strength.
2. Use of segregation criteria should be carefully evaluated if variant frequency meets criteria for BS1.
3. Caution is needed when counting segregations in presence of other possible disease-causing variants, as both variants may be contributing to the phenotype.
4. Caution is needed when distantly related (≥3rd degree) affected individuals are connected by unknown or unaffected relatives (raises possibility of multiple causes of disease).

**Modification Type:** Disease-specific

---

### PP2 - Missense in Constrained Gene

**Original ACMG Summary:** Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.

**VCEP Specifications:**

| Status | Comment |
|--------|---------|
| **Not Applicable** | Application of this rule takes into consideration empirical data quantifying levels of rare missense variant enrichment in HCM referral cohorts compared to population-based cohorts (Walsh *et al.* 2019 PMID:30696458) rather than the missense constraint score in gnomAD. For MYBPC3, there is evidence for regional enrichment of rare missense variants (see PM1 specifications). |

---

### PP3 - Computational Evidence

**Original ACMG Summary:** Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).

**Caveat:** As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Supporting** | REVEL score **≥0.70** |

**Notes:**
- As many *in silico* algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion
- Meta-predictors, such as REVEL, are preferred over multiple individual predictors
- Clinical judgment is needed if any individual algorithms or conservation data are contradictory to REVEL data
- Positive predictive value for benign/no impact predictions is generally higher than for pathogenic/impact predictions
- **SpliceAI** is recommended for evaluation of predicted splice impacts

**Modification Type:** Disease-specific

---

### PP4 - Phenotype Specificity

**Original ACMG Summary:** Patient's phenotype or family history is highly specific for a disease with a single genetic etiology.

**VCEP Specifications:**

| Status | Comment |
|--------|---------|
| **Not Applicable** | Inherited cardiomyopathies have high locus heterogeneity as well as non-genetic etiologies. |

---

### PP5 - Reputable Source

**Original ACMG Summary:** Reputable source recently reports variant as pathogenic, but the evidence is not available to the laboratory to perform an independent evaluation.

**VCEP Specifications:**

| Status | Comment |
|--------|---------|
| **Not Applicable** | This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee. (PMID: 29543229) |

---

## Benign Criteria

### BA1 - Allele Frequency >0.1%

**Original ACMG Summary:** Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Stand Alone** | gnomAD filtering allele frequency (FAF) **≥0.001** in the subpopulation with the highest frequency (popmax) |

**Notes:**
- The values used to calculate the BA1 threshold were derived from studies in Northern European populations that have been relatively well-characterized with regards to disease prevalence and variant spectrum
- These thresholds can be applied to any population where disease prevalence is considered comparable (1/300 or lower)
- The threshold is applicable when assessing variants in the context of autosomal dominant cardiomyopathy
- gnomAD is the preferred database for this calculation
- If a subpopulation specific FAF other than the popmax is needed, this value can be calculated using the AlleleFrequencyApp on the CardioDB website
- The FAF by platform (e.g., exome vs. genome; v.2.1.1 vs. v.3.1.1) should be considered
- Caution is needed when considering any population cohorts that are smaller than the smallest subpopulations within gnomAD v.2.1.1 (e.g., ~5000 individuals or ~10,000 alleles)

**Modification Type:** Disease-specific

---

### BS1 - Frequency Greater Than Expected

**Original ACMG Summary:** Allele frequency is greater than expected for disorder.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | gnomAD filtering allele frequency (FAF) **≥0.0002** in the subpopulation with the highest frequency (popmax) |

**Notes:**
- Criterion BS1 may only be used as standalone evidence to classify a variant as Likely Benign in the absence of conflicting data
- See SVI guidance (Tavtigian *et al.* 2018; Tavtigian *et al.* 2020)
- See BA1 for additional specifications that also apply to BS1

**Modification Type:** Disease-specific, Gene-specific

---

### BS2 - Observed in Healthy Adult

**Original ACMG Summary:** Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

**VCEP Specifications:**

| Status | Comment |
|--------|---------|
| **Not Applicable** | Inherited cardiomyopathies generally display reduced penetrance, variable expressivity, and adult-onset. |

---

### BS3 - Functional Studies (No Effect)

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

**VCEP Specifications:**

Evaluation of studies/assays is required prior to application of functional evidence at any strength. Refer to SVI guidance for functional evidence (Brnich *et al.* 2020).

| Strength | Criteria |
|----------|----------|
| **Strong** | See PS3 specifications |
| **Moderate** | See PS3 specifications |
| **Supporting** | See PS3 specifications |

**Modification Type:** Disease-specific

---

### BS4 - Lack of Segregation

**Original ACMG Summary:** Lack of segregation in affected members of a family.

**Caveat:** The presence of phenocopies for common phenotypes (i.e., cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | Multiple (≥2) non-segregations that are highly unlikely to be phenocopies or due to alternate variants |

**Important Considerations:**
1. The presence of "phenocopies" (e.g., athlete's heart, hypertensive heart disease, ischemic cardiomyopathy, alcoholic cardiomyopathy, diabetic cardiomyopathy) can mimic non-segregation among affected individuals
2. Families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent 'non-segregation'
3. A higher number of non-segregations is necessary for instances where alternative causes are possible (e.g., non-segregation in a sibling with childhood onset cardiomyopathy versus a grandparent with hypertension and HCM)
4. Careful consideration of the above points is required when using this data as conflicting evidence, especially when overall evidence supports likely pathogenic or pathogenic

**Modification Type:** Disease-specific

---

### BP1-BP7 - Benign Supporting

| Criterion | Status | Comment |
|-----------|--------|---------|
| **BP1** | Not Applicable | For the current genes where null variants are a known mechanism, pathogenic missense variants have also been reported. |
| **BP2** | Supporting | Other variants must be pathogenic as defined by these specifications. Testing of parents or other informative relatives is often required to determine cis/trans status. If a variant is seen in trans with another pathogenic variant in ≥2 cases and the phenotype is not more severe than when either variant is seen in isolation, this rule may be applied. <1% of cases of HCM have >1 pathogenic or likely pathogenic variant (0.6%; Alfares *et al.* 2015). This rule cannot be applied when the variant has only been observed in cis with a pathogenic variant. Caution is needed if using this criterion as a primary piece of evidence for classifying a variant as likely benign/benign. |
| **BP3** | Not Applicable | Not applicable to the current genes. |
| **BP4** | Supporting | Use of REVEL is recommended at thresholds of **≤0.40** for BP4. Meta-predictors, such as REVEL, are preferred over multiple individual predictors. Clinical judgment is needed if any individual algorithms or conservation data are contradictory to REVEL data. SpliceAI is recommended for evaluation of predicted splice impacts. |
| **BP5** | Not Applicable | Co-occurrence with an established pathogenic or likely pathogenic variant for a non-cardiomyopathy related disease does not reduce the likelihood that a variant is independently disease-causing for cardiomyopathy. |
| **BP6** | Not Applicable | This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee. (PMID: 29543229) |
| **BP7** | Supporting | Also applicable to intronic variants outside the splice consensus sequence (-4 and +7 outward) for which splicing prediction algorithms predict no impact to the splice consensus sequence NOR the creation of a new splice site AND the nucleotide is not highly conserved. Rule can be combined with BP4 to make a variant likely benign. |

---

## Rules for Combining Criteria

### Pathogenic Classification

| Criteria Combination |
|---------------------|
| 1 Very Strong (PVS1) **AND** ≥1 Strong (PS1, PS2, PS3, PS4, PP1_Strong) |
| 1 Very Strong (PVS1) **AND** ≥2 Moderate (PS3_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate) |
| 1 Very Strong (PVS1) **AND** 1 Moderate (PS3_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate) **AND** 1 Supporting (PS3_Supporting, PS4_Supporting, PM2_Supporting, PM5_Supporting, PP1, PP3) |
| 1 Very Strong (PVS1) **AND** ≥2 Supporting (PS3_Supporting, PS4_Supporting, PM2_Supporting, PM5_Supporting, PP1, PP3) |
| ≥2 Strong (PS1, PS2, PS3, PS4, PP1_Strong) |
| 1 Strong (PS1, PS2, PS3, PS4, PP1_Strong) **AND** ≥3 Moderate (PS3_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate) |
| 1 Strong (PS1, PS2, PS3, PS4, PP1_Strong) **AND** 2 Moderate (PS3_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate) **AND** ≥2 Supporting (PS3_Supporting, PS4_Supporting, PM2_Supporting, PM5_Supporting, PP1, PP3) |
| 1 Strong (PS1, PS2, PS3, PS4, PP1_Strong) **AND** 1 Moderate (PS3_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate) **AND** ≥4 Supporting (PS3_Supporting, PS4_Supporting, PM2_Supporting, PM5_Supporting, PP1, PP3) |

### Likely Pathogenic Classification

| Criteria Combination |
|---------------------|
| 1 Very Strong (PVS1) **AND** 1 Moderate (PS3_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate) |
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

### Appendix A: PVS1 Decision Tree

See the accompanying document: **CM-VCEP MYBPC3 PVS1 Decision Tree**

The decision tree provides guidance for determining PVS1 strength based on:
- Variant type (nonsense, frameshift, splice site, deletion, duplication, initiation codon)
- NMD prediction (predicted to undergo NMD vs. escape NMD)
- Impact on protein function
- Percentage of protein removed

### Appendix B: PS4 Calculator Examples

A PS4 calculator is available at **www.cardiodb.org**.

#### Example Calculations

**OR Thresholds (Lower Bound of 95% CI):**
- Supporting: ≥5
- Moderate: ≥10
- Strong: ≥20

**General Example (Variant A):**
- Clinical lab: 22 in 7,437 cases → OR 358 [95% CI: 48-2,655] = **STRONG**
- Literature: 13 in 9,162 cases → OR 171 [95% CI: 22-1,310] = **STRONG**

### Appendix C: Population Frequency Thresholds Summary

| Criterion | Threshold | Strength |
|-----------|-----------|----------|
| **BA1** | FAF ≥0.001 (gnomAD popmax) | Stand Alone |
| **BS1** | FAF ≥0.0002 (gnomAD popmax) | Strong |
| **PM2** | Upper 95% CI ≤0.00004 (gnomAD popmax) | Supporting |

### Appendix D: In Silico Prediction Thresholds

| Criterion | Tool | Threshold | Strength |
|-----------|------|-----------|----------|
| **PP3** | REVEL | ≥0.70 | Supporting |
| **BP4** | REVEL | ≤0.40 | Supporting |
| **Splice** | SpliceAI | Recommended for splice prediction evaluation | - |

### Appendix E: Segregation Thresholds

| Strength | Standard Thresholds | Highly Specific Phenotype |
|----------|---------------------|---------------------------|
| **Strong** | ≥7 segregations (LOD 2.1) | ≥5 segregations (LOD 1.5) |
| **Moderate** | ≥5 segregations (LOD 1.5) | ≥4 segregations (LOD 1.2) |
| **Supporting** | ≥3 segregations (LOD 0.9) | ≥3 segregations (LOD 0.9) |

### Appendix F: PM1 Cluster Regions

| Transcript | Cluster Region |
|------------|----------------|
| ENST00000545968 / NM_000256.3 | Codons 485-502 |
| ENST00000545968 / NM_000256.3 | Codons 1248-1266 |

---

## References

1. Abou Tayoun AN, Pesaran T, *et al.* Recommendations for interpreting the loss of function PVS1 ACMG/AMP variant criterion. **Hum Mutat** (2018) 39(11):1517-1524. PMID: 30192042

2. Jaganathan K, Kyriazopoulou Panagiotopoulou S, *et al.* Predicting Splicing from Primary Sequence with Deep Learning. **Cell** (2019) 176(3):535-548.e24. PMID: 30661751

3. Nagy E, Maquat LE. A rule for termination-codon position within intron-containing genes: when nonsense affects RNA abundance. **Trends Biochem Sci** (1998) 23(6):198-9. PMID: 9644970

4. Frank-Hansen R, Page SP, *et al.* Micro-exons of the cardiac myosin binding protein C gene: flanking introns contain a disproportionately large number of hypertrophic cardiomyopathy mutations. **Eur J Hum Genet** (2008) 16(9):1062-9. PMID: 18337725

5. Carrier L, Mearini G, *et al.* Cardiac myosin-binding protein C (MYBPC3) in cardiac pathophysiology. **Gene** (2015) 573(2):188-97. PMID: 26358504

6. Richards S, Aziz N, *et al.* Standards and guidelines for the interpretation of sequence variants: a joint consensus recommendation of the American College of Medical Genetics and Genomics and the Association for Molecular Pathology. **Genet Med** (2015) 17(5):405-24. PMID: 25741868

7. ClinGen Sequence Variant Interpretation Working Group: https://clinicalgenome.org/working-groups/sequence-variant-interpretation/

8. Brnich SE, Abou Tayoun AN, *et al.* Recommendations for application of the functional evidence PS3/BS3 criterion using the ACMG/AMP sequence variant interpretation framework. **Genome Med** (2019) 12(1):3. PMID: 31892348

9. Walsh R, Thomson KL, *et al.* Reassessment of Mendelian gene pathogenicity using 7,855 cardiomyopathy cases and 60,706 reference samples. **Genet Med** (2017) 19(2):192-203. PMID: 27532257

10. Anderson RH, Jensen B, *et al.* Key Questions Relating to Left Ventricular Noncompaction Cardiomyopathy: Is the Emperor Still Wearing Any Clothes? **Can J Cardiol** (2017) 33(6):747-757. PMID: 28395867

11. Oechslin E, Jenni R. Nosology of Noncompaction Cardiomyopathy: The Emperor Still Wears Clothes! **Can J Cardiol** (2017) 33(6):701-704. PMID: 28545618

12. Hershberger RE, Morales A, *et al.* Is Left Ventricular Noncompaction a Trait, Phenotype, or Disease? The Evidence Points to Phenotype. **Circ Cardiovasc Genet** (2017) 10(6). PMID: 29212902

13. Ross SB, Jones K, *et al.* A systematic review and meta-analysis of the prevalence of left ventricular non-compaction in adults. **Eur Heart J** (2020) 41(14):1428-1436. PMID: 31143950

14. Walsh R, Mazzarotto F, *et al.* Quantitative approaches to variant classification increase the yield and precision of genetic testing in Mendelian diseases: the case of hypertrophic cardiomyopathy. **Genome Med** (2019) 11(1):5. PMID: 30696458

15. Kelly MA, Caleshu C, *et al.* Adaptation and validation of the ACMG/AMP variant classification framework for MYH7-associated inherited cardiomyopathies: recommendations by ClinGen's Inherited Cardiomyopathy Expert Panel. **Genet Med** (2018) 20(3):351-359. PMID: 29300372

16. Jarvik GP, Browning BL. Consideration of Cosegregation in the Pathogenicity Classification of Genomic Variants. **Am J Hum Genet** (2016) 98(6):1077-1081. PMID: 27236918

17. Ioannidis NM, Rothstein JH, *et al.* REVEL: An Ensemble Method for Predicting the Pathogenicity of Rare Missense Variants. **Am J Hum Genet** (2016) 99(4):877-885. PMID: 27666373

18. Tavtigian SV, Greenblatt MS, *et al.* Modeling the ACMG/AMP variant classification guidelines as a Bayesian classification framework. **Genet Med** (2018) 20(9):1054-1060. PMID: 29300386

19. Tavtigian SV, Harrison SM, *et al.* Fitting a naturally scaled point system to the ACMG/AMP variant classification guidelines. **Hum Mutat** (2020) 41(10):1734-1737. PMID: 32720330

20. Alfares AA, Kelly MA, *et al.* Results of clinical genetic testing of 2,912 probands with hypertrophic cardiomyopathy: expanded panels offer limited additional sensitivity. **Genet Med** (2015) 17(11):880-8. PMID: 25611685

---

## Version History

| Version | Date | Notes |
|---------|------|-------|
| 1.0.0 | 4/22/2024 | Initial release. PVS1 flow chart added as a document. Link to PS4 calculator added. |

---

*This document was compiled from ClinGen VCEP specifications and ClinGen SVI recommendations. For the most current version, please refer to the ClinGen website.*
