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

Use three-figure tags with fixed meaning:

- `vMAJOR.CODE.RESOURCE`
- `MAJOR`: major milestones and large project-level changes.
- `CODE`: code fixes, implementation changes, and internal patch updates.
- `RESOURCE`: resource-catalog updates after candidate discovery and review.

Examples:

- `v1.0.1`: resource update release.
- `v1.1.1`: code-fix release.
- `v2.0.0`: next major milestone.

Daily bot rule:

- Daily GitHub Actions bot sync updates (`resource_sync.yml`) are resource updates.
- If only bot-driven resource catalog changes are shipped, use the next `vMAJOR.CODE.RESOURCE+1` tag.

## Release Notes Location

- Store release notes in [releases/README.md](releases/README.md).
- Add one file per release tag under `docs/releases/`.

## Templates

- Release checklist: [release_checklist.md](release_checklist.md)
- Release template: [../.github/release_template.md](../.github/release_template.md)
