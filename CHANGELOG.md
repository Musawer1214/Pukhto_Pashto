# Changelog

All notable changes to this project will be documented in this file.

The format is inspired by [Keep a Changelog](https://keepachangelog.com/en/1.1.0/)
and this project uses semantic version tags with a fixed role per figure:

- `vMAJOR.CODE.RESOURCE`
- `MAJOR`: major project milestones.
- `CODE`: code fixes and implementation updates.
- `RESOURCE`: resource-catalog updates.

## [Unreleased]
### Added
- None yet.

### Changed
- None yet.

### Fixed
- None yet.

## [v1.2.1] - 2026-02-22
### Added
- Added dedicated papers search page and payload:
  - `docs/papers/index.html`
  - `docs/papers/resources.json`
- Added generation-split tests in `tests/test_generate_resource_views.py`.
- Added release notes for this version at `docs/releases/v1.2.1.md`.

### Changed
- Updated `scripts/generate_resource_views.py` to partition outputs by category:
  - non-paper resources -> `docs/search/resources.json`
  - paper resources -> `docs/papers/resources.json`
- Updated `docs/search/index.html` to focus on technical resources and link to the separate papers page.
- Updated `.github/workflows/resource_sync.yml` to include papers search payload in bot PR output paths.
- Updated docs and release pointers for `v1.2.1` and middle-figure code-version progression.
- Bumped package version in `pyproject.toml` from `1.1.1` to `1.2.1`.

### Fixed
- Prevented papers from mixing into the main technical search payload while preserving category-based routing in both manual and automated runs.

## [v1.1.1] - 2026-02-18
### Changed
- Improved search-page readability and usability in `docs/search/index.html`.
- Expanded short task labels into clearer full-form labels in UI controls and resource cards.
- Standardized title casing for key UI labels and actions.
- Documented that daily GitHub Actions bot resource sync updates are released as third-figure resource versions.

### Fixed
- Prevented long resource titles and long unbroken strings from overflowing card boundaries.
- Improved capitalization and display formatting for source and task text in search results.
- Fixed quick-link paths from search page to dataset, ASR, and TTS pages to avoid 404 errors.

## [v1.0.1] - 2026-02-18
### Added
- Promoted 6 high-confidence, non-duplicate Hugging Face resources to verified catalog:
  - `ihanif/pashto_speech_2k`
  - `ihanif/pashto_speech_3k`
  - `koochikoo25/Pashto-Concatenated`
  - `koochikoo25/Whisper-medium-pashto`
  - `afaaaak/urdu_pashto_translator`
  - `DrSaqlainHassan/PashtoTokenixer`

### Changed
- Updated `resources/catalog/resources.json` to version `1.0.1` with `updated_on: 2026-02-18`.
- Regenerated resource indexes and search payload from the updated catalog.
- Refreshed pending candidate feed from full discovery sync.

### Fixed
- Kept only high-confidence Pashto-centric resources in promotion scope for this cycle.

## [v1.0.0] - 2026-02-18
### Added
- Release notes index under `docs/releases/` with `docs/releases/v1.0.0.md`.
- Improved discoverability assets: topics checklist, backlink strategy, and intent landing pages.
- Hugging Face model-card metadata in `README.md`.

### Changed
- Cleaned and restructured README and docs navigation for lower redundancy.
- Modernized `docs/search/index.html` with stronger UI/UX and interaction patterns.
- Standardized release process and checklist around semantic versioning.
- Updated package and citation metadata to `1.0.0`.

### Fixed
- Removed stale draft release-note references from documentation and templates.
- Finalized hardcoded URL usage for the `pashto-language-resources` slug.

## [v0.1] - 2026-02-14
### Added
- Verified external Pashto resource catalog and workspace resource docs.
- Structured `resources/` folder for datasets, models, benchmarks, and tools.
- Link-check script and normalization-validator tests.
- Documentation hub and model/release/process guidance.
