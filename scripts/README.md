# Scripts

Automation scripts for quality checks, resource catalog validation, and search index generation.

## Available scripts
- `validate_normalization.py`: validate normalization seed TSV format and rules.
- `check_links.py`: ensure markdown links are clickable (optional online reachability check).
- `validate_resource_catalog.py`: validate `resources/catalog/resources.json`.
- `generate_resource_views.py`: generate `resources/*/README.md`, `resources/README.md`, and `docs/search/resources.json` from the catalog.
- `sync_resources.py`: collect new candidate Pashto resources from Kaggle, Hugging Face (datasets/models/spaces), GitHub repositories, and paper endpoints into `resources/catalog/pending_candidates.json`.
- `run_resource_cycle.py`: run the full repeatable resource cycle with one command.

## Usage

Validate normalization seed file:
```bash
python scripts/validate_normalization.py data/processed/normalization_seed_v0.1.tsv
```

Validate resource catalog:
```bash
python scripts/validate_resource_catalog.py
```

Generate markdown and search index from catalog:
```bash
python scripts/generate_resource_views.py
```

Sync candidate resources for maintainer review:
```bash
python scripts/sync_resources.py --limit 20
```

Run full repeatable cycle:
```bash
python scripts/run_resource_cycle.py --limit 25
```

Run discovery only:
```bash
python scripts/run_resource_cycle.py --discover-only --limit 25
```

Check markdown links format:
```bash
python scripts/check_links.py
```

Check markdown links and verify URLs online:
```bash
python scripts/check_links.py --online
```
