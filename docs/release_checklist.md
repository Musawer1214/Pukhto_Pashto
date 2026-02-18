# Release Checklist

Use this checklist before tagging a new release.

## Required
- [ ] Update [CHANGELOG.md](../CHANGELOG.md).
- [ ] Run `python scripts/check_links.py`.
- [ ] Run `python scripts/validate_normalization.py data/processed/normalization_seed_v0.1.tsv`.
- [ ] Confirm benchmark snapshots are stored in [../benchmarks/results/README.md](../benchmarks/results/README.md) format.
- [ ] Confirm docs reflect the release scope.

## Recommended
- [ ] Run tests (`python -m pytest -q`).
- [ ] Re-check key external resource links in [resource_catalog.md](resource_catalog.md).
- [ ] Verify README rendering on GitHub and Hugging Face after push.

