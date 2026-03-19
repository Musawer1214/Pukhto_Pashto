---
name: Release task
about: Track a release checklist from prep to publish
title: "[Release] "
labels: docs
assignees: ''
---

## Target release tag
- [ ] `v0.x`

## Ownership
- Release owner: @
- Backup reviewer: @

## Changelog
- [ ] Updated [CHANGELOG.md](../../CHANGELOG.md)

## Validation
- [ ] `python scripts/check_links.py`
- [ ] `python scripts/validate_normalization.py data/processed/normalization_seed_v0.1.tsv`
- [ ] `python scripts/validate_resource_catalog.py`
- [ ] `python scripts/validate_repo_contracts.py --require-jsonschema`
- [ ] Optional tests: `python -m pytest -q`

## Release notes
- [ ] Added summary for key updates
- [ ] Included known limitations (or explicit `N/A`)
- [ ] Included benchmark snapshot references

## Publish
- [ ] Pushed to GitHub (`origin`)
- [ ] Pushed to Hugging Face (`hf`)
