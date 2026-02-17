# Pukhto/Pashto Open Language Project

Community-led open-source project to make Pashto a first-class language in speech and language technology.

## Start Here: Pashto Resource Search

**Main Resource Hub:** [Pashto Resource Search](https://musawer1214.github.io/Pukhto_Pashto/search/)

Use this first to find Pashto datasets, models, projects, code, papers, and tools.

![Pukhto Pashto Repository Banner](Repository_banner_Image.png)

## Project Links
- GitHub Pages (About): [Pukhto_Pashto Site](https://musawer1214.github.io/Pukhto_Pashto/)
- GitHub Pages (Resource Search): [Pashto Resource Search](https://musawer1214.github.io/Pukhto_Pashto/search/)

## Current Scope
- Build open Pashto datasets, benchmarks, and model references for ASR, TTS, NLP, and MT.
- Track practical tools, apps, and academic papers relevant to Pashto integration in technology.
- Keep everything transparent, reproducible, and contribution-friendly.

## Resource System (Current)

This repository now has a machine-readable and searchable resource pipeline:

- Canonical catalog: [resources/catalog/resources.json](resources/catalog/resources.json)
- Catalog schema: [resources/schema/resource.schema.json](resources/schema/resource.schema.json)
- Candidate feed (auto-generated): [resources/catalog/pending_candidates.json](resources/catalog/pending_candidates.json)
- Search UI: [docs/search/index.html](docs/search/index.html)
- Search data export: [docs/search/resources.json](docs/search/resources.json)
- Full index docs: [docs/resource_catalog.md](docs/resource_catalog.md)
- Automation docs: [docs/resource_automation.md](docs/resource_automation.md)
- Repeatable runbook: [docs/resource_cycle_runbook.md](docs/resource_cycle_runbook.md)

## How New Resources Are Added

The process is semi-automatic:

1. Auto discovery:
- Daily GitHub Action runs `.github/workflows/resource_sync.yml`.
- It updates `resources/catalog/pending_candidates.json` and opens a review PR.

2. Manual review and promotion:
- Maintainers inspect candidate quality, Pashto evidence, and license/usage compatibility.
- Approved entries are moved into `resources/catalog/resources.json` with `status: verified`.

3. Regeneration and validation:
- Run `python scripts/validate_resource_catalog.py`
- Run `python scripts/generate_resource_views.py`
- Commit generated updates (`resources/*/README.md` and `docs/search/resources.json`).

Shortcut wrapper:
- Run `python scripts/run_resource_cycle.py --limit 25`

This prevents low-confidence links from being merged directly while still automating discovery.

## Quickstart

```bash
python -m pip install -e ".[dev]"
python scripts/validate_resource_catalog.py
python scripts/generate_resource_views.py
python scripts/check_links.py
python -m pytest -q
```

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
