# ClinGen Hereditary Hemorrhagic Telangiectasia VCEP Variant Interpretation Guidelines for ACVRL1

**Version:** 1.1.0
**Released:** 3/20/2024
**Affiliation:** Hereditary Hemorrhagic Telangiectasia VCEP
**Based on:** Richards et al., 2015 ACMG/AMP Guidelines

---

## Gene Information

| Attribute | Value |
|-----------|-------|
| **Gene** | ACVRL1 (HGNC:175) |
| **HGNC Name** | activin A receptor like type 1 |
| **Transcript** | NM_000020.3 |
| **Disease** | Telangiectasia, hereditary hemorrhagic, type 2 (MONDO:0010880) |
| **Inheritance** | Autosomal dominant |

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
   - [BA1 - Allele Frequency Stand Alone](#ba1---allele-frequency-stand-alone)
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
- Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7)
- Use caution interpreting LOF variants at the extreme 3' end of a gene
- Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact
- Use caution in the presence of multiple transcripts

**VCEP Specifications:** Use ACVRL1 PVS1 Decision Tree (see Appendix A)

#### Strength Levels

| Strength | Criteria |
|----------|----------|
| **Very Strong** | Use ACVRL1 PVS1 Decision Tree |
| **Strong** | Use ACVRL1 PVS1 Decision Tree |
| **Moderate** | Use ACVRL1 PVS1 Decision Tree |

**Modification Type:** Gene-specific, Strength

---

### PS1 - Same Amino Acid Change

**Original ACMG Summary:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change. Example: Val->Leu caused by either G>C or G>T in the same codon.

**Caveat:** Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:** No modification. Use as applicable.

| Strength | Criteria |
|----------|----------|
| **Strong** | Same amino acid change as a previously established pathogenic variant regardless of nucleotide change |

**Modification Type:** No change

---

### PS2 - De Novo (Confirmed)

**Original ACMG Summary:** De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.

**Note:** Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.

**VCEP Specifications:**
- See additional information in HHT phenotype document attached
- **Note:** Low-level mosaicism has been observed in parents of individuals with HHT (PMID: 29736967, PMID: 21651515, PMID: 21378382, PMID: 21415079)

| Strength | Criteria |
|----------|----------|
| **Strong** | De novo (both maternity and paternity confirmed) in a patient with the disease and no family history |

**Modification Type:** Clarification, Disease-specific

---

### PS3 - Functional Studies

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.

**Note:** Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.

**VCEP Specifications:** HHT assays can be used as supporting evidence and bumped up to moderate/strong criteria if multiple different functional assays are concordant.

#### Strength Levels

| Strength | Criteria |
|----------|----------|
| **Strong** | mRNA splicing assays can be used as strong functional evidence. **Note:** level of evidence used may differ depending on whether the abnormal transcript is in-frame or out-of-frame, and whether there is complete or incomplete splicing impact. Do not use PS3 for splice variants that meet PVS1. |
| **Moderate** | See PS3_Supporting and Instructions below |
| **Supporting** | See approved assay types below |

#### Approved Assay Instances for PS3_Supporting

**Protein expression assays:**
- Metabolic label & IP
- WB & FACS HUVECs/BOECs
- FACS activated monocytes
- cDNA transfect, WB & ML HEK293T/COS/NIH3T3
- cDNA transfect & luciferase HepG2

**Note:** Decreased protein expression can be used as supporting pathogenic evidence if experiment was not done in a single assay, and the corresponding densitometry of western blot reflects the conclusion drawn.

**Intracellular signaling assays:**
- BRE/CAGA-luciferase
- Gal4 Smad1/Smad3 for TGF-beta/BMP9 signaling

**Binding assays:**
- BMP9 binding
- Transcription factor Sp1
- BMP9 protein-protein interaction (BLI)

**Other assays:**
- Subcellular protein localization
- Morphology: Morphology & actin cytoskeleton, tubulogenesis
- Somatic variant 2nd hit: In vivo evidence can be obtained as supporting functional evidence by identification of somatic variants in telangiectases biopsies using NGS, suggesting a second-hit mechanism leading to biallelic LOF (PMID: 31630786)

**Modification Type:** Disease-specific, Strength

---

### PS4 - Prevalence in Affected

**Original ACMG Summary:** The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.

**Note 1:** Relative risk (RR) or odds ratio (OR), as obtained from case-control studies, is >5.0 and the confidence interval around the estimate of RR or OR does not include 1.0.

**Note 2:** In instances of very rare variants where case-control studies may not reach statistical significance, the prior observation of the variant in multiple unrelated patients with the same phenotype, and its absence in controls, may be used as moderate level of evidence.

**VCEP Specifications:**
- Variant must also meet PM2_Supporting
- See HHT phenotype document in attachments for phenotype requirements

#### Strength Levels

| Strength | Criteria |
|----------|----------|
| **Strong** | 4+ probands with phenotype consistent with HHT |
| **Moderate** | 2-3 probands with phenotype consistent with HHT |
| **Supporting** | 1 proband with phenotype consistent with HHT |

**Modification Type:** Disease-specific

---

### PM1 - Mutational Hot Spot

**Original ACMG Summary:** Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.

**VCEP Specifications:**
- **Note:** If the variant falls within a PM1 region, do not use PM1 with PM5_Strong. PM1 can still be combined with PM5.

#### Strength Level

| Strength | Criteria |
|----------|----------|
| **Moderate** | Apply if variant is located in a critical residue (see list below) |

#### Critical Residues for ACVRL1

| Domain | Residues |
|--------|----------|
| Glycine-rich loop | G209-V216 |
| Phosphate anchor | K229 |
| C-helix E pairing the phosphate anchor | E242 |
| Catalytic loop | R329-N335 |
| Metal-binding loop | D348-L351 |
| BMP10 interaction cluster | His40, Val54, Val56, Arg57, Glu58, Glu59, His66, Asn71, Leu72, His73, Glu75, Leu76, Arg78, Gly79, Arg80, Thr82, Glu83, Phe84, Val85, His87 |

**Modification Type:** Gene-specific

---

### PM2 - Absent from Controls

**Original ACMG Summary:** Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

**Caveat:** Population data for indels may be poorly called by next generation sequencing.

**VCEP Specification (Supporting only):**

| Strength | Criteria |
|----------|----------|
| **Supporting** | <6 total alleles in gnomAD **OR** <0.00004 (0.004%) in gnomAD subpopulations |

**Modification Type:** Disease-specific, Strength

---

### PM3 - In Trans with Pathogenic

**Original ACMG Summary:** For recessive disorders, detected in trans with a pathogenic variant. Note: This requires testing of parents (or offspring) to determine phase.

**VCEP Specifications:** **Not Applicable**

**Comments:** HHT is an autosomal dominant disorder.

---

### PM4 - Protein Length Changes

**Original ACMG Summary:** Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

**VCEP Specifications:** No modification. Use as applicable.

| Strength | Criteria |
|----------|----------|
| **Moderate** | Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants |

**Modification Type:** None

---

### PM5 - Novel Missense at Same Residue

**Original ACMG Summary:** Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before. Example: Arg156His is pathogenic; now you observe Arg156Cys.

**Caveat:** Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | ≥2 different missense changes at same codon have been determined to be likely pathogenic or pathogenic based on HHT VCEP rules |
| **Moderate** | A different missense change at same codon has been determined to be likely pathogenic or pathogenic based on HHT VCEP rules |

**Modification Type:** Disease-specific, Strength

---

### PM6 - De Novo (Assumed)

**Original ACMG Summary:** Assumed de novo, but without confirmation of paternity and maternity.

**VCEP Specifications:** **Not Applicable**

**Comments:** De novo variants are rare in HHT. De novo variants should be confirmed not presumed for HHT.

---

### PP1 - Co-segregation

**Original ACMG Summary:** Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.

**Note:** May be used as stronger evidence with increasing segregation data.

**VCEP Specifications:** See HHT phenotype document in attachments for assignment of affected/unaffected status for purpose of inclusion in cosegregation study.

#### Strength Levels

| Strength | Meioses | Likelihood |
|----------|---------|------------|
| **Strong** | 5+ meioses | 1/32 likelihood |
| **Moderate** | 4 meioses | 1/16 likelihood |
| **Supporting** | 3 meioses | 1/8 likelihood |

**Modification Type:** Disease-specific, Strength

---

### PP2 - Missense in Constrained Gene

**Original ACMG Summary:** Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.

**VCEP Specifications:** **Not Applicable**

**Comments:** Does not apply to ACVRL1 (Z-score 2.45).

---

### PP3 - Computational Evidence

**Original ACMG Summary:** Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).

**Caveat:** As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.

**VCEP Specifications:**
- SpliceAI (PMID: 30661751): https://spliceailookup.broadinstitute.org/
- REVEL (PMID: 27666373)

| Strength | Criteria |
|----------|----------|
| **Supporting** | For missense variants: REVEL score ≥0.644 **OR** SpliceAI score ≥0.2 |
| **Supporting** | For synonymous and intronic variants: SpliceAI score ≥0.2 |

**Modification Type:** Disease-specific

---

### PP4 - Phenotype Specificity

**Original ACMG Summary:** Patient's phenotype or family history is highly specific for a disease with a single genetic etiology.

**VCEP Specifications:**
- PP4_Moderate cannot be applied to variants that meet BS1_Supporting/BS1/BA1 criteria
- If PP4_Moderate can be applied to a patient, they cannot be included in proband counting (PS4)
- See HHT phenotype document in attachments for information regarding Curaçao phenotype requirements

| Strength | Criteria |
|----------|----------|
| **Moderate** | Patient's phenotype meets consensus clinical diagnostic (Curaçao) criteria for HHT, and sequencing and large deletion/duplication analysis was performed for both ENG and ACVRL1 with any other identified variants ruled out |

**Modification Type:** Disease-specific, Strength

---

### PP5 - Reputable Source

**Original ACMG Summary:** Reputable source recently reports variant as pathogenic, but the evidence is not available to the laboratory to perform an independent evaluation.

**VCEP Specifications:** **Not Applicable**

This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee. (PMID: 29543229)

---

## Benign Criteria

### BA1 - Allele Frequency Stand Alone

**Original ACMG Summary:** Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

**VCEP Specification (Stand Alone):**

| Strength | Criteria |
|----------|----------|
| **Stand Alone** | Allele frequency is ≥1% in general population databases (e.g. gnomAD) based on Popmax FAF |

**Modification Type:** Disease-specific

---

### BS1 - Frequency Greater Than Expected

**Original ACMG Summary:** Allele frequency is greater than expected for disorder.

**VCEP Specifications:** HHT is not known to be enriched in bottlenecked populations (e.g. Ashkenazi Jewish); therefore, Popmax FAF can be calculated and applied for bottlenecked populations for BS1 and BS1_Supporting criteria.

| Strength | Criteria |
|----------|----------|
| **Strong** | >0.2% to <1% in general population databases (e.g. gnomAD) based on Popmax FAF, **OR** if variant meets BS1_Supporting and has ≥2 homozygotes |
| **Supporting** | >0.08% to 0.2% (based on gnomAD Popmax FAF) |

**Modification Type:** Disease-specific, Strength

---

### BS2 - Observed in Healthy Adult

**Original ACMG Summary:** Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

**VCEP Specifications:** **Not Applicable**

**Comments:** Full penetrance at an early age is not observed in HHT.

---

### BS3 - Functional Studies (No Effect)

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

**VCEP Specifications:**
- Normal protein expression cannot be used as benign evidence because protein function can still be altered (e.g. pathogenic dominant negative variants)

| Strength | Criteria |
|----------|----------|
| **Supporting** | See approved assay types below |

#### Approved Assay Types for BS3_Supporting

- mRNA splicing assays
- Intracellular signaling assays: BRE/CAGA-luciferase, Gal4 Smad1/Smad3 for TGF-beta/BMP9 signaling
- Binding assays: BMP9 binding, transcription factor Sp1, BMP9 protein-protein interaction (BLI)
- Subcellular protein localization
- Morphology: Morphology & actin cytoskeleton, tubulogenesis

**Modification Type:** Disease-specific, Strength

---

### BS4 - Lack of Segregation

**Original ACMG Summary:** Lack of segregation in affected members of a family.

**Caveat:** The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.

**VCEP Specifications:** See HHT phenotype document in attachments for assignment of affected/unaffected status for purpose of inclusion in cosegregation study.

| Strength | Criteria |
|----------|----------|
| **Strong** | Lack of segregation in affected members of a family |

**Modification Type:** Clarification, Disease-specific

---

### BP1-BP7 - Benign Supporting

| Criterion | Status | Comment |
|-----------|--------|---------|
| **BP1** | Not Applicable | Missense variants commonly seen in HHT genes |
| **BP2** | Applicable (Supporting) | Observed in trans with a pathogenic or likely pathogenic variant based on HHT VCEP rules. Variants must be confirmed in trans. |
| **BP3** | Not Applicable | - |
| **BP4** | Applicable (Supporting) | For missense variants: REVEL score ≤0.15 **AND** SpliceAI score ≤0.1. For synonymous and intronic variants: SpliceAI score ≤0.1. |
| **BP5** | Applicable (Supporting) | Apply if a likely pathogenic or pathogenic variant (based on HHT VCEP rules) is found in ENG |
| **BP6** | Not Applicable | Not for use as recommended by ClinGen SVI VCEP Review Committee (PMID: 29543229) |
| **BP7** | Applicable (Supporting) | For synonymous and intronic variants: SpliceAI score ≤0.1. Can be used together with BP4 evidence. |

#### BP7 Special Note

If no causative variant is found in ENG or ACVRL1, and the patient's clinical presentation and/or family history is highly suspicious for HHT, be careful to not dismiss intronic variants or synonymous variants in the last nucleotide of the exon based on computational predictions.

**Examples:**
1. ENG c.219G>A; p.Thr73= is not predicted to significantly alter splicing (SpliceAI: 0.02) and the nucleotide is weakly conserved. However, this variant was later shown to cause exon skipping (PMID: 17384219, ARUP Laboratories).
2. SpliceAI does not predict splicing effects for some deep intronic ACVRL1 intron 9 CT rich hotspot variants (PMID: 30244195). Therefore, variants that create a new 'AG' cryptic splice site in this region should not be ruled out based on SpliceAI prediction alone.

---

## Rules for Combining Criteria

### Pathogenic Classification

| Criteria Combination |
|---------------------|
| 1 Very Strong (PVS1) **AND** ≥1 Strong (PVS1_Strong, PS1, PS2, PS3, PS4, PM5_Strong, PP1_Strong) |
| 1 Very Strong (PVS1) **AND** ≥2 Moderate (PVS1_Moderate, PS3_Moderate, PS4_Moderate, PM1, PM4, PM5, PP1_Moderate, PP4_Moderate) |
| 1 Very Strong (PVS1) **AND** 1 Moderate (PVS1_Moderate, PS3_Moderate, PS4_Moderate, PM1, PM4, PM5, PP1_Moderate, PP4_Moderate) **AND** 1 Supporting (PS3_Supporting, PS4_Supporting, PM2_Supporting, PP1, PP3) |
| 1 Very Strong (PVS1) **AND** ≥2 Supporting (PS3_Supporting, PS4_Supporting, PM2_Supporting, PP1, PP3) |
| ≥2 Strong (PVS1_Strong, PS1, PS2, PS3, PS4, PM5_Strong, PP1_Strong) |
| 1 Strong (PVS1_Strong, PS1, PS2, PS3, PS4, PM5_Strong, PP1_Strong) **AND** ≥3 Moderate (PVS1_Moderate, PS3_Moderate, PS4_Moderate, PM1, PM4, PM5, PP1_Moderate, PP4_Moderate) |
| 1 Strong (PVS1_Strong, PS1, PS2, PS3, PS4, PM5_Strong, PP1_Strong) **AND** 2 Moderate (PVS1_Moderate, PS3_Moderate, PS4_Moderate, PM1, PM4, PM5, PP1_Moderate, PP4_Moderate) **AND** ≥2 Supporting (PS3_Supporting, PS4_Supporting, PM2_Supporting, PP1, PP3) |
| 1 Strong (PVS1_Strong, PS1, PS2, PS3, PS4, PM5_Strong, PP1_Strong) **AND** 1 Moderate (PVS1_Moderate, PS3_Moderate, PS4_Moderate, PM1, PM4, PM5, PP1_Moderate, PP4_Moderate) **AND** ≥4 Supporting (PS3_Supporting, PS4_Supporting, PM2_Supporting, PP1, PP3) |

### Likely Pathogenic Classification

| Criteria Combination |
|---------------------|
| 1 Very Strong (PVS1) **AND** 1 Moderate (PVS1_Moderate, PS3_Moderate, PS4_Moderate, PM1, PM4, PM5, PP1_Moderate, PP4_Moderate) |
| 1 Strong (PVS1_Strong, PS1, PS2, PS3, PS4, PM5_Strong, PP1_Strong) **AND** 1 Moderate (PVS1_Moderate, PS3_Moderate, PS4_Moderate, PM1, PM4, PM5, PP1_Moderate, PP4_Moderate) |
| 1 Strong (PVS1_Strong, PS1, PS2, PS3, PS4, PM5_Strong, PP1_Strong) **AND** ≥2 Supporting (PS3_Supporting, PS4_Supporting, PM2_Supporting, PP1, PP3) |
| ≥3 Moderate (PVS1_Moderate, PS3_Moderate, PS4_Moderate, PM1, PM4, PM5, PP1_Moderate, PP4_Moderate) |
| 2 Moderate (PVS1_Moderate, PS3_Moderate, PS4_Moderate, PM1, PM4, PM5, PP1_Moderate, PP4_Moderate) **AND** ≥2 Supporting (PS3_Supporting, PS4_Supporting, PM2_Supporting, PP1, PP3) |
| 1 Moderate (PVS1_Moderate, PS3_Moderate, PS4_Moderate, PM1, PM4, PM5, PP1_Moderate, PP4_Moderate) **AND** ≥4 Supporting (PS3_Supporting, PS4_Supporting, PM2_Supporting, PP1, PP3) |
| 1 Strong (PVS1_Strong, PS1, PS2, PS3, PS4, PM5_Strong, PP1_Strong) **AND** 2 Moderate (PVS1_Moderate, PS3_Moderate, PS4_Moderate, PM1, PM4, PM5, PP1_Moderate, PP4_Moderate) |
| 1 Very Strong (PVS1) **AND** 1 Supporting (PM2_Supporting) |

### Benign Classification

| Criteria Combination |
|---------------------|
| ≥2 Strong (BS1, BS4) |
| 1 Stand Alone (BA1) |

### Likely Benign Classification

| Criteria Combination |
|---------------------|
| ≥2 Supporting (BS1_Supporting, BS3_Supporting, BP2, BP4, BP5, BP7) |
| 1 Strong (BS1) |
| 1 Strong (BS1, BS4) **AND** 1 Supporting (BS1_Supporting, BS3_Supporting, BP2, BP4, BP5, BP7) |

---

## Appendices

### Appendix A: PVS1 Decision Tree

The ACVRL1 PVS1 Decision Tree should be used to determine the appropriate strength level for null variants. The decision tree considers:

1. **Variant type** (nonsense, frameshift, canonical splice, initiation codon, deletion)
2. **Location within the gene** (consideration of last exon, last 50bp of penultimate exon)
3. **Predicted impact on protein** (NMD vs. truncated protein)
4. **Splice site variants** - predicted impact on splicing and reading frame

Refer to the attached "ACVRL1 PVS1 Decision Tree.pptx" for the complete flowchart.

---

### Appendix B: Population Frequency Thresholds Summary

| Criterion | Threshold | Strength | Population Database |
|-----------|-----------|----------|---------------------|
| BA1 | ≥1% | Stand Alone | gnomAD Popmax FAF |
| BS1 | >0.2% to <1% | Strong | gnomAD Popmax FAF |
| BS1_Supporting | >0.08% to 0.2% | Supporting | gnomAD Popmax FAF |
| PM2_Supporting | <6 alleles OR <0.004% | Supporting | gnomAD |

---

### Appendix C: Computational Prediction Thresholds

| Tool | Pathogenic Threshold | Benign Threshold | Variant Type |
|------|---------------------|------------------|--------------|
| REVEL | ≥0.644 (PP3) | ≤0.15 (BP4) | Missense |
| SpliceAI | ≥0.2 (PP3) | ≤0.1 (BP4/BP7) | All |

---

### Appendix D: HHT Phenotype Requirements

See the attached "HHT Phenotype: Requirements for applying evidence codes" document for:
- Curaçao diagnostic criteria for HHT
- Requirements for assigning affected/unaffected status for cosegregation studies
- Phenotype requirements for PS4 proband counting

---

### Appendix E: Functional Assays

See the attached "HHT Functional Assays.xlsx" for:
- Complete list of approved functional assays
- Evidence strength assignments for each assay
- References for assay validation

---

### Appendix F: Criteria Not Applicable for ACVRL1

| Criterion | Reason |
|-----------|--------|
| PM3 | HHT is autosomal dominant disorder |
| PM6 | De novo variants are rare in HHT; should be confirmed not presumed |
| PP2 | Does not apply to ACVRL1 (Z-score 2.45) |
| PP5 | Not for use per ClinGen SVI recommendation (PMID: 29543229) |
| BS2 | Full penetrance at an early age is not observed in HHT |
| BP1 | Missense variants commonly seen in HHT genes |
| BP3 | Not applicable |
| BP6 | Not for use per ClinGen SVI recommendation (PMID: 29543229) |

---

### Appendix G: Important Notes for Evidence Code Application

1. **PS3 and PVS1:** Do not use PS3 for splice variants that meet PVS1.

2. **PM1 and PM5_Strong:** If the variant falls within a PM1 region, do not use PM1 with PM5_Strong. PM1 can still be combined with PM5.

3. **PP4 and PS4:** If PP4_Moderate can be applied to a patient, they cannot be included in proband counting (PS4).

4. **PP4 and Population Frequency:** PP4_Moderate cannot be applied to variants that meet BS1_Supporting/BS1/BA1 criteria.

5. **PS4 and PM2:** Variant must meet PM2_Supporting to apply PS4.

---

## References

1. McDonald J, Wooderchak-Donahue WL, et al. *Tissue-specific mosaicism in hereditary hemorrhagic telangiectasia: Implications for genetic testing in families.* **Am J Med Genet A** (2018) 176(7):1618-1621. PMID: 29736967

2. Eyries M, Coulet F, et al. *ACVRL1 germinal mosaic with two mutant alleles in hereditary hemorrhagic telangiectasia associated with pulmonary arterial hypertension.* **Clin Genet** (2012) 82(2):173-9. PMID: 21651515

3. Best DH, Vaughn C, et al. *Mosaic ACVRL1 and ENG mutations in hereditary haemorrhagic telangiectasia patients.* **J Med Genet** (2011) 48(5):358-60. PMID: 21378382

4. Lee NP, Matevski D, et al. *Identification of clinically relevant mosaicism in type I hereditary haemorrhagic telangiectasia.* **J Med Genet** (2011) 48(5):353-7. PMID: 21415079

5. Jaganathan K, Kyriazopoulou Panagiotopoulou S, et al. *Predicting Splicing from Primary Sequence with Deep Learning.* **Cell** (2019) 176(3):535-548.e24. PMID: 30661751

6. Ioannidis NM, Rothstein JH, et al. *REVEL: An Ensemble Method for Predicting the Pathogenicity of Rare Missense Variants.* **Am J Hum Genet** (2016) 99(4):877-885. PMID: 27666373

7. Plumitallo S, Ruiz-Llorente L, et al. *Functional analysis of a novel ENG variant in a patient with hereditary hemorrhagic telangiectasia (HHT) identifies a new Sp1 binding-site.* **Gene** (2018) 647:85-92. PMID: 29305977

8. Gedge F, McDonald J, et al. *Clinical and analytical sensitivities in hereditary hemorrhagic telangiectasia testing and a report of de novo mutations.* **J Mol Diagn** (2007) 9(2):258-65. PMID: 17384219

9. Wooderchak-Donahue WL, McDonald J, et al. *Genome sequencing reveals a deep intronic splicing ACVRL1 mutation hotspot in Hereditary Haemorrhagic Telangiectasia.* **J Med Genet** (2018) 55(12):824-830. PMID: 30244195

10. Snellings DA, Gallione CJ, et al. *Somatic Mutations in Vascular Malformations of Hereditary Hemorrhagic Telangiectasia Result in Bi-allelic Loss of ENG or ACVRL1.* **Am J Hum Genet** (2019) 105(5):894-906. PMID: 31630786

11. Faughnan ME, Mager JJ, et al. *Second International Guidelines for the Diagnosis and Management of Hereditary Hemorrhagic Telangiectasia.* **Ann Intern Med** (2020) 173(12):989-1001. PMID: 32894695

12. Porteous ME, Burn J, et al. *Hereditary haemorrhagic telangiectasia: a clinical analysis.* **J Med Genet** (1992) 29(8):527-30. PMID: 1518020

13. Berg J, Porteous M, et al. *Hereditary haemorrhagic telangiectasia: a questionnaire based study to delineate the different phenotypes caused by endoglin and ALK1 mutations.* **J Med Genet** (2003) 40(8):585-90. PMID: 12920067

14. Arthur H, Geisthoff U, et al. *Executive summary of the 11th HHT international scientific conference.* **Angiogenesis** (2015) 18(4):511-24. PMID: 26391603

15. Anderson E, Sharma L, et al. *Pulmonary arteriovenous malformations may be the only clinical criterion present in genetically confirmed hereditary haemorrhagic telangiectasia.* **Thorax** (2022) 77(6):628-630. PMID: 35165143

16. Revuz S, Decullier E, et al. *Pulmonary hypertension subtypes associated with hereditary haemorrhagic telangiectasia: Haemodynamic profiles and survival probability.* **PLoS One** (2017) 12(10):e0184227. PMID: 28981519

17. Shovlin CL, Guttmacher AE, et al. *Diagnostic criteria for hereditary hemorrhagic telangiectasia (Rendu-Osler-Weber syndrome).* **Am J Med Genet** (2000) 91(1):66-7. PMID: 10751092

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.1.0 | 3/20/2024 | Updated BMP10 interaction cluster residues (PM1); additional clarifying notes for not applying certain evidence codes together; updated HHT Phenotype attached document |
| 1.0.0 | Initial | Initial release |

---

*This document was compiled from ClinGen VCEP specifications for ACVRL1. For the most current version, please refer to the ClinGen website.*

*Generated based on ClinGen Hereditary Hemorrhagic Telangiectasia Expert Panel Specifications to the ACMG/AMP Variant Interpretation Guidelines for ACVRL1 Version 1.1.0*
