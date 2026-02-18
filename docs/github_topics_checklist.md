# GitHub Topics Checklist

Use this checklist to keep repository topics aligned with search intent and discoverability.

## Recommended Topics

- pashto
- pukhto
- pushto
- asr
- tts
- nlp
- machine-translation
- speech-recognition
- language-resources
- low-resource-languages
- multilingual
- dataset-curation

## Manual Update Steps

1. Open repository home page.
2. In the right `About` panel, click the gear icon.
3. Add or update topics.
4. Save changes.

## Monthly Audit Checklist

- [ ] Topics match project scope (ASR, TTS, NLP, MT, resources).
- [ ] Synonyms are present (pashto, pukhto, pushto).
- [ ] No stale or misleading topics remain.
- [ ] README keywords and topics are still consistent.
- [ ] GitHub Pages home and search links are present in About website/docs.

## Validation Commands

```bash
rg -n "pashto|pukhto|pushto|asr|tts|nlp|machine-translation" README.md docs
```

## Related Docs

- [Discoverability and SEO](discoverability_seo.md)
- [Backlink strategy](backlink_strategy.md)
- [Platform sync policy](platform_sync_policy.md)
