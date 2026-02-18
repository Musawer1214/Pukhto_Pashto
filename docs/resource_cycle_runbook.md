# Resource Cycle Runbook

Use this runbook whenever you want to repeat the resource update process without re-explaining it.

## Daily automation (already enabled)
- Workflow: [../.github/workflows/resource_sync.yml](../.github/workflows/resource_sync.yml)
- Schedule: every day at 04:00 UTC via GitHub Actions cron.
- Output: updates [../resources/catalog/pending_candidates.json](../resources/catalog/pending_candidates.json) and opens a review PR.

## Manual run (single command)
Run from repository root:

```bash
python scripts/run_resource_cycle.py --limit 25
```

What it executes:
1. `python scripts/sync_resources.py --limit 25`
2. `python scripts/validate_resource_catalog.py`
3. `python scripts/generate_resource_views.py`
4. `python scripts/check_links.py`
5. `python -m pytest -q`

Candidate sources in the sync step include Kaggle datasets, Hugging Face datasets/models/spaces, GitHub repositories, GitLab repositories, Zenodo records, Dataverse datasets, DataCite DOI records, and paper endpoints (arXiv, Semantic Scholar, OpenAlex, Crossref).

## Discovery-only mode
If you only want fresh candidates:

```bash
python scripts/run_resource_cycle.py --discover-only --limit 25
```

## Promotion step (manual review)
After discovery, promote only approved resources:
1. Open [../resources/catalog/pending_candidates.json](../resources/catalog/pending_candidates.json).
2. Copy selected entries into [../resources/catalog/resources.json](../resources/catalog/resources.json).
3. Ensure unique `id` and valid evidence fields.
4. Re-run:
   - `python scripts/run_resource_cycle.py --skip-pytest`
5. Commit and push.

## Guardrails
- Do not auto-promote candidates without evidence and license review.
- Keep `status: verified` only for reviewed entries.
- Do not promote "reference-only" resources where Pashto is incidental; only Pashto-centric resources are eligible.
- Treat spelling variants as valid Pashto markers during review (`pashto`, `pukhto`, `pushto`, `pakhto`, `پښتو`).
- Generated files must be committed after catalog updates.
