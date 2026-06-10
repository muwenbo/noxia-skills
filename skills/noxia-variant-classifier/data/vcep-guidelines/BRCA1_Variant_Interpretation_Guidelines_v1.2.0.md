# ClinGen ENIGMA BRCA1 and BRCA2 VCEP Variant Interpretation Guidelines for BRCA1

**Version:** 1.2.0
**Released:** January 9, 2025
**Affiliation:** ENIGMA BRCA1 and BRCA2 Variant Curation Expert Panel (VCEP)
**Based on:** Richards et al., 2015 ACMG/AMP Guidelines; Tavtigian et al., 2018 Bayesian Framework

---

## Gene Information

| Attribute | Value |
|-----------|-------|
| **Gene** | BRCA1 (HGNC:1100) |
| **HGNC Name** | BRCA1 DNA repair associated |
| **Transcript** | NM_007294.4 |
| **Genomic Reference** | NG_005905.2 (LRG 292) |
| **Disease** | BRCA1-related cancer predisposition (MONDO:0700268) |
| **Inheritance** | Autosomal dominant |
| **Recessive Phenotype** | Fanconi Anemia, complementation group S (FANCS) |

### Clinically Important Functional Domains (BRCA1)

| Domain | Amino Acid Range | Clinical Importance |
|--------|------------------|---------------------|
| **RING domain** | aa 2-101 | Clinically important |
| **Coiled-coil domain** | aa 1391-1424 | Potentially clinically important |
| **BRCT repeats** | aa 1650-1857 | Clinically important |

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
   - [PM5 - Protein Termination Codon (PTC)](#pm5---protein-termination-codon-ptc)
   - [PM6 - De Novo (Assumed)](#pm6---de-novo-assumed)
   - [PP1 - Co-segregation](#pp1---co-segregation)
   - [PP2 - Missense in Constrained Gene](#pp2---missense-in-constrained-gene)
   - [PP3 - Computational Evidence](#pp3---computational-evidence)
   - [PP4 - Combined Clinical Evidence](#pp4---combined-clinical-evidence)
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

**Original ACMG Summary:** Null variant (nonsense, frameshift, canonical +/-1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.

**Caveats:**
- Beware of genes where LOF is not a known disease mechanism
- Use caution interpreting LOF variants at the extreme 3' end of a gene
- Use caution with splice variants predicted to lead to exon skipping but leave the remainder of the protein intact
- Use caution in the presence of multiple transcripts

**VCEP Specifications:**

In alignment with SVI recommendations for PVS1 code application, evidence strength and description has been separated for different variant types. Apply according to PVS1 flowchart, which considers knowledge of clinically important functional domains.

For predicted protein termination codon (PTC) variants, apply with exon-specific weights derived for the PM5_PTC code (See Appendix D for details).

**See Specifications Table 4** (provided as a separate searchable Excel file) for a comprehensive summary of codes applicable for all variants considered against the BRCA1 PVS1 decision trees (initiation, nonsense/frameshift, deletion, duplication, splice site (donor/acceptor +/-1,2)) - organized by exon.

#### Strength Levels

| Strength | Criteria |
|----------|----------|
| **Very Strong** | Null variant in a gene where LOF is a known mechanism of disease. Apply at appropriate strength according to PVS1 flowchart. Also applies to mRNA assay data showing damaging effect - apply as PVS1 (RNA) at appropriate strength. |
| **Strong** | Apply per PVS1 flowchart based on variant position and type. For mRNA assays showing loss of function, apply as PVS1_Strong (RNA). |
| **Moderate** | Apply per PVS1 flowchart based on variant position and type. For mRNA assays showing partial loss of function, apply as PVS1_Moderate (RNA). |
| **Supporting** | Apply per PVS1 flowchart based on variant position and type. For mRNA assays showing minor impact, apply as PVS1_Supporting (RNA). |

#### PVS1 (RNA) - mRNA Assay Evidence

For splicing data, see **Specifications Figure 1B** for the process to apply codes based on:
- Location and predicted bioinformatic impact of the variant
- Adaptive weighting according to assay methodology
- Proportion of functional transcript retained

---

### PS1 - Same Amino Acid Change

**Original ACMG Summary:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.

**Caveat:** Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:**

For both missense and splicing scenarios, (Likely) Pathogenic variant classification should be assigned using VCEP specifications.

For application of PS1 for splicing predictions, see **Specifications Table 5**:
- The predicted event of the VUA must precisely match the predicted event of the known (likely) pathogenic variant
- The strength of the prediction for the VUA must be of similar or higher strength than the known variant
- For exonic variants, consider predicted or proven functional effect of missense substitutions

#### Strength Levels

| Strength | Criteria |
|----------|----------|
| **Strong** | Apply PS1 for predicted missense substitutions where a previously classified **pathogenic** variant is considered to act via protein change (no confirmed or predicted effect on mRNA splicing, SpliceAI ≤0.1). Also apply for exonic and intronic variants with same predicted impact on splicing as a previously classified **pathogenic** variant. |
| **Moderate** | Apply PS1_Moderate for predicted missense substitutions where a previously classified **likely pathogenic** variant is considered to act via protein change (SpliceAI ≤0.1). Also apply for variants with same predicted impact on splicing as a (likely) pathogenic variant with moderate confidence. |
| **Supporting** | Apply PS1_Supporting for exonic and intronic variants with same predicted impact on splicing as a previously classified (likely) pathogenic variant with lower confidence. |

#### PS1 Code Weights for Splicing Predictions (Table 5)

| VUA Position | Baseline Code | Reference Variant Position | PS1 with P variant | PS1 with LP variant |
|--------------|---------------|---------------------------|-------------------|---------------------|
| Outside donor/acceptor ±1,2 | PP3 | Same nucleotide | PS1 | PS1_Moderate |
| Outside donor/acceptor ±1,2 | PP3 | Within same donor/acceptor motif (including ±1,2) | PS1_Moderate | PS1_Supporting |
| At donor/acceptor ±1,2 | PVS1 | Within same donor/acceptor dinucleotide | PS1_Supporting | N/A |
| At donor/acceptor ±1,2 | PVS1 | Within same motif, outside dinucleotide | PS1_Supporting | PS1_Supporting |
| At donor/acceptor ±1,2 | PVS1_Strong/Moderate/Supporting | Within same dinucleotide | PS1 | N/A |
| At donor/acceptor ±1,2 | PVS1_Strong/Moderate/Supporting | Within same motif, outside dinucleotide | PS1_Moderate | PS1_Supporting |

---

### PS2 - De Novo (Confirmed)

**Original ACMG Summary:** De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.

**VCEP Specifications:** **Not Applicable**

**Comments:** BRCA1/2-related cancers occur relatively commonly. No information to calibrate the predictive capacity of de novo occurrences.

---

### PS3 - Functional Studies

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.

**VCEP Specifications:**

See **Specifications Figure 1C** for simplified flowcharts to advise application of codes for functional data, in context of variant type and location within a (potentially) clinically important functional domain.

**Do not apply** when conflicting results are present from well-established assays with sufficient controls, which cannot be explained by experimental design.

See **Specifications Table 9** (provided as a separate Excel file) for PS3 and BS3 code recommendations and rationale for code application of published functional assay data that has been calibrated.

#### Strength Levels

| Strength | Criteria |
|----------|----------|
| **Strong** | Well-established in vitro or in vivo functional studies supportive of a damaging effect. Apply PS3 for assays measuring effect via protein only OR mRNA and protein combined. See Table 9 for code recommendations from calibrated published assays. |

#### mRNA Assay Only

For assays measuring effect via mRNA only:
- Apply as **PVS1_Variable Weight (RNA)** at appropriate strength
- See **Specifications Figure 1B** and Appendix E for details

#### Approved Functional Assays

Calibrated functional assays include:
- HDR (Homology-Directed Repair) assays
- SGE (Saturation Genome Editing) assays
- Transcription activation assays
- BARD1 binding assays
- Various cell-based functional assays

See **Specifications Table 9** for complete list of calibrated assays and variant-specific results.

---

### PS4 - Prevalence in Affected

**Original ACMG Summary:** The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.

**VCEP Specifications:**

Case dataset should be ethnicity and country-matched to control dataset. If case-control LR estimates are available for a given dataset, these should be used in preference to case-control OR data, under code PP4 (or BP5, if appropriate).

**Do not use** Proband Counting as originally described.

#### Strength Level

| Strength | Criteria |
|----------|----------|
| **Strong** | Case-control studies with p-value ≤0.05 AND OR ≥4 (lower confidence interval excludes 2.0). See Appendix F for details. |

---

### PM1 - Mutational Hot Spot

**Original ACMG Summary:** Located in a mutational hot spot and/or critical and well-established functional domain without benign variation.

**VCEP Specifications:** **Not Applicable**

**Comments:** Considered as component of bioinformatic analysis (PP3/BP4).

---

### PM2 - Absent from Controls

**Original ACMG Summary:** Absent from controls (or at extremely low frequency if recessive) in population databases.

**VCEP Specifications:**

- Observation of a variant only once in a gnomAD outbred population is not informative
- Do not apply for insertion, deletion, or delins variants
- Do not apply if read depth <25 at region around the variant

#### Strength Level

| Strength | Criteria |
|----------|----------|
| **Supporting** | Absent from controls in an outbred population from gnomAD v2.1 (non-cancer, exome only subset) and gnomAD v3.1 (non-cancer). Region around the variant must have average read depth ≥25. |

---

### PM3 - In Trans with Pathogenic

**Original ACMG Summary:** For recessive disorders, detected in trans with a pathogenic variant.

**VCEP Specifications:**

Apply for patient with phenotype consistent with BRCA1-related Fanconi Anemia (FANCS), and co-occurrent variants in the same gene.

**Phenotype is considered consistent with BRCA1-related FA if:**

**(i)** Increased chromosome breakage (DEB, MMC, or spontaneous) AND at least one clinical feature indicative of BRCA1-related FA, categorized under: physical features, pathology and laboratory findings, cancer diagnosis ≤5yr.

**(ii)** Result unknown for chromosome breakage, AND at least two clinical features indicative of BRCA1-related FA under at least two of the three categories: physical features, pathology and laboratory findings, cancer diagnosis ≤5yr.

**Additional stipulations:**
- Co-occurrent P or LP variant should be assigned classification using VCEP specifications
- Variant under assessment must be sufficiently rare (not meeting a benign population evidence code)
- For related individuals, score only most severe presentation

#### PM3 Point System (Table 6)

| Proband Presentation | P or LP in trans or homozygote | Phase unknown |
|----------------------|-------------------------------|---------------|
| Phenotype consistent with BRCA1-related FA | 2 points | 1 point |

#### PM3 Evidence Strength Thresholds

| Total Points | Strength Level |
|--------------|----------------|
| 1 | PM3_Supporting |
| 2 | PM3 (Moderate) |
| ≥4 | PM3_Strong |

---

### PM4 - Protein Length Changes

**Original ACMG Summary:** Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

**VCEP Specifications:** **Not Applicable**

**Comments:** Considered as component of bioinformatic analysis (PP3/BP4).

---

### PM5 - Protein Termination Codon (PTC)

**Original ACMG Summary:** Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.

**VCEP Specifications (Repurposed):**

**PM5_PTC**: Protein termination codon (PTC) variant in an exon where a different proven pathogenic PTC variant has been seen before.

- Only applied to genomic PTC changes (not splicing)
- Weight determined by exon where the termination codon occurs (may not be the same exon as the variant position)
- Use to justify additional weight for PTC variants annotated as PVS1

See **Specifications Table 4** for PM5_PTC codes applicable per exon.

#### Strength Levels

| Strength | Criteria |
|----------|----------|
| **Strong** | PTC variant in an exon with strong evidence of pathogenic PTC variants |
| **Moderate** | PTC variant in an exon with moderate evidence of pathogenic PTC variants |
| **Supporting** | PTC variant in an exon with supporting evidence of pathogenic PTC variants |

---

### PM6 - De Novo (Assumed)

**Original ACMG Summary:** Assumed de novo, but without confirmation of paternity and maternity.

**VCEP Specifications:** **Not Applicable**

**Comments:** BRCA1/2-related cancers occur relatively commonly. No information to calibrate the predictive capacity of de novo occurrences.

---

### PP1 - Co-segregation

**Original ACMG Summary:** Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.

**VCEP Specifications:**

Recommend use of online tools:
- **COOL**: http://bjfenglab.org/
- **CAL-Leiden**: https://bioexp.net/cosegregation/

**Stipulation:** To apply code as Pathogenic Very Strong, VUS should have bioinformatically predicted (or experimentally proven) effect on protein or mRNA splicing. If co-segregation score is from a single family, or several families from an isolated population, assess the possibility of a different causative pathogenic variant.

**Note:** LR >0.48 and <2.08 doesn't provide supporting evidence in either direction (PP1 and BS4 not applicable).

#### PP1 Thresholds

| Strength | Likelihood Ratio |
|----------|-----------------|
| **Supporting** | LR ≥2.08:1 |
| **Moderate** | LR ≥4.3:1 |
| **Strong** | LR ≥18.7:1 |
| **Very Strong** | LR ≥350:1 |

---

### PP2 - Missense in Constrained Gene

**Original ACMG Summary:** Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.

**VCEP Specifications:** **Not Applicable**

**Comments:** High frequency of benign missense variants.

---

### PP3 - Computational Evidence

**Original ACMG Summary:** Multiple lines of computational evidence support a deleterious effect on the gene or gene product.

**VCEP Specifications:**

See **Specifications Figure 1A** for process to apply codes according to variant type, location, and predicted bioinformatic impact.

**Do not apply PP3 if PVS1 is met at any strength.**

#### Application Criteria

| Variant Type | Criteria |
|--------------|----------|
| **Missense/in-frame variants** | Inside a (potentially) clinically important functional domain AND predicted impact via protein change (BayesDel no-AF score ≥0.28 for BRCA1) |
| **Silent/missense/in-frame** | Predicted splicing impact (SpliceAI ≥0.2), irrespective of location in clinically important functional domain |
| **Intronic variants** | Outside of donor and acceptor ±1,2 positions AND predicted splicing impact (SpliceAI ≥0.2) |

#### Bioinformatic Thresholds for BRCA1

| Tool | PP3 Threshold (Pathogenic) | BP4 Threshold (Benign) |
|------|---------------------------|------------------------|
| **BayesDel no-AF** | ≥0.28 | ≤0.15 |
| **SpliceAI** | ≥0.2 (PP3) | ≤0.1 (BP4) |

---

### PP4 - Combined Clinical Evidence

**Original ACMG Summary:** Patient's phenotype or family history is highly specific for a disease with a single genetic etiology.

**VCEP Specifications:**

Breast cancer is very common and has a high degree of genetic heterogeneity. Use ONLY to capture combined LR towards pathogenicity, based on multifactorial likelihood clinical data.

Published data points may include:
- Co-segregation with disease
- Co-occurrence with a pathogenic variant in the same gene
- Reported family history
- Breast tumor pathology
- Case-control data

**Note:** Combined LR >0.48 and <2.08 doesn't provide supporting evidence in either direction (PP4 and BP5 not applicable).

#### PP4 Strength Thresholds

| Strength | Combined LR |
|----------|-------------|
| **Supporting** | LR ≥2.08:1 |
| **Moderate** | LR ≥4.3:1 |
| **Strong** | LR ≥18.7:1 |
| **Very Strong** | LR ≥350:1 |

See **Specifications Table 7** for example applications.

---

### PP5 - Reputable Source

**Original ACMG Summary:** Reputable source recently reports variant as pathogenic, but the evidence is not available to the laboratory to perform an independent evaluation.

**VCEP Specifications:** **Not Applicable**

This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PMID: 29543229).

---

## Benign Criteria

### BA1 - Allele Frequency >0.1%

**Original ACMG Summary:** Allele frequency is above 5% in population databases.

**VCEP Specifications:**

Apply based on maximum filter allele frequency observed in a gnomAD non-founder population, considering exome and genome data separately.

- Do not apply if read depth <20
- Do not apply to well-established pathogenic founder variants

#### Threshold

| Strength | Criteria |
|----------|----------|
| **Stand Alone** | Filter allele frequency (FAF) >0.1% (FAF >0.001) in gnomAD v2.1 (non-cancer, exome only subset) and/or gnomAD v3.1 (non-cancer), non-founder population(s). |

---

### BS1 - Frequency Greater Than Expected

**Original ACMG Summary:** Allele frequency is greater than expected for disorder.

**VCEP Specifications:**

Apply based on maximum filter allele frequency in a gnomAD non-founder population, considering exome and genome data separately.

- Do not apply if read depth <20
- Do not apply to well-established pathogenic founder variants

#### Strength Levels

| Strength | Criteria |
|----------|----------|
| **Strong** | FAF >0.01% (FAF >0.0001) in gnomAD v2.1 (non-cancer, exome only) and/or gnomAD v3.1 (non-cancer), non-founder population(s). |
| **Supporting** | FAF >0.002% (FAF >0.00002) and ≤0.01% (FAF ≤0.0001) in gnomAD non-founder population(s). |

---

### BS2 - Observed in Healthy Adult

**Original ACMG Summary:** Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder.

**VCEP Specifications:**

Applied in absence of features of recessive disease, namely Fanconi Anemia phenotype.

**Stipulations:**
- VUA should not be bioinformatically predicted (or experimentally proven) to have a clinically important effect on protein or mRNA splicing
- Co-occurrent P or LP variant should be assigned classification using VCEP specifications
- Apply only for phenotyped individuals from clinical or research cohorts
- NOT to be applied for data used to assign frequency-based codes

#### BS2 Point System (Table 8)

| Proband Presentation | VUA in trans with P or LP | Homozygote | Phase unknown with P/LP |
|---------------------|--------------------------|------------|------------------------|
| Cancer onset >50y or unaffected >50y | 4 points | 2 points | 1 point |
| Cancer onset 40-50y or unaffected 40-50y | 2 points | 1 point | 0.5 points |

#### BS2 Evidence Strength Thresholds

| Total Points | Strength Level |
|--------------|----------------|
| 1 | BS2_Supporting |
| 2 | BS2_Moderate |
| ≥4 | BS2 (Strong) |

---

### BS3 - Functional Studies (No Effect)

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

**VCEP Specifications:**

See **Specifications Figure 1C** for simplified flowcharts to advise application of codes for functional data, in context of variant type and location within a (potentially) clinically important functional domain.

**Do not apply** when conflicting results are present from well-established assays with sufficient controls, which cannot be explained by experimental design.

See **Specifications Table 9** for BS3 code recommendations from calibrated published assays.

#### Strength Level

| Strength | Criteria |
|----------|----------|
| **Strong** | Well-established in vitro or in vivo functional studies show no damaging effect on protein function. Assay measures effect via protein only OR mRNA and protein combined. |

#### mRNA Assay Only

For mRNA assays showing no damaging effect:
- Apply as **BP7_Strong (RNA)** for intronic and silent variants
- Apply as **BP7_Strong (RNA)** for missense/in-frame variants outside a clinically important functional domain
- Missense variants inside a clinically important functional domain must meet BS3 to be eligible for BP7_Strong (RNA)

---

### BS4 - Lack of Segregation

**Original ACMG Summary:** Lack of segregation in affected members of a family.

**VCEP Specifications:**

Recommend use of online tools:
- **COOL**: http://bjfenglab.org/
- **CAL-Leiden**: https://bioexp.net/cosegregation/

**Note:** LR >0.48 and <2.08 doesn't provide supporting evidence in either direction (PP1 and BS4 not applicable).

**Stipulation:** To apply code as Benign Very Strong, assess the possibility of bi-linearity to explain negative co-segregation.

#### BS4 Thresholds

| Strength | Likelihood Ratio |
|----------|-----------------|
| **Supporting** | LR ≤0.48:1 |
| **Moderate** | LR ≤0.23:1 |
| **Strong** | LR ≤0.05:1 |
| **Very Strong** | LR ≤0.00285:1 |

---

### BP1-BP7 - Benign Supporting

| Criterion | Status | Specification |
|-----------|--------|---------------|
| **BP1** | **Strength Modified (Strong)** | Apply BP1_Strong for silent substitution, missense, or in-frame insertion/deletion/delins variants **outside** a (potentially) clinically important functional domain AND no splicing predicted (SpliceAI ≤0.1). Missense prediction not applicable. |
| **BP2** | **Not Applicable** | Applied only in the context of BS2. |
| **BP3** | **Not Applicable** | Captured by bioinformatic tool prediction and domain analysis. |
| **BP4** | **Applicable** | Apply for: (1) Missense/in-frame variants inside a clinically important functional domain with no predicted impact via protein change or splicing (BayesDel no-AF ≤0.15 AND SpliceAI ≤0.1); (2) Silent variant inside a clinically important functional domain, if no predicted impact via splicing (SpliceAI ≤0.1); (3) Intronic variants outside donor/acceptor ±1,2 positions AND no predicted splicing (SpliceAI ≤0.1). |
| **BP5** | **Variable Weight** | Use ONLY to capture combined LR against pathogenicity, based on multifactorial likelihood clinical data. NOT applicable for co-observation (cases with pathogenic variants in two or more different breast-ovarian cancer risk genes). See LR thresholds below. |
| **BP6** | **Not Applicable** | Not for use as recommended by ClinGen SVI VCEP Review Committee (PMID: 29543229). |
| **BP7** | **Applicable** | Apply for: (1) Silent variant inside a clinically important functional domain, IF BP4 met; (2) Intronic variants located outside conserved donor or acceptor motif positions (at or beyond positions +7/-21), IF BP4 met. |
| **BP7_Strong (RNA)** | **Applicable** | For mRNA assays showing no damaging effect. Apply for intronic, silent, and missense/in-frame variants located outside a clinically important functional domain. |

#### BP5 Strength Thresholds

| Strength | Combined LR |
|----------|-------------|
| **Supporting** | LR ≤0.48:1 |
| **Moderate** | LR ≤0.23:1 |
| **Strong** | LR ≤0.05:1 |
| **Very Strong** | LR ≤0.00285:1 |

---

## Rules for Combining Criteria

### Approach 1: Adapted ACMG-AMP (Default)

This represents a minor adaptation of the traditional ACMG-AMP classification system, incorporating results from the Bayesian Framework analysis of Tavtigian et al 2018 (PMID: 29300386).

### Pathogenic Classification

| Criteria Combination |
|---------------------|
| 1 Very Strong AND (≥1 Strong OR ≥1 Moderate OR ≥2 Supporting) |
| 1 Strong AND (≥3 Moderate OR 2 Moderate & ≥2 Supporting OR 1 Moderate & ≥4 Supporting) |
| 2 Strong AND (≥1 Moderate OR ≥2 Supporting) |
| ≥3 Strong |

### Likely Pathogenic Classification

| Criteria Combination |
|---------------------|
| 1 Very Strong AND 1 Supporting |
| 2 Strong |
| 1 Strong AND 1-2 Moderate |
| 1 Strong AND ≥2 Supporting |
| ≥3 Moderate |
| 2 Moderate AND ≥2 Supporting |
| 1 Moderate AND ≥4 Supporting |

### Benign Classification

| Criteria Combination |
|---------------------|
| 1 Stand Alone (BA1) |
| 1 Very Strong AND (1 Strong OR 1 Moderate OR 1 Supporting) |
| ≥2 Strong |
| 1 Strong AND (2 Moderate OR 1 Moderate & ≥1 Supporting OR ≥3 Supporting) |

### Likely Benign Classification

| Criteria Combination |
|---------------------|
| 1 Strong AND (1 Supporting OR 1 Moderate) |
| 1 Moderate AND 1 Supporting |
| ≥2 Supporting |
| 1 Strong, if based on multiple evidence types* |

*Likely Benign can be assigned based on one Strong Benign code if multiple evidence types contribute to the code assigned (e.g., BS4 with multiple likelihood ratios; BP1_Strong combining variant type, position, and prediction).

### Approach 2: Point System (For Contradictory Evidence)

When both benign and pathogenic criteria are met, use the point system proposed by Tavtigian et al 2020 (PMID: 32720330).

#### Point Values

| Strength | Pathogenic | Benign |
|----------|------------|--------|
| Very Strong | +8 | -8 |
| Strong | +4 | -4 |
| Moderate | +2 | -2 |
| Supporting | +1 | -1 |
| Indeterminate | 0 | 0 |

#### Classification Thresholds

| Point Range | Classification |
|-------------|----------------|
| ≤-7 | Benign |
| -6 to -2 | Likely Benign |
| -1 to 5 | Uncertain Significance |
| 6 to 9 | Likely Pathogenic |
| ≥10 | Pathogenic |

**Caution:** Use clinical judgement when classifying variants with significant conflicting evidence (more than one code in conflict). The ENIGMA BRCA1 and BRCA2 VCEP requires a discussion before assigning a classification to such variants.

---

## Appendices

### Appendix A: Code Strength Assignment Based on Odds

| Code Strength | Odds Range (Pathogenic) | Odds Range (Benign) |
|---------------|------------------------|---------------------|
| Very Strong | ≥350 | ≤0.00285 |
| Strong | ≥18.70 to <350 | ≤0.05 to >0.00285 |
| Moderate | ≥4.30 to <18.70 | ≤0.23 to >0.05 |
| Supporting | ≥2.08 to <4.30 | ≤0.48 to >0.23 |
| No Evidence | 1.00 to <2.08 | >0.48 to 1.00 |

Based on Tavtigian et al., 2018 (PMID: 29300386). These odds ranges assume a global prior probability of pathogenicity of 0.10.

### Appendix B: Population Frequency Thresholds Summary

| Criterion | Threshold | Strength | Dataset |
|-----------|-----------|----------|---------|
| BA1 | FAF >0.001 (0.1%) | Stand Alone | gnomAD v2.1/v3.1 non-cancer, non-founder |
| BS1 | FAF >0.0001 (0.01%) | Strong | gnomAD v2.1/v3.1 non-cancer, non-founder |
| BS1_Supporting | FAF >0.00002 (0.002%) to ≤0.0001 | Supporting | gnomAD v2.1/v3.1 non-cancer, non-founder |
| PM2_Supporting | Absent from controls, read depth ≥25 | Supporting | gnomAD v2.1/v3.1 non-cancer |

### Appendix C: Bioinformatic Prediction Thresholds

| Tool | PP3 Threshold | BP4 Threshold |
|------|---------------|---------------|
| **BayesDel no-AF (BRCA1)** | ≥0.28 | ≤0.15 |
| **SpliceAI (for PP3)** | ≥0.2 | - |
| **SpliceAI (for BP4)** | - | ≤0.1 |

### Appendix D: Fanconi Anemia Clinical Features

**Physical features (~75% of affected persons):**
- Prenatal and/or postnatal short stature
- Abnormal skin pigmentation (e.g., café au lait macules, hypo-pigmentation)
- Skeletal malformations (e.g., hypoplastic thumb, hypoplastic radius)
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
- Increased fetal hemoglobin

**Cancer diagnosis:** ≤5 years of age

### Appendix E: Reference PMIDs

| Topic | PMID |
|-------|------|
| ACMG/AMP Guidelines | 25741868 (Richards et al., 2015) |
| Bayesian Framework | 29300386 (Tavtigian et al., 2018) |
| Point System | 32720330 (Tavtigian et al., 2020) |
| IARC 5-tier Classification | 18951446 (Plon et al., 2008) |
| Multifactorial Likelihood | 15290653 (Goldgar et al., 2004) |
| BRCA1/2 Classification | 17924331 (Easton et al., 2007) |
| PP5/BP6 Deprecation | 29543229 |
| SpliceAI | 31343793 |

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.2.0 | 2025-01-09 | Added CAL-Leiden tool for co-segregation; clarified LR thresholds; reworded PM3 population criteria; added PMIDs to Table 9; corrected typos; clarified PM2_Supporting, PTC code for frameshift variants, mRNA data interpretation, SpliceAI, PP3/PVS1, PS1 criteria; updated PVS1 weight for splice sites |
| 1.1.0 | 2024-11-18 | Previous release (V1.2 specifications document) |

---

## Important Notes

1. **Reference Sequences:**
   - Coding DNA reference: NG_005905.2 (LRG 292)
   - Transcript: NM_007294.4 (MANE transcript)
   - Exon numbering follows MANE transcript (differs from legacy GenBank U14680.1 numbering)

2. **Reduced Penetrance Variants:** The proposed classification criteria are set up to differentiate germline high-risk variants from variants with low/no risk. "Reduced" penetrance variants associated with moderate risk of cancer may not be reliably distinguished as risk-associated pathogenic variants (e.g., BRCA1 c.5096G>A p.Arg1699Gln, PMID: 22889855).

3. **Conflicting Evidence:** Variants with discordances across multiple evidence types will be highlighted for further study using approaches aimed at investigating reduced penetrance and/or partial effect on function/splicing.

---

*This document was compiled from ClinGen ENIGMA BRCA1 and BRCA2 VCEP specifications (Version 1.2.0). For the most current version, please refer to the ClinGen website.*
