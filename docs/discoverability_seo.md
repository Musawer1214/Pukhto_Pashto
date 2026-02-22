# Discoverability and SEO Playbook

This playbook focuses on making the repository easier to find in:

- GitHub search
- Google and Bing search
- Academic and resource discovery channels

## 1) Repository Slug Status

Current and final slug:

- `pashto-language-resources`

Previous slug:

- `Pukhto_Pashto` (legacy slug with underscore)

If slug changes again in future, update:

- `docs/_config.yml` `baseurl`
- Hardcoded URLs in `README.md`, `docs/index.md`, `docs/search/index.html`, and `docs/papers/index.html`

## 2) GitHub About Section (Manual UI)

Set these in repository `Settings -> General` and About panel:

- Description:
  - `Open-source Pashto (Pukhto/Pashto) datasets, ASR, TTS, NLP, MT, models, and benchmark resources.`
- Website:
  - [GitHub Pages home](https://musawer1214.github.io/pashto-language-resources/)
- Topics:
  - `pashto`
  - `pukhto`
  - `pushto`
  - `asr`
  - `tts`
  - `nlp`
  - `machine-translation`
  - `speech-recognition`
  - `language-resources`
  - `low-resource-languages`

## 3) Content Signals

- Keep the first 160 characters of `README.md` keyword clear.
- Use consistent terminology across pages: `Pashto (Pukhto/Pushto)`.
- Publish updates through `CHANGELOG.md` and release notes in `docs/releases/`.
- Keep `CITATION.cff` updated for scholarly reuse and citation.

## 4) Pages SEO and Crawlability

Already included in this repository:

- `docs/_config.yml` with sitemap and SEO plugin support.
- `docs/robots.txt` with sitemap reference.
- Page-level metadata and structured data in `docs/search/index.html`.

Keep these updated when renaming slug or domain.

## 5) External Discovery Boost

- Add the GitHub Pages search URL to:
  - Hugging Face model and dataset cards
  - Relevant community profiles and README links
  - Conference or demo pages for Pashto language technology
- Ask contributors to link specific resource pages in blog posts or papers.

## 6) SEO Operation Assets

- GitHub topics checklist: [github_topics_checklist.md](github_topics_checklist.md)
- Backlink strategy: [backlink_strategy.md](backlink_strategy.md)
- Intent page: [Pashto datasets](pashto_datasets.md)
- Intent page: [Pashto ASR](pashto_asr.md)
- Intent page: [Pashto TTS](pashto_tts.md)
- Release notes index: [releases/README.md](releases/README.md)

## 7) Indexing Checklist (After Push)

1. Push all changes to `main`.
2. Verify GitHub Pages is serving:
   - `/`
   - `/search/`
   - `/papers/`
   - `/robots.txt`
   - `/sitemap.xml`
3. Add site property in Google Search Console.
4. Submit sitemap URL:
   - [Sitemap file](https://musawer1214.github.io/pashto-language-resources/sitemap.xml)
5. Run URL Inspection and request indexing for:
   - Home page
   - Search page
   - Papers page
6. Recheck search visibility after 1 to 3 weeks.
