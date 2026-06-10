# ClinGen InSiGHT Hereditary Colorectal Cancer/Polyposis VCEP Variant Interpretation Guidelines for APC

**Version:** 2.1.0
**Released:** 11/24/2023
**Affiliation:** InSiGHT Hereditary Colorectal Cancer/Polyposis VCEP
**Expert Panel Page:** https://www.clinicalgenome.org/affiliation/50099
**Based on:** Richards et al., 2015 ACMG/AMP Guidelines
**Related Publications:** PMIDs 30192042, 33348689, 4843792

---

## Gene Information

| Attribute | Value |
|-----------|-------|
| **Gene** | APC (HGNC:583) |
| **HGNC Name** | APC regulator of WNT signaling pathway |
| **Transcript** | NM_000038.6 (MANE transcript) |
| **Alternative Transcripts** | NM_001127510.2, NM_001127511.3 (promoter 1B deletion) |
| **Disease** | Familial adenomatous polyposis 1 (MONDO:0021056) |
| **Inheritance** | Autosomal dominant |

### Important Notes

- These criteria are for **classic or attenuated familial adenomatous polyposis only** and do NOT apply to Gastric adenocarcinoma and proximal polyposis of the stomach (GAPPS, MONDO:0017790)
- The preferred transcript for coding, intronic and promoter 1A variants is **NM_000038.6**
- For promoter 1B deletion, the preferred transcript is **NM_001127511.3**
- Variants are described in HGVS nomenclature according to NM_000038.6 unless otherwise specified
- Numbered exons refer to exons 1-16 in NM_000038.6 transcript
- These criteria are **NOT developed for low/moderate penetrant variants** (e.g., c.3920T>A p.(Ile1307Lys) and c.3949G>C p.(Glu1317Gln))

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

**Original ACMG Summary:** Null variant (nonsense, frameshift, canonical ±1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.

**Caveats:**
- Beware of genes where LOF is not a known disease mechanism (e.g., GFAP, MYH7)
- Use caution interpreting LOF variants at the extreme 3' end of a gene
- Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact
- Use caution in the presence of multiple transcripts

**VCEP Specifications:**

APC is a gene where LOF is the predominant mechanism of disease. Based on published transcript analyses using leukocyte RNA, truncated alleles do not completely undergo nonsense mediated decay (NMD) since truncated alleles are detectable without NMD blockade. Nevertheless, truncating variants throughout the gene are well described, especially in the last exon 16 (which comprises 77% of the gene).

#### Gene Boundaries for PVS1 Application

| Boundary | Variant | Codon |
|----------|---------|-------|
| **5' boundary** | c.147_150del p.(Lys49Asnfs*20) | Codon 49 |
| **3' boundary** | c.7932_7935del p.(Tyr2645Lysfs*14) | Codon 2645 |

#### PVS1 Strength Levels

| Strength | Criteria |
|----------|----------|
| **Very Strong (PVS1)** | Null variant as per modified decision tree (Figure 1) - List A variants |
| **Strong (PVS1_Strong)** | As per modified decision tree (Figure 1) - List B variants |
| **Moderate (PVS1_Moderate)** | As per modified decision tree (Figure 1) - List C variants |
| **Supporting (PVS1_Supporting)** | As per modified decision tree (Figure 1) - List D variants |

#### Splice Variant Classification Lists

**List A (PVS1):**
- Canonical splice sites where exon skipping or cryptic splice site use disrupts reading frame affecting biologically relevant transcripts
- Canonical splice sites where exon skipping preserves reading frame AND existing clinical data supports causative role

**List B (PVS1_Strong):**
- c.1548+2T>C (weak native site splice prediction with SpliceAI - downgraded one level)
- G to non-G last nucleotide changes with consistently deleterious splicing consequences as canonical ±1,2 splice variants

**List C (PVS1_Moderate):**
- Canonical splice sites where exon skipping preserves reading frame AND existing clinical data is insufficient to support causative role

**List D (PVS1_Supporting):**
- c.729+2T>C (weak native site splice prediction with SpliceAI)
- c.933G>A,C,T (causes in-frame exon skipping)

**List E (N/A - Not Applicable):**
- Canonical splice sites affecting exon 2 (alternative transcript exists)
- Canonical splice sites where cryptic splice site use preserves reading frame leading to small in-frame indel
- c.645+2T>C (native splice site not predicted by SpliceAI)

---

### PS1 - Same Amino Acid Change

**Original ACMG Summary:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.

**Caveat:** Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:**

**Recommended Splice Prediction Programs:**
- SpliceAI: https://spliceailookup.broadinstitute.org/
- MaxEntScan: http://hollywood.mit.edu/burgelab/maxent/Xmaxentscan_scoreseq.html (5' splice sites) and http://hollywood.mit.edu/burgelab/maxent/Xmaxentscan_scoreseq_acc.html (3' splice sites)
- VarSeak: https://varseak.bio/

**Splice Prediction Thresholds:**
- SpliceAI: Loss of native splice site considered for scores 0.8-1.0; Gain of cryptic splice site: Strong (0.8-1.0), Moderate (0.2-0.8)
- MaxEntScan: Score >3 required for credibility; -15% threshold for native splice site loss; Score >3 for cryptic site use

| Strength | Criteria |
|----------|----------|
| **Strong (PS1)** | Previously established variant classified as **Pathogenic** per APC-specific modifications |
| **Moderate (PS1_Moderate)** | Previously established variant classified as **Likely Pathogenic** per APC-specific modifications |

**Applicable Variants:**
- **Missense variants:** Same amino acid change as previously established P/LP variant
- **Splice variants:** Affects splicing at the same nucleotide as previously established P/LP variant (prediction must be above defined thresholds)

**Currently Known LP Missense Variants:**
- c.3077A>G p.(Asn1026Ser)
- c.3084T>A p.(Ser1028Arg)

*Note: No missense variant has been classified as Pathogenic based on current evidence.*

---

### PS2 - De Novo (Confirmed)

**Original ACMG Summary:** De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.

**Note:** Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.

**VCEP Specifications:**

Based on SVI Recommendation for De Novo Criteria (PS2 & PM6) - Version 1.1 and Fortuno et al. 2020 (PMID: 33300245).

**Parental Assessment:**
- Parents should have been colonoscoped
- <5 colorectal adenomas in colonoscopy and no phenotypic features from Table 1 = inconspicuous
- If parents are >60 years, no signs of GI tumor, no Table 1 features, and family history inconspicuous = can be considered unaffected

**Mosaicism Considerations:**
- Be aware of somatic/postzygotic mosaicism in index patients (frequently associated with attenuated colorectal phenotype)
- Mosaicism in both index patients and parents can be used for PS2
- For low-level mosaicism (<10%) in index patients, confirm variant in at least one affected tissue sample

| Strength | De Novo Score Threshold |
|----------|------------------------|
| **Very Strong (PS2_VeryStrong)** | ≥4 de novo scores |
| **Strong (PS2)** | 2-3.5 de novo scores |
| **Moderate (PS2_Moderate)** | 1-1.5 de novo scores |

*See Tables 1 and 2 for de novo score curation.*

---

### PS3 - Functional Studies

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.

**VCEP Specifications:**

#### RNA Assays

| Strength | Criteria |
|----------|----------|
| **Very Strong (PS3_VeryStrong)** | RNA assays show: (1) premature stop codon OR (2) in-frame skipping of exon 13 or 14 **AND** absence of full-length transcript |
| **Strong (PS3)** | RNA assays show: (1) premature stop codon OR (2) in-frame skipping of exon 13 or 14 **AND** <10% of full-length transcript |
| **Moderate (PS3_Moderate)** | RNA assays show: (1) premature stop codon AND reports of exon deletion/skipping/loss, insertion of intronic nucleotides **OR** (2) in-frame skipping of exon 13 or 14 AND reports of exon deletion/skipping/loss **OR** (3) other in-frame skipping AND absent or <10% full-length transcript |
| **Supporting (PS3_Supporting)** | RNA assays show: (1) in-frame skipping of exons other than 13 or 14 AND reports of exon deletion/skipping/loss, insertion of intronic nucleotides **OR** (2) over-expression of an alternative transcript (exons 10, 11 or 15) |

#### Protein Assays

| Strength | Criteria |
|----------|----------|
| **Supporting (PS3_Supporting)** | Increased β-catenin regulated transcription activity AND/OR decreased binding to β-catenin by surface plasmon resonance (only for variants within β-catenin binding domain, codons 959-2129) |

**Technical Notes:**
- Absence of full-length transcript or <10% should be demonstrated by Sanger sequencing of full-length fragment or allele-specific expression
- Overexpression of alternative transcript should be demonstrated as shown in Aretz et al. 2004 (PMID: 15459959)

---

### PS4 - Prevalence in Affected

**Original ACMG Summary:** The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.

**VCEP Specifications:**

Based on Fortuno et al. 2020 (PMID: 33300245). Uses phenotype point system (Table 1).

| Strength | Phenotype Points Threshold |
|----------|---------------------------|
| **Very Strong (PS4_VeryStrong)** | ≥16 phenotype points |
| **Strong (PS4)** | 4-15.5 phenotype points |
| **Moderate (PS4_Moderate)** | 2-3.5 phenotype points |
| **Supporting (PS4_Supporting)** | 1-1.5 phenotype points |

*See Table 1 for phenotype points curation.*

---

### PM1 - Mutational Hot Spot

**Original ACMG Summary:** Located in a mutational hot spot and/or critical and well-established functional domain (e.g., active site of an enzyme) without benign variation.

**VCEP Specification:** **Not Applicable**

**Rationale:**
- Only two amino acid positions (1026 and 1028) have reported LP missense variants, but insufficient evidence to define as mutational hotspot
- No other known mutational hotspots for pathogenic missense germline variants in APC
- Somatic "mutation cluster region" exists but vast majority of somatic variants are truncating

---

### PM2 - Absent from Controls

**Original ACMG Summary:** Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

**Caveat:** Population data for indels may be poorly called by next generation sequencing.

**VCEP Specifications:**

**General Recommendation:** Use the total population from the non-cancer dataset from gnomAD (v2.1.1)

| Strength | Criteria |
|----------|----------|
| **Supporting (PM2_Supporting)** | Allele frequency ≤0.0003% (0.000003) if allele count >1 **OR** Allele frequency <0.001% (0.00001) if allele count ≤1 |

**Calculation Parameters:**
- Inheritance: monoallelic
- Prevalence: 1:10,000 (1:20,000 chromosomes)
- Allelic heterogeneity: 0.06 (based on most common variant c.3927_3931delAAAGA)
- Genetic heterogeneity: 1
- Penetrance: 0.9

**Notes:**
- For populations underrepresented in gnomAD, regional databases with ≥2000 tested alleles can be used (not applicable for founder populations)
- For indel variants, be careful that variant description/position in databases may be slightly different

---

### PM3 - In Trans with Pathogenic

**Original ACMG Summary:** For recessive disorders, detected in trans with a pathogenic variant.

**VCEP Specification:** **Not Applicable**

FAP has an autosomal dominant mode of inheritance.

---

### PM4 - Protein Length Changes

**Original ACMG Summary:** Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

**VCEP Specification:** **Not Applicable**

Not used due to limited available data.

---

### PM5 - Novel Missense at Same Residue

**Original ACMG Summary:** Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.

**Caveat:** Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Moderate (PM5)** | Reported missense variant at the same position was classified as **Pathogenic** per APC-specific modifications |
| **Supporting (PM5_Supporting)** | Reported missense variant at the same position was classified as **Likely Pathogenic** per APC-specific modifications |

**Requirements:**
- Grantham's distance of the variant under assessment must have an equal or higher score than the reported variant
- Do not use if mechanism of pathogenicity is a splicing defect (check with in silico splicing predictors)

**Currently Applicable Positions:**
- p.Asn1026 (c.3077A>G p.(Asn1026Ser) - LP)
- p.Ser1028 (c.3084T>A p.(Ser1028Arg) - LP)

---

### PM6 - De Novo (Assumed)

**Original ACMG Summary:** Assumed de novo, but without confirmation of paternity and maternity.

**VCEP Specifications:**

Same as PS2 - uses de novo score point-based system (Tables 1 and 2).

| Strength | De Novo Score Threshold |
|----------|------------------------|
| **Very Strong (PM6_VeryStrong)** | ≥4 de novo scores |
| **Strong (PM6_Strong)** | 2-3.5 de novo scores |
| **Moderate (PM6)** | 1-1.5 de novo scores |
| **Supporting (PM6_Supporting)** | 0.5 de novo scores |

---

### PP1 - Co-segregation

**Original ACMG Summary:** Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.

**VCEP Specifications:**

Based on Luo et al. 2019 (PMID: 31648317) and Jarvik & Browning 2016 (PMID: 27236918).

**Requirements:**
- Affected individuals must exhibit at least 0.5 phenotype points (Table 1)
- For relatives: ≥10 or "multiple" colorectal adenomas = 0.5 points
- Only count genotype and phenotype positive individuals AND obligate carriers with phenotype
- Carriers who have received chemoprevention (may have milder phenotype) can also be counted

| Strength | Meioses Required |
|----------|-----------------|
| **Strong (PP1_Strong)** | ≥7 meioses in ≥2 families |
| **Moderate (PP1_Moderate)** | 5-6 meioses in ≥1 family |
| **Supporting (PP1)** | 3-4 meioses in ≥1 family |

**Caveat:** If co-segregation is only observed in one family, consider that this observation can only give evidence that the variant or another (truly causative) variant in LD segregates with the phenotype.

---

### PP2 - Missense in Constrained Gene

**Original ACMG Summary:** Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.

**VCEP Specification:** **Not Applicable**

**Rationale:**
- Missense variants are not a frequent mutation type in APC
- Majority of missense variants are classified as benign/likely benign or VUS
- A few represent splice variants and low/moderate penetrant variants
- Currently only two positions with reported LP missense variants (p.Asn1026 and p.Ser1028)

---

### PP3 - Computational Evidence

**Original ACMG Summary:** Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).

**Caveat:** As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.

**VCEP Specifications:**

Based on Lee et al. 2018 (PMID: 30311375).

| Variant Type | Application |
|--------------|-------------|
| **Missense variants** | Do NOT use computational prediction models for conservation, evolution, etc. Only use in silico splicing predictors to reveal possible splicing effects |
| **Non-canonical splicing variants** | Multiple in silico splicing predictors support a deleterious effect = **PP3 (Supporting)** |

**Rationale:** Predictions for the only known LP missense variants at p.Asn1026 and p.Ser1028 do not clearly predict a deleterious effect.

---

### PP4 - Phenotype Specificity

**Original ACMG Summary:** Patient's phenotype or family history is highly specific for a disease with a single genetic etiology.

**VCEP Specification:** **Not Applicable**

Already captured by the specifications of PS4, and thus cannot be used as independent evidence.

---

### PP5 - Reputable Source

**Original ACMG Summary:** Reputable source recently reports variant as pathogenic, but the evidence is not available to the laboratory to perform an independent evaluation.

**VCEP Specification:** **Not Applicable**

This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PMID: 29543229). Expert opinions should only be considered if accompanied by the primary evidence used.

---

## Benign Criteria

### BA1 - Allele Frequency >5%

**Original ACMG Summary:** Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

**VCEP Specifications:**

**General Recommendation:** Use the non-cancer dataset from gnomAD (v2.1.1)

| Strength | Criteria |
|----------|----------|
| **Stand Alone (BA1)** | gnomAD Popmax Filtering Allele Frequency ≥**0.1%** (0.001) |

**Calculation Parameters:**
- Inheritance: monoallelic
- Prevalence: 1:5,000 (1:10,000 chromosomes)
- Allelic heterogeneity: 1
- Genetic heterogeneity: 0.5
- Penetrance: 0.8
- Calculated AF: ≥0.006% → 10-fold rounded value used: ≥0.1%

---

### BS1 - Frequency Greater Than Expected

**Original ACMG Summary:** Allele frequency is greater than expected for disorder.

**VCEP Specifications:**

**General Recommendation:** Use the non-cancer dataset from gnomAD (v2.1.1)

| Strength | Criteria |
|----------|----------|
| **Strong (BS1)** | gnomAD Popmax Filtering Allele Frequency ≥**0.001%** (0.00001) |

**Calculation Parameters:**
- Inheritance: monoallelic
- Prevalence: 1:5,000 (1:10,000 chromosomes)
- Allelic heterogeneity: 0.06
- Genetic heterogeneity: 1
- Penetrance: 0.8
- Calculated AF: ≥0.0008% → Rounded to ≥0.001%

---

### BS2 - Observed in Healthy Adult

**Original ACMG Summary:** Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

**VCEP Specifications:**

Based on Lee et al. 2018 (PMID: 30311375).

**Caveat:** Phenotype is usually not visible without colonoscopy.

**Database Note:** The non-cancer dataset from gnomAD (v2.1.1) cannot be used for "heterozygous healthy individuals" due to limited phenotype information. However, gnomAD can be used to search for **homozygous individuals**.

| Strength | Criteria |
|----------|----------|
| **Strong (BS2)** | ≥10 points for healthy individuals **OR** ≥2 times in homozygous state |
| **Supporting (BS2_Supporting)** | ≥3 points for healthy individuals |

**Healthy Individual Point System:**

**1 point:**
- Age ≥50 years + Less than 5 adenomatous polyps in colonoscopy + Absence of features in Table 1

**OR**
- Age ≥50 years + Colorectal cancer/polyposis was NOT the indication for testing

**0.5 points:**
- Keywords including: control, non-cancer, normal, unaffected population

---

### BS3 - Functional Studies (No Effect)

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong (BS3)** | RNA assay of synonymous or intronic variant in constitutional patient sample demonstrates no mRNA aberration **AND** biallelic expression is shown and/or nonsense-mediated decay inhibition was used |
| **Supporting (BS3_Supporting)** | RNA assay demonstrates no mRNA aberration, WITHOUT demonstration of biallelic expression or NMD inhibition **OR** Protein assay shows retention of β-catenin regulated transcription activity comparable to wild-type (only for variants within β-catenin binding domain, codons 959-2129) |

---

### BS4 - Lack of Segregation

**Original ACMG Summary:** Lack of segregation in affected members of a family.

**Caveat:** The presence of phenocopies for common phenotypes (i.e., cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong (BS4)** | Affected member without the variant scores ≥1 phenotype point **OR** ≥2 affected members without the variant each score ≥0.5 phenotype points (Table 1) |
| **Supporting (BS4_Supporting)** | Affected member without the variant scores ≥0.5 phenotype points (Table 1) |

---

### BP1-BP7 - Benign Supporting

| Criterion | Status | VCEP Specification |
|-----------|--------|-------------------|
| **BP1** | Applicable | Applicable to APC **EXCEPT** for missense variants located in the first 15-amino acid repeat of the β-catenin binding domain (codon 1021-1035). Use splice prediction tools to identify missense variants that are actually splice variants. |
| **BP2** | Applicable | Observed in trans with a (Likely) Pathogenic APC variant **OR** ≥3 times in unknown phase with different (Likely) Pathogenic APC variants |
| **BP3** | Not Applicable | Not used due to limited available data |
| **BP4** | Applicable | **Missense variants:** NOT applicable. **Synonymous/intronic variants:** Multiple in silico splicing predictors suggest no impact on gene or gene product |
| **BP5** | Applicable | (Likely) Pathogenic variant in another adenomatous polyposis gene: heterozygous variants in *POLD1* or *POLE*; biallelic variants in *MUTYH*, *NTHL1* or *MSH3*; in patients with childhood/adolescence onset: biallelic variants in *MLH1*, *MSH2*, *MSH6* or *PMS2*. Only applicable when colorectal polyposis phenotype is present. |
| **BP6** | Not Applicable | Not for use per ClinGen SVI recommendation (PMID: 29543229) |
| **BP7** | Applicable | Synonymous or intronic variant at or beyond +7/−21 for which multiple splicing prediction algorithms predict no impact to splice consensus sequence nor creation of new splice site. **Note:** Use of BP7 with BP4 is allowed. |

---

## Rules for Combining Criteria

### Important Notes (APC-Specific)

1. The combination of one **Pathogenic-Very Strong** criterion and one **Pathogenic-Supporting** criterion reaches **Likely Pathogenic**
2. The fulfillment of one **Benign-Strong** criterion reaches **Likely Benign**
3. If a rare variant fulfilling only PM2_Supporting (and no other pathogenic codes) also meets criteria for (Likely) Benign, the population data is not considered conflicting → can classify as (Likely) Benign
4. **PVS1 cannot be applied in conjunction with** splicing predictions (PP3) or RNA assays (PS3)
5. If RNA assay findings conflict with splice predictors, **RNA findings override** computational predictions (BS3 over PP3, PS3 over BP4)
6. **PS4_Variable and PP1_Variable should not be applied** if BS1 is met; PM2_Supporting is not required so clinical criteria may apply for pathogenic variants with some population data

---

### Pathogenic Classification

| Criteria Combination |
|---------------------|
| ≥2 Strong (PVS1_Strong, PS1, PS2, PS3, PS4, PM6_Strong, PP1_Strong) |
| 1 Strong AND ≥3 Moderate |
| 1 Strong AND 2 Moderate AND ≥2 Supporting |
| 1 Strong AND 1 Moderate AND ≥4 Supporting |
| 1 Very Strong (PVS1) AND ≥1 Strong (PS1, PS2, PS4, PM6_Strong, PP1_Strong) |
| 1 Very Strong (PS2_VeryStrong, PS3_VeryStrong, PS4_VeryStrong) AND ≥1 Strong |
| 1 Very Strong (PVS1) AND ≥2 Moderate |
| 1 Very Strong (PS2_VeryStrong, PS3_VeryStrong, PS4_VeryStrong) AND ≥2 Moderate |
| 1 Very Strong (PVS1) AND 1 Moderate AND 1 Supporting |
| 1 Very Strong (PS2_VeryStrong, PS3_VeryStrong, PS4_VeryStrong) AND 1 Moderate AND 1 Supporting |
| 1 Very Strong (PVS1) AND ≥2 Supporting |
| 1 Very Strong (PS2_VeryStrong, PS3_VeryStrong, PS4_VeryStrong) AND ≥2 Supporting |

### Likely Pathogenic Classification

| Criteria Combination |
|---------------------|
| 1 Strong AND 1 Moderate |
| 1 Strong AND ≥2 Supporting |
| ≥3 Moderate |
| 2 Moderate AND ≥2 Supporting |
| 1 Strong AND 2 Moderate |
| 1 Very Strong (PVS1) AND 1 Moderate |
| 1 Very Strong (PS2_VeryStrong, PS3_VeryStrong, PS4_VeryStrong) AND 1 Moderate |
| **1 Very Strong (PVS1) AND 1 Supporting** *(APC-specific)* |
| 1 Very Strong (PS2_VeryStrong, PS3_VeryStrong, PS4_VeryStrong) AND 1 Supporting |
| 1 Moderate AND ≥4 Supporting |

### Benign Classification

| Criteria Combination |
|---------------------|
| 1 Stand Alone (BA1) |
| ≥2 Strong (BS1, BS2, BS3, BS4) |

### Likely Benign Classification

| Criteria Combination |
|---------------------|
| ≥2 Supporting (BS2_Supporting, BS3_Supporting, BS4_Supporting, BP1, BP2, BP4, BP5, BP7) |
| **1 Strong (BS1, BS2, BS3, BS4)** *(APC-specific)* |

---

## Appendices

### Appendix A: Phenotype Point System (Table 1)

The phenotype point system is used for criteria: PS2, PS4, PM6, PP1, and BS4.

| Phenotype | Points |
|-----------|--------|
| Classic FAP (≥100 colorectal adenomas) | 1 point |
| Attenuated FAP (10-99 colorectal adenomas) | 0.5 points |
| ≥10 or "multiple" colorectal adenomas (for relatives in PP1) | 0.5 points |
| Colorectal cancer with polyposis | Additional points based on context |
| Desmoid tumor | Additional points |
| CHRPE (Congenital Hypertrophy of the Retinal Pigment Epithelium) | Additional points |
| Osteomas | Additional points |
| Other extracolonic manifestations | Additional points |

*Refer to the full Table 1 in the supplementary material for complete point assignments.*

### Appendix B: De Novo Score Curation (Table 2)

De novo scores are calculated based on:
1. Phenotype points of the proband
2. Parental confirmation status (maternity and paternity confirmed vs. assumed)

| Phenotype Score | Confirmed Parental Testing | Assumed (Not Confirmed) |
|-----------------|---------------------------|------------------------|
| High phenotype specificity | Higher de novo score | Lower de novo score |
| Moderate phenotype specificity | Moderate de novo score | Lower de novo score |

*Refer to the full Table 2 in the supplementary material for complete scoring matrix.*

### Appendix C: Exon Numbering Conversion Table

| Start (c.) | Stop (c.) | NM_000038.6 | NM_001127510.2 | Coding Exons ("traditional") | LRG_130 | Result of Exon Deletion/Skipping |
|-----------|----------|-------------|----------------|------------------------------|---------|----------------------------------|
| -193 | -127 | - | 1 | - | - | - |
| -126 | -19 | - | 2 | - | - | - |
| -85 | -19 | 1 | - | - | - | - |
| -18 | 135 | 2 | 3 | 1 | 4 | in-frame |
| 136 | 220 | 3 | 4 | 2 | 5 | out-of-frame |
| 221 | 422 | 4 | 5 | 3 | 6 | out-of-frame |
| 423 | 531 | 5 | 6 | 4 | 7 | out-of-frame |
| 532 | 645 | 6 | 7 | 5 | 8 | in-frame |
| 646 | 729 | 7 | 8 | 6 | 9 | in-frame |
| 730 | 834 | 8 | 9 | 7 | 10 | in-frame |
| 835 | 933 | 9 | 10 | 8 | 11 | in-frame |
| 934 | 1312 | 10 | 11 | 9 | 12 | out-of-frame |
| 1313 | 1408 | 11 | 12 | 10 | 13 | in-frame |
| 1409 | 1548 | 12 | 13 | 11 | 14 | out-of-frame |
| 1549 | 1626 | 13 | 14 | 12 | 15 | in-frame |
| 1627 | 1743 | 14 | 15 | 13 | 16 | in-frame |
| 1744 | 1958 | 15 | 16 | 14 | 17 | out-of-frame |
| 1959 | 8532 | 16 | 17 | 15 | 18 | out-of-frame |

### Appendix D: Population Frequency Thresholds Summary

| Criterion | Threshold | Strength | Database |
|-----------|-----------|----------|----------|
| BA1 | ≥0.1% (0.001) | Stand Alone | gnomAD Popmax FAF (non-cancer) |
| BS1 | ≥0.001% (0.00001) | Strong | gnomAD Popmax FAF (non-cancer) |
| PM2 | ≤0.0003% (AC>1) or <0.001% (AC≤1) | Supporting | gnomAD total population (non-cancer) |

### Appendix E: Reference PMIDs

| PMID | Reference |
|------|-----------|
| 30192042 | Abou Tayoun AN, Pesaran T et al. *Recommendations for interpreting the loss of function PVS1 ACMG/AMP variant criterion.* Hum Mutat (2018) 39(11):1517-1524 |
| 33348689 | Juanes MA. *Cytoskeletal Control and Wnt Signaling-APC's Dual Contributions in Stem Cell Division and Colorectal Cancer.* Cancers (Basel) (2020) 12(12) |
| 4843792 | Grantham R. *Amino acid difference formula to help explain protein evolution.* Science (1974) 185(4154):862-4 |
| 29543229 | Biesecker LG et al. *ClinGen recommendations for PP5 and BP6.* |
| 33300245 | Fortuno et al. (2020) - De novo criteria recommendations |
| 29300372 | Kelly et al. (2018) - Allele frequency calculator |
| 30311375 | Lee et al. (2018) - CDH1 specifications reference |
| 31648317 | Luo et al. (2019) - Co-segregation recommendations |
| 27236918 | Jarvik & Browning (2016) - Segregation analysis |
| 30311369 | Walsh et al. (2018) - Somatic variant data |
| 30311380 | Mester et al. (2018) - BP2 recommendations |
| 30311390 | Zastrow et al. (2018) - BS1 recommendations |
| 22505045 | Houdayer et al. (2012) - MaxEntScan thresholds |
| 15459959 | Aretz et al. (2004) - RNA analysis methodology |
| 19196998 | Kaufmann et al. (2009) - NMD studies |
| 20434453 | Castellsagué et al. (2010) - Allele-specific expression |
| 33011440 | Rofes et al. (2020) - Transcript analysis |
| 26613750 | Spier et al. (2015) - Somatic/postzygotic mosaicism |
| 9973305 | Farrington et al. (1999) - Parental mosaicism |
| 26054435 | Acuno-Hidalgo et al. (2015) - Mosaicism |
| 18166348 | Menendez et al. (2008) - Missense variant functional studies |
| 32750050 | Karabachev et al. (2020) - Splice variants |

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 2.1.0 | 11/24/2023 | Correction of inaccuracies in Rules for Combining Criteria; Addition of relevant instructions from supplementary material; Change in Fig. 1A (update of pathways for "G to non-G changes"); Change in Fig. 1B (transfer of splice variants between lists based on RNA and phenotype data); Update of supplementary material file |
| 2.0.0 | Previous | Initial version 2 release |

---

*This document was compiled from ClinGen VCEP specifications. For the most current version, please visit: https://cspec.genome.network/cspec/ui/svi/doc/GN089*
