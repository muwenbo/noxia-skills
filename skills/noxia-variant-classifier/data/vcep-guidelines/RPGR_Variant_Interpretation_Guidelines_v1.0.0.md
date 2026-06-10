# ClinGen X-linked Inherited Retinal Disease VCEP Variant Interpretation Guidelines for RPGR

**Version:** 1.0.0
**Released:** 5/16/2025
**Affiliation:** X-linked Inherited Retinal Disease VCEP
**Based on:** Richards et al., 2015 ACMG/AMP Guidelines

---

## Gene Information

| Attribute | Value |
|-----------|-------|
| **Gene** | RPGR (HGNC:10295) |
| **HGNC Name** | retinitis pigmentosa GTPase regulator |
| **Transcripts** | NM_001034853.2 (retinal-specific, ORF15); NM_000328.3 (broadly expressed) |
| **Disease** | RPGR-related retinopathy (MONDO:0100437) |
| **Inheritance** | X-linked inheritance |

### General Comments

In addition to the specific criteria for codes listed below, the VCEP has adopted the **point-based combining scoring** in Table 2 and Table 3 of PMID: 32720330.

- Table 2 assigns points for pathogenic (0 for indeterminate, 1 for supporting, 2 for moderate, 4 for strong, and 8 for very strong), and benign (0 for indeterminate, -1 for supporting, -2 for moderate, -4 for strong, and -8 for very strong) codes.
- Table 3 provides final categories: **Pathogenic** (>=10), **Likely Pathogenic** (6-9), **Uncertain** (0-5), **Likely Benign** (-1 to -6), **Benign** (<=-7).

### Transcript Notes

There are two transcripts for RPGR:

- **NM_001034853.2** — Transcript isoform C (retinal-specific). Reads through the exon 15 terminal splice site and continues into ORF15. This is the transcript expressed in retina and the primary transcript for these specifications.
- **NM_000328.3** — Transcript isoform A (broadly expressed). Includes 19 exons. Splices from exon 15 to exon 16 (exons 16-19). Variants in exons 16 to 19 are not associated with RPGR-related retinopathy.

The two transcripts overlap for exons 1 to 15. These rules have been specified for the ORF15 transcript with ACMG/AMP default specifications for NM_000328.3 exons 16 to 19.

### Phenotype Requirements for Pathogenic Phenotype Codes

> **Note:** All probands being considered for any pathogenic phenotype codes (e.g. PP1, PM6, PS2, PS4) at any strength must have the following phenotype characteristics:
> - Affected males should have some functional vision impairment by age 30, and/or decreased or absent cone and/or rod ERG / FAF responses.
> - Affected females can be considered if they have an affected male relative described, and their relationship is consistent with an X-linked inheritance.

### Clinical Phenotype Overview

RPGR pathology presents a broad range of clinical phenotypes depending on the specific mutation. Clinical fundus appearance can range from typical "retinitis pigmentosa" with heavy retinal pigmentation to "cone dystrophy" with disproportionate macular involvement. Functional aspects follow this range, with cone ERG responses frequently somewhat reduced by the second decade. Female gene carriers frequently show golden metallic retinal sheen before the third decade, which fades later in life.

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

**VCEP Specifications:** Use SVI recommendations (PMID 30192042) with modifications as shown in the RPGR PVS1 Decision Tree figure attached. See also splice guidance (PMID 37352859).

#### Strength Levels

| Strength | Criteria |
|----------|----------|
| **Very Strong (PVS1)** | Variants predicted to undergo NMD (nonsense/frameshift terminating in codons 2-619 in NM_001034853.2 or NM_000328.3). Nonsense or frameshift variants in codons 620-1132 (NM_001034853.2:c.1705-3398) that disrupt ORF15 glutamylation, a critical function. Splice variants causing skipping of exons 1, 11, 12, or 14 in NM_001034853.2 or exons 15, 17, 18, 19 in NM_000328.3 which disrupt reading frame. Variants that skip exons 2, 3, 4, 5, 6, 7, 8, or 10 that affect regions critical to protein function. Deletions of single exons 1, 9, 11, 12, or 14 in NM_001034853.2 or exons 15, 17, 18 in NM_000328.3. Full gene deletion. Duplications (proven or presumed in tandem) disrupting reading frame with NMD predicted. |
| **Strong (PVS1_Strong)** | Variants that remove more than 10% of the protein and are not expected to lead to NMD. Applies to nonsense/frameshift in NM_001034853.2:c.3399-3458 (codons 1132-1152) region where function is unknown but variant removes >10% of protein. |
| **Moderate (PVS1_Moderate)** | Initiation codon variants with upstream pathogenic variants of closest potential in-frame start codon. Variants in NM_000328.3 which remove <10% of the protein (after codon 872) and are not expected to lead to NMD. |
| **Supporting (PVS1_Supporting)** | Initiation codon variants without upstream pathogenic variants of closest potential in-frame start codon. |

**Modification Type:** Gene-specific, Strength

#### RPGR-Specific PVS1 Decision Tree for Nonsense/Frameshift

| Variant Location | NMD Predicted? | PVS1 Code |
|-----------------|----------------|-----------|
| Codons 2-619 (NM_001034853.2:c.4-1704 or NM_000328.3:c.4-1704) | Yes | PVS1 |
| Codons 620-783 in NM_000328.3 only (c.1705-2106) | Yes | N/A |
| NM_001034853.2:c.1705-3398 (codons 620-1132) — disrupts ORF15 glutamylation | Critical function | PVS1 |
| NM_001034853.2:c.3399-3458 (codons 1132-1152) — unknown function, removes >10% protein | No NMD | PVS1_Strong |
| NM_000328.3 variants after codon 872 — removes <10% protein | No NMD | PVS1_Moderate |

#### RPGR-Specific PVS1 Decision Tree for Splice Sites (GT-AG +/-1,2)

| Exon Skipping Consequence | PVS1 Code |
|--------------------------|-----------|
| Exons 1, 11, 12, or 14 in NM_001034853.2 — disrupts reading frame | PVS1 |
| Exons 15, 17, 18, 19 in NM_000328.3 — disrupts reading frame | PVS1 |
| Exon absent from biologically-relevant transcript(s) | N/A |
| NM_001034853.2 codons 619-1132 — disrupts ORF15 glutamylation (critical function) | PVS1 |
| Unknown function region, LoF not frequent, removes >10% protein | PVS1_Strong |
| Unknown function region, LoF not frequent, NM_000328.3 after codon 872 (<10% protein) | PVS1_Moderate |
| Exons 2, 3, 4, 5, 6, 7, 8, or 10 — preserves reading frame but affects critical region | PVS1 |

#### RPGR-Specific PVS1 Decision Tree for Deletions

| Deletion Type | PVS1 Code |
|--------------|-----------|
| Full gene deletion | PVS1 (Pathogenic warranted for male) |
| Single exons 1, 9, 11, 12, or 14 in NM_001034853.2 — disrupts reading frame + NMD | PVS1 |
| Single exons 15, 17, 18 in NM_000328.3 — disrupts reading frame + NMD | PVS1 |
| NM_001034853.2:c.1705-3398 (codons 619-1132) — disrupts ORF15 glutamylation | PVS1 |
| Exons 2, 3, 4, 5, 6, 7, 8, or 10 — truncate/alter critical regions | PVS1 |

#### PVS1 RNA/Splicing Decision Tree Notes

- PVS1 should not be applied in combination with in silico splicing predictions (PP3) for canonical splice site variants.
- Splice site variants must have no detectable nearby (+/- 20nts) strong consensus splice sequence that may constitute in-frame splicing.
- NMD prediction: premature termination codon not occurring in the 3' most exon or in the 3' most 50bp of the penultimate exon.
- NMD predicted cutoff NM_001034853.2: c.1704 (codon 619)
- NMD predicted cutoff NM_000328.3: c.2106 (codon 783)

#### RPGR Exon Map and PVS1 (RNA) Rule Table

| Exon | Transcript | Transcript Start | Transcript End | Exon Skipping Effect | NMD? | PVS1 Code | Critical to Function? |
|------|-----------|-----------------|---------------|---------------------|------|-----------|----------------------|
| Exon 1 | Both | c.-142 | c.28 | FS | NMD | PVS1 (B) | Yes |
| Exon 2 | Both | c.29 | c.154 | In frame | No NMD | PVS1 (G) | No |
| Exon 3 | Both | c.155 | c.247 | In frame | No NMD | PVS1 (F) | Yes |
| Exon 4 | Both | c.248 | c.310 | In frame | No NMD | PVS1 (F) | Yes |
| Exon 5 | Both | c.311 | c.469 | In frame | No NMD | PVS1 (F) | Yes |
| Exon 6 | Both | c.470 | c.619 | In frame | No NMD | PVS1 (F) | Yes |
| Exon 7 | Both | c.620 | c.778 | In frame | No NMD | PVS1 (F) | Yes |
| Exon 8 | Both | c.779 | c.934 | In frame | No NMD | PVS1 (F) | Yes |
| Exon 9 | Both | c.935 | c.1059 | FS | NMD | PVS1 (C) | Yes |
| Exon 10 | Both | c.1060 | c.1245 | In frame | No NMD | PVS1 (F) | Yes |
| Exon 11 | Both | c.1246 | c.1414 | FS | NMD | PVS1 (C) | Yes |
| Exon 12 | Both | c.1415 | c.1506 | FS | NMD | PVS1 (C) | Yes |
| Exon 13 | Both | c.1507 | c.1572 | In frame | No NMD | PVS1 (G) | Yes |
| Exon 14 | NM_001034853.2 | c.1573 | c.1753 | FS | No NMD | PVS1 (J) | No |
| Exon 14 | NM_000328.3 | — | — | FS | NMD | PVS1 (C) | No |
| Exon ORF15 | NM_001034853.2 | c.1754 | c.*3459 | In frame | No NMD | PVS1 (F) | Yes |
| Exon 15 | NM_000328.3 | c.1754 | c.1905 | FS | NMD | PVS1 (C) | Yes |
| Exon 16 | NM_000328.3 | c.1906 | c.2091 | In frame | No NMD | PVS1 (G) | No |
| Exon 17 | NM_000328.3 | c.2092 | c.2149 | FS | NMD | PVS1 (D) | No |
| Exon 18 | NM_000328.3 | c.2150 | c.2241 | FS | No NMD | PVS1 (H) | No |
| Exon 19 | NM_000328.3 | c.2242 | c.*463 | FS | No NMD | PVS1 (I) | No |

**Key Coordinates:**
- Start codon: c.1-c.3 (hg38: 38,327,368)
- Nearest in-frame start codon: c.21-c.23 (precludes use of PVS1(B) for initiation codon variants)
- Next nearest in-frame start codon: c.30-c.32 (in exon 3)
- Stop codon ORF15: c.*3457-c.*3459 (hg38: 38,285,542)
- Stop codon exon 19: c.*2304-c.*2306 (hg38: 38,269,627)
- NMD predicted cutoff NM_001034853.2: c.1704 (hg38: 38,287,897)
- NMD predicted cutoff NM_000328.3: c.2108 (hg38: 38,273,420)
- Stop codon after stop-loss in ORF15: c.3569 (+37 codons, hg38: 38,285,431)
- Stop codon after stop-loss in exon 19: c.2498 (+17 codons, hg38: 38,269,577)

#### PVS1 Decision Tree Footnotes

- **(a)** PVS1 should not be applied in combination with PP3. Splice site variants must have no detectable nearby (+/- 20nts) strong consensus splice sequence that may constitute in-frame splicing.
- **(b)** NMD prediction based on the premature termination codon not occurring in the 3' most exon or in the 3' most 50bp of the penultimate exon.
- **(c)** Relevant domain indicated by experimental evidence proving a critical role of the domain and/or presence of non-truncating pathogenic variants in the region.
- **(d)** For a full gene deletion of RPGR in a male, a pathogenic classification is warranted.
- **(e)** Variants terminating in codons 2-619 in NM_001034853.2:c.4-1704 and NM_000328.3:c.4-1704 (hg38: 38,287,910 to 38,327,367) undergo NMD.
- **(f)** Variants terminating in codons 619-783 in NM_000328.3:c.1705-2106 (hg38: 38,273,435 to 38,287,910) undergo NMD.
- **(g)** Variants in NM_001034853.2:c.1705-3398 (codons 619-1132, hg38: 38,287,910 to 38,285,759) disrupt glutamylation in ORF15, a critical function.
- **(h)** Role of region in protein function is unknown: NM_001034853.2:c.3399-3458 (codons 1132-1152) and 3' UTR; NM_000328.3:c.2352-2909 (codons 584-969) and 3' UTR.
- **(i)** Variants that skip exon 2 (which has a defined pathogenic missense variant, PMID 37352859) or skip or alter the RCC1 domain in exons 3-10 affect regions critical to protein function.
- **(j)** XLIRD VCEP addition: Exon skipping or use of a cryptic splice motif disrupts reading frame and is not predicted to undergo NMD, and removes a region (<10% of the protein) which has not been established as critical to protein function, but it disrupts a region in the next exon which has been established as critical to protein function. PVS1.

---

### PS1 - Same Amino Acid Change

**Original ACMG Summary:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.

**Caveat:** Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:** See RPGR specific PVS1 Decision Tree.

#### Strength Levels

| Strength | Criteria |
|----------|----------|
| **Strong (PS1)** | Same amino acid change as a previously established **Pathogenic** variant. Comparison variant must have been evaluated by the X-linked IRD VCEP using these rules. For assessing same amino acid changes, SpliceAI scores for both variants should be within 10% of each other. Also applies to same predicted splicing impact as a previously classified Pathogenic variant (see splice decision tree). |
| **Moderate (PS1_Moderate)** | Same amino acid change as a previously established **Likely Pathogenic** variant. Comparison variant must have been evaluated by the X-linked IRD VCEP. SpliceAI scores for both variants should be within 10% of each other. Also applies to same predicted splicing impact as a Likely Pathogenic or Pathogenic variant in the same splice region (see splice decision tree). |
| **Supporting (PS1_Supporting)** | Used in conjunction with PP3 for variants outside splice donor/acceptor +/-1,2 dinucleotide positions that have SpliceAI score >=0.2 and a comparable nucleotide variant within the same motif designated Likely Pathogenic. Used in conjunction with PVS1 or PVS1_(reduced strength) for variants at splice donor/acceptor +/-1,2 dinucleotide positions with comparable LP or P variant. See PVS1 Decision Tree part (b) (Table 2 from Walker 2023). |

**Modification Type:** Clarification, General recommendation

#### PS1 Splicing Code Weights (Table 2 from Walker et al., 2023)

| Variant Under Assessment | Baseline Code | Position of Comparison Variant | PS1 with P Comparison | PS1 with LP Comparison |
|--------------------------|--------------|-------------------------------|----------------------|----------------------|
| Outside splice donor/acceptor +/-1,2 | PP3 | Same nucleotide | PS1 | PS1_Moderate |
| Outside splice donor/acceptor +/-1,2 | PP3 | Within same splice donor/acceptor motif (incl. +/-1,2) | PS1_Moderate | PS1_Supporting |
| At splice donor/acceptor +/-1,2 | PVS1 | Within same splice donor/acceptor +/-1,2 | PS1_Supporting | N/A |
| At splice donor/acceptor +/-1,2 | PVS1 | Within same splice D/A region, outside +/-1,2 | PS1_Supporting | PS1_Supporting |
| At splice donor/acceptor +/-1,2 | PVS1_Strong/Mod/Supp | Within same splice donor/acceptor +/-1,2 | PS1 | N/A |
| At splice donor/acceptor +/-1,2 | PVS1_Strong/Mod/Supp | Within same splice D/A motif, outside +/-1,2 | PS1_Moderate | PS1_Supporting |

---

### PS2 - De Novo (Confirmed)

**Original ACMG Summary:** De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.

**VCEP Specifications:** Use SVI point scale for counting cases. Use option 3: "Phenotype consistent with gene but not highly specific and high genetic heterogeneity." Genetic testing of the mother through a genotyping method that can confirm maternity is required. The PM6 code is not used.

#### PS2/PM6 Point System (Per Proband)

| Phenotypic Consistency | Confirmed de novo with confirmed maternity | Assumed de novo with assumed maternity |
|------------------------|-------------------------------------------|---------------------------------------|
| Phenotype highly specific for gene | N/A | N/A |
| Phenotype consistent with gene but not highly specific | 1 point | N/A |
| Phenotype consistent with gene but not highly specific and **high genetic heterogeneity** | **0.5 points** | **0.25 points** |
| Phenotype not consistent with gene | 0 points | 0 points |

> **Note:** For RPGR, the correct row is "Phenotype consistent with gene but not highly specific and high genetic heterogeneity" (0.5 points per confirmed de novo proband, 0.25 per assumed de novo proband).

#### Evidence Strength Thresholds

| Total Points | Strength Level |
|--------------|----------------|
| 0.5 | PS2_Supporting |
| 1.0 | PS2_Moderate |
| 2.0 | PS2 (Strong) |
| 4.0 | PS2_VeryStrong |

**Modification Type:** Gene-specific

---

### PS3 - Functional Studies

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.

**VCEP Specifications:** See excel file for details. Only PS3_Supporting is available based on approved assays (OddsPath >2.1 per SVI recommendations).

#### Strength Levels

| Strength | Criteria |
|----------|----------|
| **Supporting (PS3_Supporting)** | Assays with OddsPath >2.1 as per SVI recommendations. Applies to approved functional studies listed below. -OR- Animal models that replicate the phenotype. |

**Modification Type:** Gene-specific

#### Approved Assay Instances

##### 1. Protein-Protein Interaction (PMID: 30622176)

| Attribute | Details |
|-----------|---------|
| **Author** | Zhang (Val Sheffield lab), 2019 |
| **Assay** | Wild-type or variant RPGR expressed as Flag-S fusion protein in HEK293T cells. RPGR pull-down with anti-Flag beads. PDE6D, RPGRIP1L, or RPGR detected by western blotting. |
| **Material** | HEK293T cells transiently expressing wild-type or variant Flag-S-tagged RPGR |
| **Readout** | Qualitative — presence/absence of western blotting band |
| **Controls** | Positive: WT RPGR; Negative: empty vector |
| **Approved** | Yes |
| **Strength** | PS3_Supporting; BS3 not applied |
| **Variants tested** | 6 (p.Cys812Ala, p.Met58Lys, p.Gly43Arg, p.Phe130Cys, p.Gly215Val, p.Gly275Ser) |

**Additional PMIDs for protein-protein interaction:** 20631154, 10958648, 23213406, 9990021, 36445968

##### 2. Protein Localization to Connecting Cilia (PMIDs: 30622176, 25630948)

**Assay A (PMID: 30622176):**

| Attribute | Details |
|-----------|---------|
| **Assay** | GFP-tagged RPGR expressed in RPE1 cells. Percentage of cells with GFP-positive cilia quantified within 12-15 random fields. |
| **Material** | RPE1 cells expressing wild-type or variant RPGR-GFP fusion proteins |
| **Readout** | Quantitative — percentage of cells with GFP-positive cilia, normalized to wild-type |
| **Controls** | Positive: WT RPGR (3 independent transfections) |
| **Approved** | Yes |
| **Strength** | PS3_Supporting; BS3 not applied |
| **Variants tested** | 7 (p.Cys812Ala, p.Cys812Ter, p.Met58Lys, p.Gly43Arg, p.Phe130Cys, p.Gly215Val, p.Gly275Ser) |

**Assay B (PMID: 25630948):**

| Attribute | Details |
|-----------|---------|
| **Author** | Da Costa (John Neidhardt lab), 2015 |
| **Assay** | RPGR antibody immunofluorescent staining of patient fibroblasts. Alpha-tubulin and gamma-tubulin used for ciliary structure definition. U1 snRNA rescue component required to confirm specificity. |
| **Material** | Patient fibroblasts harboring RPGR variants |
| **Readout** | Quantitative — percentage of cells with punctate RPGR localization along cilium |
| **Controls** | Positive: 3 unaffected control patients (74-84% positive) |
| **Approved** | Yes |
| **Strength** | PS3_Supporting; BS3 not applied |
| **Variants tested** | 1 (c.1245+3A>T) |
| **Note** | Rescue component must be present to confirm specificity of localization defect to the variant. |

##### 3. Glutamylation Assays (PMID: 27162334)

| Attribute | Details |
|-----------|---------|
| **Author** | Sun (Tiansen Li lab), 2016 |
| **Assay** | AAV-packaged RPGR subretinally injected into Rpgr null mice. Western blotting for RPGR and polyglutamylation (GT335 antibody). Densitometry quantification of glutamylation-to-RPGR ratio. |
| **Material** | Rpgr null mice injected with AAV-RPGR (wild-type or variant) |
| **Readout** | Semi-quantitative — ratio of polyglutamylation to total RPGR signal |
| **Controls** | Positive: WT RPGR; Negative: uninjected |
| **Approved** | Yes |
| **Strength** | PS3_Supporting; BS3 not applied |
| **Variants tested** | 2 (p.Gly874Ter, p.Glu1078Ter) |
| **Note** | Only applicable to **truncating variants in exon 15 (ORF15)**. Loss of glutamylation is recognized as a contributing factor in pathogenicity of truncating RPGR variants but is not expected to contribute to pathogenicity of missense variants due to the repetitive nature of exon 15. Also see PMID: 36445968. |

##### 4. Animal Models

| Attribute | Details |
|-----------|---------|
| **Approved** | Yes (no currently applicable knock-in study) |
| **Strength** | PS3_Supporting or PS3_Moderate; BS3 not applied |
| **Note** | The VCEP would consider a future mouse model with knock-in of a human patient-associated RPGR variant at PS3_Supporting or higher. |

---

### PS4 - Prevalence in Affected

**Original ACMG Summary:** The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.

**VCEP Specifications:** Probands counted for PS4 must be unrelated to each other. Probands may overlap with PP4 probands at the supporting level. PM2_Supporting must be met.

#### Strength Levels

| Strength | Criteria |
|----------|----------|
| **Very Strong** | >= 8 unrelated probands and PM2_Supporting must be met |
| **Strong (PS4)** | >= 6 unrelated probands and PM2_Supporting must be met |
| **Moderate (PS4_Moderate)** | 3-5 unrelated probands and PM2_Supporting must be met |
| **Supporting (PS4_Supporting)** | >= 2 unrelated probands and PM2_Supporting must be met. **OR** 1 proband meeting PS4 requirements when a separate unrelated proband has been used for PP4. |

**PS4_Supporting alternative rule:** This variant has been reported in at least 1 proband meeting one of the PS4 requirements of a male with some functional vision impairment by age 30 and/or decreased or absent ERG responses, or a female with functional visual abnormality and documentation of a male relative affected with retinitis pigmentosa, as well as a second apparently unrelated proband previously used for the PP4 code.

**Modification Type:** Gene-specific, Strength

---

### PM1 - Mutational Hot Spot

**Original ACMG Summary:** Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.

***Not Applicable*** for RPGR. See PM2_Supporting.

---

### PM2 - Absent from Controls

**Original ACMG Summary:** Absent from controls (or at extremely low frequency if recessive) in population databases.

**VCEP Specification (Supporting only):**
- Allele frequency in males <= 0.00005 (<=5x10^-5) in population databases
- Highest allele frequency in a subpopulation should be used to assess this

**Note:** In the ORF15 region of low complexity (amino acids 725-1078), population frequency data can be evaluated for PM2_Supporting / BS1 / BA1 but also needs to be reviewed by the VCEP by showing a screenshot of the gnomAD data during the presentation of the variant for VCEP approval.

**Modification Type:** Clarification, Gene-specific

---

### PM3 - In Trans with Pathogenic

**Original ACMG Summary:** For recessive disorders, detected in trans with a pathogenic variant.

***Not Applicable*** for RPGR (X-linked gene).

---

### PM4 - Protein Length Changes

**Original ACMG Summary:** Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

**VCEP Specifications:** ORF15 repetitive region (amino acids 585 to 1078) should not be evaluated here.

#### Strength Levels

| Strength | Criteria |
|----------|----------|
| **Strong (PM4_Strong)** | Use for stop loss variants in amino acid 1153. These variants will produce a 38 amino acid extension which was shown to have a deleterious effect (PMID: 33805381, variant in c.3457). |
| **Moderate (PM4)** | Protein length changes in exons 1-14, due to in-frame deletions/insertions in a non-repeat region. Or, in ORF15 outside of the repetitive region in amino acids 585 to 1078, due to in-frame deletions/insertions in a non-repeat region. |

**Modification Type:** Clarification, Gene-specific

---

### PM5 - Novel Missense at Same Residue

**Original ACMG Summary:** Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.

**Caveat:** Beware of changes that impact splicing rather than at the amino acid/protein level.

#### Strength Levels

| Strength | Criteria |
|----------|----------|
| **Moderate (PM5)** | Must have **2** comparison variants reaching pathogenic classification using these specifications. The novel change must not affect splicing (SpliceAI <= 0.2), must meet PP3, and have a Grantham score equal to or greater than the previously published variants. |
| **Supporting (PM5_Supporting)** | Same residue as a previously established **likely pathogenic** variant (assessed independently of PM5). The novel change must not affect splicing (SpliceAI <= 0.2), must meet PP3, and have a Grantham score equal to or greater than the previously published variants. |

**Modification Type:** Clarification, Gene-specific

---

### PM6 - De Novo (Assumed)

**Original ACMG Summary:** Assumed de novo, but without confirmation of paternity and maternity.

***Not Applicable*** for RPGR. See PS2 for de novo data. Genetic testing of the mother through a genotyping method that can confirm maternity is required.

---

### PP1 - Co-segregation

**Original ACMG Summary:** Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.

**VCEP Specifications:** Only phenotype positive relatives with the same variant identified in the proband should be counted as segregations. Affected female counting is eligible in cases where an affected male is described in a pedigree or the text.

#### Strength Levels

| Strength | Criteria |
|----------|----------|
| **Strong (PP1_Strong)** | >= 4 meioses in > 1 family |
| **Moderate (PP1_Moderate)** | >= 3 meioses in >= 1 family |
| **Supporting (PP1)** | >= 2 meioses in the same family, OR proband with affected mother |

**Modification Type:** Gene-specific, Strength

---

### PP2 - Missense in Constrained Gene

**Original ACMG Summary:** Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.

***Not Applicable*** for RPGR.

---

### PP3 - Computational Evidence

**Original ACMG Summary:** Multiple lines of computational evidence support a deleterious effect on the gene or gene product.

**Caveat:** PP3 can be used only once in any evaluation of a variant. This code cannot be used with the PVS1 code for canonical splice site variants.

#### Strength Levels — Missense Variants

| Strength | REVEL Score | SpliceAI Score |
|----------|------------|----------------|
| **Strong (PP3_Strong)** | > 0.932 | < 0.2 |
| **Moderate (PP3_Moderate)** | 0.773 - 0.931 | < 0.2 |
| **Supporting (PP3)** | 0.644 - 0.772 | < 0.2 |

#### Strength Levels — Splicing Variants

| Strength | Criteria |
|----------|----------|
| **Supporting (PP3)** | For variants with SpliceAI scores >= 0.2, in the two first or last two bases in an exon or the 6 intronic bases flanking an exon |

**Modification Type:** General recommendation, Clarification, Gene-specific

#### SpliceAI Decision Flowchart (for variants outside donor/acceptor +/-1,2)

| SpliceAI Delta Score | Code |
|---------------------|------|
| <= 0.1 | BP4 |
| > 0.1 and < 0.2 | PP3 N/A (Splicing); consider missense/indel predictions for exonic variants |
| >= 0.2 | PP3 (Splicing) |

---

### PP4 - Phenotype Specificity

**Original ACMG Summary:** Patient's phenotype or family history is highly specific for a disease with a single genetic etiology.

**VCEP Specifications:** A point system was developed to determine when there is enough information about a proband's phenotype to qualify for use of this code. This code can be used for a single proband. **4 or more phenotype points are required** to use this code. Do not include a proband with a suspected diagnosis of more than one retinal disease.

#### PP4 Strength Thresholds

| Total Points | Specific Criteria Required | Strength |
|--------------|---------------------------|----------|
| < 4 | — | PP4 not met |
| 4 - 7.5 | At least 1 specific criterion must be met | PP4 (Supporting) |
| >= 8 | At least 2 specific criteria must be met | PP4_Moderate |

#### PP4 Point System

**Required for use of PP4 (0 points each — must be met):**
- Males have functional vision impairment by age 30 (or by age 50 if harboring a truncating variant after c.2128 and diagnosis of cone or cone-rod dystrophy)
- Decreased or absent cone and/or rod ERG or FAF responses

**Specific RPGR Phenotype Findings List (2 points each):**
- Family history consistent with X-linked inheritance, no male-to-male transmission
- Previous exome, genome or 100+ retinal dystrophy panel (that includes X-linked genes) testing that did not provide an alternative explanation for visual impairment

**Consistent with RPGR Findings (0.5 or 1 point each):**

| Finding | Points |
|---------|--------|
| Rod involvement relatively greater than cone involvement (or cone > rod if truncating variant after c.2128 and cone/cone-rod dystrophy) | 1 |
| Onset in the 1st or 2nd decade of life (ages 2-19) | 1 |
| Delayed or milder phenotype in females (unlike carriers of other X-linked RP, female carriers show some retinal pathology by age 50, usually by age 30) | 1 |
| Patient report of night blindness/nyctalopia | 0.5 |
| Optic nerve pallor | 0.5 |
| Pigmentary retinopathy | 0.5 |
| Poor pupillary light response | 0.5 |
| Abnormal color vision | 0.5 |
| Decreased central vision acuity | 0.5 |
| Myopia | 0.5 |
| High myopia (e.g. -6 Diopter and higher) | 1.0 |
| Photodysphoria / photophobia (or 1 point if truncating variant after c.2128 and cone/cone-rod dystrophy) | 0.5 |
| Visual field constriction | 0.5 |
| Macular atrophy (only if truncating variant after c.2128 and cone/cone-rod dystrophy) | 1 |

**Family inheritance can be used with no clear genotyping in the following cases:**
- Pedigree clearly shows inheritance from mother's side of family, with no male-to-male transmission
- Patient comes from an X-linked cohort assembled before genotyping, specifically indicating no male-to-male transmission
- Patient was identified as an X-linked case within an IRD cohort that also included other sporadic cases

**Modification Type:** Clarification, Gene-specific, Strength

---

### PP5 - Reputable Source

**Original ACMG Summary:** Reputable source recently reports variant as pathogenic, but the evidence is not available to the laboratory to perform an independent evaluation.

***Not Applicable.*** This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PMID: 29543229).

---

## Benign Criteria

### BA1 - Allele Frequency >5%

**Original ACMG Summary:** Allele frequency is above 5% in population databases.

**VCEP Specification (Stand Alone):**
- Allele frequency **in males** is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium in the subpopulation with the highest frequency.

**Modification Type:** Clarification

---

### BS1 - Frequency Greater Than Expected

**Original ACMG Summary:** Allele frequency is greater than expected for disorder.

**VCEP Specification (Strong):**
- Allele frequency **in males** >= 8.3x10^-5 (based on the most frequent pathogenic allele)

**Modification Type:** Gene-specific

---

### BS2 - Observed in Healthy Adult

**Original ACMG Summary:** Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

**VCEP Specification (Strong):**
- Only count males over age 30 with a documented eye examination with functional studies (normal ERG or FAF)

**Modification Type:** Disease-specific, Gene-specific

---

### BS3 - Functional Studies (No Effect)

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

***Not Applicable*** for RPGR.

---

### BS4 - Lack of Segregation

**Original ACMG Summary:** Lack of segregation in affected members of a family.

**VCEP Specification (Strong):**
- For maternally inherited variants in RPGR, a variant present in a clinically verified (documented with a normal eye examination with functional studies including a normal ERG) unaffected male over age 30 could be used to establish this code.
- Inheritance is complicated in consanguineous families and in dual diagnoses situations so panel testing of unaffected members required to confirm presence of the variant.

**Modification Type:** Clarification, Disease-specific, Gene-specific

---

### BP1-BP7 - Benign Supporting

| Criterion | Status | Strength | Specification |
|-----------|--------|----------|---------------|
| **BP1** | Not Applicable | — | Missense variant in a gene for which primarily truncating variants are known to cause disease. |
| **BP2** | Not Applicable | — | X-linked gene. |
| **BP3** | Applicable | Supporting | Use for ORF15 repetitive regions only (amino acids 585-1078). These events can be multiple and large (e.g. 9 plus 15 total 20-30 bp is known, a single 21bp event is common). ORF15 encompasses residues 585-1152, with UniProt identifying particularly disordered regions between 609-776, 790-906, and 989-1020. |
| **BP4** | Applicable | Multiple strengths | See table below |
| **BP5** | Not Applicable | — | Variant found in a case with an alternate molecular basis for disease. |
| **BP6** | Not Applicable | — | Not for use per ClinGen SVI VCEP Review Committee (PMID: 29543229). |
| **BP7** | Applicable | Supporting | Synonymous variants or noncoding variants with no impact on splicing (SpliceAI <= 0.2) AND PhyloP < 0 for conservation. |

#### BP4 Strength Levels

| Strength | Missense Variants | Synonymous / Noncoding Variants |
|----------|-------------------|-------------------------------|
| **Stand Alone** | REVEL <= 0.003 | — |
| **Strong (BP4_Strong)** | REVEL 0.004 - 0.016 | SpliceAI <= 0.1 |
| **Moderate (BP4_Moderate)** | REVEL 0.017 - 0.183 | SpliceAI <= 0.1 |
| **Supporting (BP4)** | REVEL 0.184 - 0.290 | SpliceAI <= 0.1 |

**Modification Type:** General recommendation

#### BP7 Splice Region Exclusions (positions excluded from BP7)

- Synonymous substitutions in the first base of an exon
- Synonymous substitutions in the last three bases of an exon
- +1 through +7 of the donor sequence after an exon
- -1 through -21 of the acceptor sequence before an exon

---

## Rules for Combining Criteria

### Point-Based Classification System (PMID: 32720330)

This VCEP uses the point-based combining scoring system rather than the standard auto-calculation.

#### Point Values for Evidence Categories

| Evidence Strength | Pathogenic Points | Benign Points |
|-------------------|-------------------|---------------|
| Indeterminate | 0 | 0 |
| Supporting | 1 | -1 |
| Moderate | 2 | -2 |
| Strong | 4 | -4 |
| Very Strong | 8 | -8 |

#### Point-Based Classification Thresholds

| Category | Point Range |
|----------|------------|
| **Pathogenic** | >= 10 |
| **Likely Pathogenic** | 6 - 9 |
| **Uncertain Significance** | 0 - 5 |
| **Likely Benign** | -1 to -6 |
| **Benign** | <= -7 |

### Pathogenic Classification (Traditional Combining Rules)

| Criteria Combination |
|---------------------|
| 1 Very Strong *(PVS1, PS2_Very Strong, PS4_Very Strong)* **AND** >= 1 Strong *(PVS1_Strong, PS1, PS2, PS4, PM4_Strong, PP1_Strong, PP3_Strong)* |
| 1 Very Strong **AND** >= 2 Moderate *(PVS1_Moderate, PS1_Moderate, PS2_Moderate, PS4_Moderate, PM4, PM5, PM6, PP1_Moderate, PP3_Moderate, PP4_Moderate)* |
| 1 Very Strong **AND** 1 Moderate **AND** 1 Supporting *(PVS1_Supporting, PS2_Supporting, PS3_Supporting, PS4_Supporting, PM2_Supporting, PM5_Supporting, PM6_Supporting, PP1, PP3, PP4)* |
| 1 Very Strong **AND** >= 2 Supporting |
| >= 2 Strong |
| 1 Strong **AND** >= 3 Moderate |
| 1 Strong **AND** 2 Moderate **AND** >= 2 Supporting |
| 1 Strong **AND** 1 Moderate **AND** >= 4 Supporting |

### Likely Pathogenic Classification

| Criteria Combination |
|---------------------|
| 1 Very Strong **AND** 1 Moderate |
| 1 Very Strong **AND** >= 1 Supporting |
| 1 Strong **AND** 1 Moderate |
| 1 Strong **AND** >= 2 Supporting |
| >= 3 Moderate |
| 2 Moderate **AND** >= 2 Supporting |
| 1 Moderate **AND** >= 4 Supporting |
| 1 Strong **AND** 2 Moderate |

### Benign Classification

| Criteria Combination |
|---------------------|
| >= 2 Strong *(BS1, BS2, BS4, BP4_Strong)* |
| 1 Stand Alone *(BA1)* |

### Likely Benign Classification

| Criteria Combination |
|---------------------|
| 1 Strong *(BS1, BS2, BS4, BP4_Strong)* **AND** 1 Supporting *(BP3, BP4, BP7)* |
| >= 2 Supporting *(BP3, BP4, BP7)* |

---

## Appendices

### Appendix A: Criteria Not Applicable for RPGR

The following criteria are **Not Applicable** for RPGR and should not be used:

| Criterion | Reason |
|-----------|--------|
| PM1 | See PM2_Supporting |
| PM3 | X-linked gene (not recessive) |
| PM6 | See PS2 for de novo data; maternity confirmation required |
| PP2 | Not applicable |
| PP5 | Not for use per ClinGen SVI (PMID: 29543229) |
| BP1 | Not applicable |
| BP2 | X-linked gene |
| BP5 | Not applicable |
| BP6 | Not for use per ClinGen SVI (PMID: 29543229) |
| BS3 | Not applicable |

### Appendix B: Population Frequency Thresholds Summary

| Criterion | Threshold (in males) | Strength |
|-----------|---------------------|----------|
| BA1 | > 5% (0.05) | Stand Alone |
| BS1 | >= 8.3x10^-5 (0.000083) | Strong |
| PM2 | <= 5x10^-5 (0.00005) | Supporting |

### Appendix C: Reference PMIDs

| PMID | Reference |
|------|-----------|
| 30192042 | Abou Tayoun AN et al. Recommendations for interpreting the loss of function PVS1 ACMG/AMP variant criterion. *Hum Mutat* (2018) 39(11):1517-1524. |
| 8673101 | Meindl A et al. A gene (RPGR) with homology to the RCC1 guanine nucleotide exchange factor is mutated in X-linked retinitis pigmentosa (RP3). *Nat Genet* (1996) 13(1):35-42. |
| 32860923 | De Silva SR et al. The X-linked retinopathies: Physiological insights, pathogenic mechanisms, phenotypic features and novel therapies. *Prog Retin Eye Res* (2021) 82:100898. |
| 10932196 | Vervoort R et al. Mutational hot spot within a new RPGR exon in X-linked retinitis pigmentosa. *Nat Genet* (2000) 25(4):462-6. |
| 30622176 | Zhang Q et al. Disruption of RPGR protein interaction network is the common feature of RPGR missense variations that cause XLRP. *Proc Natl Acad Sci USA* (2019) 116(4):1353-1360. |
| 20631154 | Murga-Zamalloa CA et al. Interaction of RPGR with RAB8A GTPase: implications for cilia dysfunction and photoreceptor degeneration. *Hum Mol Genet* (2010) 19(18):3591-8. |
| 14691151 | Hong DH et al. Dominant, gain-of-function mutant produced by truncation of RPGR. *Invest Ophthalmol Vis Sci* (2004) 45(1):36-41. |
| 30567410 | Nanda A et al. Exploring the Variable Phenotypes of RPGR Carrier Females in Assessing their Potential for Retinal Gene Therapy. *Genes (Basel)* (2018) 9(12). |
| 11950860 | Rozet JM et al. Dominant X linked retinitis pigmentosa is frequently accounted for by truncating mutations in exon ORF15 of the RPGR gene. *J Med Genet* (2002) 39(4):284-5. |
| 36413997 | Pejaver V et al. Calibration of computational tools for missense variant pathogenicity classification and ClinGen recommendations for PP3/BP4 criteria. *Am J Hum Genet* (2022) 109(12):2163-2177. |
| 37352859 | Walker LC et al. Using the ACMG/AMP framework to capture evidence related to predicted and observed impact on splicing. *Am J Hum Genet* (2023) 110(7):1046-1067. |
| 32720330 | Tavtigian SV et al. Fitting a naturally scaled point system to the ACMG/AMP variant classification guidelines. *Hum Mutat* (2020) 41(10):1734-1737. |
| 29543229 | ClinGen SVI recommendation against PP5/BP6 use. |
| 27162334 | Sun X et al. Loss of RPGR glutamylation underlies the pathogenic mechanism of retinal dystrophy caused by RPGR mutations. *Proc Natl Acad Sci USA* (2016) 113(21):E2925-34. |
| 25630948 | Da Costa R et al. Neidhardt J. Assessing ciliopathy phenotype rescue in human fibroblasts. *Gene Ther* (2015) 22(5):461-8. |
| 33805381 | Stop-loss variant effect study (RPGR c.3457). |
| 10958648 | Protein-protein interaction reference. |
| 23213406 | Protein-protein interaction reference. |
| 9990021 | Protein-protein interaction reference. |
| 36445968 | Protein-protein interaction and glutamylation reference. |

### Appendix D: Pilot Variant Example

**NM_001034853.2(RPGR):c.730A>T (p.Lys244Ter)**
- Classification: **Pathogenic**
- Criteria applied: PVS1 (8 points) + PM2_Supporting (1 point) + PP1_Moderate (2 points) + PP4 (1 point) = 12 points
- This nonsense variant introduces a premature stop codon into exon 7 of 15, predicted to lead to NMD. Absent from gnomAD. Segregates with retinal dystrophy through at least 4 affected meioses from 1 family. Proband phenotype scores 5 points (X-linked inheritance 2 pts, night blindness 0.5, females milder phenotype 1, rod > cone 1, visual field constriction 0.5).

### Appendix E: HPO Terms Commonly Used for RPGR

| HPO Term | HPO ID |
|----------|--------|
| X-linked inheritance | HP:0001417 |
| Rod-cone dystrophy | HP:0000510 |
| Cone dystrophy | HP:0008020 |
| Reduced electroretinogram | HP:0000654 |
| Undetectable/Abolished ERG | HP:0000550 |
| Nyctalopia | HP:0000662 |
| Myopia | HP:0000545 |
| High myopia | HP:0011003 |
| Pigmentary retinopathy | HP:0000580 |
| Macular atrophy | HP:0007401 |
| Reduced visual acuity | HP:0007663 |
| Progressive visual loss | HP:0000529 |
| Peripheral visual field loss | HP:0007994 |
| Visual field constriction | HP:0001133 |
| Color vision defect | HP:0000551 |
| Optic disc pallor | HP:0000543 |
| Photophobia | HP:0000613 |
| Abnormal fundus autofluorescence | HP:0030602 |
| Attenuation of retinal blood vessels | HP:0007843 |

---

## Version History

| Version | Date | Notes |
|---------|------|-------|
| 1.0.0 | 5/16/2025 | Initial release. Pilot Rules Submitted as of 01/22/2024. |

---

*This document was compiled from ClinGen X-linked Inherited Retinal Disease VCEP specifications and ClinGen SVI recommendations. For the most current version, please refer to the ClinGen website.*
