# Resource Catalog

This folder holds machine-readable resource data used by docs and GitHub Pages search.

## Files
- `resources.json`: canonical Pashto resource catalog (source of truth).
- `pending_candidates.json`: automation output for discovered candidate resources.
- `resource.template.json`: starter template for adding a new resource entry.

## Required workflow
1. Sync candidates: `python scripts/sync_resources.py --limit 20`.
2. Auto-promote valid entries: `python scripts/promote_candidates.py`.
3. Run `python scripts/validate_resource_catalog.py`.
4. Run `python scripts/generate_resource_views.py`.
5. Commit catalog and generated markdown/search files.

## Promotion guardrail
- Auto-promotion accepts only valid non-duplicate entries that pass catalog validation.
- Keep only Pashto-centric resources. Exclude entries where Pashto appears only as a side reference.
- Accept Pashto naming variants (`pashto`, `pukhto`, `pushto`, `pakhto`, `pashto-script`).
