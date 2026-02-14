# 🚀 Release Process

## ⏱️ Cadence
- Monthly milestone release
- Hotfix releases as needed

## ✅ Required for release
- Changelog summary in [../CHANGELOG.md](../CHANGELOG.md)
- Benchmark snapshot in [../benchmarks/results/README.md](../benchmarks/results/README.md) format
- Known limitations section in release notes
- Reproducible commands/scripts
- Link and normalization checks:
  - `python scripts/check_links.py`
  - `python scripts/validate_normalization.py data/processed/normalization_seed_v0.1.tsv`

## 🔖 Versioning
- Use semantic-style tags for major milestones (e.g., `v0.1`, `v0.2`)

## 🧾 Templates
- Release checklist: [release_checklist.md](release_checklist.md)
- Release notes template: [../.github/release_template.md](../.github/release_template.md)
