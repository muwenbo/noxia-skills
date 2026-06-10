# ClinGen Gastric Cancer VCEP Variant Interpretation Guidelines for CDH1

**Version:** 3.1.0
**Released:** 03/29/2022
**Affiliation:** Gastric Cancer VCEP
**Expert Panel Page:** https://www.clinicalgenome.org/affiliation/50014
**Based on:** Richards et al., 2015 ACMG/AMP Guidelines
**Related Publication:** PMID 30311375

---

## Gene Information

| Attribute | Value |
|-----------|-------|
| **Gene** | CDH1 (HGNC:1748) |
| **HGNC Name** | cadherin 1 |
| **Transcript** | NM_004360.5 |
| **Disease** | Hereditary diffuse gastric cancer (MONDO:0007648) |
| **Inheritance** | Autosomal Dominant |

---

## Summary of Changes in Version 3.1

1. Specification of PM5_Supporting to nonsense and frameshift variants that are predicted/proved to undergo nonsense-mediated decay (NMD) or located upstream of the last known pathogenic truncating variant [c.2506G>T (p.Glu836Ter)].
2. Column correction for PM2_Supporting from Moderate column to Supporting column.

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

**VCEP Specifications:** RNA analysis is recommended for splicing alterations, and if the RNA evidence does not support the prediction, the strength should be updated.

#### Strength Levels

| Strength | Criteria |
|----------|----------|
| **Very Strong** | Per modified CDH1 PVS1 decision tree. |
| **Strong** | Per modified CDH1 PVS1 decision tree. **Additional CDH1 caveats:** Use PVS1_Strong as the default strength of evidence for canonical splice site variants and follow the site-specific recommendations in the splicing table. CDH1 exonic deletions or tandem duplications of in-frame exons (exons 4, 5, 8, 9, 12, 13, 15). |
| **Moderate** | Per modified CDH1 PVS1 decision tree. **Additional CDH1 caveats:** G to non-G variants disrupting the last nucleotide of an exon. Canonical splice sites predicted or demonstrated experimentally to result in in-frame partial skipping/insertion (e.g., Exon 3 donor site). |
| **Supporting** | Not applicable. |

---

### PS1 - Same Amino Acid Change

**Original ACMG Summary:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.

**VCEP Specifications:** Not applicable for CDH1.

---

### PS2 - De Novo (Confirmed)

**Original ACMG Summary:** De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.

**VCEP Specifications:** Use ClinGen's de novo point system for a highly specific phenotype (see Table S2).

#### Strength Levels

| Strength | Criteria |
|----------|----------|
| **Very Strong** | >=Two patients meet the HDGC individual phenotype criteria with parental confirmation. |
| **Strong** | One patient meets the HDGC individual phenotype criteria with parental confirmation. |

#### PS2/PM6 Point System

| Phenotypic Consistency | Confirmed Parental Relationships | Unconfirmed |
|------------------------|----------------------------------|-------------|
| Phenotype highly specific for gene | 2 points | 1 point |
| Phenotype consistent but not highly specific | 1 point | 0.5 points |
| Phenotype consistent + high genetic heterogeneity | 0.5 points | 0.25 points |
| Phenotype not consistent | 0 points | 0 points |

#### Evidence Strength Thresholds

| Points | Strength Level |
|--------|----------------|
| 0.5 | Supporting |
| 1.0 | Moderate |
| 2.0 | Strong |
| 4.0 | Very Strong |

---

### PS3 - Functional Studies

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.

**VCEP Specifications:** This rule can only be applied to demonstrate splicing defects.

#### Strength Levels

| Strength | Criteria |
|----------|----------|
| **Strong** | RNA assay demonstrating abnormal out-of-frame transcripts. |
| **Moderate** | RNA assay demonstrating abnormal in-frame transcript. |

---

### PS4 - Prevalence in Affected

**Original ACMG Summary:** The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.

**VCEP Specifications:** Use the 2020 updated clinical practice guidelines (PMID: 32758476) as the HDGC phenotype criteria. PS4 cannot be applied to variants that meet BS1 or BA1, or to variants in which less than 30% of reported individuals meet HDGC criteria.

#### Strength Levels

| Strength | Criteria |
|----------|----------|
| **Very Strong** | >=Sixteen families meet HDGC criteria. |
| **Strong** | Four to fifteen families meet HDGC criteria. |
| **Moderate** | Two or three families meet HDGC criteria. |
| **Supporting** | One family meets HDGC criteria. |

---

### PM1 - Mutational Hot Spot

**Original ACMG Summary:** Located in a mutational hot spot and/or critical and well-established functional domain without benign variation.

**VCEP Specifications:** Not applicable for CDH1.

---

### PM2 - Absent from Controls

**Original ACMG Summary:** Absent from controls (or at extremely low frequency if recessive) in population databases.

**VCEP Specifications:** Use gnomAD to determine allele frequency. The mean coverage of CDH1 in the population database used should be at least 30x.

**PM2_Supporting:**
- <= 1 out of 100,000 alleles in gnomAD cohort
- If present in >=2 individuals within a subpopulation, must be present in <= 1 out of 50,000 alleles

---

### PM3 - In Trans with Pathogenic

**Original ACMG Summary:** For recessive disorders, detected in trans with a pathogenic variant.

**VCEP Specifications:** Not applicable for CDH1.

---

### PM4 - Protein Length Changes

**Original ACMG Summary:** Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

**VCEP Specifications:** PM4 is not applied to small in-frame indels because the impact of amino acid level changes of CDH1 variants is inconclusive.

#### Strength Levels

| Strength | Criteria |
|----------|----------|
| **Moderate** | Only apply to stop-loss variants. Variant example: CDH1 c.2647T>C (p.Ter883Glnext*29). |

---

### PM5 - Novel Missense at Same Residue

**Original ACMG Summary:** Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.

**VCEP Specifications:** The nonsense or frameshift variant must not impact splicing based on RNA assay or splicing predictions.

#### Strength Levels

| Strength | Criteria |
|----------|----------|
| **Supporting** | PM5_Supporting is applicable to nonsense and frameshift variants that are predicted/proved to undergo NMD or located upstream of the last known pathogenic truncating variant [c.2506G>T (p.Glu836Ter)]. Site-specific recommendations for the application of PM5_Supporting for canonical splicing variants are provided in the splicing table. |

> **Note:** PM5_Supporting can be applied to truncating variants located upstream of the last known pathogenic truncating variant [c.2506G>T (p.Glu836Ter)].

---

### PM6 - De Novo (Assumed)

**Original ACMG Summary:** Assumed de novo, but without confirmation of paternity and maternity.

**VCEP Specifications:** Use ClinGen's de novo point system for a highly specific phenotype (see Table S2). Same point system as PS2 above.

#### Strength Levels

| Strength | Criteria |
|----------|----------|
| **Very Strong** | >=Four patients meet the HDGC individual phenotype criteria without parental confirmation. |
| **Strong** | >=Two patients meet the HDGC individual phenotype criteria without parental confirmation. |
| **Moderate** | One patient meets the HDGC individual phenotype criteria without parental confirmation. |

---

### PP1 - Co-segregation

**Original ACMG Summary:** Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.

**VCEP Specifications:** Base strength of rule code on number of meioses across one or more families.

#### Strength Levels

| Strength | Criteria |
|----------|----------|
| **Strong** | >=Seven informative meioses across >=2 families. |
| **Moderate** | Five to six informative meioses across >=1 family. |
| **Supporting** | Three to four informative meioses across >=1 family. |

---

### PP2 - Missense in Constrained Gene

**Original ACMG Summary:** Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.

**VCEP Specifications:** Not applicable for CDH1.

---

### PP3 - Computational Evidence

**Original ACMG Summary:** Multiple lines of computational evidence support a deleterious effect on the gene or gene product.

**VCEP Specifications:** PP3 cannot be applied for canonical splice sites. PP3 code also does not apply to the last nucleotide of exon 3 (c.387G). Do not use protein-based computational prediction models for missense variants.

#### Strength Levels

| Strength | Criteria |
|----------|----------|
| **Moderate** | Variants affecting the same splice site as a well-characterized variant with similar or worse in silico/RNA predictions. |
| **Supporting** | At least three in silico splicing predictors in agreement (SpliceAI, MaxEntScan, SSF, GeneSplicer, HSF, TraP, varSEAK). |

---

### PP4 - Phenotype Specificity

**Original ACMG Summary:** Patient's phenotype or family history is highly specific for a disease with a single genetic etiology.

**VCEP Specifications:** Not applicable for CDH1.

---

### PP5 - Reputable Source

**Original ACMG Summary:** Reputable source recently reports variant as pathogenic, but the evidence is not available to the laboratory to perform an independent evaluation.

**VCEP Specifications:** Not applicable for CDH1. This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PMID: 29543229).

---

## Benign Criteria

### BA1 - Allele Frequency >5%

**Original ACMG Summary:** Allele frequency is above 5% in population databases.

**VCEP Specification (Stand Alone):**
- MAF cutoff of **0.2%**
- 99.99% CI; subpopulation must have >=2,000 alleles and a minimum of five variant alleles present

---

### BS1 - Frequency Greater Than Expected

**Original ACMG Summary:** Allele frequency is greater than expected for disorder.

**VCEP Specification (Strong):**
- MAF cutoff of **0.1%**
- 99.99% CI; subpopulation must have >=2,000 alleles and a minimum of five variant alleles present
- We allow a variant to reach a likely benign classification based on BS1 alone.

---

### BS2 - Observed in Healthy Adult

**Original ACMG Summary:** Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

**VCEP Specifications:** We allow a variant to reach a likely benign classification based on BS2 alone. BS2 cannot be applied to variants in which more than 30% of reported individuals meet HDGC criteria.

#### Strength Levels

| Strength | Criteria |
|----------|----------|
| **Strong** | Variant seen in >=10 individuals without GC, DGC, gSRC tumors, or LBC and whose families do not suggest HDGC. |
| **Supporting** | Variant seen in >=3 individuals without GC, DGC, SRC tumors, or LBC and whose families do not suggest HDGC. |

---

### BS3 - Functional Studies (No Effect)

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

**VCEP Specifications:** This rule can only be used to demonstrate lack of splicing and can only be applied to synonymous, intronic, or non-coding variants. BS3 may be downgraded based on quality of data.

#### Strength Levels

| Strength | Criteria |
|----------|----------|
| **Strong** | Functional RNA studies demonstrating no impact on transcript composition. |

---

### BS4 - Lack of Segregation

**Original ACMG Summary:** Lack of segregation in affected members of a family.

**VCEP Specifications:** Beware of the presence of phenocopies (e.g., breast cancer) that can mimic lack of segregation. Also, families may have more than one pathogenic variant contributing to another AD disorder.

#### Strength Levels

| Strength | Criteria |
|----------|----------|
| **Strong** | Per original ACMG/AMP guidelines. |

---

### BP1-BP7 - Benign Supporting

| Criterion | Status | Strength | Specification |
|-----------|--------|----------|---------------|
| **BP1** | Not applicable | --- | Not applicable for CDH1. |
| **BP2** | Applicable | Strong | Variant observed in trans with known pathogenic variant (phase confirmed) OR observed in the homozygous state in individual without personal and/or family history of DGC, LBC, or SRC tumors. |
| **BP2** | Applicable | Supporting | Variant is observed in cis (or phase is unknown) with a pathogenic variant OR observed in the homozygous state in gnomAD. Evidence code is dependent on the strength of data. Take consideration of the quality of sequencing data when applying code. |
| **BP3** | Not applicable | --- | Not applicable for CDH1. |
| **BP4** | Applicable | Supporting | Splicing predictions only. At least three in silico splicing predictors in agreement (SpliceAI, MaxEntScan, SSF, GeneSplicer, HSF, TraP, varSEAK). Do not use protein-based computational prediction models and BP4 is not applicable for missense variants. |
| **BP5** | Applicable | Supporting | Per original ACMG/AMP guidelines. This applies if a P/LP variant is identified in an alternate gene known to cause HDGC (currently only CTNNA1). |
| **BP6** | Not applicable | --- | Not applicable for CDH1. This criterion is not for use as recommended by the ClinGen SVI VCEP Review Committee (PMID: 29543229). |
| **BP7** | Applicable | Supporting | Synonymous and intronic variants at or beyond +7 to -21 locations. Note the CDH1 rule specification does not require a conservation prediction. We allow use of BP7 with BP4, as appropriate, to classify variants meeting both criteria as likely benign. |

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
| 1 Very Strong **AND** 1 Moderate |
| 1 Strong **AND** 1 Moderate |
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

> **CDH1-specific note:** We allow a variant to reach a likely benign classification based on BS1 alone or BS2 alone.

---

## Appendices

### Appendix A: PVS1 Decision Tree

The CDH1 VCEP uses a modified PVS1 decision tree. Key considerations:

1. **Nonsense and frameshift variants** - Follow the standard PVS1 decision tree. Consider NMD predictions and location relative to the last known pathogenic truncating variant [c.2506G>T (p.Glu836Ter)].
2. **Canonical splice site variants** - Default to PVS1_Strong and follow site-specific recommendations in the splicing table (Appendix B).
3. **Exonic deletions/tandem duplications of in-frame exons** (exons 4, 5, 8, 9, 12, 13, 15) - Apply PVS1_Strong.
4. **G to non-G variants at last nucleotide of exon** - Apply PVS1_Moderate.
5. **Canonical splice sites resulting in in-frame partial skipping/insertion** - Apply PVS1_Moderate.

---

### Appendix B: Splicing Table

Site-specific recommendations for canonical splice site variants and the application of PM5_Supporting:

| Exon | Site | Location | Prediction if Exon Skipping | RNA Assay | Curated Variants | Recommended PVS1 Strength |
|------|------|----------|----------------------------|-----------|-----------------|--------------------------|
| Exon 1 | Donor | c.48 | Likely cryptic site | | LP: c.48+1G>A | PVS1_Strong + PM5_Supporting |
| Exon 2 | Acceptor | c.49 | Frameshift | Frameshift | P: c.49-2A>G* | PVS1_Strong + PM5_Supporting |
| Exon 2 | Donor | c.163 | | | | PVS1_Strong |
| Exon 3 | Acceptor | c.164 | Frameshift | | | PVS1_Strong |
| Exon 3 | Donor | c.387 | In-frame transcripts | | VUS: c.387+1G>A* | PVS1_Moderate |
| Exon 4 | Acceptor | c.388 | In-frame deletion (aa130-177) | | | PVS1_Strong |
| Exon 4 | Donor | c.531 | | | LP: c.531+1G>A | PVS1_Strong + PM5_Supporting |
| Exon 5 | Acceptor | c.532 | In-frame deletion (aa178-229) | | LP: c.532-1G>C | PVS1_Strong + PM5_Supporting |
| Exon 5 | Donor | c.687 | | | LP: c.687+1G>A; c.687+2T>C | PVS1_Strong + PM5_Supporting |
| Exon 6 | Acceptor | c.688 | Frameshift | | | PVS1_Strong |
| Exon 6 | Donor | c.832 | | | P: c.832+1G>T; LP: c.832+1G>A | PVS1_Strong + PM5_Supporting |
| Exon 7 | Acceptor | c.833 | Frameshift | Frameshift | P: c.833-2A>G* | PVS1_Strong + PM5_Supporting |
| Exon 7 | Donor | c.1008 | Frameshift with cryptic site | | LP: c.1008+2T>C; c.1008G>A*; c.1008G>T* | PVS1_Strong + PM5_Supporting |
| Exon 8 | Acceptor | c.1009 | In-frame deletion (aa337-379) | | | PVS1_Strong |
| Exon 8 | Donor | c.1137 | Frameshift with cryptic site | | P: c.1137+1delG; c.1137G>A*; LP: c.1137+1G>A; c.1137+2T>C | PVS1_Strong + PM5_Supporting |
| Exon 9 | Acceptor | c.1138 | In-frame deletion (aa380-440) | | | PVS1_Strong |
| Exon 9 | Donor | c.1320 | In-frame deletion (exon 9 skipping) | | LP: c.1320+1G>C* | PVS1_Strong + PM5_Supporting |
| Exon 10 | Acceptor | c.1321 | Frameshift | | | PVS1_Strong |
| Exon 10 | Donor | c.1565 | | | P: c.1565+1G>C; c.1565+1G>A; c.1565+1G>T; c.1565+2dupT; LP: c.1565+1delG | PVS1_Strong + PM5_Supporting |
| Exon 11 | Acceptor | c.1566 | Frameshift | Predicted in-frame insertion with potential rescue transcript | VUS: c.1566-1G>C; c.1566-2A>G | PVS1_Moderate |
| Exon 11 | Donor | c.1711 | | | LP: c.1711+1G>C; c.1711+1G>A; c.1711+2_1711+7delTAAGGG | PVS1_Strong + PM5_Supporting |
| Exon 12 | Acceptor | c.1712 | In-frame deletion (aa571-646) | In-frame deletion (c.1712_1720del9) | VUS: c.1712-2A>C* | PVS1_Moderate |
| Exon 12 | Donor | c.1936 | | | | PVS1_Strong |
| Exon 13 | Acceptor | c.1937 | In-frame deletion (aa646-722) | | | PVS1_Strong |
| Exon 13 | Donor | c.2164 | | | VUS: c.2164+2T>C; VUS: c.2164+2dup | PVS1_Strong |
| Exon 14 | Acceptor | c.2165 | Frameshift | | LP: c.2165-1G>C | PVS1_Strong + PM5_Supporting |
| Exon 14 | Donor | c.2295 | | | | PVS1_Strong |
| Exon 15 | Acceptor | c.2296 | In-frame deletion (aa766-813) | | LP: c.2296-1G>A; c.2296-2A>G | PVS1_Strong + PM5_Supporting |
| Exon 15 | Donor | c.2439 | | | | PVS1_Strong |
| Exon 16 | Acceptor | c.2440 | Likely cryptic site | Abnormal splicing | LP: c.2440-2A>G* | PVS1_Strong + PM5_Supporting |

\* RNA functional assay performed.

---

### Appendix C: PM5_Supporting Application to Nonsense/Frameshift Variants

PM5_Supporting can be applied to truncating variants located upstream of the last known pathogenic truncating variant [c.2506G>T (p.Glu836Ter)].

| Exon | Location | Curated Nonsense/Frameshift Variants (N=113) |
|------|----------|----------------------------------------------|
| Exon 1 | c.1-c.48 | **P (1):** c.26C>A (p.Ser9Ter). **LP (2):** c.11G>A (p.Trp4Ter); c.12G>A (p.Trp4Ter) |
| Exon 2 | c.49-c.163 | **P (4):** c.59G>A (p.Trp20Ter); c.60G>A (p.Trp20Ter); c.70G>T (p.Glu24Ter); c.124_126delCCCinsT (p.Pro42Serfs). **LP (1):** c.76G>T (p.Glu26Ter) |
| Exon 3 | c.164-c.387 | **P (8):** c.187C>T (p.Arg63Ter); c.208dup (p.Ser70Phefs); c.220C>T (p.Arg74Ter); c.283C>T (p.Gln95Ter); c.308G>A (p.Trp103Ter); c.360dup (p.His121fs); c.377del (p.Pro126Argfs); c.382delC (p.His128Ilefs). **LP (5):** c.202delT (p.Tyr68Ilefs); c.261delG (p.Arg87Serfs); c.315delC (p.Thr106Profs); c.337A>T (p.Lys113Ter); c.369_375CCGCCCC[3] (p.His128fs) |
| Exon 4 | c.388-c.531 | **P (6):** c.454_460delCAGAAGA (p.Gln152Glufs); c.480_486delinsAGAATA (p.Ile161fs); c.489C>A (p.Cys163Ter); c.521dupA (p.Asn174Lysfs); c.504delA (p.Gly169Alafs); c.529C>T (p.Gln177Ter). **LP (7):** c.436_437TC[1] (p.Pro147fs); c.454_460dup (p.Arg154Thrfs); c.455_465delAGAAGAGAGAC (p.Gln152Leufs); c.457_460delAAGA (p.Lys153Glufs); c.457A>T (p.Lys153Ter); c.467G>A (p.Trp156Ter); c.468G>A (p.Trp156Ter) |
| Exon 5 | c.532-c.687 | **P (2):** c.603delT (p.Val202Leufs); c.656del (p.Pro219fs). **LP (1):** c.594_595insT (p.Thr199fs) |
| Exon 6 | c.688-c.832 | **P (1):** c.720del (p.Asn240fs). **LP (4):** c.692_693TC[2] (p.His233fs); c.707C>A (p.Ser236Ter); c.781G>T (p.Glu261Ter); c.793G>T (p.Glu265Ter) |
| Exon 7 | c.833-c.1008 | **P (2):** c.940A>T (p.Lys314Ter); c.1003C>T (p.Arg335Ter) |
| Exon 8 | c.1009-c.1137 | **P (7):** c.1009_1010delAG (p.Ser337Phefs); c.1023T>G (p.Tyr341Ter); c.1051C>T (p.Gln351Ter); c.1064delT (p.Leu355Terfs); c.1085delT (p.Val362Glyfs); c.1107del (p.Asn369Lysfs); c.1131del (p.Thr378fs). **LP (1):** c.1031_1032dup (p.Val345fs) |
| Exon 9 | c.1138-c.1320 | **P (2):** c.1147C>T (p.Gln383Ter); c.1235_1236TA[3] (p.Ile415fs). **LP (2):** c.1170del (p.Asn390fs); c.1312del (p.Thr438fs) |
| Exon 10 | c.1321-c.1565 | **P (4):** c.1408del (p.Thr470fs); c.1476_1477delAG (p.Arg492Serfs); c.1488_1494delCGAGGAC (p.Glu497Leufs); c.1531C>T (p.Gln511Ter). **LP (7):** c.1341del (p.Lys447fs); c.1354_1357del (p.Leu452fs); c.1390del (p.Val464fs); c.1443del (p.Asn481fs); c.1460_1461del (p.Val487Alafs); c.1480G>T (p.Glu494Ter); c.1505delG (p.Gly502Alafs) |
| Exon 11 | c.1566-c.1711 | **P (4):** c.1578G>A (p.Trp526Ter); c.1587dup (p.Ala530fs); c.1590dup (p.Asn531fs); c.1612delG (p.Asp538Thrfs). **LP (3):** c.1569T>A (p.Tyr523Ter); c.1636delG (p.Ala546Leufs); c.1679dup (p.Tyr561Valfs) |
| Exon 12 | c.1712-c.1936 | **P (6):** c.1733dup (p.Gly579fs); c.1779dup (p.Ile594fs); c.1792C>T (p.Arg598Ter); c.1895_1896delAC (p.His632Argfs); c.1913G>A (p.Trp638Ter); c.1921C>T (p.Gln641Ter). **LP (2):** c.1746dup (p.Leu583Alafs); c.1917_1918del (p.Ile640fs) |
| Exon 13 | c.1937-c.2164 | **P (5):** c.1979dup (p.Gly661_Asp662insTer); c.1999del (p.Leu667fs); c.2062_2063TG[1] (p.Cys688_Glu689delinsTer); c.2095C>T (p.Gln699Ter); c.2100del (p.Val701Serfs). **LP (8):** c.1942G>T (p.Glu648Ter); c.1948_1949del (p.Ile650HisfsTer12); c.1948_1949dup (p.Ile651Serfs); c.1993del (p.Ile665Serfs); c.2029dup (p.Gln677Profs); c.2076_2077del (p.Gly693ArgfsTer3); c.2104G>T (p.Glu702Ter); c.2144delG (p.Gly715Glufs) |
| Exon 14 | c.2165-c.2295 | **P (4):** c.2265T>A (p.Tyr755Ter); c.2276delG (p.Gly759Glufs); c.2287G>T (p.Glu763Ter); c.2293C>T (p.Gln765Ter). **LP (1):** c.2272G>T (p.Glu758Ter) |
| Exon 15 | c.2296-c.2439 | **P (2):** c.2398delC (p.Arg800Alafs); c.2430delT (p.Phe810Leufs). **LP (3):** c.2311C>T (p.Gln771Ter); c.2324delG (p.Gly775Alafs); c.2386dup (p.Arg796Profs) |
| Exon 16 | c.2440-c.2649 | **P (1):** c.2506G>T (p.Glu836Ter). **LP (2):** c.2446A>T (p.Lys816Ter); c.2490dup (p.Leu831Alafs). **VUS (5):** c.2505_2506dup (p.Glu836fs); c.2526delT (p.Ala843Leufs); c.2547_2548insA (p.Ser850fs); c.2549_2550delCC (p.Ser850Phefs); c.2594G>A (p.Trp865Ter) |

---

### Appendix D: 2020 HDGC Genetic Testing Criteria

**Family criteria** (family members are first-degree or second-degree blood relatives of each other):

1. >=2 cases of gastric cancer in family regardless of age, with at least one DGC
2. >=1 case of DGC at any age in family, and >=1 case of LBC at age <70 years, in different family members
3. >=2 cases of LBC in family members <50 years of age

**Individual criteria:**

4. DGC at age <50 years
5. DGC at any age in individuals of Maori ethnicity
6. DGC at any age in individuals with a personal or family history (first-degree relative) of cleft lip or cleft palate
7. History of DGC and LBC, both diagnosed <70 years
8. Bilateral LBC, diagnosed at age <70 years
9. Gastric in situ signet ring cells (SRC) or pagetoid spread of SRCs in individuals <50 years of age

Reference: PMID 32758476

---

### Appendix E: Population Frequency Thresholds Summary

| Criterion | Threshold | Strength |
|-----------|-----------|----------|
| BA1 | >0.2% | Stand Alone |
| BS1 | >0.1% | Strong |
| PM2 | <=0.001% (1/100,000) | Supporting |

---

### Appendix F: Criteria Applicability Summary

| Criterion | Applicable | Max Strength | Notes |
|-----------|------------|-------------|-------|
| PVS1 | Yes | Very Strong | Per modified CDH1 PVS1 decision tree |
| PS1 | **No** | --- | Not applicable for CDH1 |
| PS2 | Yes | Very Strong | ClinGen de novo point system |
| PS3 | Yes | Strong | Splicing defects only (RNA assay) |
| PS4 | Yes | Very Strong | HDGC phenotype criteria (PMID: 32758476) |
| PM1 | **No** | --- | Not applicable for CDH1 |
| PM2 | Yes | Supporting only | gnomAD <=1/100,000 |
| PM3 | **No** | --- | Not applicable (not recessive) |
| PM4 | Yes | Moderate | Stop-loss variants only |
| PM5 | Yes | Supporting only | Truncating variants upstream of last known P truncation |
| PM6 | Yes | Very Strong | ClinGen de novo point system |
| PP1 | Yes | Strong | Based on informative meioses |
| PP2 | **No** | --- | Not applicable for CDH1 |
| PP3 | Yes | Moderate | Splicing predictions only; not for canonical splice sites |
| PP4 | **No** | --- | Not applicable for CDH1 |
| PP5 | **No** | --- | Not for use per ClinGen SVI |
| BA1 | Yes | Stand Alone | MAF >0.2% |
| BS1 | Yes | Strong | MAF >0.1%; can reach LB alone |
| BS2 | Yes | Strong | >=10 individuals without HDGC phenotype |
| BS3 | Yes | Strong | RNA studies; synonymous/intronic/non-coding only |
| BS4 | Yes | Strong | Per original ACMG/AMP; beware phenocopies |
| BP1 | **No** | --- | Not applicable for CDH1 |
| BP2 | Yes | Strong | In trans with P/LP or homozygous without HDGC |
| BP3 | **No** | --- | Not applicable for CDH1 |
| BP4 | Yes | Supporting | Splicing predictions only; not for missense |
| BP5 | Yes | Supporting | Alternate gene = CTNNA1 |
| BP6 | **No** | --- | Not for use per ClinGen SVI |
| BP7 | Yes | Supporting | Synonymous/intronic at >=+7 or <=-21 |

---

### Appendix G: Reference PMIDs

| PMID | Description |
|------|-------------|
| 30311375 | CDH1 VCEP publication |
| 32758476 | 2020 updated HDGC clinical practice guidelines |
| 29543229 | ClinGen SVI recommendations on PP5/BP6 |

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 3.1.0 | 03/29/2022 | (1) Specification of PM5_Supporting for nonsense/frameshift variants predicted/proved to undergo NMD or upstream of last known pathogenic truncating variant. (2) Column correction for PM2_Supporting. |

---

*This document was compiled from ClinGen VCEP specifications (Gastric Cancer VCEP, Affiliation 50014). For the most current version, please refer to the [ClinGen website](https://www.clinicalgenome.org/affiliation/50014/docs/assertion-criteria).*
