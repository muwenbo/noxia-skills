# CTLA4 Variant Interpretation Guidelines

## ClinGen Antibody Deficiencies Expert Panel Specifications to the ACMG/AMP Variant Interpretation Guidelines

**Version:** 1.0.0
**Released:** 11/19/2025
**Affiliation:** Antibody Deficiencies VCEP
**Expert Panel Page:** https://clinicalgenome.org/affiliation/50095/

---

## Table of Contents

1. [Gene and Disease Information](#1-gene-and-disease-information)
2. [CTLA4 Protein Structure and Domains](#2-ctla4-protein-structure-and-domains)
3. [Bayesian Point-Based Classification System](#3-bayesian-point-based-classification-system)
4. [Phenotype Scoring System](#4-phenotype-scoring-system)
5. [Pathogenic Criteria Specifications](#5-pathogenic-criteria-specifications)
6. [Benign Criteria Specifications](#6-benign-criteria-specifications)
7. [Functional Assays](#7-functional-assays)
8. [Population Frequency Thresholds](#8-population-frequency-thresholds)
9. [Special Considerations](#9-special-considerations)
10. [References](#10-references)

---

## 1. Gene and Disease Information

### Gene Information

| Attribute | Value |
|-----------|-------|
| **Gene Symbol** | CTLA4 |
| **HGNC ID** | HGNC:2505 |
| **HGNC Name** | Cytotoxic T-lymphocyte associated protein 4 |
| **Reference Transcript** | NM_005214.5 |
| **Alternative Transcript** | NM_001037631.3 (encodes soluble isoform) |

### Disease Information

| Attribute | Value |
|-----------|-------|
| **Disease** | Autoimmune lymphoproliferative syndrome due to CTLA4 haploinsufficiency |
| **MONDO ID** | MONDO:0014493 |
| **Mode of Inheritance** | Autosomal dominant |
| **Estimated Prevalence** | 1/200,000 – 1/1,000,000 |
| **Penetrance** | 45-70% (incomplete) |

### Disease Mechanism

Loss of function (LOF) is the established mechanism of disease. CTLA4 haploinsufficiency results in immune dysregulation characterized by autoimmunity, lymphoproliferation, and immunodeficiency.

---

## 2. CTLA4 Protein Structure and Domains

### Domain Organization

The CTLA4 protein consists of 223 amino acids organized into the following functional domains:

| Domain | Codon Range | Function |
|--------|-------------|----------|
| **Leader Peptide** | 1-35 | Signal sequence |
| **Ligand Binding Domain** | 36-151 | Extracellular domain for ligand interaction |
| **MYPPPY Motif** | 134-139 | Critical for interaction with CD80 and CD86 |
| **Transmembrane Domain** | 162-182 | Membrane anchoring |
| **Cytoplasmic Tail** | 187-223 | Regulates localization and internalization |

### Exon Organization

CTLA4 contains 4 exons:

```
Exon 1 ─── Exon 2 ─────────── Exon 3 ─── Exon 4
                    ↑
           Contains critical
           MYPPPY motif (134-139)
```

**Important Notes:**
- Exon 2 contains the critical MYPPPY motif (codons 134-139)
- Exon 3 is isoform-specific and is omitted from the alternative transcript NM_001037631.3 (soluble isoform)
- Similar clinical phenotypes are associated with null variants in exon 2 and exon 3

### Critical Functional Region

The **MYPPPY motif (residues 134-139)** is essential for CTLA4 function as it mediates interaction with ligands CD80 and CD86. Variants affecting this region are evaluated using **PM1_Moderate**.

---

## 3. Bayesian Point-Based Classification System

The Antibody Deficiencies VCEP adopts the Bayesian points scale for all criteria combinations (PMID: 29300386, PMID: 32720330).

### Evidence Strength Point Values

| Evidence Strength | Pathogenic Points | Benign Points |
|-------------------|-------------------|---------------|
| Indeterminate | 0 | 0 |
| Supporting | 1 | -1 |
| Moderate | 2 | -2 |
| Strong | 4 | -4 |
| Very Strong | 8 | -8 |

### Classification Categories

| Classification | Point Range |
|----------------|-------------|
| **Pathogenic** | ≥ 10 |
| **Likely Pathogenic** | 6 – 9 |
| **Uncertain Significance (VUS)** | 0 – 5 |
| **Likely Benign** | -1 to -6 |
| **Benign** | ≤ -7 |

---

## 4. Phenotype Scoring System

The phenotype scoring system is used for determining proband eligibility for PS4, PP4, PS2, PM6, PP1, and BS4 codes. Family members must score at least **6 phenotype points** to be considered affected.

### Clinical Criteria

| Phenotype Finding | Points |
|-------------------|--------|
| Sinopulmonary findings* | 4 |
| Non-infectious gastrointestinal or hepatobiliary disease** | 4 |
| Immune-mediated cytopenias*** | 2 |
| Nonmalignant lymphoproliferation**** | 2 |
| Severe, persistent, recurrent viral infections including skin warts | 2 |
| Immune-mediated skin and hair findings***** | 1 |
| Endocrinopathy | 1 |
| Severe, persistent, recurrent, atypical, opportunistic bacterial, mycobacterial or fungal infections | 1 |
| Neurological findings****** | 1 |
| Inflammatory findings (arthritis, vasculitis, recurrent fevers) | 1 |
| Lymphoma | 1 |

### Objective Criteria

| Laboratory/Pathology Finding | Points |
|------------------------------|--------|
| Hypogammaglobulinemia | 2 |
| Lymphopenia | 1 |
| Abnormal TBNK levels | 1 |
| Presence of autoantibodies | 1 |
| Defective antigen-specific immune responses | 1 |
| Histopathology findings of lymphocytic/granulomatous tissue infiltration | 1 |

### Detailed Phenotype Definitions

**\* Sinopulmonary findings** include:
- (A) Clinical history of: (1) recurrent sinopulmonary infections (sinusitis, otitis, bronchitis, pneumonia), (2) interstitial lung disease (lymphocytic or granulomatous), fibrotic lung disease, or lymphoid fibrotic lesions/nodules, (3) pulmonary hypertension
- (B) Abnormal PFTs
- (C) Abnormal imaging studies (GGOs, mediastinal LAD, interstitial thickening, bronchiectasis, consolidation)
- (D) Other indicators of respiratory insufficiency or failure (prolonged ICU stay, history of lung transplant)

**\*\* Non-infectious GI or hepatobiliary disease** includes: Enteropathy, hepatopathy, autoimmune hepatitis, inflammatory bowel disease, primary sclerosing cholangitis, enterocolitis, celiac disease, atrophic gastritis, lymphocytic/microscopic colitis, exocrine pancreatic insufficiency, pernicious anemia

**\*\*\* Autoimmune cytopenias** include: Thrombocytopenia, anemia, hemolytic anemia, neutropenia, Coombs/DAT positive (though autoantibody testing may be negative)

**\*\*\*\* Nonmalignant lymphoproliferation** includes: Lymphocytic infiltration, lymphadenopathy, splenomegaly, hepatosplenomegaly

**\*\*\*\*\* Skin findings** include: Eczema, atopic dermatitis, psoriasiform dermatitis, warts, alopecia, dermatitis, vitiligo, urticaria, lichenoid skin lesion

**\*\*\*\*\*\* Neurological findings** include:
- (1) Clinical findings: Seizures, aphasia, headaches, motor deficits, cerebellar ataxia, bowel/bladder involvement, bulbar involvement, or neurodevelopmental delay(s)
- (2) Imaging findings: White matter hyperintensities, leukoencephalopathy/leukodystrophy, deep brain involvement, cerebellar atrophy, demyelinating spinal cord lesions, or evidence of optic atrophy/neuritis

---

## 5. Pathogenic Criteria Specifications

### PVS1 – Null Variant

**Original ACMG Summary:** Null variant (nonsense, frameshift, canonical ±1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where LOF is a known mechanism of disease.

**VCEP Specification:** Use caution interpreting LOF variants at the extreme 3' end of the gene and with splice variants predicted to lead to exon skipping but leave the remainder of the protein intact.

#### PVS1 Strength Levels

| Strength | Points | Application |
|----------|--------|-------------|
| **Very Strong (PVS1)** | 8 | Truncating variants with NMD predicted (premature stop codon at codon 172 or lower) |
| **Strong (PVS1_Strong)** | 4 | Truncating variants in exon 3 with NMD NOT predicted (codon 173 or higher) |
| **Moderate (PVS1_Moderate)** | 2 | Nonsense/frameshift variants introducing premature stop between codons 202-223 (C-terminal truncation <10% of protein, NMD not predicted) |
| **Supporting (PVS1_Supporting)** | 1 | Initiation codon variants (no known alternative start codons; closest in-frame start codon at codon 38) |

#### PVS1 Decision Tree Summary

**For Nonsense/Frameshift Variants:**
- Predicted NMD (codon 2-172) + biologically relevant transcript → **PVS1**
- NOT predicted NMD (codon 173-223):
  - Critical region (MYPPPY motif) affected → **PVS1_Strong**
  - >10% protein removed → **PVS1_Strong**
  - <10% protein removed → **PVS1_Moderate**

**For Canonical Splice Site Variants (±1,2):**
- Exon skipping disrupts reading frame + NMD predicted → **PVS1**
- Exon skipping disrupts reading frame + NMD NOT predicted:
  - >10% protein removed → **PVS1_Strong**
  - <10% protein removed → Not applicable
- Exon skipping preserves reading frame:
  - Critical region affected → **PVS1_Strong**
  - >10% protein removed → **PVS1_Strong**

**For Deletions:**
- Full gene deletion → **PVS1**
- Single/multi-exon deletion disrupting frame + NMD predicted → **PVS1**
- Frame-disrupting deletion + NMD NOT predicted:
  - Critical region → **PVS1_Strong**
  - >10% protein removed → **PVS1_Strong**

**For Duplications:**
- Proven in tandem + frame disrupted + NMD predicted → **PVS1**
- Presumed in tandem + frame disrupted + NMD predicted → **PVS1_Strong**

**For Initiation Codon Variants:**
- No pathogenic variants upstream of closest in-frame start codon → **PVS1_Supporting**

#### Important PVS1 Caveats

- PP3 and PS3 are **mutually exclusive** with PVS1 at the very strong level to avoid over-weighing LOF evidence
- If a variant outside canonical splice sites has SpliceAI ≥0.2 and confirmed splicing disruption, evaluate PVS1 instead of PP3/PS3_Supporting

---

### PS1 – Same Amino Acid Change

**VCEP Specification:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.

| Strength | Points | Application |
|----------|--------|-------------|
| **Strong (PS1)** | 4 | Missense variant when comparison variant classified Pathogenic by VCEP without using PS1 |
| **Moderate (PS1_Moderate)** | 2 | Missense variant when comparison variant classified Likely Pathogenic by VCEP without using PS1 |
| **Supporting (PS1_Supporting)** | 1 | Splice variants with comparable variant classified P/LP by VCEP standards |

**Caveats:**
- Beware of changes that impact splicing rather than amino acid (use SpliceAI to verify)
- Splicing predictions should remain the same for WT and both mutant alleles

**For Splice Variants with PS1:**
- Located **outside** ±1,2 dinucleotide + SpliceAI ≥0.2 + comparable variant at same position classified P → **PS1** with PP3
- Located **within** ±1,2 dinucleotide + comparable variant in same donor/acceptor classified P → **PS1** with PVS1

---

### PS2 – De Novo (Confirmed)

**VCEP Specification:** De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.

#### De Novo Points Based on Phenotype Consistency

| Phenotypic Consistency | Confirmed de novo Points | Assumed de novo Points |
|------------------------|-------------------------|------------------------|
| Phenotype highly specific for gene (≥10 phenotype points, no biallelic LRBA) | 2 | 1 |
| Phenotype consistent but not highly specific (≥6 phenotype points, no biallelic LRBA) | 1 | 0.5 |
| Phenotype consistent but not highly specific AND high genetic heterogeneity (≥4 and <6 points) | 0.5 | 0.25 |
| Phenotype not consistent with gene | 0 | 0 |

#### PS2/PM6 Evidence Strength Thresholds

| Total de novo Points | Evidence Strength |
|---------------------|-------------------|
| 0.5 | Supporting (PS2_Supporting or PM6_Supporting) |
| 1 | Moderate (PS2_Moderate or PM6) |
| 2 | Strong (PS2 or PM6_Strong) |
| 4 | Very Strong (PS2_VeryStrong) |

*Maximum allowable value of 1 may contribute to overall score for assumed de novo with high genetic heterogeneity.

---

### PM6 – De Novo (Assumed)

**VCEP Specification:** De novo in a patient with disease and no family history; maternity and paternity not confirmed but assumed.

Uses the same phenotype-based point system as PS2, with reduced point values (see table above).

---

### PS3 – Functional Studies (Pathogenic)

**VCEP Specification:** Well-established in vitro or in vivo functional studies supportive of a damaging effect.

| Strength | Points | Application |
|----------|--------|-------------|
| **Strong (PS3)** | 4 | Abnormal result in approved assay with calculated OddsPath >18.7 |
| **Moderate (PS3_Moderate)** | 2 | Abnormal result in approved assay with minimum 11 total P and B variant controls |
| **Supporting (PS3_Supporting)** | 1 | Abnormal result in approved non-patient cell-based assay |

**Approved Assays for PS3_Supporting:**
1. CD80 or CD86 transendocytosis / soluble ligand uptake in non-patient cells
2. Cell surface expression of CTLA4 in non-patient cell lines
3. Protein localization / translocation in non-patient cell lines
4. In vitro T cell suppression by CTLA4 in non-patient cell lines

*Note: Patient cell-based assays are incorporated into PP4_Moderate instead.*

---

### PS4 – Case-Control Evidence

**VCEP Specification:** Prevalence of variant in affected individuals significantly increased compared to controls.

**Prerequisites:**
- Variant must NOT meet BS1 or BA1
- Probands with biallelic LRBA variants (LP/P or rare VUS) are excluded

| Strength | Points | Number of Probands Required |
|----------|--------|-----------------------------|
| **Strong (PS4)** | 4 | ≥4 independent probands |
| **Moderate (PS4_Moderate)** | 2 | 2-3 independent probands |
| **Supporting (PS4_Supporting)** | 1 | 1 proband |

**Proband Requirements (must meet ONE of the following):**
1. ≥6 phenotype points + LRBA genotyping confirms absence of biallelic LP/P variants (monoallelic LRBA variant tolerated)
2. ≥10 phenotype points (LRBA genotyping not required)

*The proband used for PS4 cannot be the same proband used for PP4.*

---

### PM1 – Critical Functional Domain

**VCEP Specification:** Located in a mutational hot spot and/or critical and well-established functional domain without benign variation.

| Strength | Points | Application |
|----------|--------|-------------|
| **Moderate (PM1)** | 2 | Variants in the MYPPPY domain (residues 134-139) |

- Not mutually exclusive with PM5
- Required for interaction with CD80 and CD86

---

### PM2 – Absence from Controls

**VCEP Specification:** Absent from controls (or at extremely low frequency).

| Strength | Points | Application |
|----------|--------|-------------|
| **Supporting (PM2_Supporting)** | 1 | Total allele frequency < 1.43 × 10⁻⁷ (0.000000143) in gnomAD v4.1.0 |

*Threshold based on prevalence 1/1,000,000, penetrance 70%, allelic heterogeneity 1, genetic heterogeneity 1.*

---

### PM3 – In Trans with Pathogenic Variant

**Not Applicable** – This code is specific to recessive disorders.

---

### PM4 – Protein Length Changes

**VCEP Specification:** Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

| Strength | Points | Application |
|----------|--------|-------------|
| **Moderate (PM4)** | 2 | In-frame deletion/insertion ≥2 amino acids with PhyloP ≥2.0 and SpliceAI <0.2 |

**Requirements:**
- In-frame deletion: ≥2 amino acids deleted, at least one deleted nucleotide highly conserved (PhyloP ≥2.0)
- In-frame insertion: ≥2 amino acids inserted, at least one adjacent amino acid highly conserved (PhyloP ≥2.0)
- SpliceAI score <0.2

**Caveats:**
- Mutually exclusive with PVS1 and PP3
- Can be used together with PM1
- Consider if region is polymorphic in healthy populations

---

### PM5 – Novel Missense at Same Residue

**VCEP Specification:** Missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.

| Strength | Points | Application |
|----------|--------|-------------|
| **Moderate (PM5)** | 2 | Comparison variant classified P/LP by VCEP without using PM5 |

**Requirements:**
- Do not apply if variant meets BS1 or BA1
- Not mutually exclusive with PM1
- Use SpliceAI to examine both variants for similar predicted effect (Δ score <0.2)

---

### PP1 – Co-segregation

**VCEP Specification:** Co-segregation with disease in multiple affected family members.

| Strength | Points | Meioses Required |
|----------|--------|-----------------|
| **Strong (PP1_Strong)** | 4 | ≥4 meioses |
| **Moderate (PP1_Moderate)** | 2 | ≥2 meioses |
| **Supporting (PP1)** | 1 | ≥1 meiosis (proband + affected relative) |

**Requirements:**
- Each family member must score ≥6 phenotype points to be considered affected
- Do not apply if variant meets BA1 or BS1 (common variants may segregate by chance)

---

### PP2 – Missense in Constrained Gene

**Not Applicable** – Analysis of CTLA4's evolutionary constraint (low missense Z-score) shows that some missense variation is tolerated.

---

### PP3 – Computational Evidence (Pathogenic)

**VCEP Specification:** Multiple lines of computational evidence support a deleterious effect.

| Strength | Points | Application |
|----------|--------|-------------|
| **Supporting (PP3)** | 1 | Missense with REVEL ≥0.75 AND CADD PHRED ≥20 |
| **Supporting (PP3)** | 1 | Non-canonical splice variants with SpliceAI Δ score ≥0.2 |

**Notes:**
- Requires agreement between REVEL and CADD for missense variants
- Mutually exclusive with PVS1 at very strong level

---

### PP4 – Phenotype Specificity

**VCEP Specification:** Patient's phenotype or family history is highly specific for a disease with a single genetic etiology.

| Strength | Points | Requirements |
|----------|--------|--------------|
| **Moderate (PP4_Moderate)** | 2 | ≥10 phenotype points + LRBA genotyping (no biallelic) + abnormal patient cell-based functional assay |
| **Supporting (PP4)** | 1 | ≥10 phenotype points + LRBA genotyping (no biallelic) |

**Patient Cell-Based Assays for PP4_Moderate:**
1. CD80-GFP transendocytosis to CTLA4-expressing patient Tregs or memory CD4+ T cells
2. Total expression of CTLA4 by patient Tregs and other T cells
3. Cell surface expression of CTLA4 by patient B cells or T cells

*The proband used for PP4 cannot be used for PS4.*
*Variant must not meet BS1 or BA1.*

---

### PP5 – Reputable Source Reports Pathogenic

**Not Applicable** – Not recommended by ClinGen SVI VCEP Review Committee (PMID: 29543229).

---

## 6. Benign Criteria Specifications

### BA1 – Population Frequency (Stand Alone)

**VCEP Specification:** Allele frequency above threshold for disease.

| Strength | Points | Threshold |
|----------|--------|-----------|
| **Stand Alone (BA1)** | N/A | GrpMax FAF ≥ 1.11 × 10⁻⁵ (0.0000111) in gnomAD v4.1.0 with ≥5 alleles total |

*Threshold based on prevalence 1/100,000, penetrance 45%, allelic heterogeneity 1, genetic heterogeneity 1.*

---

### BS1 – Greater Than Expected Frequency

**VCEP Specification:** Allele frequency is greater than expected for disorder.

| Strength | Points | Threshold |
|----------|--------|-----------|
| **Strong (BS1)** | -4 | GrpMax FAF ≥ 1.11 × 10⁻⁶ (0.00000111) in gnomAD v4.1.0 with ≥3 alleles total |

*If GrpMax FAF not listed, evaluate using maximum AF among five major continental populations (AFR, EAS, NFE, AMR, SAS) with ≥3 alleles total.*

*Threshold based on prevalence 1/500,000, penetrance 45%, allelic heterogeneity 1, genetic heterogeneity 0.5.*

---

### BS2 – Observed in Healthy Adult

**Not Applicable** – Due to incomplete penetrance (45-70%).

---

### BS3 – Functional Studies (Benign)

**VCEP Specification:** Well-established functional studies show no damaging effect on protein function or splicing.

| Strength | Points | Application |
|----------|--------|-------------|
| **Strong (BS3)** | -4 | Normal result in approved assay with calculated OddsPath <0.053 |
| **Moderate (BS3_Moderate)** | -2 | Normal result in approved assay with ≥11 total P and B variant controls |
| **Supporting (BS3_Supporting)** | -1 | Normal result in TWO different approved assays |

**Important:** A normal result in a single assay cannot be interpreted as normal CTLA4 function. BS3_Supporting requires **two different assays** showing normal results.

**Approved Assays (same as PS3):**
1. CD80/CD86 transendocytosis / soluble ligand uptake in non-patient cells
2. Cell surface expression of CTLA4 in non-patient cell lines
3. Protein localization / translocation in non-patient cell lines
4. In vitro T cell suppression in non-patient cell lines

---

### BS4 – Lack of Segregation

**VCEP Specification:** Lack of segregation in affected members of a family.

| Strength | Points | Application |
|----------|--------|-------------|
| **Strong (BS4)** | -4 | Lack of segregation in >1 affected family member |
| **Supporting (BS4_Supporting)** | -1 | Lack of segregation in 1 affected family member |

*Each family member must score ≥6 phenotype points to be considered affected.*

---

### BP1 – Missense in Truncating Gene

**Not Applicable** – Pathogenic CTLA4 variants are not limited to truncating variants; missense variants can also be pathogenic.

---

### BP2 – In Trans/Cis with Pathogenic Variant

**Not Applicable** – More applicable to large, polymorphic genes. Biallelic cases may exist for other IEI genes.

---

### BP3 – In-frame in Repetitive Region

**Not Applicable** – Repetitive regions of unknown function are not known within CTLA4.

---

### BP4 – Computational Evidence (Benign)

**VCEP Specification:** Multiple lines of computational evidence suggest no impact.

| Strength | Points | Application |
|----------|--------|-------------|
| **Supporting (BP4)** | -1 | Missense with REVEL <0.25 AND CADD PHRED <20 AND SpliceAI Δ <0.1 |
| **Supporting (BP4)** | -1 | Synonymous/intronic variants with SpliceAI Δ <0.1 |

---

### BP5 – Alternate Molecular Basis

**VCEP Specification:** Variant found in a case with an alternate molecular basis for disease.

| Strength | Points | Application |
|----------|--------|-------------|
| **Supporting (BP5)** | -1 | Two cases required with alternate molecular basis |

*Two cases required to mitigate concerns over relying on other groups' classifications of pathogenic variants in genes such as LRBA.*

---

### BP6 – Reputable Source Reports Benign

**Not Applicable** – Not recommended by ClinGen SVI VCEP Review Committee (PMID: 29543229).

---

### BP7 – Synonymous Variant

**VCEP Specification:** Synonymous variant for which splicing prediction algorithms predict no impact and nucleotide is not highly conserved.

| Strength | Points | Application |
|----------|--------|-------------|
| **Supporting (BP7)** | -1 | Apply only if BP4 is met |

**Requirements:**
- SpliceAI Δ score <0.1
- For intronic variants: located at or beyond positions +7/−21
- For synonymous exonic variants: located outside the first nucleotide or last 3 nucleotides of the exon

---

## 7. Functional Assays

### Approved Non-Patient Cell-Based Assays (PS3/BS3)

| Assay Type | Key References (PMIDs) |
|------------|------------------------|
| CD80/CD86 transendocytosis / soluble ligand uptake | 25329329, 25632005, 25367873, 27102614, 29375547, 15814706, 20870175 |
| Cell surface expression of CTLA4 | 25367873, 14578884, 29375547, 7559643, 25213377 |
| Protein localization / translocation | 7559643, 20870175, 27102614, 25367873, 29375547, 15814706 |
| In vitro T cell suppression | 29375547, 26478010, 25213377 |

### Approved Patient Cell-Based Assays (PP4_Moderate)

| Assay Type | Key References (PMIDs) |
|------------|------------------------|
| CD80-GFP transendocytosis to patient Tregs/memory CD4+ T cells | 25329329, 34111452, 28159733 |
| Total CTLA4 expression by patient Tregs/T cells | 25213377, 25329329 |
| Cell surface expression of CTLA4 by patient B/T cells | 25213377, 25329329, 34111452, 28159733 |

---

## 8. Population Frequency Thresholds

### Summary of Allele Frequency Thresholds

| Code | Threshold | Database | Minimum Alleles | Rationale |
|------|-----------|----------|-----------------|-----------|
| **BA1** | ≥1.11 × 10⁻⁵ | gnomAD v4.1.0 GrpMax FAF | 5 | Prevalence 1/100,000, Penetrance 45% |
| **BS1** | ≥1.11 × 10⁻⁶ | gnomAD v4.1.0 GrpMax FAF | 3 | Prevalence 1/500,000, Penetrance 45%, GH 0.5 |
| **PM2_Supporting** | <1.43 × 10⁻⁷ | gnomAD v4.1.0 Total AF | N/A | Prevalence 1/1,000,000, Penetrance 70% |

*GrpMax FAF = Group Maximum Filtering Allele Frequency*
*GH = Genetic Heterogeneity*

---

## 9. Special Considerations

### LRBA Considerations

LRBA deficiency causes a phenotypically overlapping condition. Consider the following:

- **Proband exclusion:** Probands with homozygous or compound heterozygous LRBA variants (rare VUS, LP, or P) are excluded from PS4/PP4 evaluation
- **Monoallelic LRBA variants** can be tolerated
- For probands with ≥6 phenotype points, LRBA genotyping is required unless they score ≥10 points

### Incomplete Penetrance

CTLA4 haploinsufficiency has incomplete penetrance (45-70%). This affects:
- BS2 is not applicable
- PP1/BS4 require ≥6 phenotype points to consider family members affected
- De novo evidence uses phenotype-based point system

### Isoform Considerations

- Reference transcript: **NM_005214.5** (full-length, membrane-bound)
- Alternative transcript: **NM_001037631.3** (soluble isoform, lacks exon 3)
- Similar clinical phenotypes are associated with null variants in both exon 2 and exon 3, despite exon 3 being omitted from the soluble isoform

### Criteria Exclusivity Rules

| Mutually Exclusive Pairs | Notes |
|-------------------------|-------|
| PVS1 + PP3 | At very strong level |
| PVS1 + PS3 | At very strong level |
| PM4 + PVS1 | |
| PM4 + PP3 | To avoid double-counting in silico data |

---

## 10. References

### Key Publications

1. **Richards S, et al. (2015)** Standards and guidelines for the interpretation of sequence variants. *Genet Med.* PMID: 25741868
2. **Tavtigian SV, et al. (2020)** Fitting a naturally scaled point system to the ACMG/AMP variant classification guidelines. *Hum Mutat.* PMID: 32720330
3. **Biesecker LG, Harrison SM (2018)** The ACMG/AMP reputable source criteria for the interpretation of sequence variants. *Genet Med.* PMID: 29543229
4. **Tayoun AN, et al. (2018)** Recommendations for interpreting the loss of function PVS1 ACMG/AMP variant criterion. *Hum Mutat.* PMID: 30192042
5. **Walker S, et al. (2023)** Using the ACMG/AMP framework to capture evidence related to predicted and observed impact on splicing. *Genet Med.* PMID: 37352859
6. **Brnich SE, et al. (2019)** Recommendations for application of the functional evidence PS3/BS3 criterion. *Genome Med.* PMID: 31892348
7. **Kuehn HS, et al. (2014)** Immune dysregulation in human subjects with heterozygous germline mutations in CTLA4. *Science.* PMID: 25329329
8. **Schwab C, et al. (2018)** Phenotype, penetrance, and treatment of 133 CTLA-4-insufficient subjects. *J Allergy Clin Immunol.* PMID: 29111214
9. **Schubert D, et al. (2014)** Autosomal dominant immune dysregulation syndrome in humans with CTLA4 mutations. *Nat Med.* PMID: 25329329

### Additional Resources

- **ClinGen Antibody Deficiencies Expert Panel:** https://clinicalgenome.org/affiliation/50095/
- **gnomAD v4.1.0:** https://gnomad.broadinstitute.org/
- **SpliceAI:** https://spliceailookup.broadinstitute.org/

---

## Document Information

| Field | Value |
|-------|-------|
| **Document Version** | 1.0.0 |
| **Based on ClinGen VCEP Version** | 1.0.0 |
| **Release Date** | 11/19/2025 |
| **Expert Panel** | ClinGen Antibody Deficiencies VCEP |
| **Gene** | CTLA4 (HGNC:2505) |
| **Reference Transcript** | NM_005214.5 |

---

*This document synthesizes the ClinGen Antibody Deficiencies Expert Panel specifications for CTLA4 variant interpretation. For the most current guidelines, please refer to the official ClinGen website.*
