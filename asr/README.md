# 🎙️ ASR Workspace

This workspace tracks ASR baseline candidates and evaluation planning. It does not yet ship a committed local ASR evaluation script or benchmark result snapshot.

## ✅ Verified Pashto-Relevant ASR Models

### 🧠 OpenAI Whisper Large v3
- Model: [huggingface.co/openai/whisper-large-v3](https://huggingface.co/openai/whisper-large-v3)
- Pashto validation: [OpenAI Whisper tokenizer map includes `"ps": "pashto"`](https://raw.githubusercontent.com/openai/whisper/main/whisper/tokenizer.py).
- Use in this repo: strong baseline and pseudo-labeling engine for bootstrapping.
- Applications: transcription, subtitle generation, dataset pre-labeling.

### 🌐 Meta MMS Coverage (ASR + TTS language support)
- Coverage page: [MMS language coverage](https://dl.fbaipublicfiles.com/mms/misc/language_coverage_mms.html)
- Pashto validation: row includes `pus` with ASR and TTS support.
- Use in this repo: multilingual transfer baseline when Pashto data is limited.
- Applications: low-resource ASR transfer experiments.

## ⚙️ Verified Inference Tooling

### 🚀 Faster-Whisper
- Repo: [github.com/SYSTRAN/faster-whisper](https://github.com/SYSTRAN/faster-whisper)
- Why useful: optimized Whisper inference for faster experimentation.
- Use in this repo: local transcription pipelines and benchmark generation speedups.

## 🧩 Integration Hints
- Keep all model/eval runs reproducible with command logs and commit hashes.
- Store evaluation outputs under [benchmarks/](../benchmarks/README.md) with model/version labels.
- Track WER/CER with dataset split and normalization policy references.

## Current Repo Status
- Shipped today: verified external ASR references, search/catalog indexing, benchmark schema, run-card templates
- Not shipped yet: checked-in local ASR eval command, config, and benchmark result JSON
- Next artifact expected here: one reproducible run card plus one matching benchmark result entry
