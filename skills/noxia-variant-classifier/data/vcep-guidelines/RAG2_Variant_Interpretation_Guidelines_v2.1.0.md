# ClinGen Severe Combined Immunodeficiency Disease VCEP Variant Interpretation Guidelines for RAG2

**Version:** 2.1.0
**Released:** 10/1/2025
**Affiliation:** Severe Combined Immunodeficiency Disease VCEP
**Based on:** Richards et al., 2015 ACMG/AMP Guidelines

**Release Notes:** Edited Likely Benign Rules for Combining Criteria. V1 had 1 strong, the change in V2 to 1 strong + 1 supporting was unintentional.

---

## Gene Information

| Attribute | Value |
|-----------|-------|
| **Gene** | RAG2 (HGNC:9832) |
| **HGNC Name** | recombination activating 2 |
| **Transcript** | NM_000536.4 |
| **Disease** | recombinase activating gene 2 deficiency (MONDO:0000573) |
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

- Given that the *RAG2* protein is encoded by a single exon (based on MANE Select transcript NM_000536.4) and nonsense-mediated decay is not predicted for nonsense or frameshift variants, PVS1 cannot be applied at the default strength to RAG2 variants (indicated by the red boxes in the attached flowchart), **except** in the case of a full gene deletion **or** removing/altering critical domain (PHD domain **and** core domain) (indicated by the purple boxes in the attached flowchart).
- PVS1 can be applied to variants not predicted to undergo nonsense-mediated decay but removing/altering the critical PHD domain (spanning amino acids 414-487) and core domain (amino acids 1-383) based on recommendations from Walker et al., preprint (see attached flowchart).
- Strength modification for variants predicted to remove >10% of the protein (see attached flowchart).
- For variants not predicted to undergo nonsense-mediated decay, at least one pathogenic variant must be present downstream in order to apply PVS1_Strong.
- The PHD domain (spanning amino acids 414-487) is defined as a region critical to protein function (PMID: 15964836).

#### Strength Levels

| Strength | Criteria |
|----------|----------|
| **Very Strong** | Use ClinGen SVI recommendations (PMID: 30192042) with two specifications: (1) PVS1 cannot be applied at the default strength to RAG2 variants where NMD is not predicted, **except** for full gene deletion or removing/altering critical domain (PHD domain and core domain); (2) PVS1 can be applied to variants not predicted to undergo NMD when removing/altering the critical PHD domain (aa 414-487) and core domain (aa 1-383). |
| **Strong** | For variants not predicted to undergo NMD but removing >10% of protein, at least one pathogenic variant **must be** present downstream in order to apply PVS1_Strong. |
| **Moderate** | For variants not predicted to undergo NMD but removing >10% of protein, when at least one pathogenic variant is **not** present downstream, downgrade to PVS1_Moderate. |
| **Supporting** | Per SVI flowchart — initiation codon variants with no pathogenic variant(s) upstream of closest potential in-frame start codon. |

#### PVS1 Flowchart Decision Tree (RAG2-Specific)

**Nonsense or Frameshift:**
- Predicted to undergo NMD → Exon present in biologically-relevant transcript(s) → **PVS1** *(Not applicable to RAG2 — single exon gene, NMD not predicted)*
- Not predicted to undergo NMD:
  - Truncated/altered region is critical to protein function (PHD domain aa 414-487 AND core domain aa 1-383) → **PVS1**
  - Role of region in protein function is unknown:
    - LoF variants frequent in general population and/or exon absent → **N/A**
    - Variant removes >10% of protein:
      - 1+ pathogenic variant present downstream → **PVS1_Strong**
      - No known downstream pathogenic variants → **PVS1_Moderate**
    - Variant removes <10% of protein → **PVS1_Moderate**

**GT-AG 1,2 Splice Sites:**
- Exon skipping or cryptic splice site disrupts reading frame and predicted to undergo NMD → **PVS1** *(red box — not applicable for RAG2)*
- Exon skipping or cryptic splice site disrupts reading frame and NOT predicted to undergo NMD:
  - Truncated/altered region critical to protein function → **PVS1**
  - Role unknown:
    - Variant removes >10% of protein:
      - 1+ pathogenic variant downstream → **PVS1_Strong**
      - No downstream pathogenic variants → **PVS1_Moderate**
    - Variant removes <10% of protein → **PVS1_Moderate**
- Exon skipping or cryptic splice site preserves reading frame:
  - Truncated/altered region critical to protein function → **PVS1**
  - Role unknown:
    - Variant removes >10% of protein:
      - 1+ pathogenic variant within deleted region → **PVS1_Strong**
      - No known pathogenic variants within deleted region → **PVS1_Moderate**
    - Variant removes <10% of protein → **PVS1_Moderate**

**Deletion (Single Exon to Full Gene):**
- Full gene deletion → **PVS1**
- Single to multi exon deletion disrupts reading frame and predicted to undergo NMD → **PVS1** *(red box — not applicable for RAG2)*
- Single to multi exon deletion disrupts reading frame and NOT predicted to undergo NMD:
  - Truncated/altered region critical to protein function → **PVS1**
  - Role unknown:
    - Variant removes >10%:
      - 1+ pathogenic variant within deleted region → **PVS1_Strong**
      - No known pathogenic variants → **PVS1_Moderate**
    - Variant removes <10% → **PVS1_Moderate**
- Preserves reading frame:
  - Truncated/altered region critical → **PVS1**
  - Role unknown: Same as above pattern

**Duplication (≥1 exon, completely contained within gene):**
- Proven in tandem → Reading frame disrupted and NMD predicted → **PVS1** *(red box)*
- Proven in tandem → No/unknown impact on reading frame and NMD → **N/A**
- Presumed in tandem → Reading frame presumed disrupted and NMD predicted → **PVS1_Strong**
- Proven not in tandem → **N/A**

**Initiation Codon:**
- No known alternative start codon:
  - ≥1 pathogenic variant(s) upstream of closest potential in-frame start codon → **PVS1_Moderate**
  - No pathogenic variant(s) upstream → **PVS1_Supporting**
- Different functional transcript uses alternative start codon → **N/A**

> **Key:** Red boxes (marked with X) = PVS1 at default strength NOT applicable to RAG2 (NMD not predicted in single-exon gene). Purple boxes = PVS1 applicable when critical domains (PHD + core) are affected.

---

### PS1 - Same Amino Acid Change

**Original ACMG Summary:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.

Example: Val->Leu caused by either G>C or G>T in the same codon.

Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | Same amino acid change as a previously established **pathogenic** variant (classified by SCID VCEP specifications for *RAG2*). Also applicable to splice variants at the same nucleotide with similar or greater impact prediction per SpliceAI. Example: c.105+1G>C is known to be pathogenic; can use PS1 for c.105+1G>T. |
| **Moderate** | Same amino acid change as a previously established **likely pathogenic** variant (classified by SCID VCEP specifications for *RAG2*). Also applicable to splice variants at the same nucleotide with similar or greater impact prediction per SpliceAI. Example: c.105+1G>C is known to be likely pathogenic; can use PS1 for c.105+1G>T. |

---

### PS2 - De Novo (Confirmed)

**Original ACMG Summary:** De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.

Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.

**VCEP Specifications:**

Use ClinGen SVI recommendations for *de novo* criteria (Version 1.1) with the following guidelines for determining phenotypic consistency of each proband:

- **"Phenotype highly specific for gene"**: proband must meet at least **PP4_Moderate** criteria
- **"Phenotype consistent with gene but not highly specific"**: proband must meet **PP4** criteria
- **"Phenotype consistent with gene but not highly specific and high genetic heterogeneity"**: proband has been asserted to have a SCID phenotype but does **not** meet PP4 criteria
- Reduce points per proband by half if the phase is unconfirmed

#### PS2/PM6 Point System (Per Proband)

| Phenotypic Consistency | Confirmed Parental Relationships | Unconfirmed Parental Relationships |
|------------------------|----------------------------------|------------------------------------|
| Phenotype highly specific for gene (meets PP4_Moderate) | 2 points | 1 point |
| Phenotype consistent but not highly specific (meets PP4) | 1 point | 0.5 points |
| Phenotype consistent + high genetic heterogeneity (does not meet PP4) | 0.5 points | 0.25 points |
| Phenotype not consistent with gene | 0 points | 0 points |

*Note: Maximum allowable value of 1 may contribute to overall score for the "high genetic heterogeneity" category.*

#### PS2/PM6 Evidence Strength Thresholds

| Total Points | Strength Level |
|--------------|----------------|
| 0.5 | PS2_Supporting / PM6_Supporting |
| 1.0 | PS2_Moderate / PM6 (Moderate) |
| 2.0 | PS2 (Strong) / PM6_Strong |
| 4.0 | PS2_VeryStrong / PM6_VeryStrong |

#### Additional Considerations for De Novo Criteria:
- **Autosomal recessive conditions**: For a *de novo* occurrence in a gene associated with an autosomal recessive condition without an additional pathogenic/likely pathogenic variant identified, the strength of evidence should be decreased by one level.
- **Mosaicism**: For cases with apparent germline mosaicism (multiple affected siblings with both parents negative for the variant), parental relationships must be confirmed in order for *de novo* criteria to apply.

---

### PS3 - Functional Studies

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.

Note: Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | PS3 may potentially be applied at the default strength level of strong for evidence from an **animal model** expressing the variant of interest and recapitulating the RAG2-SCID phenotype. |
| **Moderate** | Abnormal result in V(D)J recombination assay: **<25% of wild-type activity** in Tirosh et al., 2019 (PMID: 29772310). At least one previously observed proband with the expressed RAG2 variant meeting PP4 is required. |
| **Supporting** | Abnormal result in V(D)J recombination assay: **25-60% of wild-type activity** in Tirosh et al., 2019 (PMID: 29772310) **OR** reduced activity compared to wild type in Couëdel et al., 2010 (PMID: 20234091). At least one previously observed proband with the expressed RAG2 variant meeting PP4 is required. |

> **Important:** At least one previously observed proband with the expressed RAG2 variant meeting PP4 is required to apply PS3 at any strength.

#### Approved Assay Instances

| Assay | PMID | Approved | Proposed Strength | Readout | Description |
|-------|------|----------|-------------------|---------|-------------|
| **V(D)J recombination assay** (Couëdel et al., 2010) | 20234091 | Yes | PS3_Supporting | Semi-quantitative | Retrovirally transduced murine Rag2-/- pro-B cells expressing wild type or variant Rag2 proteins. Genomic DNA extracted 8-12 days post-transduction, PCR amplification of endogenous Ig rearrangement sequences analyzed by Southern blot for IgH D-to-J, V-to-DJ, and IgL Vκ-to-Jκ rearrangements. |
| **V(D)J recombination assay** (Tirosh et al., 2019) | 29772310 | Yes | PS3_Moderate | Quantitative | Murine Rag2-/- Abl pro-B cells transduced with retroviral vector containing human RAG2 cDNA, blocked in G0/G1 for 96 hours. GFP expression measured by flow cytometry as readout of recombination activity (% of wild-type). |
| Cellular localization assay (Couëdel et al., 2010) | 20234091 | No | — | Semi-quantitative | Western blotting of fractionated cytoplasmic/nuclear extracts. |
| Histone interaction assay (Couëdel et al., 2010) | 20234091 | No | — | Semi-quantitative | Anti-Flag coimmunoprecipitations analyzed for acetylated histone H3 and H4. |

#### Tirosh et al., 2019 V(D)J Recombination Assay – Validation Controls

| Variant | Protein Change | Classification | Mean V(D)J Activity (%) | Result | Control Type |
|---------|---------------|----------------|------------------------|--------|-------------|
| c.46C>T | p.Gln16Ter | Likely Pathogenic | 1.7 | Abnormal | Known Pathogenic |
| c.104G>C | p.Gly35Ala | Likely Pathogenic | 22.1 | Abnormal | Known Pathogenic |
| c.379A>T | p.Lys127Ter | Likely Pathogenic | 0.1 | Abnormal | Known Pathogenic |
| c.644C>T | p.Thr215Ile | Benign | 67.2 | Normal | Known Benign |
| c.686G>A | p.Arg229Gln | Pathogenic | 8.9 | Abnormal | Known Pathogenic |
| c.921G>A | p.Trp307Ter | Likely Pathogenic | 0.2 | Abnormal | Known Pathogenic |
| c.1158C>A | p.Phe386Leu | Benign | 109.1 | Normal | Known Benign |
| c.1219G>T | p.Glu407Ter | Likely Pathogenic | 2.9 | Abnormal | Known Pathogenic |
| c.1357T>A | p.Trp453Arg | Likely Pathogenic | 0.6 | Abnormal | Known Pathogenic |
| c.1433G>A | p.Cys478Tyr | Likely Pathogenic | 0.2 | Abnormal | Known Pathogenic |
| c.1504A>G | p.Met502Val | Benign | 99.6 | Normal | Known Benign |

---

### PS4 - Prevalence in Affected

**Original ACMG Summary:** The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.

Note 1: Relative risk (RR) or odds ratio (OR), as obtained from case-control studies, is >5.0 and the confidence interval around the estimate of RR or OR does not include 1.0.

Note 2: In instances of very rare variants where case-control studies may not reach statistical significance, the prior observation of the variant in multiple unrelated patients with the same phenotype, and its absence in controls, may be used as moderate level of evidence.

**VCEP Specifications:** *Not Applicable*

---

### PM1 - Mutational Hot Spot

**Original ACMG Summary:** Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.

**VCEP Specifications:**

Strength is dependent upon the location of the variant within specific functional domains (PMID: 26996199):

| Strength | Criteria |
|----------|----------|
| **Moderate** | Missense variant located in the **PHD domain** (amino acids 414-487) |
| **Supporting** | Missense variant located in the **core domain** (amino acids 1-383) |

---

### PM2 - Absent from Controls

**Original ACMG Summary:** Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

Caveat: Population data for indels may be poorly called by next generation sequencing.

**VCEP Specification (Supporting only):**
- gnomAD popmax filtering allele frequency **<0.0000588**
- An additional requirement is that **no homozygotes** have been observed in gnomAD.

---

### PM3 - In Trans with Pathogenic

**Original ACMG Summary:** For recessive disorders, detected in trans with a pathogenic variant.

Note: This requires testing of parents (or offspring) to determine phase.

**VCEP Specifications:**

Use ClinGen SVI adapted recommendations for *in trans* criterion (Version 1.0) with the additional requirement that the co-occurring variant must be classified using the **SCID VCEP specifications for *RAG2***.

**Caveat:** All variants should be sufficiently rare (meet PM2 specification). The applicability of PM3 to suspected founder variants with allele frequencies exceeding the PM2 threshold will be evaluated on a case-by-case basis by the VCEP.

#### PM3 Point System (Per Proband)

| Classification/Zygosity of Other Variant | Confirmed in Trans | Phase Unknown |
|------------------------------------------|-------------------|---------------|
| Pathogenic or Likely pathogenic variant | 1.0 | 0.5 (P) / 0.25 (LP) |
| Homozygous occurrence — Non-consanguineous (no max) | 1.0 | 1.0 |
| Homozygous occurrence — Consanguineous (max point 0.5 per family) | 0.5 | 0.5 |
| Uncertain significance variant (max point 0.5) | 0.25 | 0.0 |

*All variants should be sufficiently rare (meet PM2 specification). P = Pathogenic; LP = Likely pathogenic.*

#### PM3 Evidence Strength Thresholds

| Total Points | Strength Level |
|--------------|----------------|
| 0.5 | PM3_Supporting |
| 1.0 | PM3 (Moderate) |
| 2.0 | PM3_Strong |
| 4.0 | PM3_VeryStrong |

#### PM3 Considerations:
- **Allele Frequency**: Application of PM3 is contingent on the allele frequency of the variant being assessed and the variant presumably on the other allele both being sufficiently rare (meets PM2 threshold).
- **Phasing**: If phase cannot be determined, at least two different LP/P variants are needed to equal the weight of one LP/P co-occurrence confirmed *in trans*. If only one parent is tested and found to carry one allele, variants can be counted as *in trans*.
- **Classification**: Probands should be weighted less when the variant on the other allele is of uncertain significance. The classification of the variant on the other allele should not use evidence from the variant being interrogated (to avoid circularity).
- **Homozygous occurrences**: Default weight is dropped to 0.5 points (may be due to consanguinity). A recommended max of 1.0 points of all homozygous cases is suggested.

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

**Original ACMG Summary:** Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.

Example: Arg156His is pathogenic; now you observe Arg156Cys.

Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:**

#### For Missense Variants:

| Strength | Criteria |
|----------|----------|
| **Moderate** | Applicable at default strength if previously established variant is classified as **pathogenic** by SCID VCEP specifications. |
| **Supporting** | Applicable at reduced strength if previously established variant is classified as **likely pathogenic** by SCID VCEP specifications. |

#### For Nonsense Variants (Point-Based System):

| Strength | Criteria |
|----------|----------|
| **Strong** | ≥4 points from informative variants (see point table below). PM5_Strong should be **downgraded to PM5_Moderate** if PVS1 is applied at any strength. |
| **Moderate** | ≥2 points from informative variants. PM5_Moderate may **not** be combined with PVS1_VeryStrong (should be downgraded to PM5_Supporting if PVS1_VeryStrong is applied). |
| **Supporting** | 1 point from an informative variant. Informative variants must be classified by SCID VCEP specifications. |

#### PM5 Nonsense Variant Point Table

| Type of VUA | Informative Variant | Score |
|-------------|-------------------|-------|
| Nonsense variant predicted to lead to NMD | P/LP variant in the exon of DNA change predicted to lead to NMD | +1 pt |
| Nonsense variant predicted to lead to NMD | B/LB variant in the exon predicted to lead to NMD | -2 pt |
| Nonsense variant resulting in PTC in the final exon, not predicted to lead to NMD | P/LP variant resulting in PTC in the same exon but **downstream** of VUA | +1 pt |
| Nonsense variant resulting in PTC in the final exon, not predicted to lead to NMD | B/LB variant resulting in PTC in the same exon but **upstream** of the VUA | -2 pt |

*NMD = nonsense-mediated decay; PTC = premature termination codon*

#### PM5 Notes:
- The informative variant must be classified by the SCID VCEP specifications and may **not** be the same variant used to meet "+1 pathogenic variant downstream" on the PVS1 flowchart.
- If negative points are calculated, the curator should not apply PM5 and should reconsider if PVS1 is applicable for the VUA.
- The VUA must be sufficiently rare (meet PM2_Supporting) to apply this point system.
- If the informative variant is a frameshift or nonsense variant, it must reach classification as Pathogenic or Likely Pathogenic **without** use of PM5 and **without** use of only PVS1 plus PM2.

---

### PM6 - De Novo (Assumed)

**Original ACMG Summary:** Assumed de novo, but without confirmation of paternity and maternity.

**VCEP Specifications:** Same as PS2 — use the point-based system above. The following guidelines should be used when determining the phenotypic consistency of each proband:

- **"Phenotype highly specific for gene"**: proband must meet at least PP4_Moderate criteria
- **"Phenotype consistent with gene but not highly specific"**: proband must meet PP4 criteria
- **"Phenotype consistent with gene but not highly specific and high genetic heterogeneity"**: proband has been asserted to have a SCID phenotype but does not meet PP4 criteria
- Reduce points per proband by half if the phase is unconfirmed

See [PS2/PM6 Point System](#ps2pm6-point-system-per-proband) and [PS2/PM6 Evidence Strength Thresholds](#ps2pm6-evidence-strength-thresholds) above.

---

### PP1 - Co-segregation

**Original ACMG Summary:** Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.

Note: May be used as stronger evidence with increasing segregation data.

**VCEP Specifications:**

Use ClinGen SVI recommendations for co-segregation criterion (PMID: 30311386) with the additional specification that unaffected individuals contributing to the calculated LOD score must be **heterozygous carriers** of one of the variants observed in the affected individuals (i.e. do **not** count wild-type/wild-type individuals).

#### PP1 General Thresholds

| Strength | Likelihood | LOD Score |
|----------|------------|-----------|
| Supporting | 4:1 | 0.6 |
| Moderate | 16:1 | 1.2 |
| Strong | 32:1 | 1.5 |

#### PP1 Autosomal Dominant Thresholds

| Strength | Threshold |
|----------|-----------|
| Supporting | 2 affected segregations |
| Moderate | 4 affected segregations |
| Strong | 5 affected segregations |

#### PP1 Autosomal Recessive LOD Score Table

*Affected segregations in rows; Unaffected recessive segregations in columns.*

| Affected \ Unaffected | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|-----------------------|---|---|---|---|---|---|---|---|---|---|---|
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

*Affected segregations: affected family members in whom biallelic compound heterozygous or homozygous variants segregate. Unaffected segregations: unaffected family members (typically siblings) at risk to inherit the two variants — should be either wild-type for both variants or a heterozygous carrier for a single variant. Unaffected carrier parents do NOT count as unaffected segregations.*

---

### PP2 - Missense in Constrained Gene

**Original ACMG Summary:** Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.

**VCEP Specifications:** *Not Applicable*

**Comments:** Does not apply. The gnomAD v2.1.1 missense Z score for RAG2 (Z = 0.2) suggests this gene is not constrained for missense variation. Both benign and pathogenic missense variants are present in RAG2.

---

### PP3 - Computational Evidence

**Original ACMG Summary:** Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).

Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Supporting** | Only applicable to **synonymous or intronic variants** predicted to impact splicing by SpliceAI with a delta score **≥0.2**. **Do not apply to missense variants.** |

---

### PP4 - Phenotype Specificity

**Original ACMG Summary:** Patient's phenotype or family history is highly specific for a disease with a single genetic etiology.

**VCEP Specifications:**

PP4 applicability and strength is determined by the total points accumulated by a single affected individual according to the table below and the following total point ranges:

#### PP4 Strength Thresholds

| Total Points | Strength |
|--------------|----------|
| <1 | PP4 not met |
| 1 to <2 | PP4 (Supporting) |
| 2 to <4 | PP4_Moderate |
| ≥4 | PP4_Strong^1 |

^1 CNV (Copy number variation) testing is required to consider PP4_Strong in order to certify that the variant in question is the causative for the phenotype and not one CNV event corrected by gene therapy and not identified previously.

#### PP4 Point System

| Evidence Description | Points |
|---------------------|--------|
| Diagnostic criteria met for SCID (Criteria 1 and 3 or Criterion 4 by itself) or Leaky SCID/Omenn syndrome (excluding Criterion 2)^1 | 0.5 |
| SCID gene panel or exome/genome sequencing conducted (only applicable if genetic testing did not provide an alternative genetic explanation for SCID/Leaky SCID/Omenn syndrome phenotype) | 1 |
| Family history of SCID (only applicable if SCID gene panel or exome/genome sequencing was conducted on proband and did not provide an alternative genetic explanation for phenotype) | 0.5 |
| Decreased presence of TCRVα7.2 (<2%) in CD3+ T lymphocytes and/or mucosa-associated invariant T-cells demonstrated by flow cytometry **AND** pathogenic or likely pathogenic variants in RAG1 and DCLRE1C **have been excluded** (PMID: 39792639) | 1.5 |
| Decreased presence of TCRVα7.2 (<2%) in CD3+ T lymphocytes and/or mucosa-associated invariant T-cells demonstrated by flow cytometry **AND** pathogenic or likely pathogenic variants in RAG1 and DCLRE1C have **NOT** been excluded (PMID: 39792639) | 0.5 |
| Increased presence of 9G4+ (>10%), 9G4int (>5%) or 9G4hi (>5%) cells in CD19+ B cells demonstrated by flow cytometry **AND** pathogenic or likely pathogenic variants in RAG1 **have been excluded** (PMID: 39792639) | 1 |
| Increased presence of 9G4+ (>10%), 9G4int (>5%) or 9G4hi (>5%) cells in CD19+ B cells demonstrated by flow cytometry **AND** pathogenic or likely pathogenic variants in RAG1 have **NOT** been excluded (PMID: 39792639) | 0.5 |
| SCID phenotype corrected by RAG2 gene therapy | 4 |
| T-B-NK+ lymphocyte subset profile* (*See notes*) | 0.5 |

^1 The diagnostic criteria should follow the PIDTC 2022 specification.

\**Notes:* 1) If NK cells are not noted or are present, criteria may still be applied if SCID gene panel or exome/genome sequencing has ruled out alternative causes; 2) If maternal T cells are present, the T lymphocyte profile is still considered to be T- (autologous T cells are absent).

---

### PP5 - Reputable Source

**Original ACMG Summary:** Reputable source recently reports variant as pathogenic, but the evidence is not available to the laboratory to perform an independent evaluation.

**VCEP Specifications:** *Not Applicable*

This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PMID: 29543229).

---

## Benign Criteria

### BA1 - Allele Frequency >5%

**Original ACMG Summary:** Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

**VCEP Specifications:**

Maximum credible population allele frequency threshold determined using Whiffin/Ware calculator with the following parameters:
- Prevalence: 1:5,000
- Allelic heterogeneity: 1
- Genetic heterogeneity: 0.19 (based on the contribution of *RAG2* variants to total SCID in the PIDTC 6901 cohort reported in Dvorak et al., 2019 (PMID: 30193840, Table 1): 19.2% rounded to 19%)
- Penetrance: 50%

**Stand Alone:**
- gnomAD popmax filtering allele frequency **>0.00872**

---

### BS1 - Frequency Greater Than Expected

**Original ACMG Summary:** Allele frequency is greater than expected for disorder.

**VCEP Specifications:**

Maximum credible population allele frequency threshold determined using Whiffin/Ware calculator with the following parameters:
- Prevalence: 1:50,000
- Allelic heterogeneity: 1
- Genetic heterogeneity: 0.19 (based on the contribution of *RAG2* variants to total SCID in the PIDTC 6901 cohort reported in Dvorak et al., 2019 (PMID: 30193840, Table 1): 19.2% rounded to 19%)
- Penetrance: 100%

| Strength | Criteria |
|----------|----------|
| **Strong** | gnomAD popmax filtering allele frequency **>0.00195**. Consider also bottleneck populations. |

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

**Comments:** There is not a well-established functional study which can rule out all damaging effects on protein function.

---

### BS4 - Lack of Segregation

**Original ACMG Summary:** Lack of segregation in affected members of a family.

Caveat: The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.

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
| **BP6** | Not Applicable | This criterion is not for use as recommended by the ClinGen SVI VCEP Review Committee (PMID: 29543229). |
| **BP7** | Supporting | Applicable to both synonymous variants and deep intronic variants affecting nucleotides at or beyond the +7 (donor) and -21 (acceptor) positions. The variant should be predicted not to impact splicing by at least two out of three *in silico* tools (freely available tools include GeneSplicer, MaxEntScan, NNSplice, SpliceAI, Splicing Sequences Finder (SSF), and varSEAK). Given the potential for poor conservation of genes related to T cell and B cell development among vertebrates, nucleotide conservation is **not required** in order to apply BP7. |

---

## Rules for Combining Criteria

### Pathogenic Classification

| Criteria Combination |
|---------------------|
| 1 Very Strong **AND** ≥1 Strong |
| 1 Very Strong **AND** ≥2 Moderate |
| 1 Very Strong **AND** 1 Moderate **AND** 1 Supporting |
| 1 Very Strong **AND** ≥2 Supporting |
| ≥2 Strong |
| 1 Strong **AND** ≥3 Moderate |
| 1 Strong **AND** 2 Moderate **AND** ≥2 Supporting |
| 1 Strong **AND** 1 Moderate **AND** ≥4 Supporting |

### Likely Pathogenic Classification

| Criteria Combination |
|---------------------|
| 1 Very Strong **AND** 1 Moderate |
| 1 Strong **AND** 1 Moderate |
| 1 Strong **AND** ≥2 Supporting |
| ≥3 Moderate |
| 2 Moderate **AND** ≥2 Supporting |
| 1 Moderate **AND** ≥4 Supporting |
| 1 Strong **AND** 2 Moderate |

### Benign Classification

| Criteria Combination |
|---------------------|
| ≥2 Strong |
| 1 Stand Alone (BA1) |

### Likely Benign Classification

| Criteria Combination |
|---------------------|
| 1 Strong *(BS1, BS4)* |
| ≥2 Supporting *(BS2_Supporting, BP7)* |

---

## Appendices

### Appendix A: PVS1 Flowchart

The RAG2-specific PVS1 flowchart modifies the ClinGen SVI PVS1 flowchart (Tayoun et al., 2018; PMID: 30192042) with the following key RAG2-specific annotations:

- **Red boxes (X marks):** PVS1 at default Very Strong strength is NOT applicable to RAG2 for these paths because RAG2 is a single-exon gene and NMD is not predicted for nonsense/frameshift variants.
- **Purple boxes:** PVS1 IS applicable at Very Strong strength when the truncated/altered region is critical to protein function — specifically the PHD domain (amino acids 414-487) AND core domain (amino acids 1-383).
- **Critical domains defined:**
  - Core domain: amino acids 1-383
  - PHD domain: amino acids 414-487 (PMID: 15964836)

### Appendix B: Reference PMIDs

| PMID | Reference | Context |
|------|-----------|---------|
| 30192042 | Tayoun et al., 2018 | PVS1 loss of function criterion recommendations |
| 15964836 | — | PHD domain critical to protein function |
| 26996199 | — | Functional domain specifications for PM1 |
| 29772310 | Tirosh et al., 2019 | V(D)J recombination assay (PS3_Moderate) |
| 20234091 | Couëdel et al., 2010 | V(D)J recombination assay (PS3_Supporting) |
| 30311386 | — | Co-segregation criterion recommendations (PP1) |
| 30193840 | Dvorak et al., 2019 | PIDTC 6901 cohort — genetic heterogeneity for BA1/BS1 |
| 29543229 | — | ClinGen SVI recommendation against PP5/BP6 |
| 39792639 | — | TCRVα7.2 and 9G4+ flow cytometry biomarkers for PP4 |

### Appendix C: Population Frequency Thresholds Summary

| Criterion | Threshold | Strength | Parameters |
|-----------|-----------|----------|------------|
| BA1 | >0.00872 | Stand Alone | Prevalence 1:5,000; Allelic heterogeneity 1; Genetic heterogeneity 0.19; Penetrance 50% |
| BS1 | >0.00195 | Strong | Prevalence 1:50,000; Allelic heterogeneity 1; Genetic heterogeneity 0.19; Penetrance 100% |
| PM2 | <0.0000588 | Supporting | No homozygotes in gnomAD |

### Appendix D: RAG2 Protein Domain Map

| Region | Amino Acid Range | Significance |
|--------|-----------------|-------------|
| Core domain | 1-383 | Essential for recombination activity; critical to protein function |
| Linker region | 384-413 | Between core and PHD domains |
| PHD domain | 414-487 | Critical to protein function (histone recognition); PMID: 15964836 |
| C-terminal region | 488-527 | Beyond PHD domain |

### Appendix E: Criteria Applicability Summary

| Criterion | Applicable | Max Strength | Notes |
|-----------|-----------|-------------|-------|
| PVS1 | Yes | Very Strong | Modified for single-exon gene; see flowchart |
| PS1 | Yes | Strong | Must use SCID VCEP classifications |
| PS2 | Yes | Very Strong | Point-based system with PP4-guided phenotypic consistency |
| PS3 | Yes | Strong | Animal model (Strong); V(D)J assay <25% WT (Moderate); 25-60% WT or reduced (Supporting) |
| PS4 | No | — | Not applicable |
| PM1 | Yes | Moderate | PHD domain (Moderate); Core domain (Supporting) |
| PM2 | Yes | Supporting | <0.0000588 popmax FAF; no homozygotes |
| PM3 | Yes | Very Strong | Point-based system; co-occurring variant must use SCID VCEP classifications |
| PM4 | Yes | Moderate | Deleted region must contain P/LP variant (Moderate) or VUS (Supporting) |
| PM5 | Yes | Strong | Missense: per standard rules; Nonsense: point-based system |
| PM6 | Yes | Very Strong | Same as PS2 point-based system |
| PP1 | Yes | Strong | LOD-score based; unaffected must be carriers |
| PP2 | No | — | Gene not constrained for missense (Z = 0.2) |
| PP3 | Yes | Supporting | Synonymous/intronic only; SpliceAI ≥0.2; NOT for missense |
| PP4 | Yes | Strong | Point-based phenotype system; CNV testing required for Strong |
| PP5 | No | — | Not for use per ClinGen SVI |
| BA1 | Yes | Stand Alone | >0.00872 popmax FAF |
| BS1 | Yes | Strong | >0.00195 popmax FAF |
| BS2 | Yes | Supporting | Homozygous in healthy adult only |
| BS3 | No | — | No well-established assay to rule out all damaging effects |
| BS4 | Yes | Strong | No additional specifications |
| BP1 | No | — | Not applicable |
| BP2 | No | — | Not applicable |
| BP3 | No | — | Not applicable |
| BP4 | No | — | Not applicable |
| BP5 | No | — | Not applicable |
| BP6 | No | — | Not for use per ClinGen SVI |
| BP7 | Yes | Supporting | Synonymous/deep intronic; 2/3 in silico tools; conservation not required |

---

## Version History

| Version | Date | Notes |
|---------|------|-------|
| 2.1.0 | 10/1/2025 | Edited Likely Benign Rules for Combining Criteria. V1 had 1 strong, the change in V2 to 1 strong + 1 supporting was unintentional. |
| 2.0.0 | — | Added PP4 2025 updates with flow cytometry biomarkers (TCRVα7.2, 9G4+); updated PM3 per April 2025 SVI recommendations. |
| 1.0.0 | — | Initial release. |

---

*This document was compiled from ClinGen VCEP specifications and ClinGen SVI recommendations. For the most current version, please refer to the ClinGen website.*
