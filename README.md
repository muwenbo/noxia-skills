# noxia-skills

Claude Code skills for clinical genetic analysis and reporting against the [Noxia](https://noxia.ai) rare disease variant analysis platform.

These skills turn Claude Code into a clinical-geneticist agent: pull annotated cases out of Noxia, prioritize variants by clinical criteria, classify them with ACMG, and produce structured reports.

## Prerequisites

- Claude Code with the Noxia MCP server configured (`http://localhost:8000/mcp`)
- A running Noxia instance (dev or production)

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

## Workflow overview

```
noxia-case-management   → create case, upload VCF, annotate, set HPO
noxia-variant-analysis  → QC, candidate scan, shortlist, rank-crosscheck
noxia-reporting         → classify, mark, draft report
```

Or run everything hands-off with **noxia-fast-forward** on a `ready` case.

For negative WES results with a suggestive phenotype, **noxia-phenotype-inference** reasons from the HPO gestalt to assay-blind mechanisms (CNV, UPD, imprinting, repeat expansions, mtDNA) and recommends the right orthogonal test.

## Clinical safety floors (always enforced)

- Never re-annotate (`run_case_bioinformatics_process`) unless the case is not `ready`.
- Never force a non-ideal variant into a Primary Finding.
- VUS and negative results are valid complete reports — no over-calling.
- All MCP-submitted classifications require manual approval in the Noxia web UI.

## License

MIT
