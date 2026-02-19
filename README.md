---
license: apache-2.0
language:
- ps
- en
tags:
- pashto
- pukhto
- pushto
- asr
- tts
- nlp
- machine-translation
- language-resources
- low-resource-languages
- speech-recognition
---

# Pashto Language Resources Hub (Pukhto/Pashto)

Open-source Pashto language technology hub for datasets, models, benchmarks, ASR, TTS, NLP, and machine translation.

This repository curates verified Pashto resources and keeps validation and publishing workflows reproducible.

## Quick Links

- Search page: [Pashto Resource Search](https://musawer1214.github.io/pashto-language-resources/search/)
- Project site: [Pashto Language Resources Hub](https://musawer1214.github.io/pashto-language-resources/)
- Documentation hub: [docs/README.md](docs/README.md)
- GitHub: [Musawer1214/pashto-language-resources](https://github.com/Musawer1214/pashto-language-resources)
- Hugging Face mirror: [Musawer14/pashto-language-resources](https://huggingface.co/Musawer14/pashto-language-resources)

## High-Intent Pages

- [Pashto datasets](docs/pashto_datasets.md)
- [Pashto ASR resources](docs/pashto_asr.md)
- [Pashto TTS resources](docs/pashto_tts.md)

## Repository Structure

- `resources/`: verified external resources with structured categories.
- `data/`: normalization seeds, metadata, and data workflows.
- `asr/`: ASR notes, baselines, and references.
- `tts/`: TTS notes, baselines, and references.
- `benchmarks/`: schemas, result templates, and evaluation guidance.
- `experiments/`: reproducible run-card templates.
- `docs/`: SEO, release, platform, and contribution documentation.

## Resource Workflow

1. Discovery job (`.github/workflows/resource_sync.yml`) updates candidate feed.
2. Automation promotes valid non-duplicate candidates into `resources/catalog/resources.json`.
3. Regeneration and validation update derived views and search index.

Core commands:

```bash
python scripts/validate_resource_catalog.py
python scripts/generate_resource_views.py
python scripts/check_links.py
python -m pytest -q
```

## SEO and Discoverability

- SEO playbook: [docs/discoverability_seo.md](docs/discoverability_seo.md)
- GitHub topics checklist: [docs/github_topics_checklist.md](docs/github_topics_checklist.md)
- Backlink strategy: [docs/backlink_strategy.md](docs/backlink_strategy.md)
- Platform sync policy: [docs/platform_sync_policy.md](docs/platform_sync_policy.md)
- Search UI source: [docs/search/index.html](docs/search/index.html)
- Citation metadata: [CITATION.cff](CITATION.cff)

## Releases

- Release notes index: [docs/releases/README.md](docs/releases/README.md)
- Latest release notes: [v1.1.1](docs/releases/v1.1.1.md)
- Changelog: [CHANGELOG.md](CHANGELOG.md)

## Contributing

- Contribution guide: [CONTRIBUTING.md](CONTRIBUTING.md)
- Community communication: [community/COMMUNICATION.md](community/COMMUNICATION.md)
- Resource guidelines: [docs/dataset_guidelines.md](docs/dataset_guidelines.md)

