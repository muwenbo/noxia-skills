---
name: noxia-phenotype-inference
description: Phenotype-driven inference of disorders that the sequencing assay structurally cannot detect, for use when a Noxia case returns negative (no convincing causative variant). Reasons from the HPO gestalt to assay-blind mechanisms — CNV, UPD, imprinting/methylation, repeat expansion, deep-intronic, mtDNA — and recommends the right orthogonal confirmatory test. Use when variant analysis is complete and the result is negative/VUS, the user asks "what could WES be missing", "why negative", "phenotype-only", or wants a differential that explains a negative WES despite a suggestive phenotype.
---

# Noxia Phenotype-Only Inference

## Core insight

> **A negative sequencing result does not mean genetics-negative.** It means the answer may lie
> *outside what the assay can see.* WES sequences coding bases — it cannot see missing chromosomal
> segments, parent-of-origin errors, methylation state, or repeat-tract length. When a distinctive
> phenotype perfectly matches a disorder whose usual mechanism is invisible to the assay run, that
> disorder becomes the **most logical remaining explanation** — and the negative is *expected*, not
> reassuring.

This skill produces a **hypothesis that names the right confirmatory test**. It never produces a
finding. There is no variant to classify or mark.

## When this skill applies

Run it **only after** `noxia-variant-analysis` has completed and the honest call is **negative or
VUS** (no convincing causative variant) — and there is a **specific, coherent phenotype** to reason
from. It is not a way to rescue a thin case into a diagnosis.

This skill applies in **two distinct scenarios** — treat them the same way:

1. **Partial molecular clue:** sequencing found a suspicious but inconclusive variant (e.g.
   monoallelic VUS in an AR gene) that points toward a disorder whose second allele may be in a
   WES-blind region. Reason from *both* the variant signal and the phenotype.
2. **Completely clean negative:** sequencing found nothing suspicious at all. Reason from the
   phenotype gestalt **alone** — this is equally valid and equally important. A clean negative with a
   distinctive phenotype is the strongest possible signal that the answer lies in a WES-blind
   mechanism. Do not skip this skill because there is no variant hint.

**Do not run it** when the phenotype is non-specific (e.g. isolated DD with no distinguishing
features). The honest output there is "non-specific phenotype; no targeted orthogonal test indicated
— consider CMA + trio reanalysis as a general next step."

## Workflow

1. **Confirm the negative is real, not a QC artifact.** Re-check `get_case_qc`. A negative caused by
   low coverage is a *false negative* with a different remedy (re-sequence / fill-gap), not an
   assay-blind-mechanism case. State which it is.
2. **Establish the assay.** WES vs WGS vs panel — the blind spots are assay-specific (WGS sees most
   CNVs and deep-intronic; both WES and WGS miss UPD and methylation defects).
3. **Build the gestalt.** Pull the case HPO (`get_case` / `GET /api/cases/{id}/phenotypes`). Identify
   the *distinctive combination* — not single features. Require specific HPO overlap with a recognized
   disorder, per the loose-phenotype-matching guard in
   [noxia-variant-analysis/REFERENCE.md](../noxia-variant-analysis/REFERENCE.md).
4. **Generate top hypotheses — always, regardless of variant findings.** Consult the gestalt →
   suspicion table in [REFERENCE.md](REFERENCE.md) unconditionally:
   - **If sequencing was completely negative (no suspicious variant):** the gestalt table is your
     primary and only tool. Rank all matching rows by phenotypic specificity (how many distinctive
     HPO features match, how uniquely they map to that disorder). Produce the top 1–3 hypotheses
     purely from phenotype. A clean negative with a coherent gestalt is the strongest signal that
     the mechanism is WES-blind — do not produce zero hypotheses just because there is no variant clue.
   - **If there is a partial molecular clue:** use the variant finding to anchor the primary
     hypothesis, then use the gestalt table to surface independent secondary hypotheses that the
     variant does not explain. Both paths must be explored.
   - For each hypothesis: ask *what is the usual molecular mechanism, and could the assay actually
     have seen it?* Only retain it if the mechanism is invisible to the assay. A point-mutation
     disease the assay should have caught is not a valid WES-blind hypothesis.
5. **Name the orthogonal confirmatory test.** Be specific (CMA/SNP-array, MS-MLPA/methylation, repeat
   PCR + Southern, mtDNA sequencing + heteroplasmy, karyotype, MLPA del/dup, RNA-seq, trio for UPD).
   Order tests by: (a) lowest cost / fastest turnaround first, (b) broadest coverage of remaining
   hypotheses (one test that addresses multiple hypotheses is preferred).
6. **Write it as a hypothesis into the report** (see below). State the reasoning chain explicitly:
   phenotype gestalt → expected mechanism → why the assay missed it → confirmatory test.

## Output — route to the AI Analysis Draft, never a finding

This is speculative interpretation. It goes into the report's **AI Analysis Draft** and
`diagnostic_recommendations` — never a Primary Finding, never `mark_variant_for_report`,
never `classify_variant`.

```
mcp__noxia__draft_report_text(case_id=<id>, draft_text="<inference narrative + reasoning chain>")
mcp__noxia__update_report_fields(
  case_id = <id>,
  diagnostic_recommendations = "<numbered: the orthogonal confirmatory test(s), in priority order>"
)
```

Frame every statement as inference requiring orthogonal confirmation. Use "the phenotype is
consistent with…", "warrants methylation testing to confirm/exclude…" — never "the patient has…".

## Guardrails

- **Hypothesis, not diagnosis.** Inference from phenotype + a structurally-expected negative is a
  *pointer to the next test*, not a result. Always state confirmation is required.
- **Always produce hypotheses for a distinctive phenotype.** A completely clean negative with a
  coherent, recognizable gestalt must yield at least one ranked hypothesis. "No variant found
  therefore no hypothesis" is wrong — it confuses assay failure with biological absence. If the
  gestalt matches a WES-blind disorder, name it.
- **Rank by phenotypic specificity, not by variant support.** When sequencing offers no molecular
  clue, rank hypotheses by how many distinctive HPO features match and how uniquely they map to that
  disorder. More specific overlap = higher rank. Partial overlap = lower rank with explicit caveats.
- **Mechanism must match the negative.** Only invoke a disorder if its usual mechanism would actually
  be missed by the assay that was run. A point-mutation disease that WES *should* have caught is not
  explained by "WES missed it."
- **Cap at 1–3 hypotheses.** Do not manufacture candidates beyond what the gestalt supports.
  Breadth without specificity dilutes clinical utility.
- **Age of onset / epidemiology still applies.** Adult-onset common disease is not made monogenic by a
  negative WES.

## Checklist

- [ ] Variant analysis complete; call is genuinely negative/VUS
- [ ] Negative confirmed as real, not a QC/coverage false-negative
- [ ] Assay type established; blind spots scoped to that assay
- [ ] Distinctive HPO gestalt built (specific overlap, not vibe-level)
- [ ] REFERENCE.md gestalt table consulted unconditionally (regardless of whether a suspicious variant exists)
- [ ] **If no suspicious variant:** top 1–3 hypotheses generated from phenotype gestalt alone; zero-hypothesis output rejected
- [ ] **If partial molecular clue:** primary hypothesis anchored to variant; gestalt table consulted for independent secondary hypotheses
- [ ] All hypotheses verified: mechanism is WES-blind (or assay-appropriate blind), not a point-mutation disease the assay should have caught
- [ ] Hypotheses ranked by phenotypic specificity (number + distinctiveness of matching HPO features)
- [ ] Specific orthogonal confirmatory test named per hypothesis, in priority order (cheapest / broadest first)
- [ ] Written into AI Analysis Draft + diagnostic_recommendations as a hypothesis — no finding marked
- [ ] Reasoning chain stated explicitly; confirmation-required framing throughout

---

See [REFERENCE.md](REFERENCE.md) for the assay-blind mechanism → confirmatory-test catalog, the
phenotype-gestalt → suspicion table, and the worked Prader-Willi example.
