# ClinGen Severe Combined Immunodeficiency Disease VCEP Variant Interpretation Guidelines for RAG1

**Version:** 2.1.0
**Released:** 10/1/2025
**Affiliation:** Severe Combined Immunodeficiency Disease VCEP
**Based on:** Richards et al., 2015 ACMG/AMP Guidelines

---

## Gene Information

| Attribute | Value |
|-----------|-------|
| **Gene** | RAG1 (HGNC:9831) |
| **HGNC Name** | recombination activating 1 |
| **Transcript** | NM_000448.3 |
| **Disease** | recombinase activating gene 1 deficiency (MONDO:0000572) |
| **Inheritance** | Autosomal recessive inheritance |

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

Caveats:
- Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7).
- Use caution interpreting LOF variants at the extreme 3' end of a gene.
- Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact.
- Use caution in the presence of multiple transcripts.

**VCEP Specifications:**

Use ClinGen SVI recommendations for loss of function criterion (Tayoun et al., 2018 (PMID: 30192042)) with two modifications:

- Given that the *RAG1* protein is encoded by a single exon (based on MANE Select transcript NM_000448.3) and nonsense-mediated decay is not predicted for nonsense or frameshift variants, PVS1 cannot be applied at the default strength to RAG1 variants (indicated by the red boxes in the attached PVS1 flowchart), **except** in the case of a full gene deletion **or** removing/altering critical domain (NBD domain, DDBD domain and core domain) (indicated by the purple boxes in attached PVS1 flowchart).
- PVS1 can be applied to variants not predicted to undergo nonsense-mediated decay but removing/altering the critical NBD domain (aa 394-460), DDBD domain (aa 461-517), and core domain (aa 387-1011) based on recommendations from Walker et al., preprint (See attached PVS1 flowchart).
- Strength modification for variants predicted to remove >10% of the protein (See attached PVS1 flowchart).
- For variants not predicted to undergo nonsense-mediated decay, at least one pathogenic variant must be present downstream in order to apply PVS1_Strong (See attached PVS1 flowchart).
- The NBD domain (aa 394-460), DDBD domain (aa 461-517) and core domain (aa 387-1011) are defined as a region critical to protein function. (PMID: 26996199).

#### Strength Levels

| Strength | Criteria |
|----------|----------|
| **Very Strong** | Use ClinGen SVI recommendations for LOF criterion (PMID: 30192042). Applicable for full gene deletion or variants removing/altering critical domains (NBD aa 394-460, DDBD aa 461-517, core aa 387-1011). PVS1 cannot be applied at default strength for nonsense/frameshift variants where NMD is not predicted (red boxes in flowchart), except when removing/altering critical domains (purple boxes). |
| **Strong** | For variants not predicted to undergo NMD but removing >10% of protein, at least one pathogenic variant **must be** present downstream in order to apply PVS1_Strong. |
| **Moderate** | For variants not predicted to undergo NMD but removing >10% of protein, when at least one pathogenic variant is **not** present downstream, downgrade to PVS1_Moderate. Also applicable when variant removes <10% of protein per flowchart. |
| **Supporting** | Per PVS1 flowchart: applicable for initiation codon variants with no pathogenic variant(s) upstream of closest potential in-frame start codon. |

#### PVS1 Decision Flowchart Summary

**Nonsense or Frameshift:**
- Predicted to undergo NMD → **Not applicable** (RAG1 is single-exon, NMD not predicted)
- Not predicted to undergo NMD:
  - Truncated/altered region is critical to protein function (NBD/DDBD/core domain) → **PVS1**
  - Role of region unknown, variant removes >10% of protein:
    - 1+ pathogenic variant present downstream → **PVS1_Strong**
    - No known downstream pathogenic variants → **PVS1_Moderate**
  - Role of region unknown, variant removes <10% of protein → **PVS1_Moderate**

**GT-AG 1,2 Splice Sites:**
- Exon skipping disrupts reading frame and predicted to undergo NMD → **Not applicable** (single exon)
- Exon skipping disrupts reading frame, NOT predicted to undergo NMD:
  - Truncated/altered region is critical (NBD/DDBD/core) → **PVS1**
  - Role unknown, removes >10%:
    - 1+ pathogenic variant downstream → **PVS1_Strong**
    - No downstream pathogenic variants → **PVS1_Moderate**
  - Role unknown, removes <10% → **PVS1_Moderate**
- Exon skipping preserves reading frame:
  - Truncated/altered region is critical (NBD/DDBD/core) → **PVS1**
  - Role unknown, removes >10%:
    - 1+ pathogenic variant within deleted region → **PVS1**
    - No known pathogenic variants within deleted region → **PVS1_Moderate**
  - Role unknown, removes <10% → **PVS1_Moderate**

**Deletion (Single exon to full gene):**
- Full gene deletion → **PVS1**
- Single to multi exon deletion disrupts reading frame, predicted to undergo NMD → **Not applicable**
- Single to multi exon deletion disrupts reading frame, NOT predicted to undergo NMD:
  - Truncated/altered region is critical (NBD/DDBD/core) → **PVS1**
  - Role unknown, removes >10%:
    - 1+ pathogenic variant within deleted region → **PVS1_Strong**
    - No known pathogenic variants within deleted region → **PVS1_Moderate**
  - Role unknown, removes <10% → **PVS1_Moderate**
- Single to multi exon deletion preserves reading frame:
  - Truncated/altered region is critical (NBD/DDBD/core) → **PVS1**
  - Role unknown, removes >10%:
    - 1+ pathogenic variant within deleted region → **PVS1**
    - No known pathogenic variants within deleted region → **PVS1_Moderate**
  - Role unknown, removes <10% → **PVS1_Moderate**

**Duplication (>=1 exon, completely contained within gene):**
- Proven in tandem, reading frame disrupted and NMD predicted → **Not applicable**
- Presumed in tandem, no or unknown impact on reading frame → **N/A**
- Presumed in tandem, reading frame presumed disrupted and NMD predicted → **PVS1_Strong**
- Proven not in tandem → **N/A**

**Initiation Codon:**
- No known alternative start codon:
  - >=1 pathogenic variant(s) upstream of closest potential in-frame start codon → **PVS1_Moderate**
  - No pathogenic variant(s) upstream → **PVS1_Supporting**
- Different functional transcript uses alternative start codon → **N/A**

---

### PS1 - Same Amino Acid Change

**Original ACMG Summary:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change. Example: Val->Leu caused by either G>C or G>T in the same codon. Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | Same amino acid change as a previously established pathogenic variant. It can also be applied for splice variants at the same nucleotide and with similar impact prediction as previously reported pathogenic variant (if the predicted impact is equal to or greater than the known pathogenic variant per *in silico* splicing tool SpliceAI). Example: c.105+1G>C is known to be pathogenic, can use PS1 for c.105+1G>T. Applicable if the previously established variant is classified as **pathogenic** by SCID VCEP specifications for *RAG1*. |
| **Moderate** | Same as above, but applicable if the previously established variant is classified as **likely pathogenic** by SCID VCEP specifications for *RAG1*. |

---

### PS2 - De Novo (Confirmed)

**Original ACMG Summary:** De novo (both maternity and paternity confirmed) in a patient with the disease and no family history. Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.

**VCEP Specifications:** Use ClinGen SVI recommendations for *de novo* criteria (PMID: PS2/PM6 v1.1) with the following gene-specific guidelines for determining phenotypic consistency of each proband:

- **"Phenotype highly specific for gene"**: proband must meet at least PP4_Moderate criteria
- **"Phenotype consistent with gene but not highly specific"**: proband must meet PP4 criteria
- **"Phenotype consistent with gene but not highly specific and high genetic heterogeneity"**: proband has been asserted to have a SCID phenotype but does not meet PP4 criteria
- Reduce points per proband by half if the phase is unconfirmed

#### PS2/PM6 Point System

| Phenotypic Consistency | Confirmed Parental Relationships | Unconfirmed Parental Relationships |
|------------------------|----------------------------------|------------------------------------|
| Phenotype highly specific for gene (meets PP4_Moderate) | 2 points | 1 point |
| Phenotype consistent but not highly specific (meets PP4) | 1 point | 0.5 points |
| Phenotype consistent + high genetic heterogeneity (SCID phenotype, does not meet PP4) | 0.5 points | 0.25 points |
| Phenotype not consistent | 0 points | 0 points |

#### Evidence Strength Thresholds

| Points | Strength Level |
|--------|----------------|
| 0.5 | Supporting (PS2_Supporting / PM6_Supporting) |
| 1.0 | Moderate (PS2_Moderate / PM6) |
| 2.0 | Strong (PS2 / PM6_Strong) |
| 4.0 | Very Strong (PS2_VeryStrong / PM6_VeryStrong) |

**Additional considerations for autosomal recessive conditions:** For a *de novo* occurrence in a gene associated with a condition inherited in an autosomal recessive pattern without an additional pathogenic/likely pathogenic variant identified, the strength of evidence should be decreased by one level.

---

### PS3 - Functional Studies

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product. Note: Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | PS3 may potentially be applied at the default strength level of strong for evidence from an **animal model** expressing the variant of interest and recapitulating the RAG1-SCID phenotype. |
| **Moderate** | The strength of evidence from cellular models/*in vitro* studies is dependent upon the abnormal result in a V(D)J recombination assay: **<25% of wild-type activity** in Lee et al., 2014 (PMID: 24290284). |
| **Supporting** | **25-60% of wild-type activity** in Lee et al., 2014 (PMID: 24290284) **OR** reduced activity compared to wild type in Corneo et al., 2001 (PMID: 11313270). |

> *At least one previously observed proband with the expressed RAG1 variant meeting PP4 is required to apply PS3 at any strength.*

#### Approved Assay Instances

**General Class of Assay:** V(D)J recombination assay

| Attribute | Corneo et al., 2001 (PMID: 11313270) | Lee et al., 2014 (PMID: 24290284) |
|-----------|---------------------------------------|-------------------------------------|
| **Approved** | Yes | Yes |
| **Proposed Strength** | PS3_Supporting | PS3_Moderate |
| **Material** | SV40-transformed fibroblasts electroporated with wild type or variant RAG1 cDNA constructs and extrachromosomal V(D)J recombination substrates | Murine Rag1-/- Abl pro-B cells with a stable single integration of the pMX-INV GFP cassette flanked by two coding recombination signal sequences |
| **Readout** | Quantitative: Number of blue colonies as a readout for recombination frequency | Quantitative: GFP expression as a readout of recombination activity (reported as % of wild-type RAG1) |
| **Positive Control** | Cells expressing wild type RAG1 | Wild type RAG1 cDNA-transduced cells |
| **Negative Control** | Not reported | Empty vector-transduced cells |
| **Abnormal Threshold** | Reduced recombination frequency compared to wild type | <25% WT activity → PS3_Moderate; 25-60% WT activity → PS3_Supporting |
| **Statistical Analysis** | Not reported | Mann-Whitney U test |
| **Validation Controls** | 0 P/LP, 0 B/LB | 0 P/LP (reported by authors), 3 B/LB (G99S, H249R, K820R); VCEP curated 11 validation controls (7 P/LP, 4 B/LB) — all correctly classified |

#### PS3 Validation Control Results (Lee et al., 2014)

| Variant | Protein Change | Classification | Mean V(D)J Activity (%) | Assay Result |
|---------|---------------|----------------|------------------------|--------------|
| c.256_257del | p.Lys86fs | Pathogenic | 2.7 | Abnormal |
| c.322C>T | p.R108X | Pathogenic | 1.8 | Abnormal |
| c.1186C>T | p.R396C | Pathogenic | 0.6 | Abnormal |
| c.1331C>T | p.A444V | Pathogenic | 1.4 | Abnormal |
| c.1303A>G | p.M435V | Pathogenic | 23.6 | Abnormal |
| c.1682G>A | p.R561H | Pathogenic | 2.0 | Abnormal |
| c.2210G>A | p.R737H | Pathogenic | 0.2 | Abnormal |
| c.295G>A | p.G99S | Benign | 113.2 | Normal |
| c.746A>G | p.H249R | Benign | 112.2 | Normal |
| c.1346G>A | p.R449K | Benign | 92.1 | Normal |
| c.2459A>G | p.K820R | Benign | 117.9 | Normal |

---

### PS4 - Prevalence in Affected

**Original ACMG Summary:** The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls. Note 1: Relative risk (RR) or odds ratio (OR), as obtained from case-control studies, is >5.0 and the confidence interval around the estimate of RR or OR does not include 1.0. Note 2: In instances of very rare variants where case-control studies may not reach statistical significance, the prior observation of the variant in multiple unrelated patients with the same phenotype, and its absence in controls, may be used as moderate level of evidence.

**VCEP Specifications:** *Not Applicable*

---

### PM1 - Mutational Hot Spot

**Original ACMG Summary:** Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.

**VCEP Specifications:** Strength is dependent upon the location of the variant within specific functional domains (PMID: 26996199):

| Strength | Criteria |
|----------|----------|
| **Moderate** | Missense variant located in the **NBD domain** (amino acids 394-460) and **DDBD domain** (amino acids 461-517). |
| **Supporting** | Missense variant located elsewhere in the **core domain** (amino acids 387-1011). |

---

### PM2 - Absent from Controls

**Original ACMG Summary:** Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium. Caveat: Population data for indels may be poorly called by next generation sequencing.

**VCEP Specification (Supporting only):**
- gnomAD popmax filtering allele frequency **<0.000102**
- An additional requirement is that **no homozygotes** have been observed in gnomAD.

---

### PM3 - In Trans with Pathogenic

**Original ACMG Summary:** For recessive disorders, detected in trans with a pathogenic variant. Note: This requires testing of parents (or offspring) to determine phase.

**VCEP Specifications:** Use ClinGen SVI adapted recommendations for *in trans* criterion (SVI PM3 v1.0) with the additional requirement that the co-occurring variant must be classified using the SCID VCEP specifications for *RAG1*.

**Caveats:**
- All variants should be sufficiently rare (meet PM2 specification).
- The applicability of PM3 to suspected founder variants with allele frequencies exceeding the PM2 threshold will be evaluated on a case-by-case basis by the VCEP.

#### PM3 Point System (Per Proband)

| Classification/Zygosity of Other Variant | Confirmed in Trans | Phase Unknown |
|------------------------------------------|-------------------|---------------|
| Pathogenic or Likely pathogenic variant | 1.0 | 0.5 (P) / 0.25 (LP) |
| Homozygous, non-consanguineous (no max) | 1.0 | 1.0 |
| Homozygous, consanguineous (max 0.5/family) | 0.5 | 0.5 |
| VUS (max 0.5 total) | 0.25 | 0.0 |

All variants should be sufficiently rare (meet PM2 specification). P = Pathogenic; LP = Likely pathogenic.

#### PM3 Evidence Strength Thresholds

| Total Points | Strength Level |
|--------------|----------------|
| 0.5 | PM3_Supporting |
| 1.0 | PM3 (Moderate) |
| 2.0 | PM3_Strong |
| 4.0 | PM3_VeryStrong |

#### PM3 Considerations

- **Allele Frequency:** Application of PM3 is contingent on the allele frequency of the variant being assessed and the variant on the other allele both being sufficiently rare (meets PM2 threshold).
- **Phasing:** If the phase cannot be determined, at least two different LP/P variants are needed to equal the weight of one LP/P co-occurrence confirmed *in trans*. If only one parent is tested and found to carry one allele, variants can be counted as *in trans*.
- **Classification:** Probands should be weighted less when the variant on the other allele is of uncertain significance. To avoid circularity, the classification of the variant on the other allele should not use evidence from the variant being interrogated.
- **Homozygous occurrences:** Default weight is 0.5 points (may be due to consanguinity). A recommended max of 1.0 points of all homozygous cases is suggested.

---

### PM4 - Protein Length Changes

**Original ACMG Summary:** Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Moderate** | When applied to deletion variants, the deleted region must contain a known **pathogenic or likely pathogenic** variant that is not predicted/observed to alter splicing. |
| **Supporting** | When applied to deletion variants, the deleted region must contain a known **VUS** variant that is not predicted/observed to alter splicing. |

---

### PM5 - Novel Missense at Same Residue

**Original ACMG Summary:** Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before. Example: Arg156His is pathogenic; now you observe Arg156Cys. Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:**

**For missense variants:**

| Strength | Criteria |
|----------|----------|
| **Moderate** | Applicable at default strength (PM5) if previously established variant is classified as **pathogenic** by SCID VCEP specifications. |
| **Supporting** | Applicable at reduced strength (PM5_Supporting) if previously established variant is classified as **likely pathogenic** by SCID VCEP specifications. |

**For nonsense variants (point-based system):**

| Strength | Criteria |
|----------|----------|
| **Strong** | Nonsense variant with **4+ points** from informative variants. PM5_Strong should be **downgraded to PM5_Moderate** if PVS1 is applied at any strength. |
| **Moderate** | Nonsense variant with **2+ points** from informative variants. PM5_Moderate may **not** be combined with PVS1_VeryStrong (should be downgraded to PM5_Supporting if PVS1_VeryStrong is applied). |
| **Supporting** | Nonsense variant with **1 point** from an informative variant. Informative variants must also be classified by the SCID VCEP rule specifications. |

#### PM5 Nonsense Variant Point Table

| Type of Variant Under Assessment (VUA) | Informative Variant | Score |
|-----------------------------------------|---------------------|-------|
| Nonsense variant predicted to lead to NMD | P/LP variant in the exon of DNA change predicted to lead to NMD | +1 pt |
| Nonsense variant predicted to lead to NMD | B/LB variant in the exon predicted to lead to NMD | -2 pt |
| Nonsense variant, resulting in a PTC in the final exon, not predicted to lead to NMD | P/LP variant resulting in a PTC in the same exon but **downstream** of VUA | +1 pt |
| Nonsense variant, resulting in a PTC in the final exon, not predicted to lead to NMD | B/LB variant resulting in PTC in the same exon but **upstream** of the VUA | -2 pt |

NMD = nonsense-mediated decay; PTC = premature termination codon

**Notes:**
- The informative variant must be classified by the SCID VCEP specifications and may not be the same variant used to meet "+1 pathogenic variant downstream" on the PVS1 flowchart.
- If negative points are calculated, the curator should not apply PM5 and should reconsider if PVS1 is applicable for the VUA.
- The VUA must be sufficiently rare (meet PM2_Supporting) to apply this point system.
- If the informative variant is a frameshift or nonsense variant, it must reach classification as Pathogenic or Likely Pathogenic without use of PM5 and without use of only PVS1 plus PM2.

---

### PM6 - De Novo (Assumed)

**Original ACMG Summary:** Assumed de novo, but without confirmation of paternity and maternity.

**VCEP Specifications:** Same as PS2 — use the point-based system above. See [PS2 - De Novo (Confirmed)](#ps2---de-novo-confirmed).

The following guidelines should be used when determining the phenotypic consistency of each proband:
- **"Phenotype highly specific for gene"**: proband must meet at least PP4_Moderate criteria
- **"Phenotype consistent with gene but not highly specific"**: proband must meet PP4 criteria
- **"Phenotype consistent with gene but not highly specific and high genetic heterogeneity"**: proband has been asserted to have a SCID phenotype but does not meet PP4 criteria
- Reduce points per proband by half if the phase is unconfirmed

---

### PP1 - Co-segregation

**Original ACMG Summary:** Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease. Note: May be used as stronger evidence with increasing segregation data.

**VCEP Specifications:** Use ClinGen SVI recommendations for co-segregation criterion (PMID: 30311386) with the additional specification that unaffected individuals contributing to the calculated LOD score must be heterozygous carriers of one of the variants observed in the affected individuals (i.e., do not count wild-type/wild-type individuals).

#### PP1 Thresholds

| Strength | Likelihood | LOD Score |
|----------|------------|-----------|
| Supporting | 4:1 | 0.6 |
| Moderate | 16:1 | 1.2 |
| Strong | 32:1 | 1.5 |

#### Autosomal Recessive Segregation Table (LOD Scores)

Affected segregations are counted in rows and unaffected recessive segregations in columns. Affected segregations are affected family members in whom biallelic compound heterozygous or homozygous variants segregate. Unaffected segregations are unaffected family members (typically siblings) who are at risk to inherit the two variants identified in the proband. These individuals should be either wild-type for both variants or a heterozygous carrier for a single variant. Unaffected carrier parents DO NOT count as unaffected segregations.

| Affected \ Unaffected | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|----------------------|------|------|------|------|------|------|------|------|------|------|------|
| **0** | 0 | 0.12 | 0.25 | 0.37 | 0.5 | 0.62 | 0.75 | 0.87 | 1 | 1.12 | 1.25 |
| **1** | 0.6 | 0.73 | 0.85 | 0.98 | 1.1 | 1.23 | 1.35 | 1.48 | 1.6 | 1.73 | 1.85 |
| **2** | 1.2 | 1.33 | 1.45 | 1.58 | 1.7 | 1.83 | 1.95 | 2.08 | 2.2 | 2.33 | 2.45 |
| **3** | 1.81 | 1.93 | 2.06 | 2.18 | 2.31 | 2.43 | 2.56 | 2.68 | 2.81 | 2.93 | 3.06 |
| **4** | 2.41 | 2.53 | 2.66 | 2.78 | 2.91 | 3.03 | 3.16 | 3.28 | 3.41 | 3.53 | 3.66 |
| **5** | 3.01 | 3.14 | 3.26 | 3.39 | 3.51 | 3.63 | 3.76 | 3.88 | 4.01 | 4.13 | 4.26 |
| **6** | 3.61 | 3.74 | 3.86 | 3.99 | 4.11 | 4.24 | 4.36 | 4.49 | 4.61 | 4.74 | 4.86 |
| **7** | 4.21 | 4.34 | 4.46 | 4.59 | 4.71 | 4.84 | 4.96 | 5.09 | 5.21 | 5.34 | 5.46 |
| **8** | 4.82 | 4.94 | 5.07 | 5.19 | 5.32 | 5.44 | 5.57 | 5.69 | 5.82 | 5.94 | 6.07 |
| **9** | 5.42 | 5.54 | 5.67 | 5.79 | 5.92 | 6.04 | 6.17 | 6.29 | 6.42 | 6.54 | 6.67 |
| **10** | 6.02 | 6.15 | 6.27 | 6.4 | 6.52 | 6.65 | 6.77 | 6.9 | 7.02 | 7.15 | 7.27 |

---

### PP2 - Missense in Constrained Gene

**Original ACMG Summary:** Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.

**VCEP Specifications:** *Not Applicable*

Comments: Does not apply. The gnomAD v2.1.1 missense Z score for RAG1 (Z = 0.58) suggests this gene is not constrained for missense variation. Both benign and pathogenic missense variants are present in RAG1.

---

### PP3 - Computational Evidence

**Original ACMG Summary:** Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.). Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Supporting** | Only applicable to **synonymous or intronic variants** predicted to impact splicing by SpliceAI with a delta score **>=0.2**. **Do not apply to missense variants.** |

---

### PP4 - Phenotype Specificity

**Original ACMG Summary:** Patient's phenotype or family history is highly specific for a disease with a single genetic etiology.

**VCEP Specifications:** PP4 applicability and strength is determined by the total points accumulated by a single affected individual according to the table below and the following total point ranges:

#### PP4 Strength Thresholds

| Total Points | Strength |
|--------------|----------|
| <1 | PP4 not met |
| 1 to <2 | PP4 (Supporting) |
| 2 to <4 | PP4_Moderate |
| >=4 | PP4_Strong |

> Note: CNV (Copy number variation) testing is required to consider PP4_Strong in order to certify that the variant in question is the causative for the phenotype and not one CNV event corrected by gene therapy and not identified previously.

#### PP4 Point System

| Evidence Description | Points |
|---------------------|--------|
| Diagnostic criteria met for SCID (Criteria 1 and 3 or Criterion 4 by itself) or Leaky SCID/Omenn syndrome (excluding Criterion 2). The diagnostic criteria should follow the PIDTC 2022 specification. | 0.5 |
| SCID gene panel or exome/genome sequencing conducted (only applicable if genetic testing did not provide an alternative genetic explanation for SCID/Leaky SCID/Omenn syndrome phenotype) | 1 |
| Family history of SCID (only applicable if SCID gene panel or exome/genome sequencing was conducted on proband and did not provide an alternative genetic explanation for phenotype) | 0.5 |
| Decreased presence of TCRVα7.2 (<2%) in CD3+ T lymphocytes and/or mucosa-associated invariant T-cells demonstrated by flow cytometry **AND** pathogenic or likely pathogenic variants in RAG2 and DCLRE1C **have been excluded** (PMID: 39792639) | 1.5 |
| Decreased presence of TCRVα7.2 (<2%) in CD3+ T lymphocytes and/or mucosa-associated invariant T-cells demonstrated by flow cytometry **AND** pathogenic or likely pathogenic variants in RAG2 and DCLRE1C have **NOT** been excluded (PMID: 39792639) | 0.5 |
| Increased presence of 9G4+ (>10%), 9G4int (>5%) or 9G4hi (>5%) cells in CD19+ B cells demonstrated by flow cytometry **AND** pathogenic or likely pathogenic variants in RAG2 **have been excluded** (PMID: 39792639) | 1 |
| Increased presence of 9G4+ (>10%), 9G4int (>5%) or 9G4hi (>5%) cells in CD19+ B cells demonstrated by flow cytometry **AND** pathogenic or likely pathogenic variants in RAG2 have **NOT** been excluded (PMID: 39792639) | 0.5 |
| SCID phenotype corrected by RAG1 gene therapy | 4 |
| T-B-NK+ lymphocyte subset profile* (See notes) | 0.5 |

**Notes:**
1. If NK cells are not noted or are present, criteria may still be applied if SCID gene panel or exome/genome sequencing has ruled out alternative causes.
2. If maternal T cells are present, the T lymphocyte profile is still considered to be T- (autologous T cells are absent).

---

### PP5 - Reputable Source

**Original ACMG Summary:** Reputable source recently reports variant as pathogenic, but the evidence is not available to the laboratory to perform an independent evaluation.

**VCEP Specifications:** *Not Applicable*

This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee. (PMID: 29543229)

---

## Benign Criteria

### BA1 - Allele Frequency >5%

**Original ACMG Summary:** Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

**VCEP Specifications:** Maximum credible population allele frequency threshold determined using Whiffin/Ware calculator with the following parameters:
- Prevalence: 1:5,000
- Allelic heterogeneity: 1
- Genetic heterogeneity: 0.19 (based on the contribution of *RAG1* variants to total SCID in the PIDTC 6901 cohort reported in Dvorak et al., 2019 (PMID: 30193840, Table 1): 19.2% rounded to 19%)
- Penetrance: 50%

**VCEP Specification (Stand Alone):**
- gnomAD popmax filtering allele frequency **>0.00872**

---

### BS1 - Frequency Greater Than Expected

**Original ACMG Summary:** Allele frequency is greater than expected for disorder.

**VCEP Specifications:** Maximum credible population allele frequency threshold determined using Whiffin/Ware calculator with the following parameters:
- Prevalence: 1:50,000
- Allelic heterogeneity: 1
- Genetic heterogeneity: 0.19 (based on the contribution of *RAG1* variants to total SCID in the PIDTC 6901 cohort reported in Dvorak et al., 2019 (PMID: 30193840, Table 1): 19.2% rounded to 19%)
- Penetrance: 100%

**VCEP Specification (Strong):**
- gnomAD popmax filtering allele frequency **>0.00195**
- Consider also bottleneck populations.

---

### BS2 - Observed in Healthy Adult

**Original ACMG Summary:** Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Supporting** | Only to be used when the variant is observed in the **homozygous state** in a healthy adult. |

---

### BS3 - Functional Studies (No Effect)

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

**VCEP Specifications:** *Not Applicable*

Comments: There is not a well-established functional study which can rule out all damaging effects on protein function.

---

### BS4 - Lack of Segregation

**Original ACMG Summary:** Lack of segregation in affected members of a family. Caveat: The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | Can be applied without additional specifications. |

---

### BP1-BP7 - Benign Supporting

| Criterion | Status | Comment |
|-----------|--------|---------|
| **BP1** | Not Applicable | Does not apply. |
| **BP2** | Not Applicable | — |
| **BP3** | Not Applicable | Does not apply. |
| **BP4** | Not Applicable | — |
| **BP5** | Not Applicable | — |
| **BP6** | Not Applicable | This criterion is not for use as recommended by the ClinGen SVI VCEP Review Committee. (PMID: 29543229) |
| **BP7** | Applicable (Supporting) | Applicable to both synonymous variants and deep intronic variants affecting nucleotides at or beyond the +7 (donor) and -21 (acceptor) positions. The variant should be predicted not to impact splicing by at least two out of three *in silico* tools (freely available tools include GeneSplicer, MaxEntScan, NNSplice, SpliceAI, Splicing Sequences Finder (SSF), and varSEAK). Given the potential for poor conservation of genes related to T cell and B cell development among vertebrates, nucleotide conservation is **not required** in order to apply BP7. |

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
| 1 Strong **AND** 2 Moderate |

### Benign Classification

| Criteria Combination |
|---------------------|
| >=2 Strong |
| 1 Stand Alone (BA1) |

### Likely Benign Classification

| Criteria Combination |
|---------------------|
| 1 Strong (BS1, BS4) |
| >=2 Supporting (BS2_Supporting, BP7) |

---

## Appendices

### Appendix A: PVS1 Flowchart

See attached document: "PVS1: Specified PVS1 flowchart" for the complete decision tree.

**Key RAG1-specific modifications to the standard PVS1 flowchart:**
- Red boxes indicate where PVS1 **cannot** be applied at default strength for RAG1 (because RAG1 is encoded by a single exon and NMD is not predicted for nonsense/frameshift variants).
- Purple boxes indicate where PVS1 **can** be applied when the truncated/altered region is critical to protein function (NBD domain aa 394-460, DDBD domain aa 461-517, core domain aa 387-1011).

**Critical Domains for RAG1:**

| Domain | Amino Acid Range |
|--------|-----------------|
| NBD (Nonamer Binding Domain) | 394-460 |
| DDBD (Dimerization and DNA Binding Domain) | 461-517 |
| Core Domain | 387-1011 |

### Appendix B: Reference PMIDs

| PMID | Reference | Used For |
|------|-----------|----------|
| 30192042 | Tayoun et al., 2018 | PVS1 - ClinGen SVI LOF recommendations |
| 26996199 | — | PM1, PVS1 - Critical functional domains |
| 24290284 | Lee et al., 2014 | PS3 - V(D)J recombination assay |
| 11313270 | Corneo et al., 2001 | PS3 - V(D)J recombination assay |
| 30311386 | Oza et al., 2018 | PP1 - Co-segregation criterion |
| 30193840 | Dvorak et al., 2019 | BA1, BS1 - Population frequency thresholds |
| 29543229 | — | PP5, BP6 - Criteria not for use |
| 39792639 | — | PP4 - TCRVα7.2 and 9G4+ flow cytometry biomarkers |

### Appendix C: Population Frequency Thresholds Summary

| Criterion | Threshold | Strength | Parameters |
|-----------|-----------|----------|------------|
| BA1 | >0.00872 | Stand Alone | Prevalence 1:5,000; Allelic het. 1; Genetic het. 0.19; Penetrance 50% |
| BS1 | >0.00195 | Strong | Prevalence 1:50,000; Allelic het. 1; Genetic het. 0.19; Penetrance 100% |
| PM2 | <0.000102 | Supporting | No homozygotes in gnomAD |

### Appendix D: Criteria Applicability Summary

| Criterion | Applicable? | Max Strength | Gene-Specific Modification |
|-----------|-------------|-------------|---------------------------|
| PVS1 | Yes | Very Strong | Single-exon gene; NMD not predicted; critical domains defined |
| PS1 | Yes | Strong | Must use SCID VCEP classifications; splice variant extension |
| PS2 | Yes | Very Strong | PP4-based phenotypic consistency definitions |
| PS3 | Yes | Strong | V(D)J recombination assay; requires PP4 for proband |
| PS4 | No | — | Not applicable |
| PM1 | Yes | Moderate | NBD (394-460), DDBD (461-517), core (387-1011) |
| PM2 | Yes | Supporting | <0.000102 popmax FAF; no homozygotes in gnomAD |
| PM3 | Yes | Very Strong | Co-occurring variant must use SCID VCEP classifications |
| PM4 | Yes | Moderate | Deleted region must contain known P/LP variant |
| PM5 | Yes | Strong | Missense + nonsense variant point system |
| PM6 | Yes | Very Strong | Same as PS2 point system |
| PP1 | Yes | Strong | Unaffected must be heterozygous carriers |
| PP2 | No | — | Gene not constrained for missense (Z = 0.58) |
| PP3 | Yes | Supporting | Synonymous/intronic only; SpliceAI delta >=0.2; not for missense |
| PP4 | Yes | Strong | Point-based system with SCID-specific clinical criteria |
| PP5 | No | — | Not for use per ClinGen SVI |
| BA1 | Yes | Stand Alone | >0.00872 popmax FAF |
| BS1 | Yes | Strong | >0.00195 popmax FAF |
| BS2 | Yes | Supporting | Homozygous in healthy adult only |
| BS3 | No | — | No well-established assay to rule out all effects |
| BS4 | Yes | Strong | No additional specifications |
| BP1 | No | — | Not applicable |
| BP2 | No | — | Not applicable |
| BP3 | No | — | Not applicable |
| BP4 | No | — | Not applicable |
| BP5 | No | — | Not applicable |
| BP6 | No | — | Not for use per ClinGen SVI |
| BP7 | Yes | Supporting | Synonymous + deep intronic; conservation not required |

---

## Version History

| Version | Date | Notes |
|---------|------|-------|
| 2.1.0 | 10/1/2025 | Updated: PM5_Strong, PM5_Moderate, PM5_Supporting, PM5 Instructions; PP4 attachment table updates; PP4 instructions harmonized with attached PP4 tables; Edited Likely Benign Rules for Combining Criteria (V1 had 1 strong, the change in V2 to 1 strong + 1 supporting was unintentional — reverted to 1 strong). |

---

*This document was compiled from ClinGen VCEP specifications and ClinGen SVI recommendations. For the most current version, please refer to the ClinGen website.*
