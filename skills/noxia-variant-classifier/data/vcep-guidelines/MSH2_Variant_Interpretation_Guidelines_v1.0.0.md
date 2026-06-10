# ClinGen InSiGHT Hereditary Colorectal Cancer/Polyposis VCEP Variant Interpretation Guidelines for MSH2

**Version:** 1.0.0
**Released:** 8/9/2024
**Affiliation:** InSiGHT Hereditary Colorectal Cancer/Polyposis VCEP
**Based on:** Richards et al., 2015 ACMG/AMP Guidelines

---

## Gene Information

| Attribute | Value |
|-----------|-------|
| **Gene** | MSH2 (HGNC:7325) |
| **HGNC Name** | mutS homolog 2 |
| **Transcript** | NM_000251.3 |
| **Disease** | Lynch syndrome 1 (MONDO:0007356) |
| **Inheritance** | Autosomal dominant inheritance |
| **Disease (AR)** | Mismatch repair cancer syndrome 1 (MONDO:0010159) |
| **Inheritance (AR)** | Autosomal recessive inheritance |

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

**VCEP Specifications:** PVS1 does not apply for variants in the initiation codon of MSH2 as further ATGs exist inframe in exon 1, so this criterion is not applicable at any evidence weight for initiation codon variants.

#### Strength Levels

| Strength | Criteria |
|----------|----------|
| **Very Strong (PVS1)** | Nonsense/frameshift variant introducing Premature Termination Codon (PTC) ≤ codon 891 in MSH2. **OR** Large genomic alterations of single or multi-exon size. **OR** Variants at IVS±1 or IVS±2 where exon skipping or use of a cryptic splice site disrupts reading frame and is predicted to undergo NMD (not to be combined with PP3; not for confirmed splice defects). **OR** Variants where mRNA assays using RNA derived from patient constitutional biological samples indicate splicing aberration (with evidence that variant allele produces no full-length/reference transcript) leading to premature stop codon or in-frame deletion disrupting a functional domain or protein conformation. Splicing aberration must be confirmed in a minigene assay or an additional RNA assay from an independent laboratory if it is a non-canonical splice site variant. |
| **Strong (PVS1_Strong)** | Presumed by default in tandem duplication of ≥1 exon resulting in a frameshift before the last splice junction. This rule does not apply for variants that involve the UTR (i.e. exon 1 or last exon) and whole gene duplications. **OR** G>non-G at last base of exon if first 6 bases of the intron are not GTRRGT. If confirmed to cause a splice defect, then PVS1 should be used instead. **OR** Variants at IVS±1 or IVS±2 where exon skipping or use of a cryptic splice site preserves reading frame and the altered region is critical to protein function (not to be combined with PP3; not for confirmed splice defects). |
| **Moderate (PVS1_Moderate)** | Nonsense/frameshift variant introducing premature termination codon between codons 892 & 934 in MSH2. **OR** Variants at IVS±1 or IVS±2 where exon skipping or use of a cryptic splice site disrupts reading frame and is NOT predicted to undergo NMD. |
| **Not Applicable** | Variants in the initiation codon of MSH2 |

#### PVS1 Decision Tree for MSH2

**Nonsense or Frameshift Variants:**

| Condition | Strength |
|-----------|----------|
| Predicted to undergo NMD (PTC ≤ codon 861) | PVS1 |
| Not predicted to undergo NMD, truncated region critical (PTC ≤ codon 891) | PVS1 |
| Not predicted to undergo NMD, role of region unknown (codons 892-934) | PVS1_Moderate |

**GT-AG 1,2 Splice Sites:**

| Condition | Strength |
|-----------|----------|
| Exon skipping or cryptic splice site disrupts reading frame AND predicted to undergo NMD | PVS1 |
| Exon skipping or cryptic splice site disrupts reading frame AND NOT predicted to undergo NMD | PVS1_Moderate |
| Exon skipping or cryptic splice site preserves reading frame (altered region critical to protein function) | PVS1_Strong |

**Deletions (Single exon to full gene):** PVS1

**Duplications (≥1 exon, completely contained within gene):**

| Condition | Strength |
|-----------|----------|
| Proven in tandem with frameshift or disruption of functional domain | PVS1 |
| Presumed in tandem with frameshift before last splice junction | PVS1_Strong |

**Initiation Codon:** Not Applicable for MSH2 (further ATGs exist inframe in exon 1)

---

### PS1 - Same Amino Acid Change

**Original ACMG Summary:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.

**Example:** Val->Leu caused by either G>C or G>T in the same codon.

**Caveat:** Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:** SpliceAI masked score option should be checked on.

| Strength | Criteria |
|----------|----------|
| **Strong (PS1)** | A predicted missense substitution that encodes the same amino acid change with a different underlying nucleotide change previously established by this VCEP as Pathogenic (not a predicted or confirmed splice defect). **OR** Variants affecting the same non-canonical splice nucleotide as a confirmed pathogenic splice variant with similar or worse splicing in silico prediction using SpliceAI. |
| **Moderate (PS1_Moderate)** | A predicted missense substitution that encodes the same amino acid change with a different underlying nucleotide change as a previously established Likely Pathogenic missense variant with normal RNA result*, and PM2_supporting is met. *Otherwise, if the previously established Likely Pathogenic missense variant truly is a splice defect, the new missense variant also has to be investigated on a functional level for RNA splicing. |

---

### PS2 - De Novo (Confirmed)

**Original ACMG Summary:** De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.

**Note:** Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.

**VCEP Specifications:** Point-based system for de novo evidence

#### De Novo Point System

| Evidence Type | Points |
|---------------|--------|
| Proband with a *de novo* variant with both maternity and paternity confirmed in a case with MMR deficient LS spectrum tumor (MSI/IHC consistent with affected gene, no MLH1 methylation in tumor tissue) | **2 points per proband** |
| Proband with a *de novo* variant with both maternity and paternity confirmed in a case with LS spectrum tumor (no tumor data for MSI/IHC/methylation) | **1 point per proband** |
| Proband with assumed *de novo* variant and maternity and/or paternity unconfirmed with LS spectrum tumor (no tumor data for MSI/IHC/methylation) | **0.5 points per proband** |

**Lynch Syndrome (LS) tumors include:** colorectal/colon/rectal, endometrial, ovarian, small bowel/small intestine, renal pelvis, ureter, and stomach/gastric carcinomas, sebaceous skin tumors (adenomas and carcinomas), gliomas.

#### PS2 Strength Thresholds

| Points | Strength Level |
|--------|----------------|
| ≥ 4 | PS2 (Very Strong) |
| 2-3 | PS2 (Strong) |
| 1 | PS2_Moderate |
| 0.5 | PS2_Supporting |

---

### PS3 - Functional Studies

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.

**Note:** Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.

**VCEP Specifications:** Refer to the 'Functional assay SVI documentation (MMR genes)' for calibrated functional assays.

*The functional assay flowchart is a general framework for evaluating functional assays that were already performed, or from historic publications, not for prospective studies on variants. The information describing these assays are generic. The VCEP recommends use of the calibrated assays for prospective testing.*

| Strength | Criteria |
|----------|----------|
| **Strong (PS3)** | Calibrated functional assays with functional odds for Pathogenicity > 18.7 |
| **Moderate (PS3_Moderate)** | Calibrated functional assays with functional odds for pathogenicity >4.3 and ≤18.7 **OR** MMR function defect following functional assay flowchart* **OR** Variants with monoallelic expression: complete loss of expression (<10% of wild-type in cDNA without puromycin) of the variant allele. Full-length transcript should be analysed with and without NMD block. |
| **Supporting (PS3_Supporting)** | Calibrated functional odds for Pathogenicity >2.08 and ≤4.3 |

#### Approved Functional Assays

| Assay | Author/Year | PMID | Gene(s) | Proposed Strength | Threshold for Abnormal | Threshold for Normal |
|-------|-------------|------|---------|-------------------|------------------------|---------------------|
| CIMRA (Cell-free In vitro MMR Activity) | Drost 2018/2020 | 30504929; 31965077 | MLH1, MSH2, MSH6, PMS2 | PS3, PS3_Moderate, PS3_Supporting, BS3, BS3_Supporting | <23% (MLH1, MSH2); <18% (MSH6, PMS2) | ≥70% (MLH1, MSH2); ≥100% (MSH6, PMS2) |
| MSH2 Deep Mutational Scan | Jia/Scott 2021/2022 | 33357406; 36550560 | MSH2 | PS3, BS3 | LOF score > 0.4 | LOF score ≤ 0 |
| hESC CRISPR-based Functional Assay | Rath 2022 | 36054288 | MLH1 | PS3, PS3_Moderate, PS3_Supporting, BS3, BS3_Supporting | OddsPath_Functional > 2.08 | OddsPath_Functional < 0.48 |
| Cell-free MMR Repair Assay | Thompson 2013 | 24362816 | MMR genes | PS3_Moderate, BS3_Supporting | <25% in two independent assays | >75% in two independent assays |
| Mammalian MMR Complementation Assay | Thompson 2013 | 24362816 | MMR genes | PS3_Moderate, BS3_Supporting | <25% in two independent assays | >75% in two independent assays |
| Cellular MMR Expression Assay | Thompson 2013 | 24362816 | MMR genes | PS3_Moderate, BS3_Supporting | <25% expression | >75% expression |
| Subcellular Localization Assay | Thompson 2013 | 24362816 | MMR genes | PS3_Moderate, BS3_Supporting | Cytoplasmic localization | Nuclear localization |
| cDNA Full-Length Transcript Analysis | Morak 2019 | 31332305 | MMR genes | PS3_Moderate, BS3_Supporting | Allelic loss (≤10%) | Biallelic (50 ± 10%) |
| MNNG Cell Survival Assay | Bouvet 2019 | 30998989 | MLH1, MSH2 | PS3_Moderate, BS3_Supporting | Mean survival > 45.54% (MSH2) | Mean survival < 45.54% (MSH2) |

---

### PS4 - Prevalence in Affected

**Original ACMG Summary:** The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.

**VCEP Specifications:** *Not Applicable*

**Comments:** Due to the availability of tumor IHC data for variant classification (see PP4), PS4 has not been utilized for MMR variant classification using proband counting.

---

### PM1 - Mutational Hot Spot

**Original ACMG Summary:** Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.

**VCEP Specifications:** *Not Applicable*

**Comments:** There are no recognized mutational hot spots that could be used for classification purposes. While there are functional domains in the MMR genes, the distribution of pathogenic variants is generalized over all the domains (unpublished data).

---

### PM2 - Absent from Controls

**Original ACMG Summary:** Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

**Caveat:** Population data for indels may be poorly called by next generation sequencing.

| Strength | Criteria |
|----------|----------|
| **Supporting (PM2_Supporting)** | Absent/extremely rare (<1 in 50,000 alleles) in gnomAD v4 dataset |

---

### PM3 - In Trans with Pathogenic

**Original ACMG Summary:** For recessive disorders, detected in trans with a pathogenic variant.

**Note:** This requires testing of parents (or offspring) to determine phase.

**VCEP Specifications:** Co-occurrence with a known pathogenic/likely pathogenic sequence variant in the same gene in a patient with clinical features consistent with CMMRD as per Aronson et al 2022. For MLH1 variants - the variant has to meet PM2_Supporting criteria.

#### PM3 Point System

| Classification/Zygosity of Other Variant | Points |
|------------------------------------------|--------|
| Pathogenic/Likely Pathogenic in trans | 1.0 point |
| Pathogenic/Likely Pathogenic - phase unknown | 0.5 points |

Sum all cases with the above evidence to determine the PM3 strength.

#### PM3 Strength Thresholds

| Total Points | Strength Level |
|--------------|----------------|
| ≥ 4 | PM3_VeryStrong |
| ≥ 2 and < 4 | PM3_Strong |
| ≥ 1 and < 2 | PM3 (Moderate) |
| = 0.5 | PM3_Supporting |

---

### PM4 - Protein Length Changes

**Original ACMG Summary:** Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

**VCEP Specifications:** *Not Applicable*

**Comments:** Protein length change from an in-frame variant is not used due to lack of evidence.

---

### PM5 - Novel Missense at Same Residue

**Original ACMG Summary:** Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.

**Example:** Arg156His is pathogenic; now you observe Arg156Cys.

**Caveat:** Beware of changes that impact splicing rather than at the amino acid/protein level.

| Strength | Criteria |
|----------|----------|
| **Moderate (PM5)** | Missense change at an amino acid residue where a different missense change was classified by this VCEP as Pathogenic on the protein level and not due to aberrant splicing. Only use PM5 if PP3 is supporting for the missense change. Use PM5_Supporting if other variant is Likely Pathogenic due to a missense alteration. |
| **Supporting (PM5_Supporting)** | Missense change at an amino acid residue where a different missense change was classified as Likely Pathogenic on the protein level and not due to aberrant splicing. Only use PM5_Supporting if PP3 is supporting for the missense change. Use PM5 if other variant is Pathogenic due to a missense alteration. |

---

### PM6 - De Novo (Assumed)

**Original ACMG Summary:** Assumed de novo, but without confirmation of paternity and maternity.

**VCEP Specifications:** *Not Applicable*

**Comments:** Please see PS2 - assumed de novo evidence is incorporated into the PS2 point-based system.

---

### PP1 - Co-segregation

**Original ACMG Summary:** Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.

**Note:** May be used as stronger evidence with increasing segregation data.

**VCEP Specifications:**
- *For multiple pedigrees, results are combined by multiplying together.
- Recommended segregation analysis tool: COOL (COsegregation OnLine) v3 https://fenglab.chpc.utah.edu/cool3/manual.html
- Copy the example pedigree format and complete the fields to build the pedigree in text format. Refer to online manual for cancer types to enter into pedigree. Click on the 'Analysis' tab to view the webform for pedigree file upload and enter appropriate parameters for population and allele frequency. Penetrance file and relative risk file are not required for MMR genes. Use the 'overall Bayes Factor' to determine evidence strength.

| Strength | Criteria |
|----------|----------|
| **Strong (PP1_Strong)** | Co-segregation with disease in pedigree(s) with a combined Bayes Likelihood Ratio >18.7 in ≥2 families |
| **Moderate (PP1_Moderate)** | Co-segregation with disease in pedigree(s) with a combined Bayes Likelihood Ratio >4.3 & ≤18.7 |
| **Supporting (PP1)** | Co-segregation with disease in pedigree(s) with a combined Bayes Likelihood Ratio >2.08 & ≤4.3 |

---

### PP2 - Missense in Constrained Gene

**Original ACMG Summary:** Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.

**VCEP Specifications:** *Not Applicable*

**Comments:** Missense variant in a gene with low rate of benign missense changes does not apply.

---

### PP3 - Computational Evidence

**Original ACMG Summary:** Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).

**Caveat:** As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.

**VCEP Specifications:**
- SpliceAI masked score option should be checked on.
- For HCI-PRIORS, ensure correct gene is selected from the tabs, and enter the nucleotide number in either HGVS position or HG38 genomic co-ordinate and click 'view'. The output shows 3 substitutions at the nucleotide location, with probability based on splicing and protein predictions. Ensure the 'applicable prior' is used that corresponds to the variant under review.

| Strength | Criteria |
|----------|----------|
| **Moderate (PP3_Moderate)** | Missense variant with HCI prior probability for pathogenicity >0.81 as per https://hci-priors.hci.utah.edu/PRIORS |
| **Supporting (PP3)** | Missense variant with HCI prior probability for pathogenicity >0.68 & ≤0.81 as per https://hci-priors.hci.utah.edu/PRIORS **OR** Predicted splice defect for non-canonical splicing nucleotides using SpliceAI with delta score ≥ 0.2 as per Walker et al 2023. |

---

### PP4 - Phenotype Specificity

**Original ACMG Summary:** Patient's phenotype or family history is highly specific for a disease with a single genetic etiology.

**VCEP Specifications:**

**Standard MSI markers panel:** BAT25, BAT26, BAT40, BAT34, D5S346, D17S250, ACTC, D18S55, D10S197, MYCL; D2S123, D18S69; NR21, NR24, NR27

**Protein Expression and consistency with variant location:**
IHC evidence should be consistent with the variant gene and the protein that is tested and take into account the MutSα and MutLα heterodimers:
- MLH1 and PMS2 loss is consistent with an MLH1 pathogenic variant
- **MSH2 and MSH6 loss is consistent with an MSH2 pathogenic variant**
- MSH6 loss is consistent with an MSH6 pathogenic variant
- PMS2 loss is consistent with a PMS2 pathogenic variant

| Strength | Criteria |
|----------|----------|
| **Strong (PP4_Strong)** | ≥3 independent CRC/Endometrial MSI-H tumors in ≥2 families using a standard panel of 5-10 markers or tumor genome **and/or** loss of MMR protein expression consistent with the variant location. MSI-H tumor with inconsistent protein expression does not meet PP4_Strong. Independent tumors can be from the same patient/family. |
| **Moderate (PP4_Moderate)** | 2 independent CRC/Endometrial MSI-H tumors using a standard panel of 5-10 markers or tumor genome **and/or** loss of MMR protein expression consistent with the variant location. MSI-H tumor with inconsistent protein expression does not meet PP4_Moderate. Independent tumors can be from the same patient/family. |
| **Supporting (PP4)** | 1 CRC/Endometrial MSI-H tumor using a standard panel of 5-10 markers or tumor genome **and/or** loss of MMR protein expression consistent with the variant location. MSI-H tumor with inconsistent protein expression does not meet PP4. |

---

### PP5 - Reputable Source

**Original ACMG Summary:** Reputable source recently reports variant as pathogenic, but the evidence is not available to the laboratory to perform an independent evaluation.

**VCEP Specifications:** *Not Applicable*

This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee. (PubMed: 29543229)

---

## Benign Criteria

### BA1 - Allele Frequency >5%

**Original ACMG Summary:** Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

| Strength | Criteria |
|----------|----------|
| **Stand Alone (BA1)** | GnomAD v4 Grpmax filtering allele frequency ≥ 0.001 (0.1%) and variant is excluded as founder pathogenic variant |

---

### BS1 - Frequency Greater Than Expected

**Original ACMG Summary:** Allele frequency is greater than expected for disorder.

| Strength | Criteria |
|----------|----------|
| **Strong (BS1)** | GnomAD v4 Grpmax filtering allele frequency ≥ 0.0001 and < 0.001 (0.01-0.1%) and variant is excluded as founder pathogenic variant |

---

### BS2 - Observed in Healthy Adult

**Original ACMG Summary:** Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

| Strength | Criteria |
|----------|----------|
| **Strong (BS2)** | Co-occurrence *in trans* with a known pathogenic sequence variant in the same gene in a patient with colorectal cancer after age 45 (or other LS cancer above the median age of onset for that cancer in LS), and who has no previous or current evidence of clinical manifestations of CMMRD as per Aronson et al 2022. Confirmation of phase requires testing of parents or offspring. |

---

### BS3 - Functional Studies (No Effect)

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

**VCEP Specifications:** Refer to the 'Functional assay SVI documentation (MMR genes)' for calibrated functional assays.

*The functional assay flowchart is a general framework for evaluating functional assays that were already performed, or from historic publications, not for prospective studies on variants. The information describing these assays are generic. The VCEP recommends use of the calibrated assays for prospective testing.*

| Strength | Criteria |
|----------|----------|
| **Strong (BS3)** | Calibrated functional assays with functional odds for Pathogenicity ≤ 0.05 **OR** Synonymous substitutions and intronic variants with no associated mRNA aberration (either splicing or allelic imbalance) as determined by laboratory assays conducted with nonsense-mediated decay inhibition. Whenever abnormal transcripts are identified at similar levels in controls they will be considered naturally occurring isoforms and not mRNA aberrations. |
| **Supporting (BS3_Supporting)** | Calibrated functional assays with functional odds for Pathogenicity >0.05 & ≤0.48 **OR** Variant-specific proficient function in protein and mRNA-based lab assays as per MMR functional assay flowchart. |

---

### BS4 - Lack of Segregation

**Original ACMG Summary:** Lack of segregation in affected members of a family.

**Caveat:** The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.

**VCEP Specifications:**
- *For multiple pedigrees, results are combined by multiplying together.
- Recommended segregation analysis tool: COOL (COsegregation OnLine) v3 https://fenglab.chpc.utah.edu/cool3/manual.html
- Use the 'overall Bayes Factor' to determine evidence strength.

| Strength | Criteria |
|----------|----------|
| **Strong (BS4)** | Lack of co-segregation with disease in pedigree(s) with a combined Bayes Likelihood Ratio <0.05 |
| **Supporting (BS4_Supporting)** | Lack of co-segregation with disease in pedigree(s) with a combined Bayes Likelihood Ratio >0.05 & ≤0.48 |

---

### BP1-BP7 - Benign Supporting

| Criterion | Status | Comment |
|-----------|--------|---------|
| **BP1** | *Not Applicable* | Missense variant in a gene where only loss of function causes disease is not applicable |
| **BP2** | *Not Applicable* | BS2 is used instead |
| **BP3** | *Not Applicable* | In-frame deletions/insertions in a repetitive region without a known function is not used |
| **BP4** | **Supporting** | Missense variant with HCI-prior probability of pathogenicity <0.11 as per https://hci-priors.hci.utah.edu/PRIORS **OR** For intronic and synonymous variants: SpliceAI predicts no splicing impact with delta score ≤ 0.1 as per Walker et al 2023 |
| **BP5** | **Supporting/Strong** | See below |
| **BP6** | *Not Applicable* | This criterion is not for use as recommended by the ClinGen SVI VCEP Review Committee (PubMed: 29543229) |
| **BP7** | **Supporting** | A synonymous (silent) or intronic variant at or beyond -21/+7 (5'/3' exonic). Variants may satisfy both BP7 and BP4 |

#### BP5 - Variant Found in Case with Alternate Molecular Basis

**Original ACMG Summary:** Variant found in a case with an alternate molecular basis for disease.

| Strength | Criteria |
|----------|----------|
| **Strong (BP5_Strong)** | ≥ 4 tumors: CRC/Endometrial tumors with MSS and/or no loss of MMR protein expression and/or LS spectrum tumors with loss of MMR protein(s) that is inconsistent with the gene demonstrating genetic variation **OR** ≥2 BRAF V600E (CRC only)/*MLH1* methylation (in LS spectrum tumor only) with MSI-H/*MLH1* loss |
| **Supporting (BP5)** | 2 or 3 tumors: CRC/Endometrial tumors with MSS and/or no loss of MMR protein expression and/or LS spectrum tumors with loss of MMR protein(s) that is inconsistent with the gene demonstrating genetic variation **OR** 1 BRAF V600E (Colon only)/*MLH1* methylation (in LS spectrum tumor only) with MSI-H/*MLH1* loss |

---

## Rules for Combining Criteria

### Pathogenic Classification

| Criteria Combination |
|---------------------|
| 1 Very Strong (PVS1) **AND** ≥1 Strong (PVS1_Strong, PS1, PS2, PS3, PP1_Strong, PP4_Strong) |
| 1 Very Strong (PVS1) **AND** ≥2 Supporting (PS3_Supporting, PM2_Supporting, PM5_Supporting, PP1, PP3, PP4) |
| 1 Very Strong (PVS1) **AND** ≥1 Moderate (PVS1_Moderate, PS1_Moderate, PS2_Moderate, PS3_Moderate, PM3, PM5, PM6, PP1_Moderate, PP3_Moderate, PP4_Moderate) |
| ≥2 Strong (PVS1_Strong, PS1, PS2, PS3, PP1_Strong, PP4_Strong) |
| 1 Strong **AND** ≥3 Moderate |
| 1 Strong **AND** 2 Moderate **AND** ≥2 Supporting |
| 1 Strong **AND** 1 Moderate **AND** ≥4 Supporting |

### Likely Pathogenic Classification

| Criteria Combination |
|---------------------|
| 1 Very Strong (PVS1) **AND** 1 Supporting (PS3_Supporting, PM2_Supporting, PM5_Supporting, PP1, PP3, PP4) |
| 1 Strong (PVS1_Strong, PS1, PS2, PS3, PP1_Strong, PP4_Strong) **AND** 1 Moderate |
| 1 Strong **AND** ≥2 Supporting |
| ≥3 Moderate |
| 2 Moderate **AND** ≥2 Supporting |
| 1 Moderate **AND** ≥4 Supporting |
| 1 Strong **AND** 2 Moderate |

### Benign Classification

| Criteria Combination |
|---------------------|
| 1 Stand Alone (BA1) |
| ≥2 Strong (BS1, BS2, BS3, BS4, BP5_Strong) |

### Likely Benign Classification

| Criteria Combination |
|---------------------|
| 1 Strong (BS1, BS2, BS3, BS4, BP5_Strong) **AND** 1 Supporting (BS3_Supporting, BS4_Supporting, BP4, BP5, BP7) |

---

## Appendices

### Appendix A: PVS1 Decision Tree for MMR Genes

See the MMR PVS1 Decision Tree PDF for the complete flowchart showing how to apply PVS1 criteria for:
- Nonsense/Frameshift variants
- GT-AG splice site variants
- Deletions
- Duplications
- Initiation codon variants

**Key MSH2-Specific PVS1 Boundaries:**
- PVS1 (Very Strong): PTC ≤ codon 891
- PVS1_Moderate: PTC between codons 892-934
- Initiation codon variants: Not Applicable (further ATGs exist inframe in exon 1)

### Appendix B: MSH2 Functional Domains

| Domain | Amino Acid Positions | Exons |
|--------|---------------------|-------|
| DNA binding | 1-125 | 1-2 |
| Connector | 125-300 | 2-3 |
| MutLα interaction | 204-225 | 3 |
| EXO1 stabilisation & interaction | 266-378 | 3-5 |
| Lever | 300-457 | 4-7 |
| Clamp | 457-554 | 7-10 |
| MSH3/MSH6 interaction | 426-462, 463-504, 504-554 | 7-10 |
| Lever | 554-620 | 10-11 |
| ATPase | 620-686 | 11-13 |
| MutLα interaction | 625-673 | 11-12 |
| Helix-turn-helix | 762-794 | 14 |
| MSH3/MSH6 interaction | 671-874 | 12-16 |

### Appendix C: CMMRD Diagnostic Scoring System

**Table 3. Scoring system for aiding CMMRD diagnosis from C4CMMRD** (adapted from Aronson et al 2022; PMID: 33622763)

**≥3 points = CMMRD features meets PM3 criteria** (after excluding the diagnosis of NF1 or LFS as individuals with those disorders could easily get to 3 points)

#### Malignancies/premalignancies (one is mandatory; if more than one is present, add the points):

| Feature | Points |
|---------|--------|
| Carcinoma from the LS spectrum* at age <25 years | 3 |
| Multiple bowel adenomas at age <25 years and absence of APC/MUTYH mutation(s) or a single high-grade dysplasia adenoma at age <25 years | 3 |
| WHO grade III or IV glioma at age <25 years | 2 |
| NHL of T cell lineage or sPNET at age <18 years | 2 |
| Any malignancy at age <18 years | 1 |

#### Additional features (optional; if more than one is present, add the points):

| Feature | Points |
|---------|--------|
| Clinical sign of NF1 and/or ≥2 hyperpigmented and/or hypopigmented skin alterations Ø>1 cm | 2 |
| Diagnosis of LS in a first-degree or second-degree relative | 2 |
| Carcinoma from LS spectrum* before the age of 60 in a first-degree, second-degree or third-degree relative | 1 |
| A sibling with carcinoma from the LS spectrum*, high-grade glioma, sPNET or NHL | 2 |
| A sibling with any type of childhood malignancy | 1 |
| Multiple pilomatricomas in the patient | 2 |
| One pilomatricoma in the patient | 1 |
| Agenesis of the corpus callosum or non-therapy-induced cavernoma in the patient | 1 |
| Consanguineous parents | 1 |
| Deficiency/reduced levels of IgG2/4 and/or IgA | 1 |

*Colorectal, endometrial, small bowel, ureter, renal pelvis, biliary tract, stomach, bladder carcinoma

### Appendix D: Functional Assay Flowchart

The MMR Functional Assay Flowchart provides a framework for evaluating functional assay data:

1. **Variant Type Assessment:**
   - In-frame indel or missense variant → Check for splicing impact
   - Splice site, silent, or intronic variant → Proceed to splicing assay

2. **Calibrated Assay Pathway:**
   - If calibrated functional assay conducted → Convert functional LR to ACMG/AMP evidence weight
   - If not → Proceed to flowchart assessment

3. **Non-Calibrated Assay Assessment:**
   - Requires 2 independent assays with concordant results
   - Mammalian MMR activity assays compared to deficient cell line or pathogenic controls
   - Assessment of protein expression/stability
   - Outcomes: Deficient function (PS3_Moderate) or Proficient function (BS3_Supporting)

### Appendix E: Population Frequency Thresholds Summary

| Criterion | Threshold | Strength |
|-----------|-----------|----------|
| BA1 | ≥0.001 (0.1%) gnomAD v4 Grpmax FAF | Stand Alone |
| BS1 | ≥0.0001 and <0.001 (0.01-0.1%) gnomAD v4 Grpmax FAF | Strong |
| PM2 | <0.00002 (<1 in 50,000 alleles) in gnomAD v4 | Supporting |

### Appendix F: In Silico Prediction Tool Thresholds

**HCI-PRIORS (https://hci-priors.hci.utah.edu/PRIORS):**

| Prior Probability | Evidence Level | Corresponding Odds |
|-------------------|----------------|-------------------|
| >0.81 | PP3_Moderate | >4.3 |
| >0.68 & ≤0.81 | PP3 (Supporting) | >2.08 & ≤4.3 |
| <0.11 | BP4 (Supporting) | <0.48 |

**SpliceAI (masked score):**

| Delta Score | Evidence Level |
|-------------|----------------|
| ≥0.2 | PP3 (Supporting) - predicted splice defect |
| ≤0.1 | BP4 (Supporting) - no splicing impact |

### Appendix G: Lynch Syndrome Tumor Types

Lynch Syndrome (LS) tumors include:
- Colorectal/colon/rectal carcinoma
- Endometrial carcinoma
- Ovarian carcinoma
- Small bowel/small intestine carcinoma
- Renal pelvis carcinoma
- Ureter carcinoma
- Stomach/gastric carcinoma
- Sebaceous skin tumors (adenomas and carcinomas)
- Gliomas

### Appendix H: IHC Interpretation for MSH2 Variants

For MSH2 variants, IHC should show:
- **MSH2 and MSH6 loss** = consistent with MSH2 pathogenic variant

This reflects the MutSα heterodimer relationship where MSH2 loss leads to MSH6 instability/loss.

---

## References

1. Belman S, Parsons MT et al. *Considerations in assessing germline variant pathogenicity using cosegregation analysis.* Genet Med (2020) 22(12):2052-2059. PMID: 32773770

2. Aronson M, Colas C et al. *Diagnostic criteria for constitutional mismatch repair deficiency (CMMRD): recommendations from the international consensus working group.* J Med Genet (2022) 59(4):318-327. PMID: 33622763

3. Li S, Qian D et al. *Tumour characteristics provide evidence for germline mismatch repair missense variant pathogenicity.* J Med Genet (2020) 57(1):62-69. PMID: 31391288

4. Canson DM, Dumenil T et al. *The splicing effect of variants at branchpoint elements in cancer genes.* Genet Med (2022) 24(2):398-409. PMID: 34906448

5. Cyr JL, Brown GD et al. *The predicted truncation from a cancer-associated variant of the MSH2 initiation codon alters activity of the MSH2-MSH6 mismatch repair complex.* Mol Carcinog (2012) 51(8):647-58. PMID: 21837758

6. Drost M, Tiersma Y et al. *A functional assay-based procedure to classify mismatch repair gene variants in Lynch syndrome.* Genet Med (2019) 21(7):1486-1496. PMID: 30504929

7. Drost M, Tiersma Y et al. *Two integrated and highly predictive functional analysis-based procedures for the classification of MSH6 variants in Lynch syndrome.* Genet Med (2020) 22(5):847-856. PMID: 31965077

8. Rath A, Radecki AA et al. *A calibrated cell-based functional assay to aid classification of MLH1 DNA mismatch repair gene variants.* Hum Mutat (2022) 43(12):2295-2307. PMID: 36054288

9. Rayner E, Tiersma Y et al. *Predictive functional assay-based classification of PMS2 variants in Lynch syndrome.* Hum Mutat (2022) 43(9):1249-1258. PMID: 35451539

10. Tavtigian SV, Greenblatt MS et al. *Modeling the ACMG/AMP variant classification guidelines as a Bayesian classification framework.* Genet Med (2018) 20(9):1054-1060. PMID: 29300386

11. Abou Tayoun AN, Pesaran T et al. *Recommendations for interpreting the loss of function PVS1 ACMG/AMP variant criterion.* Hum Mutat (2018) 39(11):1517-1524. PMID: 30192042

12. Thompson BA, Walters R et al. *Contribution of mRNA Splicing to Mismatch Repair Gene Sequence Variant Interpretation.* Front Genet (2020) 11:798. PMID: 32849802

13. Whiffin N, Minikel E et al. *Using high-resolution variant frequencies to empower clinical genome interpretation.* Genet Med (2017) 19(10):1151-1158. PMID: 28518168

14. Walker LC, Hoya M et al. *Using the ACMG/AMP framework to capture evidence related to predicted and observed impact on splicing: Recommendations from the ClinGen SVI Splicing Subgroup.* Am J Hum Genet (2023) 110(7):1046-1067. PMID: 37352859

---

## Version History

| Version | Date | Notes |
|---------|------|-------|
| 1.0.0 | 8/9/2024 | Initial release |

---

*This document was compiled from ClinGen InSiGHT Hereditary Colorectal Cancer/Polyposis VCEP specifications and ClinGen SVI recommendations. For the most current version, please refer to the ClinGen website.*
