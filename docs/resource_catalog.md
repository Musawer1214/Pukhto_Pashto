# Verified Pashto Resource Catalog

Last updated: `2026-02-15`

This index points to validated Pashto-related resources tracked in structured files.

## Validation method
- Verify source URL resolves to official page or canonical repository.
- Verify explicit Pashto support markers (`Pashto`, `ps`, `ps_af`, `pus`, `pbt_Arab`) where possible.
- Include only resources with practical use for this repository.

## Structured catalog
- Canonical JSON: [../resources/catalog/resources.json](../resources/catalog/resources.json)
- Candidate feed: [../resources/catalog/pending_candidates.json](../resources/catalog/pending_candidates.json)
- JSON schema: [../resources/schema/resource.schema.json](../resources/schema/resource.schema.json)

## Generated markdown views
- Datasets: [../resources/datasets/README.md](../resources/datasets/README.md)
- Models: [../resources/models/README.md](../resources/models/README.md)
- Benchmarks: [../resources/benchmarks/README.md](../resources/benchmarks/README.md)
- Tools: [../resources/tools/README.md](../resources/tools/README.md)
- Papers: [../resources/papers/README.md](../resources/papers/README.md)

## Search page
- GitHub Pages search UI: [search/index.html](search/index.html)
- Search data export: [search/resources.json](search/resources.json)
- Automation guide: [resource_automation.md](resource_automation.md)

## Workspace mapping
- Data workspace: [../data/README.md](../data/README.md)
- ASR workspace: [../asr/README.md](../asr/README.md)
- TTS workspace: [../tts/README.md](../tts/README.md)
- Benchmarks workspace: [../benchmarks/README.md](../benchmarks/README.md)
- Applications workspace: [../apps/desktop/README.md](../apps/desktop/README.md)

## Maintenance rule
Before each release:
- Confirm links still resolve.
- Confirm Pashto support markers remain valid.
- Confirm license or usage terms are still compatible.
- Run:
  - `python scripts/validate_resource_catalog.py`
  - `python scripts/generate_resource_views.py`
