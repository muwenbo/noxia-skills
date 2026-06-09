---
name: noxia-case-management
description: Create, configure, and manage clinical cases in Noxia — covers project selection, case creation, VCF upload, annotation pipeline, HPO assignment, and case updates. Use when creating a new case, uploading a VCF, setting phenotypes, updating case metadata, or doing anything that changes case state before variant analysis begins.
---

# Noxia Case Management

## Scope

Create case → upload VCF → annotate → assign HPO → (optional) update case fields.  
Stop here — variant analysis is a separate step.

---

## Step 0 — Confirm identity and org

```
mcp__noxia__whoami
```

Note the username, org name, and org ID from the response. All subsequent steps must target this same org.

No REST session is needed for the standard workflow — VCF upload now uses a short-lived `upload_token` returned by `prepare_file_upload` (Step 3). Only open a REST session if you need to call REST-only endpoints not covered by MCP tools.

---

## Step 1 — Select a project

**Always call `list_projects` first. Confirm the project with the user before creating.**

```
mcp__noxia__list_projects
```

Project selection matters: cases inherit the org, permissions, and pipeline config from their project. Using the wrong project routes the case to the wrong team and may hide it from the relevant users. If the user hasn't specified a project, show the list and ask.

---

## Step 2 — Create the case

Before creating, inspect the VCF header to get the exact sample column name(s):

```bash
gzip -cd /path/to/CASE_ID.hg38.vcf.gz | grep "^#CHROM"
# → #CHROM  POS  ID  REF  ALT  QUAL  FILTER  INFO  FORMAT  <sample_id>
```

`gzip` is standard on macOS and Linux; no bioinformatics tools required.

Then create the case — the `case_id` is returned directly in the response:

```
mcp__noxia__create_case(
  name        = "<case_id>",
  project_id  = <confirmed above>,
  patients    = [{
    name               : "<name>",
    relation           : "proband",
    affected           : true,
    sex                : "male" | "female",
    date_of_birth      : "YYYY-MM-DD",
    medical_record_number: "<MRN or case ID>",
    vcf_sample_id      : "<exact sample column header from VCF>",
    phenotype_text     : "<brief phenotype summary>"
  }],
  phenotype_description: "<full clinical narrative>"
)
```

Do **not** attach VCFs via the `vcfs` parameter — upload via MCP in Step 3.  
For trios/duos add extra patients with `relation: "mother" | "father" | "sibling"`; set `affected: true` only for affected individuals.

---

## Step 3 — Upload VCF (MCP + tus)

Get the file size first, then call `prepare_file_upload`:

```bash
ls -l /path/to/CASE_ID.hg38.vcf.gz   # note size_bytes
```

```
mcp__noxia__prepare_file_upload(
  case_id    = <id from Step 2>,
  filename   = "CASE_ID.hg38.vcf.gz",
  filetype   = "vcf",
  size_bytes = <exact byte count>
)
```

The response includes a short-lived `upload_token` (expires ~24 h) and `upload_url`. Upload with a single tus PATCH:

```bash
curl -sS -X PATCH "<upload_url>" \
  -H "Authorization: Bearer <upload_token>" \
  -H "Tus-Resumable: 1.0.0" \
  -H "Content-Type: application/offset+octet-stream" \
  -H "Upload-Offset: 0" \
  --data-binary "@/path/to/CASE_ID.hg38.vcf.gz" \
  -w "\nHTTP %{http_code}"
```

**HTTP 204 = success.** If interrupted, HEAD the `upload_url` with the same Bearer token to read the current `Upload-Offset`, then resume PATCHing from there.

> **Pitfall:** Each `prepare_file_upload` call creates a new file record. An abandoned call (PATCH never sent) leaves an orphaned record stuck in `uploading` state. If the pipeline later runs, it may fail trying to process the incomplete file. Always confirm `upload_status: completed` via `get_case` before triggering annotation — and avoid calling `prepare_file_upload` more than once per VCF unless resuming a genuinely interrupted transfer.

See [REFERENCE.md](REFERENCE.md) for VCF requirements.

---

## Step 4 — Annotate

**Verify upload is complete before running** — check `get_case` and confirm all files show `upload_status: completed`. Starting the pipeline with an incomplete file causes a `failed` status and requires a full re-run.

```
mcp__noxia__run_case_bioinformatics_process(case_id=<id>)
```

For batch: use `wait=false` and poll `get_case` until `ready_for_review: true`.  
Pipeline order: `qc → vep → acmg + hpo_scoring → prioritization`.  
If no HPO terms are set at annotation time, prioritization is skipped — that's expected.

---

## Step 5 — Set HPO terms

Setting HPO triggers prioritization automatically.

1. Read the full phenotype description; list every positive finding (exclude negated findings).
2. Resolve ambiguous terms with semantic search:
   ```
   mcp__noxia__kb_vector_search_hpo_terms(queries=["<phrase>", ...], k=3, score_threshold=0.5)
   ```
3. Set terms:
   ```
   mcp__noxia__set_case_hpo(case_id=<id>, hpo_ids=["HP:XXXXXXX", ...])
   ```

Verify: `get_case(case_id=<id>)` and check the `hpo_terms` list.

---

## Step 6 — (Optional) Update case fields

```
mcp__noxia__update_case(case_id=<id>, ...)
```

Use to correct metadata (name, phenotype description, patient fields) after creation.

---

## Checklist

- [ ] `whoami` — org confirmed
- [ ] Project listed and confirmed with user before case creation
- [ ] VCF header inspected — `vcf_sample_id` exact match confirmed
- [ ] Case created — `case_id` noted from response
- [ ] `prepare_file_upload` called — `upload_token` and `upload_url` in hand
- [ ] tus PATCH complete — HTTP 204 received
- [ ] `get_case` confirms `upload_status: completed` (no orphaned `uploading` files)
- [ ] Annotation triggered — `run_case_bioinformatics_process`
- [ ] `ready_for_review: true` (no `failed` pipelines)
- [ ] HPO terms set — `set_case_hpo` called
- [ ] HPO terms verified — `get_case` shows correct `hpo_terms` list
- [ ] Prioritization complete

---

See [REFERENCE.md](REFERENCE.md) for VCF requirements and auth troubleshooting.
