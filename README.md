# Pashto Language Resources Hub (Pukhto/Pashto)

Open-source repository for Pashto language technology resources: datasets, models, benchmarks, ASR, TTS, NLP, and machine translation (MT).

This project curates verified Pashto resources and maintains reproducible tooling for discovery, validation, and documentation.

## Start Here

- Main resource search: [Pashto Resource Search](https://musawer1214.github.io/pashto-language-resources/search/)
- Project site: [Pashto Language Resources Hub](https://musawer1214.github.io/pashto-language-resources/)
- GitHub repository: [Musawer1214/pashto-language-resources](https://github.com/Musawer1214/pashto-language-resources)
- Hugging Face mirror: [Musawer14/pashto-language-resources](https://huggingface.co/Musawer14/pashto-language-resources)

## If You Searched For

This repository is relevant to these search intents:

- Pashto datasets
- Pashto ASR model
- Pashto TTS resources
- Pashto NLP benchmark
- Pashto machine translation resources
- Pukhto language technology
- Pushto AI resources

## Current Scope

- Build open Pashto datasets, benchmarks, and model references for ASR, TTS, NLP, and MT.
- Track practical tools, apps, and academic papers for Pashto integration in technology.
- Keep everything transparent, reproducible, and contribution-friendly.

## Resource System

Machine-readable and searchable resource pipeline:

- Canonical catalog: [resources/catalog/resources.json](resources/catalog/resources.json)
- Catalog schema: [resources/schema/resource.schema.json](resources/schema/resource.schema.json)
- Candidate feed (auto-generated): [resources/catalog/pending_candidates.json](resources/catalog/pending_candidates.json)
- Search UI source: [docs/search/index.html](docs/search/index.html)
- Search data export: [docs/search/resources.json](docs/search/resources.json)
- Resource index docs: [docs/resource_catalog.md](docs/resource_catalog.md)
- Automation docs: [docs/resource_automation.md](docs/resource_automation.md)
- Cycle runbook: [docs/resource_cycle_runbook.md](docs/resource_cycle_runbook.md)

## How New Resources Are Added

1. Auto discovery runs daily from `.github/workflows/resource_sync.yml` and updates `resources/catalog/pending_candidates.json` in a review PR.
2. Manual review checks quality, Pashto evidence, and license compatibility before promoting entries into `resources/catalog/resources.json` with `status: verified`.
3. Regeneration and validation runs `python scripts/validate_resource_catalog.py` and `python scripts/generate_resource_views.py`, then commits generated updates.

Shortcut wrapper:
- `python scripts/run_resource_cycle.py --limit 25`

## Quickstart

```bash
python -m pip install -e ".[dev]"
python scripts/validate_resource_catalog.py
python scripts/generate_resource_views.py
python scripts/check_links.py
python -m pytest -q
```

## Discoverability And SEO

- Playbook: [docs/discoverability_seo.md](docs/discoverability_seo.md)
- Docs hub: [docs/README.md](docs/README.md)
- Resource search page: [docs/search/index.html](docs/search/index.html)
- Citation metadata: [CITATION.cff](CITATION.cff)
- Platform sync policy: [docs/platform_sync_policy.md](docs/platform_sync_policy.md)

## Documentation Map

- Purpose: [PROJECT_PURPOSE.md](PROJECT_PURPOSE.md)
- Contributing: [CONTRIBUTING.md](CONTRIBUTING.md)
- Roadmap: [ROADMAP.md](ROADMAP.md)
- Governance: [GOVERNANCE.md](GOVERNANCE.md)
- License policy: [LICENSE_POLICY.md](LICENSE_POLICY.md)
- Changelog: [CHANGELOG.md](CHANGELOG.md)
- Community: [community/COMMUNICATION.md](community/COMMUNICATION.md)
- Docs hub: [docs/README.md](docs/README.md)
- Resource index: [docs/resource_catalog.md](docs/resource_catalog.md)
- Resource automation: [docs/resource_automation.md](docs/resource_automation.md)

## Resource Sections

- Datasets: [resources/datasets/README.md](resources/datasets/README.md)
- Models: [resources/models/README.md](resources/models/README.md)
- Benchmarks: [resources/benchmarks/README.md](resources/benchmarks/README.md)
- Tools: [resources/tools/README.md](resources/tools/README.md)
- Papers: [resources/papers/README.md](resources/papers/README.md)
- Projects: [resources/projects/README.md](resources/projects/README.md)
- Code: [resources/codes/README.md](resources/codes/README.md)

## Workspaces

- [data/](data/README.md): datasets, curation, metadata, quality
- [asr/](asr/README.md): ASR baselines and experiments
- [tts/](tts/README.md): TTS baselines and experiments
- [benchmarks/](benchmarks/README.md): benchmark sets and evaluation
- [experiments/](experiments/README.md): reproducible run cards
- [apps/desktop/](apps/desktop/README.md): user-facing integration references
- [models/](models/README.md): model layout and release conventions


