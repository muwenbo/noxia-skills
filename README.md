# noxia-skills

Claude Code skills for clinical genetic analysis and reporting against the [Noxia](https://noxia.ai) rare disease variant analysis platform.

These skills turn Claude Code into a clinical-geneticist agent: pull annotated cases out of Noxia, prioritize variants by clinical criteria, classify them with ACMG, and produce structured reports.

## Prerequisites

- Claude Code with the Noxia MCP server configured (`http://localhost:8000/mcp`)
- A running Noxia instance (dev or production)
- Python 3.7+ with `requests` and `beautifulsoup4` (required by **noxia-variant-classifier** only):
  ```bash
  pip install requests beautifulsoup4
  ```

## Installation

### Quick install (recommended)

```bash
npx skills add muwenbo/noxia-skills
```

### Register as a Claude Code plugin marketplace

```bash
/plugin marketplace add muwenbo/noxia-skills
```

Then browse and install via `/plugin > Discover`, or install directly:

```bash
/plugin install noxia-skills@noxia-skills
```

## Skills

| Skill | Description |
|---|---|
| **noxia-case-management** | Create cases, upload VCFs, trigger annotation, set HPO terms |
| **noxia-variant-analysis** | QC review, phenotype-driven candidate scan, ACMG opportunistic classification |
| **noxia-reporting** | Classify variants, mark for report, draft all report fields |
| **noxia-fast-forward** | End-to-end unattended analysis + reporting in one pass |
| **noxia-phenotype-inference** | Phenotype-driven inference of WES-blind disorders (negative/VUS cases) |
| **noxia-variant-classifier** | Deep ACMG/VCEP classification with ClinGen gene-specific guidelines (on-demand) |

## Workflow overview

```
noxia-case-management      → create case, upload VCF, annotate, set HPO
noxia-variant-analysis     → QC, candidate scan, shortlist, rank-crosscheck
noxia-reporting            → classify, mark, draft report
```

Or run everything hands-off with **noxia-fast-forward** on a `ready` case.

For negative WES results with a suggestive phenotype, **noxia-phenotype-inference** reasons from the HPO gestalt to assay-blind mechanisms (CNV, UPD, imprinting, repeat expansions, mtDNA) and recommends the right orthogonal test.

### Deep classification with VCEP guidelines

**noxia-variant-classifier** provides a thorough 28-criterion ACMG/AMP analysis enhanced by ClinGen VCEP (Variant Curation Expert Panel) gene-specific guidelines for 100+ genes. It is **on-demand only** — use it when you need an auditable, guideline-level classification for a specific variant.

```
noxia-variant-analysis  → identify candidate variant
noxia-variant-classifier → deep ACMG/VCEP analysis → classification proposal
noxia-reporting         → user accepts proposal → submit + draft report
```

It chains:
1. **Noxia KB lookup** (`kb_lookup_variant` + `kb_get_gene`) — annotation, gnomAD popmax, SpliceAI delta scores, domain info, PMIDs
2. **VCEP guideline file** — gene-specific criteria modifications (100+ genes bundled)
3. **ClinVar region scan** — finds other P/LP variants at the same codon for PS1/PM5
4. **PubMed/PMC literature** — optional full-text retrieval for case-level evidence (PS2/PS3/PS4/PP1)
5. **Classification proposal** — structured 28-criterion report for user review; no auto-submission

## Clinical safety floors (always enforced)

- Never re-annotate (`run_case_bioinformatics_process`) unless the case is not `ready`.
- Never force a non-ideal variant into a Primary Finding.
- VUS and negative results are valid complete reports — no over-calling.
- All MCP-submitted classifications require manual approval in the Noxia web UI.
- **noxia-variant-classifier** produces a proposal only — the user decides whether to submit.

## License

MIT
