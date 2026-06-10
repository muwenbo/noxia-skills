# ClinGen Lysosomal Diseases Expert Panel Variant Interpretation Guidelines for IDUA

**Version:** 1.2.0
**Released:** January 23, 2026
**Affiliation:** Lysosomal Diseases VCEP
**Based on:** Richards et al., 2015 ACMG/AMP Guidelines

---

## Gene Information

| Attribute | Value |
|-----------|-------|
| **Gene** | IDUA (HGNC:5391) |
| **HGNC Name** | alpha-L-iduronidase |
| **Transcript** | NM_000203.4 |
| **Disease** | Mucopolysaccharidosis type 1 (MONDO:0001586) |
| **Inheritance** | Autosomal recessive |

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
- Beware of genes where LOF is not a known disease mechanism (e.g., GFAP, MYH7)
- Use caution interpreting LOF variants at the extreme 3' end of a gene
- Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact
- Use caution in the presence of multiple transcripts

**VCEP Specifications:**

Please consult the "PVS1 Decision Tree" (Appendix A) for additional information. If PVS1 is applied, PM4 will not be applied. If an in-frame deletion is smaller than one exon, PVS1 does not apply; consider using PM4. Use the PVS1 decision tree to assess the impact of single and multi-exon duplications.

Use SpliceAI in analysis of all canonical splice site variants (see PP3 and BP4 for details on thresholds). If there is a nearby (within +/- 20 nucleotides) splice site sequence that may reconstitute in-frame splicing, this should be taken into consideration.

Consult Walker et al (PMID: 37352859) to apply PVS1 for splice motif variants.

#### Strength Levels

| Strength | Criteria |
|----------|----------|
| **Very Strong** | All nonsense and frameshift variants, unless the variant is predicted to be undetected by NMD (i.e., if the resulting PTC is in the last exon (exon 14) or in the last 50 nucleotides of the penultimate exon (exon 13; after c.1778, codon 592)). Canonical splice site variants resulting in out-of-frame exon skipping with predicted NMD. Single/multi-exon deletions resulting in out-of-frame consequence with predicted NMD. Initiation codon variants (next in-frame Met is at position 133). |
| **Strong** | Frameshift variants at 3' end of IDUA not predicted to undergo NMD (PTC downstream of c.1778) where >10% of normal sequence length is altered. Canonical splice variants resulting in in-frame exon skipping where the exon contains critical functional residues. In-frame exon deletions affecting critical residues. Single exon deletions removing >10% of protein. |
| **Moderate** | Nonsense/frameshift variants not predicted to undergo NMD where <10% of the protein is lost (~9.3%). Frameshift variants at 3' end with <10% altered. Canonical splice variants resulting in in-frame exon skipping where the region's function is unknown. In-frame exon deletions affecting <10% of protein with no critical residues. |
| **Supporting** | Not specified for IDUA |

#### PVS1 Exon-Specific Guidance Table

| Exon | Coding Nucleotides | Length | Consequence of Exon Skip | % Protein Lost | PVS1 Strength | Rationale |
|------|-------------------|--------|--------------------------|----------------|---------------|-----------|
| 1 | c.1 - c.158 | 158 bp | Out of frame | - | Very Strong | Skipping predicted to result in frameshift, PTC, and NMD |
| 2 | c.159 - c.299 | 141 bp | In frame | 7.2% | Very Strong | Contains critical substrate binding residues Arg89 and His91 |
| 3 | c.300 - c.385 | 86 bp | Out of frame | - | Very Strong | Skipping predicted to result in frameshift, PTC, and NMD |
| 4 | c.386 - c.493 | 108 bp | In frame | 5.5% | Moderate | 5.5% of protein lost (aa 128-165) |
| 5 | c.494 - c.589 | 96 bp | In frame | 4.9% | Very Strong | Contains active site residue Glu182 |
| 6 | c.590 - c.792 | 203 bp | Out of frame | - | Very Strong | Skipping predicted to result in frameshift, PTC, and NMD |
| 7 | c.793 - c.972 | 180 bp | In frame | 9.2% | Very Strong | Contains active site residue Glu299 |
| 8 | c.973 - c.1189 | 217 bp | Out of frame | - | Very Strong | Skipping predicted to result in frameshift, PTC, and NMD |
| 9 | c.1190 - c.1402 | 213 bp | In frame | 10.9% | Strong | 10.9% of protein lost (aa 397-467) |
| 10 | c.1403 - c.1524 | 122 bp | Out of frame | - | Very Strong | Skipping predicted to result in frameshift, PTC, and NMD |
| 11 | c.1525 - c.1650 | 126 bp | In frame | 6.4% | Moderate | 6.4% of protein lost (aa 508-550) |
| 12 | c.1651 - c.1727 | 77 bp | Out of frame | - | Very Strong | Skipping predicted to result in frameshift, PTC, and NMD |
| 13 | c.1728 - c.1828 | 101 bp | Out of frame | - | Moderate | Skipping predicted to result in frameshift with <10% of normal protein missing |
| 14 | c.1829 - c.1962 | 247 bp | - | 6.8% | Moderate | Last exon; <10% protein missing |

---

### PS1 - Same Amino Acid Change

**Original ACMG Summary:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.

**Caveat:** Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:**

The classification of the other variant must be made following the Lysosomal Diseases VCEP specifications. To avoid circularity, the classification of the other variant should not use evidence from the variant being interrogated. If there is a question as to whether PS1 should be applied to variant A or variant B, use the classification of the variant with a greater level of evidence to support the classification of the variant with less evidence.

When applying PS1 for amino acid changes, there should be no splicing impact for either variant, shown by splicing assay or computational predictors (SpliceAI <0.1).

| Strength | Criteria |
|----------|----------|
| **Strong** | Same amino acid change as a previously established **pathogenic** variant regardless of nucleotide change. Splice region variants following Table 3 in Walker et al (PMID: 37352859). |
| **Moderate** | Same amino acid change as a previously established **likely pathogenic** variant regardless of nucleotide change. Splice region variants following Table 3 in Walker et al (PMID: 37352859). |
| **Supporting** | Splice region variants following Table 3 in Walker et al (PMID: 37352859). |

---

### PS2 - De Novo (Confirmed)

**Original ACMG Summary:** De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.

**Note:** Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.

**VCEP Specifications:**

Note: De novo variants are rarely reported in IDUA.

| Strength | Criteria |
|----------|----------|
| **Strong** | Variant occurs de novo in an affected individual, and the biological relationship of the parent without the variant is confirmed (e.g., if the father is not heterozygous for an IDUA variant that has been detected in the patient, paternity must be confirmed). |
| **Moderate** | Variant occurs de novo in an affected individual, and the biological relationship of the parent without the variant is not confirmed. |

---

### PS3 - Functional Studies

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.

**VCEP Specifications:**

Any variant meeting the requirements below can meet PS3 (at the appropriate strength). Note that these assays are in vitro, research-based, and may not truly reflect in vivo function.

There are several studies involving expression of IDUA sequence variants in cultured cells and subsequent measurement of enzyme activity. Some studies also include analysis of IDUA synthesis and processing by Western blot. Please see Appendix C for details on the methodology used in the studies.

**Note:** PS3 will not be used for RT-PCR assays proving evidence that a variant impacts splicing. Instead, this evidence will be used to assign the appropriate weight of evidence for PVS1, following the guidance of Walker et al (PMID: 37352859).

| Strength | Criteria |
|----------|----------|
| **Moderate** | When PS3_Supporting is met for enzyme activity AND there is expression data (Western blot, pulse chase) showing a clear difference in synthesis and/or processing of alpha-iduronidase (e.g., Matte et al, 2003, PMID: 12559846; see Appendix C). |
| **Supporting** | In vitro expression studies with the following thresholds: <2% activity (Beesley et al, 2001, PMID: 11735025; Yogalingam et al, 2004, PMID: 15300847; Matte et al, 2003); <1% activity/enzyme abundance (Yu et al, 2020, PMID: 33198351). |

#### Assay Requirements for PS3_Supporting:
- Were clones sequenced to verify that the variant is present and that no artifacts have been introduced during the site-directed mutagenesis process?
- Were appropriate controls included?
  - Negative controls: Empty vector, antisense (at least one appropriate negative control is required)
  - Positive control: Wild type IDUA, normal cells (at least one appropriate positive control is required)
- Was the experiment replicated?
- If cells have intrinsic IDUA activity (e.g., COS cells), the level of activity should be stated so that this can be taken into account.

#### Approved Functional Assays

| Study | PMID | Cell Type | Readout | PS3 Threshold | BS3 Threshold |
|-------|------|-----------|---------|---------------|---------------|
| Yu et al, 2020 | 33198351 | IDUA KO HAP1 cells | Specific Relative IDUA Activity | <1% | >~10% |
| Beesley et al, 2001 | 11735025 | COS-7 cells | α-L-iduronidase activity | <2% | >10% |
| Yogalingam et al, 2004 | 15300847 | CHO cells | α-L-iduronidase activity | <2% | >10% |
| Matte et al, 2003 | 12559846 | CHO-K1 cells | Enzyme activity + Western blot | <2% | >10% |

---

### PS4 - Prevalence in Affected

**Original ACMG Summary:** The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.

**VCEP Specification:** *Not Applicable*

**Comments:** There are no case-control studies for MPS1. As this is a recessive disorder, the prevalence of the variant in affected individuals may not be increased compared to controls (who could be heterozygous carriers). The number of patients with the variant will be addressed by the PM3 evidence code.

---

### PM1 - Mutational Hot Spot

**Original ACMG Summary:** Located in a mutational hot spot and/or critical and well-established functional domain (e.g., active site of an enzyme) without benign variation.

**VCEP Specifications:**

Studies on functional domains (Bie et al, 2013, PMID: 24036510; Maita et al, 2013, PMID: 23959878; Saito et al, 2014, PMID: 24480078; Figueiredo et al, 2014, PMID: 25459762) have shown that the following residues are important to the function of IDUA:

**Active site nucleophiles:** Glu182 and Glu299

**Active site pocket and substrate binding:** Arg89, His91, Asn181, His262, Lys264, Asp301, Gly305, Trp306, Asp349, Arg363, Asn372

| Strength | Criteria |
|----------|----------|
| **Moderate** | Any missense substitutions or in-frame deletions of the above residues. There are no benign or likely benign missense or in-frame deletions of these residues in ClinVar, or common missense or in-frame deletions of these residues in gnomAD v4.1.0. |

---

### PM2 - Absent from Controls

**Original ACMG Summary:** Absent from controls (or at extremely low frequency if recessive) in population databases.

**Caveat:** Population data for indels may be poorly called by next generation sequencing.

**VCEP Specification (Supporting only):**

This criterion will be applied at the supporting level based on guidance from the ClinGen Sequence Variant Interpretation Working Group.

| Strength | Criteria |
|----------|----------|
| **Supporting** | Minor allele frequency <0.025% (0.00025) in any continental population with >2000 alleles in the most recent version of gnomAD (version # will be stated in the written summary). |

**Note:** Variants may be observed in the homozygous state because MPS1 can present in adulthood, and some variants may be hypomorphic. However, the presence and number of homozygotes should be noted.

---

### PM3 - In Trans with Pathogenic

**Original ACMG Summary:** For recessive disorders, detected in trans with a pathogenic variant.

**VCEP Specifications:**

- PM2_Supporting must be met in order to apply points to any case.
- The patient must be described as having MPS1, at a minimum. If the case meets PP4 and PM3, both criteria are applied. However, the PP4 criterion need not necessarily be met in order to apply PM3, as long as the patient is stated to have MPS1.
- For compound heterozygous cases, the second variant must have been classified by the Lysosomal Diseases VCEP.
- For rare variants that are routinely observed to be in cis with a pseudodeficiency variant, substantial additional evidence must be available to support the pathogenicity of the variant.
- If multiple unrelated compound heterozygous cases have the same genotype, and the variants are not confirmed in trans, then no more than two cases should be used for assigning points (maximum of 1 point).
- For a variant to be "confirmed in trans," parental testing in at least one parent, or another appropriate molecular method (such as cloning each allele separately followed by sequencing), must have been performed.
- To avoid circularity, the classification of the variant on the other allele should not use evidence from the variant being interrogated.

**Note:** Points will NOT be applied for any variants of uncertain significance confirmed in trans, due to the high number of pseudodeficiency variants in IDUA.

#### PM3 Point System (Per Proband)

| Classification/Zygosity of Other Variant | Confirmed in Trans | Phase Unknown |
|------------------------------------------|-------------------|---------------|
| Pathogenic or Likely pathogenic variant | 1.0 | 0.5 (P) / 0.25 (LP) |
| Homozygous occurrence (max points = 1.0) | 0.5 | N/A |

#### PM3 Evidence Strength Thresholds

| Total Points | Strength Level |
|--------------|----------------|
| 0.5 | PM3_Supporting |
| 1.0 | PM3 (Moderate) |
| 2.0 | PM3_Strong |
| 4.0 | PM3_VeryStrong |

---

### PM4 - Protein Length Changes

**Original ACMG Summary:** Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

**VCEP Specifications:**

For in-frame deletions of one or more exons, use PVS1.

| Strength | Criteria |
|----------|----------|
| **Moderate** | Stop loss variants, and in-frame deletion/insertions of two or more amino acids but less than one exon. |
| **Supporting** | In-frame deletion/insertion of one amino acid. |

---

### PM5 - Novel Missense at Same Residue

**Original ACMG Summary:** Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.

**Caveat:** Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:**

The classification of the other variant must be made following the Lysosomal Diseases VCEP specifications. To avoid circularity, the classification of the other variant should not use evidence from the variant being interrogated.

There is no splicing impact for either variant, shown by splicing assay or computational predictors (SpliceAI ≤0.1).

| Strength | Criteria |
|----------|----------|
| **Moderate** | Missense change at an amino acid residue where a different missense change determined to be **pathogenic** has been seen before. Stop loss variant if another stop loss variant has been determined to be pathogenic. |
| **Supporting** | Missense change at an amino acid residue where a different missense change determined to be **likely pathogenic** has been seen before. Stop loss variant if another stop loss variant has been determined to be likely pathogenic. |

---

### PM6 - De Novo (Assumed)

**Original ACMG Summary:** Assumed de novo, but without confirmation of paternity and maternity.

**VCEP Specification:** *Not Applicable*

**Comments:** See PS2.

---

### PP1 - Co-segregation

**Original ACMG Summary:** Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.

**VCEP Specifications:**

Based on Biesecker et al, 2024 (PMID: 38103548).

**Important:** The combination of strengths for PP1 and PP4 MUST NOT exceed strong (2 x moderate, i.e., 4 points using Bayesian system) if cases are also being counted as probands under PM3.

#### Counting Segregations:
- Do not count probands as a segregation
- Affected segregations = # affected individuals in the family with the variants minus 1
- Affected segregations are defined as affected family members (typically siblings) who harbor the variant in question and a second variant on the remaining allele
- Unaffected segregations are defined as unaffected family members, typically siblings, who are at risk to inherit the two variants (or one variant in homozygosity) identified in the proband. These individuals should be either homozygous normal or heterozygous for only one variant
- Unaffected, carrier parents DO NOT count as unaffected segregations

#### PP1 Points Table

| | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| **Affected** | 2.0 | 4.0 | 6.0 | 8.0 | 10.0 |
| **Unaffected** | 0.4 | 0.8 | 1.2 | 1.6 | 2.0 |

#### PP1 Evidence Strength Thresholds

| Points | Strength Level |
|--------|----------------|
| 1 | Supporting |
| 2 | Moderate |
| ≥4 | Strong |

---

### PP2 - Missense in Constrained Gene

**Original ACMG Summary:** Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.

**VCEP Specification:** *Not Applicable*

**Comments:** Does not apply; there are benign and pathogenic missense variants in IDUA.

---

### PP3 - Computational Evidence

**Original ACMG Summary:** Multiple lines of computational evidence support a deleterious effect on the gene or gene product.

**Caveat:** As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.

**VCEP Specifications:**

A publication on the use of in silico predictors for IDUA reported specificity of 88% and sensitivity of 75% for REVEL, using a 0.75 cutoff (PMID: 34746235). The VCEP has decided to continue using REVEL and to follow the SVI guidance (Pejaver et al, PMID: 3641399).

| Strength | Criteria |
|----------|----------|
| **Moderate** | Any missense changes with a REVEL score >0.773 (Note: The VCEP has chosen not to apply PP3 at strong). |
| **Supporting** | Missense changes with a REVEL score between 0.644 - 0.773. For in-frame insertions and deletions, use Mutation Taster (count if "disease-causing") AND MutPred-Indel (score >0.5 for "pathogenic"); apply PP3 if both predictors indicate the variant is deleterious. For non-canonical splice site variants, use SpliceAI (score >0.2 indicates disruption of the splice site). |

**URLs:**
- Mutation Taster: http://www.mutationtaster.org/
- MutPred-Indel: https://mutpred2.mutdb.org/mutpredindel/
- SpliceAI: https://spliceailookup.broadinstitute.org/

---

### PP4 - Phenotype Specificity

**Original ACMG Summary:** Patient's phenotype or family history is highly specific for a disease with a single genetic etiology.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Moderate** | 3 or more of the following criteria are met (see below) |
| **Supporting** | 2 of the following criteria are met (see below) |

#### PP4 Criteria Checklist:

1. **Deficient IDUA activity**, within the affected range (usually non-detectable or stated to be in the affected range by lab) in fibroblasts, leukocytes, or plasma.
   - Do not count if one or more pseudodeficiency variants are reported to be present, or if the result was obtained on newborn screen without confirmatory enzyme testing.

2. **Enzyme replacement therapy** results in a significant reduction in urine GAGs (either total, or dermatan or heparan sulfate).

3. **Elevated urinary and/or blood GAGs** expressed as either total GAGs, specific GAG (heparan sulfate, dermatan sulfate, or endogenous biomarker) stated to be consistent with MPS I.

4. **Clinical features specific to MPS I**: At minimum at least 2 of the following: dysostosis multiplex, hepatosplenomegaly, arthropathy, corneal involvement, valvular thickening; AND/OR case reported within the context of a larger clinically-diagnosed MPS I cohort, when published by groups with demonstrated experience in lysosomal disorders.

5. **Bone marrow transplant** results in a significant reduction in urine GAGs (either total, or dermatan or heparan sulfate).

---

### PP5 - Reputable Source

**Original ACMG Summary:** Reputable source recently reports variant as pathogenic, but the evidence is not available to the laboratory to perform an independent evaluation.

**VCEP Specification:** *Not Applicable*

This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PMID: 29543229).

---

## Benign Criteria

### BA1 - Allele Frequency >5%

**Original ACMG Summary:** Allele frequency is above 5% in population databases.

**VCEP Specification (Stand Alone):**

Any variant with Grpmax >0.005 in the most recent version of gnomAD (95% confidence interval, lower bound).

BA1 minor allele frequency cut-off calculated using http://cardiodb.org/allelefrequencyapp with:
- Prevalence = 1 in 40,000 (PMID: 33208168)
- Genetic heterogeneity = 1.0 (IDUA is the only gene known to cause MPS1)
- Allelic heterogeneity = 1.0
- Penetrance = 1.0

---

### BS1 - Frequency Greater Than Expected

**Original ACMG Summary:** Allele frequency is greater than expected for disorder.

**VCEP Specifications:**

Variants meeting only BS1 will be classified as likely benign.

| Strength | Criteria |
|----------|----------|
| **Strong** | Any variant with Grpmax >0.0025 in the most recent version of gnomAD (95% confidence interval, lower bound). |

BS1 minor allele frequency cut-off calculated using http://cardiodb.org/allelefrequencyapp with:
- Prevalence = 1 in 40,000 (PMID: 33208168)
- Genetic heterogeneity = 1.0
- Allelic heterogeneity = ~0.5 (frequency of the most common known pathogenic variants in patients with MPS1, PMID: 28595941, 29393969)
- Penetrance = 1.0

---

### BS2 - Observed in Healthy Adult

**Original ACMG Summary:** Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | BS2 can be applied if there is clear documentation that an individual of any age is either homozygous for the variant, or has the variant confirmed in trans with a pathogenic or likely pathogenic variant AND has IDUA activity in the unaffected range as documented by standard diagnostic laboratory-based activity determination. Values for IDUA activity and the reference range for the laboratory must be provided. |

**Note:** Patients with late onset MPS1 can present late in life (5th-6th decade), can have mild symptoms, and may remain undiagnosed. Therefore, it is possible that individuals who are homozygous for hypomorphic IDUA variants could be present in population databases.

---

### BS3 - Functional Studies (No Effect)

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

**VCEP Specifications:**

Variants meeting the combination of BS3_Supporting, BP4, and PM2_Supporting will be classified as likely benign.

| Strength | Criteria |
|----------|----------|
| **Supporting** | The same assays outlined for PS3 will be used for BS3. BS3_Supporting can be applied for expression of IDUA sequence variants in cultured cells and subsequent measurement of enzyme activity provided that there is no other evidence to suggest that the variant could be disease-causing (e.g., mislocalization). Thresholds: >10% activity (Beesley et al, 2001; Yogalingam et al, 2004; Matte et al, 2003); >~10% activity/enzyme abundance (Yu et al, 2020). |

---

### BS4 - Lack of Segregation

**Original ACMG Summary:** Lack of segregation in affected members of a family.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | Non-segregation with disease in a family, i.e., variant is absent in an affected individual. |

---

### BP1-BP7 - Benign Supporting

| Criterion | Status | Specification |
|-----------|--------|---------------|
| **BP1** | *Not Applicable* | Does not apply. All types of variants cause MPS1. |
| **BP2** | *Not Applicable* | - |
| **BP3** | *Not Applicable* | There are no known repetitive regions without known function in IDUA. |
| **BP4** | **Supporting** | Missense changes with a REVEL score <0.290. For in-frame insertions/deletions, use PROVEAN (score >-2.5), Mutation Taster (count if "polymorphism"), and MutPred-Indel (score <0.5); apply BP4 if all predictors indicate the variant is benign. For non-canonical splice site variants, use SpliceAI (score ≤0.1). If there is any evidence for possible creation of a cryptic splice site, this criterion should not be applied. Variants meeting BS3_Supporting, BP4, and PM2_Supporting will be classified as likely benign. |
| **BP5** | *Not Applicable* | There is no known alternate molecular basis for deficiency of alpha-L-iduronidase activity, other than variants in IDUA. |
| **BP6** | *Not Applicable* | Not for use per ClinGen SVI recommendation (PMID: 29543229). |
| **BP7** | **Supporting/Strong** | **Supporting:** BP7 can be applied if the variant is synonymous, unless the variant is in the first nucleotide or last three nucleotides of an exon, AND BP4 is met (SpliceAI score ≤0.10). If a variant meets BP7, BP4 can also be applied. **Strong:** Experimental evidence (RT-PCR, RNA Seq, minigene) shows that the variant does not impact splicing. BP7_Strong (RNA) will be used only under strict circumstances where it is clear that the allele with the variant is expressed at the normal level. |

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
| 1 Strong **AND** 1 Supporting |
| ≥2 Supporting |

---

## Appendices

### Appendix A: PVS1 Decision Tree

The PVS1 decision tree for IDUA includes IDUA-specific modifications from the SVI guidance.

#### Nonsense or Frameshift Variants
- **Predicted to undergo NMD** (PTC 5' to c.1778): → **PVS1**
- **Not predicted to undergo NMD** (PTC in last exon (exon 14) or last 50 nt of penultimate exon (c.1778 and downstream)):
  - Variant removes >10% of protein → **PVS1_Strong**
  - Variant removes <10% of protein → **PVS1_Moderate**

#### Canonical Splice Site Variants (GT-AG, +1/+2, -1/-2)
- **Exon skipping disrupts reading frame AND predicted to undergo NMD:**
  - Out-of-frame exons: 1, 3, 6, 8, 10, 12, 13 → **PVS1**
- **Exon skipping preserves reading frame** (in-frame exons: 2, 4, 5, 7, 9, 11):
  - Truncated region is critical to protein function:
    - Exon 2 (Arg89, His91), Exon 5 (Asn181, Glu182), Exon 7 (Glu299) → **PVS1**
  - Role of region is unknown:
    - Variant removes >10% of protein (exon 9) → **PVS1_Strong**
    - Variant removes <10% of protein (exons 4, 11) → **PVS1_Moderate**

#### Deletions (Single Exon to Full Gene)
- **Disrupts reading frame AND predicted to undergo NMD** → **PVS1**
- **Preserves reading frame:**
  - Critical residues affected → **PVS1_Strong**
  - Function unknown, >10% removed → **PVS1_Strong**
  - Function unknown, <10% removed → **PVS1_Moderate**
- **Full gene deletion** → **PVS1**

#### Duplications (≥1 exon, completely contained within gene)
- **Proven in tandem:**
  - Reading frame disrupted AND NMD predicted → **PVS1**
  - No or unknown impact on reading frame → N/A
- **Presumed in tandem:**
  - Reading frame presumed disrupted AND NMD predicted → **PVS1_Strong**

#### Initiation Codon Variants
- ≥1 pathogenic variant(s) upstream of closest potential in-frame start codon → **PVS1**
- The next in-frame methionine is at position 133; 6 variants upstream of Met133 are classified as pathogenic in ClinVar

---

### Appendix B: PM1 Critical Residues

#### Active Site Nucleophiles
- **Glu182**
- **Glu299**

#### Active Site Pocket and Substrate Binding Residues
- Arg89
- His91
- Asn181
- His262
- Lys264
- Asp301
- Gly305
- Trp306
- Asp349
- Arg363
- Asn372

**References:**
- Bie et al, 2013 (PMID: 24036510)
- Maita et al, 2013 (PMID: 23959878)
- Saito et al, 2014 (PMID: 24480078)
- Figueiredo et al, 2014 (PMID: 25459762)

---

### Appendix C: Approved Functional Assays (PS3/BS3)

#### Yu et al, 2020 (PMID: 33198351)
- **Assay:** Measurement of IDUA specific activity using 4-MU-α-L-iduronic acid as substrate in IDUA-deficient HAP1 cells after lentiviral transduction
- **Cell Type:** IDUA KO HAP1 cells
- **Readout:** Specific Relative IDUA Activity (IDUA activity / enzyme abundance)
- **Controls:** Positive - WT IDUA cDNA transduction; Negative - Untransduced cells
- **Validation:** Pseudodeficiency variants (p.Ala79Thr, p.His82Gln, p.Asp223Asn, p.Val322Glu)
- **Thresholds:** PS3_Supporting <1%; BS3_Supporting >~10%

#### Beesley et al, 2001 (PMID: 11735025)
- **Assay:** Site-directed mutagenesis of IDUA cDNA in mammalian expression vector (pR20.5), transfection into COS-7 cells
- **Cell Type:** COS-7 cells
- **Readout:** α-L-iduronidase activity (nmol/h/mg cell protein)
- **Controls:** Positive - WT IDUA; Negative - Untransfected cells, vector only
- **Validation:** p.His240Arg, p.Trp402Ter, p.Pro496Arg
- **Thresholds:** PS3_Supporting <2%; BS3_Supporting >10%

#### Yogalingam et al, 2004 (PMID: 15300847)
- **Assay:** Site-directed mutagenesis of IDUA cDNA in expression vector (pEFNeo), transfection into CHO cells
- **Cell Type:** CHO cells
- **Readout:** α-L-iduronidase activity (nmol/min/mg)
- **Controls:** Positive - WT IDUA; Negative - Untransfected cells, vector only
- **Validation:** p.Ala79Val, p.Gly265Arg
- **Thresholds:** PS3_Supporting <2%; BS3_Supporting >10%

#### Matte et al, 2003 (PMID: 12559846)
- **Assay:** Site-directed mutagenesis of wild-type pEF-IDUA vector, transfection into CHO-K1 cells with G418 selection
- **Cell Type:** CHO-K1 cells
- **Readout:** Enzyme activity (% of normal) + Western blot analysis
- **Controls:** Positive - WT IDUA; Negative - Untransfected cells
- **Validation:** p.Arg84del, p.Trp402Ter, p.Pro533Arg
- **Thresholds:** PS3_Supporting <2%; PS3_Moderate for variants meeting PS3_Supporting WITH accompanying Western blot evidence showing abnormal synthesis/processing; BS3_Supporting >10%

---

### Appendix D: Population Frequency Thresholds Summary

| Criterion | Threshold | Strength | Notes |
|-----------|-----------|----------|-------|
| BA1 | Grpmax >0.005 (95% CI lower bound) | Stand Alone | Based on prevalence 1:40,000 |
| BS1 | Grpmax >0.0025 (95% CI lower bound) | Strong | Based on prevalence 1:40,000, allelic heterogeneity ~0.5 |
| PM2 | MAF <0.00025 in any continental population | Supporting | >2000 alleles in gnomAD |

---

### Appendix E: Computational Prediction Thresholds

#### Missense Variants (REVEL)
| Score Range | Criterion | Strength |
|-------------|-----------|----------|
| >0.773 | PP3 | Moderate |
| 0.644 - 0.773 | PP3 | Supporting |
| <0.290 | BP4 | Supporting |

#### In-frame Insertions/Deletions
| Predictor | PP3 Threshold | BP4 Threshold |
|-----------|---------------|---------------|
| Mutation Taster | "disease-causing" | "polymorphism" |
| MutPred-Indel | >0.5 | <0.5 |
| PROVEAN | - | >-2.5 |

**Note:** PP3 for in-frame indels requires BOTH Mutation Taster AND MutPred-Indel to indicate deleterious. BP4 requires ALL three predictors to indicate benign.

#### Splice Variants (SpliceAI)
| Score | Interpretation |
|-------|----------------|
| >0.2 | PP3 (Splicing) - indicates disruption |
| ≤0.1 | BP4 (Splicing) - no predicted impact |

---

### Appendix F: Reference PMIDs

| PMID | Citation | Use |
|------|----------|-----|
| 37352859 | Walker et al | PVS1 for splice motif variants |
| 38103548 | Biesecker et al, 2024 | PP1 segregation guidance |
| 33208168 | - | MPS1 prevalence data |
| 28595941 | - | Pathogenic variant frequencies |
| 29393969 | - | Pathogenic variant frequencies |
| 24036510 | Bie et al, 2013 | Functional domain studies |
| 23959878 | Maita et al, 2013 | Functional domain studies |
| 24480078 | Saito et al, 2014 | Functional domain studies |
| 25459762 | Figueiredo et al, 2014 | Functional domain studies |
| 33198351 | Yu et al, 2020 | Functional assay |
| 11735025 | Beesley et al, 2001 | Functional assay |
| 15300847 | Yogalingam et al, 2004 | Functional assay |
| 12559846 | Matte et al, 2003 | Functional assay |
| 34746235 | - | In silico predictor validation for IDUA |
| 3641399 | Pejaver et al | REVEL thresholds |
| 29543229 | - | PP5/BP6 not recommended |
| 29300386 | Tavtigian et al, 2018 | Bayesian points system |

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.2.0 | January 23, 2026 | PP3: Updated MutPred-InDel website. PP4: Added dermatan sulfate as a biomarker. PP4: Updated to remove requirement for detailed clinical features for individuals part of large MPS I cohort from experienced groups. BS2: Minor wording update. |
| 1.1.0 | - | Previous version |
| 1.0.0 | - | Initial release |

---

*This document was compiled from ClinGen VCEP specifications and ClinGen SVI recommendations. For the most current version, please refer to the ClinGen website.*
