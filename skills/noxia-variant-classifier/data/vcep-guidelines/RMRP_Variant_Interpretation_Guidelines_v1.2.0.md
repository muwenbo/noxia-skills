# ClinGen Severe Combined Immunodeficiency Disease VCEP Variant Interpretation Guidelines for RMRP

**Version:** 1.2.0
**Released:** 1/20/2026
**Affiliation:** Severe Combined Immunodeficiency Disease VCEP
**Based on:** Richards et al., 2015 ACMG/AMP Guidelines

---

## Gene Information

| Attribute | Value |
|-----------|-------|
| **Gene** | RMRP (HGNC:10031) |
| **HGNC Name** | RNA component of mitochondrial RNA processing endoribonuclease |
| **Transcript** | NR_003051.3 |
| **Disease** | Cartilage-hair hypoplasia (MONDO:0009595) |
| **Inheritance** | Autosomal recessive inheritance |

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

| Strength | Criteria |
|----------|----------|
| ***Not Applicable*** | Does not apply. RMRP is a non-coding RNA gene; standard LOF variant types (nonsense, frameshift, canonical splice sites, initiation codon) are not applicable. |

---

### PS1 - Same Amino Acid Change

**Original ACMG Summary:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.

Example: Val->Leu caused by either G>C or G>T in the same codon.

Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Supporting** | Same amino acid change as a previously established pathogenic variant regardless of nucleotide change. Downgraded to PS1_Supporting. |

- Applicable if a different nucleotide change at the same nucleotide position has been previously classified as pathogenic or likely pathogenic.
- Cannot be applied if a different nucleotide change at the same position has been previously classified as benign or likely benign.
- Previously established variants must be classified by SCID VCEP specifications for *RMRP*.

**Modification Type:** Gene-specific, Strength

---

### PS2 - De Novo (Confirmed)

**Original ACMG Summary:** De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.

Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.

**VCEP Specifications:**

Use ClinGen SVI recommendations for *de novo* criteria (PS2/PM6 Version 1.1) with the following gene-specific phenotypic consistency guidelines:

- **"Phenotype highly specific for gene"**: proband must meet PP4_Moderate criteria (score ≥2 points)
- **"Phenotype consistent with gene but not highly specific"**: proband must meet PP4 criteria (score 1 to <2 points)
- **"Phenotype consistent with gene but not highly specific and high genetic heterogeneity"**: proband has been asserted to have a Cartilage-hair hypoplasia (CHH) phenotype but does not meet PP4 criteria
- Reduce points per proband by half if the phase is unconfirmed

**Note:** For autosomal recessive conditions, for a *de novo* occurrence without an additional pathogenic/likely pathogenic variant identified, the strength of evidence should be decreased by one level.

#### PS2/PM6 Point System

| Phenotypic Consistency | Confirmed Parental Relationships | Unconfirmed Parental Relationships |
|------------------------|----------------------------------|------------------------------------|
| Phenotype highly specific for gene (meets PP4_Moderate) | 2 points | 1 point |
| Phenotype consistent but not highly specific (meets PP4) | 1 point | 0.5 points |
| Phenotype consistent + high genetic heterogeneity (does not meet PP4) | 0.5 points | 0.25 points |
| Phenotype not consistent | 0 points | 0 points |

*Maximum allowable value of 1 may contribute to overall score for "high genetic heterogeneity" category.*

#### Evidence Strength Thresholds

| Points | Strength Level |
|--------|----------------|
| 0.5 | PS2_Supporting / PM6_Supporting |
| 1.0 | PS2_Moderate / PM6 (Moderate) |
| 2.0 | PS2 (Strong) / PM6_Strong |
| 4.0 | PS2_VeryStrong / PM6_VeryStrong |

**Modification Type:** Disease-specific, Strength

---

### PS3 - Functional Studies

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.

Note: Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.

**VCEP Specifications:**

PS3 may be applied when RT/PCR or RNA evidence indicates variant results in absent expression.

At least one previously observed proband with the expressed RMRP variant meeting PP4 is required to apply PS3 at any strength.

| Strength | Criteria |
|----------|----------|
| **Strong** | PS3 may potentially be applied at the default strength level of strong for evidence from an animal model expressing the variant of interest and recapitulating the Cartilage-hair hypoplasia (CHH) phenotype. Animal models will be reviewed on a case-by-case basis by the VCEP to determine the appropriate strength level. |
| **Supporting** | PS3_Supporting can be applied based on an abnormal result in **at least** one approved *in vitro* assay (see Approved Assay Instances below). |

**Modification Type:** Gene-specific, Disease-specific, Strength

#### Approved Assay Instances

**1. Endonucleolytic Cleavage Activity Assay**

| Attribute | Details |
|-----------|---------|
| **PMID** | 16252239 (Thiel et al., 2005), 17701897 (Thiel et al., 2007) |
| **Assay Description** | RNA and DNA extracted from normal human fibroblasts transiently transfected with wild type or variant RMRP expression constructs, evaluated by quantitative real-time PCR for RMRP, CCNB2, 5.8S rRNA, and ITS-1-bound 5.8S rRNA expression levels |
| **Material** | Normal human fibroblasts transiently transfected with wild type or variant RMRP expression constructs |
| **Readout** | Quantitative: mRNA cleavage activity normalized to wild type (inverse relative increase of CCNB2 mRNA level); rRNA cleavage activity normalized to wild type (ratio of levels of cleaved to uncleaved 5.8S rRNA) |
| **Abnormal Threshold** | mRNA cleavage activity smaller than 0.9 |
| **Approved Strength** | PS3_Supporting |

**2. Luciferase Reporter Assay**

| Attribute | Details |
|-----------|---------|
| **PMID** | 16254002 (Hermanns et al., 2005) |
| **Assay Description** | Expression plasmids containing wild type and variant RMRP promoter sequences upstream of an shRNA against luciferase were transfected in cos7 cells in combination with a luciferase expression plasmid |
| **Material** | cos7 cells transfected with luciferase-targeted shRNA under the control of wild type or variant RMRP promoters |
| **Readout** | Quantitative: Relative luciferase activity (promoter strength correlates with the degree of shRNA-mediated downregulation of luciferase expression) |
| **Abnormal Threshold** | Luciferase activity higher than 7 |
| **Approved Strength** | PS3_Supporting |

---

### PS4 - Prevalence in Affected

**Original ACMG Summary:** The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| ***Not Applicable*** | Does not apply. PS4 is applied for autosomal dominantly inherited conditions, and RMRP requires biallelic loss. |

---

### PM1 - Mutational Hot Spot

**Original ACMG Summary:** Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | Defined to include insertions/duplications between the TATA box (spanning n.-32 to n.-24) and the transcription start site (n.4). |

**Caveat:** All variants should be sufficiently rare - variant does not have to meet PM2 specification criteria but variant should not meet BS1/BA1 criteria (unless a suspected founder variant). The applicability of PM1 to suspected founder variants exceeding the BS1/BA1 threshold will be evaluated on a case-by-case basis by the VCEP.

**Modification Type:** Gene-specific

**Note (v1.2.0 update):** PM1 was updated from its previous version which required variants to meet PM2. The updated language now mirrors PM3's rarity caveat, allowing PM1 to be applied to variants that are sufficiently rare (below BS1/BA1) even if they do not meet the PM2 threshold. This change was approved by the SCID VCEP on 9/26/2025.

---

### PM2 - Absent from Controls

**Original ACMG Summary:** Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

Caveat: Population data for indels may be poorly called by next generation sequencing.

**VCEP Specification (Supporting only):**

- Downgraded to PM2_Supporting
- gnomAD popmax filtering allele frequency **<0.0000447**
- The applicability of PM2 to suspected founder variants with allele frequencies exceeding the PM2 threshold will be evaluated on a case-by-case basis by the VCEP.
- Use caution when applying PM2 based on allele frequencies derived from gnomAD exome sequencing given the reduced coverage of certain regions of *RMRP*. Ensure at least 20X read depth for allele frequencies derived from exome sequencing.

**Modification Type:** Disease-specific, Strength

---

### PM3 - In Trans with Pathogenic

**Original ACMG Summary:** For recessive disorders, detected in trans with a pathogenic variant.

Note: This requires testing of parents (or offspring) to determine phase.

**VCEP Specifications:**

Use ClinGen SVI recommendations for *in trans* criterion with the additional requirement that the co-occurring variant must be classified using the SCID VCEP specifications for *RMRP*.

**Caveat:** All variants should be sufficiently rare - variant does not have to meet PM2 specification criteria but variant should not meet BS1/BA1 criteria (unless a suspected founder variant). The applicability of PM3 to suspected founder variants exceeding the BS1/BA1 threshold will be evaluated on a case-by-case basis by the VCEP.

#### PM3 Point System (Per Proband-Family)

| Classification/Zygosity of Other Variant | Confirmed in Trans | Phase Unknown |
|------------------------------------------|-------------------|---------------|
| Pathogenic or Likely pathogenic variant | 1.0 | 0.5 (P) / 0.25 (LP) |
| Homozygous occurrence - Non-consanguineous (no max) | 1.0 | 1.0 |
| Homozygous occurrence - Consanguineous (no max) | 0.5 | 0.5 |
| Uncertain significance variant (max point 0.5) | 0.25 | 0.0 |

*All variants should be sufficiently rare (meet PM2 specification); P = Pathogenic; LP = Likely pathogenic.*

*Multiple probands from separate nuclear families that are later found to have identity-by-descent should only be counted once.*

*When consanguinity is not known or reported: if family IS NOT from a bottlenecked population (as defined by gnomAD), assume non-consanguinity; otherwise, assume consanguinity. If genetic ancestry of the family cannot be determined, assume consanguinity.*

#### PM3 Evidence Strength Thresholds

| Total Points | Strength Level |
|--------------|----------------|
| 0.5 | PM3_Supporting |
| 1.0 | PM3 (Moderate) |
| 2.0 | PM3_Strong |
| 4.0 | PM3_VeryStrong |

#### PM3 Considerations

- **Allele Frequency:** Application of PM3 is contingent on the allele frequency of the variant being assessed and the variant presumably on the other allele both being sufficiently rare (meets PM2 threshold).
- **Phasing:** If the phase cannot be determined, it is recommended that at least two different LP/P variants (depending on classifications) are needed to equal the weight of one LP/P co-occurrence confirmed in *trans*. If only one parent is tested and found to carry one allele, variants can be counted as *in trans*.
- **Classification:** Probands should be weighted less when the variant on the other allele is of uncertain significance and rare (meets PM2). To avoid circularity, the classification of the variant on the other allele should not use evidence from the variant being interrogated.
- **Homozygous Occurrences:** For non-consanguineous families, default weight is 1.0 point. For consanguineous families, the default weight is 0.5 points.

**Modification Type:** General recommendation, Strength

---

### PM4 - Protein Length Changes

**Original ACMG Summary:** Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Moderate** | Defined to include insertions/duplications of 6 or more nucleotides increasing the distance between the TATA box (spanning n.-32 to n.-24) and the transcription start site (n.4). |

**Modification Type:** Gene-specific

---

### PM5 - Novel Missense at Same Residue

**Original ACMG Summary:** Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.

Example: Arg156His is pathogenic; now you observe Arg156Cys.

Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| ***Not Applicable*** | Does not apply. RMRP is a non-coding RNA gene. |

---

### PM6 - De Novo (Assumed)

**Original ACMG Summary:** Assumed de novo, but without confirmation of paternity and maternity.

**VCEP Specifications:**

Same as PS2 - use point-based system above (PS2/PM6 Point System). The following guidelines should be used when determining the phenotypic consistency of each proband:

- **"Phenotype highly specific for gene"**: proband must meet PP4_Moderate criteria
- **"Phenotype consistent with gene but not highly specific"**: proband must meet PP4 criteria
- **"Phenotype consistent with gene but not highly specific and high genetic heterogeneity"**: proband has been asserted to have a Cartilage-hair hypoplasia (CHH) phenotype but does not meet PP4 criteria
- Reduce points per proband by half if the phase is unconfirmed

| Strength | Criteria |
|----------|----------|
| **Strong** | Use ClinGen SVI recommendations for *de novo* criteria |
| **Moderate** | Use ClinGen SVI recommendations for *de novo* criteria |
| **Supporting** | Use ClinGen SVI recommendations for *de novo* criteria |

**Modification Type:** Disease-specific, Strength

---

### PP1 - Co-segregation

**Original ACMG Summary:** Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.

Note: May be used as stronger evidence with increasing segregation data.

**VCEP Specifications:**

Use ClinGen SVI recommendations for co-segregation criterion (PMID: 30311386) with the additional specification that unaffected individuals contributing to the calculated LOD score must be heterozygous carriers of one of the variants observed in the affected individuals (i.e. do not count wild-type/wild-type individuals).

#### PP1 Thresholds (General)

| Strength | Likelihood | LOD Score |
|----------|------------|-----------|
| Supporting | 4:1 | 0.6 |
| Moderate | 16:1 | 1.2 |
| Strong | 32:1 | 1.5 |

#### PP1 Autosomal Recessive Segregation LOD Scores

Affected segregations are counted in rows and unaffected segregations in columns. Affected segregations are affected family members in whom biallelic compound heterozygous or homozygous variants segregate. Unaffected segregations are unaffected family members (typically siblings) who are at risk to inherit the two variants identified in the proband. These individuals should be either wild-type for both variants or a heterozygous carrier for a single variant. Unaffected carrier parents DO NOT count as unaffected segregations.

| Affected \ Unaffected | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|-----------------------|---|---|---|---|---|---|---|---|---|---|---|
| **0** | 0 | 0.12 | 0.25 | 0.37 | 0.50 | 0.62 | 0.75 | 0.87 | 1.00 | 1.12 | 1.25 |
| **1** | 0.60 | 0.73 | 0.85 | 0.98 | 1.10 | 1.23 | 1.35 | 1.48 | 1.60 | 1.73 | 1.85 |
| **2** | 1.20 | 1.33 | 1.45 | 1.58 | 1.70 | 1.83 | 1.95 | 2.08 | 2.20 | 2.33 | 2.45 |
| **3** | 1.81 | 1.93 | 2.06 | 2.18 | 2.31 | 2.43 | 2.56 | 2.68 | 2.81 | 2.93 | 3.06 |
| **4** | 2.41 | 2.53 | 2.66 | 2.78 | 2.91 | 3.03 | 3.16 | 3.28 | 3.41 | 3.53 | 3.66 |
| **5** | 3.01 | 3.14 | 3.26 | 3.39 | 3.51 | 3.63 | 3.76 | 3.88 | 4.01 | 4.13 | 4.26 |
| **6** | 3.61 | 3.74 | 3.86 | 3.99 | 4.11 | 4.24 | 4.36 | 4.49 | 4.61 | 4.74 | 4.86 |
| **7** | 4.21 | 4.34 | 4.46 | 4.59 | 4.71 | 4.84 | 4.96 | 5.09 | 5.21 | 5.34 | 5.46 |
| **8** | 4.82 | 4.94 | 5.07 | 5.19 | 5.32 | 5.44 | 5.57 | 5.69 | 5.82 | 5.94 | 6.07 |
| **9** | 5.42 | 5.54 | 5.67 | 5.79 | 5.92 | 6.04 | 6.17 | 6.29 | 6.42 | 6.54 | 6.67 |
| **10** | 6.02 | 6.15 | 6.27 | 6.40 | 6.52 | 6.65 | 6.77 | 6.90 | 7.02 | 7.15 | 7.27 |

**Modification Type:** General recommendation, Strength

---

### PP2 - Missense in Constrained Gene

**Original ACMG Summary:** Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| ***Not Applicable*** | Does not apply. RMRP is a non-coding RNA gene. |

---

### PP3 - Computational Evidence

**Original ACMG Summary:** Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).

Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Supporting** | Use RNAsnp to assess SNP effects on local RNA secondary structure. Apply PP3 at supporting level if p-value < 0.1. |

**Tool:** RNAsnp (https://rth.dk/resources/rnasnp/)

**Usage:** Use only for Single Nucleotide Polymorphisms inside the gene (do not use for promoter sequence).

**Parameters:**
- Input sequence: FASTA (Ensembl NR_003051.3)
- Insert SNP details
- Mode: 1
- Folding window: 100 nt
- Measure: "Distance" option
- Minimum length of the sequence interval: 50
- Cut-off the base pair probabilities: 0.01

**Threshold:** p-value < 0.1 (per Sabarinathan et al., 2013; PMID: 23315997). If the value is less than 0.1, apply PP3 as a supporting level of evidence.

**Modification Type:** Gene-specific, Strength

---

### PP4 - Phenotype Specificity

**Original ACMG Summary:** Patient's phenotype or family history is highly specific for a disease with a single genetic etiology.

**VCEP Specifications:**

PP4 applicability and strength is determined by the total points accumulated by a single affected individual according to the point system below.

#### PP4 Strength Thresholds

| Total Points | Strength |
|--------------|----------|
| <1 | PP4 not met |
| 1 to <2 | PP4 (Supporting) |
| ≥2 | PP4_Moderate |

#### PP4 Point System

| Clinical Feature | Points |
|-----------------|--------|
| Diagnostic criteria for SCID/Leaky SCID/Omenn syndrome met (per PIDTC 2022 specification) | 1.0 |
| SCID gene panel or exome/genome sequencing conducted (only applicable if genetic testing did not provide an alternative genetic explanation for SCID/Leaky SCID/Omenn syndrome phenotype) | 0.5 |
| Family history of SCID | 0.5 |
| Family history of CHH | 1.0 |
| Metaphyseal dysplasia (disproportionate short stature + radiographic evidence) | 1.0 |
| Skeletal dysplasia gene panel or WES/WGS conducted with no alternative genetic diagnosis | 1.0 |
| Hypotrichosis | 0.5 |
| Macrocytic, hypoplastic anemia | 0.25 |
| Hirschsprung disease or congenital megacolon | 0.25 |
| T-cell lymphopenia* | 0.5 |
| 3-fold or more reduction of mutant RMRP RNA (or cDNA) expression in peripheral blood mononuclear cells | 2.0 |

**Notes:**
1. The diagnostic criteria for SCID should follow the PIDTC 2022 specification. If maternal T cells are present, the T lymphocyte profile is still considered to be T- (autologous T cells are absent).
2. *Allocate 0.25 points for T-cell lymphopenia only in cases where the SCID diagnostic criteria are not applied. If the SCID diagnostic criteria were applied, the points for the T-B+NK+ lymphocyte subset profile cannot be considered.

**Modification Type:** Disease-specific, Gene-specific, Strength

---

### PP5 - Reputable Source

**Original ACMG Summary:** Reputable source recently reports variant as pathogenic, but the evidence is not available to the laboratory to perform an independent evaluation.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| ***Not Applicable*** | This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PMID: 29543229). |

---

## Benign Criteria

### BA1 - Allele Frequency >5%

**Original ACMG Summary:** Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

**VCEP Specification (Stand Alone):**

- gnomAD popmax filtering allele frequency **>0.00400**
- Maximum credible population allele frequency threshold determined using Whiffin/Ware calculator (https://www.cardiodb.org/allelefrequencyapp/) and the following parameters:
  - Prevalence: 1:5,000
  - Allelic heterogeneity: 1
  - Genetic heterogeneity: 0.04 (based on the contribution of *RMRP* variants to total SCID in the PIDTC 6901 cohort reported in Dvorak et al., 2019 (PMID: 30193840, Table 1): 3.6%, rounded to 4%)
  - Penetrance: 50%
- Use caution when applying BA1 based on allele frequencies derived from gnomAD exome sequencing given the reduced coverage of certain regions of *RMRP*. Ensure at least 20X read depth for allele frequencies derived from exome sequencing.

**Modification Type:** Disease-specific

---

### BS1 - Frequency Greater Than Expected

**Original ACMG Summary:** Allele frequency is greater than expected for disorder.

**VCEP Specification (Strong):**

- gnomAD popmax filtering allele frequency **>0.00089**
- Maximum credible population allele frequency threshold determined using Whiffin/Ware calculator (https://www.cardiodb.org/allelefrequencyapp/) and the following parameters:
  - Prevalence: 1:50,000
  - Allelic heterogeneity: 1
  - Genetic heterogeneity: 0.04 (based on the contribution of *RMRP* variants to total SCID in the PIDTC 6901 cohort reported in Dvorak et al., 2019 (PMID: 30193840, Table 1): 3.6%, rounded to 4%)
  - Penetrance: 100%
- Use caution when applying BS1 based on allele frequencies derived from gnomAD exome sequencing given the reduced coverage of certain regions of *RMRP*. Ensure at least 20X read depth for allele frequencies derived from exome sequencing.

**Modification Type:** Disease-specific

---

### BS2 - Observed in Healthy Adult

**Original ACMG Summary:** Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | Observed in ≥3 (3 or more) homozygotes in gnomAD. |
| **Supporting** | Can be applied at Supporting level of evidence if observed in at least 2 homozygotes in gnomAD. |

**Modification Type:** Gene-specific, Strength

---

### BS3 - Functional Studies (No Effect)

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| ***Not Applicable*** | Does not apply. |

---

### BS4 - Lack of Segregation

**Original ACMG Summary:** Lack of segregation in affected members of a family.

Caveat: The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | Can be applied without additional specifications. To apply the BS4 criteria, it is sufficient to have one affected family member without the segregation of the variant. |

**Note:** One individual is sufficient, as it would be unlikely to have a SCID phenocopy with non-segregation. RMRP has variable penetrance, where family members with similar genotypes may have different phenotypes (PMID: 19150606).

**Modification Type:** None

---

### BP1-BP7 - Benign Supporting

| Criterion | Status | Comment |
|-----------|--------|---------|
| **BP1** | *Not Applicable* | Does not apply. RMRP is a non-coding RNA gene; missense/truncating distinction is not relevant. |
| **BP2** | *Not Applicable* | Does not apply. It remains possible that 2 pathogenic variants appear in cis while an affected individual has an RMRP VUS/LP/P variant on the opposite allele. |
| **BP3** | *Not Applicable* | Does not apply. |
| **BP4** | *Not Applicable* | Does not apply. |
| **BP5** | *Not Applicable* | Does not apply. Studies of patients with "inborn errors of immunity" show that ~10% of cases carry molecular defects that contribute to the phenotype (PMIDs: 27577878, 35753512). Co-occurring immune deficiencies (e.g., FOXN1 and RMRP) are plausible. |
| **BP6** | *Not Applicable* | This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PMID: 29543229). |
| **BP7** | *Not Applicable* | Does not apply. |

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

### Appendix A: Criteria Summary Table

| Criterion | VCEP Strength | Status | Key Modification |
|-----------|--------------|--------|-----------------|
| PVS1 | — | Not Applicable | Non-coding RNA gene |
| PS1 | Supporting | Modified | Downgraded; same position, different nucleotide |
| PS2 | Variable (Supporting–Very Strong) | Modified | Point-based system with PP4-linked phenotype consistency |
| PS3 | Strong / Supporting | Modified | RT/PCR absent expression (Strong); approved in vitro assays (Supporting) |
| PS4 | — | Not Applicable | Autosomal recessive disorder |
| PM1 | Strong | Modified | Insertions/duplications between TATA box and TSS |
| PM2 | Supporting | Modified | Downgraded; FAF <0.0000447 |
| PM3 | Variable (Supporting–Very Strong) | Modified | SVI point-based system; co-occurring variant must use SCID VCEP specs |
| PM4 | Moderate | Modified | Insertions/duplications ≥6 nt between TATA box and TSS |
| PM5 | — | Not Applicable | Non-coding RNA gene |
| PM6 | Variable (Supporting–Strong) | Modified | Same PS2 point-based system |
| PP1 | Variable (Supporting–Strong) | Modified | SVI co-segregation with RMRP-specific carrier requirement |
| PP2 | — | Not Applicable | Non-coding RNA gene |
| PP3 | Supporting | Modified | RNAsnp tool; p-value <0.1 |
| PP4 | Supporting / Moderate | Modified | Point-based phenotype system (CHH/SCID features) |
| PP5 | — | Not Applicable | Per SVI recommendation |
| BA1 | Stand Alone | Modified | FAF >0.00400 |
| BS1 | Strong | Modified | FAF >0.00089 |
| BS2 | Strong / Supporting | Modified | ≥3 homozygotes (Strong); ≥2 homozygotes (Supporting) |
| BS3 | — | Not Applicable | — |
| BS4 | Strong | Default | One affected family member without segregation sufficient |
| BP1–BP7 | — | Not Applicable | All not applicable |

### Appendix B: Population Frequency Thresholds Summary

| Criterion | Threshold | Strength | Whiffin/Ware Parameters |
|-----------|-----------|----------|------------------------|
| BA1 | >0.00400 | Stand Alone | Prevalence 1:5,000; Allelic het. 1; Genetic het. 0.04; Penetrance 50% |
| BS1 | >0.00089 | Strong | Prevalence 1:50,000; Allelic het. 1; Genetic het. 0.04; Penetrance 100% |
| PM2 | <0.0000447 | Supporting | — |

### Appendix C: Reference PMIDs

| PMID | Reference | Context |
|------|-----------|---------|
| 16252239 | Thiel et al., 2005 | Endonucleolytic cleavage activity assay (PS3) |
| 17701897 | Thiel et al., 2007 | Endonucleolytic cleavage activity assay (PS3) |
| 16254002 | Hermanns et al., 2005 | Luciferase reporter assay (PS3) |
| 23315997 | Sabarinathan et al., 2013 | RNAsnp p-value threshold (PP3) |
| 30311386 | Oza et al., 2018 | Co-segregation recommendations (PP1) |
| 30193840 | Dvorak et al., 2019 | PIDTC 6901 cohort, RMRP contribution to SCID (BA1/BS1) |
| 29543229 | Biesecker et al., 2018 | SVI recommendation against PP5/BP6 |
| 19150606 | Makitie et al., 2009 | Variable penetrance in RMRP (BS4) |
| 27577878 | — | Inborn errors of immunity, molecular defects (BP5) |
| 35753512 | — | Inborn errors of immunity, molecular defects (BP5) |

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.2.0 | 1/20/2026 | Attached RMRP Corrections 1.6.26; Updated PM1 Strong specifications (rarity caveat aligned with PM3); Added PM3 Minor Amendments document (Proband-Family terminology, consanguinity definitions); Attached "VCEP Comments: Updates to PM1 10/23/25"; Attached "RMRP Corrections 12.12.2025" |
| 1.1.0 | — | Prior version with PM1 requiring PM2 threshold |

---

*This document was compiled from ClinGen VCEP specifications and ClinGen SVI recommendations. For the most current version, please refer to the ClinGen website.*
