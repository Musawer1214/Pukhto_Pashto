# 🎙️ ASR Workspace

Place ASR baselines, training configs, and evaluation scripts here.

## ✅ Verified Pashto-Relevant ASR Models

### 🧠 OpenAI Whisper Large v3
- Model: `https://huggingface.co/openai/whisper-large-v3`
- Pashto validation: Whisper tokenizer language map includes `"ps": "pashto"`.
- Use in this repo: strong baseline and pseudo-labeling engine for bootstrapping.
- Applications: transcription, subtitle generation, dataset pre-labeling.

### 🌐 Meta MMS Coverage (ASR + TTS language support)
- Coverage page: `https://dl.fbaipublicfiles.com/mms/misc/language_coverage_mms.html`
- Pashto validation: row includes `pus` with ASR and TTS support.
- Use in this repo: multilingual transfer baseline when Pashto data is limited.
- Applications: low-resource ASR transfer experiments.

## ⚙️ Verified Inference Tooling

### 🚀 Faster-Whisper
- Repo: `https://github.com/SYSTRAN/faster-whisper`
- Why useful: optimized Whisper inference for faster experimentation.
- Use in this repo: local transcription pipelines and benchmark generation speedups.

## 🧩 Integration Hints
- Keep all model/eval runs reproducible with command logs and commit hashes.
- Store evaluation outputs under `benchmarks/` with model/version labels.
- Track WER/CER with dataset split and normalization policy references.
