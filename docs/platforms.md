# 🌐 Platforms

## 🧭 Primary Platforms
- GitHub: code, issues, pull requests, releases
- Hugging Face Hub: models, datasets, demos
- Community chat (Discord/Matrix): contributor coordination

## 📚 Resource Discovery and Validation
- Use `docs/resource_catalog.md` as the single source of truth for validated external resources.
- Add new links only after checking official pages and explicit Pashto support markers.

## 📣 Publishing Expectations
- Every release links to changelog + benchmark snapshot.
- Every model links to dataset provenance and eval metrics.
- Every new external link must include use-case notes and where it belongs in repo structure.

## 🚀 Dual Publish Checklist (GitHub + Hugging Face)
1. `git status` is clean except intended changes.
2. Docs and resource links updated.
3. Commit created with clear scope.
4. Push to `origin` (GitHub).
5. Push to `hf` (Hugging Face).
6. Verify README render and link health on both platforms.
