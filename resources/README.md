# Resources

Structured, Pashto-focused resource tracking lives in this folder.

## Sections
- Datasets (11): [datasets/README.md](datasets/README.md)
- Models (9): [models/README.md](models/README.md)
- Benchmarks (4): [benchmarks/README.md](benchmarks/README.md)
- Tools (2): [tools/README.md](tools/README.md)
- Papers (4): [papers/README.md](papers/README.md)

## Machine-Readable Catalog
- Canonical catalog: [catalog/resources.json](catalog/resources.json)
- Candidate feed: [catalog/pending_candidates.json](catalog/pending_candidates.json)
- Schema: [schema/resource.schema.json](schema/resource.schema.json)

## Update Rule
- Add only validated resources with explicit Pashto relevance.
- Keep every external reference clickable using markdown links.
- Run `python scripts/validate_resource_catalog.py` before opening a PR.
- Run `python scripts/generate_resource_views.py` after catalog changes.

Verified resource count: `30`
