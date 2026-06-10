# ACADVL Variant Interpretation Guidelines

## ClinGen ACADVL Expert Panel Specifications to the ACMG/AMP Variant Interpretation Guidelines

**Version:** 2.1.0
**Released:** September 4, 2025
**Affiliation:** ACADVL VCEP
**Type:** Richards et al., 2015 - Combining rules

---

## Gene and Disease Information

| Parameter | Value |
|-----------|-------|
| **Gene** | ACADVL (HGNC:92) |
| **HGNC Name** | Acyl-CoA dehydrogenase very long chain |
| **Transcript** | NM_000018.4 (MANE Select) |
| **Disease** | Very long chain acyl-CoA dehydrogenase deficiency (MONDO:0008723) |
| **Mode of Inheritance** | Autosomal recessive |
| **Protein** | 655 amino acid precursor protein with 40 amino acid N-terminal target sequence |

---

## Overview

Loss of function is a known mechanism for VLCAD Deficiency. The major isoform, NM_000018.4, encodes a 655 amino acid precursor protein that contains a 40 amino acid N-terminal target sequence that is removed during uptake (Aoyama et al., 1995; PMID: 7668252). In a joint project between NCBI and EMBL-EBI (MANE), NM_000018.4 was designated as the most relevant transcript.

---

## Pathogenic Criteria

### PVS1 - Null Variant

**Original ACMG Summary:** Null variant (nonsense, frameshift, canonical +/-1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.

#### PVS1 Specifications for ACADVL

Loss of function is a known mechanism for VLCAD Deficiency. Specifications are based on published guidance for assigning strength of evidence for PVS1 (Abou Tayoun et al., 2018; PMID: 30192042).

**Important Note:** PVS1 cannot be combined with PM1.

#### Nonsense or Frameshift Variants

- **NMD Predicted** (termination before c.1778): Apply **PVS1** if exon is present in biologically-relevant transcript
- **NMD Not Predicted** (termination at c.1778 or after): Apply **PVS1_Moderate** if variant removes <10% of protein

**Caution:** Use caution when interpreting LOF variants at the 3' end of the gene. NMD is not predicted if the variant is in the last exon (exon 20) or in the last 50 nucleotides of the penultimate exon (exon 19).

#### Canonical Splice Site Variants (+1, +2, -1, -2)

All donor/acceptor sites follow the GT/AG rule, **except** for the donor splice site of intron 8, which begins with GC.

**Critical:** PVS1 should NOT be applied for variants in the splice donor site of intron 8 since the impact of GC donor splice sites is not well understood.

| Splice Site Impact | Reading Frame | NMD | PVS1 Strength |
|-------------------|---------------|-----|---------------|
| Exon skipping disrupts reading frame | Out of frame | Predicted | PVS1 |
| Exon skipping disrupts reading frame | Out of frame | Not predicted (exon 20) | PVS1_Moderate |
| Exon skipping preserves reading frame | In frame | N/A | See exon table below |

**Splice Site Predictions:**
- For +1 or +2 GT donor splice site variants: the exon immediately 5' of the variant is predicted to be skipped
- For -1 or -2 AG acceptor splice site variants: the exon immediately 3' of the variant is predicted to be skipped

#### Exon Skipping Table

| Exon | First Coding nt | Last Coding nt | Length (nts) | Frame | PVS1 Strength | Rationale |
|------|-----------------|----------------|--------------|-------|---------------|-----------|
| 1 | 1 | 62 | 62 | Out of frame | PVS1 | Fs, PTC, NMD |
| 2 | 63 | 138 | 76 | Out of frame | PVS1 | Fs, PTC, NMD |
| 3 | 139 | 204 | 66 | In frame | PVS1_Moderate | 33 aa, ~3.4% of total |
| 4 | 205 | 277 | 73 | Out of frame | PVS1 | Fs, PTC, NMD |
| 5 | 278 | 342 | 65 | Out of frame | PVS1 | Fs, PTC, NMD |
| 6 | 343 | 477 | 135 | In frame | PVS1_Moderate | 45 aa, ~6.9% of total |
| 7 | 478 | 622 | 145 | Out of frame | PVS1 | Fs, PTC, NMD |
| 8 | 623 | 752 | 130 | Out of frame | PVS1 | Fs, PTC, NMD |
| 9 | 753 | 878 | 126 | In frame | PVS1_Moderate | 42 aa, ~6.4% of total |
| 10 | 879 | 1077 | 199 | Out of frame | PVS1 | Fs, PTC, NMD |
| 11 | 1078 | 1182 | 105 | In frame | PVS1_Moderate | 35 aa, ~5.3% of total |
| 12 | 1183 | 1269 | 87 | In frame | PVS1_Moderate | 29 aa, ~4.4% of total |
| 13 | 1270 | 1332 | 63 | In frame | PVS1_Moderate | 21 aa, ~3.2% of total |
| 14 | 1333 | 1434 | 102 | In frame | PVS1_Moderate | 34 aa, ~5.2% of total |
| 15 | 1435 | 1532 | 98 | Out of frame | PVS1 | Fs, PTC, NMD |
| 16 | 1533 | 1605 | 73 | Out of frame | PVS1 | Fs, PTC, NMD |
| 17 | 1606 | 1678 | 73 | Out of frame | PVS1 | Fs, PTC, NMD |
| 18 | 1679 | 1751 | 73 | Out of frame | PVS1 | Fs, PTC, NMD |
| 19 | 1752 | 1827 | 76 | Out of frame | PVS1 | Fs, PTC, NMD |
| 20 | 1828 | 1968 | 141 | In frame | PVS1_Moderate | 47 aa, ~7.2% of total |

*Abbreviations: Fs=frameshift, PTC=premature termination codon, NMD=nonsense mediated decay*

#### Initiation Codon Variants

The next in-frame methionine is at position 6 (on transcript NM_000018). However, the first 40 amino acids comprise the leader sequence in the precursor peptide and are important for proper localization of the protein. Therefore, initiator codon variants will meet **PVS1_Strong**.

#### Deletion Variants

| Deletion Type | Condition | PVS1 Strength |
|---------------|-----------|---------------|
| Full gene deletion | N/A | PVS1 |
| Single/multi-exon deletion | Disrupts reading frame, NMD predicted | PVS1 |
| Single/multi-exon deletion | Disrupts reading frame, NMD NOT predicted, >10% protein removed | PVS1_Strong |
| Single/multi-exon deletion | Disrupts reading frame, NMD NOT predicted, <10% protein removed | PVS1_Moderate |
| Single/multi-exon deletion | Preserves reading frame, critical region (Exons 1-2, 10, 13-15, 18) | PVS1_Strong |
| Single/multi-exon deletion | Preserves reading frame, non-critical region, <10% protein removed | PVS1_Moderate |

**Critical Exons for Protein Function:** Exons 1-2, 8, 10, 13-15, 18

#### Duplication Variants

| Duplication Type | PVS1 Strength |
|------------------|---------------|
| Proven in tandem, reading frame disrupted, NMD predicted | PVS1 |
| Presumed in tandem, reading frame presumed disrupted, NMD predicted | PVS1_Strong |
| Proven not in tandem | N/A |
| No or unknown impact on reading frame and NMD | N/A |

#### PVS1 (RNA) - mRNA Assay Evidence

Well-established in vitro or in vivo functional studies supportive of a damaging effect as measured by effect on mRNA transcript profile (mRNA assay only). Apply as PVS1 (RNA) at appropriate strength based on the decision tree.

---

### PS1 - Same Amino Acid Change

**Original ACMG Summary:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.

#### Missense Variants

| Strength | Criteria |
|----------|----------|
| **PS1_Strong** | Same amino acid change as a previously established pathogenic variant classified using ACADVL specifications without application of PS1, regardless of nucleotide change **OR** Same amino acid change as ≥2 previously established likely pathogenic variants classified using ACADVL specifications without application of PS1 |
| **PS1_Moderate** | Same amino acid change as a previously established likely pathogenic variant classified using ACADVL specifications without application of PS1, regardless of nucleotide change |

**Caveat:** Assess the possibility that the variant may act directly through the DNA change (e.g., through splicing disruption as assessed by at least computational analysis) instead of through the amino acid change.

#### Splice Variants

PS1 can be applied at varying strengths for splice variants, in conjunction with either PP3 or PVS1. PS1 strength depends on:
- Location of the variant under assessment (within or outside the +/- 1,2 dinucleotide positions)
- Location of the previously classified variant (within or outside the +/- 1,2 dinucleotide position)

Refer to Table 2 in Walker et al., 2023 (PMID: 37352859) for specific combinations.

---

### PS2 - De Novo

**Original ACMG Summary:** De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.

**ACADVL Specification:** Not Applicable

---

### PS3 - Functional Studies (Damaging)

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.

#### PS3 Specifications

Functional evidence from non-patient derived material with only a single variant best reflects the variant-level data. Apply patient-derived evidence in PP4.

**Valid Assays for ACADVL:**
- Enzyme activity assays
- Total protein production (Western blot)
- Protein stability (pulse-chase)
- Dimer formation
- Transcript production

#### PS3/BS3 Flowchart Application

**Step 1: Define Disease Mechanism**
- Loss of function is the established mechanism for VLCAD deficiency

**Step 2: Evaluate Applicability**
- Does the general class of assay model pathogenesis/disease mechanism?
  - NO → Do not use PS3/BS3
  - YES → Proceed to Step 3

**Step 3: Evaluate Validity of Specific Assays**

| Controls Present? | Assay Validated? | Max Strength |
|-------------------|------------------|--------------|
| Basic controls (normal/abnormal) AND multiple replicates | Variant controls used (known P/LP or B/LB) | Proceed to Step 4 |
| Basic controls (normal/abnormal) AND multiple replicates | No variant controls | Max PS3_Supporting |
| No basic controls or replicates | Assay historically validated OR kit with defined metrics | Max PS3_Supporting |
| No basic controls or replicates | Assay not validated | Do not use PS3/BS3 |

**Step 4: Apply Evidence to Individual Variant**

| Statistical Analysis | Variant Controls | Max Strength |
|---------------------|------------------|--------------|
| Sufficient to calculate OddsPath | N/A | PS3_Very_Strong (correlate to OddsPath) |
| Not sufficient | ≤10 total controls | PS3_Supporting |
| Not sufficient | ≥11 total controls | PS3_Moderate |

#### Approved Functional Assays

| Assay Type | Material | Proposed Strength | Key References |
|------------|----------|-------------------|----------------|
| Palmitoyl-CoA oxidation | Transfected CHO cells | Supporting | Souri 1996 (PMID: 8554073) |
| Enzyme activity C16-CoA | Bacterial expression | Supporting | Goetzman 2007 (PMID: 17374501) |
| Palmitoyl-CoA oxidation | Transfected VLCAD null fibroblasts | Supporting | Takusa 2002 (PMID: 11914034), Watanabe 2000 (PMID: 10790204) |
| Palmitoyl-CoA oxidation | Baculovirus expression | Supporting | Souri 1998 (PMID: 9461620) |
| Palmitoyl-CoA oxidation | Transfected HEK293/fibroblasts | Supporting | D'Annibale 2022 (PMID: 35218577) |
| FAO/dimer formation | HEK293 transfection | Supporting | Chen 2020 (PMID: 33150772) |
| Western blot (protein) | Various transfection systems | Supporting | Multiple references |
| Pulse-chase (stability) | Transfected CHO cells | Supporting | Souri 1996 (PMID: 8554073) |

**Important:** If an enzyme activity assay has >20% activity, it cannot be weighted above PS3_Supporting regardless of flowchart results.

**Note:** Assays performed in patient cells should be counted under PP4, not PS3.

---

### PS4 - Prevalence in Affected Individuals

**Original ACMG Summary:** The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.

**ACADVL Specification:** Not Applicable

---

### PM1 - Critical Functional Domain

**Original ACMG Summary:** Located in a mutational hot spot and/or critical and well-established functional domain without benign variation.

#### PM1 Critical Regions (Moderate Strength)

| Protein Location | Functional Evidence | References |
|------------------|---------------------|------------|
| p.1-40 | Mitochondrial signal peptide | PMIDs: 18227065*, 20060901 |
| p.214-223 | Nucleotide/substrate binding | PMIDs: 18227065*, 20060901 |
| p.249-251 | Nucleotide/substrate binding | PMIDs: 18227065*, 20060901 |
| p.R326 | CpG dinucleotide | PMID: 9973285 |
| p.381-382 | FAD binding and salt-bridge interaction | PMID: 20060901 |
| p.R429 | CpG dinucleotide | PMID: 9973285 |
| p.E441 | Adjacent to FAD binding, on dimer formation loop | PMID: 20060901 |
| p.R459 | Dimerization | PMID: 14517516 |
| p.460-466 | Nucleotide/substrate binding | PMIDs: 18227065*, 20060901 |
| p.481-516 | Membrane binding | PMIDs: 18227065*, 20060901 |
| p.562 | Nucleotide/substrate binding | PMIDs: 18227065*, 20060901 |

*Protein described in mature protein nomenclature without signal peptide; add 40 amino acids to reach HGVS numbering*

**Note:** Curators may seek approval from the expert panel for identifying additional hotspots or critical regions as discovered in literature searches.

---

### PM2 - Absent from Controls

**Original ACMG Summary:** Absent from controls (or at extremely low frequency if recessive) in population databases.

#### PM2_Supporting

Variants with a highest population minor allele frequency (MAF) **<0.001 (0.1%)** in any continental population with >2000 alleles in gnomAD will meet PM2_Supporting.

**Calculation Parameters:**
- Prevalence: 1:100,000
- Allelic Contribution: 0.2
- Genetic Contribution: 1
- Penetrance: 0.75 (to allow for mild VLCADD that may develop in adulthood)
- Multiplied by 1.5 to account for mildly pathogenic variants being present in carriers

**Note:** It is acceptable for an ACADVL variant to be present in controls because VLCAD deficiency is a recessive condition. If homozygous variants are present in population databases, the number should be noted and discussed with an expert.

---

### PM3 - Detected in Trans

**Original ACMG Summary:** For recessive disorders, detected in trans with a pathogenic variant.

#### PM3 Point System

| Classification of Other Variant | Confirmed in Trans | Phase Unknown |
|---------------------------------|-------------------|---------------|
| Pathogenic or Likely pathogenic | 1.0 point | 0.5 (P) / 0.25 (LP) |
| Homozygous occurrence (Max = 1.0) | 0.5 point | N/A |

#### PM3 Strength by Points

| PM3 Strength | Points Required |
|--------------|-----------------|
| PM3_Supporting | ≥0.5 and <1.0 |
| PM3 (Moderate) | ≥1.0 and <2.0 |
| PM3_Strong | ≥2.0 and <4.0 |
| PM3_Very_Strong | ≥4.0 |

#### PM3 Requirements

1. Details of the cDNA change must be used to describe any variants used as evidence. Amino acid change alone is not sufficient.
2. Probands must also meet PP4 criteria to be counted.
3. If more than one case has the same genotype and variants are not confirmed in trans, only one case should be used to avoid overcounting.
4. If variants are confirmed in trans, multiple individuals with the same genotype can be counted if reports do not represent the same case.
5. Use these variant interpretation guidelines to classify the "other variant" to determine appropriate points.

**Confirming Trans:**
- Requires parental testing OR appropriate molecular method (such as cloning each allele separately followed by sequencing)
- Parental testing is NOT required for homozygous cases

---

### PM4 - Protein Length Change

**Original ACMG Summary:** Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

**ACADVL Specification:** Moderate strength. Follow recommendations as outlined in ACMG/AMP guidelines and/or Sequence Variant Interpretation working group.

---

### PM5 - Novel Missense at Same Residue

**Original ACMG Summary:** Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.

#### PM5 Point System

Each additional variant at the same codon: LP = 0.5 points, P = 1.0 point (as classified by the ACADVL VCEP)

| PM5 Strength | Points Required |
|--------------|-----------------|
| PM5_Strong | ≥2.0 |
| PM5_Moderate | ≥1.0 and <2.0 |
| PM5_Supporting | 0.5 |

**Note:** PM5 cannot be applied with PM1. Apply criteria with the highest strength. If both are applicable at the same strength, apply PM5 as it is amino acid specific.

**Caveat:** Assess the possibility that the variant may act directly through the DNA change (e.g., through splicing disruption) instead of through the amino acid change.

---

### PM6 - Assumed De Novo

**Original ACMG Summary:** Assumed de novo, but without confirmation of paternity and maternity.

**ACADVL Specification:** Moderate strength. No change from original ACMG guidelines.

---

### PP1 - Co-Segregation

**Original ACMG Summary:** Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.

#### PP1 Specifications for Autosomal Recessive

**Definitions:**
- **Affected segregations** = # affected individuals in the family with the variants - 1 (proband not counted)
- **Unaffected segregations** = unaffected family members at risk who are either wild-type for both variants or heterozygous carrier for a single variant
- Carrier parents DO NOT count as unaffected segregations

#### PP1 Strength by LOD Score

| Strength | Likelihood | LOD Score |
|----------|------------|-----------|
| Supporting (4:1) | 4:1 | ≥0.60 and <1.20 |
| Moderate (16:1) | 16:1 | ≥1.20 and <1.50 |
| Strong (32:1) | 32:1 | ≥1.50 |

#### LOD Score Reference Table (Autosomal Recessive)

| Affected Seg. | 0 Unaff. | 1 Unaff. | 2 Unaff. | 3 Unaff. | 4 Unaff. | 5 Unaff. |
|---------------|----------|----------|----------|----------|----------|----------|
| 0 | 0 | 0.12 | 0.25 | 0.37 | 0.5 | 0.62 |
| 1 | 0.6 | 0.73 | 0.85 | 0.98 | 1.1 | 1.23 |
| 2 | 1.2 | 1.33 | 1.45 | 1.58 | 1.7 | 1.83 |
| 3 | 1.81 | 1.93 | 2.06 | 2.18 | 2.31 | 2.43 |
| 4 | 2.41 | 2.53 | 2.66 | 2.78 | 2.91 | 3.03 |
| 5 | 3.01 | 3.14 | 3.26 | 3.39 | 3.51 | 3.63 |

*Full table extends to 10 affected and 10 unaffected segregations*

**Special Scenarios:** Individuals other than siblings may be counted in families where one parent is affected, in large families with multiple branches, or in consanguineous families.

---

### PP2 - Low Rate of Benign Missense

**Original ACMG Summary:** Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.

**ACADVL Specification:** Not Applicable. There are benign and pathogenic missense variants in ACADVL.

---

### PP3 - Computational Evidence (Damaging)

**Original ACMG Summary:** Multiple lines of computational evidence support a deleterious effect on the gene or gene product.

#### PP3 Specifications

**Missense Variants:**
- REVEL score **>0.75** meets PP3_Supporting

**In-frame Deletions/Insertions:**
- Use Mutation Taster

**Non-canonical Splice Site Variants:**
- Use SpliceAI
- PP3 can be applied if SpliceAI "high score" (Δ Score ≥ 0.5 "confidently predicted splice variants")
- Exclude any results with Δ Score ≤ 0.2 from consideration of pathogenicity

**Cryptic Splice Site Creation:**
- If a new splice site is predicted to be generated with Δ Score ≥ 0.5, this rule can be applied

**Note:** Do not apply this rule for canonical splice site changes meeting PVS1.

---

### PP4 - Patient Phenotype

**Original ACMG Summary:** Patient's phenotype or family history is highly specific for a disease with a single genetic etiology.

#### PP4 Point System for ACADVL

| Description of Evidence | Points |
|------------------------|--------|
| VLCAD enzyme activity (β-Oxidation Flux) ≤20% of normal | 2 |
| VLCAD enzyme activity (β-Oxidation Flux) 21-27% of normal | 1 |
| Assertion of reduced VLCAD activity without specific levels | 1 |
| NBS C14:1 Levels from 0.8 - 0.99 μM | 1 (a) |
| Assertion of abnormal NBS "consistent with VLCADD" without specific levels | 0.5 |
| Follow-Up Plasma Acylcarnitine analysis "consistent with VLCADD" without specific levels | 0.5 (b) |

**Notes:**
- (a) To reach PP4_Moderate using NBS data, C14:1 Levels must be ≥1.0 μM
- (b) If NBS C14:1 Levels are ≥1.0 μM, this can be upweighted to 1 point

#### PP4 Strength by Points

| PP4 Strength | Points Required |
|--------------|-----------------|
| PP4_Supporting | 1.0 point |
| PP4_Moderate | 2.0 points |

**Abnormal Tests Consistent with VLCAD Deficiency:**
- Deficient VLCAD enzyme activity in patient cells (leukocytes, fibroblasts, liver, heart, skeletal muscle, or amniocytes)
- Abnormal C14:1 acylcarnitine values from newborn screening (NBS)
- Abnormal acylcarnitine values from follow-up plasma analysis

---

### PP5 - Reputable Source (Pathogenic)

**Original ACMG Summary:** Reputable source recently reports variant as pathogenic, but the evidence is not available to the laboratory to perform an independent evaluation.

**ACADVL Specification:** Not Applicable. This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PMID: 29543229).

---

## Benign Criteria

### BA1 - Stand Alone Benign (Population Frequency)

**Original ACMG Summary:** Allele frequency is above 5% in population databases.

#### BA1 Specification

Variants with a highest population minor allele frequency (MAF) **≥0.007 (0.7%)** in any continental population with >2000 alleles in gnomAD will meet BA1.

**Calculation Parameters:**
- Prevalence: 1:30,000
- Allelic Contribution: 1
- Genetic Contribution: 1
- Penetrance: 0.75

---

### BS1 - Allele Frequency Greater than Expected

**Original ACMG Summary:** Allele frequency is greater than expected for disorder.

#### BS1 Specification (Strong)

Variants with a highest population minor allele frequency (MAF) **≥0.0035 (0.35%)** in any continental population with >2000 alleles in gnomAD will meet BS1.

**Calculation Parameters:**
- Prevalence: 1:30,000
- Allelic Contribution: 0.5
- Genetic Contribution: 1
- Penetrance: 0.75

---

### BS2 - Observed in Healthy Individual

**Original ACMG Summary:** Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

**ACADVL Specification:** Not Applicable

---

### BS3 - Functional Studies (No Damaging Effect)

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

#### BS3 Specifications

Apply criteria at the level determined by validation parameters using the PS3/BS3 flowchart.

**Valid Assays:**
- Enzyme activity assays
- Total protein production
- Protein stability
- Dimer formation
- Transcript production

| BS3 Strength | Application |
|--------------|-------------|
| BS3_Strong | Per flowchart validation |
| BS3_Moderate | Per flowchart validation |
| BS3_Supporting | Per flowchart validation |

---

### BS4 - Lack of Segregation

**Original ACMG Summary:** Lack of segregation in affected members of a family.

**ACADVL Specification:** Strong strength. Follow recommendations as outlined in ACMG/AMP guidelines and/or Sequence Variant Interpretation working group.

---

### BP1 - Missense in Truncating Gene

**Original ACMG Summary:** Missense variant in a gene for which primarily truncating variants are known to cause disease.

**ACADVL Specification:** Not Applicable. There are known pathogenic missense variants in ACADVL.

---

### BP2 - Observed in Trans/Cis

**Original ACMG Summary:** Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder or observed in cis with a pathogenic variant in any inheritance pattern.

**ACADVL Specification:** Supporting strength. No change from original ACMG guidelines.

---

### BP3 - In-frame in Repetitive Region

**Original ACMG Summary:** In-frame deletions/insertions in a repetitive region without a known function.

**ACADVL Specification:** Not Applicable. There are no known repetitive regions without known function in ACADVL.

---

### BP4 - Computational Evidence (No Impact)

**Original ACMG Summary:** Multiple lines of computational evidence suggest no impact on gene or gene product.

#### BP4 Specifications

**Missense Variants:**
- REVEL score **<0.5** meets BP4_Supporting

**In-frame Deletions/Insertions:**
- Use Mutation Taster

**Non-canonical Splice Site Variants:**
- Use SpliceAI
- BP4 can be applied if Δ Score ≤ 0.1
- Do NOT apply this rule if there is evidence for creation of a cryptic splice site

**Note:** BP4 can be used with BP7 code.

---

### BP5 - Alternate Molecular Basis

**Original ACMG Summary:** Variant found in a case with an alternate molecular basis for disease.

**ACADVL Specification:** Not Applicable. An individual could be a carrier of a pathogenic variant in ACADVL and have another disorder.

---

### BP6 - Reputable Source (Benign)

**Original ACMG Summary:** Reputable source recently reports variant as benign, but the evidence is not available to the laboratory to perform an independent evaluation.

**ACADVL Specification:** Not Applicable. This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PMID: 29543229).

---

### BP7 - Synonymous/Intronic Variant

**Original ACMG Summary:** A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.

#### BP7 Specifications

| Strength | Criteria |
|----------|----------|
| **BP7_Strong** | In vitro evidence (RNA) of no splicing impact for intronic or synonymous variants irrespective of position and predicted impact on splicing |
| **BP7_Supporting** | Synonymous variant for which splicing prediction algorithms predict no impact to splice consensus sequence nor creation of new splice site AND nucleotide is not highly conserved |

**Additional Application:**
- Can be used for intronic variants that fall outside the minimal splice region (≥+7 or ≤-21)
- Can be used with BP4 code

---

## Rules for Combining Criteria

### Pathogenic Classification

| Evidence Combination |
|---------------------|
| 1 Very Strong AND ≥1 Strong |
| 1 Very Strong AND ≥2 Moderate |
| 1 Very Strong AND 1 Moderate AND 1 Supporting |
| 1 Very Strong AND ≥2 Supporting |
| ≥2 Strong |
| 1 Strong AND ≥3 Moderate |
| 1 Strong AND 2 Moderate AND ≥2 Supporting |
| 1 Strong AND 1 Moderate AND ≥4 Supporting |

### Likely Pathogenic Classification

| Evidence Combination |
|---------------------|
| 1 Very Strong AND 1 Moderate |
| 1 Strong AND 1 Moderate |
| 1 Strong AND ≥2 Supporting |
| ≥3 Moderate |
| 2 Moderate AND ≥2 Supporting |
| 1 Moderate AND ≥4 Supporting |
| 1 Strong AND 2 Moderate |

### Benign Classification

| Evidence Combination |
|---------------------|
| ≥2 Strong |
| 1 Stand Alone (BA1) |

### Likely Benign Classification

| Evidence Combination |
|---------------------|
| 1 Strong AND 1 Supporting |
| ≥2 Supporting |

---

## Quick Reference Summary

### Criteria Not Applicable for ACADVL

| Criterion | Reason |
|-----------|--------|
| PS2 | De novo not applicable for AR conditions |
| PS4 | Not applicable |
| PP2 | Benign and pathogenic missense variants exist |
| PP5 | Not recommended by ClinGen SVI |
| BS2 | Not applicable |
| BP1 | Pathogenic missense variants exist |
| BP3 | No repetitive regions without function |
| BP5 | Carriers can have other disorders |
| BP6 | Not recommended by ClinGen SVI |

### Key Thresholds

| Parameter | Threshold |
|-----------|-----------|
| BA1 (Stand Alone Benign) | MAF ≥0.7% |
| BS1 (Benign Strong) | MAF ≥0.35% |
| PM2 (Supporting) | MAF <0.1% |
| PP3 REVEL (Damaging) | >0.75 |
| BP4 REVEL (Benign) | <0.5 |
| SpliceAI (Damaging) | Δ Score ≥0.5 |
| SpliceAI (Benign) | Δ Score ≤0.1 |
| SpliceAI (Exclude) | Δ Score ≤0.2 |

### Special Considerations

1. **PVS1 and PM1 cannot be combined**
2. **PM5 and PM1 cannot be combined** - apply the criterion with highest strength; if equal, use PM5
3. **Intron 8 splice donor site** - PVS1 should not be applied due to GC donor splice site
4. **Patient-derived functional data** should be counted under PP4, not PS3
5. **Enzyme activity >20%** cannot support PS3 above Supporting strength

---

## References

1. Abou Tayoun AN, et al. (2018) PMID: 30192042 - PVS1 Guidance
2. Aoyama T, et al. (1995) PMID: 7668252 - VLCAD protein characterization
3. Walker S, et al. (2023) PMID: 37352859 - Splice variant guidance
4. Jaganathan K, et al. (2019) PMID: 30661751 - SpliceAI
5. Houdayer C, et al. (2012) PMID: 22505045 - Splicing predictions
6. Tang R, et al. (2016) PMID: 27313609 - Splicing predictions
7. ClinGen SVI VCEP Review Committee (2018) PMID: 29543229 - PP5/BP6 recommendations
8. Gobin-Limballe S, et al. (2010) PMID: 20060901 - VLCAD functional domains
9. Miller N, et al. (1999) PMID: 9973285 - CpG dinucleotide hotspots
10. Souri M, et al. (2006) PMID: 18227065 - VLCAD structure/function
11. Andresen BS, et al. (1999) PMID: 14517516 - Dimerization

---

*Document compiled from ClinGen ACADVL VCEP specifications v2.1.0 and associated supplementary materials.*
