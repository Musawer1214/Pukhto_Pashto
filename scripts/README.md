# ⚙️ Scripts

Automation scripts for data checks and documentation hygiene.

## Available Scripts
- Normalization validator: [validate_normalization.py](validate_normalization.py)
- Markdown link checker: [check_links.py](check_links.py)

## Usage

Validate normalization seed file:
```bash
python scripts/validate_normalization.py data/processed/normalization_seed_v0.1.tsv
```

Check markdown links are clickable-format links:
```bash
python scripts/check_links.py
```

Check markdown links and verify URLs online:
```bash
python scripts/check_links.py --online
```
