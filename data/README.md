# 🗂️ Data Workspace

- `raw/` incoming source files
- `processed/` cleaned/aligned artifacts
- `metadata/` manifests, speaker/dialect info, QA reports

## First Contribution (Normalization Starter)
- `processed/normalization_seed_v0.1.tsv` starter normalization examples
- `../docs/pashto_normalization_v0.1.md` baseline normalization policy
- `../scripts/validate_normalization.py` basic file validator

## Validate Seed File
```bash
python scripts/validate_normalization.py data/processed/normalization_seed_v0.1.tsv
```
