# ClinGen PTEN Expert Panel Variant Interpretation Guidelines for PTEN

**Version:** 3.1.0
**Released:** 3/14/2024
**Affiliation:** PTEN VCEP
**Based on:** Richards et al., 2015 ACMG/AMP Guidelines

---

## Gene Information

| Attribute | Value |
|-----------|-------|
| **Gene** | PTEN (HGNC:9588) |
| **HGNC Name** | phosphatase and tensin homolog |
| **Transcript** | NM_000314.8 (protein: NP_000305.3) |
| **Disease** | PTEN Hamartoma Tumor Syndrome (PHTS) |
| **Inheritance** | Autosomal Dominant |

---

## Table of Contents

1. [Pathogenic Criteria](#pathogenic-criteria)
   - [PVS1 - Null Variant](#pvs1---null-variant)
   - [PS1 - Same Amino Acid Change](#ps1---same-amino-acid-change)
   - [PS2 - De Novo (Confirmed)](#ps2---de-novo-confirmed)
   - [PS3 - Functional Studies](#ps3---functional-studies)
   - [PS4 - Prevalence in Affected / Phenotype Specificity](#ps4---prevalence-in-affected--phenotype-specificity)
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

**VCEP Specifications:**

Follow SVI guidance using PTEN-specific information per Tayoun et al. 2018 (PMID: 30192042). Use the PTEN PVS1 decision tree (see Appendix A) for all variant types.

**1. Nonsense and Frameshift Variants:**
- **PVS1** applies to variants predicted to result in nonsense-mediated decay (NMD); the predicted NMD cutoff for PTEN occurs at c.1121 (p.D375)
- For nonsense or frameshift variants at the 3' end of the gene NOT predicted to undergo NMD, PVS1 may still be applied if the protein is disrupted at or 5' to c.1121 (NM_000314.6)
- **PVS1_Moderate** applies to variants resulting in protein truncation 3' of this cutoff

**2. Splicing Variants (+/-1,2 intronic positions):**
- Only apply to variants resulting in NMD (refer to decision tree) OR entire exon deletion:
  - Exons 1, 2, 4, 5, 6, or 7 deletions OR multi-exon deletion: **PVS1** (resulting frameshift)
  - Exons 3, 8, or 9 deletions: **PVS1_Strong** (in-frame but truncated/altered region is critical to protein function)

**3. Deletion (Single/multi exon to full gene):** Refer to decision tree

**4. Duplication:** Refer to decision tree

**5. Initiation Codon:** **PVS1** applies to initiation codon variants. No known alternative start codon in other transcripts. Sufficient patient data supports pathogenicity of initiation codon variants.

#### Strength Levels

| Strength | Criteria |
|----------|----------|
| **Very Strong** | Use PTEN PVS1 decision tree |
| **Strong** | Use PTEN PVS1 decision tree |
| **Moderate** | Use PTEN PVS1 decision tree |
| **Supporting** | Not specified for PTEN |

#### PVS1 Decision Tree Summary

| Variant Type | Scenario | Strength |
|-------------|----------|----------|
| **Nonsense/Frameshift** | Predicted to undergo NMD (stop codon or disruption at or 5' to p.D375/c.1121) | PVS1 |
| **Nonsense/Frameshift** | Not predicted to undergo NMD (stop codon 3' to p.D375) and role of region in protein function is unknown | PVS1_Moderate |
| **Splice (+/-1,2)** | Exon skipping/cryptic splice disrupts reading frame and predicted to undergo NMD (disruption at or 5' to p.D375) | PVS1 |
| **Splice (+/-1,2)** | Exon skipping preserves reading frame; truncated/altered region is critical (entire exon 3, 8, or 9) | PVS1_Strong |
| **Deletion (single-multi exon)** | Single (exon 1, 2, 4, 5, 6, or 7) or multi-exon deletion disrupting reading frame and predicted to undergo NMD | PVS1 |
| **Deletion (single exon)** | Preserves reading frame; truncated/altered region is critical (entire exon 3, 8, or 9) | PVS1_Strong |
| **Full gene deletion** | Complete gene deletion | PVS1 |
| **Duplication (≥1 exon)** | Proven in tandem; reading frame disrupted and NMD predicted | PVS1 |
| **Duplication (≥1 exon)** | Presumed in tandem; reading frame presumed disrupted and NMD predicted | PVS1_Strong |
| **Duplication (≥1 exon)** | In tandem; reading frame disrupted but NMD NOT predicted (tandem duplication of exon 3 or 8) | PVS1_Strong |
| **Duplication (≥1 exon)** | Presumed in tandem; reading frame presumed disrupted but NMD NOT predicted (exon 3 or 8) | PVS1_Moderate |
| **Duplication (≥1 exon)** | Proven not in tandem / no or unknown impact on reading frame and NMD | N/A |
| **Initiation Codon** | Any initiation codon variant | PVS1 |

> **Note:** Exon must be present in biologically-relevant transcript NM_000314.8. LoF variants in the exon must not be frequent in the general population.

---

### PS1 - Same Amino Acid Change

**Original ACMG Summary:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.

**VCEP Specifications:**

PS1 will be applied as described and expanded to include a different nucleotide substitution for an intronic splice site variant if the predicted impact is equal to or greater than the known pathogenic variant per in silico splicing tools. Caution should be used when applying this criterion to exonic variants causing aberrant splicing.

| Strength | Criteria |
|----------|----------|
| **Strong** | Same amino acid change as a previously established pathogenic variant regardless of nucleotide change **OR** different variant at same nucleotide position as a pathogenic splicing variant, where in silico models predict impact equal to or greater than the known pathogenic variant |

---

### PS2 - De Novo (Confirmed)

**Original ACMG Summary:** De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.

**VCEP Specifications:**

PS2 and PM6 are combined in a counting system. Confirmed (PS2) and assumed (PM6) de novo observations are tallied together.

| Strength | Criteria |
|----------|----------|
| **Very Strong** | Two proven de novo (PS2) observations **OR** four assumed de novo (PM6) observations **OR** one proven + two assumed de novo observations in a patient with the disease and no family history |
| **Strong** | One proven de novo (both maternity and paternity confirmed) observation in a patient with the disease and no family history |

---

### PS3 - Functional Studies

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | RNA, mini-gene, or other assay demonstrating an impact on splicing |
| **Moderate** | Phosphatase activity score ≤ -1.11 per Mighell et al. 2018 (PMID: 29706350). In the supplementary material (Table S2), search for the variant in columns A or B and confirm it is listed as TRUE under column I (high confidence). The cumulative score is in column G |
| **Supporting** | Phosphatase activity <50% of wild-type or abnormal in vitro cellular assay or transgenic model with phenotype different from wild-type that does not meet PS3_Moderate |

#### Approved Functional Assays for PS3_Supporting

| Assay Type | Description | References |
|-----------|-------------|------------|
| **Phosphatase activity** | In vitro assay demonstrating >50% reduction in phosphatase activity compared to wild type. Must include catalytic dead control (e.g., p.C124S) and at least three biological replicates | Myers et al. 1998 (PMID: 9811831), Stambolic et al. 1998 (PMID: 9778245), Han et al. 2000 (PMID: 10866302), Rodriguez-Escudero et al. 2011 (PMID: 21828076), Costa et al. 2015 (PMID: 26504226), Malek et al. 2017 (PMID: 29056325) |
| **Protein expression / AKT signaling** | Decreased PTEN or increased pAKT expression | Tan 2011 (PMID: 21194675), Spinelli 2015 (PMID: 25527629) |
| **Protein localization** | Disruption of protein cellular localization | Lobo et al. 2009 (PMID: 19457929), He et al. 2012 (PMID: 22962422), Gil et al. 2015 (PMID: 25875300) |
| **Cellular phenotypes** | Aberrant cellular phenotypes including defective cell migration, proliferation, and invasion | Costa et al. 2015 (PMID: 26504226), Malek et al. 2017 (PMID: 29056325) |

---

### PS4 - Prevalence in Affected / Phenotype Specificity

**Original ACMG Summary:** The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.

**VCEP Specifications:**

**Use 1 (Case-Control):** Unlikely to be used for a condition as rare as PHTS. However, if sufficiently powered, a case-control study finding an odds ratio >2 for a PHTS component phenotype with p<0.05 and 95% confidence interval with lower limit >1.5, this criterion may be applied. **May not be applied in combination with PP4.**

**Use 2 (Phenotype Specificity):** Phenotype specificity scores are added across independent probands. **May not be applied if BS1 applies.**

**Adult Scoring (Cleveland Clinic Score, Tan 2011):**

| Feature | Score | Feature | Score |
|---------|-------|---------|-------|
| **Neurological** | | **Breast** | |
| Macrocephaly | 6 | Cancer dx <40 yrs | 4 |
| Extreme macrocephaly (men: ≥63 cm, women: ≥60 cm) | 10 | Cancer dx 40-49 yrs | 2 |
| Lhermitte-Duclos disease | 10 | Cancer dx ≥50 yrs | 1 |
| Autism/developmental delay | 1 | Fibrocystic breast disease | 1 |
| **Skin** | | **Thyroid** | |
| Trichilemmoma (biopsy-proven) | 10 | Cancer dx <20 yrs | 10 |
| Oral papillomas | 6 | Cancer dx 20-49 yrs | 4 |
| Penile freckling | 6 | Cancer dx ≥50 yrs | 1 |
| Acral keratoses | 1 | Goiter, nodules, or Hashimoto's thyroiditis | 4 |
| Lipoma | 1 | **Genitourinary** | |
| Arteriovenous malformation | 6 | Endometrial cancer dx 20-29 yrs | 6 |
| **Gastrointestinal** | | Endometrial cancer dx 30-49 yrs | 6 |
| ≥5 gastrointestinal polyps, any type | 6 | Endometrial cancer dx ≥50 yrs | 1 |
| Hamartoma or ganglioneuroma | 10 | Uterine fibroids | 1 |
| Glycogenic acanthosis | 10 | Renal cell carcinoma | 1 |

**Adult Proband Scoring:**
- **1 point** per proband with Cleveland Clinic (CC) score >30
- **0.5 points** per proband with CC score of 25-29

**Pediatric Scoring:**

| Feature | Score (points) |
|---------|---------------|
| Macrocephaly of >2 SD to <4 SD | 2 |
| Extreme macrocephaly (≥4 SD) | 3 |
| PTEN-specific MRI characteristics (dilated Virchow-Robin, prominent perivascular spaces) | 2 |
| Autism/developmental delay (DD)/intellectual disability (ID) | 2 |
| Penile freckling | 3 |
| Lipoma | 1 |
| Oral papilloma | 3 |
| Hamartomatous polyp(s) | 3 |
| Arteriovenous malformation/hemangioma | 2 |
| Thyroid cancer | 3 |
| Thyroid nodule/Hashimoto's thyroiditis | 2 |

**Pediatric Proband Scoring:**
- **1 point** per proband with pediatric phenotype score >5
- **0.5 points** per proband with pediatric phenotype score of 4, but autism/developmental delay/intellectual disability may NOT contribute to the score

#### PS4 Strength Thresholds

| Specificity Score | Strength Level |
|-------------------|----------------|
| ≥16 | PS4_Very Strong |
| 4-15.5 | PS4 (Strong) |
| 2-3.5 | PS4_Moderate |
| 1-1.5 | PS4_Supporting |

---

### PM1 - Mutational Hot Spot

**Original ACMG Summary:** Located in a mutational hot spot and/or critical and well-established functional domain without benign variation.

**VCEP Specifications:**

Defined to include residues in one of PTEN's catalytic motifs (NP_000305.3, Lee 1999):

| Motif | Residues |
|-------|----------|
| **WPD loop** | 90-94 |
| **P-loop (phosphatase core)** | 123-130 |
| **TI-loop** | 166-168 |

| Strength | Criteria |
|----------|----------|
| **Moderate** | Located in a catalytic motif: residues 90-94, 123-130, or 166-168 (NP_000305.3) |

---

### PM2 - Absent from Controls

**Original ACMG Summary:** Absent from controls (or at extremely low frequency if recessive) in population databases.

**VCEP Specification (Supporting only):**
- Variant present at **<0.00001 (0.001%)** allele frequency in gnomAD or another large sequenced population
- If multiple alleles are present within any subpopulation, allele frequency in that subpopulation must be **<0.00002 (0.002%)**

---

### PM3 - In Trans with Pathogenic

**Original ACMG Summary:** For recessive disorders, detected in trans with a pathogenic variant.

**VCEP Specifications:** **Not applicable** to PTEN (autosomal dominant disorder).

---

### PM4 - Protein Length Changes

**Original ACMG Summary:** Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

**VCEP Specifications:**

For in-frame insertions or deletions, criteria may apply only if the variant impacts at least one residue in one of the catalytic motifs specified in PM1. Criteria will also apply for variants resulting in protein extension (stop-loss).

| Strength | Criteria |
|----------|----------|
| **Moderate** | In-frame deletion/insertion impacting at least one residue in a catalytic motif (residues 90-94, 123-130, or 166-168), **OR** variants causing protein extension (stop-loss) |

---

### PM5 - Novel Missense at Same Residue

**Original ACMG Summary:** Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.

**VCEP Specifications:**

- This rule may be applied when the known variant is **pathogenic or likely pathogenic**, unless applying would lead to a higher (pathogenic) classification for the variant being assessed
- The variant in question need not be novel but must have a **BLOSUM62** (Henikoff 1992) score **equal to or less than** the known variant

| Strength | Criteria |
|----------|----------|
| **Moderate** | Missense change at an amino acid residue where a different missense change determined to be pathogenic or likely pathogenic has been seen before. The variant being interrogated must have a BLOSUM62 score equal to or less than the known variant |

#### BLOSUM62 Matrix

| | Ala | Arg | Asn | Asp | Cys | Gln | Glu | Gly | His | Ile | Leu | Lys | Met | Phe | Pro | Ser | Thr | Trp | Tyr | Val |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Ala** | 4 | | | | | | | | | | | | | | | | | | | |
| **Arg** | -1 | 5 | | | | | | | | | | | | | | | | | | |
| **Asn** | -2 | 0 | 6 | | | | | | | | | | | | | | | | | |
| **Asp** | -2 | -2 | 1 | 6 | | | | | | | | | | | | | | | | |
| **Cys** | 0 | -3 | -3 | -3 | 9 | | | | | | | | | | | | | | | |
| **Gln** | -1 | 1 | 0 | 0 | -3 | 5 | | | | | | | | | | | | | | |
| **Glu** | -1 | 0 | 0 | 2 | -4 | 2 | 5 | | | | | | | | | | | | | |
| **Gly** | 0 | -2 | 0 | -1 | -3 | -2 | -2 | 6 | | | | | | | | | | | | |
| **His** | -2 | 0 | 1 | -1 | -3 | 0 | 0 | -2 | 8 | | | | | | | | | | | |
| **Ile** | -1 | -3 | -3 | -3 | -1 | -3 | -3 | -4 | -3 | 4 | | | | | | | | | | |
| **Leu** | -1 | -2 | -3 | -4 | -1 | -2 | -3 | -4 | -3 | 2 | 4 | | | | | | | | | |
| **Lys** | -1 | 2 | 0 | -1 | -3 | 1 | 1 | -2 | -1 | -3 | -2 | 5 | | | | | | | | |
| **Met** | -1 | -1 | -2 | -3 | -1 | 0 | -2 | -3 | -2 | 1 | 2 | -1 | 5 | | | | | | | |
| **Phe** | -2 | -3 | -3 | -3 | -2 | -3 | -3 | -3 | -1 | 0 | 0 | -3 | 0 | 6 | | | | | | |
| **Pro** | -1 | -2 | -2 | -1 | -3 | -1 | -1 | -2 | -2 | -3 | -3 | -1 | -2 | -4 | 7 | | | | | |
| **Ser** | 1 | -1 | 1 | 0 | -1 | 0 | 0 | 0 | -1 | -2 | -2 | 0 | -1 | -2 | -1 | 4 | | | | |
| **Thr** | 0 | -1 | 0 | -1 | -1 | -1 | -1 | -2 | -2 | -1 | -1 | -1 | -1 | -2 | -1 | 1 | 5 | | | |
| **Trp** | -3 | -3 | -4 | -4 | -2 | -2 | -3 | -2 | -2 | -3 | -2 | -3 | -1 | 1 | -4 | -3 | -2 | 11 | | |
| **Tyr** | -2 | -2 | -2 | -3 | -2 | -1 | -2 | -3 | 2 | -1 | -1 | -2 | -1 | 3 | -3 | -2 | -2 | 2 | 7 | |
| **Val** | 0 | -3 | -3 | -3 | -1 | -2 | -2 | -3 | -3 | 3 | 1 | -2 | 1 | -1 | -2 | -2 | 0 | -3 | -1 | 4 |

---

### PM6 - De Novo (Assumed)

**Original ACMG Summary:** Assumed de novo, but without confirmation of paternity and maternity.

**VCEP Specifications:**

PM6 is combined with PS2 in a counting system (see PS2 section above for Very Strong thresholds).

| Strength | Criteria |
|----------|----------|
| **Very Strong** | Four or more occurrences of PM6 **OR** two occurrences of PM6 AND one occurrence of PS2 |
| **Strong** | Two occurrences of PM6 **OR** one occurrence of PM6 for an individual with a highly specific phenotype (meets criteria to count towards PS4). Note: when PM6_Strong is applied for a single individual with phenotype specificity, the individual will NOT be counted towards PS4 as well |
| **Moderate** | Assumed de novo, without confirmation of paternity and maternity, in a proband with the disease and no family history |

---

### PP1 - Co-segregation

**Original ACMG Summary:** Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.

**VCEP Specifications:**

| Strength | Meioses Required | Additional Requirements |
|----------|-----------------|------------------------|
| **Supporting** | 3 or 4 meioses | — |
| **Moderate** | 5 or 6 meioses | — |
| **Strong** | ≥7 meioses | Across at least two families |

---

### PP2 - Missense in Constrained Gene

**Original ACMG Summary:** Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Supporting** | Missense variant in PTEN (gene has a low rate of benign missense variation and missense variants are a common mechanism of disease). Applied per original ACMG guidelines, no modification |

---

### PP3 - Computational Evidence

**Original ACMG Summary:** Multiple lines of computational evidence support a deleterious effect on the gene or gene product.

**VCEP Specifications:**

| Variant Type | Tool(s) | Thresholds |
|-------------|---------|------------|
| **Synonymous or intronic variants** | SpliceAI **AND** VarSeak | SpliceAI: scores 0.5-1 are considered evidence of pathogenic. VarSeak: Class 4 and 5 are considered evidence of pathogenic. Both tools must agree (concordance) |
| **Missense variants** | REVEL | Score **> 0.7** |

> **Commentary:** Per Bayesian adaptation (Tavtigian et al., 2018), REVEL scores >0.7 equated with moderate evidence strength for pathogenicity. However, since the VCEP also applies PP2 for missense variants, evidence strength was downgraded to supporting level.

---

### PP4 - Phenotype Specificity

**Original ACMG Summary:** Patient's phenotype or family history is highly specific for a disease with a single genetic etiology.

**VCEP Specifications:** **Not applicable.** Phenotype specificity has been incorporated into the rule specifications for PS4 Use 2. See PS4 section.

---

### PP5 - Reputable Source

**Original ACMG Summary:** Reputable source recently reports variant as pathogenic, but the evidence is not available to the laboratory to perform an independent evaluation.

**VCEP Specifications:** **Not applicable.** This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PMID: 29543229).

---

## Benign Criteria

### BA1 - Allele Frequency >5%

**Original ACMG Summary:** Allele frequency is above 5% in population databases.

**VCEP Specification (Stand Alone):**
- gnomAD filtering allele frequency **>0.00056 (0.056%)**

> **Note:** BA1 threshold calculated using Whiffin et al. (PMID: 28518168) approach with allelic heterogeneity set to 1, using prevalence of 1/9,000 and 10% penetrance.

---

### BS1 - Frequency Greater Than Expected

**Original ACMG Summary:** Allele frequency is greater than expected for disorder.

**VCEP Specifications:**

Based on the Whiffin et al. (PMID: 28518168) approach using:
- **Prevalence:** 1 in 9,000 (based on 15 disease-associated alleles among ~135,000 gnomAD individuals)
- **Allelic heterogeneity:** 22/282 (based on prevalence of most common pathogenic PTEN variants, p.R130X and p.R335X, per Tan et al. PMID: 21194675 and Bubien 2013 PMID: 23335809)
- **Penetrance:** 10% (overall cancer by age 40 for men ≈20% per Bubien 2013)

| Strength | gnomAD Filtering Allele Frequency |
|----------|----------------------------------|
| **Strong** | 0.000043 (0.0043%) up to 0.00056 (0.056%) |
| **Supporting** | 0.0000043 (0.00043%) up to 0.000043 (0.0043%) |

---

### BS2 - Observed in Healthy Adult

**Original ACMG Summary:** Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | Variant observed in the **homozygous state** in a healthy or PHTS-unaffected individual. One observation if homozygous status is confirmed via parental testing; two independent observations if not confirmed. If BS1 is also applied, downgrade to Supporting level to avoid a variant reaching benign status solely based on homozygous occurrences due to high population frequency |
| **Supporting** | Two homozygous observations with no clinical data provided, **OR** meets criteria for BS2 but BS1 is also applied |

---

### BS3 - Functional Studies (No Effect)

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | For intronic or synonymous variants: RNA, mini-gene, or other assay demonstrates **no impact on splicing** |
| **Supporting** | In vitro or in vivo functional study showing no damaging effect on protein function |

#### Approved Assays for BS3_Supporting

| Assay | Criteria | References |
|-------|----------|------------|
| **Mighell et al. 2018 massively parallel functional assay** | In Table S2, variant must be TRUE under column I (high confidence). Apply BS3_Supporting for variants with cumulative score (column G) **> 0** | PMID: 29706350 |
| **Phosphatase assays** | Lipid phosphatase activity comparable to wild type **PLUS** a second assay appropriate to the protein domain demonstrating no statistically significant difference from wild type. Phosphatase assays must include catalytic dead control (p.C124S, NP_000305.3) and at least three biological replicates | Myers et al. 1998 (PMID: 9811831), Stambolic et al. 1998 (PMID: 9778245), Han et al. 2000 (PMID: 10866302), Rodriguez-Escudero et al. 2011 (PMID: 21828076), Costa et al. 2015 (PMID: 26504226), Malek et al. 2017 (PMID: 29056325) |

**Examples of second assays for BS3_Supporting:**
- PTEN/pAKT expression: Tan et al. 2011 (PMID: 21194675), Spinelli et al. 2015 (PMID: 25527629)
- Protein cellular localization: Lobo et al. 2009 (PMID: 19457929), He et al. 2012 (PMID: 22962422), Gil et al. 2015 (PMID: 25875300)
- Cellular phenotypes (migration, proliferation, invasion): Costa et al. 2015 (PMID: 26504226), Malek et al. 2017 (PMID: 29056325)

---

### BS4 - Lack of Segregation

**Original ACMG Summary:** Lack of segregation in affected members of a family.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | Lack of segregation in affected members of **two or more families** |
| **Supporting** | Lack of segregation in affected members of **one family** |

---

### BP1-BP7 - Benign Supporting

| Criterion | Status | Specification |
|-----------|--------|---------------|
| **BP1** | **Not Applicable** | This rule is not applicable to PTEN (missense variants are a known mechanism of disease) |
| **BP2** | **Applicable (Supporting)** | Observed in trans with a pathogenic or likely pathogenic PTEN variant **OR** at least three observations in cis and/or phase unknown with different pathogenic/likely pathogenic PTEN variants. The other variant may be either pathogenic or likely pathogenic |
| **BP3** | **Not Applicable** | This rule is not applicable to PTEN |
| **BP4** | **Applicable (Supporting)** | Splicing variants: Concordance of SpliceAI (scores 0-0.2) **AND** VarSeak (Class 1 and 2) predicting no splicing impact. Missense variants: REVEL score **< 0.5**. **Not** to be applied for variants which may impact the intron 1 splice donor or acceptor sites; use cautiously for variants which may impact the intron 6 splice acceptor |
| **BP5** | **Applicable (Supporting)** | Variant found in a case with an alternate molecular basis for disease. At least **two** such cases required. The other gene/disorder must be considered highly penetrant **AND** patient's personal/family history must demonstrate no overlap between the other gene and PTEN |
| **BP6** | **Not Applicable** | Not for use per ClinGen SVI VCEP Review Committee (PMID: 29543229) |
| **BP7** | **Applicable (Supporting)** | A synonymous (silent) or intronic variant at or beyond **+7/-21** for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site |

---

## Rules for Combining Criteria

Variants will be classified per Richards et al., 2015 with the following exceptions:
- **1 Benign Strong (BS) = Likely Benign**
- **1 Pathogenic Very Strong (PVS) + 1 Pathogenic Supporting (PP) = Likely Pathogenic**
- Variants with conflicting evidence may be classified using the Bayesian points system (Tavtigian et al., 2018)

### Pathogenic Classification

| Criteria Combination |
|---------------------|
| 1 Very Strong (PVS1, PS2_VeryStrong, PS4_VeryStrong, PM6_VeryStrong) **AND** ≥1 Strong (PVS1_Strong, PS1, PS2, PS3, PS4, PM6_Strong, PP1_Strong) |
| 1 Very Strong **AND** ≥2 Moderate (PVS1_Moderate, PS3_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate) |
| 1 Very Strong **AND** 1 Moderate **AND** 1 Supporting (PS3_Supporting, PS4_Supporting, PM2_Supporting, PP1, PP2, PP3) |
| 1 Very Strong **AND** ≥2 Supporting |
| ≥2 Strong |
| 1 Strong **AND** ≥3 Moderate |
| 1 Strong **AND** 2 Moderate **AND** ≥2 Supporting |
| 1 Strong **AND** 1 Moderate **AND** ≥4 Supporting |

### Likely Pathogenic Classification

| Criteria Combination |
|---------------------|
| 1 Very Strong **AND** 1 Moderate |
| 1 Very Strong **AND** 1 Supporting |
| 1 Strong **AND** 1 Moderate |
| 1 Strong **AND** ≥2 Supporting |
| 1 Strong **AND** 2 Moderate |
| ≥3 Moderate |
| 2 Moderate **AND** ≥2 Supporting |
| 1 Moderate **AND** ≥4 Supporting |

### Benign Classification

| Criteria Combination |
|---------------------|
| 1 Stand Alone (BA1) |
| ≥2 Strong (BS1, BS2, BS3, BS4) |

### Likely Benign Classification

| Criteria Combination |
|---------------------|
| 1 Strong (BS1, BS2, BS3, BS4) |
| ≥2 Supporting (BS1_Supporting, BS2_Supporting, BS3_Supporting, BS4_Supporting, BP2, BP4, BP5, BP7) |

---

## Appendices

### Appendix A: PVS1 Decision Tree

The PTEN PVS1 decision tree assigns strength levels based on variant type and predicted functional impact. The biologically relevant transcript is **NM_000314.8**.

**Key Decision Points:**

1. **Nonsense/Frameshift:** Is the stop codon or disruption at or 5' to p.D375 (c.1121)?
   - Yes → PVS1
   - No, and role of region unknown → PVS1_Moderate

2. **Canonical Splice Sites (+/-1,2):** Does exon skipping disrupt reading frame with NMD predicted?
   - Yes, with disruption at or 5' to p.D375 → PVS1
   - In-frame but critical region (exon 3, 8, or 9) → PVS1_Strong

3. **Deletions:** Does the deletion disrupt reading frame with NMD predicted?
   - Exon 1, 2, 4, 5, 6, 7 or multi-exon (frameshift) → PVS1
   - Exon 3, 8, or 9 (in-frame, critical) → PVS1_Strong
   - Full gene deletion → PVS1

4. **Duplications (≥1 exon, completely within gene):**
   - Proven in tandem, frameshift + NMD → PVS1
   - Presumed in tandem, presumed frameshift + NMD → PVS1_Strong
   - In tandem but NMD not predicted (exon 3 or 8) → PVS1_Strong (proven) / PVS1_Moderate (presumed)
   - Not in tandem or unknown impact → N/A

5. **Initiation Codon:** → PVS1

**Critical regions for in-frame deletions/skipping:** Entire exon 3, exon 8, or exon 9.

### Appendix B: Population Frequency Thresholds Summary

| Criterion | Threshold | Strength |
|-----------|-----------|----------|
| BA1 | >0.00056 (0.056%) | Stand Alone |
| BS1 | 0.000043-0.00056 (0.0043%-0.056%) | Strong |
| BS1_Supporting | 0.0000043-0.000043 (0.00043%-0.0043%) | Supporting |
| PM2_Supporting | <0.00001 (0.001%) | Supporting |

**Frequency Calculation Parameters (Whiffin et al.):**
- Prevalence: 1/9,000
- Allelic heterogeneity: 22/282
- Penetrance: 10%

### Appendix C: Key In Silico Tools and Thresholds

| Tool | Pathogenic Threshold | Benign Threshold | Applicable Variant Types |
|------|---------------------|-------------------|------------------------|
| **REVEL** | >0.7 (PP3) | <0.5 (BP4) | Missense |
| **SpliceAI** | 0.5-1.0 (PP3) | 0-0.2 (BP4) | Synonymous, intronic |
| **VarSeak** | Class 4-5 (PP3) | Class 1-2 (BP4) | Synonymous, intronic |
| **Mighell et al. functional score** | ≤ -1.11 (PS3_Moderate) | >0 (BS3_Supporting) | Missense (phosphatase activity) |

> **Note:** For splicing variants, PP3 and BP4 require concordance of both SpliceAI and VarSeak. BP4 should NOT be applied for variants that may impact the intron 1 splice donor or acceptor sites, and should be used cautiously for variants impacting the intron 6 splice acceptor.

### Appendix D: Criteria Applicability Summary

| Criterion | Status | Max Strength |
|-----------|--------|-------------|
| PVS1 | Applicable | Very Strong |
| PS1 | Applicable | Strong |
| PS2 | Applicable | Very Strong |
| PS3 | Applicable | Strong |
| PS4 | Applicable (Use 1 & 2) | Very Strong |
| PM1 | Applicable | Moderate |
| PM2 | Applicable | Supporting |
| PM3 | **Not Applicable** | — |
| PM4 | Applicable | Moderate |
| PM5 | Applicable | Moderate |
| PM6 | Applicable | Very Strong |
| PP1 | Applicable | Strong |
| PP2 | Applicable | Supporting |
| PP3 | Applicable | Supporting |
| PP4 | **Not Applicable** (incorporated into PS4) | — |
| PP5 | **Not Applicable** | — |
| BA1 | Applicable | Stand Alone |
| BS1 | Applicable | Strong |
| BS2 | Applicable | Strong |
| BS3 | Applicable | Strong |
| BS4 | Applicable | Strong |
| BP1 | **Not Applicable** | — |
| BP2 | Applicable | Supporting |
| BP3 | **Not Applicable** | — |
| BP4 | Applicable | Supporting |
| BP5 | Applicable | Supporting |
| BP6 | **Not Applicable** | — |
| BP7 | Applicable | Supporting |

### Appendix E: Reference PMIDs

| PMID | Reference |
|------|-----------|
| 26504226 | Costa HA et al. Discovery and functional characterization of a neomorphic PTEN mutation. Proc Natl Acad Sci U S A (2015) 112(45):13976-81 |
| 25875300 | Gil A et al. A functional dissection of PTEN N-terminus. PLoS One (2015) 10(4):e0119287 |
| 10866302 | Han SY et al. Functional evaluation of PTEN missense mutations. Cancer Res (2000) 60(12):3147-51 |
| 22962422 | He X et al. PTEN lipid phosphatase activity and proper subcellular localization. J Clin Endocrinol Metab (2012) 97(11):E2179-87 |
| 1438297 | Henikoff S, Henikoff JG. Amino acid substitution matrices from protein blocks. Proc Natl Acad Sci U S A (1992) 89(22):10915-9 |
| 19457929 | Lobo GP et al. Germline and somatic cancer-associated mutations in the ATP-binding motifs of PTEN. Hum Mol Genet (2009) 18(15):2851-62 |
| 29056325 | Malek M et al. PTEN Regulates PI(3,4)P(2) Signaling Downstream of Class I PI3K. Mol Cell (2017) 68(3):566-580.e10 |
| 29706350 | Mighell TL et al. A Saturation Mutagenesis Approach to Understanding PTEN Lipid Phosphatase Activity. Am J Hum Genet (2018) 102(5):943-955 |
| 9811831 | Myers MP et al. The lipid phosphatase activity of PTEN is critical for its tumor suppressor function. Proc Natl Acad Sci U S A (1998) 95(23):13513-8 |
| 25741868 | Richards S et al. Standards and guidelines for the interpretation of sequence variants. Genet Med (2015) 17(5):405-24 |
| 21828076 | Rodriguez-Escudero I et al. A comprehensive functional analysis of PTEN mutations. Hum Mol Genet (2011) 20(21):4132-42 |
| 25527629 | Spinelli L et al. Functionally distinct groups of inherited PTEN mutations in autism and tumour syndromes. J Med Genet (2015) 52(2):128-34 |
| 9778245 | Stambolic V et al. Negative regulation of PKB/Akt-dependent cell survival by PTEN. Cell (1998) 95(1):29-39 |
| 29300386 | Tavtigian SV et al. Modeling the ACMG/AMP variant classification guidelines as a Bayesian classification framework. Genet Med (2018) 20(9):1054-1060 |
| 21194675 | Tan MH et al. A clinical scoring system for selection of patients for PTEN mutation testing. Am J Hum Genet (2011) 88(1):42-56 |
| 30192042 | Tayoun AN et al. Recommendations for interpreting the loss of function PVS1 ACMG/AMP variant criterion. Hum Mutat (2018) |
| 28518168 | Whiffin N et al. Using high-resolution variant frequencies to empower clinical genome interpretation. Genet Med (2017) |
| 23335809 | Bubien V et al. High cumulative risks of cancer in patients with PTEN hamartoma tumour syndrome. J Med Genet (2013) |
| 29543229 | Biesecker LG et al. ClinGen Sequence Variant Interpretation VCEP Review. Genet Med (2018) |

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 3.1.0 | 3/14/2024 | Minor changes: (1) Correct SpliceAI cutoff for BP4 rule, (2) Correct the Rules for Combining Criteria, (3) Add BLOSUM matrix, Cleveland Clinic score and Pediatric score tables |

---

*This document was compiled from ClinGen PTEN VCEP specifications v3.1.0. For the most current version, please refer to the ClinGen website.*
