# 🤝 Contributing

Thanks for helping build open Pashto AI resources.

## 🧩 Ways to Contribute
- Data recording and validation
- Text normalization and terminology fixes
- Model training/evaluation scripts
- Documentation, issue triage, and testing
- External resource discovery and validation

## 🌐 Mozilla Common Voice Path
You can contribute to Pashto data directly on Common Voice and connect it back to this project.

Common Voice Pashto actions:
- Speak: [commonvoice.mozilla.org/ps/speak](https://commonvoice.mozilla.org/ps/speak)
- Write: [commonvoice.mozilla.org/ps/write](https://commonvoice.mozilla.org/ps/write)
- Listen: [commonvoice.mozilla.org/ps/listen](https://commonvoice.mozilla.org/ps/listen)
- Review: [commonvoice.mozilla.org/ps/review](https://commonvoice.mozilla.org/ps/review)

Then contribute here by opening an issue/PR with:
- what you worked on,
- what data quality gap you observed,
- what concrete follow-up is needed in this repository.

## 🔍 External Resource Contribution Rules
- Add or update entries in [resources/catalog/resources.json](resources/catalog/resources.json) using [resources/catalog/resource.template.json](resources/catalog/resource.template.json).
- Validate catalog changes with `python scripts/validate_resource_catalog.py`.
- Regenerate resource docs and search data with `python scripts/generate_resource_views.py`.
- Use [docs/resource_catalog.md](docs/resource_catalog.md) and [docs/resource_automation.md](docs/resource_automation.md) for full rules.
- Prefer official pages and model/dataset cards over third-party reposts.

## 🔄 Contribution Flow
1. Open or pick an issue.
2. Comment your plan.
3. Create a branch and make focused changes.
4. Open a PR with clear summary and testing notes.

## ✅ Standards
- Keep changes small and reviewable.
- Include reproducible steps for data/model changes.
- Document assumptions, limitations, and risks.
- Respect contributors and community guidelines.

## 🏷️ Priority Labels (Recommended)
- `good first issue`
- `data`
- `asr`
- `tts`
- `benchmark`
- `docs`
- `help wanted`
