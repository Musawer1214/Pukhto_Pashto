# 📊 Benchmark Results

Store benchmark outputs in this folder using a stable layout when real runs are ready to publish:

```text
benchmarks/results/
  asr/
    2026-02-14_whisper-large-v3_fleurs-ps-af.json
  tts/
    2026-02-14_mms-tts_prompt-set-v1.json
  nlp/
    2026-02-14_nllb-600m_belebele-pbt-arab.json
```

## Required Format
- Use JSON files matching:
  - [benchmarks/schema/benchmark_result.schema.json](../schema/benchmark_result.schema.json)

## Current Repo Status
- The repo currently ships benchmark schemas and templates.
- No committed benchmark result snapshots are published in this folder yet.
- Do not add placeholder result files; only check in runs backed by a real command, config, and run card.

## Templates
- ASR template: [templates/asr_result.example.json](templates/asr_result.example.json)
- TTS template: [templates/tts_result.example.json](templates/tts_result.example.json)
- NLP template: [templates/nlp_result.example.json](templates/nlp_result.example.json)
