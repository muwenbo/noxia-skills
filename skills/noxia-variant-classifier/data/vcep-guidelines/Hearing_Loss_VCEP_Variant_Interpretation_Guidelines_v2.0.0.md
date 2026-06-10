# ClinGen Hearing Loss VCEP Variant Interpretation Guidelines

**Version:** 2.0.0
**Released:** 3/30/2022
**Affiliation:** Hearing Loss VCEP (ClinGen Affiliation 50007)
**Based on:** Richards et al., 2015 ACMG/AMP Guidelines
**Related Publication:** PMID 30311386

---

## Summary of Changes from Version 1 (March 2022)

1. Removal of PM2 at moderate strength and use of the PM2 cutoff at supporting strength
2. Functional assay strength and evidence using the criteria from Brnich et al., including downgrading PS3 to supporting for all specified COCH assays
3. Removal of PP4 and PM1 specifications of genes that are outside of the HL VCEP defined scope

---

## Gene Information

| Gene | HGNC ID | HGNC Name | Transcript | Disease | MONDO ID | Inheritance |
|------|---------|-----------|------------|---------|----------|-------------|
| **CDH23** | HGNC:13733 | cadherin related 23 | NM_022124.6 | Usher syndrome; Nonsyndromic genetic deafness | MONDO:0019501; MONDO:0019497 | AR |
| **COCH** | HGNC:2180 | cochlin | NM_004086.3 | Nonsyndromic genetic deafness | MONDO:0019497 | AD |
| **GJB2** | HGNC:4284 | gap junction protein beta 2 | NM_004004.6 | Nonsyndromic genetic deafness | MONDO:0019497 | AR |
| **KCNQ4** | HGNC:6298 | potassium voltage-gated channel subfamily Q member 4 | NM_004700.4 | Nonsyndromic genetic deafness | MONDO:0019497 | AD |
| **MYO6** | HGNC:7605 | myosin VI | NM_004999.4 | Nonsyndromic genetic deafness | MONDO:0019497 | AD |
| **MYO7A** | HGNC:7606 | myosin VIIA | NM_000260.4 | Usher syndrome; Nonsyndromic genetic deafness | MONDO:0019501; MONDO:0019497 | AR |
| **SLC26A4** | HGNC:8818 | solute carrier family 26 member 4 | NM_000441.2 | Pendred syndrome | MONDO:0010134 | AR |
| **TECTA** | HGNC:11720 | tectorin alpha | NM_005422.4 | Nonsyndromic genetic deafness | MONDO:0019497 | AD; AR |
| **USH2A** | HGNC:12601 | usherin | NM_206933.4 | Usher syndrome | MONDO:0019501 | AR |

---

## Summary of Gene-Specific Rules

| Gene | Disease, Inheritance | PVS1 Applicable | PM1: Mutational Hot Spot | Functional Assays | PP4 Applicable |
|------|---------------------|-----------------|--------------------------|-------------------|----------------|
| CDH23 | Usher syndrome, AR | Yes | N/A | N/A | Yes |
| COCH | Nonsyndromic HL, AD | N/A | N/A | Localization, secretion, dimerization (IF/WB) | N/A |
| GJB2 | Nonsyndromic SNHL, AR | Yes | N/A | Electrical coupling assays, dye transfer assays | N/A |
| KCNQ4 | Nonsyndromic SNHL, AD | Yes | aa 271-292 (pore-forming region) | N/A | N/A |
| MYO6 | Nonsyndromic SNHL, AD | Yes | N/A | N/A | N/A |
| MYO7A | Usher syndrome, AR | Yes | N/A | N/A | Yes |
| SLC26A4 | Pendred syndrome, AR | Yes | N/A | Radio isotope and fluorescence assays | Yes |
| TECTA | Nonsyndromic SNHL, AD/AR | Yes (AR only) | N/A | N/A | N/A |
| USH2A | Usher syndrome, AR | Yes | N/A | N/A | Yes |

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

**Caveats:**
- Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7)
- Use caution interpreting LOF variants at the extreme 3' end of a gene
- Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact
- Use caution in the presence of multiple transcripts

**VCEP Specifications:**

- PVS1 should be considered for the following genes with variants assessed in the Hearing Loss Variant Pilot: **GJB2, CDH23, USH2A, SLC26A4, MYO6, MYO7A, TECTA, KCNQ4**
- For other genes, LOF must be an established disease mechanism, and the gene/disease association must be Strong or Definitive clinical validity level as outlined in Strande et al. 2017 (PMID: 28552198)
- If above criteria is met, follow PVS1 flowchart as recommended by the SVI

#### Strength Levels

| Strength | Criteria |
|----------|----------|
| **Very Strong** | Null variant in a gene with established LOF as a disease mechanism; see PVS1_Strong, PVS1_Moderate, PVS1_Supporting for reduced evidence applications |
| **Strong** | See PVS1 flowchart for PVS1_Strong variants in gene where LOF is a known mechanism of disease |
| **Moderate** | See PVS1 flowchart for PVS1_Moderate variants in gene where LOF is a known mechanism of disease |
| **Supporting** | See PVS1 flowchart for PVS1_Supporting variants in gene where LOF is a known mechanism of disease |

---

### PS1 - Same Amino Acid Change

**Original ACMG Summary:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change. Example: Val->Leu caused by either G>C or G>T in the same codon.
**Caveat:** Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | Same amino acid change as an established pathogenic variant; OR splice variants at same nucleotide and with similar impact prediction as previously reported pathogenic variant |

- Established variant must meet criteria for pathogenicity by the HL specifications
- Can also use PS1 for splice variants located in the splice consensus sequence, at the same nucleotide position as a previously reported pathogenic variant
  - Example: c.105+1G>C is known to be pathogenic, can use PS1 for c.105+1G>T
- No additional hearing loss specifications for missense variants. Follow recommendations as outlined in Richards 2015 and/or the Sequence Variant Interpretation working group within ClinGen
- Caveat (from ACMG/AMP guidelines): Assess the possibility that the variant may act directly through the DNA change (e.g. through splicing disruption as assessed by at least computational analysis) instead of through the amino acid change

---

### PS2 - De Novo (Confirmed)

**Original ACMG Summary:** De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.
**Note:** Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.

**VCEP Specifications:** Follow recommendations as specified by the ClinGen Sequence Variant Interpretation working group. Determine number of points per proband using Table 1. Sum the total number of points for all probands, and determine the strength of the evidence using Table 2.

#### Table 1: Points Awarded Per De Novo Occurrence

| Phenotypic Consistency | Confirmed De Novo | Assumed De Novo |
|------------------------|-------------------|-----------------|
| Phenotype highly specific for gene | 2 | 1 |
| Phenotype consistent with gene but not highly specific | 1 | 0.5 |
| Phenotype consistent with gene but not highly specific and high genetic heterogeneity* | 0.5 | 0.25 |
| Phenotype not consistent with gene | 0 | 0 |

*Maximum allowable value of 1 may contribute to overall score

#### Table 2: PS2/PM6 Evidence Strength Thresholds

| Points | Strength Level |
|--------|----------------|
| 0.5 | Supporting (PS2_Supporting or PM6_Supporting) |
| 1.0 | Moderate (PS2_Moderate or PM6) |
| 2.0 | Strong (PS2 or PM6_Strong) |
| 4.0 | Very Strong (PS2_VeryStrong or PM6_VeryStrong) |

**Examples:**
- **Very Strong (4 points):** 2 proven de novo occurrences; OR 1 proven + 2 assumed de novo occurrences; OR 4 assumed de novo occurrences
- **Strong (2 points):** 1 proven de novo occurrence; OR 2 assumed de novo occurrences
- **Moderate (1 point):** 1 proven de novo occurrence (phenotype consistent but not specific to gene); OR 1 assumed de novo occurrence; OR 2 assumed de novo occurrences (phenotype/gene not specific)
- **Supporting (0.5 points):** 1 assumed de novo occurrence (phenotype/gene not specific)

---

### PS3 - Functional Studies

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.
**Note:** Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.

**VCEP Specifications:**

- Variant specific knock-in mouse models can be used as **strong** evidence
- Recommend that functional evidence, **except for a variant specific mouse model**, is **not** used as strong evidence, due to the absence of well-established functional studies for hearing loss genes

| Strength | Criteria |
|----------|----------|
| **Strong** | Knock-in mouse model demonstrates the phenotype |
| **Moderate** | Validated functional studies show a deleterious effect (predefined list - see gene-specific assays below) |
| **Supporting** | Functional studies with limited validation show a deleterious effect (predefined list - see gene-specific assays below) |

#### Gene-Specific Approved Functional Assays

**GJB2: Electrical coupling assays, dye transfer assays → PS3_Moderate**

- **Dye Transfer Assays:** Expect results that compare the fluorescence of a variant-transfected cell to both a negative control (or H2O injected control) and a wildtype-transfected cell. PS3_Moderate would be applied if the variant results in no dye transfer or significantly different dye transfer when compared to the wildtype.
- **Electrical Coupling Assays:** Expect results comparing the current of the variant-transfected cells to both a negative control (i.e. H2O injected control) and a wildtype-transfected cell. PS3_Moderate would be applied if the variant results in significantly different current compared to the wildtype, and the current is comparable to background levels/negative control.

**SLC26A4: Radio isotope and fluorescence assays → PS3_Supporting**

- **Radio Isotope Assays:** PS3_Supporting would be applied when cells transfected with mutant SLC26A4 show a statistically significant decreased efflux of iodide compared to wildtype pendrin.
- **Fluorescence Assays:** PS3_Supporting would be applied when a cell transfected with the mutant SLC26A4 shows a statistically significant difference in fluorescence (Delta-Fmax %) compared to the wildtype protein, and when the fluorescence is not significantly different from that of an empty vector control.

**COCH: Localization, secretion, and dimerization studies (immunofluorescence and Western blotting) → PS3_Supporting**

- **Localization:** PS3_Supporting would be applied if the mutant cochlin protein does not aggregate into extracellular deposits or in the perinuclear region, comparable to the localization of wildtype cochlin.
- **Secretion:** PS3_Supporting would be applied if cochlin protein containing the variant does not show secretion from transfected cells, but aggregates in cell regions such as the ER, Golgi and nucleus or is degraded.
- **Dimerization:** In a non-reducing environment, wildtype cochlin migrate quickly and appear smaller than in the reduced state because the structure is maintained by disulfide bonds. PS3_Supporting would be applied if the cochlin protein containing the variant forms more, or less, stable disulfide bonds when compared to the wildtype in non-reducing conditions.

**Other genes/assays → PS3_Supporting (if criteria met):**

If not listed above, OK to use PS3_Supporting for other genes/functional analyses if:
1. The assay has been validated by a known pathogenic and benign variant **AND**
2. There is plausible reason that the function the assay is testing relates to the phenotype **AND**
3. The assay conditions are likely to mimic the physiological environment

---

### PS4 - Prevalence in Affected

**Original ACMG Summary:** The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.

**VCEP Specifications:**

- If a published case-control study exists, use the data from the study, per ACMG/AMP guidelines
- Exclude cases with an alternate cause of disease

**Autosomal Dominant:**

If the variant meets PM2_Supporting, the criterion may be applied with the strength noted based on the following proband count observations:

| Strength | Proband Count (AD Only) |
|----------|------------------------|
| **Strong** | >=15 probands with variant, and variant meets PM2_Supporting |
| **Moderate** | >=6 probands with variant, and variant meets PM2_Supporting |
| **Supporting** | >=2 probands with variant, and variant meets PM2_Supporting |

**Autosomal Recessive:**

- If a published case-control study does not exist, and the variant is reported at high frequency in both cases and controls, a Chi-squared or Fisher's Exact test can be performed to determine if the variant is statistically higher in cases than the general population
- The gene must be definitively associated with hearing loss. Fisher's exact test is preferred if sample size allows
- This should be done with caution, since the general population databases are not a true control cohort, and could have individuals with hearing loss present. This analysis can be used as evidence for pathogenicity, but should not be used as evidence against pathogenicity
- The rule can be applied if the % of positive case alleles is higher than the % of positive alleles from the general population with a P value that is <=0.05

---

### PM1 - Mutational Hot Spot

**Original ACMG Summary:** Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Moderate** | Mutational hot spot or well-studied functional domain without benign variation (**KCNQ4 pore-forming region only**) |

- **KCNQ4** (NM_004700.4): missense variants located within **amino acids 271-292** can be awarded PM1. This region is the pore-forming intramembrane region where many variants that cause autosomal dominant hearing loss are located (Naito et al. 2013, PMID: 23717403). There are only two missense variants in this region in gnomAD, each with only a single allele (rs763326539: 1/33578 Latino chromosomes; rs55737429: 1/111720 European chromosomes).
- PM1 is **not applicable** for CDH23, COCH, GJB2, MYO6, MYO7A, SLC26A4, TECTA, or USH2A.

---

### PM2 - Absent from Controls

**Original ACMG Summary:** Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
**Caveat:** Population data for indels may be poorly called by next generation sequencing.

**VCEP Specification (Supporting only):**

Per SVI recommendation, PM2 will **not** be used at Moderate strength.

| Inheritance | PM2_Supporting Threshold |
|-------------|-------------------------|
| Autosomal Recessive | MAF <=0.00007 (0.007%) |
| Autosomal Dominant | MAF <=0.00002 (0.002%) |

**Notes:**
- Some genes are associated to both autosomal recessive and autosomal dominant hearing loss, and therefore for these genes the AD MAFs should be used for PM2_Supporting, since these are the more conservative thresholds
- For PM2_Supporting, use actual frequencies in gnomAD; do not apply confidence interval or filtering allele frequency
- Background: Rarity or absence in the general population is not robust evidence for pathogenicity, particularly for autosomal recessive disorders

---

### PM3 - In Trans with Pathogenic

**Original ACMG Summary:** For recessive disorders, detected in trans with a pathogenic variant.
**Note:** This requires testing of parents (or offspring) to determine phase.

**VCEP Specifications:** Use the point system as recommended by the ClinGen Sequence Variation Interpretation working group. Determine appropriate points for each proband using Table 1. Sum the total number of points for all probands, and determine the strength using Table 2.

- Use caution if the variant is observed in an isolated population in multiple probands, especially if the same pathogenic variant is observed in trans. Consider downgrading strength in this scenario.

#### Table 1: PM3 Point System (Per Proband)

| Classification/Zygosity of Other Variant | Known in Trans | Phase Unknown |
|------------------------------------------|---------------|---------------|
| Pathogenic/Likely pathogenic | 1.0 | 0.5 |
| Homozygous occurrence (max points from homozygotes = 1.0) | 0.5 | N/A |
| Rare VUS on other allele, OR Homozygous due to consanguinity (max 0.5 total) | 0.25 | N/A |

#### Table 2: PM3 Evidence Strength Thresholds

| Total Points | Strength Level |
|--------------|----------------|
| 0.5 | PM3_Supporting |
| 1.0 | PM3 (Moderate) |
| 2.0 | PM3_Strong |
| 4.0 | PM3_VeryStrong |

---

### PM4 - Protein Length Changes

**Original ACMG Summary:** Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Moderate** | Protein length change due to an in-frame deletion or insertion that are not located in repetitive regions |

No changes from ACMG/AMP guidelines. Follow recommendations as outlined in ACMG/AMP guidelines and/or Sequence Variant Interpretation working group.

---

### PM5 - Novel Missense at Same Residue

**Original ACMG Summary:** Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.
Example: Arg156His is pathogenic; now you observe Arg156Cys.
**Caveat:** Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | Missense change at same codon as **two** different pathogenic missense variants. Located at an amino acid residue with known pathogenic variation (at least 2 other variants at the same site meet pathogenic criteria based on independent data) |
| **Moderate** | Missense change at same codon as another pathogenic missense variant. No changes from ACMG/AMP guidelines |

**Caveat:** Assess whether the variants in question could have an impact at the DNA level, such as through splicing impacts.

---

### PM6 - De Novo (Assumed)

**Original ACMG Summary:** Assumed de novo, but without confirmation of paternity and maternity.

**VCEP Specifications:** See PS2 above - use the same point-based system. PM6 is incorporated into the PS2/PM6 point system.

---

### PP1 - Co-segregation

**Original ACMG Summary:** Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.
**Note:** May be used as stronger evidence with increasing segregation data.

**VCEP Specifications:** Follow general recommendations from ClinGen's Sequence Variant Interpretation working group.

- For both autosomal dominant and autosomal recessive segregation counting, **do not count probands as a segregation**
  - Affected segregations = # affected individuals in the family with the variant (dominant) or variants (recessive) - 1

#### PP1 Thresholds

| Strength | Likelihood | LOD Score | AD Threshold | AR Threshold |
|----------|------------|-----------|--------------|--------------|
| Supporting | 4:1 | 0.6 | 2 affected segregations | See LOD score table |
| Moderate | 16:1 | 1.2 | 4 affected segregations | See LOD score table |
| Strong | 32:1 | 1.5 | 5 affected segregations | See LOD score table |

**Dominant segregations:**
- LOD scores are calculated with the following equation: Z (LOD score) = log10(1 / 0.5^Segregations)
- Only count affected individuals (minus proband) that are positive for the variant

**Autosomal recessive segregations:**
- LOD scores are calculated with the following equation: Z (LOD score) = log10(1 / (0.25^#affected_segregations x 0.75^#unaffected_segregations))
- The "0.25" and "0.75" numbers represent the risk of being affected vs. unaffected in a classic AR disease model in which both parents are carriers
- Affected segregations = affected family members (typically siblings) who harbor the variant in question and a second variant on the remaining allele
- Unaffected segregations = unaffected family members, typically siblings, who are at risk to inherit the two variants identified in the proband. These individuals should be either wild-type for both variants identified in the proband, or a heterozygous carrier for a single variant
- Unaffected, carrier parents DO NOT count as unaffected segregations

#### AR Segregation LOD Score Table

| Affected Seg. \ Unaffected Seg. | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|----|------|------|------|------|------|------|------|------|------|------|------|
| **0** | 0 | 0.12 | 0.25 | 0.37 | 0.5 | 0.62 | 0.75 | 0.87 | 1 | 1.12 | 1.25 |
| **1** | 0.6 | 0.73 | 0.85 | 0.98 | 1.1 | 1.23 | 1.35 | 1.48 | 1.6 | 1.73 | 1.85 |
| **2** | 1.2 | 1.33 | 1.45 | 1.58 | 1.7 | 1.83 | 1.95 | 2.08 | 2.2 | 2.33 | 2.45 |
| **3** | 1.81 | 1.93 | 2.06 | 2.18 | 2.31 | 2.43 | 2.56 | 2.68 | 2.81 | 2.93 | 3.06 |
| **4** | 2.41 | 2.53 | 2.66 | 2.78 | 2.91 | 3.03 | 3.16 | 3.28 | 3.41 | 3.53 | 3.66 |
| **5** | 3.01 | 3.14 | 3.26 | 3.39 | 3.51 | 3.63 | 3.76 | 3.88 | 4.01 | 4.13 | 4.26 |
| **6** | 3.61 | 3.74 | 3.86 | 3.99 | 4.11 | 4.24 | 4.36 | 4.49 | 4.61 | 4.74 | 4.86 |
| **7** | 4.21 | 4.34 | 4.46 | 4.59 | 4.71 | 4.84 | 4.96 | 5.09 | 5.21 | 5.34 | 5.46 |
| **8** | 4.82 | 4.94 | 5.07 | 5.19 | 5.32 | 5.44 | 5.57 | 5.69 | 5.82 | 5.94 | 6.07 |
| **9** | 5.42 | 5.54 | 5.67 | 5.79 | 5.92 | 6.04 | 6.17 | 6.29 | 6.42 | 6.54 | 6.67 |
| **10** | 6.02 | 6.15 | 6.27 | 6.4 | 6.52 | 6.65 | 6.77 | 6.9 | 7.02 | 7.15 | 7.27 |

---

### PP2 - Missense in Constrained Gene

**Original ACMG Summary:** Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.

**VCEP Specifications:** *Not Applicable*

Advise against using this rule because there are few such genes that this would apply to, particularly genes associated to autosomal recessive hearing loss.

---

### PP3 - Computational Evidence

**Original ACMG Summary:** Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).
**Caveat:** As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Supporting** | REVEL score >=0.7, or predicted impact to splicing using MaxEntScan |

- Use **REVEL** and **MaxEntScan**
- For missense variants, award PP3 if REVEL score is **>=0.7**
- If splicing is predicted to be impacted, either creation of a cryptic splice site, or disruption of a native splice site, award PP3
- For splice variants (except for canonical -/+1 or 2), use MaxEntScan
- For -/+1 or 2 splice variants, **do not use PP3** if you are using PVS1

---

### PP4 - Phenotype Specificity

**Original ACMG Summary:** Patient's phenotype or family history is highly specific for a disease with a single genetic etiology.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Supporting** | Patient's phenotype highly specific for gene or fully sequenced gene set (see gene-specific phenotypes below) |

- The HL-EP applied this rule to HL syndromes if all causative genes have been sequenced and the detection rate at least doubles when the added clinical feature is present
- Advise against using PP4 for patients with nonsyndromic or apparently nonsyndromic hearing loss, given genetic heterogeneity

#### PP4 Gene-Specific Phenotypes

| Gene | Syndrome | Phenotype | Detection Rate (Unselected HL) | Detection Rate (With Phenotype) |
|------|----------|-----------|-------------------------------|-------------------------------|
| SLC26A4 | Pendred syndrome | Hearing loss with enlarged vestibular aqueduct (EVA) and/or Mondini malformation (incomplete partitioning type 2) | 2.6% (Sloan-Heggen et al., 2016) | 50% for a single mutation (Albert et al., 2006; Azaiez et al., 2007; Chattaraj et al., 2017; Choi, Madeo et al., 2009; Pryor et al., 2005) |
| MYO7A, CDH23 | Usher syndrome Type I | Moderately-severe to profound hearing loss and retinitis pigmentosa (onset typically in first decade), +/- vestibular dysfunction | 4.3% (Sloan-Heggen et al., 2016) | 78.7% for 2 mutations (Le Quesne Stabej et al., 2012) |
| USH2A | Usher syndrome Type II | Mild to severe hearing loss and retinitis pigmentosa (onset typically in first or second decade) | 2.9% (Sloan-Heggen et al., 2016) | 60.3% (Le Quesne Stabej et al., 2012) |

---

### PP5 - Reputable Source

**Original ACMG Summary:** Reputable source recently reports variant as pathogenic, but the evidence is not available to the laboratory to perform an independent evaluation.

**VCEP Specifications:** *Not Applicable*

This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PMID: 29543229).

---

## Benign Criteria

### BA1 - Allele Frequency >5%

**Original ACMG Summary:** Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

**VCEP Specification (Stand Alone):**

| Inheritance | BA1 Threshold |
|-------------|---------------|
| Autosomal Recessive | MAF >=0.005 (0.5%) |
| Autosomal Dominant | MAF >=0.001 (0.1%) |

**Notes:**
- Some genes are associated to both autosomal recessive and autosomal dominant hearing loss; use the AR MAFs for BA1 since these are more conservative
- Use filtering allele frequency in ExAC or 95% confidence interval
- **BA1 does NOT apply** to variants on the exclusion list (see Appendix D)

---

### BS1 - Frequency Greater Than Expected

**Original ACMG Summary:** Allele frequency is greater than expected for disorder.

**VCEP Specifications:**

| Inheritance | BS1 (Strong) | BS1_Supporting |
|-------------|-------------|----------------|
| Autosomal Recessive | MAF >=0.003 (0.3%) | MAF >=0.0007 (0.07%) |
| Autosomal Dominant | MAF >=0.0002 (0.02%) | No BS1_Supporting criteria for AD |

- BS1 = Likely benign, provided there is no conflicting evidence
- Use filtering allele frequency in ExAC or 95% confidence interval
- **BS1 does NOT apply** to variants on the exclusion list (see Appendix D)

---

### BS2 - Observed in Healthy Adult

**Original ACMG Summary:** Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | Observation of variant (biallelic with known pathogenic variant for recessive) in controls inconsistent with disease penetrance |

- Advise caution when using this rule, since most of hearing loss is autosomal recessive, and autosomal dominant hearing loss could display reduced penetrance or variable expression
- However, if biallelic observations in controls are inconsistent with disease penetrance, this may be applicable

---

### BS3 - Functional Studies (No Effect)

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

**VCEP Specifications:**

- Recommend that functional evidence is **not** used as strong evidence, due to the absence of well-established functional studies for hearing loss genes
- BS3 is available at **Supporting** strength only

| Strength | Criteria |
|----------|----------|
| **Supporting** | Functional study shows no deleterious effect (predefined list - see below) |

#### Gene-Specific BS3 Assays

**GJB2: Electrical coupling assays, dye transfer assays → BS3_Supporting**

- **Dye Transfer Assays:** BS3_Supporting can be applied if the variant results in dye transfer comparable to the wildtype.
- **Electrical Coupling Assays:** BS3_Supporting would be applied if the variant results in a current comparable to the wildtype.

**SLC26A4: Radio isotope and fluorescence assays → BS3_Supporting**

- **Radio Isotope Assays:** BS3_Supporting would be applied if the variant results in iodide efflux levels comparable to the wildtype.
- **Fluorescence Assays:** BS3_Supporting would be applied if the variant results in fluorescence comparable to the wildtype.

**COCH: Localization, secretion, and dimerization studies (immunofluorescence and Western blotting) → BS3_Supporting**

- **Localization:** BS3_Supporting would be applied if the variant results in extracellular deposits comparable to the wildtype.
- **Secretion:** BS3_Supporting would be applied if the variant results in secretion comparable to the wildtype.
- **Dimerization:** BS3_Supporting would be applied if the variant results in molecular weight and size comparable to the wildtype.

**Other genes/assays → BS3_Supporting (if criteria met):**

If not listed above, OK to use BS3_Supporting for other genes/functional analyses if:
1. The assay has been validated by a known pathogenic and benign variant **AND**
2. There is plausible reason that the function the assay is testing relates to the phenotype **AND**
3. The assay conditions are likely to mimic the physiological environment

---

### BS4 - Lack of Segregation

**Original ACMG Summary:** Lack of segregation in affected members of a family.
**Caveat:** The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | Non-segregation with disease |

**Phenotype+/genotype- (affected individual does NOT carry variant):**
- Strong evidence for benign
- Be cautious when using this as the possibility for phenocopy is high
- The hearing loss phenotype should be consistent within the family to consider it a non-segregation, though intra-familial variability has been reported
- Factors to consider:
  - **Age of onset** (congenital/early childhood vs. adult onset). Hearing loss prevalence increases significantly with age. A congenital hearing loss in a child and a late onset hearing loss in a grandparent would not be a consistent phenotype
  - **Severity** (mild vs. profound). Minor differences may exist among family members. Progression in older individuals may account for a discrepancy
  - **Sex-based differences** (infertility, genes on X chromosomes)
  - **Audiogram shape** - may not be completely consistent among family members even with same etiology

**Genotype+/phenotype- (individual carries variant but is NOT affected):**
- Confounding variables: Age-related/sex-related penetrance, variable expressivity, etc.
- If the gene is associated with later onset and individual with the non-segregation is beyond the expected age that the hearing loss would occur, consider applying **BS4_Supporting**
- Recommend only using for fully penetrant genes (typically genes associated with AR hearing loss)
- Must be confident that patient is truly unaffected and a hearing loss is not missed or subclinical. Be cautious if only phenotyping was newborn hearing screening. Diagnostic audiometric testing (auditory brainstem response (ABR) or audiogram should be required)
- Any evidence for reduced penetrance, **do not use BS4**

---

### BP1-BP7 - Benign Supporting

| Criterion | Status | Comment |
|-----------|--------|---------|
| **BP1** | Not Applicable | Do not use |
| **BP2** | Supporting | Observed in trans with a dominant variant/observed in cis with a pathogenic variant. Use with caution. For genes associated with both dominant and recessive hearing loss, consider whether an earlier onset/more severe phenotype could be present if variant is identified in trans with a dominant variant |
| **BP3** | Supporting | In-frame indels in repeat region without known function. No changes from ACMG/AMP guidelines |
| **BP4** | Supporting | Computational evidence suggests no impact; REVEL score <=0.15 or no impact to splicing in MaxEntScan. Make sure to also check MaxEntScan to rule out the creation of a cryptic splice site |
| **BP5** | Supporting (AD only) | Variant in an autosomal dominant gene found in a patient with an alternate explanation. **Do not use for AR** - an individual could be carrier of pathogenic variant and have an alternate cause. Caveat: consider whether multiple pathogenic AD variants could cause a more severe phenotype or whether multigenic inheritance is known to occur (e.g., Bardet-Biedl syndrome) |
| **BP6** | Not Applicable | Not for use as recommended by the ClinGen SVI VCEP Review Committee (PMID: 29543229) |
| **BP7** | Supporting | Silent variant with no predicted impact to splicing. No changes from ACMG/AMP guidelines |

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
| PVS1 **AND** PM2_Supporting* |
| 1 Very Strong **AND** 1 Moderate |
| 1 Strong **AND** 1-2 Moderate |
| 1 Strong **AND** >=2 Supporting |
| >=3 Moderate |
| 2 Moderate **AND** >=2 Supporting |
| 1 Moderate **AND** >=4 Supporting |

*The addition of this rule is the only modification made from the original ACMG/AMP published guidelines for combining criteria.

### Benign Classification

| Criteria Combination |
|---------------------|
| 1 Stand-Alone (BA1) |
| >=2 Strong |

### Likely Benign Classification

| Criteria Combination |
|---------------------|
| BS1 with no conflicting evidence* |
| 1 Strong **AND** 1 Supporting |
| >=2 Supporting |

*The addition of this rule is the only modification made from the original ACMG/AMP published guidelines for combining criteria. This addition is consistent with recommendations by the Cardiomyopathy Expert Panel and the RASopathy Expert Panel.

---

## Appendices

### Appendix A: PVS1 Flowchart

#### Nonsense or Frameshift Variants

**Predicted to undergo NMD:**
- Exon is present in biologically-relevant transcript(s) → **PVS1**
- Exon is absent from biologically-relevant transcript(s) → **N/A**

**Not predicted to undergo NMD:**
- Truncated/altered region is critical to protein function → **PVS1_Strong**
- Role of region in protein function is unknown:
  - LoF variants in this exon are frequent in general population and/or exon is absent from biologically-relevant transcript(s) → **N/A**
  - LoF variants in this exon are NOT frequent in general population and/or exon is present in biologically-relevant transcript(s):
    - Variant removes >10% of protein → **PVS1_Strong**
    - Variant removes <10% of protein → **PVS1_Moderate**

**Exon skipping or use of cryptic splice site disrupts reading frame and is predicted to undergo NMD:**
- Exon is present in biologically-relevant transcript(s) → **PVS1**
- Exon is absent from biologically-relevant transcript(s) → **N/A**

**Exon skipping or use of cryptic splice site disrupts reading frame and is NOT predicted to undergo NMD:**
- Truncated/altered region is critical to protein function → **PVS1_Strong**
- Role of region in protein function is unknown:
  - LoF variants in this exon are frequent in general population and/or exon is absent from biologically-relevant transcript(s) → **N/A**
  - LoF variants in this exon are NOT frequent in general population and/or exon is present in biologically-relevant transcript(s):
    - Variant removes >10% of protein → **PVS1_Strong**
    - Variant removes <10% of protein → **PVS1_Moderate**

**Exon skipping or use of cryptic splice site preserves reading frame:**
- Truncated/altered region is critical to protein function → **PVS1_Strong**
- Role of region in protein function is unknown:
  - LoF variants in this exon are frequent in general population and/or exon is absent from biologically-relevant transcript(s) → **N/A**
  - LoF variants in this exon are NOT frequent in general population and/or exon is present in biologically-relevant transcript(s):
    - Variant removes >10% of protein → **PVS1_Strong**
    - Variant removes <10% of protein → **PVS1_Moderate**

#### Deletion Variants (Single exon to full gene)

- Full gene deletion → **PVS1**
- Single to multi-exon deletion, disrupts reading frame, predicted to undergo NMD:
  - Exon is present in biologically-relevant transcript(s) → **PVS1**
  - Exon is absent from biologically-relevant transcript(s) → **N/A**
- Single to multi-exon deletion, disrupts reading frame, NOT predicted to undergo NMD:
  - Truncated/altered region is critical to protein function → **PVS1_Strong**
  - Role of region in protein function is unknown:
    - LoF variants in this exon are frequent in general population and/or exon is absent from biologically-relevant transcript(s) → **N/A**
    - LoF variants in this exon are NOT frequent:
      - Variant removes >10% of protein → **PVS1_Strong**
      - Variant removes <10% of protein → **PVS1_Moderate**
- Single to multi-exon deletion, preserves reading frame:
  - Truncated/altered region is critical to protein function → **PVS1_Strong**
  - Role of region in protein function is unknown:
    - LoF variants in this exon are frequent in general population and/or exon is absent from biologically-relevant transcript(s) → **N/A**
    - LoF variants in this exon are NOT frequent:
      - Variant removes >10% of protein → **PVS1_Strong**
      - Variant removes <10% of protein → **PVS1_Moderate**

#### Duplication Variants (>=1 exon, completely contained within gene)

- Proven in tandem:
  - Reading frame disrupted and NMD predicted to occur → **PVS1**
- Presumed in tandem:
  - No or unknown impact on reading frame and NMD → **N/A**
  - Reading frame presumed disrupted and NMD predicted to occur → **PVS1_Strong**
- Proven not in tandem → **N/A**

#### Initiation Codon Variants

- No known alternative start codon in other transcripts:
  - >=1 pathogenic variant(s) upstream of closest potential in-frame start codon → **PVS1_Moderate**
  - No pathogenic variant(s) upstream of closest potential in-frame start codon → **PVS1_Supporting**
- Different functional transcript uses alternative start codon → **N/A**

---

### Appendix B: Reference PMIDs

| Reference | PMID |
|-----------|------|
| Richards et al. 2015 (ACMG/AMP Guidelines) | 25741868 |
| Hearing Loss VCEP Publication | 30311386 |
| PP5/BP6 Not Recommended | 29543229 |
| Strande et al. 2017 (Clinical Validity) | 28552198 |
| Naito et al. 2013 (KCNQ4 PM1 region) | 23717403 |
| Albert et al. 2006 (SLC26A4/EVA) | - |
| Azaiez et al. 2007 (SLC26A4/EVA) | - |
| Chattaraj et al. 2017 (SLC26A4/EVA) | - |
| Sloan-Heggen et al. 2016 (HL detection rates) | - |
| Le Quesne Stabej et al. 2012 (Usher syndrome) | - |

---

### Appendix C: Population Frequency Thresholds Summary

| Criterion | AR Threshold | AD Threshold | Strength |
|-----------|-------------|-------------|----------|
| BA1 | >=0.005 (0.5%) | >=0.001 (0.1%) | Stand Alone |
| BS1 | >=0.003 (0.3%) | >=0.0002 (0.02%) | Strong |
| BS1_Supporting | >=0.0007 (0.07%) | N/A | Supporting |
| PM2_Supporting | <=0.00007 (0.007%) | <=0.00002 (0.002%) | Supporting |

**MAF Threshold Derivation:**

| Parameter | AR | AD |
|-----------|----|----|
| Prevalence | 1/200 | 1/30 (BA1); 1/150 (BS1) |
| Allelic Heterogeneity | 7.2% (BA1); 4.4% (BS1); 1.0% (BS1_Supp) | 5% |
| Penetrance | 100% | 80% |

**Notes on MAF thresholds:**
- For genes associated to both AR and AD hearing loss, use the AD MAFs for PM2_Supporting (more conservative)
- For PM2_Supporting, use actual frequencies in gnomAD; do not apply confidence interval or filtering allele frequency
- For BA1, BS1, and BS1_Supporting, use filtering allele frequency in ExAC or 95% confidence interval

---

### Appendix D: Variant Exclusion List (BA1/BS1 Not Applicable)

The following high-frequency pathogenic variants should NOT be classified as benign or likely benign based on their allele frequency:

| Gene | Transcript | cDNA | Protein | ClinVar ID | Pathogenicity | MAF* |
|------|-----------|------|---------|------------|---------------|------|
| GJB2 | NM_004004.6 | c.35delG | p.Gly12Valfs*2 | 17004 | Pathogenic | 0.97% (European) |
| GJB2 | NM_004004.6 | c.235delC | p.Leu79Cysfs*3 | 17014 | Pathogenic | 0.64% (EA) |
| GJB2 | NM_004004.6 | c.167delT | p.Leu56Argfs*26 | 17010 | Pathogenic | 1.63% (AJ) |
| GJB2 | NM_004004.6 | c.-22-2A>C | p.? | 375406 | Uncertain Significance | 0.45% (AJ) |
| GJB2 | NM_004004.6 | c.71G>A | p.Trp24* | 17002 | Pathogenic | 0.45% (SA) |
| GJB2 | NM_004004.6 | c.34G>T | p.Gly12Cys | 44740 | Likely Pathogenic | 0.38% (Latino) |
| GJB2 | NM_004004.6 | c.109G>A | p.Val37Ile | 17023 | Pathogenic | 8.19% (EA) |
| GJB2 | NM_004004.6 | c.101T>C | p.Met34Thr | 17000 | Pathogenic | 2.00% (EF) |
| SLC26A4 | NM_000441.2 | c.919-2A>G | p.? | 4840 | Pathogenic | 0.48% (EA) |
| SLC26A4 | NM_000441.2 | c.349C>T | p.Leu117Phe | 43555 | Pathogenic | 0.51% (AJ) |

*The highest subpopulation frequency in gnomAD is shown. EA: East Asian; AJ: Ashkenazi Jewish; SA: South Asian; EF: European (Finnish)

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 2.0.0 | 3/30/2022 | (1) Removal of PM2 at moderate strength and use of PM2 cutoff at supporting strength. (2) Functional assay strength and evidence using criteria from Brnich et al., including downgrading PS3 to supporting for all specified COCH assays. (3) Removal of PP4 and PM1 specifications of genes outside HL VCEP defined scope |
| 1.0.0 | 2018 | Initial version |

---

*This document was compiled from ClinGen VCEP specifications and ClinGen SVI recommendations. For the most current version, please refer to the ClinGen website at https://www.clinicalgenome.org/affiliation/50007/docs/assertion-criteria*
