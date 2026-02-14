# Common Voice Scripted Speech 24.0 - Pashto Integration Guide

This project recognizes Mozilla Common Voice as a major source for Pashto ASR
progress and community participation.

## Dataset
- Name: Common Voice Scripted Speech 24.0 - Pashto
- Dataset page: [Mozilla Data Collective - Common Voice Pashto 24.0](https://datacollective.mozillafoundation.org/datasets/cmj8u3pnb00llnxxbfvxo3b14)
- Release date: `2025-12-05`
- Format: `MP3` with TSV metadata
- Approximate size: `49.98 GB`
- License: `CC0-1.0`

## Important Usage Rules
- Do not attempt to identify speakers.
- Do not re-host or re-share the raw dataset files.
- Keep provenance and version information when reporting experiments.

## How To Use In This Repository
1. Download from the official Mozilla Data Collective page.
2. Extract locally under:
   `data/raw/common_voice_scripted_ps_v24/`
3. Keep raw audio out of git.
4. Use project scripts/docs for normalization, splits, and benchmarking.

Recommended local structure:
```text
data/raw/common_voice_scripted_ps_v24/
  clips/
  train.tsv
  dev.tsv
  test.tsv
```

## How To Contribute Through Mozilla Common Voice
Contributors can directly improve Pashto resources on Common Voice:
- Speak: [commonvoice.mozilla.org/ps/speak](https://commonvoice.mozilla.org/ps/speak)
- Write: [commonvoice.mozilla.org/ps/write](https://commonvoice.mozilla.org/ps/write)
- Listen: [commonvoice.mozilla.org/ps/listen](https://commonvoice.mozilla.org/ps/listen)
- Review: [commonvoice.mozilla.org/ps/review](https://commonvoice.mozilla.org/ps/review)

## Contribution Loop Back To This Project
After contributing on Common Voice, open an issue/PR here and share:
- what task you worked on (speak/write/listen/review),
- what quality gaps you observed,
- what dataset or modeling step should be improved next.

Use issue labels:
- `data`
- `good first issue`
- `help wanted`
