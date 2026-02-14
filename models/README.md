# 🧠 Models Workspace

This folder defines how local model artifacts and metadata should be organized.

## Folder Layout
- ASR models: [asr/](asr/)
- TTS models: [tts/](tts/)

## Recommended Model Package Structure
- `model_card.md` (required)
- `config.json` or training config reference
- `metrics.json` with benchmark results
- `LICENSE` or explicit upstream license link
- `PROVENANCE.md` with dataset sources and versions

## Release Rules
- Do not upload third-party weights unless the source license allows redistribution.
- Every released checkpoint must include dataset provenance and metric context.
- Keep links to benchmark evidence in [../benchmarks/README.md](../benchmarks/README.md).
