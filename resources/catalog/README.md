# Resource Catalog

This folder holds machine-readable resource data used by docs and GitHub Pages search.

## Files
- `resources.json`: canonical Pashto resource catalog (source of truth).
- `pending_candidates.json`: automation output for candidate resources requiring review.
- `resource.template.json`: starter template for adding a new resource entry.

## Required workflow
1. Update `resources.json`.
2. Run `python scripts/validate_resource_catalog.py`.
3. Run `python scripts/generate_resource_views.py`.
4. Commit both catalog and generated markdown/search files.

## Promotion guardrail
- Promote only Pashto-centric resources. Exclude entries where Pashto appears only as a side reference.
- Accept Pashto naming variants during review (`pashto`, `pukhto`, `pushto`, `pakhto`, `پښتو`).
