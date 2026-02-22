# 🧰 Scripts

Use these scripts to keep the Pashto resource catalog clean, verified, and searchable.

## 👶 If You Are New, Start Here

Run this safe checklist from repo root:

```bash
python scripts/validate_resource_catalog.py
python scripts/generate_resource_views.py
python scripts/check_links.py
python -m pytest -q
```

## 🧭 Which Script Should I Run?

- `validate_normalization.py`  
  Validate normalization TSV format and rules.
- `check_links.py`  
  Check markdown links for formatting (and optionally live URL reachability).
- `validate_resource_catalog.py`  
  Validate `resources/catalog/resources.json`.
- `generate_resource_views.py`  
  Generate:
  - `resources/*/README.md`
  - `resources/README.md`
  - `docs/search/resources.json` (technical, non-paper)
  - `docs/papers/resources.json` (papers)
- `sync_resources.py`  
  Discover new candidates from public sources into `resources/catalog/pending_candidates.json`.
- `promote_candidates.py`  
  Promote valid, non-duplicate candidates into `resources/catalog/resources.json`.
- `review_existing_resources.py`  
  Audit existing catalog entries and remove stale/low-signal ones with logged reasons.
- `run_resource_cycle.py`  
  Run the full repeatable cycle in one command.

## ▶️ Common Commands

Validate normalization seed:
```bash
python scripts/validate_normalization.py data/processed/normalization_seed_v0.1.tsv
```

Validate catalog:
```bash
python scripts/validate_resource_catalog.py
```

Generate markdown + search payloads:
```bash
python scripts/generate_resource_views.py
```

Discover new candidates:
```bash
python scripts/sync_resources.py --limit 20
```

Review existing resources:
```bash
python scripts/review_existing_resources.py
```

Stricter relevance audit:
```bash
python scripts/review_existing_resources.py --enforce-pashto-relevance
```

Promote candidates:
```bash
python scripts/promote_candidates.py
```

Promote without live URL checks:
```bash
python scripts/promote_candidates.py --skip-url-check
```

Run full cycle:
```bash
python scripts/run_resource_cycle.py --limit 25
```

Discovery-only run:
```bash
python scripts/run_resource_cycle.py --discover-only --limit 25
```

Check links:
```bash
python scripts/check_links.py
```

Check links with online validation:
```bash
python scripts/check_links.py --online
```
