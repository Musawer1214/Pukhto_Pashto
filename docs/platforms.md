# Platforms

## Primary Platforms

- GitHub: code, issues, pull requests, releases, and docs source.
- Hugging Face Hub: models, datasets, and demos.
- Community chat (Discord/Matrix): contributor coordination.

## Resource Discovery and Validation

- Use [docs/resource_catalog.md](resource_catalog.md) as the single source of truth for validated external resources.
- Add new links only after checking official pages and explicit Pashto support markers.

## Publishing Expectations

- Every release links to changelog and benchmark snapshot.
- Every model links to dataset provenance and evaluation metrics.
- Every new external link includes use-case notes and target location in repo structure.
- CI must pass before merging (`.github/workflows/ci.yml`).

## Dual Publish Checklist (GitHub and Hugging Face)

1. `git status` is clean except intended changes.
2. Docs and resource links are updated.
3. Commit message is scoped and explicit.
4. Push to `origin` (GitHub).
5. Push to `hf` (Hugging Face).
6. Verify README render and link health on both platforms.

## Discoverability Checklist

- Keep GitHub About description, topics, and website URL updated.
- Keep [docs/discoverability_seo.md](discoverability_seo.md) current with slug and sitemap URLs.
- Ensure links from Hugging Face cards point to both the repository and search page.

## Operations Guide

- GitHub operations and manual UI tasks: [github_operations.md](github_operations.md)

