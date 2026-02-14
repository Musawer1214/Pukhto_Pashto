# 🔊 TTS Workspace

Place TTS baselines, training configs, and quality-evaluation scripts here.

## ✅ Verified Pashto-Relevant TTS Resources

### 🌐 Meta MMS Coverage (ASR + TTS language support)
- Coverage page: [MMS language coverage](https://dl.fbaipublicfiles.com/mms/misc/language_coverage_mms.html)
- Pashto validation: row includes `pus` with TTS support.
- Use in this repo: multilingual transfer baseline for Pashto synthesis.
- Applications: baseline voice generation, pronunciation checks, accessibility tools.

### 🧪 Meta MMS TTS Model Collection
- Model card: [huggingface.co/facebook/mms-tts](https://huggingface.co/facebook/mms-tts)
- Why useful: broad multilingual TTS package with language-specific checkpoints.
- Use in this repo: evaluate Pashto synthesis quality against curated text prompts.

### 🛠️ Coqui TTS Toolkit
- Repo: [github.com/coqui-ai/TTS](https://github.com/coqui-ai/TTS)
- Why useful: open training/inference toolkit to fine-tune custom Pashto voices.
- Use in this repo: reproducible TTS training scripts and quality A/B experiments.

## 🧩 Integration Hints
- Keep text normalization consistent between ASR and TTS experiments.
- Pair objective metrics with human listening checks in benchmark notes.
- Document voice style, speaker metadata, and license provenance for every release.
