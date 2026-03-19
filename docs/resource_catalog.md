# 📦 Verified Pashto Resource Catalog

Catalog freshness is tracked in [resources/catalog/resources.json on GitHub](https://github.com/Musawer1214/pashto-language-resources/blob/main/resources/catalog/resources.json)
via the `updated_on` field.

This page explains how Pashto resources are stored, validated, and published.

## 👀 What Counts as a Valid Resource?

- URL must resolve to the official page or canonical repository.
- Pashto support must be explicit (`Pashto`, `Pukhto`, `Pushto`, `Pakhto`, `ps`, `ps_af`, `pus`, `pbt_Arab`, `پښتو`).
- Resources where Pashto is only a side mention are rejected.
- Multilingual resources are accepted only when `pashto_evidence` is clear and strong.

## 🧱 Structured Data Files

- Canonical JSON: [resources/catalog/resources.json on GitHub](https://github.com/Musawer1214/pashto-language-resources/blob/main/resources/catalog/resources.json)
- Candidate feed: [resources/catalog/pending_candidates.json on GitHub](https://github.com/Musawer1214/pashto-language-resources/blob/main/resources/catalog/pending_candidates.json)
- JSON schema: [resources/schema/resource.schema.json on GitHub](https://github.com/Musawer1214/pashto-language-resources/blob/main/resources/schema/resource.schema.json)
- Contract schemas: [resources/schema/ on GitHub](https://github.com/Musawer1214/pashto-language-resources/tree/main/resources/schema)

## 📚 Generated Resource Views

- Datasets: [../resources/datasets/README.md](../resources/datasets/README.md)
- Models: [../resources/models/README.md](../resources/models/README.md)
- Benchmarks: [../resources/benchmarks/README.md](../resources/benchmarks/README.md)
- Tools: [../resources/tools/README.md](../resources/tools/README.md)
- Papers: [../resources/papers/README.md](../resources/papers/README.md)
- Projects: [../resources/projects/README.md](../resources/projects/README.md)
- Code: [../resources/codes/README.md](../resources/codes/README.md)

## 🔎 Search Pages

- Technical search UI (non-paper): [search/index.html](search/index.html)
- Technical search payload: [search/resources.json](search/resources.json)
- Papers search UI: [papers/index.html](papers/index.html)
- Papers search payload: [papers/resources.json](papers/resources.json)
- Automation guide: [resource_automation.md](resource_automation.md)

## 🗂️ Workspace Mapping

- Data workspace: [data/README.md on GitHub](https://github.com/Musawer1214/pashto-language-resources/blob/main/data/README.md)
- ASR workspace: [asr/README.md on GitHub](https://github.com/Musawer1214/pashto-language-resources/blob/main/asr/README.md)
- TTS workspace: [tts/README.md on GitHub](https://github.com/Musawer1214/pashto-language-resources/blob/main/tts/README.md)
- Benchmarks workspace: [benchmarks/README.md on GitHub](https://github.com/Musawer1214/pashto-language-resources/blob/main/benchmarks/README.md)
- Applications workspace: [apps/desktop/README.md on GitHub](https://github.com/Musawer1214/pashto-language-resources/blob/main/apps/desktop/README.md)

## 🛠️ Maintenance Checklist

Before each release:

- Confirm links still resolve.
- Confirm Pashto support markers are still valid.
- Confirm license/usage terms remain compatible.
- Run:
  - `python scripts/validate_resource_catalog.py`
  - `python scripts/validate_repo_contracts.py --require-jsonschema`
  - `python scripts/generate_resource_views.py`
