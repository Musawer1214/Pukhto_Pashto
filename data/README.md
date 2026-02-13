# 🗂️ Data Workspace

- `raw/` incoming source files
- `processed/` cleaned/aligned artifacts
- `metadata/` manifests, speaker/dialect info, QA reports

## First Contribution (Normalization Starter)
- `processed/normalization_seed_v0.1.tsv` starter normalization examples
- `../docs/pashto_normalization_v0.1.md` baseline normalization policy
- `../scripts/validate_normalization.py` basic file validator

## External Source: Mozilla Common Voice (Pashto)
- Dataset: `Common Voice Scripted Speech 24.0 - Pashto`
- Source page:
  `https://datacollective.mozillafoundation.org/datasets/cmj8u3pnb00llnxxbfvxo3b14`
- Local target path: `data/raw/common_voice_scripted_ps_v24/`
- Integration guide: `../docs/common_voice_pashto_24.md`

### Notes
- Keep raw downloaded dataset files out of git.
- Track source URL + version in experiment notes for reproducibility.

## Validate Seed File
```bash
python scripts/validate_normalization.py data/processed/normalization_seed_v0.1.tsv
```
