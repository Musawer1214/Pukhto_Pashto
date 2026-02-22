# Resource Automation

This repository uses automated discovery and promotion to keep Pashto resources current while preserving validation guardrails.

## Goals
- Discover new Pashto-relevant resources from trusted public endpoints.
- Keep a machine-readable canonical catalog.
- Auto-promote only candidates that pass strict validation and deduplication checks.

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
- Technical search export: [search/resources.json](search/resources.json)
- Papers search export: [papers/resources.json](papers/resources.json)

## Scripts
- Validate catalog: `python scripts/validate_resource_catalog.py`
- Generate markdown and search indexes: `python scripts/generate_resource_views.py`
- Review existing resources for stale/deleted entries: `python scripts/review_existing_resources.py`
- Sync new candidates: `python scripts/sync_resources.py --limit 20`
- Auto-promote valid candidates: `python scripts/promote_candidates.py`
- Full run wrapper: `python scripts/run_resource_cycle.py --limit 25`

## GitHub Actions
- CI (`.github/workflows/ci.yml`) enforces:
  - catalog validation
  - generated file consistency
  - markdown link checks
  - tests
- Resource Sync (`.github/workflows/resource_sync.yml`) runs daily, syncs candidates, auto-promotes valid non-duplicate entries, regenerates views and both search payloads, and opens a PR.
  - Before candidate sync, it reviews existing entries and removes stale/deleted or non-Pashto/low-value entries only with strong logged reasons.

## Promotion flow
1. Review existing resources and remove stale entries with strong reasons.
2. Sync candidates into `resources/catalog/pending_candidates.json`.
3. Auto-promote valid, non-duplicate, URL-available entries into `resources/catalog/resources.json`.
4. Run:
   - `python scripts/validate_resource_catalog.py`
   - `python scripts/generate_resource_views.py`
5. Review PR and merge.

## Runbook
- Reusable process guide: [resource_cycle_runbook.md](resource_cycle_runbook.md)
