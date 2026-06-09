# Case Management — Reference

## VCF requirements

- hg38 coordinates
- bgzipped (`.vcf.gz`) with tabix index (`.vcf.gz.tbi`) in the same directory
- Sample column header must **exactly match** `vcf_sample_id` set in Step 2
- Multi-sample family VCF: upload once; `vcf_type` defaults to `"family"`
- Per-sample VCFs: upload separately per patient with `vcf_type=per_sample`

---

## Auth troubleshooting

MCP and REST are independent sessions. Both must resolve to the same org:

| Check | Command |
|---|---|
| Which user/org is the MCP session? | `mcp__noxia__whoami` |
| Which user/org is the REST session? | `GET /api/auth/me` (with cookie jar) |

If they differ, log the REST session into the correct org before proceeding.

---

## Useful REST endpoints

| Purpose | Endpoint |
|---|---|
| Case header | `GET /api/cases/<id>` |
| Pipeline status | `GET /api/cases/<id>/pipelines` |
| Phenotypes | `GET /api/cases/<id>/phenotypes` |
| List cases in project | `GET /api/projects/<pid>/cases` |
