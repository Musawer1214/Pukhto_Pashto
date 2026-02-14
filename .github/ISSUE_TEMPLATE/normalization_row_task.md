---
name: Normalization row task (good first issue)
about: Add new Pashto text-normalization rows to the seed dataset
title: "[Data][Normalization] Add rows for "
labels: data, good first issue
assignees: ''
---

## Goal
Add new high-quality rows to:
- [data/processed/normalization_seed_v0.1.tsv](../../data/processed/normalization_seed_v0.1.tsv)

## What to add
- [ ] 5-20 new rows with unique `id` values
- [ ] `raw_text` and `normalized_text` filled for every row
- [ ] short `note` explaining the normalization change

## Quality checklist
- [ ] no empty fields
- [ ] no duplicate `id`
- [ ] punctuation/spacing normalized consistently
- [ ] meaning preserved (no semantic rewrite)

## Validation
Run:
```bash
python scripts/validate_normalization.py data/processed/normalization_seed_v0.1.tsv
```

Paste result here:
```
# validation output
```

## Acceptance criteria
- [ ] validator passes
- [ ] rows are realistic Pashto examples
- [ ] PR links this issue
