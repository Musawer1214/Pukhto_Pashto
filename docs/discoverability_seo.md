# Discoverability and SEO Playbook

This playbook focuses on making the repository easier to find in:

- GitHub search
- Google/Bing search
- Academic and resource discovery channels

## 1) Repository Rename Recommendation

Current slug is `pashto-language-resources`.

Previous slug was `Pukhto_Pashto`, which was less search-friendly due to underscore and mixed spelling.

Recommended slug options:

1. `pashto-language-resources`
2. `pashto-ai-resources`
3. `pashto-language-tech`

Selection rule:
- Prefer the name that starts with `pashto` and includes a clear intent word like `resources`.

After rename:
- Update `docs/_config.yml` `baseurl`.
- Update hardcoded URLs in `README.md`, `docs/index.md`, and `docs/search/index.html`.
- Keep old links alive via GitHub redirect behavior, but still update links in-repo.

## 2) GitHub About Section (Manual UI)

Set these in repository `Settings -> General` and About panel:

- Description:
  - `Open-source Pashto (Pukhto/Pashto) datasets, ASR, TTS, NLP, MT, models, and benchmark resources.`
- Website:
  - [GitHub Pages home](https://musawer1214.github.io/pashto-language-resources/) (or new slug after rename)
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
- Publish regular updates in `CHANGELOG.md` and GitHub Releases.
- Keep `CITATION.cff` updated for scholarly reuse and citation.

## 4) Pages SEO and Crawlability

Already included in this repository:

- `docs/_config.yml` with sitemap and SEO plugin support.
- `docs/robots.txt` with sitemap reference.
- Page-level metadata and structured data in `docs/search/index.html`.

Keep these updated when renaming slug or domain.

## 5) External Discovery Boost

- Add the GitHub Pages search URL to:
  - Hugging Face model/dataset cards
  - Relevant community profiles and README links
  - Conference/demo pages for Pashto language technology
- Ask contributors to link specific resource pages in blog posts or papers.

## 6) Indexing Checklist (After Push)

1. Push all changes to `main`.
2. Verify GitHub Pages is serving:
   - `/`
   - `/search/`
   - `/robots.txt`
   - `/sitemap.xml`
3. Add site property in Google Search Console.
4. Submit sitemap URL:
   - [Sitemap file](https://musawer1214.github.io/pashto-language-resources/sitemap.xml)
5. Run URL Inspection and request indexing for:
   - Home page
   - Search page
6. Recheck search visibility after 1 to 3 weeks.

