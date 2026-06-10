# ClinGen Rett and Angelman-like Disorders Expert Panel Variant Interpretation Guidelines for CDKL5

**Version:** 5.0.0
**Released:** 7/30/2025
**Affiliation:** Rett and Angelman-like Disorders VCEP
**Based on:** Richards et al., 2015 ACMG/AMP Guidelines

---

## Gene Information

| Attribute | Value |
|-----------|-------|
| **Gene** | CDKL5 (HGNC:11411) |
| **HGNC Name** | cyclin dependent kinase like 5 |
| **Transcript** | NM_001323289.2 |
| **Disease** | CDKL5 disorder (MONDO:0100039) |
| **Inheritance** | X-linked inheritance |

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
   - [BA1 - Allele Frequency Stand Alone](#ba1---allele-frequency-stand-alone)
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

Refer to PVS1 flow chart for additional guidance (see Appendix A).

**Additional Notes:**
- Do not use PVS1 for truncating variants in CDKL5 C-terminus (exons 19-21, or after p.P904) **when using the historically used transcript (NM_003159.2)**
- CDKL5 has non-coding exons. There is evidence that loss of just non-coding CDKL5 exon 1 is pathogenic given previous de novo findings in patients affected with CDKL5-disease (GeneDx internal data), therefore, for losses involving just CDKL5 exon 1, PVS1 can be applied
- For intragenic deletions/duplications that preserve reading frame:
  - For single exon in-frame deletions, assign the same strength (PVS1, PVS1_Strong, or PVS1_Moderate) as for splice site variants that preserve reading frame
  - For multiple exon in-frame deletions, PVS1 can be assigned to deletions that include single in-frame exons in the PVS1 category OR if the exon contains a functionally important domain as specified in PM1
- Given the extensive data available for CDKL5, classifications for single or multi-exon in-frame deletions are assigned as PVS1 or PVS1_Strong. Exceptions are CDKL5 exon 17 due to a limited number of pathogenic variants reported to date

#### Strength Levels

| Strength | Criteria |
|----------|----------|
| **Very Strong (PVS1)** | Use as defined by ClinGen SVI working group (PMID:30192042). Applicable for:<br>- Null variants up to p.R948 **when using the major brain isoform (NM_001323289.2)**<br>- Frameshift variants that result in a read-through of the stop codon<br>- Canonical splice site variants predicted to result in an out-of-frame product<br>- Canonical splice site variants or single in-frame deletions predicted to preserve reading frame (exons 7, 10, 13) and for non-coding exon 1 (NM_001323289.2)<br>- In-frame deletions including the PM1 functional domains (p.V19_K43 ATP binding domain or p.T169_Y171 TEY phosphorylation domain)<br>- Deletions and duplications ≥1 exon in size (completely contained within CDKL5 gene) where reading frame is disrupted and NMD is predicted to occur<br>- Full gene deletion |
| **Strong (PVS1_Strong)** | Applicable for:<br>- Canonical splice site variants that flank exon 18 (the final exon of NM_001323289.2)<br>- Single to multi exon deletions that disrupt the reading frame such that exon 18 is truncated/altered<br>- Duplications ≥1 exon in size (completely contained within CDKL5 gene) where reading frame is presumed to be disrupted and NMD is predicted to occur |
| **Moderate (PVS1_Moderate)** | Applicable for:<br>- Any truncating variant distal of p.R948 (when using major brain isoform, NM_001323289.2)<br>- Canonical splice site variants that flank exon 17 (in-frame exon) (NM_001323289.2) |
| **Supporting (PVS1_Supporting)** | Applicable for initiation codon variants in CDKL5 |

---

### PS1 - Same Amino Acid Change

**Original ACMG Summary:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.

**Example:** Val->Leu caused by either G>C or G>T in the same codon.

**Caveat:** Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | Same amino acid change as a previously established pathogenic variant regardless of nucleotide change. No modification from original ACMG criterion. |

---

### PS2 - De Novo (Confirmed)

**Original ACMG Summary:** De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.

**Note:** Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.

**VCEP Specifications:**

Applicable to all genes in affected individuals identified as mosaic for the variant (as the presence of a variant in the mosaic state is confirmatory of the variant being de novo). Because of the very high de novo rate of pathogenic variants in CDKL5, de novo observation can be attributed the highest value points per proband (2 points for confirmed de novo and 1 point for assumed de novo) if the patient is known to be affected with a neurodevelopmental phenotype consistent with the gene.

#### Strength Levels

| Strength | Criteria |
|----------|----------|
| **Very Strong** | ≥2 independent occurrences of PS2<br>OR<br>≥2 independent occurrences of PM6 and one occurrence of PS2 |
| **Strong** | 1 occurrence of PS2 |

---

### PS3 - Functional Studies

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.

**Note:** Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | RNA studies that demonstrate abnormal splicing and an out-of-frame transcript. Do not use for canonical splice site variants and when PVS1 is used. |
| **Supporting** | RNA studies that demonstrate abnormal splicing and an in-frame product (unless it affects an in-frame exon specified in the PVS1 section). See included table for acceptable functional studies. |

#### Approved Functional Assays for CDKL5

| Assay Name | Measured Parameter | Expected Deleterious Result (PS3_Supporting) | Expected Benign Result (BS3) | References |
|------------|-------------------|---------------------------------------------|------------------------------|------------|
| In vitro autophosphorylation assays | Auto-phosphorylation of CDKL5 | Absence of auto-phosphorylation | Not recommended | PMID: 16935860 |
| In vitro phosphorylation-TEY assay | Phosphorylation of TEY motif | Absence of phosphorylation | Not recommended | PMID: 16935860 |
| Subcellular localization assay | Subcellular distribution | Unidentifiable with Hoechst staining and localizes partially within the cytoplasm | Not recommended | PMID: 16935860 |
| In vitro kinase assay | Enzymatic activity of CDKL5 | Absence of phosphorylation of CDKL5 substrates (MeCP2 and Dnmt1) | Not recommended | PMID: 27265524, 16935860 |

---

### PS4 - Prevalence in Affected

**Original ACMG Summary:** The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.

**Note 1:** Relative risk (RR) or odds ratio (OR), as obtained from case-control studies, is >5.0 and the confidence interval around the estimate of RR or OR does not include 1.0.

**Note 2:** In instances of very rare variants where case-control studies may not reach statistical significance, the prior observation of the variant in multiple unrelated patients with the same phenotype, and its absence in controls, may be used as moderate level of evidence.

**VCEP Specifications:**

- Detailed phenotype not needed. Need to confirm patient is 'affected with a neurodevelopmental phenotype consistent with the gene' at a minimum
- Patient can be published OR an internal case OR observed at an outside lab (i.e., via ClinVar) OR described in the reputable databases (RettBASE). However independent case has to be confirmed to be a different patient than yours (compare gender/age)
- Do not use this criterion for variants where BS1 is applied or where PM2 does not apply

| Strength | Criteria |
|----------|----------|
| **Strong** | 5+ observations |
| **Moderate** | 3-4 observations |
| **Supporting** | Use for 2nd independent occurrence |

---

### PM1 - Mutational Hot Spot

**Original ACMG Summary:** Located in a mutational hot spot and/or critical and well-established functional domain (e.g., active site of an enzyme) without benign variation.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Moderate** | Located in a mutational hot spot and/or critical and well-established functional domain:<br>- **ATP binding region:** amino acids 19-43<br>- **TEY phosphorylation site:** amino acids 169-171 |

---

### PM2 - Absent from Controls

**Original ACMG Summary:** Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

**Caveat:** Population data for indels may be poorly called by next generation sequencing.

**VCEP Specification (Supporting only):**

| Strength | Criteria |
|----------|----------|
| **Supporting** | Absent/rare from controls in an ethnically-matched cohort population sample. Use if absent, zero observations in control databases. |

---

### PM3 - In Trans with Pathogenic

**Original ACMG Summary:** For recessive disorders, detected in trans with a pathogenic variant.

**Note:** This requires testing of parents (or offspring) to determine phase.

**VCEP Specifications:**

| Status | Comment |
|--------|---------|
| **Not Applicable** | Not applicable for CDKL5 (X-linked inheritance) |

---

### PM4 - Protein Length Changes

**Original ACMG Summary:** Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Moderate** | Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants. Do not use for in-frame deletions/insertions in CDKL5 C-terminus (exons 19-21, or after p.P904) **(when using the NM_003159.2 transcript)**. |
| **Supporting** | Smaller in-frame events (<3 amino acid residues) unless they occur in a functionally important region (see PM1 for functionally important domains). |

---

### PM5 - Novel Missense at Same Residue

**Original ACMG Summary:** Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.

**Example:** Arg156His is pathogenic; now you observe Arg156Cys.

**Caveat:** Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | ≥2 different missense changes affecting the amino acid residue. Do not apply PM1 in these situations. |
| **Moderate** | Applicable to all genes as written. A Grantham or BLOSUM score comparison can be used to determine if the variant is predicted to be as or more damaging than the established pathogenic variant. |

---

### PM6 - De Novo (Assumed)

**Original ACMG Summary:** Assumed de novo, but without confirmation of paternity and maternity.

**VCEP Specifications:**

Because of the very high de novo rate of pathogenic variants in CDKL5, de novo observation can be attributed the highest value points per proband (2 points for confirmed de novo and 1 point for assumed de novo) if the patient is known to be affected with a neurodevelopmental phenotype consistent with the gene.

| Strength | Criteria |
|----------|----------|
| **Very Strong** | ≥4 independent occurrences of PM6. Evidence from literature must be fully evaluated to support independent events. |
| **Strong** | ≥2 independent occurrences of PM6. Evidence from literature must be fully evaluated to support independent events. |
| **Moderate** | 1 occurrence of PM6. |

---

### PP1 - Co-segregation

**Original ACMG Summary:** Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.

**Note:** May be used as stronger evidence with increasing segregation data.

**VCEP Specifications:**

Note: Individuals must have disease consistent with reported phenotype (even if on the mild end of spectrum of the disease).

| Strength | Criteria |
|----------|----------|
| **Strong** | ≥5 informative meioses |
| **Moderate** | 3-4 informative meioses |
| **Supporting** | 2 informative meioses |

---

### PP2 - Missense in Constrained Gene

**Original ACMG Summary:** Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.

**VCEP Specifications:**

| Status | Comment |
|--------|---------|
| **Not Applicable** | Not applicable for CDKL5 |

---

### PP3 - Computational Evidence

**Original ACMG Summary:** Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).

**Caveat:** As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Supporting** | Multiple lines of computational evidence support a deleterious effect:<br>- **For missense variants:** Use REVEL with a score ≥ 0.644<br>- **For splice site variants:** Use SpliceAI with a score ≥ 0.2 |

---

### PP4 - Phenotype Specificity

**Original ACMG Summary:** Patient's phenotype or family history is highly specific for a disease with a single genetic etiology.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Supporting** | Phenotype specific for disease with single genetic etiology. See gene specific clinical phenotype guidelines below. |

#### CDKL5 Clinical Phenotype Guidelines

**Core Phenotypes (need to be met for PP4):**
- Seizures, including infantile spasms, beginning in infancy
- Global developmental delay
- Intellectual disability
- Hypotonia
- Severely impaired gross motor function
- Cortical visual impairment in the first 12 months

**Supportive Criteria (do not need to be met for PP4; however in the absence of one core phenotype, two or more supportive phenotypes can be used in its place):**
- Sleep disturbances
- Gastrointestinal dysfunction
- Subtle dysmorphic features (broad forehead, large, deep-set eyes, tapered fingers, full lips, anteverted nostrils in males)
- Bruxism
- Hand stereotypies
- Periodic breathing
- Laughing, screaming spells
- Cold hands and feet
- Peripheral vasomotor dysfunction

---

### PP5 - Reputable Source

**Original ACMG Summary:** Reputable source recently reports variant as pathogenic, but the evidence is not available to the laboratory to perform an independent evaluation.

**VCEP Specifications:**

| Status | Comment |
|--------|---------|
| **Not Applicable** | This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PMID: 29543229) |

---

## Benign Criteria

### BA1 - Allele Frequency Stand Alone

**Original ACMG Summary:** Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

**VCEP Specifications:**

The frequency cutoffs are based on MECP2 expected disease allele frequency (1 in 10,000 for the disease prevalence / (1.5 alleles [assumes 50/50 male/female ratio] * 0.8 for 80% penetrance)). MECP2 is the most prevalent of the genes covered in the Rett/Angelman-like working group and was chosen as most conservative number.

| Strength | Criteria |
|----------|----------|
| **Stand Alone** | Allele frequency above **0.05% (0.0005)**<br>- Use large population databases (i.e., gnomAD)<br>- Use if variant is present at ≥0.000083 (0.0083%) in any sub-population<br>- Use if allele frequency is met in any general continental population dataset of at least 2,000 observed alleles |

---

### BS1 - Frequency Greater Than Expected

**Original ACMG Summary:** Allele frequency is greater than expected for disorder.

**VCEP Specifications:**

The frequency cutoffs are based on MECP2 expected disease allele frequency divided by 10-fold. MECP2 is the most prevalent of the genes covered in the Rett/Angelman-like working group and was chosen as most conservative number.

| Strength | Criteria |
|----------|----------|
| **Strong** | Allele frequency greater than expected for disease **(0.025% or 0.00025)**<br>- Use large population databases (i.e., gnomAD)<br>- Use if variant is present at ≥0.0000083 (0.00083%) and <0.000083 (0.0083%) in any sub-population<br>- Use if allele frequency is met in any general continental population dataset of at least 2,000 observed alleles |

---

### BS2 - Observed in Healthy Adult

**Original ACMG Summary:** Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

**VCEP Specifications:**

- Should be applied in cases where the healthy adult is devoid of neurodevelopmental phenotypes
- Best to use with internal curated data that includes clinical information or published patients that have been phenotyped

| Strength | Criteria |
|----------|----------|
| **Strong** | Observed in the heterozygous/hemizygous state in a healthy adult: 2 unaffected (related or unrelated) heterozygotes or hemizygotes |
| **Supporting** | Observed in the heterozygous/hemizygous state in a healthy adult: 1 unaffected (related or unrelated) heterozygote or hemizygote |

---

### BS3 - Functional Studies (No Effect)

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | RNA functional studies that demonstrate no impact on splicing and transcript composition. It can be downgraded based on quality of data. Not applicable for other functional studies. |

**Note:** BS3 is **not recommended** for the approved functional assays (autophosphorylation, TEY phosphorylation, subcellular localization, kinase assays) - see PS3 table above.

---

### BS4 - Lack of Segregation

**Original ACMG Summary:** Lack of segregation in affected members of a family.

**Caveat:** The presence of phenocopies for common phenotypes (i.e., cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.

**VCEP Specifications:**

Need to confirm that the family member is 'affected with a neurodevelopmental phenotype consistent with the gene' at a minimum.

| Strength | Criteria |
|----------|----------|
| **Strong** | Absent in a similarly affected family member, when seen in two or more families |
| **Supporting** | Absent in a similarly affected family member |

---

### BP1-BP7 - Benign Supporting

| Criterion | Status | Specifications |
|-----------|--------|----------------|
| **BP1** | Not Applicable | Not applicable for CDKL5 |
| **BP2** | Supporting | Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder; or observed in cis with a pathogenic variant in any inheritance pattern. **BP2 is not applicable for *in trans* state.** Note: Knock out of CDKL5 results in disease but viable phenotype. |
| **BP3** | Supporting | In-frame deletions/insertions in a repetitive region without a known function. BP3 is applicable if there are in-frame deletions/duplications in a repetitive region where other in-frame deletions/duplications have been observed with an overall frequency commensurate with the BA1 threshold for this gene. |
| **BP4** | Supporting | Multiple lines of computational evidence suggest no impact on gene or gene product:<br>- **For missense variants:** Use REVEL with a score ≤ 0.290<br>- **For splice site variants:** Use SpliceAI with a score ≤ 0.1 |
| **BP5** | Supporting/Moderate/Strong | Variant found in a case with an alternate molecular basis for disease. For example if a variant in CDKL5 is identified in a patient with lissencephaly in whom a pathogenic variant is identified in the PAFAH1B1 gene. Do not apply if variant is de novo.<br>- **Supporting:** 1 case with alternate molecular basis<br>- **Moderate:** 2 cases with alternate molecular basis<br>- **Strong:** ≥3 cases with alternate molecular basis |
| **BP6** | Not Applicable | This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PMID: 29543229) |
| **BP7** | Supporting | A synonymous (silent) variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.<br>- Defined 'not highly conserved' regions as those with PhastCons score <1 and/or PhyloP score <0.1 and/or the variant is the reference nucleotide in one primate and/or three mammal species<br>- For splice site variants use SpliceAI with a score ≤ 0.1<br>- **Note:** For silent variants BP4 and BP7 can be added |

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

### Appendix A: PVS1 Decision Tree for CDKL5 (NM_001323289.2)

#### Nonsense or Frameshift Variants

| Scenario | Condition | Strength |
|----------|-----------|----------|
| Predicted to undergo NMD | Exon is present in biologically-relevant transcript(s) | PVS1 |
| Predicted to undergo NMD | Exon is absent from biologically-relevant transcript(s) | N/A |
| Not predicted to undergo NMD | Upstream of most distal de novo LOF variant (p.R948); Frameshift that results in a read-through of the stop codon | PVS1 |
| Not predicted to undergo NMD | Downstream of most distal de novo LOF variant (p.R948) | PVS1_Moderate |

#### Canonical Splice Site Variants (GT--AG, +/-1,2)

| Scenario | Condition | Strength |
|----------|-----------|----------|
| Exon skipping/cryptic splice disrupts reading frame, predicted to undergo NMD | Exon is present in biologically-relevant transcript(s) | PVS1 |
| Exon skipping/cryptic splice disrupts reading frame, predicted to undergo NMD | Exon is absent from biologically-relevant transcript(s) | N/A |
| Exon skipping/cryptic splice disrupts reading frame, NOT predicted to undergo NMD (Exon 18) | Truncated/altered region is critical to protein function (Exon 18) | PVS1_Strong |
| Exon skipping/cryptic splice preserves reading frame (Exons 7, 10, 13, 17) | Role of region in protein function is unknown (Exon 17) | PVS1_Moderate |
| Exon skipping/cryptic splice preserves reading frame (Exons 7, 10, 13, 17) | Truncated/altered region is critical to protein function (Exons 7, 10, 13) | PVS1 |

#### Deletions (Single Exon to Full Gene)

| Scenario | Condition | Strength |
|----------|-----------|----------|
| Full gene deletion | - | PVS1 |
| Single to multi exon deletion, disrupts reading frame, predicted to undergo NMD | Exon is present in biologically-relevant transcript(s) | PVS1 |
| Single to multi exon deletion, disrupts reading frame, predicted to undergo NMD | Exon is absent from biologically-relevant transcript(s) | N/A |
| Single to multi exon deletion, disrupts reading frame, NOT predicted to undergo NMD (Exon 18) | Truncated/altered region is critical to protein function (Exon 18) | PVS1_Strong |
| Single to multi exon deletion, preserves reading frame (Exons 7, 10, 13, 17) | Role of region in protein function is unknown (Exon 17) + LoF variants in this exon are not frequent in general population | Variant removes >10% of protein: PVS1<br>Variant removes <10% of protein: PVS1_Moderate |
| Single to multi exon deletion, preserves reading frame | Truncated/altered region is critical to protein function (Exons 1, 7, 10, 13 + any in-frame combination including PM1 functional domains: p.19_43 ATP binding or p.169_171 TEY phosphorylation) | PVS1 |
| Deletion of non-coding region (Exon 1) | - | PVS1 |

#### Duplications (≥1 Exon, Completely Contained Within Gene)

| Scenario | Condition | Strength |
|----------|-----------|----------|
| Proven in tandem | Reading frame disrupted and NMD predicted to occur | PVS1 |
| Proven in tandem | No or unknown impact on reading frame and NMD | N/A |
| Presumed in tandem | Reading frame presumed disrupted and NMD predicted to occur | PVS1_Strong |
| Proven not in tandem | - | N/A |

#### Initiation Codon Variants

| Scenario | Condition | Strength |
|----------|-----------|----------|
| No known alternative start codon in other transcripts | No pathogenic variant(s) upstream of closest potential in-frame start codon | PVS1_Supporting |

---

### Appendix B: Population Frequency Thresholds Summary

| Criterion | Threshold | Strength |
|-----------|-----------|----------|
| BA1 | ≥0.05% (0.0005) in any sub-population | Stand Alone |
| BS1 | ≥0.00083% and <0.0083% in any sub-population | Strong |
| PM2 | Absent (0 observations) in control databases | Supporting |

**Note:** Use allele frequency from any general continental population dataset of at least 2,000 observed alleles. Use large population databases (i.e., gnomAD).

---

### Appendix C: Computational Predictor Thresholds

| Predictor | PP3 Threshold (Pathogenic) | BP4 Threshold (Benign) | Application |
|-----------|---------------------------|------------------------|-------------|
| REVEL | ≥0.644 | ≤0.290 | Missense variants |
| SpliceAI | ≥0.2 | ≤0.1 | Splice site variants |

**Reference:** Pejaver V, Byrne AB et al. (2022) PMID: 36413997

---

### Appendix D: References

1. Krishnaraj R, Ho G et al. *RettBASE: Rett syndrome database update.* **Hum Mutat** (2017) 38(8):922-931. PMID: 28544139

2. Raymond L, Diebold B et al. *Validation of high-resolution DNA melting analysis for mutation scanning of the CDKL5 gene: identification of novel mutations.* **Gene** (2013) 512(1):70-5. PMID: 23064044

3. Hector RD, Kalscheuer VM et al. *CDKL5 variants: Improving our understanding of a rare neurologic disorder.* **Neurol Genet** (2017) 3(6):e200. PMID: 29264392

4. Rosas-Vargas H, Bahi-Buisson N et al. *Impairment of CDKL5 nuclear localisation as a cause for severe infantile encephalopathy.* **J Med Genet** (2008) 45(3):172-8. PMID: 17993579

5. Wang IT, Allen M et al. *Loss of CDKL5 disrupts kinome profile and event-related potentials leading to autistic-like phenotypes in mice.* **Proc Natl Acad Sci U S A** (2012) 109(52):21516-21. PMID: 23236174

6. Pejaver V, Byrne AB et al. *Calibration of computational tools for missense variant pathogenicity classification and ClinGen recommendations for PP3/BP4 criteria.* **Am J Hum Genet** (2022) 109(12):2163-2177. PMID: 36413997

---

### Appendix E: Criteria Summary Table

| Criterion | Applicable Strengths | Modification Type |
|-----------|---------------------|-------------------|
| PVS1 | Very Strong, Strong, Moderate, Supporting | Disease-specific |
| PS1 | Strong | None |
| PS2 | Very Strong, Strong | No change |
| PS3 | Strong, Supporting | Disease-specific |
| PS4 | Strong, Moderate, Supporting | Strength |
| PM1 | Moderate | Disease-specific |
| PM2 | Supporting | Strength |
| PM3 | Not Applicable | - |
| PM4 | Moderate, Supporting | Disease-specific, Strength |
| PM5 | Strong, Moderate | Strength, None |
| PM6 | Very Strong, Strong, Moderate | Strength |
| PP1 | Strong, Moderate, Supporting | Strength |
| PP2 | Not Applicable | - |
| PP3 | Supporting | General recommendation |
| PP4 | Supporting | Disease-specific |
| PP5 | Not Applicable | - |
| BA1 | Stand Alone | Disease-specific |
| BS1 | Strong | Disease-specific |
| BS2 | Strong, Supporting | Strength |
| BS3 | Strong | Disease-specific |
| BS4 | Strong, Supporting | Strength |
| BP1 | Not Applicable | - |
| BP2 | Supporting | Disease-specific |
| BP3 | Supporting | None |
| BP4 | Supporting | General recommendation |
| BP5 | Strong, Moderate, Supporting | Disease-specific, Strength |
| BP6 | Not Applicable | - |
| BP7 | Supporting | None |

---

## Version History

| Version | Release Date | Notes |
|---------|--------------|-------|
| 5.0.0 | 7/30/2025 | Modification to the population frequency cutoffs for BA1 and BS1 |

---

*This document was compiled from ClinGen VCEP specifications. For the most current version, please refer to the ClinGen website.*

*ClinGen Rett and Angelman-like Disorders Expert Panel*
