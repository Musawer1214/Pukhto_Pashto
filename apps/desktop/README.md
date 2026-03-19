# 🖥️ Desktop Integration

This repo does not currently ship a local desktop app. For now, this folder tracks verified external demo references and the requirements a future local app must meet before it is claimed as shipped.

## ✅ Verified Application Building Blocks

### 🎤 Speech Input: Faster-Whisper
- Repo: [github.com/SYSTRAN/faster-whisper](https://github.com/SYSTRAN/faster-whisper)
- Use in apps: fast offline/near-real-time transcription components.

### 🔈 Speech Output: Coqui TTS
- Repo: [github.com/coqui-ai/TTS](https://github.com/coqui-ai/TTS)
- Use in apps: local speech synthesis modules for Pashto-enabled UX.

### 🌍 Translation Layer: OPUS MT (via multilingual models)
- Models:
  - [huggingface.co/Helsinki-NLP/opus-mt-en-mul](https://huggingface.co/Helsinki-NLP/opus-mt-en-mul)
  - [huggingface.co/Helsinki-NLP/opus-mt-mul-en](https://huggingface.co/Helsinki-NLP/opus-mt-mul-en)
- Pashto validation: language list includes `pus`.
- Use in apps: Pashto↔English assistive translation path for demos.

## ✅ Verified External Demos

- Pashto ASR V3 Space: [ihanif/pashto-asr-v3](https://huggingface.co/spaces/ihanif/pashto-asr-v3)
- Pashto ASR Space: [ihanif/pashto-asr](https://huggingface.co/spaces/ihanif/pashto-asr)
- Pashto Translator Space: [Umar4321/Pashto-Translator](https://huggingface.co/spaces/Umar4321/Pashto-Translator)
- Pashto to English Dictionary Space: [EngrAamirBangash/Pashto2English-Dictionary](https://huggingface.co/spaces/EngrAamirBangash/Pashto2English-Dictionary)

## Requirements Before Shipping Local App Code
1. One reproducible ASR or TTS benchmark artifact is checked into the repo.
2. The app path is documented with exact commands and dependencies.
3. Demo claims in docs and release notes point to committed code, not only external links.
