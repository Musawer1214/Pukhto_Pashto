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

# 🌍 Pashto Language Resources Hub (Pukhto/Pashto)

Open-source Pashto language technology hub for **datasets, models, benchmarks, ASR, TTS, NLP, and machine translation**.

This project helps contributors find, verify, and improve Pashto AI resources in one place.

## 👋 New Here? Start in 2 Minutes

1. Search technical resources: [Pashto Resource Search](https://musawer1214.github.io/pashto-language-resources/search/)
2. Search papers/documentation: [Pashto Papers Search](https://musawer1214.github.io/pashto-language-resources/papers/)
3. Read beginner docs: [docs/README.md](docs/README.md)

## 🔗 Quick Links

- Project site: [Pashto Language Resources Hub](https://musawer1214.github.io/pashto-language-resources/)
- GitHub repo: [Musawer1214/pashto-language-resources](https://github.com/Musawer1214/pashto-language-resources)
- Hugging Face mirror: [Musawer14/pashto-language-resources](https://huggingface.co/Musawer14/pashto-language-resources)

## 🎯 Popular Pages

- [Pashto datasets](docs/pashto_datasets.md)
- [Pashto ASR resources](docs/pashto_asr.md)
- [Pashto TTS resources](docs/pashto_tts.md)
- [Verified resource catalog guide](docs/resource_catalog.md)

## 🗂️ Repository Map (Simple)

- `resources/` verified external resources (dataset/model/benchmark/tool/paper/project/code)
- `data/` normalization seeds and dataset workflows
- `asr/` speech recognition notes and baselines
- `tts/` text-to-speech notes and baselines
- `benchmarks/` result schemas and evaluation templates
- `docs/` documentation, SEO, release, and operations guides

## 🔄 How Updates Work

### Automatic (GitHub Actions)
- Daily workflow (`.github/workflows/resource_sync.yml`) discovers candidates.
- Valid non-duplicate entries are promoted into `resources/catalog/resources.json`.
- Search data and README views are regenerated.

### Manual (Maintainers/Contributors)
- Run scripts locally to discover, validate, and regenerate outputs.

```bash
python -m venv .venv
. .venv/bin/activate
pip install -e ".[dev]"
python scripts/validate_resource_catalog.py
python scripts/generate_resource_views.py
python scripts/validate_repo_contracts.py --require-jsonschema
python scripts/audit_resource_pipeline.py
python scripts/check_links.py
python -m pytest -q
```

## Local Setup

Use one supported local setup path from repo root:

```bash
python -m venv .venv
. .venv/bin/activate
pip install --upgrade pip
pip install -e ".[dev]"
```

Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

## 🚀 Contributing

- Contribution guide: [CONTRIBUTING.md](CONTRIBUTING.md)
- Community communication: [community/COMMUNICATION.md](community/COMMUNICATION.md)
- Resource guidelines: [docs/dataset_guidelines.md](docs/dataset_guidelines.md)

## 📈 SEO and Discoverability

- SEO playbook: [docs/discoverability_seo.md](docs/discoverability_seo.md)
- GitHub topics checklist: [docs/github_topics_checklist.md](docs/github_topics_checklist.md)
- Backlink strategy: [docs/backlink_strategy.md](docs/backlink_strategy.md)
- Platform sync policy: [docs/platform_sync_policy.md](docs/platform_sync_policy.md)
- Search UI source: [docs/search/index.html](docs/search/index.html)
- Papers UI source: [docs/papers/index.html](docs/papers/index.html)
- Citation metadata: [CITATION.cff](CITATION.cff)

## 🧾 Releases

- Release notes index: [docs/releases/README.md](docs/releases/README.md)
- Latest release notes: [v1.2.1](docs/releases/v1.2.1.md)
- Changelog: [CHANGELOG.md](CHANGELOG.md)
