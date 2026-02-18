# Release Notes Draft: v0.1.1

Status: draft  
Target date: TBD

## Summary

v0.1.1 focuses on discoverability improvements and cross-platform consistency between GitHub and Hugging Face.

## Highlights

- Added HF model-card YAML metadata to `README.md`.
- Added SEO operations docs:
  - `docs/github_topics_checklist.md`
  - `docs/backlink_strategy.md`
- Added intent landing pages:
  - `docs/pashto_datasets.md`
  - `docs/pashto_asr.md`
  - `docs/pashto_tts.md`
- Expanded docs hub and index references for new SEO content.

## Validation Checklist

- [ ] `python scripts/check_links.py`
- [ ] `python scripts/validate_resource_catalog.py`
- [ ] `python -m pytest -q`

## Release Commands

```bash
git tag v0.1.1
git push origin v0.1.1
```

## Compare

- GitHub compare: [v0.1...v0.1.1](https://github.com/Musawer1214/pashto-language-resources/compare/v0.1...v0.1.1)

