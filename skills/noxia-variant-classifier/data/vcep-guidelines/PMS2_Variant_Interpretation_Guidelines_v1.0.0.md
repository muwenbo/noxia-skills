# ClinGen InSiGHT Hereditary Colorectal Cancer/Polyposis VCEP Variant Interpretation Guidelines for PMS2

**Version:** 1.0.0
**Released:** 8/9/2024
**Affiliation:** InSiGHT Hereditary Colorectal Cancer/Polyposis VCEP
**Based on:** Richards et al., 2015 ACMG/AMP Guidelines

---

## Gene Information

| Attribute | Value |
|-----------|-------|
| **Gene** | PMS2 (HGNC:9122) |
| **HGNC Name** | PMS1 homolog 2, mismatch repair system component |
| **Transcript** | NM_000535.7 |
| **Disease** | Lynch syndrome 4 (MONDO:0013699) — Autosomal dominant inheritance; Mismatch repair cancer syndrome 1 (MONDO:0010159) — Autosomal recessive inheritance |
| **Inheritance** | Autosomal dominant (Lynch syndrome 4); Autosomal recessive (CMMRD) |

> **Important Note:** *PMS2* NGS results need confirmation by other orthogonal assays as well as functional assessment (e.g. Long-Range or cDNA), if variants are located in the *PMS2CL* pseudogene homologous regions (exons 11-15). Gene-specific penetrance estimates are available at http://lscarisk.org/

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
- Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7).
- Use caution interpreting LOF variants at the extreme 3' end of a gene.
- Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact.
- Use caution in the presence of multiple transcripts.

**VCEP Specifications:** PVS1 criteria is adapted from Tayoun et al. 2018. Refer to the PVS1 Decision Tree (Appendix A) for full details.

#### Strength Levels

| Strength | Criteria |
|----------|----------|
| **Very Strong** | Nonsense/frameshift variant introducing Premature Termination Codon (PTC) at or before codon 798 in *PMS2*. **OR** Large genomic alterations of single or multi-exon size (deletions). **OR** Variants at IVS+/-1 or IVS+/-2 where exon skipping or use of a cryptic splice site disrupts reading frame and is predicted to undergo NMD. Not to be combined with PP3 and not to be used for a confirmed splice defect (see PVS1 for variants where patient mRNA assays indicate splicing aberration). If exon skipping or use of a cryptic splice site preserves reading frame and the altered region is critical to protein function then use PVS1_Strong. If exon skipping or use of a cryptic splice site disrupts reading frame and is NOT predicted to undergo NMD then use PVS1_Moderate. **OR** Variants where mRNA assays using RNA derived from patient constitutional biological samples indicate that the variant allele results in a splicing aberration (with evidence that the variant allele produces no full-length/reference transcript) leading to premature stop codon or in-frame deletion disrupting a functional domain or protein conformation. Splicing aberration must be confirmed in a minigene assay or an additional RNA assay from an independent laboratory if it is a non-canonical splice site variant. |
| **Strong** | Variants in the initiation codon of *PMS2*. **OR** Presumed by default in tandem duplication of >=1 exon resulting in a frameshift before the last splice junction. This rule does not apply for variants that involve the UTR (i.e. exon 1 or last exon) and whole gene duplications. **OR** G>non-G at last base of exon if first 6 bases of the intron are not GTRRGT. If confirmed to cause a splice defect, then PVS1 should be used instead. **OR** Variants at IVS+/-1 or IVS+/-2 where exon skipping or use of a cryptic splice site preserves reading frame and the altered region is critical to protein function. Not to be combined with PP3 and not to be used for a confirmed splice defect. |
| **Moderate** | Nonsense/frameshift variant introducing premature termination codon between codons 799 & 862 in *PMS2*. |
| **Supporting** | — (not specified) |

**Notes:**
- NMD boundary for PMS2: codon 798 (using >=50 nucleotide NMD-rule)
- Last exon PTC boundary for PMS2: codon 798
- Region of unknown function for PMS2: codons 799-862
- IVS+/-1 and IVS+/-2 are the least invariant nucleotides in a splice site
- A known functional protein domain is reported to harbor sequence variants that introduce deleterious changes to protein function (via missense alteration, protein sequence deletion, or protein truncation in the last exon) AND are associated with high risk of cancer. Physical boundaries for functional domains are shown in the MMR functional domains file.

---

### PS1 - Same Amino Acid Change

**Original ACMG Summary:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change. Example: Val->Leu caused by either G>C or G>T in the same codon. Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:** SpliceAI masked score option should be checked on.

| Strength | Criteria |
|----------|----------|
| **Strong** | A predicted missense substitution that encodes the same amino acid change with a different underlying nucleotide change previously established by this VCEP as Pathogenic (not a predicted or confirmed splice defect). **OR** Variants affecting the same non-canonical splice nucleotide as a confirmed pathogenic splice variant with similar or worse splicing in silico prediction using SpliceAI. |
| **Moderate** | A predicted missense substitution that encodes the same amino acid change with a different underlying nucleotide change as a previously established Likely Pathogenic missense variant with normal RNA result*, and PM2_supporting is met. *Otherwise, if the previously established Likely Pathogenic missense variant truly is a splice defect, the new missense variant also has to be investigated on a functional level for RNA splicing. |

---

### PS2 - De Novo (Confirmed)

**Original ACMG Summary:** De novo (both maternity and paternity confirmed) in a patient with the disease and no family history. Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.

**VCEP Specifications:**

Proband with a *de novo* variant with both maternity and paternity confirmed in a case with MMR deficient LS spectrum tumor (i.e. MSI/IHC consistent with affected gene, with no MLH1 methylation in tumor tissue, with the exception of MLH1 constitutional promoter methylation. If there is no tumor data, see PS2_Moderate). Refer to Appendix for protein expression consistent with variant location. **2 points per proband**

OR

Proband with a *de novo* variant with both maternity and paternity confirmed in a case with LS spectrum tumor (with no tumor data for MSI/IHC/methylation, otherwise see PS2). **1 point per proband**

OR

Proband with assumed *de novo* variant and maternity and/or paternity unconfirmed with LS spectrum tumor (No tumor data for MSI/IHC/methylation). **0.5 points per proband**

*Lynch Syndrome (LS) tumors include: colorectal/colon/rectal, endometrial, ovarian, small bowel/small intestine, renal pelvis, ureter, and stomach/gastric carcinomas, sebaceous skin tumors (adenomas and carcinomas), gliomas.*

#### PS2/PM6 Point System

| Phenotypic Scenario | Points per Proband |
|---------------------|-------------------|
| De novo confirmed + MMR deficient LS spectrum tumor (MSI/IHC consistent, no MLH1 methylation) | 2.0 |
| De novo confirmed + LS spectrum tumor (no tumor data) | 1.0 |
| Assumed de novo (maternity/paternity unconfirmed) + LS spectrum tumor (no tumor data) | 0.5 |

#### Evidence Strength Thresholds

| Points | Strength Level |
|--------|----------------|
| >= 4 | Very Strong (PS2) |
| 2-3 | Strong (PS2) |
| 1 | Moderate (PS2_Moderate) |
| 0.5 | Supporting (PS2_Supporting) |

---

### PS3 - Functional Studies

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product. Note: Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.

**VCEP Specifications:** Refer to file 'Functional assay SVI documentation (MMR genes)' for calibrated functional assays.

> *The functional assay flowchart is a general framework for evaluating functional assays that were already performed, or from historic publications, not for prospective studies on variants. The information describing these assays are generic. The VCEP recommends use of the calibrated assays for prospective testing.*

| Strength | Criteria |
|----------|----------|
| **Strong** | Calibrated functional assays with functional odds for Pathogenicity > 18.7 |
| **Moderate** | Calibrated functional assays with functional odds for pathogenicity >4.3 and <= 18.7 **OR** MMR function defect following functional assay flowchart* **OR** Variants with monoallelic expression: complete loss of expression (<10% of wild-type in cDNA without puromycin) of the variant allele. Full-length transcript should be analysed with and without NMD block. |
| **Supporting** | Calibrated functional odds for Pathogenicity >2.08 and <= 4.3 |

#### Approved Assay Instances

| Assay | Author(s) | PMID | Gene(s) | Type | Proposed Strength | Normal Threshold | Abnormal Threshold |
|-------|-----------|------|---------|------|-------------------|------------------|--------------------|
| CIMRA (Cell-free MMR Activity) | Drost et al. | 30504929; 31965077 | MLH1, MSH2, MSH6, PMS2 | Calibrated | PS3, PS3_Moderate, PS3_Supporting, BS3, BS3_Supporting | >=100% for PMS2 | <18% for PMS2 |
| Chemical Selection Deep Sequencing | Jia; Scott et al. | 33357406; 36550560 | MSH2 | Calibrated | PS3, BS3 | LOF score <= 0 | LOF score > 0.4 |
| hESC CRISPR-based MMR Assay | Rath et al. | 36054288 | MLH1 | Calibrated | PS3, PS3_Moderate, PS3_Supporting, BS3, BS3_Supporting | OddsPath < 0.48 | OddsPath > 2.08 |
| Cell-free MMR Repair Assay | Thompson et al. | 24362816 | MMR genes | Non-calibrated | PS3_Moderate, BS3_Supporting | >75% in two independent assays | <25% in two independent assays |
| Mammalian MMR Complementation | Thompson et al. | 24362816 | MMR genes | Non-calibrated | PS3_Moderate, BS3_Supporting | >75% in two independent assays | <25% in two independent assays |
| Cellular-based MMR Expression | Thompson et al. | 24362816 | MMR genes | Non-calibrated | PS3_Moderate, BS3_Supporting | >75% in two independent assays | <25% in two independent assays |
| MMR Protein Subcellular Localization | Thompson et al. | 24362816 | MMR genes | Non-calibrated | PS3_Moderate, BS3_Supporting | Nuclear localization | Cytoplasmic localization |
| cDNA Analysis of Full-Length Transcripts | Morak et al. | 31332305 | MMR genes | Non-calibrated | PS3_Moderate, BS3_Supporting | Biallelic (50 +/- 10%) | Allelic loss (<=10%) |
| Methylation Agent Cell Survival | Bouvet et al. | 30998989 | MLH1, MSH2 | Non-calibrated | PS3_Moderate, BS3_Supporting | Mean survival < 68.7% (MLH1); < 45.54% (MSH2) | Mean survival > 68.7% (MLH1); > 45.54% (MSH2) |

---

### PS4 - Prevalence in Affected

**Original ACMG Summary:** The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.

***Not Applicable***

**Comments:** Due to the availability of tumor IHC data for variant classification (see PP4), PS4 has not been utilized for MMR variant classification using proband counting.

---

### PM1 - Mutational Hot Spot

**Original ACMG Summary:** Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.

***Not Applicable***

**Comments:** There are no recognized mutational hot spots that could be used for classification purposes. While there are functional domains in the MMR genes, the distribution of pathogenic variants is generalized over all the domains (unpublished data).

---

### PM2 - Absent from Controls

**Original ACMG Summary:** Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium. Caveat: Population data for indels may be poorly called by next generation sequencing.

**VCEP Specification (Supporting only):**
- Absent/extremely rare (<1 in 50,000 alleles) in gnomAD v4 dataset
- Outbred control reference groups currently used: Genome Aggregation Database non-cancer dataset (gnomad.broadinstitute.org)

---

### PM3 - In Trans with Pathogenic

**Original ACMG Summary:** For recessive disorders, detected in trans with a pathogenic variant. Note: This requires testing of parents (or offspring) to determine phase.

**VCEP Specifications:** Co-occurrence with a known pathogenic/likely pathogenic sequence variant in the same gene in a patient with clinical features consistent with CMMRD as per Aronson et al 2022 — Refer to "Table for CMMRD diagnosis" (Appendix D). For MLH1 variants — the variant has to meet PM2_Supporting criteria.

#### PM3 Point System (Per Proband)

| Classification/Zygosity of Other Variant | Points |
|------------------------------------------|--------|
| Pathogenic/Likely Pathogenic *in trans* | 1.0 |
| Pathogenic/Likely Pathogenic — phase unknown | 0.5 |

Sum all cases with the above evidence to determine the PM3 strength.

#### PM3 Evidence Strength Thresholds

| Total Points | Strength Level |
|--------------|----------------|
| >= 4 | PM3_VeryStrong |
| >= 2 and < 4 | PM3_Strong |
| >= 1 and < 2 | PM3 (Moderate) |
| = 0.5 | PM3_Supporting |

#### CMMRD Diagnostic Scoring System (Aronson et al. 2022)

>= 3 points = CMMRD features meets PM3 criteria (after excluding the diagnosis of NF1 or LFS, as individuals with those disorders could easily reach 3 points).

**Malignancies/premalignancies** (one is mandatory; if more than one is present, add the points):

| Feature | Points |
|---------|--------|
| Carcinoma from the LS spectrum* at age <25 years | 3 |
| Multiple bowel adenomas at age <25 years and absence of APC/MUTYH mutation(s) or a single high-grade dysplasia adenoma at age <25 years | 3 |
| WHO grade III or IV glioma at age <25 years | 2 |
| NHL of T cell lineage or sPNET at age <18 years | 2 |
| Any malignancy at age <18 years | 1 |

**Additional features** (optional; if more than one is present, add the points):

| Feature | Points |
|---------|--------|
| Clinical sign of NF1 and/or >=2 hyperpigmented and/or hypopigmented skin alterations diameter >1 cm | 2 |
| Diagnosis of LS in a first-degree or second-degree relative | 2 |
| Carcinoma from LS spectrum* before the age of 60 in a first-degree, second-degree or third-degree relative | 1 |
| A sibling with carcinoma from the LS spectrum*, high-grade glioma, sPNET or NHL | 2 |
| A sibling with any type of childhood malignancy | 1 |
| Multiple pilomatricomas in the patient | 2 |
| One pilomatricoma in the patient | 1 |
| Agenesis of the corpus callosum or non-therapy-induced cavernoma in the patient | 1 |
| Consanguineous parents | 1 |
| Deficiency/reduced levels of IgG2/4 and/or IgA | 1 |

*LS spectrum cancers: colorectal, endometrial, small bowel, ureter, renal pelvis, biliary tract, stomach, bladder carcinoma.*

---

### PM4 - Protein Length Changes

**Original ACMG Summary:** Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

***Not Applicable***

**Comments:** Protein length change from an in-frame variant is not used due to lack of evidence.

---

### PM5 - Novel Missense at Same Residue

**Original ACMG Summary:** Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before. Example: Arg156His is pathogenic; now you observe Arg156Cys. Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Moderate** | Missense change at an amino acid residue where a different missense change was classified by this VCEP as Pathogenic on the protein level and not due to aberrant splicing. Only use PM5 if PP3 is supporting for the missense change. Use PM5_Supporting if other variant is Likely Pathogenic due to a missense alteration. |
| **Supporting** | Missense change at an amino acid residue where a different missense change was classified as Likely Pathogenic on the protein level and not due to aberrant splicing. Only use PM5_Supporting if PP3 is supporting for the missense change. Use PM5 if other variant is Pathogenic due to a missense alteration. |

---

### PM6 - De Novo (Assumed)

**Original ACMG Summary:** Assumed de novo, but without confirmation of paternity and maternity.

***Not Applicable***

**Comments:** Please see PS2 — assumed de novo is incorporated into the PS2 point-based system (0.5 points per proband with assumed de novo and unconfirmed maternity/paternity).

---

### PP1 - Co-segregation

**Original ACMG Summary:** Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease. Note: May be used as stronger evidence with increasing segregation data.

**VCEP Specifications:** For multiple pedigrees, results are combined by multiplying together.

Recommended segregation analysis tool: **COOL (COsegregation OnLine) v3** — https://fenglab.chpc.utah.edu/cool3/manual.html

Copy the example pedigree format and complete the fields to build the pedigree in text format. Refer to online manual for cancer types to enter into pedigree. Click on the 'Analysis' tab to view the webform for pedigree file upload and enter appropriate parameters for population and allele frequency. Penetrance file and relative risk file are not required for MMR genes. Use the 'overall Bayes Factor' to determine evidence strength.

Penetrance estimates for *PMS2* are from ten Broeke et al. 2015.

| Strength | Bayes Likelihood Ratio |
|----------|----------------------|
| **Strong** | Combined Bayes Likelihood Ratio >18.7 in >=2 families |
| **Moderate** | Combined Bayes Likelihood Ratio >4.3 & <=18.7 |
| **Supporting** | Combined Bayes Likelihood Ratio >2.08 & <=4.3 |

---

### PP2 - Missense in Constrained Gene

**Original ACMG Summary:** Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.

***Not Applicable***

**Comments:** Missense variant in a gene with low rate of benign missense changes does not apply.

---

### PP3 - Computational Evidence

**Original ACMG Summary:** Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.). Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.

**VCEP Specifications:** SpliceAI masked score option should be checked on. For HCI-PRIORS, ensure correct gene is selected from the tabs, and enter the nucleotide number in either HGVS position or HG38 genomic co-ordinate and click 'view'. The output shows 3 substitutions at the nucleotide location, with probability based on splicing and protein predictions. Ensure the 'applicable prior' is used that corresponds to the variant under review.

| Strength | Criteria |
|----------|----------|
| **Moderate** | Missense variant with HCI prior probability for pathogenicity >0.81 as per https://hci-priors.hci.utah.edu/PRIORS |
| **Supporting** | Missense variant with "MAPP/PP2 Prior P" score >0.68 & <=0.81 from http://hci-lovd.hci.utah.edu/variants.php?select_db=PMS2_priors&action=search_unique **OR** Predicted splice defect for non-canonical splicing nucleotides using SpliceAI with delta score >= 0.2 as per Walker et al 2023. |

**Derivation of probability values from Odds:**
- 0.68 probability corresponds to odds of 2.08 for Pathogenic Supporting level of evidence using 0.5 prior — consistent with ACMG Bayesian model.
- 0.81 probability corresponds to odds of 4.3 for Pathogenic Moderate level of evidence using 0.5 prior — consistent with ACMG Bayesian model.

---

### PP4 - Phenotype Specificity

**Original ACMG Summary:** Patient's phenotype or family history is highly specific for a disease with a single genetic etiology.

**VCEP Specifications:**

Standard MSI markers panel: BAT25, BAT26, BAT40, BAT34, D5S346, D17S250, ACTC, D18S55, D10S197, MYCL; D2S123, D18S69; NR21, NR24, NR27.

**Protein Expression and consistency with variant location:**

IHC evidence should be consistent with the variant gene and the protein that is tested and take into account the MutS-alpha and MutL-alpha heterodimers:
- MLH1 and PMS2 loss is consistent with an *MLH1* pathogenic variant
- MSH2 and MSH6 loss is consistent with an *MSH2* pathogenic variant
- MSH6 loss is consistent with an *MSH6* pathogenic variant
- **PMS2 loss is consistent with a *PMS2* pathogenic variant**

| Strength | Criteria |
|----------|----------|
| **Strong** | >=3 independent CRC/Endometrial MSI-H tumors in >=2 families using a standard panel of 5-10 markers or tumor genome **and/or** loss of MMR protein expression consistent with the variant location. MSI-H tumor with inconsistent protein expression does not meet PP4_Strong. Independent tumors can be from the same patient/family. |
| **Moderate** | 2 independent CRC/Endometrial MSI-H tumors using a standard panel of 5-10 markers or tumor genome **and/or** loss of MMR protein expression consistent with the variant location. MSI-H tumor with inconsistent protein expression does not meet PP4_Moderate. |
| **Supporting** | 1 CRC/Endometrial MSI-H tumor using a standard panel of 5-10 markers or tumor genome **and/or** loss of MMR protein expression consistent with the variant location. MSI-H tumor with inconsistent protein expression does not meet PP4. |

---

### PP5 - Reputable Source

**Original ACMG Summary:** Reputable source recently reports variant as pathogenic, but the evidence is not available to the laboratory to perform an independent evaluation.

***Not Applicable***

This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PMID: 29543229).

---

## Benign Criteria

### BA1 - Allele Frequency >5%

**Original ACMG Summary:** Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

**VCEP Specification (Stand Alone):**
- GnomAD v4 Grpmax filtering allele frequency **>= 0.0028 (0.28%)** and variant is excluded as founder pathogenic variant.

---

### BS1 - Frequency Greater Than Expected

**Original ACMG Summary:** Allele frequency is greater than expected for disorder.

**VCEP Specification (Strong):**
- GnomAD v4 Grpmax filtering allele frequency **>= 0.0001 and < 0.001 (0.01-0.1%)** and variant is excluded as founder pathogenic variant.

---

### BS2 - Observed in Healthy Adult

**Original ACMG Summary:** Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

**VCEP Specification (Strong):**

Co-occurrence *in trans* with a known pathogenic sequence variant in the same gene in a patient with colorectal cancer after age 45 (or other LS cancer above the median age of onset for that cancer in LS), and who has no previous or current evidence of clinical manifestations of CMMRD as per Aronson et al 2022 (Refer to 'Table for CMMRD diagnosis' in Appendix D). Confirmation of phase requires testing of parents or offspring.

---

### BS3 - Functional Studies (No Effect)

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

**VCEP Specifications:** Refer to file 'Functional assay SVI documentation (MMR genes)' for calibrated functional assays.

> *The functional assay flowchart is a general framework for evaluating functional assays that were already performed, or from historic publications, not for prospective studies on variants. The information describing these assays are generic. The VCEP recommends use of the calibrated assays for prospective testing.*

| Strength | Criteria |
|----------|----------|
| **Strong** | Calibrated functional assays with functional odds for Pathogenicity <= 0.05 **OR** Synonymous substitutions and intronic variants with no associated mRNA aberration (either splicing or allelic imbalance) as determined by laboratory assays conducted with nonsense-mediated decay inhibition. Whenever abnormal transcripts are identified at similar levels in controls they will be considered naturally occurring isoforms and not mRNA aberrations. |
| **Supporting** | Calibrated functional assays with functional odds for Pathogenicity >0.05 & <=0.48 **OR** Variant-specific proficient function in protein and mRNA-based lab assays as per MMR functional assay flowchart. |

---

### BS4 - Lack of Segregation

**Original ACMG Summary:** Lack of segregation in affected members of a family. Caveat: The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.

**VCEP Specifications:** For multiple pedigrees, results are combined by multiplying together.

Recommended segregation analysis tool: **COOL (COsegregation OnLine) v3** — https://fenglab.chpc.utah.edu/cool3/manual.html

| Strength | Bayes Likelihood Ratio |
|----------|----------------------|
| **Strong** | Combined Bayes Likelihood Ratio <0.05 |
| **Supporting** | Combined Bayes Likelihood Ratio >0.05 & <=0.48 |

---

### BP1-BP7 - Benign Supporting

| Criterion | Status | Comment |
|-----------|--------|---------|
| **BP1** | *Not Applicable* | Missense variant in a gene where only loss of function causes disease is not applicable. |
| **BP2** | *Not Applicable* | BS2 is used instead. |
| **BP3** | *Not Applicable* | In-frame deletions/insertions in a repetitive region without a known function is not used. |
| **BP4** | Supporting | Missense variant with "MAPP/PP2 Prior P" score <0.11 from http://hci-lovd.hci.utah.edu/variants.php?select_db=PMS2_priors&action=search_unique **OR** For intronic and synonymous variants: SpliceAI predicts no splicing impact with delta score <= 0.1 as per Walker et al 2023. SpliceAI masked score option should be checked on. |
| **BP5** | Supporting / Strong | **Strong:** >=4 tumors: CRC/Endometrial tumors with MSS and/or no loss of MMR protein expression and/or LS spectrum tumors with loss of MMR protein(s) that is inconsistent with the gene demonstrating genetic variation **OR** >=2 BRAF V600E (CRC only)/MLH1 methylation (in LS spectrum tumor only) with MSI-H/MLH1 loss. **Supporting:** 2 or 3 tumors: CRC/Endometrial tumors with MSS and/or no loss of MMR protein expression and/or LS spectrum tumors with loss of MMR protein(s) that is inconsistent with the gene demonstrating genetic variation **OR** 1 BRAF V600E (Colon only)/MLH1 methylation (in LS spectrum tumor only) with MSI-H/MLH1 loss. |
| **BP6** | *Not Applicable* | This criterion is not for use as recommended by the ClinGen SVI VCEP Review Committee (PMID: 29543229). |
| **BP7** | Supporting | A synonymous (silent) or intronic variant at or beyond -21/+7 (5'/3' exonic). Variants may satisfy both BP7 and BP4. |

**Note on BP4 probability derivation:** 0.11 probability corresponds to odds of 0.48 for Benign Supporting level of benign evidence using 0.2 prior — consistent with ACMG Bayesian model.

---

## Rules for Combining Criteria

### Pathogenic Classification

| Criteria Combination |
|---------------------|
| 1 Very Strong (PVS1) **AND** >= 1 Strong (PVS1_Strong, PS1, PS2, PS3, PP1_Strong, PP4_Strong) |
| 1 Very Strong (PVS1) **AND** >= 2 Moderate (PVS1_Moderate, PS1_Moderate, PS2_Moderate, PS3_Moderate, PM3, PM5, PM6, PP1_Moderate, PP3_Moderate, PP4_Moderate) |
| 1 Very Strong (PVS1) **AND** >= 2 Supporting (PS3_Supporting, PM2_Supporting, PM5_Supporting, PP1, PP3, PP4) |
| >= 2 Strong (PVS1_Strong, PS1, PS2, PS3, PP1_Strong, PP4_Strong) |
| 1 Strong **AND** >= 3 Moderate |
| 1 Strong **AND** 2 Moderate **AND** >= 2 Supporting |
| 1 Strong **AND** 1 Moderate **AND** >= 4 Supporting |
| 1 Very Strong (PVS1) **AND** >= 1 Moderate |

### Likely Pathogenic Classification

| Criteria Combination |
|---------------------|
| 1 Very Strong (PVS1) **AND** 1 Supporting |
| 1 Strong **AND** 1 Moderate |
| 1 Strong **AND** >= 2 Supporting |
| >= 3 Moderate |
| 2 Moderate **AND** >= 2 Supporting |
| 1 Moderate **AND** >= 4 Supporting |
| 1 Strong **AND** 2 Moderate |

### Benign Classification

| Criteria Combination |
|---------------------|
| >= 2 Strong (BS1, BS2, BS3, BS4, BP5_Strong) |
| 1 Stand Alone (BA1) |

### Likely Benign Classification

| Criteria Combination |
|---------------------|
| 1 Strong (BS1, BS2, BS3, BS4, BP5_Strong) **AND** 1 Supporting (BS3_Supporting, BS4_Supporting, BP4, BP5, BP7) |
| >= 2 Supporting (BS3_Supporting, BS4_Supporting, BP4, BP5, BP7) |

---

## Appendices

### Appendix A: PVS1 Decision Tree

The PVS1 Decision Tree for MMR genes provides a structured framework for assigning PVS1 strength levels based on variant type:

**Nonsense or Frameshift:**
- Predicted to undergo NMD (PTC <= codon 798 in PMS2): **PVS1**
- Not predicted to undergo NMD, but truncated region is critical to protein function (PTC <= codon 798): **PVS1**
- Not predicted to undergo NMD, role of region unknown (codons 799-862 in PMS2): **PVS1_Moderate**

**GT-AG 1,2 Splice Sites:**
- Exon skipping or cryptic splice site disrupts reading frame and predicted to undergo NMD: **PVS1**
- Exon skipping or cryptic splice site disrupts reading frame and NOT predicted to undergo NMD: **PVS1_Moderate**
- Exon skipping or cryptic splice site preserves reading frame: **PVS1_Strong**

**Deletion (Single exon to full gene):** **PVS1**

**Duplication (>=1 exon, completely contained within gene):**
- Proven in tandem, frameshift before last splice junction (NMD predicted): **PVS1**
- Proven in tandem, in-frame insertion disrupting functional domain: **PVS1**
- Presumed in tandem, frameshift before last splice junction: **PVS1_Strong**

**Initiation Codon:**
- *PMS2* initiation codon variants: **PVS1_Strong**

### Appendix B: MMR Functional Domains for PMS2

PMS2 protein functional domains (amino acid positions):

| Exon(s) | Nucleotide Range | Amino Acid Range | Domain |
|---------|-----------------|------------------|--------|
| 1 | 1-23 | 1-8 | — |
| 2 | 24-163 | 8-55 | ATPase |
| 3 | 164-250 | 55-84 | ATPase |
| 4 | 251-353 | 84-118 | ATPase |
| 5 | 354-537 | 118-179 | ATPase |
| 6 | 538-705 | 180-235 | ATPase |
| 7 | 706-803 | 236-268 | — |
| 8 | 804-903 | 268-301 | — |
| 9 | 904-988 | 302-330 | — |
| 10 | 989-1144 | 330-382 | — |
| 11 | 1145-2006 | 382-669 | NLS (625-632, 675) |
| 12-15 | 2007-2599 | 669-862 | MLH1 interaction (725-759, 759-815, 816-862) |

**NLS (Nuclear Localization Signal):** codons 585-595, 650-663
**NES (Nuclear Export Signal):** codons 469-478

### Appendix C: Population Frequency Thresholds Summary

| Criterion | Threshold | Strength |
|-----------|-----------|----------|
| BA1 | >= 0.0028 (0.28%) gnomAD v4 Grpmax FAF | Stand Alone |
| BS1 | >= 0.0001 and < 0.001 (0.01-0.1%) gnomAD v4 Grpmax FAF | Strong |
| PM2 | < 0.00002 (1 in 50,000 alleles) gnomAD v4 | Supporting |

### Appendix D: MMR Functional Assay Flowchart

The MMR functional assay flowchart guides evaluation of functional data based on variant type:

1. **In-frame indel or missense variant:**
   - If first/last 3 bases of exon or splicing impact predicted → treat as splice site variant
   - If calibrated functional assay conducted → use quantitative multifactorial analysis OR convert functional LR to ACMG/AMP evidence weight
   - If no calibrated assay → require 2 independent assays with concordant results:
     - Mammalian MMR activity assays → assess repair levels
     - If similar to deficient cell line/pathogenic controls → assess protein expression/stability
       - <=25% relative expression → **Deficient function**
       - >=75% relative expression → subcellular localization and cellular-based MMR activity assays
         - Cytoplasmic, tolerant to DNA damage or high mutator phenotype → **Deficient function**
         - Nuclear, sensitive to DNA damage and no mutator phenotype → **Proficient function**

2. **Splice site, silent, or intronic variant:**
   - Splicing assay → evaluate extent of impact
     - Complete impact → **Deficient function**
     - No impact + in-frame or missense variant → route through in-frame/missense pathway
     - No impact + not in-frame/missense → **Proficient function**
     - Unknown/Partial impact + in-frame or missense → route through in-frame/missense pathway
     - Unknown/Partial impact + not in-frame/missense → check for NMD-inhibitors and patient-derived RNA assays → further research calibrating against clinical data

### Appendix E: Reference PMIDs

| # | Reference |
|---|-----------|
| 1 | Belman S, Parsons MT et al. *Considerations in assessing germline variant pathogenicity using cosegregation analysis.* **Genet Med** (2020) 22(12):2052-2059. PMID: 32773770 |
| 2 | Aronson M, Colas C et al. *Diagnostic criteria for constitutional mismatch repair deficiency (CMMRD): recommendations from the international consensus working group.* **J Med Genet** (2022) 59(4):318-327. PMID: 33622763 |
| 3 | Li S, Qian D et al. *Tumour characteristics provide evidence for germline mismatch repair missense variant pathogenicity.* **J Med Genet** (2020) 57(1):62-69. PMID: 31391288 |
| 4 | Canson DM, Dumenil T et al. *The splicing effect of variants at branchpoint elements in cancer genes.* **Genet Med** (2022) 24(2):398-409. PMID: 34906448 |
| 5 | Cyr JL, Brown GD et al. *The predicted truncation from a cancer-associated variant of the MSH2 initiation codon alters activity of the MSH2-MSH6 mismatch repair complex.* **Mol Carcinog** (2012) 51(8):647-58. PMID: 21837758 |
| 6 | Drost M, Tiersma Y et al. *A functional assay-based procedure to classify mismatch repair gene variants in Lynch syndrome.* **Genet Med** (2019) 21(7):1486-1496. PMID: 30504929 |
| 7 | Drost M, Tiersma Y et al. *Two integrated and highly predictive functional analysis-based procedures for the classification of MSH6 variants in Lynch syndrome.* **Genet Med** (2020) 22(5):847-856. PMID: 31965077 |
| 8 | Rath A, Radecki AA et al. *A calibrated cell-based functional assay to aid classification of MLH1 DNA mismatch repair gene variants.* **Hum Mutat** (2022) 43(12):2295-2307. PMID: 36054288 |
| 9 | Rayner E, Tiersma Y et al. *Predictive functional assay-based classification of PMS2 variants in Lynch syndrome.* **Hum Mutat** (2022) 43(9):1249-1258. PMID: 35451539 |
| 10 | Tavtigian SV, Greenblatt MS et al. *Modeling the ACMG/AMP variant classification guidelines as a Bayesian classification framework.* **Genet Med** (2018) 20(9):1054-1060. PMID: 29300386 |
| 11 | Abou Tayoun AN, Pesaran T et al. *Recommendations for interpreting the loss of function PVS1 ACMG/AMP variant criterion.* **Hum Mutat** (2018) 39(11):1517-1524. PMID: 30192042 |
| 12 | Thompson BA, Walters R et al. *Contribution of mRNA Splicing to Mismatch Repair Gene Sequence Variant Interpretation.* **Front Genet** (2020) 11:798. PMID: 32849802 |
| 13 | Whiffin N, Minikel E et al. *Using high-resolution variant frequencies to empower clinical genome interpretation.* **Genet Med** (2017) 19(10):1151-1158. PMID: 28518168 |
| 14 | Walker LC, Hoya M et al. *Using the ACMG/AMP framework to capture evidence related to predicted and observed impact on splicing: Recommendations from the ClinGen SVI Splicing Subgroup.* **Am J Hum Genet** (2023) 110(7):1046-1067. PMID: 37352859 |

---

## Version History

| Version | Date | Notes |
|---------|------|-------|
| 1.0.0 | 8/9/2024 | Initial release |

---

*This document was compiled from ClinGen InSiGHT Hereditary Colorectal Cancer/Polyposis VCEP specifications and ClinGen SVI recommendations. For the most current version, please refer to the ClinGen website.*
