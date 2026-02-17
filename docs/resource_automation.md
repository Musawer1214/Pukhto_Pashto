# Resource Automation

This repository uses a semi-automated process to keep Pashto resources current while preserving human review.

## Goals
- Discover new Pashto-relevant resources from trusted public endpoints.
- Keep a machine-readable canonical catalog.
- Prevent unreviewed low-confidence resources from directly entering verified lists.

## Covered source types
- Kaggle datasets
- Hugging Face datasets
- Hugging Face models
- Hugging Face Spaces (projects)
- GitHub repositories (projects and code)
- GitLab repositories (projects and code)
- Zenodo records
- Dataverse datasets
- DataCite DOI records
- Research-paper endpoints (arXiv, Semantic Scholar, OpenAlex, Crossref)

## Files involved
- Canonical verified catalog: [../resources/catalog/resources.json](../resources/catalog/resources.json)
- Candidate feed: [../resources/catalog/pending_candidates.json](../resources/catalog/pending_candidates.json)
- Catalog schema: [../resources/schema/resource.schema.json](../resources/schema/resource.schema.json)
- Search export: [search/resources.json](search/resources.json)

## Scripts
- Validate catalog: `python scripts/validate_resource_catalog.py`
- Generate markdown and search index: `python scripts/generate_resource_views.py`
- Sync new candidates: `python scripts/sync_resources.py --limit 20`
- Full run wrapper: `python scripts/run_resource_cycle.py --limit 25`

## GitHub Actions
- CI (`.github/workflows/ci.yml`) enforces:
  - catalog validation
  - generated file consistency
  - markdown link checks
  - tests
- Resource Sync (`.github/workflows/resource_sync.yml`) runs daily and opens a PR with candidate updates.

## Review flow
1. Inspect candidate entries in `resources/catalog/pending_candidates.json`.
2. Select useful items and move them into `resources/catalog/resources.json`.
3. Set `status` to `verified` only after checking evidence and license.
4. Run:
   - `python scripts/validate_resource_catalog.py`
   - `python scripts/generate_resource_views.py`
5. Commit and open PR.

## Runbook
- Reusable process guide: [resource_cycle_runbook.md](resource_cycle_runbook.md)
