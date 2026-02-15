# 🧪 Benchmarks

Define fixed test sets, metrics, and leaderboard generation scripts.

## 📦 Result Storage
- Result format guide: [results/README.md](results/README.md)
- JSON schema: [schema/benchmark_result.schema.json](schema/benchmark_result.schema.json)

## ✅ Verified Benchmark Sources

### 🌸 FLEURS (Pashto speech benchmark)
- Dataset: [huggingface.co/datasets/google/fleurs](https://huggingface.co/datasets/google/fleurs)
- Pashto validation: [fleurs.py includes `ps_af`](https://huggingface.co/datasets/google/fleurs/blob/main/fleurs.py).
- Primary use: multilingual ASR benchmark with fixed split conventions.

### 📘 Belebele (Pashto reading benchmark)
- Dataset: [huggingface.co/datasets/facebook/belebele](https://huggingface.co/datasets/facebook/belebele)
- Pashto validation: subset includes `pbt_Arab`.
- Primary use: comprehension benchmark for multilingual NLP models.

### 🌍 FLORES-200 (Pashto translation benchmark)
- Dataset/language list: [facebookresearch/flores/tree/main/flores200](https://github.com/facebookresearch/flores/tree/main/flores200)
- Pashto validation: language list includes `pbt_Arab`.
- Primary use: fixed-reference MT evaluation for Pashto translation experiments.

### 🗣️ Common Voice Pashto v24
- Dataset: [Mozilla Data Collective - Common Voice Pashto 24.0](https://datacollective.mozillafoundation.org/datasets/cmj8u3pnb00llnxxbfvxo3b14)
- Primary use: ASR train/dev/test experiments and project baseline tracking.

## 📏 Recommended Metrics
- ASR: `WER`, `CER`
- TTS: `MCD`/objective proxies + human MOS-style scoring
- NLP: task-specific accuracy/F1 with fixed test set
- MT: `BLEU`, `chrF`, `COMET`

## 🧾 Reporting Template
- Benchmark dataset + version
- Model + checkpoint version
- Normalization policy version
- Metrics and error analysis summary
- Reproducible command/config reference
