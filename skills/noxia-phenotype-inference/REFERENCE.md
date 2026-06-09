# Phenotype-Only Inference — Reference

## Assay-blind mechanism → confirmatory test catalog

The question for every candidate disorder: **what is its usual molecular mechanism, and could the
assay that was run actually have seen it?** "Sees?" columns are the typical case — capture design,
coverage, and caller all vary.

| Mechanism | WES sees? | WGS sees? | Orthogonal confirmatory test | Example disorders |
|---|---|---|---|---|
| Large CNV / exon-level del-dup | usually ❌ | ✅ | CMA (SNP/aCGH), MLPA del/dup | DMD/BMD del-dup, contiguous-gene syndromes |
| Microdeletion / microduplication syndrome | ❌ | ✅ | CMA | 22q11.2 del, 1p36, 16p11.2, Williams (7q11.23) |
| Aneuploidy / whole-chromosome | ❌ | partial | Karyotype / CMA | Turner (45,X), Klinefelter (47,XXY) |
| **Uniparental disomy (UPD)** — looks fully normal on seq | ❌ | ❌ | SNP array (trio), trio methylation, trio WES | PWS/Angelman (UPD15), Silver-Russell (UPD7), TNDM |
| **Imprinting / methylation defect** | ❌ | ❌ | Methylation analysis: **MS-MLPA**, MS-PCR | Prader-Willi, Angelman, Beckwith-Wiedemann, Silver-Russell |
| **Repeat expansion** | ❌ | partial / unreliable | Targeted PCR + Southern blot / RP-PCR | Fragile X (FMR1), Huntington (HTT), DM1 (DMPK), Friedreich (FXN), SCAs, C9orf72 |
| Deep-intronic / regulatory / promoter | ❌ (outside capture) | ✅ | Targeted Sanger / RNA-seq | deep-intronic ABCA4, CFTR, GAA |
| Mitochondrial DNA variant / heteroplasmy | usually ❌ (nuclear capture) | partial | mtDNA sequencing + heteroplasmy quantitation | MELAS, MERRF, LHON, Leigh |
| Low-level / tissue-specific mosaicism | ❌ at low VAF | ❌ at low VAF | Deep targeted seq, affected-tissue biopsy | PIK3CA-overgrowth, McCune-Albright (GNAS) |
| Balanced translocation / inversion | ❌ | partial | Karyotype / optical genome mapping | position-effect / gene-disrupting rearrangements |
| Pseudogene / segmental-dup region (mismapping) | unreliable | better w/ long-read | Gene-specific assay (e.g. MLPA), long-read | **SMA (SMN1 exon-7 del)**, CYP21A2, PMS2 |

**RNA / functional gap:** even when a candidate variant *is* in coding sequence, a negative call can
reflect a splicing/expression effect that needs RNA-seq or functional assay to demonstrate — flag
this when a strong phenotype points at one gene but the DNA call is VUS.

## Phenotype gestalt → suspicion table

Distinctive *combinations* — not single features. Use as a prompt to consider the assay-blind
mechanism, then verify specific HPO overlap before asserting.

| Gestalt | Suspect | Mechanism (why seq is negative) | First test |
|---|---|---|---|
| Neonatal hypotonia → later hyperphagia/obesity, hypogonadism, short stature, DD | Prader-Willi | imprinting (paternal 15q11-q13 del / matUPD15 / IC defect) | Methylation (MS-MLPA) |
| Happy/excitable demeanor, severe speech deficit, ataxia, seizures, DD | Angelman | imprinting (maternal 15q11-q13 / patUPD15 / UBE3A) | Methylation (MS-MLPA) |
| Hemihypertrophy, macroglossia, omphalocele, neonatal hyperinsulinism, organomegaly | Beckwith-Wiedemann | 11p15 methylation / UPD | Methylation (11p15) |
| IUGR, relative macrocephaly, body asymmetry, feeding difficulty, 5th-finger clinodactyly | Silver-Russell | 11p15 hypomethylation / matUPD7 | Methylation + UPD7 |
| Male: macroorchidism, DD/autism, long face, large ears, joint laxity | Fragile X | FMR1 CGG repeat expansion | FMR1 repeat PCR/Southern |
| Progressive ataxia, areflexia, cardiomyopathy, scoliosis, diabetes | Friedreich ataxia | FXN GAA expansion | FXN repeat assay |
| Adult progressive chorea, psychiatric change, dominant family history | Huntington | HTT CAG expansion | HTT repeat assay |
| Myotonia, distal weakness, cataracts, frontal balding, cardiac conduction defect | Myotonic dystrophy 1 | DMPK CTG expansion | DMPK repeat assay |
| Lactic acidosis, stroke-like episodes, sensorineural HL, maternal inheritance | Mitochondrial (MELAS) | mtDNA point variant / heteroplasmy | mtDNA sequencing |
| Infant: symmetric proximal weakness, areflexia, tongue fasciculation | SMA | SMN1 exon-7 homozygous deletion (pseudogene region) | SMN1/SMN2 MLPA |
| Multiple congenital anomalies + DD without a unifying coding hit | submicroscopic CNV / contiguous-gene | sub-resolution deletion/duplication | CMA |

## Worked example — Prader-Willi inferred *because* WES was negative

**Clinical clues:** DD + ID, short stature + microcephaly, **bilateral cryptorchidism + hypoplastic
genitalia** (striking), brain extra-axial space widening, pulmonary hypoplasia, multiple congenital
anomalies. No single feature is diagnostic, but **hypotonia-like DD + hypogonadism + short stature in
a young male** is a classic PWS triad.

**Why WES was negative — by design:**

| PWS mechanism | Frequency | Detectable by WES? |
|---|---|---|
| Paternal 15q11-q13 deletion | ~70% | ❌ usually missed (CNV) |
| Paternal UPD | ~25% | ❌ completely invisible (sequence is all present — wrong *parent*) |
| Imprinting-center defect | ~5% | ⚠️ rarely |

WES sequences genes but cannot detect missing segments or parent-of-origin errors. UPD looks normal
on WES because all the sequence is there — the problem is *whose* DNA it is, not what it says.

**Reasoning chain:**

```
Multisystem anomalies
   ↓  WES negative → rules out most single-gene disorders
Remaining candidates must involve chromosomal architecture or epigenetics
   ↓  hypogonadism + DD + short stature = classic PWS
PWS = imprinting defect, NOT a point mutation
   ↓  WES is the wrong tool — the negative is expected
→ Confirm with CMA + methylation testing
```

**The core insight:** PWS was inferred *precisely because* WES was negative. A point-mutation disease
would have shown up. The negative result, combined with a phenotype matching an imprinting disorder,
made PWS the most logical remaining explanation — to be confirmed by methylation analysis, never
asserted as a finding from sequencing data alone.
