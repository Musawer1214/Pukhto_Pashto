---
name: Release task
about: Track a release checklist from prep to publish
title: "[Release] "
labels: docs
assignees: ''
---

## Target release tag
- [ ] `v0.x`

## Changelog
- [ ] Updated [CHANGELOG.md](../../CHANGELOG.md)

## Validation
- [ ] `python scripts/check_links.py`
- [ ] `python scripts/validate_normalization.py data/processed/normalization_seed_v0.1.tsv`
- [ ] Optional tests: `python -m pytest -q`

## Release notes
- [ ] Added summary for key updates
- [ ] Included known limitations
- [ ] Included benchmark snapshot references

## Publish
- [ ] Pushed to GitHub (`origin`)
- [ ] Pushed to Hugging Face (`hf`)
