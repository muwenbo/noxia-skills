# ClinGen TP53 VCEP Variant Interpretation Guidelines for TP53

**Version:** 2.4.0
**Released:** 11/20/2025
**Affiliation:** TP53 VCEP
**Based on:** Tavtigian et al., 2020 - Bayesian adaptation of Richards et al., 2015 ACMG/AMP Guidelines
**Classification System:** Point-based (modified Bayesian points system)

---

## Gene Information

| Attribute | Value |
|-----------|-------|
| **Gene** | TP53 (HGNC:11998) |
| **HGNC Name** | tumor protein p53 |
| **Transcript** | NM_000546.5 |
| **Disease** | Li-Fraumeni syndrome (MONDO:0018875) |
| **Inheritance** | Autosomal dominant inheritance |

---

## TP53 Protein Domains

| Domain | Amino Acid Range |
|--------|-----------------|
| **TAD1** | aa 17-25 |
| **TAD2** | aa 48-56 |
| **Proline residues** | aa 64-92 |
| **DNA binding domain** | aa 100-292 |
| **Hinge domain** | aa 293-324 |
| **Oligomerization domain** | aa 325-356 |
| **C-terminal domain (Basic domain)** | aa 368-387 |

---

## Point-Based Classification System

| Category | Point Range |
|----------|------------|
| **Pathogenic** | ≥ 10 |
| **Likely Pathogenic** | 6 to 9 |
| **Uncertain Significance (VUS)** | -1 to 5 |
| **Likely Benign** | -6 to -2 |
| **Benign** | ≤ -7 |

> **CAVEAT:** A final point value of -1 may be overridden to Likely Benign in cases where at least 2 benign evidence codes are applied AND PM2_Supporting is the only pathogenic code applied.

---

## Table of Contents

1. [Pathogenic Criteria](#pathogenic-criteria)
   - [PVS1 - Null Variant](#pvs1---null-variant)
   - [PS1 - Same Amino Acid Change](#ps1---same-amino-acid-change)
   - [PS2 - De Novo](#ps2---de-novo)
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
   - [PP4 - Phenotype Specificity / Low VAF (CHIP)](#pp4---phenotype-specificity--low-vaf-chip)
   - [PP5 - Reputable Source](#pp5---reputable-source)
2. [Benign Criteria](#benign-criteria)
   - [BA1 - Allele Frequency ≥0.1%](#ba1---allele-frequency-01)
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

**Default Point Value:** 8 (Very Strong)

**VCEP Specifications:**

Please utilize the PVS1 decision tree for application of PVS1 code. The decision tree details the specific strengths each type of null variant may be applied at. Summary details below:

#### Initiation Codon Variants

- **PVS1** (8 points): PVS1 may be applied to initiation codon variants

#### Nonsense or Frameshift Variants

| Condition | Strength | Points |
|-----------|----------|--------|
| Predicted to result in NMD: nonsense upstream of p.Lys351 or frameshift-induced PTC upstream of p.Lys351 | **PVS1** | 8 |
| Not predicted to undergo NMD, variant in **p.Lys351 to p.Ala355** range (removes >10% of protein) | **PVS1_Strong** | 4 |
| Not predicted to undergo NMD, variant in **p.Gly356 to p.Asp393** range (removes <10% of protein) | **PVS1_Moderate** | 2 |
| Frameshift-induced PTC downstream of the natural stop codon (stop codon read-through) | **PVS1_Moderate** | 2 |

#### Canonical Splice Variants (±1,2 intronic positions)

| Condition | Strength | Points |
|-----------|----------|--------|
| Predicted splicing alterations that are PTC resulting in NMD (or in-frame but targeting critical domains/residues) — E3 through E10 acceptor/donor sites | **PVS1** | 8 |
| Predicted splicing alterations that target the start codon (Exon 2 donor) | **PVS1** | 8 |
| Predicted splicing alterations do not affect reading-frame (E1 donor, E2 acceptor) | **PVS1_N/A** | — |
| Some predictions are very short in-frame with no obvious functional impact (E8 acceptor) | **PVS1_N/A** | — |
| Splicing alteration predicted to shorten (<10% of protein removed) or expand C-terminal end of unknown function (E10 donor, E11 acceptor) | **PVS1_Moderate** | 2 |

#### Deletions (Single Exon to Full Gene)

| Condition | Strength | Points |
|-----------|----------|--------|
| Full gene deletion | **PVS1** | 8 |
| Single exon deletion does not target the coding sequence (delE1) | **PVS1_N/A** | — |
| Deletion targeting initiation codon, preserving rescue ATG p.Met40 in exon 4 (delE1_E2, delE1_E3, delE2, delE2_E3) | **PVS1** | 8 |
| Deletion targeting initiation codon AND rescue ATG p.Met40 (e.g., delE1_E7, delE2_E5, delE2_E10) | **PVS1** | 8 |
| Deletion disrupting reading frame, predicted NMD (PTC upstream of p.Lys351) — e.g., delE3, delE5, delE6, delE7, delE8, delE9 and multi-exon combinations | **PVS1** | 8 |
| Deletion disrupting reading frame, NOT predicted NMD — truncated/altered region critical (delE10, multi-exon ending in intron 10) | **PVS1** | 8 |
| Deletion including last exon — truncated/altered region critical (any multi-exon combination targeting E11, e.g., delE10_E11, delE5_E11) | **PVS1** | 8 |
| Deletion including last exon — role unknown, removes <10% protein (delE11) | **PVS1_Moderate** | 2 |
| Deletion preserves reading frame — truncated/altered region critical (delE4, and multi-exon combinations) | **PVS1** | 8 |

#### Duplications (≥1 exon, completely contained within TP53)

| Condition | Strength | Points |
|-----------|----------|--------|
| **Proven in tandem** — reading frame disrupted, NMD predicted (e.g., dupE3, dupE5_E7) | **PVS1** | 8 |
| **Proven in tandem** — no/unknown impact on reading frame and NMD (e.g., dupE4, dupE5_E6) | **PVS1_N/A** | — |
| **Proven in tandem** — targets initiation codon (e.g., dupE2, dupE2_E3) | **PVS1_N/A** | — |
| **Presumed in tandem** — reading frame presumed disrupted, NMD predicted (e.g., dupE3, dupE5_E7) | **PVS1_Strong** | 4 |
| **Presumed in tandem** — no/unknown impact on reading frame and NMD | **PVS1_N/A** | — |
| **Presumed in tandem** — targets initiation codon | **PVS1_N/A** | — |
| **Proven not in tandem** | **PVS1_N/A** | — |

#### RNA-based Evidence

For variants inducing aberrant transcripts identified via mRNA assay, apply as **PVS1_Variable Weight (RNA)** following recommendations from Walker et al., 2023 (PMID: 37352859), downgrading one strength level if the assay data indicates leakiness.

#### PVS1 Caveats

- PS3 should **not** be applied at any strength if PVS1 is applied at full strength (8 points)
- Downgrade PS3 to PS3_Moderate if PVS1_Strong is applied
- PP3 should **not** be used in combination with PVS1

---

### PS1 - Same Amino Acid Change

**Original ACMG Summary:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.

**VCEP Specifications:** This rule code can only be used to compare variants asserted as pathogenic or likely pathogenic following the ClinGen *TP53* VCEP's specifications. Must confirm there is no difference using RNA data or SpliceAI (SpliceAI < 0.2).

| Strength | Criteria | Points |
|----------|----------|--------|
| **Strong** | Can be applied to variants asserted as **Pathogenic** following the *TP53* VCEP's specifications | 4 |
| **Moderate** | Can be applied to variants asserted as **Likely Pathogenic** following the *TP53* VCEP's specifications | 2 |

**Caveat:** If both PS1 and PM5 are met, apply the strongest weight possible for each rule code not to exceed a combined strength of **strong (4 points in total)**.

---

### PS2 - De Novo

**Original ACMG Summary:** De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.

**VCEP Specifications:** *De novo* points should be tallied using the table for tallying proband points based on whether maternity and paternity have been confirmed and the type of cancer(s) seen in the proband. This includes probands that are confirmed constitutional mosaics (low *TP53* VAF on blood or buccal testing with the mutation detected in non-lymphocyte tissue and/or segregating in children) which may be counted as a confirmed *de novo* case.

For probands with multiple cancers, use the most specific/highest weight cancer to determine point application for that proband. Points for all probands should be tallied to determine the strength of PS2 code application, consistent with SVI guidance.

> **Note:** The *TP53* VCEP has opted to drop PM6 and use PS2 exclusively for *de novo* evidence.

#### Table of LFS Cancers and Points for PS2 Code Application

**Strongly Associated LFS Cancers:**

| Points per Proband | Cancer Type |
|-------------------|-------------|
| **4 points** (maternity & paternity confirmed) | Breast cancer (including DCIS) < 31 years of age |
| **4 points** (confirmed) | Choroid plexus carcinoma |
| **4 points** (confirmed) | Adrenocortical adenoma or carcinoma < 18 years of age |
| **4 points** (confirmed) | Rhabdomyosarcoma or osteosarcoma < 46 years of age |
| **2 points** (maternity & paternity assumed) | Same cancers as above |

**Moderately Associated LFS Cancers:**

| Points per Proband | Cancer Type |
|-------------------|-------------|
| **2 points** (maternity & paternity confirmed) | Breast cancer (including DCIS) ≥ 31 and < 50 years of age |
| **2 points** (confirmed) | Malignant brain tumor (excluding optic glioma) < 46 years of age |
| **2 points** (confirmed) | Adrenocortical adenoma or carcinoma ≥ 18 and < 50 years of age |
| **2 points** (confirmed) | Primary lung cancer (excluding carcinoid tumors) < 46 years of age |
| **2 points** (confirmed) | Rhabdomyosarcoma or osteosarcoma > 45 years of age |
| **2 points** (confirmed) | Other sarcoma (e.g., malignant phyllodes tumor, leiomyosarcoma, liposarcoma, etc.) < 60 years of age (**EXCEPT** dermatofibrosarcoma or Ewing sarcoma) |
| **2 points** (confirmed) | Hypodiploid acute lymphoblastic leukemia |
| **2 points** (confirmed) | Sonic hedgehog-activated medulloblastoma |
| **1 point** (maternity & paternity assumed) | Same cancers as above |

#### PS2 Code Strength Based on Total Points

| Strength | Total Points | Default Point Value |
|----------|-------------|-------------------|
| **PS2_Supporting** | 1 | 1 |
| **PS2_Moderate** | 2-3 | 2 |
| **PS2 (Strong)** | 4-7 | 4 |
| **PS2_Very Strong** | ≥ 8 | 8 |

---

### PS3 - Functional Studies

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.

**VCEP Specifications:**

Kato et al., 2003 (PMID: 12826609) systematic data performed best on the test set of reference variants and remains the primary functional assay underlying the classification. Giacomelli et al., 2018 (PMID: 30224644) assays are also systematic and available for all p53 missense variants. Both Kato and Giacomelli assays have results available for every possible missense variant.

#### Approved Assay Instances and Thresholds

**1. Kato et al., 2003 (PMID: 12826609) — Transactivation Class:**
Classification based on the median transactivation activity using eight promoters in yeast. Values can be found in the NCI TP53 Database.

| Classification | Activity Threshold |
|---------------|-------------------|
| **Non-functional** | ≤ 20% activity |
| **Partially-functional** | > 20% and ≤ 75% activity |
| **Functional** | > 75% activity (supertransactivation treated as Functional) |

**2. Giacomelli et al., 2018 (PMID: 30224644) — Growth Suppression Assay:**
Classification based on results from growth suppression assays in A549 human cells.

| Classification | Etoposide Z-score Threshold |
|---------------|---------------------------|
| **LOF** | ≤ -0.21 |
| **No LOF** | > -0.21 |

**3. Kawaguchi et al., 2005 (PMID: 16007150) — Oligomerization Assay:**
Classification based on the ability to form an oligomer in yeast.

| Classification | Result |
|---------------|--------|
| **Abnormal** | Monomer/dimer |
| **Normal** | Tetramer |

**4. Kotler et al., 2018 (PMID: 29979965) — Relative Fitness Score:**
Classification based on relative fitness scores (RFS) from in vitro growth assays in H1299 human cells. Available only for variants within the DNA binding domain.

| Classification | RFS Threshold |
|---------------|--------------|
| **LOF** | RFS ≥ -1.0 |
| **No LOF** | RFS < -1.0 |

**5. Funk et al., 2025 (PMID: 39774325) — CRISPR Saturation Mutagenesis:**
Classification based on relative fitness scores (RFS) from CRISPR-mediated saturation mutagenesis in human cancer cells. Results available for a limited number of exons.

| Classification | RFS Threshold |
|---------------|--------------|
| **LOF** | RFS ≥ 0 |
| **No LOF** | RFS < 0 |

**6. Other Assays:**
Colony formation assays, growth suppression assays, apoptosis assays, tetramer assays, or knock-in mouse models may be considered. Non-systematic assays are harder to calibrate but if they meet Brnich et al., 2019 (PMID: 31892348) recommendations and agree with Kato et al., 2003, they should be taken into account.

#### PS3 Strength Determination — Missense Variants with Kato Data

| Kato Classification | Other Assay Results | Code | Points |
|--------------------|--------------------|----|--------|
| **Non-functional** | LOF by majority of other eligible assays | **PS3 (Strong)** | 4 |
| **Non-functional** | noLOF (Giacomelli) BUT Abnormal (Kawaguchi) | **PS3_Supporting** | 1 |
| **Partially functional** | LOF by majority of other available assays | **PS3_Moderate** | 2 |
| **Partially functional** | noLOF by all available assays | **BS3_Supporting** | -1 |
| **Functional** | noLOF by majority of available eligible assays | **BS3 (Strong)** | -4 |

#### PS3 Strength Determination — Missense Variants without Kato Data & Small Deletions

| Other Assay Results | Code | Points |
|--------------------|------|--------|
| LOF by majority of available assays | **PS3_Supporting** | 1 |
| noLOF by majority of available assays | **BS3_Supporting** | -1 |

> **Note:** PS3_Supporting may also be applied to small deletions that demonstrate LOF on the majority of available assays.

#### PS3/BS3 Caveats

- **Do not** apply PS3 at any weight for "missense" variants using protein-level assays (Kato, Giacomelli) if PP3 is applied based on SpliceAI
- If there is any laboratory evidence of splicing aberration, consider PVS1_Variable Weight (RNA) instead
- Functional missense codes should **not** be applied if PVS1 is applied for splicing
- Downgrade to PS3_Moderate if PVS1_Strong is applied
- **Do not** apply PS3 at any strength if PVS1 is applied at full strength (8 points)

---

### PS4 - Prevalence in Affected

**Original ACMG Summary:** The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.

**VCEP Specifications:**

There are two widely used clinical criteria for assessing the likelihood of Li-Fraumeni syndrome — Classical and Chompret criteria — with the Chompret criteria being less restrictive.

#### PS4 Point System per Proband

| Evidence Type | Single Observation | Points per Proband |
|--------------|-------------------|-------------------|
| **Clinical Criteria** | Revised Chompret | 0.5 |
| **Clinical Criteria** | Classic LFS Criteria | 1 |
| **Tumor Pathology** | HER2+ breast cancer < 40 years* | 0.5 |

> \* Do not apply the HER2+ half point to individuals who have been given points for meeting Classical or Chompret criteria due to breast cancer diagnosis <31 years of age. Points attributed to HER2 status may only be applied in unrelated individuals who underwent multigene panel testing with no other P/LP variants in cancer predisposition genes.

#### PS4 Code Strength Based on Total Points

| Strength | Total Points | Default Point Value |
|----------|-------------|-------------------|
| **PS4_Supporting** | 1-1.5 | 1 |
| **PS4_Moderate** | 2-3.5 | 2 |
| **PS4 (Strong)** | 4-7.5 | 4 |
| **PS4_Very Strong** | ≥ 8 | 8 |

#### PS4 Caveats

- Do not apply PS4 for probands with *de novo TP53* variants — use PS2 instead
- Variant must meet **PM2_Supporting** in order for PS4 to be applied at any strength
- Individuals who underwent targeted *TP53* single gene testing may not count towards applied points

---

### PM1 - Mutational Hot Spot

**Original ACMG Summary:** Located in a mutational hot spot and/or critical and well-established functional domain without benign variation.

**VCEP Specifications:**

There are several known major hotspots for the *TP53* gene. This code can be used for variants within the following codons using canonical transcript NM_000546.4: **175, 245, 248, 249, 273, 282**.

This code can also be used for germline missense variants seen in cancerhotspots.org (v2) with ≥ 10 somatic occurrences for the same amino acid change, following the recommendation from the ClinGen Germline/Somatic Variant Curation Subcommittee (PMID: 30311369).

| Strength | Criteria | Points |
|----------|----------|--------|
| **Moderate** | Missense variants within codons 175, 245, 248, 249, 273, 282 (NM_000546.4) OR germline missense variants in cancerhotspots.org with **≥ 10** somatic occurrences for the same amino acid change | 2 |
| **Supporting** | Missense variants seen in cancerhotspots.org with **2-9** somatic occurrences for the same amino acid change | 1 |

---

### PM2 - Absent from Controls

**Original ACMG Summary:** Absent from controls (or at extremely low frequency if recessive) in population databases.

**VCEP Specification (Supporting only, 1 point):**

- Variant should have an allele frequency of **< 0.00003 (0.003%)** in gnomAD or another large sequenced population
- If multiple alleles are present within any genetic ancestry group, allele frequency in that group must be **< 0.00004 (0.004%)**
- Genetic ancestry groups influenced by founder effects (Ashkenazi Jewish, Finnish, Amish, Middle Eastern, and "Remaining") should be ignored
- If the variant does not meet any population rule codes (PM2, BA1, BS1) **AND** has a total allele frequency > 0.00003 with no single genetic ancestry group having multiple alleles with a frequency > 0.00004, curators should recalculate allele frequency based on alleles with VAF > 0.35 to exclude likely CHIP contamination
- In general, the most recent version of gnomAD should be used

| Strength | Criteria | Points |
|----------|----------|--------|
| **Supporting** | Allele frequency < 0.00003 in gnomAD (with ancestry group adjustment) | 1 |

---

### PM3 - In Trans with Pathogenic

**Original ACMG Summary:** For recessive disorders, detected in trans with a pathogenic variant.

**Not Applicable.** This rule does not apply to TP53/Li-Fraumeni syndrome (autosomal dominant).

---

### PM4 - Protein Length Changes

**Original ACMG Summary:** Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

**Not Applicable.**

---

### PM5 - Novel Missense at Same Residue

**Original ACMG Summary:** Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.

**VCEP Specifications:** This code can be applied for a missense change at an amino acid residue where one or more pathogenic/likely pathogenic variants have been identified following the ClinGen *TP53* VCEP's specifications. The previously established P/LP variant must reach a classification of pathogenicity without PM5.

Grantham should be used to compare the variants. The variant being evaluated must be equal or worse (Grantham value is greater than) than the known pathogenic variant. Splicing should be ruled out with either RNA data or SpliceAI (SpliceAI < 0.2).

| Strength | Criteria | Points |
|----------|----------|--------|
| **Strong** | Missense variant at an amino acid residue where **≥ 2** different missense variants previously determined to be **Pathogenic** according to the *TP53* VCEP's specifications | 4 |
| **Moderate** | Missense variant at an amino acid residue where **1** different missense variant previously determined to be **Pathogenic** according to the *TP53* VCEP's specifications | 2 |
| **Supporting** | Missense variant at an amino acid residue where **1** different missense variant previously determined to be **Likely Pathogenic** according to the *TP53* VCEP's specifications. The previously seen LP variant must have clinical data demonstrating pathogenicity (i.e., PS2, PS4, PP1) | 1 |

**Caveat:** If both PS1 and PM5 are met, apply the strongest weight possible for each rule code not to exceed a combined strength of **strong (4 points in total)**.

---

### PM6 - De Novo (Assumed)

**Original ACMG Summary:** Assumed de novo, but without confirmation of paternity and maternity.

**Not Applicable.** Combined with PS2. Use PS2 instead of PM6.

---

### PP1 - Co-segregation

**Original ACMG Summary:** Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.

**VCEP Specifications:** Meioses should be counted for individuals who both carry the variant and have a relevant cancer (see LFS cancers table). Meioses can be counted through unaffected obligate carriers. Caution should be used in counting meioses across many families where breast cancer is the only cancer present as this is a common cancer type.

In cases where multiple individuals in a family have a relevant cancer and only tumor testing demonstrating the variant (no germline data), meioses may be applied if the variant has been demonstrated in the germline in at least one individual in the family.

**Caveats:**
- Positive tumor testing must exist in multiple family members; meioses should not be applied if there is only positive tumor testing in a single individual
- If the variant allele fraction in the tumor is not consistent with the variant being heterozygous, it should not count towards meioses
- Use caution if the family does not meet Classic LFS criteria
- Do not apply PP1 if variant meets BA1/BS1 criteria

| Strength | Criteria | Points |
|----------|----------|--------|
| **Strong** | Cosegregation in ≥ 7 meioses across > 1 family | 4 |
| **Moderate** | Cosegregation in 5-6 meioses in/across 1 or more families | 2 |
| **Supporting** | Cosegregation in 3-4 meioses in/across 1 or more families | 1 |

See Table of LFS Cancers for PP1 (and PS2) code application (same table as PS2 above).

---

### PP2 - Missense in Constrained Gene

**Original ACMG Summary:** Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.

**Not Applicable.**

---

### PP3 - Computational Evidence

**Original ACMG Summary:** Multiple lines of computational evidence support a deleterious effect on the gene or gene product.

**VCEP Specifications:**

According to the published study by Fortuno et al., 2018 (PMID: 29775997), the tools selected are **aGVGD** (not available for single amino acid in-frame deletions) and **BayesDel**. To investigate potential effects on splicing, the **SpliceAI** tool was selected based on recommendations from the ClinGen SVI Splicing Subgroup. All variants should be assessed to consider if there are splicing effects predicted. **PP3 should not be used in combination with PVS1.**

#### Missense Variants

| Strength | Criteria | Points |
|----------|----------|--------|
| **PP3_Moderate** | aGVGD Class **C65** AND BayesDel score **≥ 0.16** (AND no predicted splicing, SpliceAI < 0.2) | 2 |
| **PP3 (Supporting)** | aGVGD class **C25-C55** AND BayesDel score **≥ 0.16** (AND no predicted splicing, SpliceAI < 0.2) | 1 |
| *No evidence* | aGVGD class **C0-C15** AND BayesDel **< 0.16** | — |
| *No evidence* | aGVGD class **C65** AND BayesDel **< 0.16** | — |

#### Single Amino Acid In-Frame Deletions

| Strength | Criteria | Points |
|----------|----------|--------|
| **PP3 (Supporting)** | BayesDel score **≥ 0.16** | 1 |

#### Exonic Splice Variants and Intronic Splice Variants (excluding ±1,2 positions)

Includes synonymous (silent) variants and apparent "missense" variants or "single amino acid in-frame deletions" for which there is a predicted splice effect.

| Strength | Criteria | Points |
|----------|----------|--------|
| **PP3 (Supporting)** | SpliceAI **≥ 0.2** | 1 |

---

### PP4 - Phenotype Specificity / Low VAF (CHIP)

**Original ACMG Summary:** Patient's phenotype or family history is highly specific for a disease with a single genetic etiology.

**VCEP Specifications:**

The frequency of likely somatic variants in blood among patients undergoing multigene panel testing is high for variants in *TP53*. *TP53* variants observed at a low variant allele fraction (VAF) may be due to true constitutional mosaicism, technical assay issues, a clone driven by underlying malignancy or previous treatment with chemotherapy, or clonal hematopoiesis of indeterminate potential (CHIP).

Fortuno et al., 2022 (PMID: 34906512) demonstrated that the observation of *TP53* variants at low VAF is a significant predictor of variant pathogenicity.

| Strength | Criteria | Points |
|----------|----------|--------|
| **Moderate** | At least **2** independent observations of the variant with VAF **5-25%** | 2 |
| **Supporting** | Observation of the variant with VAF **5-35%** (i.e., once or multiple times with VAF >25-35% and/or once with VAF 5-25%) | 1 |

#### PP4 Caveats

- This evidence code assumes a somatic origin of the *TP53* variant
- PP4 and points towards any phenotype-based rule codes (e.g., PS4, PS2, PP1) cannot be applied **in the same individual** in combination
- This code should **not** be applied if the low VAF *TP53* variant has been identified in a patient with blood cancer
- Do not apply this code if variant meets BA1 or BS1
- Variant must have been detected on MGPT in order for this code to be applied

---

### PP5 - Reputable Source

**Original ACMG Summary:** Reputable source recently reports variant as pathogenic, but the evidence is not available to the laboratory to perform an independent evaluation.

**Not Applicable.** This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PMID: 29543229).

---

## Benign Criteria

### BA1 - Allele Frequency ≥0.1%

**Original ACMG Summary:** Allele frequency is above 5% in population databases.

**VCEP Specification (Stand Alone):**

Filtering allele frequency (FAF) of **≥ 0.001 (0.1%)** in gnomAD continental subpopulations of a single genetic ancestry group (excluding genetic ancestry groups influenced by founder effects: Ashkenazi Jewish, Finnish, Amish, Middle Eastern, and "Remaining").

- Genetic ancestry group must have ≥ 2,000 alleles tested and a minimum of 2 alleles present
- Caution should be exerted if the majority of alleles have a variant allele fraction ("allele balance" in gnomAD) below 0.35

| Criterion | Threshold | Classification |
|-----------|-----------|---------------|
| **BA1** | FAF ≥ 0.001 (0.1%) | **Benign (Stand Alone)** |

---

### BS1 - Frequency Greater Than Expected

**Original ACMG Summary:** Allele frequency is greater than expected for disorder.

**VCEP Specification (Strong, -4 points):**

Filtering allele frequency (FAF) of **≥ 0.0003 but < 0.001** in gnomAD continental subpopulations of a single genetic ancestry group (excluding founder effect groups).

- Genetic ancestry group must have ≥ 2,000 alleles tested and a minimum of 2 alleles present
- Caution should be exerted if the majority of alleles have a variant allele fraction below 0.35
- Calculated using Whiffin-Ware method: prevalence 1 in 5,000, genetic and allelic heterogeneity at 100%, penetrance at 30%

| Criterion | Threshold | Points |
|-----------|-----------|--------|
| **BS1** | FAF ≥ 0.0003 and < 0.001 | -4 |

---

### BS2 - Observed in Healthy Adult

**Original ACMG Summary:** Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

**VCEP Specifications:** Using *TP53* multigene panel testing results from two diagnostic labs, the VCEP compared the proportion of cancer-free individuals by age 60 in *TP53* carriers vs. *TP53*-negative controls. Females counted towards BS2 should be unrelated probands. If there is any VAF provided, variants with VAF ≤ 35%, suggestive of somatic origin, should not be included in these counts. Individuals with a diagnosis of sarcoma ≥ 61 years of age should not be counted towards the BS2 total.

| Strength | Criteria | Points |
|----------|----------|--------|
| **Strong** | ≥ 8 unrelated females who have reached at least 60 years of age without cancer (from a single source) | -4 |
| **Moderate** | 4-7 unrelated females who have reached at least 60 years of age without cancer (from a single source) | -2 |
| **Supporting** | 2-3 unrelated females who have reached at least 60 years of age without cancer (from a single source) | -1 |

> Cases cannot be counted across sources. Individuals must all come from a single source (single lab, database, etc.).

---

### BS3 - Functional Studies (No Effect)

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

**VCEP Specifications:** Same assays as PS3 (see above for assay thresholds and classifications).

#### BS3 Strength Determination — Missense Variants with Kato Data

| Kato Classification | Other Assay Results | Code | Points |
|--------------------|--------------------|----|--------|
| **Functional** | noLOF by majority of available eligible assays | **BS3 (Strong)** | -4 |
| **Partially functional** | noLOF by **all** available assays | **BS3_Supporting** | -1 |

#### BS3 for Small Deletions

- BS3_Supporting may also be applied to small deletions with available Kotler et al. data that are LOF by the majority of available assays

#### BS3 Caveats

- **Do not** apply BS3 at any weight for "missense" variants using protein-level assays (Kato, Giacomelli) if PP3 is applied based on SpliceAI
- If there is any laboratory evidence of splicing aberration, consider PVS1_Variable Weight (RNA) instead
- Functional missense codes should **not** be applied if PVS1 is applied for splicing

---

### BS4 - Lack of Segregation

**Original ACMG Summary:** Lack of segregation in affected members of a family.

**VCEP Specification (Strong, -4 points):**

Lack of segregation in affected family members (i.e., family members diagnosed with LFS-associated cancers as described in Table of LFS Cancers and Points for PS2 and PP1 Code Application).

| Strength | Criteria | Points |
|----------|----------|--------|
| **Strong** | Lack of segregation in affected family members | -4 |

---

### BP1-BP7 - Benign Supporting

| Criterion | Status | Comment |
|-----------|--------|---------|
| **BP1** | Not Applicable | This rule code does not apply to these genes, as truncating variants account for only a portion of disease causing variants |
| **BP2** | Not Applicable | Not applicable |
| **BP3** | Not Applicable | Not applicable |
| **BP4** | Applicable (see below) | Computational evidence suggesting no impact |
| **BP5** | Not Applicable | Not applicable |
| **BP6** | Not Applicable | Not for use as recommended by ClinGen SVI (PMID: 29543229) |
| **BP7** | Applicable (see below) | Synonymous/intronic variant with no predicted splicing impact |

#### BP4 - Computational Evidence (Benign)

**Missense Variants:**

| Strength | Criteria | Points |
|----------|----------|--------|
| **BP4_Moderate** | BayesDel **≤ -0.008** irrespective of aGVGD score (**except C65** — do not apply BP4_Moderate) AND no predicted differences in splicing (SpliceAI < 0.2) | -2 |
| **BP4 (Supporting)** | BayesDel **< 0.16 and > -0.008** irrespective of aGVGD score (**except C65** — do not apply BP4) AND no predicted differences in splicing (SpliceAI < 0.2) | -1 |

**Single Amino Acid In-Frame Deletions:**

| Strength | Criteria | Points |
|----------|----------|--------|
| **BP4 (Supporting)** | BayesDel score **< 0.16** AND no predicted splicing impact (SpliceAI < 0.2) | -1 |

**Synonymous (Silent) or Intronic Variants (outside ±1,2 positions):**

| Strength | Criteria | Points |
|----------|----------|--------|
| **BP4 (Supporting)** | SpliceAI **≤ 0.1** | -1 |

#### BP7 - Synonymous/Intronic Variant

| Strength | Criteria | Points |
|----------|----------|--------|
| **Strong** | A (synonymous) silent or intronic variant for which RNA splicing assay data demonstrates **no splicing aberration**, as per recommendations from Walker et al., 2023 (PMID: 37352859) | -4 |
| **Supporting** | A synonymous (silent) outside of the core splice motif (last three nucleotides and first nucleotide of the exon) or intronic variant at or beyond +7 to -21 positions for which SpliceAI predicts no impact (BP4 is met, SpliceAI ≤ 0.1). No requirement to assess for nucleotide conservation (Walker et al., 2023; PMID: 37352859) | -1 |

---

## Rules for Combining Criteria

This specification uses the **Tavtigian et al., 2020 Bayesian point-based system** for combining criteria. Points from all applicable criteria are summed to determine the final classification.

### Point-Based Classification

| Category | Total Points |
|----------|-------------|
| **Pathogenic** | ≥ 10 |
| **Likely Pathogenic** | 6 to 9 |
| **Uncertain Significance** | -1 to 5 |
| **Likely Benign** | -6 to -2 |
| **Benign** | ≤ -7 |

### Default Point Values by Strength

| Evidence Strength | Pathogenic Points | Benign Points |
|-------------------|------------------|---------------|
| **Very Strong** | 8 | — |
| **Strong** | 4 | -4 |
| **Moderate** | 2 | -2 |
| **Supporting** | 1 | -1 |
| **Stand Alone** | — | BA1 (Benign) |

### Special Classification Override

A final point value of **-1** may be overridden to **Likely Benign** in cases where at least 2 benign evidence codes are applied AND PM2_Supporting is the only pathogenic code applied.

---

## Appendices

### Appendix A: PVS1 Decision Tree

The disease-specific PVS1 decision tree for *TP53* is available as a supplementary file. It covers:
- Initiation codon variants
- Nonsense or frameshift variants (NMD prediction based on p.Lys351 boundary)
- Canonical splice variants (±1,2 positions) with exon-by-exon predictions
- Single to multi-exon deletions (with reading frame and NMD assessment)
- Duplications (proven vs. presumed in tandem)

Key reference: NM_000546.6 transcript. Splicing predictions for GT-AG sites are based on SpliceAI and available experimental data. PVS1_Variable Weight (RNA) may be applicable for variants with RNA-based assay data demonstrating aberration (see Supplementary Table S1). Δ = exon skipping, ▼ = intron retention.

### Appendix B: PS3/BS3 Functional Flowchart

**Missense variants with Kato data available:**
1. Non-functional (Kato) → LOF by majority of other assays → **PS3**
2. Non-functional (Kato) → noLOF (Giacomelli) BUT Abnormal (Kawaguchi) → **PS3_Supporting**
3. Partially functional (Kato) → LOF by majority of other assays → **PS3_Moderate**
4. Partially functional (Kato) → noLOF by all available assays → **BS3_Supporting**
5. Functional (Kato) → noLOF by majority of available assays → **BS3**

**Missense variants with no available Kato data and small deletions:**
1. LOF by majority of available assays → **PS3_Supporting**
2. noLOF by majority of available assays → **BS3_Supporting**

### Appendix C: PP3/BP4/BP7 In Silico Flowchart

**Missense Variants:**
- BayesDel ≥ 0.16 + aGVGD C65 → **PP3_Moderate**
- BayesDel ≥ 0.16 + aGVGD C25-C55 → **PP3**
- BayesDel < 0.16 + aGVGD C0-C15 → *No evidence*
- BayesDel < 0.16 + aGVGD C65 → *No evidence*
- BayesDel < 0.16 and > -0.008 (except C65) + SpliceAI < 0.2 → **BP4**
- BayesDel ≤ -0.008 (except C65) + SpliceAI < 0.2 → **BP4_Moderate**

**Single aa In-Frame Deletions:**
- BayesDel ≥ 0.16 → **PP3**
- BayesDel < 0.16 + SpliceAI < 0.2 → **BP4**

**Exonic/Intronic Splice Variants (excl. ±1,2):**
- SpliceAI ≥ 0.2 → **PP3**

**Silent or Intronic Variants:**
- SpliceAI ≤ 0.1 → **BP4**
- Silent variant outside core splice motif or intronic at/beyond +7 to -21 where BP4 met → **BP7**

### Appendix D: Population Frequency Thresholds Summary

| Criterion | Threshold | Strength | Points |
|-----------|-----------|----------|--------|
| **BA1** | FAF ≥ 0.001 (0.1%) | Stand Alone (Benign) | N/A |
| **BS1** | FAF ≥ 0.0003 and < 0.001 | Strong (Benign) | -4 |
| **PM2** | AF < 0.00003 (0.003%) | Supporting (Pathogenic) | 1 |

> Exclude genetic ancestry groups influenced by founder effects (Ashkenazi Jewish, Finnish, Amish, Middle Eastern, and "Remaining"). Genetic ancestry group must have ≥ 2,000 alleles tested and a minimum of 2 alleles present.

### Appendix E: Criteria Summary Table

| Criterion | Status | Strength(s) Available | Points |
|-----------|--------|-----------------------|--------|
| PVS1 | Applicable | Very Strong / Strong / Moderate / N/A | 8 / 4 / 2 / — |
| PS1 | Applicable | Strong / Moderate | 4 / 2 |
| PS2 | Applicable | Very Strong / Strong / Moderate / Supporting | 8 / 4 / 2 / 1 |
| PS3 | Applicable | Strong / Moderate / Supporting | 4 / 2 / 1 |
| PS4 | Applicable | Very Strong / Strong / Moderate / Supporting | 8 / 4 / 2 / 1 |
| PM1 | Applicable | Moderate / Supporting | 2 / 1 |
| PM2 | Applicable | Supporting only | 1 |
| PM3 | **Not Applicable** | — | — |
| PM4 | **Not Applicable** | — | — |
| PM5 | Applicable | Strong / Moderate / Supporting | 4 / 2 / 1 |
| PM6 | **Not Applicable** | Combined with PS2 | — |
| PP1 | Applicable | Strong / Moderate / Supporting | 4 / 2 / 1 |
| PP2 | **Not Applicable** | — | — |
| PP3 | Applicable | Moderate / Supporting | 2 / 1 |
| PP4 | Applicable | Moderate / Supporting | 2 / 1 |
| PP5 | **Not Applicable** | — | — |
| BA1 | Applicable | Stand Alone | Benign |
| BS1 | Applicable | Strong | -4 |
| BS2 | Applicable | Strong / Moderate / Supporting | -4 / -2 / -1 |
| BS3 | Applicable | Strong / Supporting | -4 / -1 |
| BS4 | Applicable | Strong | -4 |
| BP1 | **Not Applicable** | — | — |
| BP2 | **Not Applicable** | — | — |
| BP3 | **Not Applicable** | — | — |
| BP4 | Applicable | Moderate / Supporting | -2 / -1 |
| BP5 | **Not Applicable** | — | — |
| BP6 | **Not Applicable** | — | — |
| BP7 | Applicable | Strong / Supporting | -4 / -1 |

### Appendix F: Reference PMIDs

| PMID | Reference | Context |
|------|-----------|---------|
| 12826609 | Kato et al., 2003 | Primary transactivation assay (PS3/BS3) |
| 30224644 | Giacomelli et al., 2018 | Growth suppression assay (PS3/BS3) |
| 16007150 | Kawaguchi et al., 2005 | Oligomerization assay (PS3/BS3) |
| 29979965 | Kotler et al., 2018 | Relative fitness scores, DNA binding domain (PS3/BS3) |
| 39774325 | Funk et al., 2025 | CRISPR saturation mutagenesis (PS3/BS3) |
| 31892348 | Brnich et al., 2019 | Recommendations for functional evidence application |
| 33300245 | — | Non-systematic assay documentation |
| 29775997 | Fortuno et al., 2018 | Bioinformatics tool performance comparison for TP53 (PP3/BP4) |
| 37352859 | Walker et al., 2023 | RNA-based assay recommendations (PVS1, BP7) |
| 26014290 | Bougeard et al., 2015 | Revised Chompret criteria (PS4) |
| 32485079 | Fortuno et al., 2020 | HER2+ breast tumor pathology predictor (PS4) |
| 34906512 | Fortuno et al., 2022 | Low VAF as predictor of pathogenicity (PP4) |
| 29189820 | — | Somatic variants in multigene panel testing (PP4) |
| 30311369 | — | ClinGen Germline/Somatic Variant Curation Subcommittee (PM1) |
| 29300386 | Tavtigian et al., 2018 | Bayesian framework for ACMG/AMP rules (BS2) |
| 16644204 | Lalloo et al., 2006 | LFS prevalence (BS1 calculation) |
| 29543229 | — | ClinGen SVI recommendation against PP5/BP6 |

---

## Version History

| Version | Date | Notes |
|---------|------|-------|
| v2.0.0 | — | Major version 2 VCEP updates with SVI feedback from first submission incorporated. Points based evidence combining criteria based on modified Bayesian points system. |
| v2.1.0 | — | Minor edit to PS3/BS3 language for clarification purposes. No change to rule codes. |
| v2.2.0 | — | Deleted comment from PVS1 spreadsheet. |
| v2.3.0 | — | Minor PP4 language clarifications. Minor BP7 strong code language clarification. Updated functional and in silico flowcharts (publication versions). |
| v2.4.0 | 11/20/2025 | Minor update of the functional rules to incorporate eligible assay data. Added caveat that functional codes should not be applied if PVS1 is applied for splicing. Added clarification to avoid double counting of PS4 HER2+ points. Minor language clarifications. Uploaded additional supporting files. Updated Cspec to Tavtigian points based system instead of combining criteria. |

---

*This document was compiled from ClinGen TP53 VCEP specifications v2.4.0. For the most current version, please refer to the ClinGen website.*
