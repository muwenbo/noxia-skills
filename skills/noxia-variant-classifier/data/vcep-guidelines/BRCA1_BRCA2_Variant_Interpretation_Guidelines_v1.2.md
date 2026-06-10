# ClinGen ENIGMA VCEP Variant Interpretation Guidelines for BRCA1 & BRCA2

**Version:** 1.2
**Released:** 2024-11-18
**Affiliation:** ENIGMA (Evidence-based Network for the Interpretation of Germline Mutant Alleles) Variant Curation Expert Panel
**Based on:** Richards et al., 2015 ACMG/AMP Guidelines (PMID: 25741868)

---

## Gene Information

### BRCA1

| Attribute | Value |
|-----------|-------|
| **Gene** | BRCA1 (HGNC:1100) |
| **HGNC Name** | BRCA1 DNA repair associated |
| **Transcript** | NM_007294.4 (ENST00000357654.9) |
| **Genomic Reference** | NG_005905.2 (LRG 292) |
| **Disease** | Hereditary breast and ovarian cancer syndrome |
| **Associated Conditions** | Breast cancer, Ovarian cancer, Fanconi anemia complementation group S (FANCS) |
| **Inheritance** | Autosomal dominant (cancer susceptibility); Autosomal recessive (Fanconi anemia) |

### BRCA2

| Attribute | Value |
|-----------|-------|
| **Gene** | BRCA2 (HGNC:1101) |
| **HGNC Name** | BRCA2 DNA repair associated |
| **Transcript** | NM_000059.4 (ENST00000380152.8) |
| **Genomic Reference** | NG_012772.3 (LRG 293) |
| **Disease** | Hereditary breast and ovarian cancer syndrome |
| **Associated Conditions** | Breast cancer, Ovarian cancer, Pancreatic cancer, Prostate cancer, Fanconi anemia complementation group D1 (FANCD1) |
| **Inheritance** | Autosomal dominant (cancer susceptibility); Autosomal recessive (Fanconi anemia) |

### Clinically Important Functional Domains

| Gene | Domain | Amino Acid Range | Notes |
|------|--------|------------------|-------|
| BRCA1 | RING domain | aa 2-101 | Clinically important functional domain |
| BRCA1 | Coiled-coil domain | aa 1391-1424 | *Potentially* clinically important functional domain |
| BRCA1 | BRCT repeats | aa 1650-1857 | Clinically important functional domain |
| BRCA2 | PALB2 binding domain | aa 10-40 | Clinically important functional domain |
| BRCA2 | DNA binding domain | aa 2481-3186 | Clinically important functional domain |

---

## Table of Contents

1. [Pathogenic Criteria](#pathogenic-criteria)
   - [PVS1 - Null Variant](#pvs1---null-variant)
   - [PS1 - Same Amino Acid Change / Splicing Prediction](#ps1---same-amino-acid-change--splicing-prediction)
   - [PS2 - De Novo (Confirmed)](#ps2---de-novo-confirmed)
   - [PS3 - Functional Studies](#ps3---functional-studies)
   - [PS4 - Prevalence in Affected](#ps4---prevalence-in-affected)
   - [PM1 - Mutational Hot Spot](#pm1---mutational-hot-spot)
   - [PM2 - Absent from Controls](#pm2---absent-from-controls)
   - [PM3 - In Trans with Pathogenic (Fanconi Anemia)](#pm3---in-trans-with-pathogenic-fanconi-anemia)
   - [PM4 - Protein Length Changes](#pm4---protein-length-changes)
   - [PM5 - Novel Missense at Same Residue](#pm5---novel-missense-at-same-residue)
   - [PM5_PTC - Protein Termination Codon Variant](#pm5_ptc---protein-termination-codon-variant)
   - [PM6 - De Novo (Assumed)](#pm6---de-novo-assumed)
   - [PP1 - Co-segregation](#pp1---co-segregation)
   - [PP2 - Missense in Constrained Gene](#pp2---missense-in-constrained-gene)
   - [PP3 - Computational Evidence](#pp3---computational-evidence)
   - [PP4 - Clinical Data (Multifactorial Likelihood)](#pp4---clinical-data-multifactorial-likelihood)
   - [PP5 - Reputable Source](#pp5---reputable-source)
2. [Benign Criteria](#benign-criteria)
   - [BA1 - Allele Frequency >0.1%](#ba1---allele-frequency-01)
   - [BS1 - Frequency Greater Than Expected](#bs1---frequency-greater-than-expected)
   - [BS2 - Observed in Healthy Adult](#bs2---observed-in-healthy-adult)
   - [BS3 - Functional Studies (No Effect)](#bs3---functional-studies-no-effect)
   - [BS4 - Lack of Segregation](#bs4---lack-of-segregation)
   - [BP1 - Truncating Variants Primary](#bp1---truncating-variants-primary)
   - [BP2 - Observed in Trans/Cis](#bp2---observed-in-transcis)
   - [BP3 - In-Frame in Repetitive Region](#bp3---in-frame-in-repetitive-region)
   - [BP4 - Computational Evidence (No Impact)](#bp4---computational-evidence-no-impact)
   - [BP5 - Alternate Molecular Basis](#bp5---alternate-molecular-basis)
   - [BP6 - Reputable Source (Benign)](#bp6---reputable-source-benign)
   - [BP7 - Synonymous / Deep Intronic](#bp7---synonymous--deep-intronic)
3. [Rules for Combining Criteria](#rules-for-combining-criteria)
4. [Appendices](#appendices)

---

## Pathogenic Criteria

### PVS1 - Null Variant

**Original ACMG Summary:** Null variant (nonsense, frameshift, canonical ±1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.

**VCEP Specifications:**

In alignment with SVI recommendations for PVS1 code application, evidence strength and description has been separated for different variant types. Apply according to PVS1 flowchart, which considers knowledge of clinically important functional domains.

For predicted protein termination codon (PTC) variants, apply with exon-specific weights derived for the PM5_PTC code.

**Full gene deletion** is considered **Stand-Alone evidence** for pathogenicity.

#### PVS1 Decision Tree Considerations

| Variant Type | Considerations |
|--------------|----------------|
| **Initiation codon variants** | Consider impact on protein translation initiation |
| **Nonsense/Frameshift** | Apply exon-specific PVS1 weight; consider NMD prediction |
| **Canonical splice site (±1,2)** | Apply based on splicing predictions; consider rescue of in-frame transcript |
| **Single/Multi-exon deletion** | Consider reading frame; in-frame deletions in non-essential regions may warrant lower weight |
| **Duplication** | Consider impact on reading frame and protein function |

#### Strength Levels

PVS1 strength is determined by exon location, NMD prediction, and functional domain considerations. Refer to **Table 4** (separate Excel file) for exon-specific code assignments.

| Strength | General Application |
|----------|---------------------|
| **Very Strong (PVS1)** | Null variants predicted to undergo NMD or located in critical functional domains |
| **Strong (PVS1_Strong)** | Variants with some evidence of potential escape from NMD |
| **Moderate (PVS1_Moderate)** | Variants with higher likelihood of producing truncated protein with residual function |
| **Supporting (PVS1_Supporting)** | Variants where loss of function is less certain |

---

### PVS1 (RNA) - mRNA Assay Evidence

**Description:** Null variant in a gene where loss of function is a known mechanism of disease, as measured by effect on mRNA transcript profile - mRNA assay only.

**VCEP Specifications:**

Assay measures effect via mRNA only. Apply as **PVS1_Variable Weight (RNA)**. See **Figure 1B** for the process to apply codes for splicing data, in context of:
- Location and predicted bioinformatic impact of the variant
- Adaptive weighting according to assay methodology
- Proportion of functional transcript retained

---

### PS1 - Same Amino Acid Change / Splicing Prediction

**Original ACMG Summary:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.

**VCEP Specifications:**

#### For Missense Variants

| Strength | Criteria |
|----------|----------|
| **Strong (PS1)** | Predicted missense substitution where a previously classified **Pathogenic** variant acts via protein change (no confirmed or predicted effect on mRNA splicing; SpliceAI ≤0.1) |
| **Moderate (PS1_Moderate)** | Predicted missense substitution where a previously classified **Likely Pathogenic** variant acts via protein change (no confirmed or predicted effect on mRNA splicing; SpliceAI ≤0.1) |

#### For Splicing Variants

PS1 can be applied for exonic and intronic variants with the same predicted impact on splicing as a previously classified (Likely) Pathogenic variant. Weight varies depending on relative positions and confidence in classification of the reference variant.

**Prerequisites for splicing application:**
1. The predicted event of the VUA must precisely match the predicted event of the known (Likely) Pathogenic variant (e.g., both predicted to lead to exon A skipping, or both to enhanced use of cryptic site B)
2. The strength of the prediction for the VUA must be of similar or higher strength than the strength of the prediction for the known (Likely) Pathogenic variant
3. For an exonic variant, predicted or proven functional effect of missense substitution/s encoded by the VUA and (Likely) Pathogenic variant should be considered before PS1 code application

#### PS1 Code Weights for Splicing Predictions (Table 5)

| Variant Under Assessment (VUA) | Baseline Code | Position of Reference vs VUA | PS1 with P Reference | PS1 with LP Reference |
|--------------------------------|---------------|------------------------------|----------------------|----------------------|
| Outside donor/acceptor ±1,2 dinucleotide | PP3 | Same nucleotide | PS1 | PS1_Moderate |
| Outside donor/acceptor ±1,2 dinucleotide | PP3 | Within same donor/acceptor motif (including ±1,2) | PS1_Moderate | PS1_Supporting |
| At donor/acceptor ±1,2 dinucleotide | PVS1 | Within same donor/acceptor dinucleotide | PS1_Supporting | N/A |
| At donor/acceptor ±1,2 dinucleotide | PVS1 | Within same motif, outside dinucleotide | PS1_Supporting | PS1_Supporting |
| At donor/acceptor ±1,2 dinucleotide | PVS1_Strong/Moderate/Supporting | Within same donor/acceptor dinucleotide | PS1 | N/A |
| At donor/acceptor ±1,2 dinucleotide | PVS1_Strong/Moderate/Supporting | Within same motif, outside dinucleotide | PS1_Moderate | PS1_Supporting |

**Note:** Donor/acceptor motif ranges for GT-AG introns:
- **Donor site motif:** Last 3 bases of exon and 6 nucleotides of intronic sequence adjacent to exon
- **Acceptor site motif:** First base of exon and 20 nucleotides upstream from exon boundary

---

### PS2 - De Novo (Confirmed)

**Original ACMG Summary:** De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.

**VCEP Specifications:** **Do not use**

BRCA1/2-related cancers occur relatively commonly. No information exists to calibrate the predictive capacity of de novo occurrences.

---

### PS3 - Functional Studies

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.

**VCEP Specifications:**

#### mRNA Assay Only (Use Alternative Code)

When assay measures effect via mRNA only, apply as **PVS1_Variable Weight (RNA)**. See Figure 1B for the process to apply codes for splicing data.

#### Functional Assays (Protein Effect)

When assay measures effect via protein only OR mRNA and protein combined:

See **Figure 1C** for simplified flowchart to advise application of codes for functional data, in context of:
- Variant type
- Location within a (potentially) clinically important functional domain

See **Table 9** (separate Excel spreadsheet) for a comprehensive table of applicable codes using published calibrated functional assay results.

#### Key Principles for PS3/BS3 Application

1. Functional assay data must be from a calibrated assay
2. Consider variant type and predicted/observed splicing before applying codes
3. For missense variants in functional domains, protein functional assays carry more weight
4. For variants outside functional domains, splicing assays may be most informative

---

### PS4 - Prevalence in Affected

**Original ACMG Summary:** The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.

**VCEP Specifications:**

Apply for case-control studies meeting: **p-value ≤0.05 AND OR ≥4** (lower confidence interval excludes 2.0)

**Requirements:**
- Case dataset should be ethnicity and country-matched to control dataset
- If case-control LR estimates are available for a given dataset, these should be used in preference to case-control OR data, under code **PP4** (or **BP5**, if appropriate)

**Note:** Personal and family history of cancer may be used as predictors of pathogenicity if derived by clinical calibration, and applied under code **PP4** (or **BP5**, if appropriate).

#### PS4_Moderate (Proband Counting)

**Do not use** Proband Counting as originally described.

---

### PM1 - Mutational Hot Spot

**Original ACMG Summary:** Located in a mutational hot spot and/or critical and well-established functional domain without benign variation.

**VCEP Specifications:** **Do not use**

Considered as component of bioinformatic analysis (PP3/BP4).

---

### PM2 - Absent from Controls

**Original ACMG Summary:** Absent from controls (or at extremely low frequency if recessive) in population databases.

**VCEP Specification (Supporting only):**

| Criterion | Threshold | Application |
|-----------|-----------|-------------|
| **PM2_Supporting** | Absent from gnomAD (exome and genome) | Supporting evidence only |

**Preferred datasets:**
- gnomAD v2.1 non-cancer, exomes
- gnomAD v3.1 non-cancer, genomes

**Important caveats:**
- Observation of a variant **only once** in a gnomAD outbred population is **not informative** (no code applied)
- **Do not apply** for insertion, deletion, or delins variants
- **Do not apply** if read depth <25 at region around the variant
- Exclude data if variant failed quality control filter

---

### PM3 - In Trans with Pathogenic (Fanconi Anemia)

**Original ACMG Summary:** For recessive disorders, detected in trans with a pathogenic variant.

**VCEP Specifications:**

Apply for patient with phenotype consistent with BRCA1- or BRCA2-related **Fanconi Anemia (FA)**, and co-occurrent variants in the same gene.

#### Phenotype Criteria for BRCA1/2-related FA

Phenotype is considered **consistent with BRCA1- or BRCA2-related FA** if meeting criteria (i) OR (ii):

**(i)** Increased chromosome breakage and radial forms on cytogenetic testing of lymphocytes with DEB and/or MMC OR evidence of spontaneous chromosome breakage, **PLUS** at least one clinical feature from:
- Physical features
- Pathology and laboratory findings
- Cancer diagnosis ≤5 years

**(ii)** Result unknown for DEB/MMC chromosome breakage test or spontaneous chromosome breakage, **AND** at least two clinical features under at least two of the three categories above.

#### FA Clinical Features

**Physical features (~75% of affected persons):**
- Prenatal and/or postnatal short stature
- Abnormal skin pigmentation (café au lait macules, hypo-pigmentation)
- Skeletal malformations (hypoplastic thumb, hypoplastic radius)
- Microcephaly, triangular face
- Ophthalmic anomalies
- Genitourinary tract anomalies

**Pathology and laboratory findings (non-cancer related):**
- Inordinate toxicities from chemotherapy or radiation
- Progressive bone marrow failure
- Aplastic anemia
- Myelodysplastic syndrome
- Macrocytosis
- Cytopenia (thrombocytopenia, leukopenia, neutropenia)
- Increased fetal hemoglobin (often precedes anemia)

**Cancer diagnosis:** ≤5 years of age

#### PM3 Point System (Table 6)

| Presentation | P or LP in trans or homozygote | Phase unknown |
|--------------|--------------------------------|---------------|
| Phenotype consistent with BRCA1/2-related FA | 2 points | 1 point |

**Final PM3 code assignment based on sum of points:**

| Total Points | Code |
|--------------|------|
| ≥4 points | PM3_Strong |
| 2 points | PM3 (Moderate) |
| 1 point | PM3_Supporting |

**Requirements:**
- Co-occurrent P or LP variant should be assigned classification using VCEP specifications
- VUA must be sufficiently rare (not meeting a benign population evidence code)
- Stipulation for in trans can be met by:
  - Genotyping of at least one parent, OR
  - Assumed if VUA is seen with at least 2 different P/LP variants
  - Inferred in homozygote FA-affected patient due to consanguineous union
  - Inferred if both maternal and paternal lineages present with family history of cancer consistent with BRCA1/2-related cancers
- For related individuals, score only most severe presentation

---

### PM4 - Protein Length Changes

**Original ACMG Summary:** Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

**VCEP Specifications:** **Do not use**

Considered as component of bioinformatic analysis (PP3/BP4).

---

### PM5 - Novel Missense at Same Residue

**Original ACMG Summary:** Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.

**VCEP Specifications:** **Do not use**

Considered as component of bioinformatic analysis (PP3/BP4).

---

### PM5_PTC - Protein Termination Codon Variant

**Description:** Repurposing of PM5 code. Protein termination codon (PTC) variant in an exon where a different proven pathogenic PTC variant has been seen before.

**VCEP Specifications:**

Use to justify additional weight for PTC variants annotated as PVS1. Only applied to **genomic PTC changes** (not splicing). Weight determined by exon where the nucleotide change occurs.

See **Table 4** (separate Excel file) for PM5_PTC codes applicable for predicted termination codon variants organized by exon.

See **Supplementary Table 1** for justification of BRCA1 and BRCA2 exon-specific weights.

---

### PM6 - De Novo (Assumed)

**Original ACMG Summary:** Assumed de novo, but without confirmation of paternity and maternity.

**VCEP Specifications:** **Do not use**

BRCA1/2-related cancers occur relatively commonly. No information exists to calibrate the predictive capacity of de novo occurrences.

---

### PP1 - Co-segregation

**Original ACMG Summary:** Co-segregation with disease in multiple affected family members.

**VCEP Specifications:**

Apply weight based on Bayes Score (Likelihood Ratio):

| Strength | LR Threshold |
|----------|--------------|
| **PP1 (Supporting)** | LR ≥2.08:1 |
| **PP1_Moderate** | LR ≥4.3:1 |
| **PP1_Strong** | LR ≥18.7:1 |
| **PP1_Very Strong** | LR ≥350:1 |

**Recommended tool:** COOL online tool (http://bjfenglab.org/)
Additional information and pedigree formatting: https://fenglab.chpc.utah.edu/cool3/manual.html

**Stipulation for Very Strong:**
- VUS should have bioinformatically predicted (or experimentally proven) effect on protein or mRNA splicing
- If co-segregation score is from a single family, or several families from an isolated population, assess the possibility of a different causative pathogenic variant

---

### PP2 - Missense in Constrained Gene

**Original ACMG Summary:** Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.

**VCEP Specifications:** **Do not use**

High frequency of benign missense variants in BRCA1/2.

---

### PP3 - Computational Evidence

**Original ACMG Summary:** Multiple lines of computational evidence support a deleterious effect on the gene or gene product.

**VCEP Specifications:**

**Do not apply PP3 if PVS1 is met at any strength.**

#### For Missense/In-frame Variants

Apply PP3 for missense or in-frame insertion, deletion, or delins variants:
- **Inside** a (potentially) clinically important functional domain
- **AND** predicted impact via protein change (BayesDel predicted Impact)

**BayesDel Thresholds (no AF):**

| Gene | PP3 (Impact) |
|------|--------------|
| BRCA1 | ≥0.28 |
| BRCA2 | ≥0.30 |

#### For Predicted Splicing

Apply PP3 for predicted splicing (**SpliceAI ≥0.2**) for:
- Silent variants
- Missense/in-frame variants (irrespective of location in clinically important functional domain)
- Intronic variants outside of the donor and acceptor ±1,2 positions

See **Figure 1A** for process to apply codes according to variant type, location, and predicted bioinformatic impact.

---

### PP4 - Clinical Data (Multifactorial Likelihood)

**Original ACMG Summary:** Patient's phenotype or family history is highly specific for a disease with a single genetic etiology.

**VCEP Specifications:**

Breast cancer is very common and has high genetic heterogeneity. Use **ONLY** to capture combined LR towards pathogenicity, based on multifactorial likelihood clinical data.

| Strength | LR Threshold |
|----------|--------------|
| **PP4 (Supporting)** | LR ≥2.08:1 |
| **PP4_Moderate** | LR ≥4.3:1 |
| **PP4_Strong** | LR ≥18.7:1 |
| **PP4_Very Strong** | LR ≥350:1 |

**Combined LR 1.00 to <2.08** is not informative (PP4 not applicable).

**Data types that may contribute:**
- Co-segregation with disease
- Co-occurrence with a pathogenic variant in the same gene
- Reported family history
- Breast tumor pathology
- Case-control data

**Usage notes:**
- Use in context of clinically calibrated evidence types
- Provide sufficient detail to review data sources, types, and weights
- Can apply for unpublished data where there is no appropriate ACMG/AMP code
- See **Table 7** for example applications

---

### PP5 - Reputable Source

**Original ACMG Summary:** Reputable source recently reports variant as pathogenic, but the evidence is not available to the laboratory to perform an independent evaluation.

**VCEP Specifications:** **Do not use**

---

## Benign Criteria

### BA1 - Allele Frequency >0.1%

**Original ACMG Summary:** Allele frequency is above a defined threshold in population databases.

**VCEP Specification (Stand Alone):**

| Criterion | Threshold |
|-----------|-----------|
| **BA1** | Above 0.001 (0.1%) |

**Application:**
- Apply based on **maximum filter allele frequency** observed in a gnomAD non-founder population, considering exome and genome data separately
- **Do not apply** if read depth <20
- **Do not apply** to well-established pathogenic founder variants
- Exclude data if variant failed quality control filter

**Preferred datasets:**
- gnomAD v2.1 non-cancer, exomes
- gnomAD v3.1 non-cancer, genomes

---

### BS1 - Frequency Greater Than Expected

**Original ACMG Summary:** Allele frequency is greater than expected for disorder.

**VCEP Specification:**

| Criterion | Threshold |
|-----------|-----------|
| **BS1 (Strong)** | Above 0.0001 (0.01%) |
| **BS1_Supporting** | >0.00002 (0.002%) to ≤0.0001 (0.01%) |

**Application:**
- Apply based on **maximum filter allele frequency** in a gnomAD non-founder population, considering exome and genome data separately
- **Do not apply** if read depth <20
- **Do not apply** to well-established pathogenic founder variants
- Exclude data if variant failed quality control filter

**Preferred datasets:**
- gnomAD v2.1 non-cancer, exomes
- gnomAD v3.1 non-cancer, genomes

---

### BS2 - Observed in Healthy Adult

**Original ACMG Summary:** Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder.

**VCEP Specifications:**

Applied in **absence of features of recessive disease**, namely Fanconi Anemia phenotype.

#### BS2 Point System (Table 8)

| Proband Presentation | VUA in trans with P or LP | Homozygote | Phase unknown |
|----------------------|---------------------------|------------|---------------|
| First cancer onset >50y OR cancer-unaffected at follow-up >50y | 4 points | 2 points | 1 point |
| First cancer onset 40-50y OR cancer-unaffected at follow-up 40-50y | 2 points | 1 point | 0.5 points |

**Final BS2 code assignment based on sum of points:**

| Total Points | Code |
|--------------|------|
| ≥4 points | BS2 (Strong) |
| 2 points | BS2_Moderate |
| 1 point | BS2_Supporting |

**Requirements:**
- VUA should **not** be bioinformatically predicted (or experimentally proven) to have a clinically important effect on protein or mRNA splicing
- Co-occurrent P or LP variant should be assigned classification using VCEP specifications
- Apply **only** for phenotyped individuals from clinical or research cohorts
- **NOT** to be applied for data used to assign frequency-based codes
- Note: Variants observed as ≥2 homozygotes in gnomAD (assumed unaffected adults) are already captured by BA1 or BS1 frequency codes

---

### BS3 - Functional Studies (No Effect)

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

**VCEP Specifications:**

#### mRNA Assay Only (Use Alternative Code)

When assay measures effect via mRNA only, apply as **BP7_Strong (RNA)** for:
- Intronic variants
- Silent variants
- Missense/in-frame variants located **outside** a (potentially) clinically important functional domain

See **Figure 1B** for process to apply codes for splicing data.

#### Functional Assays (Protein Effect)

When assay measures effect via protein only OR mRNA and protein combined:

See **Figure 1C** for process to apply codes for functional data, in context of variant type and location.

See **Table 9** (separate Excel spreadsheet) for comprehensive table of applicable codes using published calibrated functional assay results.

---

### BS4 - Lack of Segregation

**Original ACMG Summary:** Lack of segregation in affected members of a family.

**VCEP Specifications:**

Apply weight based on Bayes Score (Likelihood Ratio):

| Strength | LR Threshold |
|----------|--------------|
| **BS4_Supporting** | LR ≤0.48 to >0.23:1 |
| **BS4_Moderate** | LR ≤0.23:1 |
| **BS4 (Strong)** | LR ≤0.05:1 |
| **BS4_Very Strong** | LR ≤0.00285:1 |

**Recommended tool:** COOL online tool (http://bjfenglab.org/)
Additional information and pedigree formatting: https://fenglab.chpc.utah.edu/cool3/manual.html

**Stipulation for Very Strong:**
- Assess the possibility of bi-linearity to explain negative co-segregation

---

### BP1 - Truncating Variants Primary

**Original ACMG Summary:** Missense variant in a gene for which primarily truncating variants are known to cause disease.

**VCEP Specifications:**

Apply **BP1_Strong** for silent substitution, missense, or in-frame insertion/deletion/delins variants:
- Located **outside** a (potentially) clinically important functional domain
- **AND** no splicing predicted (SpliceAI ≤0.1)
- Missense prediction not applicable

See **Figure 1A** for process to apply codes according to variant type, location, and predicted bioinformatic impact.

---

### BP2 - Observed in Trans/Cis

**Original ACMG Summary:** Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder, or observed in cis with a pathogenic variant in any inheritance pattern.

**VCEP Specifications:** **Do not use**

Applied only in the context of BS2.

---

### BP3 - In-Frame in Repetitive Region

**Original ACMG Summary:** In-frame deletions/insertions in a repetitive region without a known function.

**VCEP Specifications:** **Do not use**

Captured by bioinformatic tool prediction and domain analysis.

---

### BP4 - Computational Evidence (No Impact)

**Original ACMG Summary:** Multiple lines of computational evidence suggest no impact on gene or gene product.

**VCEP Specifications:**

Apply BP4 for:

1. **Missense or in-frame variants inside a functional domain:**
   - No predicted impact via protein change (BayesDel predicted No Impact)
   - **AND** no predicted impact via splicing (SpliceAI ≤0.1)

2. **Silent variants inside a functional domain:**
   - No predicted impact via splicing (SpliceAI ≤0.1)

3. **Intronic variants outside donor/acceptor ±1,2:**
   - No predicted impact via splicing (SpliceAI ≤0.1)

**BayesDel Thresholds (no AF):**

| Gene | BP4 (No Impact) |
|------|-----------------|
| BRCA1 | ≤0.15 |
| BRCA2 | ≤0.18 |

See **Figure 1A** for process to apply codes according to variant type, location, and predicted bioinformatic impact.

---

### BP5 - Alternate Molecular Basis

**Original ACMG Summary:** Variant found in a case with an alternate molecular basis for disease.

**VCEP Specifications:**

**N/A for co-observation:** Cases with pathogenic variants in two (or more) different known breast-ovarian cancer risk genes have no specific phenotype.

Use **ONLY** to capture combined LR against pathogenicity, based on multifactorial likelihood clinical data.

| Strength | LR Threshold |
|----------|--------------|
| **BP5 (Supporting)** | LR ≤0.48 to >0.23:1 |
| **BP5_Moderate** | LR ≤0.23:1 |
| **BP5_Strong** | LR ≤0.05:1 |
| **BP5_Very Strong** | LR ≤0.00285:1 |

**Combined LR >0.48-1.00** is not informative (BP5 not applicable).

**Usage notes:**
- Use in context of clinically calibrated evidence types
- Provide sufficient detail to review data sources, types, and weights
- See **Table 7** for example applications

---

### BP6 - Reputable Source (Benign)

**Original ACMG Summary:** Reputable source recently reports variant as benign but the evidence is not available to the laboratory to perform an independent evaluation.

**VCEP Specifications:** **Do not use**

---

### BP7 - Synonymous / Deep Intronic

**Original ACMG Summary:** A synonymous (silent) variant for which splicing prediction algorithms predict no impact, and the nucleotide is not highly conserved.

**VCEP Specifications:**

Apply BP7 for:

1. **Silent variant inside a functional domain:**
   - IF BP4 is met (SpliceAI ≤0.1)

2. **Intronic variants located outside conserved donor or acceptor motif positions (at or beyond positions +7/-21):**
   - IF BP4 is met (SpliceAI ≤0.1)

**Note:** Following convention, this code is applied **in addition to BP4** to capture the low prior probability of pathogenicity of silent variants. Nucleotide conservation is not considered relevant.

See **Figure 1A** for process to apply codes according to variant type, location, and predicted bioinformatic impact.

---

### BP7_Strong (RNA)

**Description:** Repurposing of BP7 code. Well-established in vitro or in vivo functional studies shows no damaging effect on protein function as measured by effect on mRNA transcript profile - mRNA assay only.

**VCEP Specifications:**

Apply **BP7_Strong (RNA)** for:
- Intronic variants
- Silent variants
- Missense/in-frame variants located **outside** a (potentially) clinically important functional domain

When assay measures effect via mRNA only.

See **Figure 1B** for process to apply codes for splicing data, in context of location and predicted bioinformatic impact, and adaptive weighting according to assay methodology and proportion of functional transcript retained.

---

## Rules for Combining Criteria

### Approach 1: Adapted ACMG-AMP (Default)

This approach represents a minor adaptation of the traditional ACMG-AMP classification system, incorporating results from the Bayesian Framework analysis (Tavtigian et al 2018).

### Pathogenic Classification

| Criteria Combination |
|---------------------|
| 1 Very Strong **AND** (≥1 Strong OR ≥1 Moderate OR ≥2 Supporting) |
| 1 Strong **AND** (≥3 Moderate OR 2 Moderate & ≥2 Supporting OR 1 Moderate & ≥4 Supporting) |
| 2 Strong **AND** (≥1 Moderate OR ≥2 Supporting) |
| ≥3 Strong |

### Likely Pathogenic Classification

| Criteria Combination |
|---------------------|
| 1 Very Strong **AND** 1 Supporting |
| 2 Strong |
| 1 Strong **AND** 1-2 Moderate |
| 1 Strong **AND** ≥2 Supporting |
| ≥3 Moderate |
| 2 Moderate **AND** ≥2 Supporting |
| 1 Moderate **AND** ≥4 Supporting |

### Benign Classification

| Criteria Combination |
|---------------------|
| 1 Stand-alone (BA1) |
| 1 Very Strong **AND** (1 Strong OR 1 Moderate OR 1 Supporting) |
| ≥2 Strong |
| 1 Strong **AND** (2 Moderate OR 1 Moderate & ≥1 Supporting OR ≥3 Supporting) |

### Likely Benign Classification

| Criteria Combination |
|---------------------|
| 1 Strong **AND** (1 Supporting OR 1 Moderate) |
| 1 Moderate **AND** 1 Supporting |
| ≥2 Supporting |
| 1 Strong, **if based on multiple evidence types*** |

*Likely Benign can be assigned based on one Strong Benign code if multiple evidence types contribute to the code assigned. For example: BS4, if multiple likelihood ratios contribute to the combined likelihood ratio used to assign strong evidence; BP1_Strong represents a combination of the following evidence types: variant type, position (domain info) and prediction (splicing).

---

### Approach 2: Point System (For Contradictory Evidence)

The second approach, to be applied **when both benign and pathogenic criteria are met**, is the point system (Tavtigian et al 2020, PMID: 32720330).

#### Point Values

| Pathogenic Code Strength | Points | Benign Code Strength | Points |
|--------------------------|--------|----------------------|--------|
| Very Strong | +8 | Very Strong | -8 |
| Strong | +4 | Strong | -4 |
| Moderate | +2 | Moderate | -2 |
| Supporting | +1 | Supporting | -1 |
| Indeterminate | 0 | Indeterminate | 0 |

**Note:** Contradictory evidence includes uninformative bioinformatic evidence; PP3 and BP4 not assigned = Indeterminate (0 points).

#### Point Ranges for Classification

| Point Range | Classification |
|-------------|----------------|
| ≤-7 | Benign |
| -6 to -2 | Likely Benign |
| -1 to 5 | Uncertain Significance |
| 6 to 9 | Likely Pathogenic |
| ≥10 | Pathogenic |

**Important caution:** Use clinical judgment when classifying variants using the points system if there is significant conflicting evidence (more than one code in conflict). The ENIGMA BRCA1 and BRCA2 VCEP requires discussion before assigning a classification to such variants.

**Note:** Both approaches assume a global prior probability of pathogenicity of 0.10. On this basis:
- Any evidence type reaching **1000:1 odds against pathogenicity** is sufficient to classify a variant as **stand-alone Benign**
- Evidence with combined odds of **350:1 against** (equivalent to lower bound of Very Strong Benign evidence) is sufficient to classify a variant as **Likely Benign**

---

## Odds of Pathogenicity Reference

| Code Strength | Odds Range (Pathogenic) | Odds Range (Benign) |
|---------------|-------------------------|---------------------|
| Very Strong | ≥350 | ≤0.00285 |
| Strong | ≥18.70 to <350 | ≤0.05 to >0.00285 |
| Moderate | ≥4.30 to <18.70 | ≤0.23 to >0.05 |
| Supporting | ≥2.08 to <4.30 | ≤0.48 to >0.23 |
| No evidence | 1.00 to <2.08 | >0.48 to 1.00 |

---

## Appendices

### Appendix A: Odds of Pathogenicity Assignment

Designation of likelihood ratios (LRs) to ACMG/AMP rule code strengths were based on LR ranges proposed as consistent with ACMG/AMP qualitative rule strengths for future classification in a Bayesian framework (Tavtigian et al 2018, PMID: 29300386). The benign category intervals are calculated as inverse odds to the pathogenic category intervals. These odds ranges assume a global prior probability of pathogenicity of 0.10.

### Appendix B: Multifactorial Likelihood Analysis

The current multifactorial likelihood model for BRCA1/2 variant interpretation allows for inclusion of LRs for pathogenicity estimated from clinical data:
- Co-segregation with disease
- Co-occurrence with a pathogenic variant in the same gene
- Reported family history
- Breast tumor pathology
- Case-control data

**Key references:**
- Goldgar et al 2004, PMID: 15290653
- Thompson et al 2005, PMID: 12900794
- Easton et al 2007, PMID: 17924331
- Spurdle et al 2014, PMID: 25857409
- de la Hoya et al 2016, PMID: 27008870
- Parsons et al 2019, PMID: 31131967
- Li et al 2020, PMID: 31853058

### Appendix C: Gene Structure and Functional Domains

**BRCA1 Exon Structure:**
- Exons are sequentially numbered to match the exon descriptions of the MANE transcript (NM_007294.4)
- Legacy exon numbering (GenBank U14680.1) has exon 4 missing due to a correction after initial description

**BRCA2 Exon Structure:**
- 27 exons
- Large exon 11 contains multiple functional regions

### Appendix D: PVS1 Decision Tree

See separate **Table 4** Excel file for comprehensive PVS1 and PM5_PTC codes by exon.

### Appendix E: mRNA and Functional Assay Specifications

See **Figures 1B and 1C** in the main specification document and **Table 9** (separate Excel file) for functional assay data.

### Appendix F: Case-Control Studies (PS4)

Requirements for PS4 application:
- p-value ≤0.05
- OR ≥4 (lower confidence interval excludes 2.0)
- Ethnicity and country-matched datasets

### Appendix G: Population Frequency Thresholds

| Criterion | Threshold | Strength |
|-----------|-----------|----------|
| BA1 | >0.001 (0.1%) | Stand-alone |
| BS1 | >0.0001 (0.01%) | Strong |
| BS1_Supporting | >0.00002 to ≤0.0001 | Supporting |
| PM2_Supporting | Absent from gnomAD | Supporting |

**Quality control requirements:**
- Read depth ≥20 (BA1, BS1) or ≥25 (PM2)
- Exclude data failing quality control filter
- Do not apply PM2 for indels

### Appendix H: Fanconi Anemia (PM3/BS2)

**BRCA1-related FA:** FANCS
**BRCA2-related FA:** FANCD1

See Tables 6 and 8 for point-based scoring systems.

### Appendix I: Co-segregation Analysis (PP1/BS4)

Recommended tool: **COOL** (http://bjfenglab.org/)

LR thresholds are derived from the Bayesian framework (Tavtigian et al 2018).

### Appendix J: Bioinformatic Predictions (PP3/BP4/BP1)

**Splicing Predictions:**
- SpliceAI ≥0.2: PP3 applicable
- SpliceAI ≤0.1: BP4/BP1 applicable

**Missense Predictions (BayesDel no AF):**
| Gene | PP3 (Impact) | BP4 (No Impact) |
|------|--------------|-----------------|
| BRCA1 | ≥0.28 | ≤0.15 |
| BRCA2 | ≥0.30 | ≤0.18 |

**Donor/Acceptor Motif Positions (GT-AG introns):**
- Donor: Last 3 bases of exon + 6 intronic nucleotides
- Acceptor: First base of exon + 20 upstream nucleotides

### Appendix K: Clinical Evidence (PP4/BP5)

Combined clinical LR calculated by multiplying individual LRs. See Table 7 for example applications.

---

## Special Notes

### Reduced Penetrance Variants

The proposed classification criteria are set up to differentiate germline high-risk variants (associated with cancer risk equivalent to classical pathogenic variants known or predicted to encode a premature termination codon) from variants with low/no risk.

**Important:** "Reduced" penetrance variants associated with moderate risk of cancer may not be reliably distinguished as risk-associated pathogenic variants. Example: BRCA1 c.5096G>A p.Arg1699Gln (Spurdle et al 2012, PMID: 22889855).

Variants with discordances across multiple evidence types will be highlighted for further study using approaches aimed at investigating reduced penetrance and/or partial effect on function/splicing.

---

## Reference PMIDs

| Citation | PMID |
|----------|------|
| Richards et al., 2015 (ACMG/AMP Guidelines) | 25741868 |
| Tavtigian et al., 2018 (Bayesian Framework) | 29300386 |
| Tavtigian et al., 2020 (Point System) | 32720330 |
| Goldgar et al., 2004 | 15290653 |
| Thompson et al., 2005 | 12900794 |
| Easton et al., 2007 | 17924331 |
| Plon et al., 2008 (IARC 5-tier) | 18951446 |
| Tavtigian et al., 2008 | 8972225 |
| Spurdle et al., 2012 | 22889855 |
| Spurdle et al., 2014 | 25857409 |
| de la Hoya et al., 2016 | 27008870 |
| Vallee et al., 2016 | 26913838 |
| Parsons et al., 2019 | 31131967 |
| Li et al., 2020 | 31853058 |

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.2 | 2024-11-18 | Current version |

---

*This document was compiled from ClinGen ENIGMA VCEP specifications V1.2 (2024-11-18). For the most current version, supplementary tables, and searchable lookup files (Tables 4 and 9), please refer to the original VCEP documentation.*
