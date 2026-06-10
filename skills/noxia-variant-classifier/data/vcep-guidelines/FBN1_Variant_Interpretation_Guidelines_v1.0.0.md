# ClinGen FBN1 VCEP Variant Interpretation Guidelines for FBN1

**Version:** 1.0.0
**Released:** January 4, 2022
**Affiliation:** FBN1 VCEP
**Expert Panel Page:** https://www.clinicalgenome.org/affiliation/50046
**Based on:** Richards et al., 2015 ACMG/AMP Guidelines

---

## Gene Information

| Attribute | Value |
|-----------|-------|
| **Gene** | FBN1 (HGNC:3603) |
| **HGNC Name** | fibrillin 1 |
| **Transcript** | NM_000138 |
| **Disease** | Marfan syndrome (MONDO:0007947) |
| **Inheritance** | Autosomal Dominant |

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
   - [BA1 - Allele Frequency >0.1%](#ba1---allele-frequency-01)
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
- Use caution interpreting LOF variants at the extreme 3' end of a gene.
- Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact.

**VCEP Specifications:**
- Follow the adapted PVS1 flowchart (see Appendix A).
- There is only 1 relevant transcript for FBN1 (NM_000138).
- The C-terminal region is proven to be critical to protein function (multiple LP/P variants identified in this region).
- PP3 cannot be applied if using the PVS1 criterion for splice site variants in position +/- 1/2.

#### Strength Levels

| Strength | Criteria |
|----------|----------|
| **Very Strong** | Nonsense/frameshift variants predicted to undergo NMD (not affecting last exon or 55 last nt of penultimate exon). 1,2 splice site variants leading to exon skipping or use of a cryptic splice site disrupting the reading frame and predicted to undergo NMD. Full gene deletion. Single to multi-exon deletion disrupting the reading frame and predicted to undergo NMD. Duplication (>=1 exon in size and completely contained within gene) proven in tandem and disrupting the reading frame and predicted to undergo NMD. |
| **Strong** | Nonsense/frameshift variants predicted to escape NMD (affecting last exon, last 55nt of the penultimate exon). 1,2 splice site variants leading to exon skipping or use of a cryptic splice site disrupting the reading frame and predicted to escape NMD. 1,2 splice site variants leading to exon skipping or use of a cryptic splice site but preserving the reading frame. Single to multi-exon deletion disrupting the reading frame and predicted to escape NMD. Single to multi-exon deletion preserving the reading frame. Duplication (>=1 exon in size and completely contained within gene) presumed in tandem and presumably disrupting the reading frame and predicted to escape NMD. |
| **Moderate** | Initiation codon variant with 1 or more pathogenic variant(s) upstream of closest potential in-frame start codon. |

**Notes on NMD prediction:**
- NMD is predicted to occur when a stop codon is integrated in the FBN1 sequence except for stop codons in the last exon or the last 55 nucleotides of the penultimate exon.
- Critical region: Use the same regions defined for the PM1 and PM1_strong arguments.

---

### PS1 - Same Amino Acid Change

**Original ACMG Summary:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | Same amino acid change as a previously established pathogenic variant regardless of nucleotide change. |

**Caveats:**
- Beware of changes that impact splicing rather than the amino acid. Splicing predictions should remain the same for WT and both mutant alleles.
- Original variant should be pathogenic according to the (modified) ACMG guidelines for variant classification.

**Modification Type:** None

---

### PS2 - De Novo (Confirmed)

**Original ACMG Summary:** De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.

**VCEP Specifications:**
- Use the SVI WG point-based system.
- The EP recommends that the parents had a full clinical work-up and an echocardiogram to exclude MFS/HTAAD.

#### Phenotypic Definitions for PS2/PM6

| Category | Definition |
|----------|-----------|
| **Highly specific for disease** | TAAD + ectopia lentis (mainly caused by variants in FBN1) |
| **Consistent with gene but not highly specific** | TAAD + systemic score >=7 (can be caused by variants in few other HTAAD genes) |
| **Consistent but genetic heterogeneity** | (Isolated) TAAD, isolated ectopia lentis, and in case of a child (age <20yrs) systemic score >=7 in whom TAAD is progressive and can be developed later in life |

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
| 2.0-3.0 | Strong |
| 4.0 | Very Strong |

---

### PS3 - Functional Studies

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.

**VCEP Specifications:**
- Use the Functional Assay SVI Documentation.

#### Approved Functional Studies

**Functional studies deemed appropriate:**
- cDNA analyses showing altered FBN1 sequence
- Functional studies showing altered FBN1 protein or RNA expression, proteolysis, folding, assembly, trafficking, secretion, Ca2+ binding, matrix deposition (cfr Dave Hollister assay), microfibril fragmentation/catabolism in an in vitro engineered system

**Functional studies NOT deemed appropriate:**
- Non-specific altered TGF-beta signaling or histological hallmarks of medial degeneration, which are associated with many other types of variants in genes that are associated with MFS or HTAAD in general

**Step 3 assessment:** Studies should be performed in the presence of NMD inhibitor.

| Strength | Criteria |
|----------|----------|
| **Strong** | Follow the Functional Assay SVI Documentation |
| **Moderate** | Follow the Functional Assay SVI Documentation |
| **Supporting** | Follow the Functional Assay SVI Documentation |

---

### PS4 - Prevalence in Affected

**Original ACMG Summary:** The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.

**VCEP Specifications:**
- Each additional proband meeting Ghent criteria or having ectopia lentis may receive **1 point**.
- Those having only thoracic aortic disease or high systemic score, or those for which the phenotype is not described in the literature, will receive **0.5 points**.
- **Caveat:** BA1/BS1 should NOT be met.

| Strength | Points Required |
|----------|----------------|
| **Strong** | >= 4 points |
| **Moderate** | 2-3.5 points |
| **Supporting** | 1-1.5 points |

---

### PM1 - Mutational Hot Spot

**Original ACMG Summary:** Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | Cysteine residues in cbEGF-like domains. **Caveat:** PM5/PS1 should not be used when this argument applies. |
| **Moderate** | Cys in EGF-like domain, Cys in TB domain, Cys in hybrid domain, (D/N)-X-(D/N)-(E/Q)-Xm-(D/N)-Xn-(Y/F) substitution in cbEGF-like domain, invariant calcium-binding or hydroxylation residue in cbEGF-like domain, critical Gly between Cys2-Cys3 in cbEGF-like domain, Gly between Cys3-Cys4 if there is an upstream cbEGF domain, Cys-creating variants. **Caveat:** N to S substitution in the second N of the consensus sequence and G to A might be tolerated; PM1 should not be used in these cases. |

> **Note:** A detailed table with the specific residues for which PM1_strong and PM1 could be considered is provided in the supplemental material (see Appendix B).

---

### PM2 - Absent from Controls

**Original ACMG Summary:** Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

**VCEP Specification (Supporting only):**
- gnomAD popmax filtering allele frequency **<0.0005%** (<5.0E-6)
- Use the highest ethnic population allele frequency.
- **Caveat:** PVS1 + PM2_Supporting may reach Likely Pathogenic.
- **Caveat:** Do not use Finnish, Ashkenazi Jewish, or "Other" populations in gnomAD.
- Minimum amount of studied alleles should be 2000.

**Note:** PM2 at moderate level is not applicable for FBN1 (autosomal dominant disorder).

---

### PM3 - In Trans with Pathogenic

**Original ACMG Summary:** For recessive disorders, detected in trans with a pathogenic variant.

**VCEP Specifications:** *Not Applicable* - Marfan syndrome is an autosomal dominant disorder.

---

### PM4 - Protein Length Changes

**Original ACMG Summary:** Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Moderate** | Applicable as described per original ACMG guidelines. |

**Caveat:** Cannot be applied simultaneously with PVS1 (at any strength level).

**Modification Type:** None

---

### PM5 - Novel Missense at Same Residue

**Original ACMG Summary:** Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Moderate** | Applicable as described per original ACMG guidelines. |

**Caveats:**
- Use argument with caution when the original missense variant created a cysteine especially in a cbEGF-like domain (cfr PM1_strong) as this may increase the pathogenicity level of this variant improperly.
- Original variant should be pathogenic according to the (modified) ACMG guidelines for variant classification.

**Modification Type:** None

---

### PM6 - De Novo (Assumed)

**Original ACMG Summary:** Assumed de novo, but without confirmation of paternity and maternity.

**VCEP Specifications:** Use the SVI WG point-based system - same as PS2 (see [PS2 section](#ps2---de-novo-confirmed) for phenotypic definitions and point system).

---

### PP1 - Co-segregation

**Original ACMG Summary:** Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.

**VCEP Specifications:**
- Only count affected individuals from the same family (minus proband) that carry the variant or obligate carriers known with the disease.
- The EP will not specifically define "affected", "clinical examination" or cut-offs for aortic Z-scores. These are left to the discretion of the referring physicians.
- Caution needed when counting segregations in presence of other possible disease-causing variants.
- Caution needed when distantly related affected individuals are connected by unknown or unaffected relatives (raises possibility of multiple causes of disease).

#### PP1 Thresholds

| Strength | Number of Affected Individuals |
|----------|-------------------------------|
| **Supporting** | 2-3 affected individuals |
| **Moderate** | 4 affected individuals |
| **Strong** | >=5 affected individuals |

---

### PP2 - Missense in Constrained Gene

**Original ACMG Summary:** Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.

**VCEP Specifications:**
- FBN1 missense constraint z score is higher than 5 (above the 3.09 threshold), hence PP2 is applicable as described.
- **Caveat:** If this argument is used pro-pathogenicity, there must be other arguments supporting pathogenicity, and no arguments supporting a benign assertion.

| Strength | Criteria |
|----------|----------|
| **Supporting** | Applicable as described with caveat above. |

**Modification Type:** None

---

### PP3 - Computational Evidence

**Original ACMG Summary:** Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).

**VCEP Specifications:**

| Variant Type | Prediction Tool(s) | Threshold |
|-------------|-------------------|-----------|
| **Missense** | REVEL | >= 0.75 (pathogenic) |
| **Splice** | GeneSplicer, MaxEntScan, NNSPLICE | All 3 programs must be in concordance |

| Strength | Criteria |
|----------|----------|
| **Supporting** | Meets the above thresholds. |

**Caveat:** PP3 cannot be applied if using the PVS1 criterion for splice site variants in position +/- 1/2.

---

### PP4 - Phenotype Specificity

**Original ACMG Summary:** Patient's phenotype or family history is highly specific for a disease with a single genetic etiology.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Supporting** | Use if patient fulfils revised Ghent criteria. Can be used if any of the family members have a highly specific phenotype. |

**Modification Type:** Disease-specific

---

### PP5 - Reputable Source

**Original ACMG Summary:** Reputable source recently reports variant as pathogenic, but the evidence is not available to the laboratory to perform an independent evaluation.

**VCEP Specifications:** *Not Applicable* - This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PMID: 29543229).

---

## Benign Criteria

### BA1 - Allele Frequency >0.1%

**Original ACMG Summary:** Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

**VCEP Specification (Stand Alone):**
- Allele frequency above **0.1%** (>0.001) in ExAC and gnomAD.
- Use the ethnic population with the highest allele frequency.
- **Caveat:** Do not use Finnish, Ashkenazi Jewish, or "Other" populations in gnomAD.
- Minimum amount of studied alleles should be 2000.

---

### BS1 - Frequency Greater Than Expected

**Original ACMG Summary:** Allele frequency is greater than expected for disorder.

**VCEP Specification (Strong):**
- Allele frequency greater than expected for disease: **>0.005%** (>5.0E-5).
- Use the ethnic population with the highest allele frequency.
- **Caveat:** Do not use Finnish, Ashkenazi Jewish, or "Other" populations in gnomAD.
- Minimum amount of studied alleles should be 2000.

---

### BS2 - Observed in Healthy Adult

**Original ACMG Summary:** Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

**VCEP Specifications:** *Not Applicable*

---

### BS3 - Functional Studies (No Effect)

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

**VCEP Specifications:**
- See PS3 for guidelines on appropriate functional studies.
- Same approved and non-approved functional assays apply.

| Strength | Criteria |
|----------|----------|
| **Strong** | Follow the Functional Assay SVI Documentation showing no damaging effect. |

**Modification Type:** None

---

### BS4 - Lack of Segregation

**Original ACMG Summary:** Lack of segregation in affected members of a family.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | Applicable as described. Caution is warranted when the phenotype is not highly specific. Lack of segregation should then be clear in >1 affected family member. |

**Modification Type:** None

---

### BP1-BP7 - Benign Supporting

| Criterion | Status | Specification |
|-----------|--------|---------------|
| **BP1** | *Not Applicable* | Missense variant in gene where only LOF causes disease - not applicable to FBN1. |
| **BP2** | Supporting (Disease-specific) | Observed in trans in multiple cases (+2) with co-occurring pathogenic variants and phenotype is not more severe than when seen in isolation. Observed in cis with a pathogenic variant, if the pathogenic variant has been seen in isolation in a patient with the disease phenotype. |
| **BP3** | *Not Applicable* | In-frame deletions/insertions in a repetitive region without a known function - not applicable to FBN1. |
| **BP4** | Supporting (Disease-specific) | Recommended prediction program for missense variants: REVEL, use **0.326** as discriminatory cut-off value. Recommended prediction programs for splice variants: GeneSplicer, MaxEntScan, and NNSPLICE. The outcome of all 3 prediction programs need to be in concordance. |
| **BP5** | Supporting (None) | Variant found in a case with an alternate molecular basis for disease. Applicable as described. |
| **BP6** | *Not Applicable* | This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PMID: 29543229). |
| **BP7** | Supporting (None) | A synonymous (silent) variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved. Applicable as described. |

---

## Rules for Combining Criteria

### Criteria Strength Categories

| Category | Applicable Criteria |
|----------|-------------------|
| **Pathogenic Very Strong** | PVS1, PS2_very strong, PM6_very strong |
| **Pathogenic Strong** | PS1, PS2, PS3, PS4, PVS1_strong, PM1_strong, PM6_strong, PP1_strong |
| **Pathogenic Moderate** | PM1, PM4, PM5, PM6, PVS1_moderate, PS2_moderate, PS3_moderate, PS4_moderate, PP1_moderate |
| **Pathogenic Supporting** | PP1, PP2, PP3, PP4, PVS1_supportive, PS2_supportive, PS3_supportive, PS4_supportive, PM2_supportive, PM6_supportive |
| **Benign Stand Alone** | BA1 |
| **Benign Strong** | BS1, BS3, BS4 |
| **Benign Supporting** | BP2, BP4, BP5, BP7 |

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
| 1 Very Strong **AND** PM2_supportive |
| 1 Strong **AND** 1-2 Moderate |
| 1 Strong **AND** >=2 Supporting |
| >=3 Moderate |
| 2 Moderate **AND** >=2 Supporting |
| 1 Moderate **AND** >=4 Supporting |

### Benign Classification

| Criteria Combination |
|---------------------|
| 1 Stand-Alone (BA1) |
| >=2 Strong |

### Likely Benign Classification

| Criteria Combination |
|---------------------|
| 1 Strong **AND** 1 Supporting |
| >=2 Supporting |

---

## Appendices

### Appendix A: PVS1 Flowchart

The FBN1 VCEP has simplified the PVS1 flowchart based on those arguments which only apply to FBN1. The biological relevant FBN1 transcript is **NM_000138**.

#### Nonsense or Frameshift Variants

```
Predicted to undergo NMD --> PVS1
Not predicted to undergo NMD:
  |-- Truncated/altered region is critical to protein function --> PVS1_strong
  |-- Role of region in protein is unknown:
       |-- Removes >10% protein --> PVS1_strong
       |-- Removes <10% protein --> PVS1_moderate
```

#### 1,2 Splice Site Variants (GT->AG)

```
Disrupts reading frame and predicted to undergo NMD --> PVS1
Full gene deletion --> PVS1
Disrupts reading frame and NOT predicted to undergo NMD:
  |-- Truncated/altered region is critical to protein function --> PVS1_strong
  |-- Role of region in protein is unknown:
       |-- Removes >10% protein --> PVS1_strong
       |-- Removes <10% protein --> PVS1_moderate
Preserves reading frame:
  |-- Truncated/altered region is critical to protein function --> PVS1_strong
```

#### Deletions (Single Exon to Full Gene)

```
Disrupts reading frame and predicted to undergo NMD --> PVS1
Disrupts reading frame and NOT predicted to undergo NMD:
  |-- Truncated/altered region is critical to protein function --> PVS1_strong
  |-- Role of region in protein is unknown:
       |-- Removes >10% protein --> PVS1_strong
       |-- Removes <10% protein --> PVS1_moderate
Preserves reading frame:
  |-- Truncated/altered region is critical to protein function --> PVS1_strong
```

#### Duplications (>=1 Exon, Completely Contained Within Gene)

```
Proven in tandem:
  |-- Disrupts reading frame and predicted to undergo NMD --> PVS1
  |-- Unknown impact on reading frame and NMD --> N/A
Presumed in tandem:
  |-- Disrupts reading frame and NOT predicted to undergo NMD --> PVS1_strong
Proven NOT in tandem --> N/A
```

#### Initiation Codon Variants

```
Initiation codon variant --> PVS1_moderate
(with 1 or more pathogenic variant(s) upstream of closest potential in-frame start codon)
```

---

### Appendix B: PM1 Domain Residues Summary

The FBN1 VCEP provided detailed lists of residues for PM1_strong and PM1 consideration. Residue tables are available in the supplemental material of the ClinGen specification document.

#### PM1_Strong Residues (Cysteine Residues in cbEGF-like Domains)

Substitution of cysteine residues in cbEGF-like domains is considered very likely to be pathogenic given literature-based evidence. These include 258 cysteine residues across cbEGF1 through cbEGF43 (exons 7-64), all involved in disulfide bonds with potential impact of folding defect.

**Domains covered:** cbEGF1-cbEGF43 (6 Cys residues per domain)

#### PM1 (Moderate) Residues

The following domain types and residue categories qualify for PM1 at moderate strength:

| Domain Type | Residues | Structure Analysis |
|------------|----------|-------------------|
| **EGF-like domains** (EGF1-EGF3) | Cysteine residues (exons 2-5) | Disulfide bond / folding defect |
| **Hybrid domains** (Hyb1, Hyb2) | Cysteine residues (exons 5-6, 21-22) | Disulfide bond / folding defect |
| **TB domains** (TB1-TB7) | Cysteine residues (exons 9-10, 16-17, 24, 37-38, 41-42, 50-51, 57) | Disulfide bond / folding defect |
| **cbEGF-like domains** | Critical Gly between Cys2-Cys3 and Gly between Cys3-Cys4 (if upstream cbEGF domain exists) | Interdomain packaging / folding defect |
| **cbEGF-like domains** | (D/N)-X-(D/N)-(E/Q)-Xm-(D/N)-Xn-(Y/F) consensus residues | Calcium binding / folding defect |
| **Any domain** | Cys-creating variants | Disulfide bond / folding defect |

---

### Appendix C: Population Frequency Thresholds Summary

| Criterion | Threshold | Strength | Population Notes |
|-----------|-----------|----------|-----------------|
| BA1 | >0.1% (>0.001) | Stand Alone | Highest ethnic popmax; exclude FIN, ASJ, OTH; min 2000 alleles |
| BS1 | >0.005% (>5.0E-5) | Strong | Highest ethnic popmax; exclude FIN, ASJ, OTH; min 2000 alleles |
| PM2 | <0.0005% (<5.0E-6) | Supporting | Highest ethnic popmax; exclude FIN, ASJ, OTH; min 2000 alleles |

---

### Appendix D: Computational Prediction Tool Thresholds

| Tool | Variant Type | Pathogenic Threshold (PP3) | Benign Threshold (BP4) |
|------|-------------|--------------------------|----------------------|
| **REVEL** | Missense | >= 0.75 | <= 0.326 |
| **GeneSplicer** | Splice | Concordance required | Concordance required |
| **MaxEntScan** | Splice | Concordance required | Concordance required |
| **NNSPLICE** | Splice | Concordance required | Concordance required |

**Note:** For splice variants, the outcome of all 3 prediction programs need to be in concordance for both PP3 and BP4.

---

### Appendix E: PS2/PM6 Phenotypic Definitions

| Phenotype Category | Clinical Definition |
|-------------------|-------------------|
| **Highly specific for disease** | TAAD + ectopia lentis |
| **Consistent with gene but not highly specific** | TAAD + systemic score >=7 |
| **Consistent but genetic heterogeneity** | (Isolated) TAAD, isolated ectopia lentis, and in case of a child (age <20yrs) systemic score >=7 in whom TAAD is progressive and can be developed later in life |

**Recommendation:** The EP recommends that the parents had a full clinical work-up and an echocardiogram to exclude MFS/HTAAD.

---

### Appendix F: Criteria Not Applicable for FBN1

| Criterion | Reason |
|-----------|--------|
| PM3 | Marfan syndrome is autosomal dominant; in trans testing not applicable |
| BS2 | Not applicable for FBN1 |
| BP1 | FBN1 is not a gene where only LOF causes disease |
| BP3 | Not applicable for FBN1 |
| PP5 | Not for use per ClinGen SVI recommendation (PMID: 29543229) |
| BP6 | Not for use per ClinGen SVI recommendation (PMID: 29543229) |

---

### Appendix G: Reference PMIDs

| PMID | Context |
|------|---------|
| 29543229 | ClinGen SVI recommendation for PP5/BP6 deprecation |

---

## Version History

| Version | Date | Description |
|---------|------|-------------|
| 1.0.0 | January 4, 2022 | Initial release of FBN1 VCEP specifications |

---

*This document was compiled from ClinGen FBN1 VCEP specifications (ClinGen_FBN1_ACMG_Specifications_v1). For the most current version, please refer to the [ClinGen website](https://www.clinicalgenome.org/affiliation/50046/docs/assertion-criteria).*
