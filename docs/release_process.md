# Release Process

## Cadence

- Scheduled release: monthly milestone or when a major quality threshold is met.
- Hotfix release: any urgent fixes that should not wait for the next milestone.

## Required for Release

- Changelog summary in [../CHANGELOG.md](../CHANGELOG.md)
- Benchmark snapshot in [../benchmarks/results/README.md](../benchmarks/results/README.md) format
- Known limitations section in release notes
- Reproducible commands or scripts
- Validation checks:
  - `python scripts/check_links.py`
  - `python scripts/validate_normalization.py data/processed/normalization_seed_v0.1.tsv`
  - `python scripts/validate_resource_catalog.py`

## Versioning

- Use semantic version tags: `vMAJOR.MINOR.PATCH`.
- Example: `v1.0.0`, `v1.0.1`, `v1.1.0`, `v2.0.0`.

## Release Notes Location

- Store release notes in [releases/README.md](releases/README.md).
- Add one file per release tag under `docs/releases/`.

## Templates

- Release checklist: [release_checklist.md](release_checklist.md)
- Release template: [../.github/release_template.md](../.github/release_template.md)
