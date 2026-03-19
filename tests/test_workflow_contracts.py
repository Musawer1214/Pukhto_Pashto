from pathlib import Path

from scripts.generate_resource_views import CATEGORY_CONFIG, PAPERS_SEARCH_OUTPUT, TECHNICAL_SEARCH_OUTPUT


def test_resource_sync_workflow_tracks_generated_outputs() -> None:
    workflow = (
        Path(__file__).resolve().parents[1]
        / ".github"
        / "workflows"
        / "resource_sync.yml"
    ).read_text(encoding="utf-8")

    expected_paths = {"resources/README.md", TECHNICAL_SEARCH_OUTPUT.as_posix(), PAPERS_SEARCH_OUTPUT.as_posix()}
    expected_paths.update(Path(path).as_posix() for path, _title in CATEGORY_CONFIG.values())

    for expected in expected_paths:
        assert expected in workflow


def test_ci_runs_repo_contract_validation() -> None:
    workflow = (
        Path(__file__).resolve().parents[1]
        / ".github"
        / "workflows"
        / "ci.yml"
    ).read_text(encoding="utf-8")

    assert "python scripts/validate_repo_contracts.py --require-jsonschema" in workflow
