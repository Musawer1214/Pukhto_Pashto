# 📚 Verified Pashto Resource Catalog

Last updated: `2026-02-14`

This catalog lists external resources validated for Pashto relevance and possible integration in this repository.

## ✅ Validation Method
- Confirmed the source URL resolves to the official page.
- Confirmed Pashto support by explicit code/name on the page where available (`ps`, `ps_af`, `pbt_Arab`, `pus`).
- Added only resources with clear practical use for this repo (data, models, benchmarks, apps).

## 🗂️ Datasets

| Resource | Link | Pashto Validation | How to Use Here | Applications |
|---|---|---|---|---|
| Common Voice Scripted Speech 24.0 - Pashto | `https://datacollective.mozillafoundation.org/datasets/cmj8u3pnb00llnxxbfvxo3b14` | Official Pashto dataset page | ASR training/eval under `data/raw/common_voice_scripted_ps_v24/` | ASR, pronunciation analysis, data bootstrapping |
| Google FLEURS | `https://huggingface.co/datasets/google/fleurs` | `fleurs.py` includes `ps_af` | External benchmark split in `benchmarks/` | Multilingual ASR benchmarking |
| OSCAR Corpus | `https://huggingface.co/datasets/oscar-corpus/oscar` | Includes `unshuffled_deduplicated_ps` | Text LM and normalization support in `data/processed/` | NLP pretraining, lexicon growth |
| Wikimedia Wikipedia | `https://huggingface.co/datasets/wikimedia/wikipedia` | Includes `20231101.ps` | High-quality text source and terminology checks | NLP, glossary, language modeling |
| Belebele | `https://huggingface.co/datasets/facebook/belebele` | Includes `pbt_Arab` subset | Comprehension benchmark in `benchmarks/` | Multilingual reading-comprehension eval |

## 🤖 Models

| Resource | Link | Pashto Validation | How to Use Here | Applications |
|---|---|---|---|---|
| Whisper Large v3 | `https://huggingface.co/openai/whisper-large-v3` | Whisper tokenizer language map contains `"ps": "pashto"` | ASR baseline in `asr/` | Transcription, subtitle generation |
| MMS language coverage | `https://dl.fbaipublicfiles.com/mms/misc/language_coverage_mms.html` | Row for `pus` shows ASR/TTS support | Compare multilingual transfer baselines | Low-resource ASR/TTS transfer |
| MMS TTS model collection | `https://huggingface.co/facebook/mms-tts` | Official MMS TTS collection aligned with coverage table | Evaluate multilingual Pashto TTS checkpoints in `tts/` | Speech synthesis and assistive audio |
| NLLB-200 Distilled 600M | `https://huggingface.co/facebook/nllb-200-distilled-600M` | `special_tokens_map.json` contains `pbt_Arab` | Baseline translation experiments under `apps/` and `benchmarks/` | Pashto-centered MT pipelines |
| OPUS MT en→mul | `https://huggingface.co/Helsinki-NLP/opus-mt-en-mul` | Language list includes `pus` | Pashto translation baseline via multilingual target | Translation in demos and tooling |
| OPUS MT mul→en | `https://huggingface.co/Helsinki-NLP/opus-mt-mul-en` | Language list includes `pus` | Reverse translation baseline | Translation and bilingual UX |

## 🧪 Benchmarks and Evaluation

| Resource | Link | Recommended Metric Focus |
|---|---|---|
| FLEURS (speech) | `https://huggingface.co/datasets/google/fleurs` | WER, CER |
| Common Voice Pashto | `https://datacollective.mozillafoundation.org/datasets/cmj8u3pnb00llnxxbfvxo3b14` | WER, CER, error buckets |
| Belebele (reading) | `https://huggingface.co/datasets/facebook/belebele` | Accuracy/F1 |

## 🖥️ Applications and Tooling

| Resource | Link | How to Use Here |
|---|---|---|
| Faster-Whisper | `https://github.com/SYSTRAN/faster-whisper` | Production-style and local ASR inference speedups |
| Coqui TTS | `https://github.com/coqui-ai/TTS` | Train/fine-tune Pashto TTS and run desktop synthesis |

## 📄 Research Anchors (for reading and citation)
- Whisper paper: `https://arxiv.org/abs/2212.04356`
- MMS paper: `https://arxiv.org/abs/2305.13516`
- NLLB paper: `https://arxiv.org/abs/2207.04672`
- FLEURS paper: `https://arxiv.org/abs/2205.12446`

## 🔄 Maintenance Rule
Before each release, re-open each external link and confirm:
- Resource still exists.
- Pashto support marker is unchanged.
- License/usage terms are still compatible with this project.
