# 🗺️ Roadmap

This roadmap tracks workstreams by shipped status and exit criteria, not aspiration alone.

## Active Now

### Catalog and Automation Hardening
- Status: active
- What is already shipped: verified catalog, candidate intake, review/removal flow, generated README views, GitHub Pages search, CI validation
- Exit criteria:
  - contract checks cover pending candidates, removal log, generated search payloads, and benchmark result files
  - daily sync stops resurfacing known dead links
  - auto-promotion only promotes high-confidence candidates by default

### Docs, Search, and Release Operations
- Status: active
- What is already shipped: contributor docs, release notes, search pages, daily sync PR flow
- Exit criteria:
  - published docs stop linking to repo-only dead ends
  - release task, template, and notes use the same validation checklist
  - public communication endpoints and review ownership are easy to find from the repo

## Next Proof Points

### Benchmarks and Experiments Starter Path
- Status: in preparation
- Required before claiming a benchmark baseline:
  - one checked-in run card under `experiments/`
  - one benchmark result JSON under `benchmarks/results/` that matches the schema
  - exact commands and config references used for that result

### Research Workspace Maturity
- Status: in preparation
- Required before claiming local ASR/TTS baselines:
  - at least one reproducible evaluation path in `asr/` or `tts/`
  - committed config or notebook references
  - release notes that point to the resulting artifacts

## Later, After the Proof Points Exist

### Public Demos and Leaderboard
- Status: later
- Dependency: benchmark starter artifacts and stable baseline runs
- Exit criteria:
  - demo links or app code are checked in and documented
  - leaderboard metrics point to committed result files and run cards

### Community Rotation and Maintenance Depth
- Status: later
- Dependency: stable release ownership and review rotation practice
- Exit criteria:
  - repeatable maintainer handoff process
  - recurring public review threads with documented follow-ups
