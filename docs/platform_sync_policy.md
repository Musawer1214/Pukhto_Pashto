# Platform Sync Policy (GitHub and Hugging Face)

This project is mirrored on two platforms:

- GitHub: `Musawer1214/pashto-language-resources`
- Hugging Face: `Musawer14/pashto-language-resources`

The goal is to keep content equivalent while respecting platform differences.

## Canonical Flow

1. Make and validate changes locally.
2. Push to GitHub `main` first.
3. Sync the resulting content snapshot to Hugging Face `main`.

## Compatibility Rules

- Avoid committing large binary files directly when syncing to Hugging Face.
- Prefer URL-hosted images in docs when possible.
- Keep absolute links pinned to the final slug `pashto-language-resources`.
- Keep one shared `README.md` that is valid on both platforms.

## Shared Markdown Subset (GitHub + Hugging Face)

Use a lowest-common-denominator style in shared docs:

- Standard Markdown headings, bullet lists, links, and fenced code blocks.
- Relative links for internal files whenever possible.
- YAML front matter only where needed (`README.md` for HF metadata, docs pages for Jekyll SEO).
- Avoid GitHub-only HTML widgets and avoid HF-specific custom blocks in shared files.

## Known Platform Differences

- GitHub accepts regular Git binary blobs in many repos.
- Hugging Face may reject binary blobs unless stored with Xet or LFS-compatible flow.
- Hugging Face may warn about missing model-card metadata in README; this is a warning, not a push blocker.

## Tagging Strategy

- Create annotated tags on GitHub release commits.
- If Hugging Face rejects a tag because of blocked binary history, create the same tag name on the HF-safe `hf/main` commit.
- Keep release notes content identical even when commit hashes differ across platforms.

## Safe Update Checklist

1. Run checks:
   - `python scripts/check_links.py`
   - `python scripts/validate_resource_catalog.py`
   - `python -m pytest -q`
2. Confirm slug links:
   - `rg -n "pashto-language-resources" README.md docs pyproject.toml`
3. Push GitHub:
   - `git push origin main`
4. Push Hugging Face:
   - `git push hf <sync-branch>:main`
5. Verify both remotes:
   - `git ls-remote origin refs/heads/main`
   - `git ls-remote hf refs/heads/main`

## Conflict Handling

If GitHub and Hugging Face histories diverge:

- Keep GitHub `main` as canonical source history.
- Sync Hugging Face using a content snapshot commit based on `hf/main`.
- Do not rewrite remote history unless explicitly required.
