# ClinGen Familial Hypercholesterolemia VCEP Variant Interpretation Guidelines for LDLR

**Version:** 1.2.0
**Released:** 11/9/2021
**Affiliation:** Familial Hypercholesterolemia VCEP (ClinGen Affiliation 50004)
**Based on:** Richards et al., 2015 ACMG/AMP Guidelines
**Related Publication:** https://doi.org/10.1101/2021.03.17.21252755
**Release Notes:** Updated for clarification on PM3 and BP2, and typo correction.

---

## Gene Information

| Attribute | Value |
|-----------|-------|
| **Gene** | LDLR (HGNC:6547) |
| **HGNC Name** | low density lipoprotein receptor |
| **Transcript** | NM_000527.5 |
| **Disease** | hypercholesterolemia, familial (MONDO:0007750) |
| **Inheritance** | Autosomal Dominant (heterozygous FH); Autosomal Recessive (homozygous FH) |

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
   - [BA1 - Allele Frequency >0.5%](#ba1---allele-frequency-05)
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
- Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7).
- Use caution interpreting LOF variants at the extreme 3' end of a gene.
- Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact.
- Use caution in the presence of multiple transcripts.

**VCEP Specifications:** See PVS1 flow diagram (Figure 1 / Appendix A). LDLR-specific recommendations adapted from Tayoun et al., 2018.

**Modification Type:** Disease-specific, Strength

#### Strength Levels

| Strength | Criteria |
|----------|----------|
| **Very Strong (PVS1)** | See PVS1 flow diagram (Figure 1). Null variants (nonsense, frameshift, canonical +/-1 or 2 splice sites, initiation codon, single or multi-exon deletion) where LOF is the known mechanism. |
| **Strong (PVS1_Strong)** | See PVS1 flow diagram (Figure 1). Downgraded from Very Strong per flowchart when specific conditions apply (e.g., exon skipping with in-frame result, variants in last exon). |
| **Moderate (PVS1_Moderate)** | See PVS1 flow diagram (Figure 1). Further downgraded per flowchart based on transcript and NMD considerations. |
| **Supporting** | See PVS1 flow diagram (Figure 1). Lowest applicable PVS1 strength. |

---

### PS1 - Same Amino Acid Change

**Original ACMG Summary:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong (PS1)** | Missense variant at the same codon as a variant classified pathogenic (by these guidelines), and predicts the same amino acid change. **Caveat:** there is no in silico predicted splicing impact for either variant. |

**Modification Type:** Clarification

---

### PS2 - De Novo (Confirmed)

**Original ACMG Summary:** De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.

**Note:** Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.

**VCEP Specifications:** Variant is de novo in a patient with the disease and no family history. Follow SVI guidance for de novo occurrences: https://clinicalgenome.org/working-groups/sequence-variant-interpretation/

**Modification Type:** Clarification

---

### PS3 - Functional Studies

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.

**Note:** Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong (PS3 - Level 1)** | Study of the whole LDLR cycle (LDLR expression/biosynthesis, LDL binding, and LDL internalization) performed in heterologous cells (with no endogenous LDLR) transfected with mutant plasmid. Assay result of **<70% of wild-type activity** in either expression/biosynthesis, binding **OR** internalization. |
| **Moderate (PS3_Moderate - Level 2)** | See Level 2 criteria below. |
| **Supporting (PS3_Supporting - Level 3)** | See Level 3 criteria below. |

**Modification Type:** Disease-specific, Strength

#### Level 2 (PS3_Moderate) Detailed Criteria

1. Study of **only part** of the LDLR cycle following Level 1 methodology, **or** whole or part of the LDLR cycle in true homozygous patient cells. Assay result of **<70% of wild-type activity** in either LDLR expression/biosynthesis, LDL binding OR internalization.
2. RNA studies, using RNA extracted from heterozygous or true homozygous patient cells, where aberrant transcript is confirmed by sequencing and is quantified as **>25% of total transcript** from heterozygous cells or **50% of total transcript** from homozygous cells.
3. Variants with **two or more Level 3 functional studies** (must be different assays); or any Level 3 functional study #1-4 performed by **two or more independent labs** with concordant results.

#### Level 3 (PS3_Supporting) Detailed Criteria

1. Study of LDLR cycle (whole or part) in heterozygous patient cells, with assay result of **<85% of wild-type activity** in either LDLR expression/biosynthesis, LDL binding OR internalization.
2. Luciferase studies with transcription levels of **<50%** compared to wild-type (applicable to 5'UTR/promoter variants).
3. Minigene splicing assays with **<10% wild-type transcript** present where an aberrant transcript from the candidate variant is confirmed by sequencing.
4. High-throughput assays, including alternative microscopy assays (e.g., Thormaehlen et al., 2015), Multiplex Assays of Variant Effect (MAVE) (e.g., Weile & Roth, 2018) and deep mutational scanning assays, only if the assay has been validated with a **minimum of four pathogenic and four benign variant controls** in LDLR. *Note: % activity thresholds will be defined by the FH VCEP as more data becomes available.*
5. RNA studies, using RNA extracted from heterozygous or homozygous patient cells, with aberrant transcript confirmed by sequencing (but **without transcript quantification**).

> **Note:** Functional assays performed in compound heterozygous patient cells are not considered applicable in PS3/BS3 criteria since it is difficult to delineate the individual effect of each variant.

---

### PS4 - Prevalence in Affected

**Original ACMG Summary:** The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong (PS4)** | Variant is found in **>=10 unrelated FH cases** (FH diagnosis met by validated clinical criteria). **Caveat:** variant must also meet PM2. |
| **Moderate (PS4_Moderate)** | Variant is found in **6-9 unrelated FH cases** (FH diagnosis made by validated clinical criteria). **Caveat:** variant must also meet PM2. |
| **Supporting (PS4_Supporting)** | Variant is found in **2-5 unrelated FH cases** (FH diagnosis made by validated clinical criteria). **Caveat:** variant must also meet PM2. |

**Modification Type:** Disease-specific, Strength

---

### PM1 - Mutational Hot Spot

**Original ACMG Summary:** Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Moderate (PM1)** | Missense variant located in **exon 4**, or a missense change in one of **60 highly conserved cysteine residues** (listed in Appendix B). **Caveat:** variant must also meet PM2. |

**Modification Type:** Disease-specific

---

### PM2 - Absent from Controls

**Original ACMG Summary:** Absent from controls (or at extremely low frequency if recessive) in population databases.

**VCEP Specification (Moderate):**
- Variant has a **PopMax MAF <=0.0002 (0.02%)** in gnomAD.
- Consider exceptions for known founder variants.

**Note:** PopMax refers to the gnomAD subpopulation with the highest allele frequency.

**Modification Type:** Disease-specific

---

### PM3 - In Trans with Pathogenic

**Original ACMG Summary:** For recessive disorders, detected in trans with a pathogenic variant.

**Note:** This requires testing of parents (or offspring) to determine phase.

**VCEP Specifications:** This criterion can be used for a candidate LDLR variant observed in an individual with a **homozygous FH phenotype** when there is only one other pathogenic or likely pathogenic variant in **LDLR (in trans), APOB or PCSK9**. **Caveat:** variant must also meet PM2.

**Modification Type:** Disease-specific

---

### PM4 - Protein Length Changes

**Original ACMG Summary:** Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Moderate (PM4)** | In-frame deletion/insertions smaller than one whole exon, or in-frame whole-exon duplications not considered in any PVS1 criteria. **Caveat:** variant must also meet PM2. |

**Modification Type:** Disease-specific

---

### PM5 - Novel Missense at Same Residue

**Original ACMG Summary:** Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong (PM5_Strong)** | Missense variant at a codon with **>=2 missense variants classified pathogenic** (by these guidelines), and predicts a different amino acid change. |
| **Moderate (PM5)** | Missense variant at the same codon as a variant classified pathogenic (by these guidelines), and predicts a different amino acid change. |

**Modification Type:** Strength (PM5_Strong); Clarification (PM5)

---

### PM6 - De Novo (Assumed)

**Original ACMG Summary:** Assumed de novo, but without confirmation of paternity and maternity.

**VCEP Specifications:** See PS2 above. Follow SVI guidance for de novo occurrences.

**Modification Type:** Clarification

---

### PP1 - Co-segregation

**Original ACMG Summary:** Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.

**Note:** May be used as stronger evidence with increasing segregation data.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong (PP1_Strong)** | Variant segregates with phenotype in **>=6 informative meioses** in >=1 family. Must include **>=2 affected relatives** (LDL-C >75th centile) with the variant. |
| **Moderate (PP1_Moderate)** | Variant segregates with phenotype in **4-5 informative meioses** in >=1 family. Must include **>=2 affected relatives** (LDL-C >75th centile) with the variant. |
| **Supporting (PP1)** | Variant segregates with phenotype in **2-3 informative meioses** in >=1 family. Must include **>=1 affected relative** (LDL-C >75th centile) with the variant. |

**Modification Type:** Disease-specific, Strength

#### Co-segregation Notes (from Supplementary Figure 2)

- Index cases should **not** be counted as positive cases for co-segregation results.
- Only consider relatives from the relevant side of the family (i.e., the side from which the variant was inherited).
- Informative meioses include affected relatives carrying the variant and unaffected relatives who do not carry the variant.
- Affected status is defined as LDL-C >75th centile.
- Unaffected status (for BS4) is defined as LDL-C <50th centile.

---

### PP2 - Missense in Constrained Gene

**Original ACMG Summary:** Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.

**VCEP Specifications:** **Not Applicable** - This criterion is not used for LDLR.

---

### PP3 - Computational Evidence

**Original ACMG Summary:** Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).

**Caveat:** As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.

**VCEP Specifications (Supporting):**

**For Missense Variants:**
- REVEL score **>=0.75** is supportive evidence of pathogenicity (PP3).

**For Splicing Predictions (using MaxEntScan):**
- **Do not apply** if PVS1 (or modified strength) is met.
- **Do not apply** if splicing functional data is available.
- If both missense and splicing prediction are applicable, only **1 prediction** of affecting function is necessary to apply PP3.

**Modification Type:** Disease-specific

#### MaxEntScan Splicing Thresholds

Apply A, B, or C based on variant location:

**(A) Variant at -20 to +3 (acceptor) or -3 to +6 (donor) relative to authentic splice site:**
- Authentic splice site strength variant/wild-type score **<0.8** → PP3
- Score **>=1.0** → BP4

**(B) Variant creates de novo splice site (acceptor >=50bp upstream of donor, or donor >=50bp downstream of acceptor):**
- De novo splice site strength variant/authentic wild-type score **>0.9** → PP3
- Score **<0.8** → BP4

**(C) Variant at -20 to +3 relative to intra-exonic AG (>=50bp upstream of donor) or -3 to +6 relative to intra-exonic GT (>=50bp downstream of acceptor):**
- Both variant cryptic/wild-type cryptic score **>1.1** AND cryptic acceptor/authentic acceptor (or cryptic donor/authentic donor) score **>0.9** → PP3

**Note:** BP4 is applicable to exonic variants outside of the 50 base limits detailed above, given the unlikelihood of such variants to impact splicing in LDLR.

---

### PP4 - Phenotype Specificity

**Original ACMG Summary:** Patient's phenotype or family history is highly specific for a disease with a single genetic etiology.

**VCEP Specifications (Supporting):** Any LDLR variant identified in an FH patient [diagnosis based on validated clinical criteria, e.g. Dutch Lipid Clinic Network (>=6), Simon Broome (possible/definite), MEDPED], after alternative causes of high cholesterol are excluded. **Caveat:** variant must also meet PM2.

**Modification Type:** Disease-specific

---

### PP5 - Reputable Source

**Original ACMG Summary:** Reputable source recently reports variant as pathogenic, but the evidence is not available to the laboratory to perform an independent evaluation.

**VCEP Specifications:** **Not Applicable** - This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PMID: 29543229).

---

## Benign Criteria

### BA1 - Allele Frequency >0.5%

**Original ACMG Summary:** Allele frequency is above 5% in population databases.

**VCEP Specification (Stand Alone):**
- Variant has a **PopMax FAF >=0.005 (0.5%)** in gnomAD.

**Modification Type:** Disease-specific

---

### BS1 - Frequency Greater Than Expected

**Original ACMG Summary:** Allele frequency is greater than expected for disorder.

**VCEP Specification (Strong):**
- Variant has a **PopMax FAF >=0.002 (0.2%)** and <0.005 (0.5%) in gnomAD.

**Modification Type:** Disease-specific

---

### BS2 - Observed in Healthy Adult

**Original ACMG Summary:** Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

**VCEP Specification (Strong):**
- Variant is identified in **>=3 heterozygous** or **>=1 homozygous** well-phenotyped, untreated, normolipidemic adults (unrelated).

**Modification Type:** Disease-specific

---

### BS3 - Functional Studies (No Effect)

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong (BS3 - Level 1)** | Study of the whole LDLR cycle (LDLR expression/biosynthesis, LDL binding, and LDL internalization) performed in heterologous cells (with no endogenous LDLR) transfected with mutant plasmid. Assay result of **>90% of wild-type activity** in expression/biosynthesis, binding **AND** internalization. **Note:** studies of only part of the LDLR cycle are not eligible for BS3 or BS3_Supporting. |
| **Supporting (BS3_Supporting - Level 3)** | See Level 3 benign criteria below. |

**Modification Type:** Disease-specific, Strength

#### Level 3 (BS3_Supporting) Detailed Criteria

1. Study of whole LDLR cycle in **true homozygous patient cells**, with assay result of **>90% of wild-type activity** in biosynthesis, binding AND internalization; **or** in **heterozygous patient cells** with assay result of **>95% of wild-type activity** in biosynthesis, binding AND internalization.
2. Luciferase studies with transcription levels of **>90%** when compared to wild-type (applicable to 5'UTR/promoter variants).
3. RNA studies, using RNA extracted from heterozygous or homozygous patient cells, with:
   - (a) Aberrant transcript quantification, where aberrant transcript is **<10% of total transcript**, OR
   - (b) Without transcript quantification where **no aberrant transcript** is confirmed by sequencing.
4. Minigene splicing assay where **only wild-type transcript** is present and confirmed by sequencing.
5. High-throughput assays as defined above; only applicable when assay can indicate the **whole LDLR cycle** (LDLR expression/biosynthesis, LDL binding AND internalization) is unaffected.

> **Note:** Functional assays performed in compound heterozygous patient cells are not considered applicable in PS3/BS3 criteria since it is difficult to delineate the individual effect of each variant.

---

### BS4 - Lack of Segregation

**Original ACMG Summary:** Lack of segregation in affected members of a family.

**VCEP Specification (Strong):**
- Lack of segregation in **>=2 index case families** (unrelated), when data is available for **>=2 informative meioses** in each family.
- **Caveat:** must be >=1 unaffected relative (LDL-C <50th centile) who is positive for the variant.

**Modification Type:** Disease-specific

---

### BP1-BP7 - Benign Supporting

| Criterion | Status | Specification |
|-----------|--------|---------------|
| **BP1** | **Not Applicable** | Missense variant in gene where only LoF causes disease. Not applicable to LDLR. |
| **BP2** | **Applicable (Supporting)** | If a FH patient with a heterozygous phenotype has a pathogenic or likely pathogenic variant in LDLR (in trans), APOB or PCSK9, BP2 is applicable to any additional LDLR variants. |
| **BP3** | **Not Applicable** | In-frame deletions/insertions in a repetitive region without a known function. Not applicable to LDLR. |
| **BP4** | **Applicable (Supporting)** | REVEL score <=0.5 (missense variants), or no predicted impact to splicing using MaxEntScan (see PP3 splicing thresholds). |
| **BP5** | **Not Applicable** | Variant found in a case with an alternate molecular basis for disease. Not applicable to LDLR. |
| **BP6** | **Not Applicable** | Not for use as recommended by the ClinGen SVI VCEP Review Committee (PMID: 29543229). |
| **BP7** | **Applicable (Supporting)** | Variant is synonymous. **Caveat:** variant must also meet BP4 (i.e. no predicted impact on splicing). |

---

## Rules for Combining Criteria

*Adapted from Richards et al., 2015; no changes to original scoring algorithm.*

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
| 1 Very Strong **AND** 1 Moderate |
| 1 Strong **AND** 1-2 Moderate |
| 1 Strong **AND** >=2 Supporting |
| >=3 Moderate |
| 2 Moderate **AND** >=2 Supporting |
| 1 Moderate **AND** >=4 Supporting |

### Benign Classification

| Criteria Combination |
|---------------------|
| 1 Stand Alone (BA1) |
| >=2 Strong |

### Likely Benign Classification

| Criteria Combination |
|---------------------|
| 1 Strong **AND** 1 Supporting |
| >=2 Supporting |

### Variant of Uncertain Significance (VUS)

Criteria shown above are not met **OR** the criteria for pathogenic and benign are contradictory.

---

## Appendices

### Appendix A: PVS1 Flowchart

The LDLR-specific PVS1 flowchart is an adaptation of Tayoun et al., 2018. It provides guidance for determining the appropriate strength level (Very Strong, Strong, Moderate, or Supporting) for null variants based on:

- **Variant type:** Nonsense, frameshift, canonical splice site (+/-1,2), initiation codon, single/multi-exon deletion
- **NMD prediction:** Whether the variant is predicted to undergo nonsense-mediated decay
- **Exon skipping impact:** Whether exon skipping results in an in-frame or out-of-frame transcript
- **Functional domain impact:** Whether the affected region is critical for LDLR function
- **Last exon considerations:** Variants in the last exon or near the 3' end of the gene

Refer to Figure 1 in the original specification document for the complete flowchart.

### Appendix B: LDLR Conserved Cysteine Residues (PM1)

60 highly conserved cysteine residues involved in disulfide bond formation. Missense changes at these residues qualify for PM1.

| Residue | Domain | Predicted Impact |
|---------|--------|------------------|
| p.Cys27 | LDL-receptor class A 1 | folding defect |
| p.Cys34 | LDL-receptor class A 1 | folding defect |
| p.Cys39 | LDL-receptor class A 1 | folding defect |
| p.Cys46 | LDL-receptor class A 1 | folding defect |
| p.Cys52 | LDL-receptor class A 1 | folding defect |
| p.Cys63 | LDL-receptor class A 1 | folding defect |
| p.Cys68 | LDL-receptor class A 2 | folding defect |
| p.Cys75 | LDL-receptor class A 2 | folding defect |
| p.Cys82 | LDL-receptor class A 2 | folding defect |
| p.Cys89 | LDL-receptor class A 2 | folding defect |
| p.Cys95 | LDL-receptor class A 2 | folding defect |
| p.Cys104 | LDL-receptor class A 2 | folding defect |
| p.Cys109 | LDL-receptor class A 3 | folding defect; LDL binding defect |
| p.Cys116 | LDL-receptor class A 3 | folding defect; LDL binding defect |
| p.Cys121 | LDL-receptor class A 3 | folding defect; LDL binding defect |
| p.Cys128 | LDL-receptor class A 3 | folding defect; LDL binding defect |
| p.Cys134 | LDL-receptor class A 3 | folding defect; LDL binding defect |
| p.Cys143 | LDL-receptor class A 3 | folding defect; LDL binding defect |
| p.Cys148 | LDL-receptor class A 4 | folding defect; receptor-recycling defect; LDL binding defect |
| p.Cys155 | LDL-receptor class A 4 | folding defect; LDL binding defect |
| p.Cys160 | LDL-receptor class A 4 | folding defect; receptor-recycling defect; LDL binding defect |
| p.Cys167 | LDL-receptor class A 4 | folding defect; LDL binding defect |
| p.Cys173 | LDL-receptor class A 4 | folding defect; receptor-recycling defect; LDL binding defect |
| p.Cys184 | LDL-receptor class A 4 | folding defect; LDL binding defect |
| p.Cys197 | LDL-receptor class A 5 | folding defect; LDL binding defect |
| p.Cys204 | LDL-receptor class A 5 | folding defect; LDL binding defect |
| p.Cys209 | LDL-receptor class A 5 | folding defect; LDL binding defect |
| p.Cys216 | LDL-receptor class A 5 | folding defect; LDL binding defect |
| p.Cys222 | LDL-receptor class A 5 | folding defect; receptor-recycling defect; LDL binding defect |
| p.Cys231 | LDL-receptor class A 5 | folding defect; LDL binding defect |
| p.Cys236 | LDL-receptor class A 6 | folding defect; LDL binding defect |
| p.Cys243 | LDL-receptor class A 6 | folding defect; LDL binding defect |
| p.Cys248 | LDL-receptor class A 6 | folding defect; LDL binding defect |
| p.Cys255 | LDL-receptor class A 6 | folding defect; LDL binding defect |
| p.Cys261 | LDL-receptor class A 6 | folding defect; LDL binding defect |
| p.Cys270 | LDL-receptor class A 6 | folding defect; LDL binding defect |
| p.Cys276 | LDL-receptor class A 7 | folding defect; LDL binding defect |
| p.Cys284 | LDL-receptor class A 7 | folding defect; LDL binding defect |
| p.Cys289 | LDL-receptor class A 7 | folding defect; LDL binding defect |
| p.Cys296 | LDL-receptor class A 7 | folding defect; LDL binding defect |
| p.Cys302 | LDL-receptor class A 7 | folding defect; LDL binding defect |
| p.Cys313 | LDL-receptor class A 7 | folding defect; LDL binding defect |
| p.Cys318 | EGF-like 1 | folding defect; LDL binding defect |
| p.Cys325 | EGF-like 1 | folding defect; LDL binding defect |
| p.Cys329 | EGF-like 1 | folding defect; LDL binding defect |
| p.Cys338 | EGF-like 1 | folding defect; LDL binding defect |
| p.Cys340 | EGF-like 1 | folding defect; LDL binding defect |
| p.Cys352 | EGF-like 1 | folding defect; LDL binding defect |
| p.Cys358 | EGF-like 2; calcium-binding | folding defect; receptor-recycling defect |
| p.Cys364 | EGF-like 2; calcium-binding | folding defect; receptor-recycling defect |
| p.Cys368 | EGF-like 2; calcium-binding | folding defect; receptor-recycling defect |
| p.Cys377 | EGF-like 2; calcium-binding | folding defect; receptor-recycling defect |
| p.Cys379 | EGF-like 2; calcium-binding | folding defect; receptor-recycling defect |
| p.Cys392 | EGF-like 2; calcium-binding | folding defect; receptor-recycling defect |
| p.Cys667 | EGF-like 3 | folding defect; receptor-recycling defect |
| p.Cys677 | EGF-like 3 | folding defect; receptor-recycling defect |
| p.Cys681 | EGF-like 3 | folding defect; receptor-recycling defect |
| p.Cys696 | EGF-like 3 | folding defect; receptor-recycling defect |
| p.Cys698 | EGF-like 3 | folding defect; receptor-recycling defect |
| p.Cys711 | EGF-like 3 | folding defect; receptor-recycling defect |

*Adapted from Guo et al., 2019. Residues correspond to LDLR transcript NM_000527.5.*

### Appendix C: LDLR Exon Information

| Exon | Start (g.) | Stop (g.) | Start (c.) | Stop (c.) | Length | Start Phase | End Phase |
|------|-----------|----------|-----------|----------|--------|-------------|-----------|
| 1 | 11089463 | 11089615 | -86 | 67 | 153 | - | 1 |
| 2 | 11100223 | 11100345 | 68 | 190 | 123 | 1 | 1 |
| 3 | 11102664 | 11102786 | 191 | 313 | 123 | 1 | 1 |
| 4 | 11105220 | 11105600 | 314 | 694 | 381 | 1 | 1 |
| 5 | 11106565 | 11106687 | 695 | 817 | 123 | 1 | 1 |
| 6 | 11107392 | 11107514 | 818 | 940 | 123 | 1 | 1 |
| 7 | 11110652 | 11110771 | 941 | 1060 | 120 | 1 | 1 |
| 8 | 11111514 | 11111639 | 1061 | 1186 | 126 | 1 | 1 |
| 9 | 11113278 | 11113449 | 1187 | 1358 | 172 | 1 | 2 |
| 10 | 11113535 | 11113762 | 1359 | 1586 | 228 | 2 | 2 |
| 11 | 11116094 | 11116212 | 1587 | 1705 | 119 | 2 | 1 |
| 12 | 11116859 | 11116998 | 1706 | 1845 | 140 | 1 | 0 |
| 13 | 11120092 | 11120233 | 1846 | 1987 | 142 | 0 | 1 |
| 14 | 11120370 | 11120522 | 1988 | 2140 | 153 | 1 | 1 |
| 15 | 11123174 | 11123344 | 2141 | 2311 | 171 | 1 | 1 |
| 16 | 11128008 | 11128085 | 2312 | 2389 | 78 | 1 | 1 |
| 17 | 11129513 | 11129670 | 2390 | 2547 | 158 | 1 | 0 |
| 18 | 11131281 | 11133820 | 2548 | 2583 | 35 | 0 | - |

*Phase: the position of an exon/intron boundary within a codon. A phase of zero means the boundary falls between codons, one means between the first and second base, and two means between the second and third base. Genomic (g.) coordinates correspond to reference sequence NC_000019.9, and coding (c.) coordinates correspond to LDLR transcript NM_000527.5.*

### Appendix D: Population Frequency Thresholds Summary

| Criterion | gnomAD Metric | Threshold | Strength |
|-----------|---------------|-----------|----------|
| BA1 | PopMax FAF | >=0.005 (0.5%) | Stand Alone |
| BS1 | PopMax FAF | >=0.002 (0.2%) and <0.005 (0.5%) | Strong |
| PM2 | PopMax MAF | <=0.0002 (0.02%) | Moderate |

**Frequency threshold derivation parameters:**

| Parameter | BA1 | BS1 | PM2 |
|-----------|-----|-----|-----|
| Prevalence | 1/250 | 1/250 | 1/250 |
| Penetrance | 50% | 95% | 95% |
| Allelic Heterogeneity | 1.0 | 1.0 | 0.1 |
| Genetic Heterogeneity | 1.0 | 0.9 | 0.9 |

*Note: BA1 metrics were equal to 0.4%; however, the BA1 threshold was conservatively increased to 0.5%.*

### Appendix E: PS3/BS3 Functional Study Summary Table

| Level | Pathogenic (PS3) | Benign (BS3) |
|-------|------------------|--------------|
| **Level 1 (Strong / Strong)** | Whole LDLR cycle in heterologous cells (no endogenous LDLR) with mutant plasmid; **<70%** WT activity in expression, binding OR internalization | Whole LDLR cycle in heterologous cells (no endogenous LDLR) with mutant plasmid; **>90%** WT activity in expression, binding AND internalization |
| **Level 2 (Moderate / N/A)** | (1) Part of LDLR cycle (Level 1 method) or whole/part in homozygous cells; <70% WT. (2) RNA with aberrant transcript >25% (het) or 50% (hom). (3) Two+ Level 3 studies or Level 3 #1-4 by 2+ labs | *Not applicable* |
| **Level 3 (Supporting / Supporting)** | (1) Whole/part LDLR cycle in het cells; <85% WT. (2) Luciferase <50% WT. (3) Minigene <10% WT transcript. (4) Validated high-throughput assays. (5) RNA with aberrant transcript, no quantification | (1) Whole cycle in hom cells >90% or het cells >95% WT. (2) Luciferase >90% WT. (3) RNA aberrant <10% or no aberrant transcript. (4) Minigene with only WT transcript. (5) High-throughput assays covering whole cycle |

### Appendix F: Reference PMIDs

- PMID: 29543229 - ClinGen SVI recommendations for PP5/BP6 (not for use)
- Richards et al., 2015 - ACMG/AMP Variant Classification Guidelines
- Tayoun et al., 2018 - PVS1 flowchart framework
- Guo et al., 2019 - LDLR cysteine residue analysis
- Thormaehlen et al., 2015 - Alternative microscopy assays
- Weile & Roth, 2018 - MAVE/deep mutational scanning framework

---

## Version History

| Version | Date | Notes |
|---------|------|-------|
| 1.2.0 | 11/9/2021 | Updated for clarification on PM3 and BP2, and typo correction |
| 1.1.0 | — | Prior version |
| 1.0.0 | 9/27/2020 | Initial approved specification |

---

*This document was compiled from ClinGen VCEP specifications and ClinGen SVI recommendations. For the most current version, please refer to the [ClinGen website](https://www.clinicalgenome.org/affiliation/50004/docs/assertion-criteria).*
