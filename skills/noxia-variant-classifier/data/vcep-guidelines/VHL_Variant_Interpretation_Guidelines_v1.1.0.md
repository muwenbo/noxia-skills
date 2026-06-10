# ClinGen VHL VCEP Variant Interpretation Guidelines for VHL

**Version:** 1.1.0
**Released:** 1/10/2025
**Affiliation:** VHL VCEP
**Based on:** Richards et al., 2015 ACMG/AMP Guidelines

**Release Notes (v1.1.0):** Clarifications made to PM2, BA1, and BS1. Updated language to gnomAD v4, removed language around using the "non-cancer" set (which did not contain TCGA germline samples) as this set is no longer used in v4. Changed PM2_Supporting from complete absence in gnomAD to PM2_Supporting ≤ 1.56E-6 GroupMax FAF. Disease entity and transcript added.

---

## Gene Information

| Attribute | Value |
|-----------|-------|
| **Gene** | VHL (HGNC:12687) |
| **HGNC Name** | von Hippel-Lindau tumor suppressor |
| **Transcript** | NM_000551.4 |
| **Disease** | von Hippel-Lindau disease (MONDO:0008667) |
| **Inheritance** | Autosomal dominant inheritance |

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

**VCEP Specifications:**

VHL has 3 exons. Loss of function is a known mechanism of VHL disease. The VCEP provides a VHL-specific PVS1 decision tree with the following key modifications:

- **Do not apply PVS1** for truncations that occur prior to Codon 54 (including frameshift events that start and end prior to Codon 54 but the truncation extends beyond Codon 54).
- The 10% PVS1 downgrade to Moderate cannot apply to VHL because of the small gene size.
- All exons should be considered as "present in biologically relevant transcripts" in the PVS1 decision tree.

**VHL Functional Domains:**
- 1st Beta (β) domain: AA 63–154 (especially Nuclear Export: AA 114–155)
- Alpha (α) domain: AA 155–192 (especially Elongin C binding: AA 157–172)
- Second Beta (β) domain: AA 193–204

**NMD Prediction:** Experimental evidence supports NMD in 1st exon after codon 54 and to 5' region of 2nd exon (codon 138). NMD predicted region: AA 55–AA 136 (c.408).

#### Strength Levels

| Variant Type | Condition | Strength |
|--------------|-----------|----------|
| **Nonsense / Frameshift** | Prior to codon 54 | N/A (do not apply) |
| **Nonsense / Frameshift** | Predicted to undergo NMD (AA 54–136) AND exon present in biologically relevant transcript(s) | **PVS1** (Very Strong) |
| **Nonsense / Frameshift** | Not predicted to undergo NMD (AA 137–213) AND in critical domain (AA 63–204) | **PVS1** (Very Strong) |
| **Nonsense / Frameshift** | Not predicted to undergo NMD AND role of region unknown (AA 205–213) | **PVS1_Moderate** |
| **GT-AG splice (±1,2)** | Exon skipping (all exons are critical to VHL function) | **PVS1** (Very Strong) |
| **GT-AG splice** | Cryptic splice disrupts reading frame AND in critical domain (AA 63–204) or NMD predicted (AA 55–136) | **PVS1** (Very Strong) |
| **GT-AG splice** | Cryptic splice disrupts reading frame AND NOT in critical domain AND NMD predicted (AA 55–62) | **PVS1_Strong** |
| **GT-AG splice** | Cryptic splice preserves reading frame AND in critical domain (AA 63–204) | **PVS1_Strong** |
| **GT-AG splice** | Cryptic splice preserves reading frame AND outside critical domain (AA 205–213) or NMD predicted (AA 55–62) | **PVS1_Moderate** |
| **Deletion** | Full gene deletion | **PVS1** (Very Strong) |
| **Deletion** | Single to multi exon deletion (exon present in biologically relevant transcript) | **PVS1** (Very Strong) |
| **Duplication** | Proven in tandem AND reading frame disrupted AND NMD predicted (AA 55–136) | **PVS1** (Very Strong) |
| **Duplication** | Proven in tandem AND no/unknown impact on reading frame and NMD | **N/A** |
| **Duplication** | Presumed in tandem AND reading frame presumed disrupted AND NMD predicted (AA 55–136) | **PVS1_Strong** |
| **Initiation Codon** | Met 1 (VHL p30) — a different functional transcript (VHL p19) uses an alternative start codon at Met 54 | **N/A** |

**Note on splice variants:** There is a cryptic exon (E1') in intron 1, and silent variants in exon 2 are reported to cause skipping of exon 1. If there is functional evidence of exon skipping (RNA splice assay), then PVS1 can apply. Do not double-count evidence — PVS1 should be used in place of PS3 for functional evidence confirming splice alteration, but PS3 may still apply to other relevant assays (e.g., HIF1/2α).

**Note on GT-AG splice sites:** Only applies to variants from codon 54 and on.

**Note on initiation codon:** VHL Met 1 truncation or missense would not affect VHL p19 (second start at codon 54). Start loss at codon 54 would result in impact to both VHL p30 and p19, truncating prior to any known functional domains (PVS1). Missense at Met 54 would not result in as strong an impact as full-length VHL p30 would still be produced (N/A via PVS1 decision tree).

---

### PS1 - Same Amino Acid Change

**Original ACMG Summary:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | Applied only to variants with interpretation by the VHL VCEP or by a variant with pathogenicity established using VHL VCEP specifications. |

**Caveat:** Beware of changes that impact splicing rather than at the amino acid/protein level.

---

### PS2 - De Novo (Confirmed)

**Original ACMG Summary:** De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.

**VCEP Specifications:** Use the SVI-recommended point-based scoring system with disease-specific phenotype detailed as follows:

- **Danish Criteria** (Binderup et al. 2022, updated Danish Criteria): Phenotype highly specific for VHL
- **Consistent Phenotype:** 1 phenotype of VHL disease without family history or strong indication of VHL phenotype
- **Nonspecific Phenotype:** Specific information on tumor types is not provided

**Negative panel testing requirements:**
- For Renal Cell Carcinoma: Tumor histopathology should be clear cell; negative panel should include at least SDHB/C/D
- For Pheochromocytoma only: Negative panels should include at least SDHB/C/D and RET
- If paper states Danish or International Criteria but does not provide case-specific details, count as "Phenotype consistent"
- If there is no family history of VHL disease, RCC and Pheochromocytoma only will count as "Phenotype consistent" (with negative panel testing)

#### PS2/PM6 De Novo Point System

| Phenotypic Consistency | Confirmed de novo (PS2) | Assumed de novo (PM6) |
|------------------------|------------------------|-----------------------|
| Phenotype highly specific for gene (Danish Criteria) | 2 points | 1 point |
| Phenotype consistent with gene but not highly specific (e.g., VHL 2C, Pheo only, gene panel negative) | 1 point | 0.5 points |
| Phenotype consistent but not highly specific and high genetic heterogeneity* (e.g., Pheo only, VHL tested only) | 0.5 points | 0.25 points |
| Phenotype not consistent with gene | 0 points | 0 points |

\*Maximum allowable value of 1 may contribute to overall score.

#### De Novo Evidence Strength Thresholds

| Points | Strength Level |
|--------|----------------|
| ≥0.5 but <1 | Supporting |
| ≥1 but <2 | Moderate |
| ≥2 but <4 | Strong |
| ≥4 | Very Strong |

**Note:** A single proband cannot be very strong evidence, but multiple probands can be combined to reach very strong (4+ points).

---

### PS3 - Functional Studies

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Supporting** | Acceptable assays (see below) that display functional effect. Follow Brnich et al. workflow with ≥10 controls for PS3_Supporting. |

**Note:** PS3 is applied at Supporting strength only for the approved assay types below (based on available validation data). PS3_Moderate may be achieved with ≥11 controls per Brnich et al. guidance. For splicing evidence, PS3 (Strong) applies when RNA transcripts carrying splicing mutation display splicing defects in patient cells; PS3_Moderate applies when demonstrated in in-vivo or in-vitro assays.

**Acceptable assays that display functional effect in VHL:**
1. **HIF 1/2α degradation assays** — HIF1/2α is not degraded
2. **VBC complex stability** — VBC complex stability is affected
3. **ECM formation / Fibronectin binding** — Pathogenicity supported by abnormal ECM formation and impaired fibronectin binding

**VHL Type-specific considerations:**
- **VHL Type 1 and 2A/B:** In-vitro assays should display total loss of HIF1/2α degradation (i.e., HIF1/2α presence). VBC complex stability may also be affected.
- **VHL Type 2C:** Typically missense variants in the alpha domain. Do not usually affect HIF1/2α. If HIF1/2α maintains presence and VHL Type 2C is suspected, assays evaluating fibronectin deposition or extracellular matrix assembly should be used.

**Do not double-count:** If PVS1 is applied for splice variants, PS3 should not also be used for the same splice evidence. PS3 can still apply to other relevant functional assays (e.g., HIF1/2α).

#### Approved Assay Instances

| Assay | Representative PMID | Readout | Approved Strength |
|-------|---------------------|---------|-------------------|
| **VBC Complex Stability (Protein stability assay)** | PMID:21715564 (Rechsteiner 2011) | Western blot — band for intact VHL vs. degradation products | PS3_Supporting |
| **HIF1/2α Degradation** | PMID:11331613 (Clifford 2001) | SDS-PAGE — ubiquitinated vs. non-ubiquitinated HIF1α bands | PS3_Supporting |
| **Fibronectin Binding** | PMID:11331612 (Hoffman 2001) | SDS-PAGE — fibronectin bands at expected sizes | PS3_Supporting |
| **Fibronectin Deposition (ELISA)** | PMID:11331612 (Hoffman 2001) | Plate reader — comparison to WT OD readout | PS3_Supporting |
| **Fibronectin Deposition (Immunofluorescence)** | PMID:11331612 (Hoffman 2001) | Immunofluorescence — presence/shape of fibronectin vs. DAPI | PS3_Supporting |

**Additional representative PMIDs for functional assays:**
- VBC/VCB complex stability: Miller et al. 2005 (PMID:15611064); Hacker et al. 2008 (PMID:19030229); Hansen et al. 2002 (PMID:11865071)
- HIF1/2α degradation: Miller et al. 2005 (PMID:15611064); Clifford et al. 2001 (PMID:11331613); Hacker et al. 2008 (PMID:19030229); Rathmell et al. 2004 (PMID:15574766); Bangiyeva et al. 2009 (PMID:19602254)
- Fibronectin deposition: Ohh et al. 1998 (PMID:9651579)

---

### PS4 - Prevalence in Affected

**Original ACMG Summary:** The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.

**VCEP Specifications:** Use a proband point-based scoring system. Unrelated probands are to be used and may be aggregated across all three phenotype categories. If there is a pedigree with a choice of probands with VHL disease, choose the proband that most closely matches Danish Criteria.

#### PS4 Proband Scoring (Unrelated Probands)

| Phenotype Category | Points per Proband |
|--------------------|--------------------|
| **Danish Criteria** (highly specific; panel not required unless only RCC+Pheo) | 1 point |
| **Consistent but not highly specific** (e.g., Pheochromocytoma only, VHL 2C, panel testing negative) | 0.5 points |
| **Nonspecific / Unspecified** (e.g., VHL cohort without detailed phenotype; RCC+Pheo without panel) | 0.25 points |

**Note:** When a case with RCC+Pheo does not have a panel, they are scored as "Nonspecific" (0.25 points).

#### PS4 Evidence Strength Thresholds

| Points | Strength Level |
|--------|----------------|
| 1 | PS4_Supporting |
| 2–4 | PS4_Moderate |
| 5–15 | PS4 (Strong) |
| 16+ | PS4_VeryStrong |

**Example:** For variant A: 2 probands meet Danish Criteria (2 × 1 pt = 2) + 2 probands display Pheochromocytoma only (2 × 0.5 pt = 1) + 4 probands defined as VHL probands but lack further criteria (4 × 0.25 pt = 1) = 4 total points → PS4_Moderate.

---

### PM1 - Mutational Hot Spot

**Original ACMG Summary:** Located in a mutational hot spot and/or critical and well-established functional domain (e.g., active site of an enzyme) without benign variation.

**VCEP Specifications:** PM1 can be used for: (1) known germline mutational hotspots, (2) somatic hotspots from cancerhotspots.org where there is not already a germline mutational hotspot (per Walsh et al. 2018 and cancerhotspots.org v2), and (3) location in a key functional domain if a residue is not a germline or somatic hotspot.

| Strength | Criteria |
|----------|----------|
| **Moderate** | Putative missense variants at known germline hotspots AND/OR in key functional domains AND/OR somatic variants with ≥10 instances for the same AA in cancerhotspots.org |
| **Supporting** | Putative missense variants seen in somatic databases with <10 instances for the same AA in cancerhotspots.org |

#### Germline and Somatic Hotspot Residues

| Hotspots | Type | References |
|----------|------|------------|
| R167, C162, L178, Y98, N78, P86 | Germline | Stebbins et al. (PMID:10205047) |
| 65, 76, 78, 80, 86, 88, 96, 98, 112, 117, 161, 162, 167, 170, 176 | Germline | Chiorean et al. 2022 (PMID:35475554) |
| S65, S68, V74, ~~N78~~, ~~S80~~, ~~P86~~, ~~W88~~, L89, S111, Y112, G114, H115, ~~W117~~, D121, L135, I151, L158, ~~R161~~, ~~C162~~, L169 | Somatic (germline hotspots marked through; use as "germline" not somatic) | cancerhotspots.org & Walsh et al. 2018 (PMIDs: 29247016, 30311369) |

**Key functional domains for PM1:**
- Beta (β) domain: AA 63–155 (Nuclear Export)
- Alpha (α) domain: AA 156–192 (Elongin C binding)
- Second Beta (β) domain: AA 193–204

---

### PM2 - Absent from Controls

**Original ACMG Summary:** Absent from controls (or at extremely low frequency if recessive) in population databases.

**VCEP Specification (Supporting only):**
- PM2_Supporting can be applied for variants either absent from gnomAD or with **≤0.00000156 (0.000156%) GroupMax Filtering Allele Frequency** in gnomAD (based on gnomAD v4 release).
- If no GroupMax Filtering Allele Frequency is calculated (e.g., due to a single variant present), PM2_Supporting may also be applied.
- Follow all SVI general guidance on applying population filters.

---

### PM3 - In Trans with Pathogenic

**Original ACMG Summary:** For recessive disorders, detected in trans with a pathogenic variant.

**VCEP Specifications:** **Not Applicable** — VHL is autosomal dominant.

---

### PM4 - Protein Length Changes

**Original ACMG Summary:** Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Moderate** | In-frame insertions/deletions in the Beta and Alpha domains AND stop-loss variants adding significant additional amino acids to VHL. Functional domains: Beta (β) domain (AA 63–155, Nuclear Export), Alpha (α) domain (AA 156–192, Elongin C binding), Second Beta (β) domain (AA 193–204). |

**Notes:**
- Multiple pathogenic cases and experimental evidence of stop-loss extensions in VHL are associated with Type 2A VHL disease (Sorrell et al. 2011, PMID:20560986).
- PM4 does not apply to in-frame indels prior to codon 54 that do not alter the Met54 VHL p19 codon and beyond.

---

### PM5 - Novel Missense at Same Residue

**Original ACMG Summary:** Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Moderate** | Pathogenicity of prior variant must be established by interpretation of the VHL VCEP or using VHL VCEP specifications. The **Grantham distance** should be used to compare variants — the variant under consideration must have an equal or larger Grantham distance than the classified pathogenic variant (Grantham, 1974, PMID:4843792). Splice metapredictors should be used to ensure the variant is not predicted to have an effect on splicing. |

---

### PM6 - De Novo (Assumed)

**Original ACMG Summary:** Assumed de novo, but without confirmation of paternity and maternity.

**VCEP Specifications:** See PS2 evidence code for scoring and phenotypes. Assumed de novo receives half the points as compared to maternity and paternity confirmed de novo. If paternity and maternity are not confirmed, score using the PM6 code.

PM6 can receive "VeryStrong" strength. For example, if there are >4 de novo probands with Danish Criteria and none have paternity confirmed, this can receive PM6_VeryStrong.

**Note:** The VCI as of Nov 2022 does not allow PM6_VeryStrong. Instead apply the PS2 evidence code and increase the strength to "VeryStrong" with a note that paternity and/or maternity is not confirmed.

See the [PS2/PM6 De Novo Point System](#ps2pm6-de-novo-point-system) above.

---

### PP1 - Co-segregation

**Original ACMG Summary:** Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.

**VCEP Specifications:** Meioses can be counted additively across multiple families. This code may only be applied when the phenotype is highly consistent with VHL (**Danish Criteria** in a family with history of disease).

#### PP1 Meiosis Thresholds

| Strength | Meiosis Count |
|----------|---------------|
| **Supporting (PP1)** | 3–4 meioses across ≥1 family |
| **Moderate (PP1_Moderate)** | 5–6 meioses across ≥1 family |
| **Strong (PP1_Strong)** | >7 meioses across ≥2 families |

---

### PP2 - Missense in Constrained Gene

**Original ACMG Summary:** Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.

**VCEP Specifications:** **Not Applicable.** While there are known pathogenic missense variants in VHL, there is also evidence of benign or common missense variants. gnomAD shows VHL is not intolerant to missense (Z score = -0.39). Missense variants in VHL will need to achieve pathogenic interpretation via other evidence codes.

---

### PP3 - Computational Evidence

**Original ACMG Summary:** Multiple lines of computational evidence support a deleterious effect on the gene or gene product.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Supporting** | For **missense variants**: REVEL score **≥0.664** |
| **Supporting** | For **splice variants**: Concordance of **SpliceAI (>0.5)** AND **VarSeak (class 4 or class 5)** |

**Notes:**
- The SpliceAI score alone can be applied if VarSeak is unable to accept the variant type.
- For canonical splice variants, do not use PP3 if PVS1 is applied.

---

### PP4 - Phenotype Specificity

**Original ACMG Summary:** Patient's phenotype or family history is highly specific for a disease with a single genetic etiology.

**VCEP Specifications:** **Not Applicable.** Combine with PS4 to avoid double counting probands.

---

### PP5 - Reputable Source

**Original ACMG Summary:** Reputable source recently reports variant as pathogenic, but the evidence is not available to the laboratory to perform an independent evaluation.

**VCEP Specifications:** **Not Applicable.** This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PMID:29543229).

---

## Benign Criteria

### BA1 - Allele Frequency >5%

**Original ACMG Summary:** Allele frequency is above 5% in population databases.

**VCEP Specification (Stand Alone):**
- Use a BA1 cut-off of **≥0.000156 (0.0156%) GroupMax Filtering Allele Frequency** in gnomAD (based on gnomAD v4 release).
- Follow all SVI general guidance on applying population filters.

---

### BS1 - Frequency Greater Than Expected

**Original ACMG Summary:** Allele frequency is greater than expected for disorder.

**VCEP Specification (Strong):**
- Use BS1 cut-off of **≥0.0000156 (0.00156%) GroupMax Filtering Allele Frequency** in gnomAD (based on gnomAD v4).
- Follow all SVI general guidance on applying population filters.

---

### BS2 - Observed in Healthy Adult

**Original ACMG Summary:** Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

**VCEP Specifications:** VHL is not highly penetrant at an early age.

| Strength | Criteria |
|----------|----------|
| **Strong** | At least 3 individuals, all ≥65 years old, unaffected, harboring the same variant, with **full phenotyping and screening** for the absence of VHL-related cancers. |
| **Supporting** | At least 3 individuals, all ≥65 years old, unaffected, harboring the same variant, **lacking full phenotyping and screening**, with no noted VHL-related cancers. |

---

### BS3 - Functional Studies (No Effect)

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

**VCEP Specifications (Supporting):**

Evidence of benign effect is demonstrated when:
- **HIF1/2α assay** replicates WT function (HIF1/2α displays degradation) AND/OR
- **VBC complex stability** is not affected AND/OR
- **ECM formation / fibronectin binding** is unaffected

**VHL Type-specific considerations:**
- **VHL Type 1 and 2A/B:** HIF1/2α displays degradation (replicates WT function), VCB-CR E3 ubiquitin ligase complex stability is not affected, and/or ECM formation/fibronectin binding is unaffected.
- **VHL Type 2C:** These variants typically do not affect HIF1/2α; **absence of HIF1/2α alone when testing a suspected VHL Type 2C variant should NOT be used for BS3.** Functional studies of fibronectin and ECM formation are needed for VHL Type 2C.

**Additional notes:**
- This rule can be used and weighted as appropriate for functional tests of variants prior to codon 54 (which show the VHL19 product is not impacted).
- Follow modified SVI guidance for functional assays, general controls, and benign controls.
- For splicing variants (and intronic/synonymous), RNA assays must demonstrate no impact on splicing.

---

### BS4 - Lack of Segregation

**Original ACMG Summary:** Lack of segregation in affected members of a family.

**VCEP Specifications:** For BS4, affected members of the pedigree should fulfill the **Danish Criteria** for VHL. BS4 should not be used if the affected members are only affected with pheochromocytoma (e.g., VHL 2C) and/or Renal Cell Carcinoma alone. Family members should be fully characterized for VHL manifestations to be considered unaffected, and be at least **65 years old** (age at which full penetrance should be reached).

**Examples:**
- Two siblings who both have VHL per Danish Criteria: one has a VHL variant, and the other does not → BS4 could be used.
- Two siblings both fully characterized: one has VHL manifestations, the other is >65 yo without VHL manifestations. If both carry the VHL variant → BS4 could be used.
- If a parent fulfills Danish Criteria but the child is phenotyped and has no manifestations → BS4 **cannot** be used as the child could develop VHL manifestations at a later age.

| Strength | Criteria |
|----------|----------|
| **Strong** | Lack of segregation is seen in affected members of **≥2 families** |
| **Supporting** | Lack of segregation is seen in **1 family** |

---

### BP1-BP7 - Benign Supporting

| Criterion | Status | Specification |
|-----------|--------|---------------|
| **BP1** | Not Applicable | This rule does not apply to VHL, as truncating variants account for only a portion of disease-causing variants. |
| **BP2** | Applicable (Strong and Supporting) | **BP2_Strong:** (i) Variant observed in trans with a known pathogenic variant (phase confirmed), in the absence of congenital polycythemia; OR (ii) observed in the homozygous state in an individual without personal/family history of VHL disease or congenital polycythemia; OR (iii) observed in cis or with unknown phase with ≥3 different pathogenic VHL variants. **BP2_Supporting:** Variant is observed in cis (or phase is unknown) with a pathogenic VHL variant. **Note:** BP2 should not be used in the presence of any clinical or molecular findings of congenital polycythemia. |
| **BP3** | Applicable (Supporting) | BP3 can be applied to the 8× GXEEX AA repeat motif in the 5' end of VHL p30 (AA 14–48). The rest of the coding regions in VHL do not contain repeats (none contain LINE/SINE, low complexity, or other repeat types as identified by RepeatMasker) and BP3 is not applicable to those regions. |
| **BP4** | Applicable (Supporting) | Due to lack of benign variants and the drop in classification accuracy for benign VHL variants, **missense predictors should NOT be used** to assign BP4. BP4 can be applied to assess **lack of splicing impact** with concordance of **SpliceAI (≤0.1)** AND **VarSeak (Class 1 or Class 2)**. The SpliceAI score alone can be applied if VarSeak is unable to accept the variant type. |
| **BP5** | Applicable (Supporting) | BP5 can be applied for ≥2 co-occurrences with pathogenic variants in a different gene that fully explained the patient's phenotype. Requirements: (1) variant in other gene must be considered highly penetrant considering individual's age, tumor type, and gender; (2) patient's personal and family history (including up to 2nd degree relatives) should not overlap with VHL features and tumor histologies. Example: An individual with personal/family history of chromophobic RCC positive for a VHL variant and a pathogenic FLCN variant → BP5 could apply (non-clear cell RCC is not associated with VHL). Counter-example: An individual with pheochromocytoma harboring VHL + pathogenic SDHB → BP5 would NOT apply (pheo is a known VHL risk). |
| **BP6** | Not Applicable | This criterion is not for use as recommended by the ClinGen SVI VCEP Review Committee (PMID:29543229). |
| **BP7** | Applicable (Supporting) | To evaluate splice prediction, use the BP4 code. If BP4 is met for lack of splice effect, BP7 can be applied to silent or intronic variants where the **PhyloP score is ≤0.2**. |

---

## Rules for Combining Criteria

### Pathogenic Classification

| Criteria Combination | Available Codes |
|---------------------|-----------------|
| 1 Very Strong AND ≥1 Strong | VS: PVS1, PS2_VeryStrong, PS4_VeryStrong · S: PS1, PS2, PS4, PP1_Strong |
| 1 Very Strong AND ≥2 Moderate | VS: PVS1, PS2_VeryStrong, PS4_VeryStrong · M: PS2_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate |
| 1 Very Strong AND 1 Moderate AND 1 Supporting | VS + M + Su (see codes below) |
| 1 Very Strong AND ≥2 Supporting | VS + Su: PS2_Supporting, PS3_Supporting, PS4_Supporting, PM1_Supporting, PM2_Supporting, PP1, PP3 |
| ≥2 Strong | S: PS1, PS2, PS4, PP1_Strong |
| 1 Strong AND ≥3 Moderate | S + M: PS2_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate |
| 1 Strong AND 2 Moderate AND ≥2 Supporting | S + 2M + Su |
| 1 Strong AND 1 Moderate AND ≥4 Supporting | S + 1M + 4Su |

### Likely Pathogenic Classification

| Criteria Combination | Available Codes |
|---------------------|-----------------|
| 1 Very Strong AND 1 Moderate | VS + M |
| 1 Strong AND 1 Moderate | S + M |
| 1 Strong AND ≥2 Supporting | S + Su |
| ≥3 Moderate | M: PS2_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate |
| 2 Moderate AND ≥2 Supporting | 2M + Su |
| 1 Moderate AND ≥4 Supporting | 1M + 4Su |
| 1 Strong AND 2 Moderate | S + 2M |

### Benign Classification

| Criteria Combination | Available Codes |
|---------------------|-----------------|
| ≥2 Strong | S: BS1, BS2, BS4, BP2_Strong |
| 1 Stand Alone (BA1) | BA1 |

### Likely Benign Classification

| Criteria Combination | Available Codes |
|---------------------|-----------------|
| 1 Strong AND 1 Supporting | S: BS1, BS2, BS4, BP2_Strong · Su: BS2_Supporting, BS3_Supporting, BS4_Supporting, BP2, BP3, BP4, BP5, BP7 |
| ≥2 Supporting | Su: BS2_Supporting, BS3_Supporting, BS4_Supporting, BP2, BP3, BP4, BP5, BP7 |

---

## Appendices

### Appendix A: PVS1 Decision Tree

```
VHL PVS1 Decision Tree (applies from codon 54 onward)

NONSENSE / FRAMESHIFT
├── Prior to codon 54 → N/A (do not apply)
├── Predicted to undergo NMD (AA 54-136)
│   └── Exon present in biologically relevant transcript(s) → PVS1
└── Not predicted to undergo NMD (AA 137-213)
    ├── Truncated/altered region in critical domain (AA 63-204) → PVS1
    └── Role of region unknown (AA 205-213) → PVS1_Moderate

GT-AG SPLICE (±1,2) — Only from codon 54 onward
├── Exon skipping (all exons critical to VHL) → PVS1
├── Cryptic splice disrupts reading frame, predicted to undergo NMD
│   ├── In critical domain (AA 63-204) or NMD region → PVS1
│   └── Outside critical domain, NMD predicted (AA 55-62) → PVS1_Strong
├── Cryptic splice disrupts reading frame, NOT predicted to undergo NMD
│   ├── In critical domain (AA 63-204) → PVS1
│   └── Role unknown (AA 205-213) → PVS1_Strong
└── Cryptic splice preserves reading frame
    ├── In critical domain (AA 63-204) → PVS1_Strong
    └── Outside critical domain (AA 205-213) or NMD region (AA 55-62) → PVS1_Moderate

DELETION (single exon to full gene)
├── Full gene deletion → PVS1
└── Single to multi exon deletion
    └── Exon present in biologically relevant transcript(s) → PVS1

DUPLICATION (≥1 exon, must be completely contained within gene)
├── Proven in tandem
│   ├── Reading frame disrupted AND NMD predicted (AA 55-136) → PVS1
│   └── No or unknown impact on reading frame and NMD → N/A
├── Presumed in tandem
│   └── Reading frame presumed disrupted AND NMD predicted (AA 55-136) → PVS1_Strong
└── Proven not in tandem → [follow standard guidelines]

INITIATION CODON
└── Met 1 (VHL p30): Different functional transcript (VHL p19) uses
    alternative start codon at Met 54 → N/A
```

### Appendix B: VHL Functional Domains

| Domain | Amino Acid Range | Function |
|--------|-----------------|----------|
| N-terminal region | AA 1–53 | Contains 8× GXEEX repeat motif (AA 14–48); prior to VHL p19 start |
| 1st Beta (β) domain | AA 63–154 | Substrate binding |
| Nuclear Export region | AA 114–155 | Nuclear export function |
| Alpha (α) domain | AA 155–192 | Elongin C binding (AA 157–172) |
| Second Beta (β) domain | AA 193–204 | Structural |
| C-terminal region | AA 205–213 | Minimal functional role; role unknown |

### Appendix C: Population Frequency Thresholds Summary

| Criterion | Threshold | Database | Strength |
|-----------|-----------|----------|----------|
| BA1 | ≥0.000156 (0.0156%) GroupMax FAF | gnomAD v4 | Stand Alone |
| BS1 | ≥0.0000156 (0.00156%) GroupMax FAF | gnomAD v4 | Strong |
| PM2 | ≤0.00000156 (0.000156%) GroupMax FAF or absent | gnomAD v4 | Supporting |

### Appendix D: Danish Criteria for VHL Disease

The Danish Criteria (Binderup et al. 2022, PMID:35709961) provide updated diagnostic criteria for VHL disease. When a patient's phenotype meets Danish Criteria, this is considered "phenotype highly specific for gene" in PS2/PM6 and PS4 scoring. Specific details of tumor types and criteria should be referenced from the published guidelines.

### Appendix E: Computational Predictors Summary

| Predictor | Pathogenic Threshold (PP3) | Benign Threshold (BP4) | Variant Type |
|-----------|---------------------------|------------------------|--------------|
| REVEL | ≥0.664 | Not used for missense | Missense |
| SpliceAI | >0.5 | ≤0.1 | Splice |
| VarSeak | Class 4 or 5 | Class 1 or 2 | Splice |
| PhyloP | — | ≤0.2 (for BP7) | Silent/intronic |

**Note:** For BP4, missense predictors should NOT be used due to lack of benign variants and drop in classification accuracy for benign VHL variants.

### Appendix F: Reference PMIDs

| # | Citation | PMID |
|---|----------|------|
| 1 | Ohh M et al. The von Hippel-Lindau tumor suppressor protein is required for proper assembly of an extracellular fibronectin matrix. Mol Cell (1998) | 9651579 |
| 2 | Clifford SC et al. Contrasting effects on HIF-1alpha regulation by disease-causing pVHL mutations correlate with patterns of tumourigenesis in von Hippel-Lindau disease. Hum Mol Genet (2001) | 11331613 |
| 3 | Kamada M et al. von Hippel-Lindau protein promotes the assembly of actin and vinculin and inhibits cell motility. Cancer Res (2001) | 11358843 |
| 4 | Micale L et al. VHL frameshift mutation as target of nonsense-mediated mRNA decay in Drosophila melanogaster and human HEK293 cell line. J Biomed Biotechnol (2009) | 20145706 |
| 5 | Taylor C et al. Determination of the consequences of VHL mutations on VHL transcripts in renal cell carcinoma. Int J Oncol (2012) | 22825683 |
| 6 | Lenglet M et al. Identification of a new VHL exon and complex splicing alterations in familial erythrocytosis or von Hippel-Lindau disease. Blood (2018) | 29891534 |
| 7 | Buffet A et al. Germline mutations in the new E1' cryptic exon of the VHL gene in patients with tumours of von Hippel-Lindau disease spectrum or with paraganglioma. J Med Genet (2020) | 31996412 |
| 8 | Caravita S et al. Pulmonary arterial hypertension associated with a von Hippel-Lindau gene mutation. J Heart Lung Transplant (2016) | 27578599 |
| 9 | Bartels M et al. Novel Homozygous Mutation of the Internal Translation Initiation Start Site of VHL is Exclusively Associated with Erythrocytosis. Hum Mutat (2015) | 26224408 |
| 10 | Brnich SE et al. Recommendations for application of the functional evidence PS3/BS3 criterion using the ACMG/AMP sequence variant interpretation framework. Genome Med (2019) | 31892348 |
| 11 | Walsh MF et al. Integrating somatic variant data and biomarkers for germline variant classification in cancer predisposition genes. Hum Mutat (2018) | 30311369 |
| 12 | Chang MT et al. Accelerating Discovery of Functional Mutant Alleles in Cancer. Cancer Discov (2018) | 29247016 |
| 13 | Hwang S et al. Germline mutation of Glu70Lys is highly frequent in Korean patients with von Hippel-Lindau (VHL) disease. J Hum Genet (2014) | 25078357 |
| 14 | Hong B et al. Frequent Mutations of VHL Gene and the Clinical Phenotypes in the Largest Chinese Cohort With Von Hippel-Lindau Disease. Front Genet (2019) | 31620170 |
| 15 | Sorrell AD et al. Clinical and functional properties of novel VHL mutation (X214L) consistent with Type 2A phenotype and low risk of renal cell carcinoma. Clin Genet (2011) | 20560986 |
| 16 | Grantham R. Amino acid difference formula to help explain protein evolution. Science (1974) | 4843792 |
| 17 | Bluyssen HA et al. Fibronectin is a hypoxia-independent target of the tumor suppressor VHL. FEBS Lett (2004) | 14706840 |
| 18 | Binderup MLM et al. von Hippel-Lindau disease: Updated guideline for diagnosis and surveillance. Eur J Med Genet (2022) | 35709961 |

---

## Version History

| Version | Date | Notes |
|---------|------|-------|
| 1.1.0 | 1/10/2025 | Clarifications to PM2, BA1, BS1. Updated to gnomAD v4. Changed PM2_Supporting threshold. Disease entity and transcript added. |

---

*This document was compiled from ClinGen VHL VCEP specifications v1.1.0 and ClinGen SVI recommendations. For the most current version, please refer to the ClinGen website.*
