# ClinGen Congenital Myopathies Expert Panel Variant Interpretation Guidelines for MTM1

**Version:** 1.0.0
**Released:** 8/7/2024
**Affiliation:** Congenital Myopathies VCEP
**Based on:** Richards et al., 2015 ACMG/AMP Guidelines

---

## Gene Information

| Attribute | Value |
|-----------|-------|
| **Gene** | MTM1 (HGNC:7448) |
| **HGNC Name** | myotubularin 1 |
| **Transcript** | NM_000252.3 |
| **Disease** | Centronuclear myopathy (MONDO:0018947) |
| **Inheritance** | X-linked inheritance |

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

**VCEP Specifications:** See PVS1 flowchart (gene-specific modification). MTM1 uses the biologically-relevant transcript NM_000252.3.

#### Strength Levels

| Strength | Criteria |
|----------|----------|
| **Very Strong (PVS1)** | See PVS1 flowchart below |
| **Strong (PVS1_Strong)** | See PVS1 flowchart below |
| **Moderate (PVS1_Moderate)** | See PVS1 flowchart below |
| **Supporting (PVS1_Supporting)** | See PVS1 flowchart below |

#### PVS1 Decision Tree for MTM1

**Nonsense or Frameshift Variants:**

| Condition | NMD Status | Strength |
|-----------|------------|----------|
| Predicted to undergo NMD (up to c.1593, p.531) | NMD expected | **PVS1** |
| Not predicted to undergo NMD, exon present in biologically-relevant transcript | Truncated region critical to protein function | **PVS1_Strong** |
| Not predicted to undergo NMD, exon present in biologically-relevant transcript | Role of region unknown, variant removes >10% of protein | **PVS1_Strong** |
| Not predicted to undergo NMD, exon present in biologically-relevant transcript | Role of region unknown, variant removes <10% of protein | **PVS1_Moderate** |
| Exon absent from biologically-relevant transcript(s) | - | N/A |

**Canonical Splice Site Variants (GT-AG, +/-1,2):**

| Condition | Strength |
|-----------|----------|
| Exon skipping/cryptic splice disrupts reading frame AND NMD predicted | **PVS1** |
| Exon skipping/cryptic splice preserves reading frame (in-frame exons: 2, 5-15), truncated region critical | **PVS1_Strong** |
| Exon skipping/cryptic splice preserves reading frame, role unknown, variant removes >10% | **PVS1_Strong** |
| Exon skipping/cryptic splice preserves reading frame, role unknown, variant removes <10% | **PVS1_Moderate** |
| Exon skipping/cryptic splice disrupts reading frame AND NOT predicted to undergo NMD, truncated region critical | **PVS1_Strong** |
| Exon skipping/cryptic splice disrupts reading frame AND NOT predicted to undergo NMD, role unknown, removes >10% | **PVS1_Strong** |
| Exon skipping/cryptic splice disrupts reading frame AND NOT predicted to undergo NMD, role unknown, removes <10% | **PVS1_Moderate** |

**Deletions (Single exon to full gene):**

| Condition | Strength |
|-----------|----------|
| Full gene deletion | **PVS1** |
| Disrupts reading frame AND NMD predicted | **PVS1** |
| Preserves reading frame, truncated region critical | **PVS1_Strong** |
| Preserves reading frame, role unknown, removes >10% | **PVS1_Strong** |
| Preserves reading frame, role unknown, removes <10% | **PVS1_Moderate** |
| Disrupts reading frame AND NOT predicted to undergo NMD, truncated region critical | **PVS1_Strong** |
| Disrupts reading frame AND NOT predicted to undergo NMD, role unknown, removes >10% | **PVS1_Strong** |
| Disrupts reading frame AND NOT predicted to undergo NMD, role unknown, removes <10% | **PVS1_Moderate** |

**Duplications (>=1 exon, completely contained within gene):**

| Condition | Strength |
|-----------|----------|
| Proven in tandem, reading frame disrupted AND NMD predicted | **PVS1** |
| Presumed in tandem, reading frame presumed disrupted AND NMD predicted | **PVS1_Strong** |
| No or unknown impact on reading frame and NMD | N/A |

**Initiation Codon Variants:**

| Condition | Strength |
|-----------|----------|
| Different functional transcript uses alternative start codon | **PVS1_Supporting** |
| No known alternative start codon, >=1 pathogenic variant upstream of closest potential in-frame start codon | **PVS1_Moderate** |
| No known alternative start codon, no pathogenic variants upstream | N/A |

---

### PS1 - Same Amino Acid Change

**Original ACMG Summary:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.

**Example:** Val->Leu caused by either G>C or G>T in the same codon.

**Caveat:** Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:** No change - use as originally described.

| Strength | Criteria |
|----------|----------|
| **Strong** | Same amino acid change as a previously established pathogenic variant regardless of nucleotide change |
| **Moderate** | No change - use as originally described |
| **Supporting** | No change - use as originally described |

---

### PS2 - De Novo (Confirmed)

**Original ACMG Summary:** De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.

**Note:** Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.

**VCEP Specifications:** No change - use as originally described.

| Strength | Criteria |
|----------|----------|
| **Very Strong** | No change - use as originally described |
| **Strong** | De novo (both maternity and paternity confirmed) in a patient with the disease and no family history |
| **Moderate** | No change - use as originally described |
| **Supporting** | No change - use as originally described |

---

### PS3 - Functional Studies

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.

**Note:** Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | May only be considered for **variant-specific mouse models**. Currently, no other assays are applicable at this strength. (Disease-specific modification) |
| **Moderate** | Where indicated, some of the assays from PS3_Supporting may be stacked to reach Moderate Strength (Gene-specific modification) |
| **Supporting** | Five specific assays are approved (see below). Additional assays may be used if validated appropriately. |

#### PS3_Supporting Approved Assays

The following five assays are approved for PS3_Supporting:

1. **Phosphatase Activity**
   - **Abnormal Readout:** Reduced phosphatase activity (measured via levels of PtdIns and PtdIns5p or increased levels of precursors)
   - **References:** PMID: 10900271, 14660569, 21135508, 12646134, 23071445

2. **Myotubularin Localization**
   - **Abnormal Readout:** Altered localization (presence in spots/aggregates/extensions, loss of cytoplasmic localization)
   - **References:** PMID: 17651088, 12118066, 20682747

3. **Myotubularin Translocation**
   - **Abnormal Readout:** Loss of MTM1 recruitment to late endosomal compartment following EGF stimulation
   - **Reference:** PMID: 14722070

4. **Intracellular Trafficking**
   - **Abnormal Readout:** Reduced localization/trafficking of receptor proteins (trafficking of endosomal cargo is thought to require phosphoinositide conversion and may be disrupted by defective MTM1 activity)
   - **References:** PMID: 14722070, 26760201

5. **Protein and Lipid Association**
   - **Abnormal Readout:** Decreased association with known binding partner (BIN1, Desmin, hVPS34-PI 3-Kinase, MTMR12, Phosphoinositide, or EEA Membrane association)
   - **References:** PMID: 23917616, 21135508, 17651088, 23818870, 14722070

**Important Notes:**
- **Myotubularin Localization and Myotubularin Translocation should NOT be stacked** because they may not be assessing independent biological function
- If not listed above, PS3_Supporting may be used for other functional analyses if:
  - The assay has been validated by a known pathogenic and benign variant AND
  - There is plausible reason that the function the assay is testing relates to the phenotype AND
  - The assay conditions are likely to mimic the physiological environment

---

### PS4 - Prevalence in Affected

**Original ACMG Summary:** The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.

**Notes:**
- Relative risk (RR) or odds ratio (OR), as obtained from case-control studies, is >5.0 and the confidence interval around the estimate of RR or OR does not include 1.0
- In instances of very rare variants where case-control studies may not reach statistical significance, the prior observation of the variant in multiple unrelated patients with the same phenotype, and its absence in controls, may be used as moderate level of evidence

**VCEP Specifications:** X-linked case counts are adopted from the Rett and Angelman-like disorders VCEP (PMID: 34837432). PS4 can be used to count cases for both affected males (XY) and females (XX). **Females must meet PP4 to be counted towards PS4.**

| Strength | Case Count |
|----------|------------|
| **Strong (PS4)** | 5+ cases |
| **Moderate (PS4_Moderate)** | 3-4 cases |
| **Supporting (PS4_Supporting)** | 2 cases |

---

### PM1 - Mutational Hot Spot

**Original ACMG Summary:** Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.

**VCEP Specifications:** *Not Applicable*

**Comments:** There are no defined hotspots or critical functional domains in MTM1 at this time.

---

### PM2 - Absent from Controls

**Original ACMG Summary:** Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

**Caveat:** Population data for indels may be poorly called by next generation sequencing.

**VCEP Specification (Supporting only):**

| Strength | Criteria |
|----------|----------|
| **Supporting** | PM2_Supporting may be applied if the minor allele frequency in population databases of at least 2000 alleles is **absent** (1 observation allowed in females only) |

---

### PM3 - In Trans with Pathogenic

**Original ACMG Summary:** For recessive disorders, detected in trans with a pathogenic variant.

**Note:** This requires testing of parents (or offspring) to determine phase.

**VCEP Specifications:** *Not Applicable*

**Comments:** Biallelic case counts should not be used for MTM1 (X-linked inheritance).

---

### PM4 - Protein Length Changes

**Original ACMG Summary:** Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

**VCEP Specifications:** No change - use as originally described.

| Strength | Criteria |
|----------|----------|
| **Strong** | No change - use as originally described |
| **Moderate** | Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants |
| **Supporting** | No change - use as originally described |

---

### PM5 - Novel Missense at Same Residue

**Original ACMG Summary:** Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.

**Example:** Arg156His is pathogenic; now you observe Arg156Cys.

**Caveat:** Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:** No change - use as originally described.

| Strength | Criteria |
|----------|----------|
| **Strong** | No change - use as originally described |
| **Moderate** | Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before |
| **Supporting** | No change - use as originally described |

---

### PM6 - De Novo (Assumed)

**Original ACMG Summary:** Assumed de novo, but without confirmation of paternity and maternity.

**VCEP Specifications:** No change - use as originally described.

| Strength | Criteria |
|----------|----------|
| **Strong** | No change - use as originally described |
| **Moderate** | Assumed de novo, but without confirmation of paternity and maternity |
| **Supporting** | No change - use as originally described |

---

### PP1 - Co-segregation

**Original ACMG Summary:** Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.

**Note:** May be used as stronger evidence with increasing segregation data.

**VCEP Specifications:** X-linked segregation counts adopted from the Rett and Angelman-like disorders VCEP (PMID: 34837432)

| Strength | Segregation Count |
|----------|-------------------|
| **Strong (PP1_Strong)** | At least 5 segregations |
| **Moderate (PP1_Moderate)** | 3-4 segregations |
| **Supporting (PP1)** | 2 segregations |

---

### PP2 - Missense in Constrained Gene

**Original ACMG Summary:** Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.

**VCEP Specifications:** *Not Applicable*

**Comments:** MTM1 is not a gene that is constrained for missense variation. Hence PP2 is not applicable.

---

### PP3 - Computational Evidence

**Original ACMG Summary:** Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).

**Caveat:** As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Supporting** | PP3 is met if **REVEL score >= 0.7** OR if the variant is predicted to impact splicing using **SpliceAI score >= 0.5** |

---

### PP4 - Phenotype Specificity

**Original ACMG Summary:** Patient's phenotype or family history is highly specific for a disease with a single genetic etiology.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Supporting** | See criteria below for affected males and carrier females |

#### PP4 Criteria for Affected Males

Must be **negative for BIN1, RYR1, and DNM2 variants** AND have:

- Muscle biopsy with rounded muscle fibers with a single centrally located nucleus surrounded by a halo devoid of contractile elements, but containing mitochondria

#### PP4 Criteria for Carrier Females

Must have a **panel test for neuromuscular disease to rule out other causes** AND:

- Observation of myopathy (may be asymmetric) AND at least 1 other feature:
  - Unilateral skeletal asymmetry
  - Narrow, elongated face
  - High arched palate

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

| Strength | Criteria |
|----------|----------|
| **Stand Alone** | The minor allele frequency using the filtering allele frequency of either exomes or genomes in gnomAD is **>= 0.000016** (0.0016%). All continental gnomAD populations used should have at least 2000 alleles and >1 observation. |

---

### BS1 - Frequency Greater Than Expected

**Original ACMG Summary:** Allele frequency is greater than expected for disorder.

**VCEP Specification (Strong):**

| Strength | Criteria |
|----------|----------|
| **Strong** | The minor allele frequency using the filtering allele frequency of either exomes or genomes in gnomAD is **>= 0.0000016** (0.00016%). All continental gnomAD populations used should have at least 2000 alleles and >1 observation. |

---

### BS2 - Observed in Healthy Adult

**Original ACMG Summary:** Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

**VCEP Specifications:** No change - use as originally described.

| Strength | Criteria |
|----------|----------|
| **Strong** | Observed in a healthy adult individual for an X-linked (hemizygous) disorder, with full penetrance expected at an early age |
| **Moderate** | No change - use as originally described |
| **Supporting** | No change - use as originally described |

---

### BS3 - Functional Studies (No Effect)

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

**VCEP Specifications:** *Not Applicable*

**Comments:** The VCEP has decided that lack of demonstrated effect in a functional assay should not count against the pathogenicity of an MTM1 variant because of the numerous possible functions of myotubularin; therefore all specified functional assays will only be used as evidence for pathogenicity.

---

### BS4 - Lack of Segregation

**Original ACMG Summary:** Lack of segregation in affected members of a family.

**Caveat:** The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.

**VCEP Specifications:** No change - use as originally described.

| Strength | Criteria |
|----------|----------|
| **Strong** | Lack of segregation in affected members of a family |
| **Moderate** | No change - use as originally described |
| **Supporting** | No change - use as originally described |

---

### BP1-BP7 - Benign Supporting

| Criterion | Status | Comment |
|-----------|--------|---------|
| **BP1** | *Not Applicable* | Both missense and truncating variants in MTM1 are disease-causing |
| **BP2** | Applicable | Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder or observed in cis with a pathogenic variant in any inheritance pattern. No change - use as originally described. |
| **BP3** | *Not Applicable* | There are no regions in MTM1 where BP3 would apply |
| **BP4** | Applicable | BP4 is met if **REVEL score <= 0.15** OR if the variant is **not predicted to impact splicing using SpliceAI** |
| **BP5** | Applicable | Variant found in a case with an alternate molecular basis for disease. No change - use as originally described. |
| **BP6** | *Not Applicable* | This criterion is not for use as recommended by the ClinGen SVI VCEP Review Committee (PMID: 29543229) |
| **BP7** | Applicable | A synonymous variant for which **SpliceAI** predicts no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved |

---

## Rules for Combining Criteria

### Pathogenic Classification

| Criteria Combination |
|---------------------|
| 1 Very Strong (PVS1, PS2_VeryStrong) **AND** >= 1 Strong (PS1, PS2, PS3, PS4, PM4_Strong, PM5_Strong, PM6_Strong, PP1_Strong) |
| 1 Very Strong **AND** >= 2 Moderate (PS1_Moderate, PS2_Moderate, PS3_Moderate, PS4_Moderate, PM4, PM5, PM6, PP1_Moderate) |
| 1 Very Strong **AND** 1 Moderate **AND** 1 Supporting (PS1_Supporting, PS2_Supporting, PS3_Supporting, PS4_Supporting, PM2_Supporting, PM4_Supporting, PM5_Supporting, PM6_Supporting, PP1, PP3, PP4) |
| 1 Very Strong **AND** >= 2 Supporting |
| >= 2 Strong |
| 1 Strong **AND** >= 3 Moderate |
| 1 Strong **AND** 2 Moderate **AND** >= 2 Supporting |
| 1 Strong **AND** 1 Moderate **AND** >= 4 Supporting |

### Likely Pathogenic Classification

| Criteria Combination |
|---------------------|
| 1 Very Strong **AND** 1 Moderate |
| 1 Strong **AND** 1 Moderate |
| 1 Strong **AND** >= 2 Supporting |
| >= 3 Moderate |
| 2 Moderate **AND** >= 2 Supporting |
| 1 Moderate **AND** >= 4 Supporting |
| 1 Strong **AND** 2 Moderate |

### Benign Classification

| Criteria Combination |
|---------------------|
| >= 2 Strong (BS1, BS2, BS4, BP2_Strong, BP5_Strong) |
| 1 Stand Alone (BA1) |

### Likely Benign Classification

| Criteria Combination |
|---------------------|
| 1 Strong (BS1, BS2, BS4, BP2_Strong, BP5_Strong) **AND** 1 Supporting (BS2_Supporting, BS4_Supporting, BP2, BP4, BP5, BP7) |
| >= 2 Supporting (BS2_Supporting, BS4_Supporting, BP2, BP4, BP5, BP7) |

---

## Appendices

### Appendix A: Population Frequency Thresholds Summary

| Criterion | Threshold | Strength |
|-----------|-----------|----------|
| BA1 | >= 0.000016 (0.0016%) | Stand Alone |
| BS1 | >= 0.0000016 (0.00016%) | Strong |
| PM2 | Absent (1 observation allowed in females only) | Supporting |

**Note:** All thresholds use gnomAD filtering allele frequency from exomes or genomes. All continental gnomAD populations used should have at least 2000 alleles and >1 observation.

### Appendix B: Computational Prediction Thresholds

| Criterion | Tool | Threshold | Interpretation |
|-----------|------|-----------|----------------|
| PP3 | REVEL | >= 0.7 | Supports pathogenicity |
| PP3 | SpliceAI | >= 0.5 | Supports splicing impact |
| BP4 | REVEL | <= 0.15 | Supports benign |
| BP4 | SpliceAI | No impact predicted | Supports benign |

### Appendix C: Approved Functional Assays Summary

| Assay Category | Assay Type | Abnormal Readout | Strength |
|----------------|------------|------------------|----------|
| Phosphatase Activity | In vitro phosphatase assay | Reduced phosphatase activity; increased PtdIns/PtdIns(3,5)P levels | PS3_Supporting |
| Myotubularin Localization | Immunofluorescence | Altered localization (spots/aggregates/extensions) | PS3_Supporting |
| Myotubularin Translocation | EGF stimulation assay | Loss of MTM1 recruitment to late endosomes | PS3_Supporting |
| Intracellular Trafficking | EGFR/TfR trafficking | Reduced receptor trafficking | PS3_Supporting |
| Protein Association | Co-IP with BIN1 | Reduced binding to BIN1 | PS3_Supporting |
| Protein Association | Co-IP with Desmin | Reduced binding to Desmin | PS3_Supporting |
| Protein Association | Co-IP with hVPS34 | Reduced binding to hVPS34-PI 3-Kinase | PS3_Supporting |
| Protein Association | Co-IP with MTMR12 | Reduced binding to MTMR12 | PS3_Supporting |
| Lipid Association | Phosphoinositide binding | Reduced phosphoinositide binding | PS3_Supporting |
| Lipid Association | EEA1/2xFYVE membrane | No decrease in PI(3)P levels | PS3_Supporting |
| Mouse Model | Variant-specific mouse model | Disease phenotype recapitulated | PS3_Strong |

**Note:** Myotubularin Localization and Myotubularin Translocation assays should NOT be stacked.

### Appendix D: Reference PMIDs

| PMID | Citation |
|------|----------|
| 23917616 | Royer B, Hnia K et al. The myotubularin-amphiphysin 2 complex in membrane tubulation and centronuclear myopathies. EMBO Rep (2013) 14(10):907-15 |
| 21135508 | Hnia K, Tronchère H et al. Myotubularin controls desmin intermediate filament architecture and mitochondrial dynamics in human and mouse skeletal muscle. J Clin Invest (2011) 121(1):70-85 |
| 17651088 | Cao C, Laporte J et al. Myotubularin lipid phosphatase binds the hVPS15/hVPS34 lipid kinase complex on endosomes. Traffic (2007) 8(8):1052-67 |
| 14722070 | Tsujita K, Itoh T et al. Myotubularin regulates the function of the late endosome through the gram domain-phosphatidylinositol 3,5-bisphosphate interaction. J Biol Chem (2004) 279(14):13817-24 |
| 26760201 | Ketel K, Krauss M et al. A phosphoinositide conversion mechanism for exit from endosomes. Nature (2016) 529(7586):408-12 |
| 23818870 | Gupta VA, Hnia K et al. Loss of catalytically inactive lipid phosphatase myotubularin-related protein 12 impairs myotubularin stability and promotes centronuclear myopathy in zebrafish. PLoS Genet (2013) 9(6):e1003583 |
| 12118066 | Laporte J, Blondeau F et al. The PtdIns3P phosphatase myotubularin is a cytoplasmic protein that also localizes to Rac1-inducible plasma membrane ruffles. J Cell Sci (2002) 115(Pt 15):3105-17 |
| 20682747 | Beggs AH, Böhm J et al. MTM1 mutation associated with X-linked myotubular myopathy in Labrador Retrievers. Proc Natl Acad Sci USA (2010) 107(33):14697-702 |
| 10900271 | Taylor GS, Maehama T et al. Myotubularin, a protein tyrosine phosphatase mutated in myotubular myopathy, dephosphorylates the lipid second messenger, phosphatidylinositol 3-phosphate. Proc Natl Acad Sci USA (2000) 97(16):8910-5 |
| 14660569 | Tronchère H, Laporte J et al. Production of phosphatidylinositol 5-phosphate by the phosphoinositide 3-phosphatase myotubularin in mammalian cells. J Biol Chem (2004) 279(8):7304-12 |
| 12646134 | Schaletzky J, Dove SK et al. Phosphatidylinositol-5-phosphate activation and conserved substrate specificity of the myotubularin phosphatidylinositol 3-phosphatases. Curr Biol (2003) 13(6):504-9 |
| 23071445 | Amoasii L, Bertazzi DL et al. Phosphatase-dead myotubularin ameliorates X-linked centronuclear myopathy phenotypes in mice. PLoS Genet (2012) 8(10):e1002965 |
| 22068590 | Pierson CR, Dulin-Smith AN et al. Modeling the human MTM1 p.R69C mutation in murine Mtm1 results in exon 4 skipping and a less severe myotubular myopathy phenotype. Hum Mol Genet (2012) 21(4):811-25 |
| 34837432 | McKnight D, Bean L et al. Recommendations by the ClinGen Rett/Angelman-like expert panel for gene-specific variant interpretation methods. Hum Mutat (2022) 43(8):1097-1113 |
| 29543229 | ClinGen Sequence Variant Interpretation Working Group. Recommendations for interpreting the loss of function PVS1 ACMG/AMP variant criterion. Hum Mutat (2018) 39(11):1517-1524 |

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 8/7/2024 | Initial release |

---

*This document was compiled from ClinGen VCEP specifications and ClinGen SVI recommendations. For the most current version, please refer to the ClinGen website.*
