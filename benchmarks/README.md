# 🧪 Benchmarks

Define fixed test sets, metrics, and leaderboard generation scripts.

## ✅ Verified Benchmark Sources

### 🌸 FLEURS (Pashto speech benchmark)
- Dataset: `https://huggingface.co/datasets/google/fleurs`
- Pashto validation: `fleurs.py` includes `ps_af`.
- Primary use: multilingual ASR benchmark with fixed split conventions.

### 📘 Belebele (Pashto reading benchmark)
- Dataset: `https://huggingface.co/datasets/facebook/belebele`
- Pashto validation: subset includes `pbt_Arab`.
- Primary use: comprehension benchmark for multilingual NLP models.

### 🗣️ Common Voice Pashto v24
- Dataset: `https://datacollective.mozillafoundation.org/datasets/cmj8u3pnb00llnxxbfvxo3b14`
- Primary use: ASR train/dev/test experiments and project baseline tracking.

## 📏 Recommended Metrics
- ASR: `WER`, `CER`
- TTS: `MCD`/objective proxies + human MOS-style scoring
- NLP: task-specific accuracy/F1 with fixed test set

## 🧾 Reporting Template
- Benchmark dataset + version
- Model + checkpoint version
- Normalization policy version
- Metrics and error analysis summary
- Reproducible command/config reference
