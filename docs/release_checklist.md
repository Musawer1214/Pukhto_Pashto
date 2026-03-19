# Release Checklist

Use this checklist before tagging a new release.

## Required

- [ ] Update [CHANGELOG.md](../CHANGELOG.md).
- [ ] Add release notes under [releases/README.md](releases/README.md).
- [ ] Assign a release owner and backup reviewer.
- [ ] Run `python scripts/check_links.py`.
- [ ] Run `python scripts/validate_normalization.py data/processed/normalization_seed_v0.1.tsv`.
- [ ] Run `python scripts/validate_resource_catalog.py`.
- [ ] Run `python scripts/validate_repo_contracts.py --require-jsonschema`.
- [ ] Confirm benchmark snapshots are stored in [../benchmarks/results/README.md](../benchmarks/results/README.md) format.
- [ ] Include known limitations in the release notes, or an explicit `N/A`.
- [ ] Confirm docs reflect the release scope.

## Recommended

- [ ] Run tests (`python -m pytest -q`).
- [ ] Re-check key external resource links in [resource_catalog.md](resource_catalog.md).
- [ ] Verify README rendering on GitHub and Hugging Face after push.
- [ ] Verify GitHub and Hugging Face `main` trees are content-equivalent.
- [ ] Push release tag to both platforms.
