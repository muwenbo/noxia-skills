# ClinGen Antibody Deficiencies Expert Panel Specifications to the ACMG/AMP Variant Interpretation Guidelines for PIK3CD

**Version:** 1.0.0
**Released:** December 16, 2025
**Affiliation:** Antibody Deficiencies VCEP
**Expert Panel:** [ClinGen Antibody Deficiencies](https://clinicalgenome.org/affiliation/50095/)
**Type:** Tavtigian et al., 2020 - Bayesian adaptation of Richards et al., 2015

---

## Table of Contents

1. [General Information](#1-general-information)
2. [Scope and Disease Mechanism](#2-scope-and-disease-mechanism)
3. [Pathogenic Criteria Specifications](#3-pathogenic-criteria-specifications)
4. [Benign Criteria Specifications](#4-benign-criteria-specifications)
5. [Phenotype Scoring Criteria](#5-phenotype-scoring-criteria)
6. [De Novo Occurrence Scoring](#6-de-novo-occurrence-scoring)
7. [Bayesian Point-Based Classification System](#7-bayesian-point-based-classification-system)
8. [Functional Assay Guidelines](#8-functional-assay-guidelines)
9. [Computational Predictors](#9-computational-predictors)
10. [References](#10-references)

---

## 1. General Information

### Gene Information

| Field | Value |
|-------|-------|
| **Gene** | PIK3CD (HGNC:8977) |
| **HGNC Name** | Phosphatidylinositol-4,5-bisphosphate 3-kinase catalytic subunit delta |
| **Canonical Transcript** | NM_005026.3 |
| **Disease** | Immunodeficiency 14 (MONDO:0014222) |
| **Mode of Inheritance** | Autosomal dominant |
| **Disease Mechanism** | Gain-of-function (GOF) |

### General Comments

The current specifications for PIK3CD variant curation are written in relation to **autosomal dominant** rather than autosomal recessive forms of disease, with a **gain-of-function** rather than loss-of-function mechanism of pathogenicity.

> **Important:** There is no a priori way to exclude one mode of inheritance or the other, so both need to be considered initially while assessing the variant. However, in general, only variants predicted to lead to a **single missense amino acid substitution** have thus far been shown to have a gain-of-function (GOF) effect in PIK3CD, so any other types of variants should not enter this classification criteria.

---

## 2. Scope and Disease Mechanism

### Applicable Variant Types

These specifications apply to:
- **Missense variants** associated with gain-of-function mechanism
- Variants evaluated for autosomal dominant PIK3CD-related immunodeficiency (APDS1)

### Variants Outside Scope

Variants with predicted impact on splicing (SpliceAI Δ score ≥0.2) should **not** be evaluated using these specifications but rather using alternative specifications for autosomal recessive disease with a loss-of-function mechanism, unless functional evidence indicates a gain-of-function effect.

---

## 3. Pathogenic Criteria Specifications

### PVS1 - Null Variant

| Strength | Application |
|----------|-------------|
| **Not Applicable** | Does not apply given gain-of-function disease mechanism |

---

### PS1 - Same Amino Acid Change

**Original ACMG Summary:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.

#### PS1 (Strong) - 4 points
- Use for missense variants when other variant was classified as **Pathogenic** for autosomal dominant PIK3CD gain-of-function-related disease by Antibody Deficiencies VCEP specifications without using PS1
- Neither change should be predicted to affect splicing (SpliceAI Δ score <0.2)

#### PS1_Moderate - 2 points
- Use for missense variants when other variant was classified as **Likely Pathogenic** for autosomal dominant PIK3CD gain-of-function-related disease by Antibody Deficiencies VCEP specifications without using PS1
- Neither change should be predicted to affect splicing (SpliceAI Δ score <0.2)

---

### PS2 - De Novo Occurrence

**Original ACMG Summary:** De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.

**VCEP Modification:** This code has been adapted to also reward de novo occurrences in cases where maternity and paternity are suspected but not confirmed (PM6 code is not in use).

#### PS2_VeryStrong - 8 points
- Use when there are **≥4 de novo occurrences** according to Table 2
- Can only be applied if the variant does not meet BA1 or BS1

#### PS2 (Strong) - 4 points
- Use when there are **2-3 de novo occurrences** according to Table 2
- Can only be applied if the variant does not meet BA1 or BS1

#### PS2_Moderate - 2 points
- Use when there is **1 de novo occurrence** according to Table 2
- Can only be applied if the variant does not meet BA1 or BS1

#### PS2_Supporting - 1 point
- Use when there is **1 de novo occurrence** with lower phenotypic consistency
- Can only be applied if the variant does not meet BA1 or BS1

**Phenotypic Consistency Determination:**
1. If proband scores ≥4 and <6 phenotype points but lacks PIK3R1 genotyping → "Phenotype consistent with gene but not highly specific and high genetic heterogeneity"
2. If proband scores ≥6 phenotype points but lacks PIK3R1 genotyping → "Phenotype consistent with gene but not highly specific"
3. If proband scores ≥10 phenotype points AND has PIK3R1 genotyping → "Phenotype highly specific for gene"

---

### PS3 - Functional Studies

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.

#### PS3 (Strong) - 4 points
Apply for:
- Evidence from an **animal model** expressing the variant and recapitulating the APDS phenotype
- Abnormal result in an approved in vitro assay with calculated **OddsPath >18.7**

**Approved High-Throughput Assay:**
- Enrichment of variant in high phospho-S6 and phospho-AKT T cells relative to low phospho-S6 and phospho-AKT T cells within NGS-based screen of donor T cells subjected to CRISPR-mediated adenine base-editing (PMID: 40543502)

#### PS3_Moderate - 2 points
- Abnormal result in approved in vitro assay with minimum of 11 total pathogenic and benign variant controls

#### PS3_Supporting - 1 point
Apply based on abnormal result in an approved in vitro assay:

**Approved Assay Classes:**
| Assay Class | References |
|-------------|------------|
| AKT kinase activity assay | PMID: 24136356, 24165795, 28414062 |
| Lipid kinase activity | PMID: 24136356, 28167755, 28414062 |
| Lipid vesicle affinity | PMID: 24136356 |
| Conformational dynamics | PMID: 28167755, 28414062 |

> **Note:** Protein binding assays testing PIK3CD binding to PIK3R1 were excluded based on lack of evidence of altered binding by disease-associated variants. Patient cell-based functional assays are considered under PP4_Moderate instead.

---

### PS4 - Prevalence in Affected Individuals

**Original ACMG Summary:** The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.

**Requirements for counting probands:**
- Proband must reach ≥6 points in phenotype scoring criteria (Table 3)
- At minimum, a primary immunodeficiency or antibody gene testing panel must have identified no LP/P variants in PIK3R1
- If no gene panel was performed, ≥10 phenotype points required
- Variant must not meet BS1 or BA1

#### PS4 (Strong) - 4 points
- **≥4 probands** meeting phenotype and genetic testing requirements

#### PS4_Moderate - 2 points
- **2-3 probands** meeting phenotype and genetic testing requirements

#### PS4_Supporting - 1 point
- **1 proband** meeting phenotype and genetic testing requirements

> **Important:** A proband used for PP4 or PP4_Moderate cannot be included in PS4.

---

### PM1 - Mutational Hot Spot

| Strength | Application |
|----------|-------------|
| **Not Applicable** | Does not apply to PIK3CD variant curation for this disease entity |

---

### PM2 - Absent from Controls

**Original ACMG Summary:** Absent from controls (or at extremely low frequency if recessive) in population databases.

#### PM2_Supporting - 1 point
- Applicable to variants with total allele frequency **<0.00000132** across all populations in gnomAD v4.1.0

**Threshold Parameters (Whiffin/Ware Calculator):**
| Parameter | Value |
|-----------|-------|
| Prevalence | 1 in 4,000 (PMID: 17577648, 23201919) |
| Allelic heterogeneity | 1 |
| Genetic heterogeneity | 1 |
| Penetrance | 0.95 (PMID: 27555459, 36749229, 37390899) |

---

### PM3 - In Trans with Pathogenic Variant

| Strength | Application |
|----------|-------------|
| **Not Applicable** | Does not apply since model of inheritance is autosomal dominant |

---

### PM4 - Protein Length Changes

| Strength | Application |
|----------|-------------|
| **Not Applicable** | Does not apply since mechanism is GOF caused by missense mutations |

---

### PM5 - Novel Missense at Same Residue

**Original ACMG Summary:** Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.

#### PM5 (Moderate) - 2 points
- Use for missense variants when other variant at same position was classified as **Pathogenic** for AD PIK3CD-related disease without using PM5
- Neither change should be predicted to affect splicing (SpliceAI Δ score ≤0.2)
- Do not apply at codon where any benign variants are known
- Variant must have Grantham distance ≥ that of known pathogenic variant

#### PM5_Supporting - 1 point
- Use for missense variants when other variant was classified as **Likely Pathogenic** for AD PIK3CD-related disease without using PM5
- Same caveats as above

---

### PM6 - Assumed De Novo

| Strength | Application |
|----------|-------------|
| **Not Applicable** | De novo occurrences without parental confirmation are counted under PS2 using the point system |

---

### PP1 - Co-segregation

**Original ACMG Summary:** Co-segregation with disease in multiple affected family members.

**Requirements:**
- Each family member must reach ≥6 points in PS4 counting rubric to be considered affected
- Should not be applied when variant meets BA1 or BS1
- Combined strength of PP1 and PP4 is limited (PP1_Strong can meet PP4 but not PP4_Moderate)

#### PP1_Strong - 4 points
- Co-segregation across **≥4 meioses** in one family or combined across multiple unrelated families

#### PP1_Moderate - 2 points
- Co-segregation across **≥2 meioses** in one family or combined across multiple unrelated families

#### PP1 (Supporting) - 1 point
- Co-segregation across **≥1 meiosis** (variant present in proband + affected relative)

---

### PP2 - Low Rate of Benign Missense

| Strength | Application |
|----------|-------------|
| **Not Applicable** | Given GOF mechanism, it is not reasonable to expect any missense variant will lead to GOF |

---

### PP3 - Computational Evidence (Pathogenic)

**Original ACMG Summary:** Multiple lines of computational evidence support a deleterious effect.

#### PP3 (Supporting) - 1 point
Met by a missense variant with:
- **REVEL score ≥0.644** AND
- **CADD PHRED score ≥25.3**

> **Note:** Higher strength levels (PP3_Moderate/Strong) not recommended due to poor performance and significant discordance between REVEL and CADD for PIK3CD variants.

**SpliceAI Caveat:** Variants with SpliceAI Δ score ≥0.2 should not be evaluated using these specifications.

---

### PP4 - Specific Phenotype

**Original ACMG Summary:** Patient's phenotype or family history is highly specific for a disease with a single genetic etiology.

#### PP4_Moderate - 2 points
Met when proband:
- Scores ≥10 phenotype points AND
- Has genotyping to rule out PIK3R1 variant AND
- Has patient cell-based functional assays showing abnormally high PI3K delta pathway activity

**Patient Cell-Based Functional Assays:**
- Isolate T cells from affected and unaffected patients
- Stimulation by anti-CD3 and anti-CD28 antibodies
- Assessment by western blotting or flow cytometry with phospho-specific antibodies
- Detect AKT phosphorylation at Ser473 or Thr308
- Detect S6 phosphorylation at Ser235/Ser236 or Ser240/Ser244
- Phosphorylation may be 1.2-fold to 7.5-fold higher in affected vs. healthy control

#### PP4 (Supporting) - 1 point
Met when proband:
- Scores ≥10 phenotype points AND
- Has genotyping to rule out PIK3R1 variant

> **Note:** Proband used for PP4/PP4_Moderate cannot be included in PS4. Variant must not meet BS1 or BA1.

---

### PP5 - Reputable Source Reports Pathogenic

| Strength | Application |
|----------|-------------|
| **Not Applicable** | Not for use per ClinGen SVI VCEP Review Committee (PMID: 29543229) |

---

## 4. Benign Criteria Specifications

### BA1 - Allele Frequency Stand-Alone

**Original ACMG Summary:** Allele frequency is above 5% in population databases.

#### BA1 (Stand Alone)
- Applicable to variants with **GrpMax filtering allele frequency ≥0.00316** in gnomAD v4.1.0
- If GrpMax not listed, use maximum AF among five major continental populations

**Threshold Parameters:**
| Parameter | Value |
|-----------|-------|
| Inheritance | Biallelic |
| Prevalence | 1 in 100,000 (adjusted from PMID: 34352450) |
| Allelic heterogeneity | 1 |
| Genetic heterogeneity | 1 |
| Penetrance | 1 |

---

### BS1 - Allele Frequency Greater Than Expected

#### BS1 (Strong) - (-4) points
- Applicable to variants with **GrpMax filtering allele frequency ≥0.000316** in gnomAD v4.1.0
- Threshold derived by decreasing BA1 cutoff by one order of magnitude

---

### BS2 - Observed in Healthy Individual

| Strength | Application |
|----------|-------------|
| **Not Applicable** | Does not apply due to incomplete penetrance and variable expressivity |

---

### BS3 - Functional Studies (Benign)

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies show no damaging effect.

#### BS3 (Strong) - (-4) points
- May be applied for evidence from animal model expressing variant and failing to recapitulate APDS phenotype
- Reviewed case-by-case by VCEP

#### BS3_Moderate - (-2) points
- Normal result in approved in vitro assay with minimum 11 total P and B variant controls

#### BS3_Supporting - (-1) point
- Normal result in **at least two different approved in vitro assays** (from two separate assay classes)

**Approved Assay Classes:**
- AKT kinase activity assay
- Lipid kinase activity
- NGS-based CRISPR screen (PMID: 40543502)
- Lipid vesicle affinity
- Conformational dynamics

---

### BS4 - Lack of Segregation

**Original ACMG Summary:** Lack of segregation in affected members of a family.

#### BS4 (Strong) - (-4) points
- Patients lacking segregation must reach ≥6 points on phenotypic scoring
- Lack of segregation in **>1 affected family member**

#### BS4_Supporting - (-1) point
- Only **1 affected family member** lacks segregation

---

### BP1 - Missense in Truncating Gene

| Strength | Application |
|----------|-------------|
| **Not Applicable** | — |

---

### BP2 - In Trans/Cis with Pathogenic

| Strength | Application |
|----------|-------------|
| **Not Applicable** | Field does not understand all potential allelic mechanisms; combinatorial variant effects cannot be excluded |

---

### BP3 - In-Frame in Repetitive Region

| Strength | Application |
|----------|-------------|
| **Not Applicable** | — |

---

### BP4 - Computational Evidence (Benign)

**Original ACMG Summary:** Multiple lines of computational evidence suggest no impact.

#### BP4 (Supporting) - (-1) point
Met by missense variant with:
- **REVEL score ≤0.290** AND
- **CADD PHRED score ≤22.7**

Also met by:
- Synonymous or intronic variant not predicted to impact splicing (SpliceAI Δ score <0.1)

> **Note:** Variants with SpliceAI Δ score ≥0.2 should not be evaluated using these specifications.

---

### BP5 - Alternate Molecular Basis

#### BP5 (Supporting) - (-1) point
- Variant found in case with alternate molecular basis for disease
- **At least two such cases required**

---

### BP6 - Reputable Source Reports Benign

| Strength | Application |
|----------|-------------|
| **Not Applicable** | Not for use per ClinGen SVI (PMID: 29543229) |

---

### BP7 - Synonymous/Intronic with No Splicing Impact

#### BP7 (Supporting) - (-1) point
- Met for synonymous variant if SpliceAI does not predict splicing defect (cutoff <0.1)
- Synonymous variants in first nucleotide of exon or final 3 nucleotides of exon are **not eligible**
- Met for intronic variant if SpliceAI does not predict splicing defect (cutoff <0.1)
- Intronic variants between +1 and +6 or between -1 and -20 are **not eligible** (splice region)

---

## 5. Phenotype Scoring Criteria

### Table 3: PIK3CD Phenotype Scoring Criteria

#### Clinical Phenotype

| Feature | Points |
|---------|--------|
| Recurrent sinopulmonary infections and/or their sequelae* | 4 |
| Nonmalignant lymphoproliferation (hepatosplenomegaly, lymphadenopathy) | 4 |
| Severe, persistent, recurrent, atypical, opportunistic viral infections (esp herpesviral, including skin warts) | 3 |
| Lymphoma | 2 |
| Non-infectious gastrointestinal or hepatobiliary disease*** | 1 |
| Other organ-/tissue-specific autoimmune/inflammatory disease**** | 1 |
| Pre-(IUGR) or post-natal failure to thrive / short stature with Z-score <-2** | 0.5 |
| Neurodevelopmental delay and neuropsychiatric disorders** | 0.5 |
| Malignancy (non-lymphoma) | 0.5 |

#### Laboratory Phenotype

| Feature | Points |
|---------|--------|
| Increased proportion of CD27low CD24bright CD38bright early transitional T1/T2 B cells | 2 |
| Increased proportion of follicular helper T cells | 2 |
| Decreased proportion of switched memory B cells | 1 |
| Increased expression of senescent T markers (CD57+, KLRG1, lack of CD27/28) | 1 |
| Increased CD10+ B cells | 1 |
| Histopath findings with lymphoid hyperplasia (lymphadenopathy, lymphadenitis, reactive hyperplasia) | 1 |
| Immune-mediated cytopenias | 1 |
| Abnormal immunoglobulin levels | 0.5 (abnormal IgG) / 0.5 (elevated IgM) |
| Lymphopenia | 0.5 |
| Abnormal TBNK levels | 0.5 |
| Peripheral eosinophilia | 0.5 |
| Serum IgE >500kU/L | 0.5 |

#### Footnotes

**\*Recurrent sinopulmonary infections and/or their sequelae** includes:
- (A) Clinical history of recurrent sinopulmonary (upper and lower respiratory tract) infections such as sinusitis, otitis, pneumonia/pneumonitis, bronchitis, bronchiectasis, or abnormal pulmonary function test
- (B) Imaging/pathology findings of bronchiectasis, mosaic attenuation, peribronchial inflammation, air-space opacities, bronchial wall thickening, volume loss, or atelectasis

**\*\*More prevalent** in PIK3R1-related APDS2 +/- SHORT syndrome but still noted in some APDS1 patients

**\*\*\*Non-infectious gastrointestinal or hepatobiliary disease** includes:
Enteropathy, hepatopathy, autoimmune hepatitis, inflammatory bowel disease, primary sclerosing cholangitis, enterocolitis, celiac disease, atrophic gastritis, lymphocytic/microscopic colitis, exocrine pancreatic insufficiency, or pernicious anemia

**\*\*\*\*Endocrinopathies** (e.g., Type I diabetes, autoimmune thyroiditis), vasculitis, arthritis, serositis, glomerulonephritis, inflammatory skin disease (e.g., erythema nodosum, dermatitis), inflammatory eye disease (e.g., uveitis), SLE-like features, etc.

---

## 6. De Novo Occurrence Scoring

### Table 1: Points Awarded Per De Novo Occurrence

| Phenotypic Consistency | Confirmed De Novo | Assumed De Novo |
|------------------------|-------------------|-----------------|
| Phenotype highly specific for gene | 2 | 1 |
| Phenotype consistent with gene but not highly specific | 1 | 0.5 |
| Phenotype consistent with gene but not highly specific and high genetic heterogeneity* | 0.5 | 0.25 |
| Phenotype not consistent with gene | 0 | 0 |

*Maximum allowable value of 1 may contribute to overall score

### Table 2: ACMG/AMP Evidence Strength Level for De Novo Occurrence(s)

| Total De Novo Points | Evidence Strength |
|---------------------|-------------------|
| 0.5 | Supporting |
| 1 | Moderate |
| 2 | Strong |
| ≥4 | Very Strong |

---

## 7. Bayesian Point-Based Classification System

### Evidence Point Values

| Evidence Strength | Pathogenic Points | Benign Points |
|-------------------|-------------------|---------------|
| Indeterminate | 0 | 0§ |
| Supporting | 1 | -1 |
| Moderate | 2 | -2† |
| Strong | 4 | -4 |
| Very Strong | 8 | -8† |

### Classification Categories

| Category | Point Range |
|----------|-------------|
| **Pathogenic** | ≥10 |
| **Likely Pathogenic** | 6-9 |
| **Uncertain Significance (VUS)** | 0-5 |
| **Likely Benign** | -1 to -6 |
| **Benign** | ≤-7 |

> Reference: PMID: 32720330

---

## 8. Functional Assay Guidelines

### Approved In Vitro Assays for PS3/BS3

| Assay Class | Method | References |
|-------------|--------|------------|
| **AKT kinase activity** | Measurement of AKT phosphorylation in cell-free or cell-based systems | PMID: 24136356, 24165795, 28414062 |
| **Lipid kinase activity** | Assessment of PI3K lipid kinase enzymatic activity | PMID: 24136356, 28167755, 28414062 |
| **Lipid vesicle affinity** | Membrane binding assessment | PMID: 24136356 |
| **Conformational dynamics** | Hydrogen-deuterium exchange mass spectrometry | PMID: 28167755, 28414062 |
| **High-throughput functional screen** | CRISPR-mediated adenine base-editing in T cells | PMID: 40543502 |

### Patient Cell-Based Assays (for PP4_Moderate)

**Methodology:**
1. Isolate T cells from affected and unaffected patients
2. Stimulate with anti-CD3 and anti-CD28 antibodies
3. Assess PI3K delta pathway function using:
   - Western blotting or flow cytometry
   - Phospho-specific antibodies for pAKT (Ser473 or Thr308) and/or pS6 (Ser235/236 or Ser240/244)

**Expected Results:**
- Phosphorylation upregulated 1.2-fold to 7.5-fold in affected patient cells
- May be abrogated by PI3K-specific inhibitor (e.g., idelalisib)

---

## 9. Computational Predictors

### REVEL and CADD Thresholds

| Predictor | PP3 Threshold (Pathogenic) | BP4 Threshold (Benign) |
|-----------|---------------------------|------------------------|
| **REVEL** | ≥0.644 | ≤0.290 |
| **CADD PHRED** | ≥25.3 | ≤22.7 |

> **Requirement:** Both predictors must agree for PP3 or BP4 to be applied. This dual requirement addresses discordance observed in PIK3CD variants.

### SpliceAI Thresholds

| Application | SpliceAI Δ Score |
|-------------|------------------|
| Predicted splicing impact (exclude from GOF specs) | ≥0.2 |
| No predicted splicing impact (BP4/BP7 eligible) | <0.1 |

---

## 10. References

### Key Publications

1. **Richards S, et al.** (2015) Standards and guidelines for the interpretation of sequence variants: a joint consensus recommendation of the ACMG and AMP. *Genet Med.* PMID: 25741868

2. **Tavtigian SV, et al.** (2020) Fitting a naturally scaled point system to the ACMG/AMP variant classification guidelines. *Hum Mutat.* PMID: 32720330

3. **Brnich SE, et al.** (2019) Recommendations for application of the functional evidence PS3/BS3 criterion using the ACMG/AMP sequence variant interpretation framework. *Genome Med.* PMID: 31892348

4. **Angulo I, et al.** (2013) Phosphoinositide 3-kinase δ gene mutation predisposes to respiratory infection and airway damage. *Science.* PMID: 24136356

5. **Lucas CL, et al.** (2014) Dominant-activating germline mutations in the gene encoding the PI(3)K catalytic subunit p110δ result in T cell senescence and human immunodeficiency. *Nat Immunol.* PMID: 24165795

6. **Biesecker LG, et al.** (2024) Evidence-based calibrated thresholds for use of PP1/BS4 criteria for Mendelian disorders. *Am J Med Genet.* PMID: 38103548

### gnomAD Database

- Version: gnomAD v4.1.0
- URL: https://gnomad.broadinstitute.org/

### Population Frequency Calculator

- Whiffin/Ware Calculator: https://www.cardiodb.org/allelefrequencyapp/

---

## Summary Table: PIK3CD ACMG/AMP Criteria Application

| Code | Strength(s) | Points | Application Status |
|------|-------------|--------|-------------------|
| PVS1 | — | — | Not Applicable (GOF mechanism) |
| PS1 | Strong/Moderate | 4/2 | Applicable |
| PS2 | VeryStrong/Strong/Moderate/Supporting | 8/4/2/1 | Applicable (modified) |
| PS3 | Strong/Moderate/Supporting | 4/2/1 | Applicable |
| PS4 | Strong/Moderate/Supporting | 4/2/1 | Applicable |
| PM1 | — | — | Not Applicable |
| PM2 | Supporting | 1 | Applicable (downgraded) |
| PM3 | — | — | Not Applicable (AD inheritance) |
| PM4 | — | — | Not Applicable (GOF mechanism) |
| PM5 | Moderate/Supporting | 2/1 | Applicable |
| PM6 | — | — | Not Applicable (covered by PS2) |
| PP1 | Strong/Moderate/Supporting | 4/2/1 | Applicable |
| PP2 | — | — | Not Applicable |
| PP3 | Supporting | 1 | Applicable (dual predictor required) |
| PP4 | Moderate/Supporting | 2/1 | Applicable |
| PP5 | — | — | Not Applicable |
| BA1 | Stand Alone | — | Applicable |
| BS1 | Strong | -4 | Applicable |
| BS2 | — | — | Not Applicable |
| BS3 | Strong/Moderate/Supporting | -4/-2/-1 | Applicable |
| BS4 | Strong/Supporting | -4/-1 | Applicable |
| BP1 | — | — | Not Applicable |
| BP2 | — | — | Not Applicable |
| BP3 | — | — | Not Applicable |
| BP4 | Supporting | -1 | Applicable (dual predictor required) |
| BP5 | Supporting | -1 | Applicable |
| BP6 | — | — | Not Applicable |
| BP7 | Supporting | -1 | Applicable |

---

*Document compiled from ClinGen Antibody Deficiencies VCEP specifications, pilot results, and SVI feedback. For official guidance, refer to the ClinGen website.*
