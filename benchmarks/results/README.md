# 📊 Benchmark Results

Store benchmark outputs in this folder using a stable layout:

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

## Templates
- ASR template: [templates/asr_result.example.json](templates/asr_result.example.json)
- TTS template: [templates/tts_result.example.json](templates/tts_result.example.json)
- NLP template: [templates/nlp_result.example.json](templates/nlp_result.example.json)
