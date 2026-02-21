# Resource Cycle Runbook

Use this runbook whenever you want to repeat the resource update process without re-explaining it.

## Daily automation (already enabled)
- Workflow: [../.github/workflows/resource_sync.yml](../.github/workflows/resource_sync.yml)
- Schedule: every day at 04:00 UTC via GitHub Actions cron.
- Output: reviews existing resources for stale/deleted links and non-Pashto/low-value entries (removing only with strong logged reasons), updates [../resources/catalog/pending_candidates.json](../resources/catalog/pending_candidates.json), auto-promotes valid non-duplicate entries into [../resources/catalog/resources.json](../resources/catalog/resources.json), regenerates views, and opens a review PR.

## Manual run (single command)
Run from repository root:

```bash
python scripts/run_resource_cycle.py --limit 25
```

What it executes:
1. `python scripts/review_existing_resources.py`
2. `python scripts/sync_resources.py --limit 25`
3. `python scripts/promote_candidates.py`
4. `python scripts/validate_resource_catalog.py`
5. `python scripts/generate_resource_views.py`
6. `python scripts/check_links.py`
7. `python -m pytest -q`

Candidate sources in the sync step include Kaggle datasets, Hugging Face datasets/models/spaces, GitHub repositories, GitLab repositories, Zenodo records, Dataverse datasets, DataCite DOI records, and paper endpoints (arXiv, Semantic Scholar, OpenAlex, Crossref).

## Discovery-only mode + manual promotion
If you want fresh candidates without auto-promotion:
1. Run `python scripts/run_resource_cycle.py --discover-only --limit 25`.
2. Review [../resources/catalog/pending_candidates.json](../resources/catalog/pending_candidates.json).
3. Manually move selected entries into [../resources/catalog/resources.json](../resources/catalog/resources.json).
4. Re-run `python scripts/run_resource_cycle.py --skip-pytest`.
5. Commit and push.

## Guardrails
- Auto-promotion accepts only entries that pass dedupe, URL-availability checks, and catalog validation checks.
- Existing resources are auto-removed only for strong reasons (for example confirmed hard-missing links, duplicates, or missing Pashto relevance), with reasons stored in `resources/catalog/removal_log.json`.
- Keep `status: verified` for entries that pass automation checks and repository review.
- Do not promote "reference-only" resources where Pashto is incidental; only Pashto-centric resources are eligible.
- Treat spelling variants as valid Pashto markers during review (`pashto`, `pukhto`, `pushto`, `pakhto`, `pashto-script`).
- Generated files must be committed after catalog updates.

## Versioning for Daily Bot Updates

- Daily candidate-sync updates from GitHub Actions (`resource_sync.yml`) are resource updates.
- When those updates are reviewed and released, increment the third figure in `vMAJOR.CODE.RESOURCE`.
- Example sequence: `v1.1.1` (code fix) -> `v1.1.2` (bot resource release).
