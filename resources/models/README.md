# Models

## Pashto-Relevant Models

| Resource | Link | Pashto Evidence | Primary Use |
|---|---|---|---|
| Whisper Large v3 | [Hugging Face - openai/whisper-large-v3](https://huggingface.co/openai/whisper-large-v3) | [Tokenizer map includes `ps`](https://raw.githubusercontent.com/openai/whisper/main/whisper/tokenizer.py) | ASR baseline |
| MMS Coverage Table | [Meta MMS language coverage](https://dl.fbaipublicfiles.com/mms/misc/language_coverage_mms.html) | Includes `pus` with ASR/TTS support | Multilingual transfer |
| MMS 1B All (ASR) | [Hugging Face - facebook/mms-1b-all](https://huggingface.co/facebook/mms-1b-all) | [Coverage table includes `pus` with ASR support](https://dl.fbaipublicfiles.com/mms/misc/language_coverage_mms.html) | Multilingual ASR transfer baseline |
| MMS TTS | [Hugging Face - facebook/mms-tts](https://huggingface.co/facebook/mms-tts) | Aligned with MMS coverage table | TTS baseline |
| NLLB-200 Distilled 600M | [Hugging Face - facebook/nllb-200-distilled-600M](https://huggingface.co/facebook/nllb-200-distilled-600M) | [`special_tokens_map.json` includes `pbt_Arab`](https://huggingface.co/facebook/nllb-200-distilled-600M/blob/main/special_tokens_map.json) | Translation baseline |
| OPUS MT en->mul | [Hugging Face - opus-mt-en-mul](https://huggingface.co/Helsinki-NLP/opus-mt-en-mul) | Model language list includes `pus` | English->Pashto path |
| OPUS MT mul->en | [Hugging Face - opus-mt-mul-en](https://huggingface.co/Helsinki-NLP/opus-mt-mul-en) | Model language list includes `pus` | Pashto->English path |
| PashtoBERT | [Hugging Face - mdarhri/pashto-bert](https://huggingface.co/mdarhri/pashto-bert) | Model card states it is trained on Pashto corpus data | Pashto NLP encoder baseline |

## Integration Paths
- ASR workspace: [../../asr/README.md](../../asr/README.md)
- TTS workspace: [../../tts/README.md](../../tts/README.md)
- Apps workspace: [../../apps/desktop/README.md](../../apps/desktop/README.md)
