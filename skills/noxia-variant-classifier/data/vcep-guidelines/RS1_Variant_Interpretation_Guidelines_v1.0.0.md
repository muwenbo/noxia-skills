# ClinGen X-linked Inherited Retinal Disease Expert Panel Variant Interpretation Guidelines for RS1

**Version:** 1.0.0
**Released:** 5/16/2025
**Affiliation:** X-linked Inherited Retinal Disease VCEP
**Based on:** Richards et al., 2015 ACMG/AMP Guidelines

---

## Gene Information

| Attribute | Value |
|-----------|-------|
| **Gene** | RS1 (HGNC:10457) |
| **HGNC Name** | retinoschisin 1 |
| **Transcript** | NM_000330.4 |
| **Disease** | X-linked retinoschisis (MONDO:0010725) |
| **Inheritance** | X-linked inheritance |

---

## General Comments

In addition to the specific criteria for codes listed below, the VCEP has adopted the **point-based combining scoring** in Table 2 and Table 3 of PMID: 32720330 (Tavtigian et al., 2020). Table 2 assigns points for pathogenic (0 for indeterminate, 1 for supporting, 2 for moderate, 4 for strong, and 8 for very strong), and benign (0 for indeterminate, -1 for supporting, -2 for moderate, -4 for strong, and -8 for very strong) codes. Table 3 provides final categories of **Pathogenic (>=10)**, **Likely Pathogenic (6-9)**, **Uncertain (0-5)**, **Likely Benign (-1 to -6)**, **Benign (<=-7)**. This replaces the combining rules listed below.

### Phenotype Requirement for Pathogenic Phenotype Codes

> **Note:** Probands being considered for any pathogenic phenotype codes (e.g. PP1, PP4, PM6, PS2, PS4) at any strength must have the following phenotype characteristics:
> - Affected males should have some functional vision impairment by age 13
> - With either observed foveo-macular changes or ERG measurement of a subnormal B wave

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

**VCEP Specifications:** Use the attached RS1-specific PVS1 Decision Tree file, which has been modified from Abou Tayoun et al., 2018 (PMID 30192042) and incorporates splice site guidance from Walker et al., 2023 (PMID 37352859). Refer to the RS1-specific PVS1 Decision Tree document for complete information.

The structure of RS1 is important for function. The RS1 monomers have cystine disulfide bonds within a RS1 monomer and bonds with the two neighboring monomers to form an octomer substructure and bonds to the second RS1 octomer that completes the paired octomer structure. Within this structure there are a number of sites that have been shown to function in other types of protein structure stabilization.

#### Strength Levels

| Strength | Criteria |
|----------|----------|
| **Very Strong** | Applies to nonsense, frameshift, splice site, and deletion variants in NM_000330.4 c.1A to c.671C (p.Met1 to p.Cys223) and to duplications in NM_000330.4 c.1 to c.472 (p.Met1 to p.Asp158). |
| **Strong** | Applies to frameshift variants, GT--AG splice variants, deletions, duplications or nonsense variants in NM_000330.4 c.672 to c.677 (p.Asp224 to p.*225). |
| **Moderate** | Use RS1-specific PVS1 Decision Tree file as per Abou Tayoun et al. and Walker et al. guidance. |

**Modification Type:** Gene-specific

#### PVS1 Decision Tree Summary

**Nonsense or Frameshift:**

| Region | NMD Predicted? | PVS1 Strength |
|--------|---------------|---------------|
| NM_000330.4:c.1-472 | Yes | PVS1 |
| NM_000330.4:c.473-671 (up to p.Cys223) | No, but impacts critical structure/function | PVS1 |
| NM_000330.4:c.672-677 | No, function of region unknown, LoF not frequent in general population | PVS1_Strong |

**GT--AG +/-1,2 Splice Sites:**

| Scenario | PVS1 Strength |
|----------|---------------|
| Skipping exons 1-3 (c.1-184), disrupts reading frame, predicted NMD | PVS1 |
| Exon skipping in c.473-671, impacts regions critical to protein structure up through p.Cys223 | PVS1 |
| c.672-677 changes, function of region unknown | PVS1_Strong |

**Note:** Splice site variants at +/-1,2 positions should NOT be applied in combination with in silico splicing predictions (PP3). Splice site variants must have no detectable nearby (+/-20nts) strong consensus splice sequence that may constitute in-frame splicing.

**Deletion (single exon to full gene):**

| Scenario | PVS1 Strength |
|----------|---------------|
| Full gene deletion in a male | PVS1 (Pathogenic warranted) |
| Single to multi exon deletion disrupting reading frame, predicted NMD | PVS1 |
| Exons 1-3 (c.1-184), single exon deletions disrupt reading frame | PVS1 |
| c.672-677 deletions, function of region unknown | PVS1_Strong |
| Exon 4-6 single exon or multi exon deletions preserving reading frame, up to p.Cys223 (c.1-671) impacting critical protein structure | PVS1 |

**Duplication (>=1 exon, completely contained within gene):**

| Scenario | PVS1 Strength |
|----------|---------------|
| Proven/presumed in tandem, c.1-472, predicted NMD | PVS1 |
| c.473-671, impacts critical protein structure | PVS1 |
| c.672-677, function of region unknown | PVS1_Strong |

**Initiation Codon:**

| Scenario | PVS1 Strength |
|----------|---------------|
| p.Met1 (c.1-3) is the only known start codon; >=1 pathogenic variant(s) upstream of the closest potential in-frame start codon at c.441-443 (p.Met147) | PVS1 |

#### NMD Prediction Boundary

NMD prediction based on the premature termination codon not occurring in the 3' most exon or in the 3' most 50bp of the penultimate exon: **p.Ser2 to p.Asp158** in transcript NM_000330.4:c.4-472.

#### Key Transcript Positions

| Feature | Position | Notes |
|---------|----------|-------|
| Start codon | c.1-3 (p.1) | |
| Nearest in-frame start codon | c.441-443 (p.147) | In exon 5 |
| Next nearest in-frame start codon | c.639-641 (p.213) | In exon 6 |
| Stop codon | c.675-677 (p.225) | |
| NMD predicted cutoff | c.472 | |
| Stop codon after stop-loss | c.*127 | Adds 43 amino acids |

#### RS1 Exon Map (NM_000330.4)

| Exon | Acceptor Start | Donor End | HG38 Start | HG38 End | FS/In-frame | NMD? | PVS1 Code | Critical? | Domain |
|------|---------------|-----------|------------|----------|-------------|------|-----------|-----------|--------|
| 1 | c.-40 | c.52 | 18,672,108 | 18,672,017 | FS | NMD | PVS1 (B) | Yes | Leader sequence |
| 2 | c.53 | c.78 | 18,657,665 | 18,657,640 | FS | NMD | PVS1 (C) | Yes | Leader sequence |
| 3 | c.79 | c.184 | 18,656,758 | 18,656,653 | FS | NMD | PVS1 (C) | Yes | RS1 domain |
| 4 | c.185 | c.326 | 18,647,332 | 18,647,191 | In-frame | NMD | PVS1 (F) | Yes | Discoidin domain |
| 5 | c.327 | c.522 | 18,644,625 | 18,644,430 | In-frame | No NMD | PVS1 (F) | Yes | Discoidin domain |
| 6 | c.523 | c.*2316 | 18,642,156 | 18,639,688 | In-frame | No NMD | PVS1 (F) | Yes | Discoidin domain |

**Note:** All exons 1-6 are considered "critical to protein function" based on pathogenic missense variants identified in all exons. The requirement for being more than 10% of total protein length does not apply. No potential "rescue isoforms" are known.

---

### PS1 - Same Amino Acid Change

**Original ACMG Summary:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.

**Caveat:** Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:** Refer to the RS1-specific PVS1 Decision Tree document for complete information.

#### Strength Levels

| Strength | Criteria |
|----------|----------|
| **Strong** | Same amino acid change as a previously established **Pathogenic** variant. Comparison variant must have been evaluated by the X-linked IRD VCEP using these rules and established as Pathogenic. For assessing same amino acid changes, SpliceAI scores for both variants should be within 10% of each other. |
| **Moderate** | Same amino acid change as a previously established **(Likely) Pathogenic** variant. Comparison variant must have been evaluated by the X-linked IRD VCEP and established as Likely Pathogenic. SpliceAI scores for both variants should be within 10% of each other. |
| **Supporting** | Same amino acid change as a previously established **(Likely) Pathogenic** variant evaluated by the X-linked IRD VCEP and established as Likely Pathogenic. SpliceAI scores for both variants should be within 10% of each other. |

**Modification Type:** Clarification, General recommendation

#### PS1 Splicing Evaluation Rules

**When evaluating splicing impact with a previously classified Pathogenic variant (PS1 Strong):**
- Use in conjunction with PP3 for variants located **outside** the splice donor/acceptor +/-1,2 dinucleotide positions that have SpliceAI score >=0.2 and have a comparable nucleotide variant at the same position designated Pathogenic.
- Use in conjunction with PVS1 for variants located **at** the splice donor/acceptor +/-1,2 dinucleotide positions that have a comparable variant within the same splice donor/acceptor +/-1,2 dinucleotide designated Pathogenic.

**When evaluating splicing impact with a previously classified Likely Pathogenic or Pathogenic variant (PS1 Moderate):**
- Use with PP3 for variants outside +/-1,2 positions with SpliceAI >=0.2 and comparable LP variant at same position.
- Use with PP3 for variants outside +/-1,2 positions with SpliceAI >=0.2 and comparable P variant within same splice region with same predicted impact.
- Use with PVS1 at any strength for variants at +/-1,2 positions with SpliceAI >=0.2 and comparable P variant within same splice motif region but outside +/-1,2 positions with same predicted impact.

**When evaluating splicing impact with a previously classified Likely Pathogenic variant (PS1 Supporting):**
- Use with PP3 for variants outside +/-1,2 positions with SpliceAI >=0.2 and comparable LP variant within same splice motif region but outside +/-1,2 positions with same predicted impact.
- Use with PVS1 for variants at +/-1,2 positions with SpliceAI >=0.2 and comparable P variant at same +/-1,2 position with same predicted impact.
- Use with PVS1 for variants at +/-1,2 positions with comparable LP or P variant within same splice motif region but outside +/-1,2 positions with same predicted impact.
- Use with PVS1 at any strength for variants at +/-1,2 positions with comparable LP variant within same splice motif region but outside +/-1,2 positions with same predicted impact.

#### PS1 Code Weights for Splice Variants (Table 2 from Walker et al., 2023)

| Variant Under Assessment | Baseline Code | Position of Comparison Variant | PS1 with P Comparison | PS1 with LP Comparison |
|--------------------------|--------------|-------------------------------|----------------------|----------------------|
| Outside splice donor/acceptor +/-1,2 | PP3 | Same nucleotide | PS1 | PS1_Moderate |
| Outside splice donor/acceptor +/-1,2 | PP3 | Within same splice donor/acceptor motif (incl. +/-1,2) | PS1_Moderate | PS1_Supporting |
| At splice donor/acceptor +/-1,2 | PVS1 | Within same +/-1,2 dinucleotide | PS1_Supporting | N/A |
| At splice donor/acceptor +/-1,2 | PVS1 | Within same splice region, outside +/-1,2 | PS1_Supporting | PS1_Supporting |
| At splice donor/acceptor +/-1,2 | PVS1_Strong/Moderate/Supporting | Within same +/-1,2 dinucleotide | PS1 | N/A |
| At splice donor/acceptor +/-1,2 | PVS1_Strong/Moderate/Supporting | Within same splice motif, outside +/-1,2 | PS1_Moderate | PS1_Supporting |

---

### PS2 - De Novo (Confirmed)

**Original ACMG Summary:** De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.

**Note:** Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.

**VCEP Specifications:** Use SVI point scale for counting cases (see PS2/PM6 Tables). Use option 1 "Phenotype highly specific for gene" when OCT (optical coherence tomography) data showing schisis is available.

#### PS2/PM6 Point System (Table 1)

| Phenotypic Consistency | Confirmed de novo with confirmed maternity | Assumed de novo with assumed maternity |
|------------------------|--------------------------------------------|----------------------------------------|
| **Phenotype highly specific for gene** - Requires OCT showing schisis | 2.0 points per proband | 1.0 points per proband |
| **Phenotype consistent with gene but not highly specific** - Use when lacking OCT data | 1.0 points per proband | 0.5 points per proband |

#### PS2/PM6 Evidence Strength Thresholds (Table 2)

| Total Points | Strength Level |
|--------------|----------------|
| 0.5 | Supporting |
| 1.0 | Moderate |
| 2.0 | Strong |
| 4.0 | Very Strong |

**Modification Type:** Gene-specific

---

### PS3 - Functional Studies

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.

**Note:** Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.

**VCEP Specifications:** See RS1 Functional Assay sheet.

#### Strength Levels

| Strength | Criteria |
|----------|----------|
| **Strong** | Variants tested in high quality knock-out/knock-in variant mouse lines can meet PS3 at the strong level. |
| **Supporting** | Use at the supporting strength for most assays (see Functional Assays Table). |

**Modification Type:** Gene-specific, Strength

#### Approved Functional Assay Instances

**1. Secretion Defect Assays**

| PMID | Author (Lab) | Year | Cell Line | Readout | Approved? | Strength |
|------|-------------|------|-----------|---------|-----------|----------|
| 12417531 | Wang (Trump lab) | 2002 | COS-7 | Qualitative WB | **Yes** | PS3_Supporting; BS3 not applied |
| 12746437 | Wu (Molday lab) | 2003 | HEK293 | Qualitative WB | **Yes** | PS3_Supporting; BS3 not applied |
| 16361673 | Wang (Trump lab) | 2006 | COS-7 | Qualitative WB | No | N/A |
| 17525175 | Dyka (Molday lab) | 2007 | HEK293 | Qualitative WB | **Yes** | PS3_Supporting; BS3 not applied |
| 19849666 | Gleghorn (Trump/Bulleid labs) | 2009 | HEK293 | Qualitative WB | **Yes** | PS3_Supporting; BS3 not applied |
| 20809529 | Vijayasarathy (Sieving lab) | 2010 | COS-7 | Qualitative WB | No | N/A |
| 29851975 | Sudha (Arunachalam lab) | 2018 | COS-7 | Qualitative WB | No | N/A |
| 30630865 | Heymann (Sieving/Steven labs) | 2019 | HEK293 | Qualitative WB | No | N/A |
| 30040949 | Plössl (Friedrich lab) | 2018 | HEK293 | Quantitative WB | No | N/A |

**Description:** Wild-type or RS1 variants transfected into cells; Western blot analysis of secretion into cell culture medium vs. cell lysate retention. Abnormal = absence of secreted RS1 band in the medium.

**2. Endoplasmic Reticulum Retention or Processing Assays**

| PMID | Author (Lab) | Year | Assay | Approved? | Strength |
|------|-------------|------|-------|-----------|----------|
| 12417531 | Wang (Trump lab) | 2002 | Proteolytic processing (signal peptide removal) | **Yes** | PS3_Supporting; BS3 not applied |
| 12417531 | Wang (Trump lab) | 2002 | Immunofluorescence co-localization with ER markers | **Yes** | PS3_Supporting; BS3 not applied |
| 12746437 | Wu (Molday lab) | 2003 | WB for ER retention | **Yes** | PS3_Supporting; BS3 not applied |

**Description:** Assesses whether mutant RS1 is retained in the endoplasmic reticulum vs. properly processed and secreted. Includes signal peptide processing assays and immunofluorescence-based ER co-localization.

**3. Multimerization or Co-Assembly Assays**

| PMID | Author (Lab) | Year | Assay | Approved? | Strength |
|------|-------------|------|-------|-----------|----------|
| 16361673 | Wang (Trump lab) | 2006 | Oligomerization (non-reducing WB) | **Yes** | PS3_Supporting; BS3 not applied |
| 16361673 | Wang (Trump lab) | 2006 | Oligomerization in Weri-Rb1 and COS-7 | **Yes** | PS3_Supporting; BS3 not applied |
| 19849666 | Gleghorn (Trump/Bulleid labs) | 2009 | Co-transfection co-assembly | **Yes** | PS3_Supporting; BS3 not applied |

**Description:** Tests whether mutant RS1 can form proper oligomeric structures (octamers) or co-assemble with wild-type RS1. Abnormal = formation of monomers/dimers only, inability to form octamers.

**4. Minigene Assays**

| PMID | Author (Lab) | Year | Assay | Approved? | Strength |
|------|-------------|------|-------|-----------|----------|
| 35456481 | Bender (Hufnagel lab) | 2022 | Exon 2 minigene (gel electrophoresis + Sanger) | **Yes** | Since SpliceAI >0.2, use with in silico evidence per RS1 PVS1 Decision Tree |
| 20809529 | Vijayasarathy (Sieving lab) | 2010 | cDNA-based minigene (WB + Sanger) | **Yes** | PS3_Supporting (not PVS1, since data indicates protein still produced) |

**Description:** DNA fragments including RS1 exonic regions with flanking intronic sequence cloned into expression vectors. Tests impact on splicing by gel electrophoresis and Sanger sequencing of transcripts.

**5. Animal Model Assays**

| PMID | Author (Lab) | Year | Model | Approved? | Strength |
|------|-------------|------|-------|-----------|----------|
| 29379415 | Chen (Gu lab) | 2018 | TALEN knock-in mouse (p.Tyr65Ter) | **Yes** | PS3 (Strong) |
| 31174210 | Liu (Romano lab) | 2019 | Rs1 mutant mouse lines (C59S, R141C) | **Yes** | PS3 (Strong) |
| 30040949 | Plössl (Friedrich lab) | 2018 | Exogenous RS1 expression + retinal membrane binding | **Yes** | PS3_Supporting; BS3 not applied |

**Description:** Knock-in/knock-out mouse models tested for retinal phenotype (ERG responses, immunohistochemistry, Western blot). High quality knock-in models meet PS3 at the strong level.

**6. Protein-Protein Interaction Assays**

| PMID | Author (Lab) | Year | Assay | Approved? | Strength |
|------|-------------|------|-------|-----------|----------|
| 30040949 | Plössl (Friedrich lab) | 2018 | Binding to HEK293 cells expressing ATP1A3/ATP1B2 | **Yes** | PS3_Supporting; BS3 not applied |
| 30040949 | Plössl (Friedrich lab) | 2018 | Binding to murine retinal Rs1h-/Y membranes | **Yes** | PS3_Supporting; BS3 not applied |

**Description:** Tests whether mutant RS1 can bind to Na/K-ATPase subunits (ATP1A3, ATP1B2) or retinal membranes. Abnormal = absent/minimal binding signal compared to wild-type.

---

### PS4 - Prevalence in Affected

**Original ACMG Summary:** The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.

**VCEP Specifications:** Probands must meet phenotype requirements (see General Comments). PM2_Supporting must be met for all strength levels.

#### Strength Levels

| Strength | Criteria |
|----------|----------|
| **Very Strong** | >=9 probands, each with retinoschisis. PM2_Supporting must be met. |
| **Strong** | 5-8 probands, each with retinoschisis. PM2_Supporting must be met. |
| **Moderate** | 3-4 probands diagnosed with retinoschisis. PM2_Supporting must be met. |
| **Supporting** | 1 proband diagnosed with retinoschisis + a second proband answering the PP4 requirements, PM2_Supporting must be met. **OR** 2 probands, each with retinoschisis, PM2_Supporting must be met. |

**Modification Type:** Gene-specific, Strength

---

### PM1 - Mutational Hot Spot

**Original ACMG Summary:** Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.

**VCEP Specifications:**

#### Strength Levels

| Strength | Criteria |
|----------|----------|
| **Strong** | Applies to variants in amino acids **p.Cys40, p.Cys59, p.Cys63, p.Cys110, p.Cys142, p.Cys219, and p.Cys223** which form disulfide bridges required for structure of the retinoschisin monomer, dimers, or octamers. |
| **Moderate** | Applies to amino acids **p.Glu72, p.Trp122, p.Trp163, p.Arg200, p.Glu215** which form salt bridges that are required for higher order structure of octamers and paired octamers. |

**Modification Type:** Gene-specific

---

### PM2 - Absent from Controls

**Original ACMG Summary:** Absent from controls (or at extremely low frequency if recessive) in population databases.

**Caveat:** Population data for indels may be poorly called by next generation sequencing.

**VCEP Specification (Supporting only):**
- At low frequency in **males** in population databases
- Use **<2.0x10^-6** for cutoff
- This is defined relative to the BA1 cutoff

**Modification Type:** Clarification, Gene-specific

---

### PM3 - In Trans with Pathogenic

**Original ACMG Summary:** For recessive disorders, detected in trans with a pathogenic variant.

**VCEP Specifications:** **Not Applicable** - RS1 is an X-linked gene; this criterion does not apply.

---

### PM4 - Protein Length Changes

**Original ACMG Summary:** Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

**VCEP Specifications:** Use SVI specification.

| Strength | Criteria |
|----------|----------|
| **Moderate** | In-frame deletion/insertions smaller than one whole exon, in a non-repetitive region, or stop-loss variants. Variant must not be considered in any PVS1 criteria. Variant must also meet PM2. |

**Modification Type:** General recommendation, Gene-specific

---

### PM5 - Novel Missense at Same Residue

**Original ACMG Summary:** Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.

**Caveat:** Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Moderate** | Same residue as a previously established **pathogenic** variant classified using these specifications (assessed independently of PM5). The novel change must not affect splicing (SpliceAI <=0.2), must meet PP3, and have a Grantham score equal or greater than the previously published variants. |
| **Supporting** | Same residue as a previously established **likely pathogenic** variant classified using these specifications (assessed independently of PM5). The novel change must not affect splicing (SpliceAI <=0.2), must meet PP3, and have a Grantham score equal or greater than the previously published variants. |

**Modification Type:** Clarification, Gene-specific

---

### PM6 - De Novo (Assumed)

**Original ACMG Summary:** Assumed de novo, but without confirmation of paternity and maternity.

**VCEP Specifications:** **Not Applicable** - See PS2 for de novo data. De novo evidence (both confirmed and assumed) is handled through the PS2/PM6 point system described under PS2.

---

### PP1 - Co-segregation

**Original ACMG Summary:** Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.

**Note:** May be used as stronger evidence with increasing segregation data.

**VCEP Specifications:** Probands must meet phenotype requirements. Only phenotype positive **male** relatives with the same variant identified in the proband should be counted as segregations.

#### Strength Levels

| Strength | Criteria |
|----------|----------|
| **Strong** | >=3 meioses in 1 or 2 families |
| **Moderate** | 2 meioses in a family (e.g. 2 brothers and mother genotyped; 3 brothers without mother's genotype; or uncle and nephew) |
| **Supporting** | 1 meiosis in a family |

**Modification Type:** Gene-specific, Strength

---

### PP2 - Missense in Constrained Gene

**Original ACMG Summary:** Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.

**VCEP Specifications:** **Not Applicable**

**Comments:** Loss of function variants are underrepresented. The Z score in gnomAD is 0.97. The pLoF eligible alleles for this code is 0/303.

---

### PP3 - Computational Evidence

**Original ACMG Summary:** Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).

**Caveat:** As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.

**VCEP Specifications:** Use the SpliceAI flowchart included in the RS1-specific PVS1 Decision Tree file.

#### For Missense Variants (REVEL-based)

| Strength | REVEL Score | Additional Requirements |
|----------|------------|------------------------|
| **Strong** | >0.931 | SpliceAI <0.2 (not predicted to disrupt splicing) |
| **Moderate** | 0.773 - 0.931 | SpliceAI <0.2 (not predicted to disrupt splicing) |
| **Supporting** | 0.644 - 0.772 | SpliceAI <0.2 (not predicted to disrupt splicing) |

#### For Splicing Predictions (SpliceAI-based)

| SpliceAI Delta Score | Code Applied |
|---------------------|-------------|
| >=0.2 | PP3 applied (then see PS1 splice variant rules for comparison variants) |
| >0.1 and <0.2 | PP3 N/A for splicing; consider missense/indel predictions for exonic variants |
| <=0.1 | BP4 applied (see BP4 section) |

**Modification Type:** General recommendation

#### SpliceAI Flowchart Notes

For variants located outside of donor/acceptor +/-1,2 dinucleotide positions:
- SpliceAI delta score >=0.2: **PP3** applied; see RS1-specific PVS1 (RNA) Decision Tree for PS1 combinations
- SpliceAI delta score >0.1 and <0.2: **PP3 N/A** (splicing); consider missense/indel predictions for exonic variants
- SpliceAI delta score <=0.1: **BP4** applied

**Donor and acceptor splice region positions excluded from BP7:**
- Synonymous substitutions in the first base of an exon
- Synonymous substitutions in the last three bases of an exon
- +1 through +7 of the donor sequence after an exon
- -1 through -21 of the acceptor sequence before an exon

---

### PP4 - Phenotype Specificity

**Original ACMG Summary:** Patient's phenotype or family history is highly specific for a disease with a single genetic etiology.

**VCEP Specifications:** Probands must meet phenotype requirements: affected males should have some functional vision impairment by age 13, with a diagnosis of Retinoschisis and an image of schisis.

#### Strength Levels

| Strength | Criteria |
|----------|----------|
| **Moderate** | A male proband diagnosed with retinoschisis by the age of 13 with visual acuity impairment, showing schisis, **and** having retinal detachment. |
| **Supporting** | A male proband diagnosed with retinoschisis by the age of 13 with visual acuity impairment **and** showing schisis. |

**Modification Type:** Clarification, Gene-specific, Strength

---

### PP5 - Reputable Source

**Original ACMG Summary:** Reputable source recently reports variant as pathogenic, but the evidence is not available to the laboratory to perform an independent evaluation.

**VCEP Specifications:** **Not Applicable** - This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PMID: 29543229).

---

## Benign Criteria

### BA1 - Allele Frequency >5%

**Original ACMG Summary:** Allele frequency is above 5% in population databases.

**VCEP Specifications:** Any variant meeting both BA1 and PP3 must be reviewed by the VCEP.

**VCEP Specification (Stand Alone):**
- Allele frequency **>=2x10^-4** in **males** in population databases (Exome Sequencing Project, 1000 Genomes, or Exome Aggregation Consortium) in the subpopulation with the highest frequency.

**Modification Type:** Clarification

---

### BS1 - Frequency Greater Than Expected

**Original ACMG Summary:** Allele frequency is greater than expected for disorder.

**VCEP Specifications:** Variants meeting both BS1 and PP3 must be reviewed by the VCEP.

**VCEP Specification (Strong):**
- Allele frequency **>=2x10^-5** in **males** in population databases
- The highest allele frequency in population databases should be used

**Modification Type:** Gene-specific

---

### BS2 - Observed in Healthy Adult

**Original ACMG Summary:** Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

**VCEP Specification (Strong):**
- Only count **males over age 30** with a documented eye exam without retinoschisis
- BS2_Strong for variants observed in **at least 3 unaffected males**

**Modification Type:** Disease-specific, Gene-specific

---

### BS3 - Functional Studies (No Effect)

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

**VCEP Specifications:** **Not Applicable**

**Comments:** The many secretion assays have not tested enough benign variants to meet the threshold in PMID 31892348 Supplemental Table 1 or Supplemental Table 2.

---

### BS4 - Lack of Segregation

**Original ACMG Summary:** Lack of segregation in affected members of a family.

**Caveat:** The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.

**VCEP Specification (Supporting):**
- Paternal inheritance is inconsistent with this gene
- For RS1, unaffected males over age 10 who have been examined could be used to establish this code if they have no schisis and good acuity

**Modification Type:** Gene-specific

---

### BP1-BP7 - Benign Supporting

| Criterion | Status | Comment |
|-----------|--------|---------|
| **BP1** | Not Applicable | Missense variant in a gene for which primarily truncating variants are known to cause disease. |
| **BP2** | Not Applicable | For this X-linked gene, only variants in cis with a pathogenic variant in RS1 in an affected male could be used, but these variants could have combined effect. The VCEP does not use this code. |
| **BP3** | Not Applicable | In-frame deletions/insertions in a repetitive region without a known function. |
| **BP4** | See below | Multiple lines of computational evidence suggest no impact on gene or gene product. |
| **BP5** | Not Applicable | Variant found in a case with an alternate molecular basis for disease. |
| **BP6** | Not Applicable | This criterion is not for use as recommended by the ClinGen SVI VCEP Review Committee (PMID: 29543229). |
| **BP7** | See below | Synonymous variant with no predicted splicing impact and low conservation. |

#### BP4 - Computational Evidence (Benign)

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Stand Alone** | Missense variants: REVEL <=0.003 with SpliceAI <=0.1 |
| **Strong** | Missense variants: REVEL between 0.004 and 0.016 with SpliceAI <=0.1 |
| **Moderate** | Missense variants: REVEL between 0.017 and 0.183 with SpliceAI <=0.1 |
| **Supporting** | Missense variants: REVEL between 0.184 and 0.290 with SpliceAI <=0.1 **OR** Synonymous variants or noncoding variants: SpliceAI <=0.1 |

**Modification Type:** General recommendation

#### BP7 - Synonymous Variant

**VCEP Specifications:** This code may be used with BP4 as described in the RS1-specific PVS1 Decision Tree file splicing document and Walker et al., 2023.

| Strength | Criteria |
|----------|----------|
| **Strong** | Applies to splicing assay data demonstrating a variant is NOT associated with aberrantly spliced transcript(s) relative to transcript profiles in controls. See RS1 PVS1 Decision Tree. As per Walker et al., 2023 (PMID 37352859) guidance. |
| **Supporting** | Synonymous variants or noncoding variants with no impact on splicing (SpliceAI <=0.1) **AND** PhyloP <0.1 for conservation. |

**Modification Type:** Clarification, Gene-specific

---

## Rules for Combining Criteria

> **Note:** The VCEP has adopted the point-based combining scoring system (PMID: 32720330). This replaces the traditional combining rules below. Point assignments: Pathogenic codes: 0 (indeterminate), 1 (supporting), 2 (moderate), 4 (strong), 8 (very strong). Benign codes: 0 (indeterminate), -1 (supporting), -2 (moderate), -4 (strong), -8 (very strong).

### Point-Based Classification Thresholds

| Total Points | Classification |
|-------------|---------------|
| >=10 | Pathogenic |
| 6 to 9 | Likely Pathogenic |
| 0 to 5 | Uncertain Significance |
| -1 to -6 | Likely Benign |
| <=-7 | Benign |

### Traditional Pathogenic Classification

| Criteria Combination |
|---------------------|
| 1 Very Strong *(PVS1, PS2_Very Strong, PS4_Very Strong)* **AND** >=1 Strong *(PVS1_Strong, PS1, PS2, PS3, PS4, PM1_Strong, PP1_Strong, PP3_Strong)* |
| 1 Very Strong **AND** >=2 Moderate *(PVS1_Moderate, PS1_Moderate, PS2_Moderate, PS4_Moderate, PM1, PM4, PM5, PP1_Moderate, PP3_Moderate, PP4_Moderate)* |
| 1 Very Strong **AND** 1 Moderate **AND** 1 Supporting *(PS1_Supporting, PS2_Supporting, PS3_Supporting, PS4_Supporting, PM2_Supporting, PM5_Supporting, PP1, PP3, PP4)* |
| 1 Very Strong **AND** >=2 Supporting |
| >=2 Strong |
| 1 Strong **AND** >=3 Moderate |
| 1 Strong **AND** 2 Moderate **AND** >=2 Supporting |
| 1 Strong **AND** 1 Moderate **AND** >=4 Supporting |

### Traditional Likely Pathogenic Classification

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
| >=2 Strong *(BS1, BS2, BP4_Strong)* |
| 1 Stand Alone *(BA1)* |

### Likely Benign Classification

| Criteria Combination |
|---------------------|
| 1 Strong *(BS1, BS2, BP4_Strong)* **AND** 1 Supporting *(BS4_Supporting, BP4, BP7)* |
| >=2 Supporting *(BS4_Supporting, BP4, BP7)* |

---

## Appendices

### Appendix A: PVS1 Decision Tree

Refer to the RS1 PVS1 Decision Tree PDF (updated 1/24/2024) for the full visual flowchart including:
- Part (a): PVS1 Decision Tree for nonsense, frameshift, splice, deletion, duplication, and initiation codon variants
- Part (b): RS1-specific PVS1 (RNA) Decision Tree for Splicing
- Part (c): RS1 PVS1 (RNA) rule table for +/-1,2 changes and RNA splicing assays
- Part (d): RS1 exon map
- Part (e): Generic PVS1 scoring (Figure 2 from Walker et al., 2023)

### PVS1 Scoring Categories (from Walker et al., 2023, Figure 2)

- **(A)** 5' UTR region - No splicing alteration predicted or use of a cryptic splice motif does not affect the coding sequence.
- **(B)** Exon skipping or use of a cryptic splice motif eliminates the initiation codon and there are no alternative start codons.
- **(C)** Exon skipping or use of a cryptic splice motif disrupts reading frame and is predicted to undergo NMD.
- **(D)** Exon skipping or use of a cryptic splice motif preserves reading frame, and removes a region (>10% of the protein) which has not been established as critical to protein function.
- **(E)** Exon skipping or use of a cryptic splice motif disrupts reading frame and is predicted to undergo NMD.
- **(F)** Exon skipping or use of a cryptic splice motif preserves reading frame, and removes a region which has been established as critical to protein function.
- **(G)** Exon skipping or use of a cryptic splice motif preserves reading frame, and removes a region (<10% of the protein) which has not been established as critical to protein function.
- **(H)** Exon skipping or use of a cryptic splice motif disrupts reading frame and is not predicted to undergo NMD, and removes a region (<10% of the protein) which has not been established as critical to protein function.
- **(I)** Exon skipping or use of a cryptic splice motif disrupts reading frame and is not predicted to undergo NMD, and removes a region (<10% of the protein) which has not been established as critical to protein function.

### Appendix B: Population Frequency Thresholds Summary

| Criterion | Threshold | Population | Strength |
|-----------|-----------|------------|----------|
| BA1 | >=2x10^-4 | Males, highest subpopulation | Stand Alone |
| BS1 | >=2x10^-5 | Males, highest subpopulation | Strong |
| PM2 | <2.0x10^-6 | Males | Supporting |

### Appendix C: Computational Prediction Thresholds Summary

#### PP3/BP4 REVEL Thresholds for Missense Variants

| REVEL Score | Pathogenic Code | Benign Code |
|------------|----------------|-------------|
| >0.931 | PP3_Strong | - |
| 0.773 - 0.931 | PP3_Moderate | - |
| 0.644 - 0.772 | PP3_Supporting | - |
| 0.291 - 0.643 | Indeterminate | Indeterminate |
| 0.184 - 0.290 | - | BP4_Supporting |
| 0.017 - 0.183 | - | BP4_Moderate |
| 0.004 - 0.016 | - | BP4_Strong |
| <=0.003 | - | BP4_Stand Alone |

**Note:** All REVEL-based predictions require SpliceAI <=0.1 (for BP4) or SpliceAI <0.2 (for PP3).

#### SpliceAI Thresholds

| SpliceAI Delta Score | Code |
|---------------------|------|
| >=0.2 | PP3 (for splicing) |
| >0.1 and <0.2 | Indeterminate (splicing) |
| <=0.1 | BP4 (for splicing) |

### Appendix D: PM1 Critical Residues

**Disulfide Bridge Residues (PM1_Strong):**
- p.Cys40, p.Cys59, p.Cys63, p.Cys110, p.Cys142, p.Cys219, p.Cys223

**Salt Bridge Residues (PM1_Moderate):**
- p.Glu72, p.Trp122, p.Trp163, p.Arg200, p.Glu215

### Appendix E: Reference PMIDs

| # | PMID | Citation |
|---|------|----------|
| 1 | 36402656 | Heymann JB, Vijayasarathy C et al. Advances in understanding the molecular structure of retinoschisin while questions remain of biological function. Prog Retin Eye Res (2023) 95:101147. |
| 2 | 12417531 | Wang T, Waters CT et al. Intracellular retention of mutant retinoschisin is the pathological mechanism underlying X-linked retinoschisis. Hum Mol Genet (2002) 11(24):3097-105. |
| 3 | 12746437 | Wu WW, Molday RS. Defective discoidin domain structure, subunit assembly, and endoplasmic reticulum processing of retinoschisin are primary mechanisms responsible for X-linked retinoschisis. J Biol Chem (2003) 278(30):28139-46. |
| 4 | 16361673 | Wang T, Zhou A et al. Molecular pathology of X linked retinoschisis: mutations interfere with retinoschisin secretion and oligomerisation. Br J Ophthalmol (2006) 90(1):81-6. |
| 5 | 17525175 | Dyka FM, Molday RS. Coexpression and interaction of wild-type and missense RS1 mutants associated with X-linked retinoschisis: its relevance to gene therapy. Invest Ophthalmol Vis Sci (2007) 48(6):2491-7. |
| 6 | 19849666 | Gleghorn LJ, Trump D et al. Wild-type and missense mutants of retinoschisin co-assemble resulting in either intracellular retention or incorrect assembly of the functionally active octamer. Biochem J (2009) 425(1):275-83. |
| 7 | 20809529 | Vijayasarathy C, Sui R et al. Molecular mechanisms leading to null-protein product from retinoschisin (RS1) signal-sequence mutants in X-linked retinoschisis (XLRS) disease. Hum Mutat (2010) 31(11):1251-60. |
| 8 | 29379415 | Chen D, Xu T et al. Recapitulating X-Linked Juvenile Retinoschisis in Mouse Model by Knock-In Patient-Specific Novel Mutation. Front Mol Neurosci (2017) 10:453. |
| 9 | 29851975 | Sudha D, Neriyanuri S et al. Understanding variable disease severity in X-linked retinoschisis: Does RS1 secretory mechanism determine disease severity? PLoS One (2018) 13(5):e0198086. |
| 10 | 30040949 | Plössl K, Schmid V et al. Pathomechanism of mutated and secreted retinoschisin in X-linked juvenile retinoschisis. Exp Eye Res (2018) 177:23-34. |
| 11 | 30630865 | Heymann JB, Vijayasarathy C et al. Cryo-EM of retinoschisin branched networks suggests an intercellular adhesive scaffold in the retina. J Cell Biol (2019) 218(3):1027-1038. |
| 12 | 31174210 | Liu Y, Kinoshita J et al. Mouse models of X-linked juvenile retinoschisis have an early onset phenotype, the severity of which varies with genotype. Hum Mol Genet (2019) 28(18):3072-3090. |
| 13 | 35456481 | Bender C, Woo EG et al. Predominant Founder Effect among Recurrent Pathogenic Variants for an X-Linked Disorder. Genes (Basel) (2022) 13(4). |
| 14 | 32720330 | Tavtigian SV, Harrison SM et al. Fitting a naturally scaled point system to the ACMG/AMP variant classification guidelines. Hum Mutat (2020) 41(10):1734-1737. |
| 15 | 30192042 | Abou Tayoun AN, Pesaran T et al. Recommendations for interpreting the loss of function PVS1 ACMG/AMP variant criterion. Hum Mutat (2018) 39(11):1517-1524. |
| 16 | 37352859 | Walker LC, Hoya M et al. Using the ACMG/AMP framework to capture evidence related to predicted and observed impact on splicing: Recommendations from the ClinGen SVI Splicing Subgroup. Am J Hum Genet (2023) 110(7):1046-1067. |

---

## Version History

| Version | Date | Notes |
|---------|------|-------|
| 1.0.0 | 5/16/2025 | Initial release of X-linked IRD VCEP specifications for RS1 |

---

*This document was compiled from ClinGen VCEP specifications and ClinGen SVI recommendations. For the most current version, please refer to the ClinGen website.*
