# ClinGen Myeloid Malignancy VCEP Variant Interpretation Guidelines for RUNX1

**Version:** 3.0.0
**Released:** 8/14/2025
**Affiliation:** Myeloid Malignancy Variant Curation Expert Panel (MM-VCEP)
**Based on:** Tavtigian et al., 2020 - Bayesian adaptation of Richards et al., 2015 ACMG/AMP Guidelines

---

## Gene Information

| Attribute | Value |
|-----------|-------|
| **Gene** | RUNX1 (HGNC:10471) |
| **HGNC Name** | RUNX family transcription factor 1 |
| **Transcript** | NM_001754.4 (RUNX1c) |
| **Disease** | Hereditary thrombocytopenia and hematologic cancer predisposition syndrome (MONDO:0011071) |
| **Inheritance** | Autosomal dominant |

---

## Release Notes (v3.0.0)

1. New gnomAD MAF threshold for PM2_supporting ≤ 0.00005 to account for larger population in gnomAD v4.
2. Upgraded strength of PM1 to PM1_strong when used for missense variants at the following residues: R107, K110, A134, R162, R166, S167, R169, G170, K194, T196, D198, R201, R204. Added a caveat to not use PM5/PS1 at any level if PM1 was applied.
3. Upgraded strength of PM4 to PM4_strong for in-frame deletions/insertions at the same 13 hotspot residues. Added an allowance to use PM4 for stop-loss variants.
4. Established PVS1_variable (RNA) and BP7_variable (RNA) to be used when RNA data is available for splicing variants. PS1 is now able to be used for splicing variants with the same predicted splicing event as a known pathogenic/likely pathogenic splicing variant.
5. Conservation data is no longer considered when applying BP7. BP7 is limited to intronic variants, and synonymous variants which don't occur in the last 3 nucleotides preceding a canonical donor splice site or the first nucleotide following a canonical acceptor splice site.
6. Revised PM5 to account for Grantham scores when evaluating missense variants.

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
   - [BA1 - Allele Frequency ≥0.15%](#ba1---allele-frequency-015)
   - [BS1 - Frequency Greater Than Expected](#bs1---frequency-greater-than-expected)
   - [BS2 - Observed in Healthy Adult](#bs2---observed-in-healthy-adult)
   - [BS3 - Functional Studies (No Effect)](#bs3---functional-studies-no-effect)
   - [BS4 - Lack of Segregation](#bs4---lack-of-segregation)
   - [BP1-BP7 - Benign Supporting](#bp1-bp7---benign-supporting)
3. [Rules for Combining Criteria](#rules-for-combining-criteria)
4. [Appendices](#appendices)

---

## RUNX1 Phenotypic Criteria

The phenotype of a deleterious RUNX1 mutation encompasses at least one of the following three criteria:

1. **Thrombocytopenia:** Mild to moderate thrombocytopenia with normal platelet size and volume in the absence of other causative factors such as autoimmune (e.g., antibodies against platelet surface antigens) or drug-related thrombocytopenia.
2. **Platelet defects:** Platelet ultrastructural and/or functional defects including platelet alpha or dense granule secretion defects or impaired platelet aggregation — particularly in response to collagen and epinephrine.
3. **Hematologic malignancy:** Diagnosis of a hematologic malignancy, most commonly affecting the myeloid lineage causing acute myeloid leukemia (AML) or myelodysplastic syndrome (MDS), less frequently involving the lymphoid lineage manifesting as T-acute lymphoblastic leukemia (T-ALL). There are rare case-reports of patients with germline RUNX1 mutations and mixed myeloproliferative syndromes/MDS such as chronic myelomonocytic leukemia, as well as case-reports of patients with B-ALL and hairy-cell leukemia.

---

## Pathogenic Criteria

### PVS1 - Null Variant

**Original ACMG Summary:** Null variant (nonsense, frameshift, canonical ±1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.

**VCEP Specifications:**

MM-VCEP notes:
1. Use RUNX1 isoform c as the default transcript (NM_001754.4), since this is the isoform used for annotation by most clinical laboratories.
2. Three major isoforms (a, b, c) are expressed by use of two promoters and alternative splicing. RUNX1 LOF variants are a common mechanism of disease in FPD/AML. C-terminal truncating variants not predicted to undergo nonsense-mediated mRNA decay (NMD) are classified as PVS1_strong. Deletions of exon 1-3, presumably only affecting RUNX1 isoform c, meet PVS1_moderate.
3. Most splicing effects are based on predictions. Rules can be modified when RNA evidence becomes available using Walker et al., 2023 (PMID: 37352859) as a guide.

**PVS1_Variable (RNA):** When RNA/splicing data is available for a variant, apply PVS1 at the appropriate strength level based on the predicted effect of the aberrant mRNA on protein translation as it corresponds to the PVS1_Variable splicing table. Strength may also be modified based on the quality of the RNA analysis. For "leaky" splice sites, strength level should be decreased by one if a near-complete impact is demonstrated, but no code should be applied if an incomplete impact is demonstrated.

**RNA quality considerations (ranked best to worst):**
1. Comparison to a control is necessary
2. Patient RNA is better than minigene assays
3. Primers should capture the possibility of multi-exonic/multi-cassette events
4. NMD inhibitors (e.g., puromycin, PAXgene tubes) should be used, particularly when the predicted effect is NMD
5. Quantification: SNP analysis > PSI analysis > capillary electrophoresis > gel band density estimation
6. Multiple studies are better than a single study

#### Strength Levels

| Strength | Criteria | Default Points |
|----------|----------|----------------|
| **Very Strong (PVS1)** | Per modified RUNX1 PVS1 decision tree for SNVs and CNVs and table of splicing effects | 8 |
| **Strong (PVS1_Strong)** | Per modified RUNX1 PVS1 decision tree for SNVs and CNVs and table of splicing effects | 4 |
| **Moderate (PVS1_Moderate)** | Per modified RUNX1 PVS1 decision tree for SNVs and CNVs and table of splicing effects | 2 |

#### PVS1 Decision Tree for SNVs (Nonsense and Frameshift)

```
RUNX1 (NM_001754.4) - Nonsense or Frameshift
│
├── Predicted to undergo NMD
│   ├── Exon is absent from RUNX1 isoform a and b
│   │   └── c.1-c.97 → N/A (PVS1 not applicable)
│   │
│   └── Exon is present in all biologically relevant transcripts
│       ├── Nonsense: c.98-c.916
│       ├── Frameshift (-1): c.98-c.758
│       └── Frameshift (+1): c.98-c.779
│       → PVS1 (Very Strong)
│
└── Not predicted to undergo NMD
    └── Truncated/altered region is critical to protein function
        ├── Nonsense: c.917-c.1440
        ├── Frameshift (-1): c.759-c.1440
        └── Frameshift (+1): c.780-c.1440
        → PVS1_Strong
```

#### PVS1 Decision Tree for CNVs (Single or Multi-exon Deletions)

```
RUNX1 (NC_000021.9) - Single or multi-exon deletion
│
├── Full gene deletion
│   → Pathogenic Classification
│
├── Disrupts reading frame
│   └── Truncated/altered region is critical to protein function*
│       ├── Yes → PVS1_Strong
│       └── Follow the same predictions under the RUNX1 PVS1
│           decision tree for SNVs
│
└── Preserves reading frame or impact on reading frame is unknown
    └── Role of region in protein function is unknown
        └── LOF variants in this exon are not frequent in population
            and exon is present in biologically relevant transcript
            ├── Variant removes <10% of protein# → PVS1_Moderate
            └── Otherwise → PVS1_Strong
```

#### Canonical Splice Site Variants — Summary of Splicing Effects

| Intron | GT-AG ±1,2 Splice Site | Location | Predicted or Published Effects | Classification |
|--------|------------------------|----------|-------------------------------|----------------|
| Intron 2 | Donor | c.58 | Only affect isoform c, but not isoform a and b | N/A |
| Intron 2 | Acceptor | c.59 | Only affect isoform c, but not isoform a and b | N/A |
| Intron 2 | Donor | c.97 | Only affect isoform c, but not isoform a and b | N/A |
| Intron 3 | Acceptor | c.98 | Only affect isoform c, but not isoform a and b | N/A |
| | | | If Skip Exon 4 with frameshift on isoform c AND cause nonsense/frameshift on isoform a/b | **PVS1** |
| Intron 3 | Donor | c.351 | Skip Exon 4 with frameshift | **PVS1** |
| Intron 4 | Acceptor | c.352 | Skip Exon 5 with frameshift OR Use of Cryptic splice acceptor with a frameshift, PMID: 10508512 | **PVS1** |
| Intron 4 | Donor | c.508 | Skip Exon 5 with frameshift OR Use of Cryptic splice donor with a frameshift, PMID: 11830488 | **PVS1** |
| Intron 5 | Acceptor | c.509 | Skip Exon 6 with in frame Δ171-205 and G170 (GGG→GGA), deletion in RHD | **PVS1_Strong** |
| Intron 5 | Donor | c.613 | Skip Exon 6 with in frame Δ171-205 and G170 (GGG→GGA), deletion in RHD | **PVS1_Strong** |
| Intron 6 | Acceptor | c.614 | Skip Exon 7 with in frame Δ206-269 and R205N (AGG→AAT), remove 13% of protein | **PVS1_Strong** |
| Intron 6 | Donor | c.805 | Skip Exon 7 with in frame Δ206-269 and R205N (AGG→AAT), remove 13% of protein | **PVS1_Strong** |
| Intron 7 | Acceptor | c.806 | Skip Exon 8 with in frame Δ270-323 and D269A (GAT→GCG), deletion in TAD | **PVS1_Strong** |
| Intron 7 | Donor | c.967 | Skip Exon 8 with in frame Δ270-323 and D269A (GAT→GCG), deletion in TAD | **PVS1_Strong** |
| Intron 8 | Acceptor | c.968 | Likely use of cryptic site, the last exon contains 33% of protein | **PVS1_Strong** |

---

### PS1 - Same Amino Acid Change

**Original ACMG Summary:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change. Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:**

MM-VCEP notes:
1. The previously established pathogenic variant must be reviewed by the MM-VCEP and asserted pathogenic/likely pathogenic before this rule can be applied.
2. For missense variants, RNA data or agreement in splicing predictor show no impact on splicing.
3. For splice site variants, do not apply this code except for variants in the canonical donor/acceptor ("dinucleotide") sites, the U2 donor motif (last 3 bases of the exon and 6 nucleotides of the intron), or the U2 acceptor motif (20 nucleotides of the intron and 1st base of the exon). Splicing predictions for the variant being evaluated and the known P/LP variant should match with at least similar scores. Do not apply for +2G>C variants.

#### Strength Levels

**For missense variants:**

| Strength | Criteria | Default Points |
|----------|----------|----------------|
| **Strong (PS1)** | Same amino acid change as a previously established **pathogenic** variant regardless of nucleotide change | 4 |
| **Moderate (PS1_Moderate)** | Same amino acid change as a previously established **likely pathogenic** variant regardless of nucleotide change | 2 |

**For splice site variants:**

| Strength | Criteria |
|----------|----------|
| **PS1_Variable** | Follow recommendations from the ClinGen SVI Splicing Subgroup (Walker et al., 2023, PMID: 37352859) |

#### PS1 Splicing Application Table

| Variant Under Assessment (VUA) | Baseline Code Applicable to VUA | Position of Comparison Variant Relative to VUA | PS1 Code with P Comparison Variant | PS1 Code with LP Comparison Variant |
|---|---|---|---|---|
| Located outside splice donor/acceptor ±1,2 dinucleotide positions | PP3 | Same nucleotide | PS1 | PS1_Moderate |
| Located outside splice donor/acceptor ±1,2 dinucleotide positions | PP3 | Within same splice donor/acceptor motif (including at ±1,2 positions) | PS1_Moderate | PS1_Supporting |
| Located at splice donor/acceptor ±1,2 dinucleotide positions | PVS1 | Within same splice donor/acceptor motif | PS1_Supporting | N/A |
| Located at splice donor/acceptor ±1,2 dinucleotide positions | PVS1 | Within same splice donor/acceptor region, but outside ±1,2 dinucleotide* | PS1_Supporting | PS1_Supporting |
| Located at splice donor/acceptor ±1,2 dinucleotide positions | PVS1_Strong, PVS1_Moderate, or PVS1_Supporting | Within same splice donor/acceptor motif | PS1 | PS1_Supporting |
| Located at splice donor/acceptor ±1,2 dinucleotide positions | PVS1_Strong, PVS1_Moderate, or PVS1_Supporting | Within same splice donor/acceptor motif, but outside ±1,2 dinucleotide* | PS1_Supporting | PS1_Supporting |

**Prerequisites for all:** The predicted event of the VUA must precisely match the predicted event of the comparison (likely) pathogenic variant (e.g., both predicted to lead to exon skipping, or both to lead to enhanced use of a cryptic splice motif). AND the strength of the prediction for the VUA must be of similar or higher strength than the comparison [likely] pathogenic variant.

*\*If relevant, splicing assay data for a pathogenic variant outside a ±1,2 dinucleotide position may be used to update a PVS1 decision tree and hence the applicable PVS1 code for a ±1,2 dinucleotide variant.*

---

### PS2 - De Novo (Confirmed)

**Original ACMG Summary:** De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.

**VCEP Specifications:**

MM-VCEP notes:
1. The FPD/AML phenotype is not highly specific and there is substantial genetic heterogeneity. The maximum allowable value is **1 point** contributing to the overall score.
2. The phenotype of a deleterious RUNX1 mutation encompasses at least one of the three RUNX1-phenotypic criteria (see [RUNX1 Phenotypic Criteria](#runx1-phenotypic-criteria)).
3. No family history is defined as the absence of the variant and any of the RUNX1-phenotypic criteria in first and second-degree relatives.
4. The maximum allowable strength by combining PS2 and PM6 is to apply one moderate or two supporting rules (maximum 1 point).

Following the ClinGen SVI Working Group guidance, de novo RUNX1 variants are scored at the **third tier** of the point-based system ("Phenotype consistent with gene but not highly specific and high genetic heterogeneity"):

| Strength | Criteria | Default Points |
|----------|----------|----------------|
| **Moderate (PS2_Moderate)** | ≥ 2 proven de novo occurrences (both maternity and paternity confirmed) in patients with FPD/AML phenotype | 2 |
| **Supporting (PS2_Supporting)** | 1 proven de novo occurrence (both maternity and paternity confirmed) in a patient with FPD/AML phenotype | 1 |

> **Important:** Maximum allowable combined value for PS2 + PM6 = 1 point.

---

### PS3 - Functional Studies

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.

**VCEP Specifications:**

MM-VCEP notes:
1. **Transactivation assays** demonstrating altered transactivation compared to wildtype (wt) are the primary functional study. Promoter sequences of M-CSFR, PF4, C-FMS, and GZMB, containing consensus RUNX1 binding sites TGTGGT, have been used. The transactivation assay must include wt and known pathogenic controls, as well as co-expression with CBFβ.
2. **Secondary assays** include:
   - Electrophoretic mobility shift assays and yeast hybrid assays (decreased DNA binding affinity)
   - Co-immunoprecipitation, FRET, and affinity assays (diminished heterodimerization with CBFβ)
   - Immunofluorescence and cell-fractionation with Western Blot (abnormal cellular localization)
   - Sorted primary hematopoietic stem and progenitor cells (reduced colony-forming potential)
   - Xenotransplantation experiments (abnormal function in vivo)

#### Strength Levels

| Strength | Criteria | Default Points |
|----------|----------|----------------|
| **Strong (PS3)** | Transactivation assays demonstrating altered transactivation (<20% of wt, and/or reduced to levels similar to well-established pathogenic variants such as R201Q or R166Q) **AND** data from a secondary assay demonstrating altered function. Not applicable if variant meets PVS1. If variant meets PVS1_strong, upgrade to PVS1. | 4 |
| **Moderate (PS3_Moderate)** | Transactivation assays demonstrating altered transactivation (<20% of wt and/or reduced to levels similar to well-established pathogenic variants such as R201Q or R166Q) **OR** ≥ 2 secondary assays demonstrating altered function | 2 |
| **Supporting (PS3_Supporting)** | Transactivation assays demonstrating enhanced transactivation (>115% of wt) | 1 |

---

### PS4 - Prevalence in Affected

**Original ACMG Summary:** The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.

**VCEP Specifications:**

MM-VCEP notes:
1. There is currently no published RUNX1 case-control study. The MM-VCEP created a "quasi-case-control study" with the estimated number of probands worldwide and the overall gnomAD population as control cohort.
2. To apply this code, the proband must meet the RUNX1-phenotypic criteria (see PS2) and the variant must be either absent from gnomAD or only present once.

#### Strength Levels

| Strength | Criteria | Default Points |
|----------|----------|----------------|
| **Strong (PS4)** | ≥ 4 probands meeting at least one of the RUNX1-phenotypic criteria (OR 127.1) | 4 |
| **Moderate (PS4_Moderate)** | 2-3 probands meeting at least one of the RUNX1-phenotypic criteria (OR 63.5-95.3) | 2 |
| **Supporting (PS4_Supporting)** | 1 proband meeting at least one of the RUNX1-phenotypic criteria (OR 31.8) | 1 |

---

### PM1 - Mutational Hot Spot

**Original ACMG Summary:** Located in a mutational hot spot and/or critical and well-established functional domain without benign variation.

**VCEP Specifications:**

MM-VCEP notes:
1. The Runt Homology Domain (RHD) has been established as a highly conserved DNA binding domain without any benign variation in ClinVar. Thirteen somatic and/or germline mutational hotspots within the RHD have been identified: **R107, K110, A134, R162, R166, S167, R169, G170, K194, T196, D198, R201, R204**.
2. Variants in other parts of the RHD (AA 89-204) have been described as likely pathogenic/pathogenic before, with additional evidence of germline P/LP RUNX2 variants affecting AA 89 and 94 (PMID: 17290219), a gene with a Runt Homology Domain with 90% sequence homology with RUNX1. AA 89 is also still part of the β-sheet of the CBF heterodimerization domain, which is functionally important.
3. No reported germline RUNX1 mutations in AA residues 77-88 of the RHD to date.

#### Strength Levels

| Strength | Criteria | Default Points |
|----------|----------|----------------|
| **Strong (PM1_Strong)** | Variant affecting one of the following 13 AA residues within the RHD: **R107, K110, A134, R162, R166, S167, R169, G170, K194, T196, D198, R201, R204** | 4 |
| **Supporting (PM1_Supporting)** | Variant affecting one of the other AA residues **89-204** within the RHD | 1 |

---

### PM2 - Absent from Controls

**Original ACMG Summary:** Absent from controls (or at extremely low frequency if recessive) in population databases.

**VCEP Specification (Supporting only):**

| Strength | Criteria | Default Points |
|----------|----------|----------------|
| **Supporting (PM2_Supporting)** | Minor allele frequency **≤ 0.00005** with at least 2,000 alleles tested and 20x coverage at the position | 1 |

---

### PM3 - In Trans with Pathogenic

**Original ACMG Summary:** For recessive disorders, detected in trans with a pathogenic variant.

**VCEP Specification:** **Not Applicable**

FPD/AML is inherited in an autosomal dominant manner; PM3 is not applicable.

---

### PM4 - Protein Length Changes

**Original ACMG Summary:** Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

**VCEP Specifications:**

MM-VCEP notes:
1. The RHD has been established as a highly conserved DNA binding domain without any benign variation in ClinVar. The same 13 hotspot residues as PM1 apply.
2. Variants in other parts of the RHD (AA 89-204) have been described as LP/P before, with supporting evidence from RUNX2.
3. PM4 is now also applicable to stop-loss variants causing a protein extension.

#### Strength Levels

**For in-frame deletion/insertion variants:**

| Strength | Criteria | Default Points |
|----------|----------|----------------|
| **Strong (PM4_Strong)** | In-frame deletion/insertion impacting at least one of the following AA residues within the RHD: **R107, K110, A134, R162, R166, S167, R169, G170, K194, T196, D198, R201, R204** | 4 |
| **Moderate (PM4)** | In-frame deletion/insertion impacting at least one of the following AA residues within the RHD: R107, K110, A134, R162, R166, S167, R169, G170, K194, T196, D198, R201, R204 | 2 |
| **Supporting (PM4_Supporting)** | In-frame deletion/insertion impacting at least one of the other AA residues **89-204** within the RHD | 1 |

**For stop-loss variants:**

| Strength | Criteria | Default Points |
|----------|----------|----------------|
| **Moderate (PM4)** | Stop-loss variant causing a protein extension | 2 |

---

### PM5 - Novel Missense at Same Residue

**Original ACMG Summary:** Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.

**VCEP Specifications:**

MM-VCEP notes:
1. RNA data or SpliceAI ≤ 0.20 required (variant must not impact splicing).
2. The previously established pathogenic variant must be reviewed by the MM-VCEP and asserted P/LP before this rule can be applied.
3. For missense variants, the **Grantham score** of the alternate residue of the new variant should be equal or higher to that of the alternate residue of the known P/LP variant.
4. There are at least two nonsense/frameshift variants curated as pathogenic in each exon (exons 3-7) without applying PM5_Supporting.

#### Strength Levels

| Strength | Criteria | Default Points |
|----------|----------|----------------|
| **Strong (PM5_Strong)** | Missense change at an AA residue where **≥ 2** different missense changes have been determined to be pathogenic before (after accounting for Grantham scores) | 4 |
| **Moderate (PM5)** | Missense change at an AA residue where a different missense change has been determined to be **pathogenic** before (after accounting for Grantham scores) | 2 |
| **Supporting (PM5_Supporting)** | Missense change at an AA residue where a different missense change has been determined to be **likely pathogenic** before (after accounting for Grantham scores). Also applied to nonsense/frameshift variants downstream of c.98 (in transcript NM_001754.4) | 1 |

**Caveats:**
- The variant must not impact splicing based on RNA assay or SpliceAI ≤ 0.20.
- Nonsense/frameshift variants before c.98 only affect one of the RUNX1 functional transcripts. PVS1 is also not applicable in this region based on the RUNX1 PVS1 decision tree.
- **PM5 cannot be used if PM1 was applied at any strength level.**

#### Grantham Score Reference

The Grantham score measures the physicochemical distance between amino acids. When applying PM5, the Grantham score of the new variant's alternate residue should be **equal or higher** than that of the known P/LP variant's alternate residue.

| | Arg | Leu | Pro | Thr | Ala | Val | Gly | Ile | Phe | Tyr | Cys | His | Gln | Asn | Lys | Asp | Glu | Met | Trp |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Ser** | 110 | 145 | 74 | 58 | 99 | 124 | 56 | 142 | 155 | 144 | 112 | 89 | 68 | 46 | 121 | 65 | 80 | 135 | 177 |
| **Arg** | | 102 | 103 | 71 | 112 | 96 | 125 | 97 | 97 | 77 | 180 | 29 | 43 | 86 | 26 | 96 | 54 | 91 | 101 |
| **Leu** | | | 98 | 92 | 96 | 32 | 138 | 5 | 22 | 36 | 198 | 99 | 113 | 153 | 107 | 172 | 138 | 15 | 61 |
| **Pro** | | | | 38 | 27 | 68 | 42 | 95 | 114 | 110 | 169 | 77 | 76 | 91 | 103 | 108 | 93 | 87 | 147 |
| **Thr** | | | | | 58 | 69 | 59 | 89 | 103 | 92 | 149 | 47 | 42 | 65 | 78 | 85 | 65 | 81 | 128 |
| **Ala** | | | | | | 64 | 60 | 94 | 113 | 112 | 195 | 86 | 91 | 111 | 106 | 126 | 107 | 84 | 148 |
| **Val** | | | | | | | 109 | 29 | 50 | 55 | 192 | 84 | 96 | 133 | 97 | 152 | 121 | 21 | 88 |
| **Gly** | | | | | | | | 135 | 153 | 147 | 159 | 98 | 87 | 80 | 127 | 94 | 98 | 127 | 184 |
| **Ile** | | | | | | | | | 21 | 33 | 198 | 94 | 109 | 149 | 102 | 168 | 134 | 10 | 61 |
| **Phe** | | | | | | | | | | 22 | 205 | 100 | 116 | 158 | 102 | 177 | 140 | 28 | 40 |
| **Tyr** | | | | | | | | | | | 194 | 83 | 99 | 143 | 110 | 160 | 122 | 36 | 37 |
| **Cys** | | | | | | | | | | | | 174 | 154 | 139 | 202 | 154 | 170 | 196 | 215 |
| **His** | | | | | | | | | | | | | 24 | 68 | 32 | 81 | 40 | 87 | 115 |
| **Gln** | | | | | | | | | | | | | | 46 | 53 | 61 | 29 | 101 | 130 |
| **Asn** | | | | | | | | | | | | | | | 94 | 23 | 42 | 142 | 174 |
| **Lys** | | | | | | | | | | | | | | | | 101 | 56 | 95 | 110 |
| **Asp** | | | | | | | | | | | | | | | | | 45 | 160 | 181 |
| **Glu** | | | | | | | | | | | | | | | | | | 126 | 152 |
| **Met** | | | | | | | | | | | | | | | | | | | 67 |

*(Grantham, 1974, PMID: 4843792)*

---

### PM6 - De Novo (Assumed)

**Original ACMG Summary:** Assumed de novo, but without confirmation of paternity and maternity.

**VCEP Specifications:**

MM-VCEP notes:
1. FPD/AML phenotype is not highly specific and there is substantial genetic heterogeneity. The maximum allowable value is **1 point** contributing to the overall score.
2. The phenotype of a deleterious RUNX1 mutation encompasses at least one of the three phenotypic criteria (see PS2).
3. No family history is defined as the absence of the variant and any of the RUNX1-phenotypic criteria in first and second-degree relatives.
4. The maximum allowable strength by combining PS2 and PM6 is to apply one moderate or two supporting rules (maximum 1 point).

Following the SVI guidance, assumed de novo RUNX1 variants are scored at the **third tier** of the point-based system:

| Strength | Criteria | Default Points |
|----------|----------|----------------|
| **Moderate (PM6)** | ≥ 4 assumed de novo occurrences (without confirmation of maternity and paternity) in patients with FPD/AML phenotype | 2 |
| **Supporting (PM6_Supporting)** | 2 or 3 assumed de novo occurrences (without confirmation of maternity and paternity) in patients with FPD/AML phenotype | 1 |

> **Important:** Maximum allowable combined value for PS2 + PM6 = 1 point.

---

### PP1 - Co-segregation

**Original ACMG Summary:** Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.

**VCEP Specifications:**

MM-VCEP notes:
1. The MM-VCEP adopted the SVI-supported approach with additional meioses supporting higher evidence levels based on calculated LOD scores.
2. Affected individuals show at least one of the RUNX1-phenotypic criteria (see PS2).
3. Only genotype and phenotype positive individuals and obligate carriers are counted.
4. The MM-VCEP waived the ACMG/AMP recommendation for demonstrating co-segregation in more than one family given that many RUNX1 variants are unique to families and do not occur in other unrelated families.

#### Strength Levels

| Strength | Meioses | LOD Score | Default Points |
|----------|---------|-----------|----------------|
| **Strong (PP1_Strong)** | ≥ 7 meioses observed within one or across multiple families | ~2.1 | 4 |
| **Moderate (PP1_Moderate)** | 5 or 6 meioses observed within one or across multiple families | ~1.5 | 2 |
| **Supporting (PP1)** | 3 or 4 meioses observed within one or across multiple families | ~0.9 | 1 |

---

### PP2 - Missense in Constrained Gene

**Original ACMG Summary:** Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.

**VCEP Specification:** **Not Applicable**

The recommended cutoff for PP2 by the SVI is a missense constraint z score of ≥ 3.09, which was not met by RUNX1 (2.48 on ExAC and 2.08 on gnomAD). In addition, there are 9 benign/likely benign missense RUNX1 variants in ClinVar.

---

### PP3 - Computational Evidence

**Original ACMG Summary:** Multiple lines of computational evidence support a deleterious effect on the gene or gene product.

**VCEP Specifications:**

MM-VCEP notes:
1. For in-silico evaluation of missense variants, the MM-VCEP recommends using **REVEL**, a meta-predictor combining 13 individual tools with high sensitivity and specificity. REVEL was found to be among the highest performing tools (AUC=1) based on evaluation of 25 germline P/LP and 25 B/LB missense variants in RUNX1.
2. The threshold was based on REVEL scores at 90% sensitivity and 90% specificity, respectively.
3. For splice prediction, **SpliceAI** was found to be the highest performing tool. Thresholds: PP3 ≥ 0.38, BP4 ≤ 0.20.
4. For some variant types where REVEL or SpliceAI scores are not available, multiple other predictors in agreement can be used.
5. PP3 cannot be applied for canonical splice site variants.

#### Strength Levels

| Variant Type | Criteria | Default Points |
|-------------|----------|----------------|
| **Missense variants** | REVEL score ≥ 0.88 **OR** SpliceAI ≥ 0.38 (including creation of cryptic novel splice sites) | 1 |
| **Synonymous and intronic (intron 4-8) variants** | SpliceAI ≥ 0.38 (including creation of cryptic novel splice sites) | 1 |

**Caveats:**
- Do not use for variants with a predicted splicing effect that is proven by RNA analysis. See PVS1_Variable (RNA).
- Do not use for canonical splice site variants.

---

### PP4 - Phenotype Specificity

**Original ACMG Summary:** Patient's phenotype or family history is highly specific for a disease with a single genetic etiology.

**VCEP Specification:** **Not Applicable**

The FPD/AML phenotype is rather unspecific and can be caused by a number of other inherited predisposition syndromes, somatic mutations, or environmental factors that are insufficient to meet the original ACMG/AMP rule PP4.

---

### PP5 - Reputable Source

**Original ACMG Summary:** Reputable source recently reports variant as pathogenic, but the evidence is not available to the laboratory to perform an independent evaluation.

**VCEP Specification:** **Not Applicable**

This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PMID: 29543229).

---

## Benign Criteria

### BA1 - Allele Frequency ≥0.15%

**Original ACMG Summary:** Allele frequency is above 5% in population databases.

**VCEP Specification (Stand Alone):**

MM-VCEP notes:
The threshold was derived using the Whiffin/Ware calculator with a prevalence of 1 in 40, conservative unascertained penetrance of 85%, allelic heterogeneity of 100%, and maximum genetic heterogeneity of 10%. A 95% confidence interval was used.

| Strength | Criteria | Default Points |
|----------|----------|----------------|
| **Stand Alone (BA1)** | Minor allele frequency **≥ 0.0015 (0.15%)** in any general continental population dataset with ≥ 2,000 alleles tested and variant present in ≥ 5 alleles | N/A |

---

### BS1 - Frequency Greater Than Expected

**Original ACMG Summary:** Allele frequency is greater than expected for disorder.

**VCEP Specification (Strong):**

MM-VCEP notes:
Similarly derived using the Whiffin/Ware calculator but with maximum genetic heterogeneity of 1% (one magnitude lower than BA1).

| Strength | Criteria | Default Points |
|----------|----------|----------------|
| **Strong (BS1)** | Minor allele frequency **between 0.00015 (0.015%) and 0.0015 (0.15%)** in any general continental population dataset with ≥ 2,000 alleles tested and variant present in ≥ 5 alleles | -4 |

**Note:** The variant can be classified as likely benign based on BS1 alone if there is no contradictory evidence supporting pathogenicity.

---

### BS2 - Observed in Healthy Adult

**Original ACMG Summary:** Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

**VCEP Specification:** **Not Applicable**

BS2 is not applicable since FPD/AML patients display incomplete penetrance and the average age of onset of hematologic malignancies is 33 years.

---

### BS3 - Functional Studies (No Effect)

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

**VCEP Specifications:**

Same assay framework as PS3 (transactivation assays with wt and known pathogenic controls, co-expression with CBFβ, and secondary assays).

#### Strength Levels

| Strength | Criteria | Default Points |
|----------|----------|----------------|
| **Strong (BS3)** | Transactivation assays demonstrating **normal transactivation (80-115% of wt)** AND data from a secondary assay demonstrating normal function | -4 |
| **Supporting (BS3_Supporting)** | Transactivation assays demonstrating **normal transactivation (80-115% of wt)** | -1 |

---

### BS4 - Lack of Segregation

**Original ACMG Summary:** Lack of segregation in affected members of a family.

**VCEP Specifications:**

This code should only be applied for genotype-negative, phenotype-positive family members.

| Strength | Criteria | Default Points |
|----------|----------|----------------|
| **Strong (BS4)** | Applicable when observed in **≥ 2 informative meioses** | -4 |

---

### BP1-BP7 - Benign Supporting

| Criterion | Status | Specification | Default Points |
|-----------|--------|---------------|----------------|
| **BP1** | Not Applicable | BP1 is not applicable for RUNX1 because both truncating and missense variants cause FPD/AML | — |
| **BP2** | Applicable | Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder or observed in cis with a pathogenic variant in any inheritance pattern. Biallelic pathogenic variants in RUNX1 have never been reported in FPD/AML patients. | -1 |
| **BP3** | Not Applicable | RUNX1 does not contain a repetitive region without known function | — |
| **BP4** | Applicable | **For missense variants:** REVEL score < 0.50 AND SpliceAI ≤ 0.20. **For synonymous and intronic variants:** SpliceAI ≤ 0.20 | -1 |
| **BP5** | Not Applicable | In rare circumstances, a patient can carry two pathogenic variants in genes predisposing to hematologic malignancies | — |
| **BP6** | Not Applicable | Not for use as recommended by ClinGen SVI VCEP Review Committee (PMID: 29543229) | — |
| **BP7** | Applicable | **Synonymous variants** (excluding those in the last 3 nucleotides preceding a canonical donor splice site or the first nucleotide following a canonical acceptor splice site) with SpliceAI Δ scores ≤ 0.20. **Intronic variants** with SpliceAI Δ scores ≤ 0.20. **BP7_Variable (RNA):** Applicable for variants with RNA data, with weighting based on the quality of the available RNA data. | -1 |

---

## Rules for Combining Criteria

### Point-Based Variant Classification

| Category | Point Range |
|----------|-------------|
| **Pathogenic** | ≥ 10 |
| **Likely Pathogenic** | 6 – 9 |
| **Uncertain Significance (VUS)** | 0 – 5 |
| **Likely Benign** | -1 – -6 |
| **Benign** | ≤ -7 |

### Default Point Values Summary

| Criterion | Very Strong (8) | Strong (4) | Moderate (2) | Supporting (1) |
|-----------|----------------|------------|--------------|----------------|
| **PVS1** | PVS1 | PVS1_Strong | PVS1_Moderate | — |
| **PS1** | — | PS1 | PS1_Moderate | — |
| **PS2** | — | — | PS2_Moderate | PS2_Supporting |
| **PS3** | — | PS3 | PS3_Moderate | PS3_Supporting |
| **PS4** | — | PS4 | PS4_Moderate | PS4_Supporting |
| **PM1** | — | PM1_Strong | — | PM1_Supporting |
| **PM2** | — | — | — | PM2_Supporting |
| **PM4** | — | PM4_Strong | PM4 | PM4_Supporting |
| **PM5** | — | PM5_Strong | PM5 | PM5_Supporting |
| **PM6** | — | — | PM6 | PM6_Supporting |
| **PP1** | — | PP1_Strong | PP1_Moderate | PP1 |
| **PP3** | — | — | — | PP3 |

| Criterion | Stand Alone | Strong (-4) | Moderate (-2) | Supporting (-1) |
|-----------|------------|-------------|---------------|-----------------|
| **BA1** | BA1 | — | — | — |
| **BS1** | — | BS1 | — | — |
| **BS3** | — | BS3 | — | BS3_Supporting |
| **BS4** | — | BS4 | — | — |
| **BP2** | — | — | — | BP2 |
| **BP4** | — | — | — | BP4 |
| **BP7** | — | — | — | BP7 |

### Traditional Combining Rules

#### Pathogenic Classification

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

#### Likely Pathogenic Classification

| Criteria Combination |
|---------------------|
| 1 Very Strong **AND** 1 Moderate |
| 1 Strong **AND** 1 Moderate |
| 1 Strong **AND** ≥2 Supporting |
| ≥3 Moderate |
| 2 Moderate **AND** ≥2 Supporting |
| 1 Moderate **AND** ≥4 Supporting |

#### Benign Classification

| Criteria Combination |
|---------------------|
| 1 Stand Alone (BA1) |
| ≥2 Strong |

#### Likely Benign Classification

| Criteria Combination |
|---------------------|
| 1 Strong **AND** 1 Supporting |
| ≥2 Supporting |

**Note:** BS1 alone can classify a variant as Likely Benign if there is no contradictory evidence supporting pathogenicity.

---

## Appendices

### Appendix A: Criteria Not Applicable to RUNX1

| Criterion | Reason |
|-----------|--------|
| PM3 | FPD/AML is inherited in an autosomal dominant manner |
| PP2 | Missense constraint z score not met (2.48 ExAC, 2.08 gnomAD; threshold ≥ 3.09) |
| PP4 | FPD/AML phenotype is unspecific |
| PP5 | Not for use per ClinGen SVI recommendation (PMID: 29543229) |
| BS2 | FPD/AML has incomplete penetrance; average age of onset for hematologic malignancies is 33 years |
| BP1 | Both truncating and missense variants cause FPD/AML |
| BP3 | RUNX1 does not contain a repetitive region without known function |
| BP5 | Patients can carry two pathogenic variants in genes predisposing to hematologic malignancies |
| BP6 | Not for use per ClinGen SVI recommendation (PMID: 29543229) |

### Appendix B: Functional Assay Ranges (PS3/BS3)

| Transactivation Level (% of wt) | Interpretation | Code |
|--------------------------------|----------------|------|
| < 20% (or levels similar to R201Q/R166Q) | Damaging | PS3 (with secondary assay) or PS3_Moderate (alone or with ≥2 secondary assays) |
| > 115% | Enhanced (gain-of-function) | PS3_Supporting |
| 80% – 115% | Normal | BS3_Supporting (alone) or BS3 (with normal secondary assay) |
| 20% – 80% | Indeterminate range | Not applicable for PS3 or BS3 |

### Appendix C: Population Frequency Thresholds Summary

| Criterion | Threshold | Strength | Additional Requirements |
|-----------|-----------|----------|------------------------|
| BA1 | ≥ 0.0015 (0.15%) | Stand Alone | ≥ 2,000 alleles tested, variant in ≥ 5 alleles |
| BS1 | 0.00015 – 0.0015 (0.015% – 0.15%) | Strong | ≥ 2,000 alleles tested, variant in ≥ 5 alleles |
| PM2 | ≤ 0.00005 (0.005%) | Supporting | ≥ 2,000 alleles tested, ≥ 20x coverage |

### Appendix D: Pilot Classification Results

| Variant | ClinVar Classification | MM-VCEP Classification | Codes Applied |
|---------|----------------------|----------------------|---------------|
| c.1441T>G (p.Ter481Gly) | Uncertain significance | VUS | PM2_supporting, PS4_supporting, PM4 |
| c.484A>G (p.Arg162Gly) | Pathogenic | Pathogenic | PM2_supporting, PP3, PM1_strong, PS3_moderate, PS4_supporting, PP1 |
| c.485G>A (p.Arg162Lys) | Likely Pathogenic | Likely Pathogenic | PM2_supporting, PP3, PM1_strong, PS4_moderate, PP1 |
| c.582A>C (p.Lys194Asn) | Likely Pathogenic | Likely Pathogenic | PM2_supporting, PM1_strong, PP1, PS4_supporting |
| c.581_586del (p.Lys194_Ile195del) | Uncertain significance | VUS | PM2_supporting, PM4_strong |
| c.592G>A (p.Asp198Asn) | Likely Pathogenic | Likely Pathogenic | PM2_supporting, PP3, PM1_strong, PS4_supporting |
| c.596G>C (p.Gly199Ala) | Uncertain significance | VUS | PM2_supporting, PP3, PM1_supporting |
| c.314A>C (p.His105Pro) | Likely Pathogenic | VUS | PM2_supporting, PP3, PM1_supporting, PS4_supporting |
| c.466G>A (p.Ala156Thr) | Uncertain significance | VUS | PM2_supporting, PP3, PM1_supporting |
| c.1308C>T (p.Ser436=) | Uncertain significance | Likely Benign | PM2_supporting, BP4, BP7 |
| c.891C>T (p.His297=) | Uncertain significance | Likely Benign | BP4, BP7 |
| c.969G>A (p.Thr323=) | Likely benign | VUS | — |
| c.510G>T (p.Gly170=) | Likely benign | Likely Benign | PM2_supporting, BP4, BP7 |
| c.508+4C>T | Likely benign | VUS | BP4 |
| c.351+5T>C | Likely benign | VUS | PM2_supporting, BP4 |
| c.968-2A>G | — | Pathogenic | PM2_supporting, PVS1_strong, PS1 |
| c.351+1G>C | Uncertain significance | Pathogenic | PVS1, PM2_supporting, PS1 |
| c.292del (p.Leu98SerfsTer24) | Pathogenic | Likely Pathogenic | PM2_supporting, PM5_supporting, PVS1 |
| c.*484T>C | Benign | Benign | BA1, BP2 |
| c.1338C>T (p.Leu446=) | Benign | Benign | BS1, BP4, BP7, BP2 |

### Appendix E: Reference PMIDs

| PMID | Reference |
|------|-----------|
| 37352859 | Walker LC, Hoya M, Wiggins GAR, et al. Using the ACMG/AMP framework to capture evidence related to predicted and observed impact on splicing: Recommendations from the ClinGen SVI Splicing Subgroup. *Am J Hum Genet*. 2023;110(7):1046-1067. |
| 17290219 | Matheny CJ, Speck ME, Cushing PR, et al. Disease mutations in RUNX1 and RUNX2 create nonfunctional, dominant-negative, or hypomorphic alleles. *EMBO J*. 2007;26(4):1163-1175. |
| 4843792 | Grantham R. Amino acid difference formula to help explain protein evolution. *Science*. 1974;185(4154):862-864. |
| 29543229 | ClinGen SVI VCEP Review Committee recommendation on PP5/BP6. |
| 10508512 | Referenced for cryptic splice acceptor with frameshift at intron 4 acceptor. |
| 11830488 | Referenced for cryptic splice donor with frameshift at intron 4 donor. |

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 3.0.0 | 8/14/2025 | New gnomAD v4 MAF threshold for PM2; PM1/PM4 upgrades to strong for 13 hotspot residues; PVS1_variable and BP7_variable for RNA data; PS1 for splicing variants; BP7 conservation no longer required; PM5 revised for Grantham scores |

---

*This document was compiled from ClinGen MM-VCEP specifications for RUNX1 (Version 3.0.0). For the most current version, please refer to the ClinGen website.*
