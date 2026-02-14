# 🗂️ Data Workspace

- [raw/](raw/) incoming source files
- [processed/](processed/) cleaned/aligned artifacts
- [metadata/](metadata/) manifests, speaker/dialect info, QA reports

## ✅ Verified External Datasets

### 🎙️ Common Voice Scripted Speech 24.0 - Pashto
- Link: [Mozilla Data Collective - Common Voice Pashto 24.0](https://datacollective.mozillafoundation.org/datasets/cmj8u3pnb00llnxxbfvxo3b14)
- Why useful: largest open community Pashto speech source for ASR training and evaluation.
- How to use here: download to `data/raw/common_voice_scripted_ps_v24/` and follow [docs/common_voice_pashto_24.md](../docs/common_voice_pashto_24.md).

### 🌸 Google FLEURS (Pashto config)
- Link: [huggingface.co/datasets/google/fleurs](https://huggingface.co/datasets/google/fleurs)
- Pashto validation: [`fleurs.py` includes `"ps_af"`](https://huggingface.co/datasets/google/fleurs/blob/main/fleurs.py).
- Why useful: standardized multilingual speech benchmark split for comparable ASR scores.
- How to use here: treat as external eval set for [benchmarks/](../benchmarks/README.md) and avoid training/eval leakage.

### 📖 OSCAR Corpus (Pashto web text)
- Link: [huggingface.co/datasets/oscar-corpus/oscar](https://huggingface.co/datasets/oscar-corpus/oscar)
- Pashto validation: dataset includes `unshuffled_deduplicated_ps`.
- Why useful: large-scale Pashto text for LM pretraining and lexicon expansion.
- How to use here: normalize and sample into [processed/](processed/) for NLP/ASR language model support.

### 📰 Wikimedia Wikipedia (Pashto dump)
- Link: [huggingface.co/datasets/wikimedia/wikipedia](https://huggingface.co/datasets/wikimedia/wikipedia)
- Pashto validation: subset includes `20231101.ps`.
- Why useful: cleaner encyclopedia-style Pashto text for terminology and style balance.
- How to use here: include as a high-quality text source in normalization and glossary workflows.

### 📘 Belebele (reading-comprehension benchmark)
- Link: [huggingface.co/datasets/facebook/belebele](https://huggingface.co/datasets/facebook/belebele)
- Pashto validation: subset includes `pbt_Arab`.
- Why useful: useful downstream benchmark for comprehension-oriented NLP progress in Pashto.
- How to use here: benchmark multilingual encoders and track improvements in [benchmarks/](../benchmarks/README.md).

## First Contribution (Normalization Starter)
- [processed/normalization_seed_v0.1.tsv](processed/normalization_seed_v0.1.tsv) starter normalization examples
- [docs/pashto_normalization_v0.1.md](../docs/pashto_normalization_v0.1.md) baseline normalization policy
- [scripts/validate_normalization.py](../scripts/validate_normalization.py) basic file validator

## 🧪 Validate Seed File
```bash
python scripts/validate_normalization.py data/processed/normalization_seed_v0.1.tsv
```

## 📝 Notes
- Keep raw downloaded dataset files out of git.
- Track source URL + version in experiment notes for reproducibility.
- Re-check external links before every milestone release.
