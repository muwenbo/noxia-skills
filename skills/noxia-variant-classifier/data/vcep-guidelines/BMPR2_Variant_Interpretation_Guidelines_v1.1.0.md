# ClinGen Pulmonary Hypertension Expert Panel Variant Interpretation Guidelines for BMPR2

**Version:** 1.1.0
**Released:** 4/6/2024
**Affiliation:** Pulmonary Hypertension VCEP
**Based on:** Richards et al., 2015 ACMG/AMP Guidelines

---

## Gene Information

| Attribute | Value |
|-----------|-------|
| **Gene** | BMPR2 (HGNC:1078) |
| **HGNC Name** | bone morphogenetic protein receptor type 2 |
| **Transcript** | NM_001204.7 |
| **Disease** | Pulmonary arterial hypertension (MONDO:0015924) |
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
   - [BA1 - Allele Frequency >1%](#ba1---allele-frequency-1)
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

- **Biologically relevant transcript:** NM_001204.7
- **NMD boundary:** LOF variants 5' or at c.2816 (exons 1-12) are expected to undergo NMD. Variants 3' to c.2816 (exon 13) are not expected to undergo NMD
- **Exon 13:** Does not contain regions critical for protein function and encodes <10% of the protein
- **Exception:** p.Trp13X (W13X) is known to escape NMD and produce a truncated protein (PMID: 20095988)
- **Critical regions for protein function:**
  - Ligand binding domain (aa 33-131)
  - Kinase domain (aa 203-504)
  - Heterodimerization domain (aa 485-492)
  - Transmembrane domain (aa 151-171)
- **Canonical splice variants:** RNA splicing assay data is not necessary for applying PVS1; follow the decision tree based on the predicted effect of disrupted splicing
- **In-frame exons:** Exons 1, 2, 3, 4, 6 are in-frame and a loss of a canonical splice acceptor/donor is not expected to result in NMD
- **Non-canonical splice site variants:** May be applicable for PVS1 according to the decision tree when RNA splicing assay data is available
- **Initiation codon:** Located in exon 1. There are approximately 27 in-frame downstream AUG initiation codons including 5 sites located in exons 4-6 having translation initiation scores similar or greater than the exon 1 codon (PMID: 20095988). However, there are many P/LP variants upstream of exons 4-6

#### Strength Levels

| Strength | Criteria |
|----------|----------|
| **Very Strong** | Null variant (nonsense, frameshift, canonical +/-1 or 2 splice sites, initiation codon, single or multi-exon deletion) where LOF is a known mechanism. **Use the PVS1 decision tree guide.** |
| **Strong** | Use the PVS1 decision tree guide |
| **Moderate** | Use the PVS1 decision tree guide |

#### PVS1 Decision Tree Summary

| Variant Type | Condition | PVS1 Strength |
|--------------|-----------|---------------|
| **Nonsense/Frameshift** | Predicted to undergo NMD (5' or at c.2816, exons 1-12), exon present in NM_001204.7 | PVS1 |
| **Nonsense/Frameshift** | Not predicted to undergo NMD (3' to c.2816/exon 13 or p.Trp13X), removes >10% protein | PVS1_Strong |
| **Nonsense/Frameshift** | Not predicted to undergo NMD, removes <10% protein | PVS1_Moderate |
| **Canonical splice (+/-1,2)** | Exon skipping disrupts reading frame + NMD predicted, exon present | PVS1 |
| **Canonical splice (+/-1,2)** | Exon skipping disrupts reading frame, NOT predicted to undergo NMD, removes >10% protein | PVS1_Strong |
| **Canonical splice (+/-1,2)** | Exon skipping disrupts reading frame, NOT predicted to undergo NMD, removes <10% protein | PVS1_Moderate |
| **Canonical splice (+/-1,2)** | Exon skipping preserves reading frame (in-frame exons: 1,2,3,4,6), removes >10% protein | PVS1_Strong |
| **Canonical splice (+/-1,2)** | Exon skipping preserves reading frame, removes <10% protein | PVS1_Moderate |
| **Non-canonical splice + RNA data** | Loss of wt acceptor/donor, disrupts reading frame, and/or affects critical region | PVS1 |
| **Deletion (single to full gene)** | Full gene deletion | PVS1 |
| **Deletion** | Disrupts reading frame + NMD predicted (exons 1-12), exon present | PVS1 |
| **Deletion** | Disrupts reading frame, NOT predicted to undergo NMD, removes <10% protein | PVS1_Moderate |
| **Deletion** | Preserves reading frame, affects critical region | PVS1_Strong |
| **Duplication (proven in tandem)** | Reading frame disrupted + NMD predicted (exons 1-12) | PVS1 |
| **Duplication (presumed in tandem)** | Reading frame presumed disrupted + NMD predicted (exons 1-12) | PVS1_Strong |
| **Initiation codon** | No known alternative start codon, >=1 P/LP variant upstream of closest potential in-frame start codon | PVS1_Moderate |

---

### PS1 - Same Amino Acid Change

**Original ACMG Summary:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change. Example: Val->Leu caused by either G>C or G>T in the same codon.

**Caveat:** Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | Same amino acid change as a previously established *pathogenic* variant regardless of nucleotide change |
| **Moderate** | Same amino acid change as a previously established *likely pathogenic* variant regardless of nucleotide change |

**Modification Type:** Strength (for Moderate level)

---

### PS2 - De Novo (Confirmed)

**Original ACMG Summary:** De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.

**Note:** Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | De novo (both maternity and paternity confirmed) in a patient with the disease and no family history |

**Modification Type:** No change

---

### PS3 - Functional Studies

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.

**Note:** Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.

**VCEP Specifications:**

PS3 can be applied additively with PP3 if applicable.

| Strength | Criteria |
|----------|----------|
| **Strong** | Use the BMPR2 functional assay document for guidance on allowable assays. Known variant validation controls (i.e. established pathogenic and benign variants) are required. One exception is if the same functional assay has been performed for the same variant by two independent groups and demonstrated to have the same functional effect by both groups. Also applicable for non-canonical splice site variants when RNA splice site assay data is available demonstrating abnormal splicing; positive and negative controls are required, preferably from patients and matched unaffected individuals. Note that splicing assay results may be tissue-sensitive. |
| **Supporting** | Use the BMPR2 functional assay document for guidance on allowable assays. If no known variant validation controls (i.e. established pathogenic and benign variants) were used, then score at the supporting strength. |

**Modification Type:** General recommendation, Gene-specific

#### Approved Functional Assays

The following functional assays have been validated for BMPR2 variant assessment:

**1. Gene Reporter Assay (Luciferase)**

| Parameter | Details |
|-----------|---------|
| **PMID** | 12045205 |
| **Author** | Rudarakanchana et al. |
| **Year** | 2002 |
| **Method** | Luciferase reporter assay measuring BMP-responsive element activity |
| **Validation** | Tested pathogenic and benign controls |
| **Interpretation** | Reduced activity indicates loss of function |

**2. Cell Surface Localization Assay**

| Parameter | Details |
|-----------|---------|
| **Method** | GFP- or myc-tagged BMPR2 constructs |
| **Interpretation** | Cytoplasmic retention indicates protein misfolding |

**3. RNA Splicing Assay**

| Parameter | Details |
|-----------|---------|
| **Requirements** | Positive and negative controls required |
| **Note** | Splicing assay results may be tissue-sensitive |

---

### PS4 - Prevalence in Affected

**Original ACMG Summary:** The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.

**Notes:**
- Note 1: Relative risk (RR) or odds ratio (OR), as obtained from case-control studies, is >5.0 and the confidence interval around the estimate of RR or OR does not include 1.0
- Note 2: In instances of very rare variants where case-control studies may not reach statistical significance, the prior observation of the variant in multiple unrelated patients with the same phenotype, and its absence in controls, may be used as moderate level of evidence

**VCEP Specifications:**

Affected individuals are defined as having a mean pulmonary artery pressure (mPAP) >20 mm Hg by right heart catheterization (RHC), or estimated by echocardiography if RHC is not advised.

Strength is based on the number of unrelated PAH (heritable and/or idiopathic) probands identified with a variant. Unpublished, VCEP-approved internal case/variant data is acceptable if the proband does not have another pathogenic or likely pathogenic BMPR2 variant.

**Note:** PS4 (at any strength) and PM2_supporting can be used additively.

| Strength | Criteria |
|----------|----------|
| **Strong** | Prior observation of the variant in **>4 unrelated patients** with the same phenotype, and its absence in controls |
| **Moderate** | Prior observation of the variant in **>3 unrelated patients** with the same phenotype, and its absence in controls |
| **Supporting** | Prior observation of the variant in **>1 unrelated patients** with the same phenotype, and its absence in controls |

**Modification Type:** Disease-specific

#### Supporting Data for PS4 Thresholds

| # Patients with same BMPR2 variant | Machado et al 2015 | Southgate et al 2020 |
|---|---|---|
| >=3 patients | 51/384 (13.3%) | 50/486 (10.3%) |
| 2 patients | 55/384 (14.3%) | 67/486 (13.8%) |
| 1 patient | 278/384 (72.4%) | 369/486 (75.9%) |

---

### PM1 - Mutational Hot Spot

**Original ACMG Summary:** Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.

**VCEP Specifications:**

Well-established functional domains for BMPR2 include:
- Extracellular (ligand-binding) domain
- Protein kinase domain
- Heterodimerization motif within the kinase domain

Strong evidence based on evolutionary conservation, *in vitro* functional assays, and protein structural analyses indicates the critical (or non-critical) nature of specific amino acid residues within each of these domains. Strength should be applied accordingly.

| Strength | Criteria |
|----------|----------|
| **Strong** | Variant changes a *critical* amino acid |
| **Moderate** | Variant changes an amino acid in the extracellular domain (aa 33-131) or kinase domain (aa 203-504) but without functional evidence indicating critical or non-critical |

**Modification Type:** Gene-specific, Strength

#### Critical Amino Acids (PM1_Strong)

| Domain | Critical Residues |
|--------|-------------------|
| **Extracellular domain** | p.Cys34, Cys60, Cys66, Cys84, Cys94, Cys99, Cys116, Cys117, Cys118, Cys123 |
| **Kinase domain** | p.Gly210, Gly212, Lys230, Glu/Asn245, Asp333, Asn338, Asp351, Gly353, Glu386, Asp405, Gly410, Arg491 |
| **KD heterodimerization** | p.Asp485, Gln486, Asp487, Ala488, Arg489, Ala490, Arg491, Leu492 |

#### Non-Critical Residues (Apply BS3)

The following residues have been demonstrated *non-critical/not necessary* for kinase activity based on a luciferase assay:
- p.Gln42Arg, Gly47Gln, Gln82His, Thr102Ala, Ser107Pro, Gly182Asp, Met186Val, Glu503Asp, Arg899X, Arg899Pro

#### Scientific Basis for Critical Residues

**Extracellular Domain:**
The 10 invariant cysteine residues in the BMPR2 ECD are required for correct protein folding. *In vitro* mutagenesis and X-crystallography studies identified these cysteine residues conserved across the related type II BMP, MIS, and activin receptors, each of which is necessary for receptor ligand protein folding of the ligand domain (Greenwald et al., 1999; Machado et al., 2006).

**Kinase Domain:**
- **Invariant residues:** G212, K230, D333, N338, D351, E386, D405, R491
- **Nearly invariant residues:** G210, E/N245, G353, G410
- The invariant arginine at position 491 is indispensable for signaling since it forms an ion pair with a highly conserved glutamic acid at position 386 (Zhang et al., 1994; Hanks and Hunter, 1995)

**Heterodimerization Domain (aa 485-492):**
Hydrogen deuterium exchange mass spectrometry (HDX-MS), small angle X-ray scattering (SAXS), and molecular dynamics simulations have shown that the alphaH-alphaI linker (residues 485-492) is critical for type I receptor dimerization. Several PAH-causing mutations (C483R, D485G, D487V, A490D/V, R491W/Q) cluster at this dimer interface.

---

### PM2 - Absent from Controls

**Original ACMG Summary:** Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

**Caveat:** Population data for indels may be poorly called by next generation sequencing.

**VCEP Specifications:**

PAH has a prevalence of 15-50 cases/million individuals and the population allele frequency threshold for PM2 is based on this frequency. There is no evidence for a genetic ancestry effect on PAH prevalence, so the use of any sub-population data is acceptable (as long as there is a minimum allele count of 1,000).

As specified by the SVI WG, PM2 is scored at the **supporting level only**.

**Note:** PM2_supporting and PS4 (at any strength) can be used additively.

| Strength | Criteria |
|----------|----------|
| **Supporting** | Present at **<0.01%** among gnomAD controls, using the subpopulation with the highest frequency and at least 1,000 allele counts |

**Modification Type:** Disease-specific

---

### PM3 - In Trans with Pathogenic

**Original ACMG Summary:** For recessive disorders, detected in trans with a pathogenic variant. Note: This requires testing of parents (or offspring) to determine phase.

**VCEP Specifications:**

***Not Applicable***

**Comments:** PAH is autosomal dominant.

---

### PM4 - Protein Length Changes

**Original ACMG Summary:** Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Moderate** | Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants |

**Modification Type:** No change

---

### PM5 - Novel Missense at Same Residue

**Original ACMG Summary:** Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before. Example: Arg156His is pathogenic; now you observe Arg156Cys.

**Caveat:** Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Moderate** | Novel missense change at an amino acid residue where a different missense change determined to be *pathogenic* has been seen before. Also applicable for variants affecting the same splice site as a confirmed splice variant with similar or worse splicing in silico predictions |
| **Supporting** | Novel missense change at an amino acid residue where a different missense change determined to be *likely pathogenic* has been seen before |

**Modification Type:** General recommendation, Strength

---

### PM6 - De Novo (Assumed)

**Original ACMG Summary:** Assumed de novo, but without confirmation of paternity and maternity.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Moderate** | Assumed de novo, but without confirmation of paternity and maternity |

**Modification Type:** No change

---

### PP1 - Co-segregation

**Original ACMG Summary:** Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease. Note: May be used as stronger evidence with increasing segregation data.

**VCEP Specifications:**

**Note:** PAH exhibits variable age of onset and incomplete penetrance.

Three levels of evidence are applied based on autosomal dominant likelihood ratios of 10 (3 meioses, LOD 0.9, supporting), 30 (5 meioses, LOD 1.5, moderate), and 100 (7 meioses, LOD 2.1, strong) provided that PM2 (absent or rare in large population cohorts) is met.

Demonstration of segregation in more than one family is not necessary as *BMPR2* is a well-established PAH gene. (PMID: 29300372)

| Strength | Criteria |
|----------|----------|
| **Strong** | Co-segregation with disease in **>=7 affected family members** |
| **Moderate** | Co-segregation with disease in **>=5 affected family members** |
| **Supporting** | Co-segregation with disease in **>=3 affected family members** |

**Modification Type:** Strength

---

### PP2 - Missense in Constrained Gene

**Original ACMG Summary:** Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.

**VCEP Specifications:**

***Not Applicable***

**Comments:** BMPR2 is not constrained for missense variants.

---

### PP3 - Computational Evidence

**Original ACMG Summary:** Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).

**Caveat:** As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Supporting** | REVEL >=0.75 for missense variants OR SpliceAI >=0.2 for non-canonical splice variants. No up/downgrading. If no REVEL score or SpliceAI prediction is available, then CADD >=20 can be used. |

**Note:** Can be applied additively with PS3 if applicable.

**Modification Type:** General recommendation

---

### PP4 - Phenotype Specificity

**Original ACMG Summary:** Patient's phenotype or family history is highly specific for a disease with a single genetic etiology.

**VCEP Specifications:**

***Not Applicable***

**Comments:** PAH does not have a single genetic etiology.

---

### PP5 - Reputable Source

**Original ACMG Summary:** Reputable source recently reports variant as pathogenic, but the evidence is not available to the laboratory to perform an independent evaluation.

**VCEP Specifications:**

***Not Applicable***

This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee. (PMID: 29543229)

---

## Benign Criteria

### BA1 - Allele Frequency >1%

**Original ACMG Summary:** Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Stand Alone** | Allele frequency is above **1%** in gnomAD, including any sub-population with at least 1,000 allele counts |

**Modification Type:** Disease-specific

---

### BS1 - Frequency Greater Than Expected

**Original ACMG Summary:** Allele frequency is greater than expected for disorder.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | Allele frequency **>=0.1%** among gnomAD controls, using the subpopulation with the highest frequency and at least 1,000 allele counts |

**Modification Type:** Disease-specific

---

### BS2 - Observed in Healthy Adult

**Original ACMG Summary:** Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

**VCEP Specifications:**

Strength based on number of homozygotes observed among gnomAD controls. Criteria not applicable for heterozygotes as *BMPR2* variants exhibit incomplete penetrance.

| Strength | Criteria |
|----------|----------|
| **Strong** | Observed in **>=3 homozygotes** in gnomAD controls or reported in the literature (healthy adult individuals) |
| **Supporting** | Observed in **>=2 homozygotes** in gnomAD controls or reported in the literature (healthy adult individuals) |

**Modification Type:** Disease-specific, Gene-specific

---

### BS3 - Functional Studies (No Effect)

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | Use the BMPR2 functional assay document for acceptable assays and guidance |

**Modification Type:** Gene-specific

**Pre-classified Non-Critical Residues (BS3 applicable):**
- p.Gln42Arg, Gly47Gln, Gln82His, Thr102Ala, Ser107Pro, Gly182Asp, Met186Val, Glu503Asp, Arg899X, Arg899Pro

These residues have been demonstrated non-critical/not necessary for kinase activity based on a luciferase assay.

**Note:** Residues p.Cys34, Cys60, Cys66, Cys84, Cys94, Cys99, Cys116, Cys117, Cys118, Cys123, Gly210, Gly212, Lys230, Glu/Asn245, Asp333, Asn338, Asp351, Gly353, Glu386, Asp405, Gly410, Asp485, Gln486, Asp487, Ala488, Arg489, Ala490, Arg491, and Leu492 have been demonstrated *critical* (apply PM1_strong instead).

---

### BS4 - Lack of Segregation

**Original ACMG Summary:** Lack of segregation in affected members of a family.

**Caveat:** The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.

**VCEP Specifications:**

Lack of disease segregation among *BMPR2* variant carriers should **not** be scored due to low penetrance of PAH variants in families. Lack of variant segregation in affected family members **should** be scored.

| Strength | Criteria |
|----------|----------|
| **Strong** | Lack of variant segregation in affected members of a family |

**Modification Type:** No change

---

### BP1-BP7 - Benign Supporting

| Criterion | Status | Comment |
|-----------|--------|---------|
| **BP1** | Not Applicable | Both LOF and missense variants are known to cause PAH |
| **BP2** | Not Applicable | BMPR2 variants are not fully penetrant |
| **BP3** | Supporting | In frame-deletions/insertions in a repetitive region without a known function (No change) |
| **BP4** | Supporting | REVEL <=0.25 for missense variants OR SpliceAI <=0.1 for non-canonical splice variants. No up/downgrading. If no REVEL or SpliceAI available, then CADD <=10 can be used |
| **BP5** | Not Applicable | BMPR2 is the major causal PAH gene |
| **BP6** | Not Applicable | Not for use per ClinGen SVI WG recommendation (PMID: 29543229) |
| **BP7** | Supporting/Strong | See BP7 specifications below |

#### BP7 Specifications

| Strength | Criteria |
|----------|----------|
| **Strong** | If BP7 is met and negative RNA splicing assay data is available, then apply BP7_strong. Acceptable splicing assays should have positive and negative controls, preferably from patients and matched unaffected individuals. Note that splicing assay results may be tissue-sensitive. |
| **Supporting** | A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved. Applicable after assignment of BP4 for no adverse splicing predictions, and inclusive of exonic and intronic variants. **Not applicable** for synonymous variants located at the first base or the last three bases of an exon. |

**Note:** Use default SpliceAI predictions.

---

## Rules for Combining Criteria

### Pathogenic Classification

| Criteria Combination |
|---------------------|
| 1 Very Strong (PVS1) **AND** >=1 Strong (PVS1_Strong, PS1, PS2, PS3, PS4, PM1_Strong, PP1_Strong) |
| 1 Very Strong (PVS1) **AND** >=2 Moderate (PVS1_Moderate, PS1_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate) |
| 1 Very Strong (PVS1) **AND** 1 Moderate (PVS1_Moderate, PS1_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate) **AND** 1 Supporting (PS3_Supporting, PS4_Supporting, PM2_Supporting, PM5_Supporting, PP1, PP3) |
| 1 Very Strong (PVS1) **AND** >=2 Supporting (PS3_Supporting, PS4_Supporting, PM2_Supporting, PM5_Supporting, PP1, PP3) |
| >=2 Strong (PVS1_Strong, PS1, PS2, PS3, PS4, PM1_Strong, PP1_Strong) |
| 1 Strong (PVS1_Strong, PS1, PS2, PS3, PS4, PM1_Strong, PP1_Strong) **AND** >=3 Moderate (PVS1_Moderate, PS1_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate) |
| 1 Strong (PVS1_Strong, PS1, PS2, PS3, PS4, PM1_Strong, PP1_Strong) **AND** 2 Moderate (PVS1_Moderate, PS1_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate) **AND** >=2 Supporting (PS3_Supporting, PS4_Supporting, PM2_Supporting, PM5_Supporting, PP1, PP3) |
| 1 Strong (PVS1_Strong, PS1, PS2, PS3, PS4, PM1_Strong, PP1_Strong) **AND** 1 Moderate (PVS1_Moderate, PS1_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate) **AND** >=4 Supporting (PS3_Supporting, PS4_Supporting, PM2_Supporting, PM5_Supporting, PP1, PP3) |

### Likely Pathogenic Classification

| Criteria Combination |
|---------------------|
| 1 Very Strong (PVS1) **AND** 1 Moderate (PVS1_Moderate, PS1_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate) |
| 1 Strong (PVS1_Strong, PS1, PS2, PS3, PS4, PM1_Strong, PP1_Strong) **AND** 1 Moderate (PVS1_Moderate, PS1_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate) |
| 1 Strong (PVS1_Strong, PS1, PS2, PS3, PS4, PM1_Strong, PP1_Strong) **AND** >=2 Supporting (PS3_Supporting, PS4_Supporting, PM2_Supporting, PM5_Supporting, PP1, PP3) |
| >=3 Moderate (PVS1_Moderate, PS1_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate) |
| 2 Moderate (PVS1_Moderate, PS1_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate) **AND** >=2 Supporting (PS3_Supporting, PS4_Supporting, PM2_Supporting, PM5_Supporting, PP1, PP3) |
| 1 Moderate (PVS1_Moderate, PS1_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate) **AND** >=4 Supporting (PS3_Supporting, PS4_Supporting, PM2_Supporting, PM5_Supporting, PP1, PP3) |
| 1 Strong (PVS1_Strong, PS1, PS2, PS3, PS4, PM1_Strong, PP1_Strong) **AND** 2 Moderate (PVS1_Moderate, PS1_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate) |

### Benign Classification

| Criteria Combination |
|---------------------|
| >=2 Strong (BS1, BS2, BS3, BS4, BP7_Strong) |
| 1 Stand Alone (BA1) |

### Likely Benign Classification

| Criteria Combination |
|---------------------|
| 1 Strong (BS1, BS2, BS3, BS4, BP7_Strong) **AND** 1 Supporting (BS2_Supporting, BP3, BP4, BP7) |
| >=2 Supporting (BS2_Supporting, BP3, BP4, BP7) |

---

## Appendices

### Appendix A: Population Frequency Thresholds Summary

| Criterion | Threshold | Strength |
|-----------|-----------|----------|
| BA1 | >1% | Stand Alone |
| BS1 | >=0.1% | Strong |
| PM2 | <0.01% | Supporting |

**Notes:**
- Use gnomAD subpopulation with highest frequency
- Minimum allele count of 1,000 required
- PAH prevalence: 15-50 cases per million individuals

### Appendix B: BMPR2 Protein Domains

| Domain | Amino Acid Range | Function |
|--------|------------------|----------|
| Signal peptide | 1-26 | Protein targeting |
| Extracellular/Ligand-binding | 33-131 | BMP ligand binding |
| Transmembrane | 151-171 | Membrane anchoring |
| Kinase domain | 203-504 | Serine/threonine kinase activity |
| Heterodimerization motif | 485-492 | Type I receptor interaction |
| Cytoplasmic tail | 505-1038 | Regulatory functions |

### Appendix C: NMD Prediction

| Region | NMD Status |
|--------|------------|
| 5' or at c.2816 (exons 1-12) | Expected to undergo NMD |
| 3' to c.2816 (exon 13) | NOT expected to undergo NMD |
| p.Trp13X (W13X) | Known to escape NMD |

**In-frame exons (splice variants not expected to result in NMD):** Exons 1, 2, 3, 4, 6

### Appendix D: Computational Prediction Thresholds

| Tool | Pathogenic Threshold (PP3) | Benign Threshold (BP4) |
|------|---------------------------|------------------------|
| REVEL | >=0.75 | <=0.25 |
| SpliceAI | >=0.2 | <=0.1 |
| CADD (alternative) | >=20 | <=10 |

### Appendix E: Reference PMIDs

| PMID | Description |
|------|-------------|
| 20095988 | W13X NMD escape; alternative start codons |
| 12045205 | Functional analysis of BMPR2 mutations (Rudarakanchana et al., 2002) |
| 26387786 | BMPR2 variant catalog (Machado et al., 2015) |
| 31406341 | Molecular genetic framework for PAH (Southgate et al., 2020) |
| 29543229 | ClinGen SVI recommendation against PP5/BP6 |
| 29300372 | Segregation analysis guidelines |
| 9886286 | Extracellular domain structure (Greenwald et al., 1999) |
| 7768349 | Kinase domain structure (Hanks and Hunter, 1995) |
| 12221115 | Functional heterogeneity of BMPR2 mutants (Nishihara et al., 2002) |

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.1.0 | 4/6/2024 | Formatting edit only |
| 1.0.0 | Initial | Initial release |

---

*This document was compiled from ClinGen VCEP specifications. For the most current version, please refer to the ClinGen website.*

*Generated based on ClinGen Pulmonary Hypertension Expert Panel Specifications to the ACMG/AMP Variant Interpretation Guidelines for BMPR2.*
