# 🖥️ Desktop Integration

Tracks desktop app integration for ASR/TTS/translation pipelines.

## ✅ Verified Application Building Blocks

### 🎤 Speech Input: Faster-Whisper
- Repo: `https://github.com/SYSTRAN/faster-whisper`
- Use in apps: fast offline/near-real-time transcription components.

### 🔈 Speech Output: Coqui TTS
- Repo: `https://github.com/coqui-ai/TTS`
- Use in apps: local speech synthesis modules for Pashto-enabled UX.

### 🌍 Translation Layer: OPUS MT (via multilingual models)
- Models:
  - `https://huggingface.co/Helsinki-NLP/opus-mt-en-mul`
  - `https://huggingface.co/Helsinki-NLP/opus-mt-mul-en`
- Pashto validation: language list includes `pus`.
- Use in apps: Pashto↔English assistive translation path for demos.

## 🧩 Suggested Desktop Pipeline
1. Mic input → ASR transcription
2. Optional translation (Pashto ↔ English)
3. Optional TTS playback in Pashto
4. Save logs for QA and benchmark replay
