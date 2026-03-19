import json
from pathlib import Path

import pytest

from scripts.validate_repo_contracts import validate_repo_contracts


def _schema_path(name: str) -> Path:
    return Path(__file__).resolve().parents[1] / "resources" / "schema" / name


def _pending_payload() -> dict:
    return {
        "generated_on": "2026-03-20T00:00:00Z",
        "sources": ["huggingface-datasets"],
        "candidate_count": 1,
        "candidates": [
            {
                "id": "candidate-hf-dataset-pashto-live",
                "title": "Pashto Live Dataset",
                "url": "https://example.org/live",
                "category": "dataset",
                "source": "huggingface",
                "status": "candidate",
                "summary": "Candidate Pashto dataset for contract testing.",
                "primary_use": "Needs maintainer review before promotion to verified catalog.",
                "tasks": ["asr"],
                "pashto_evidence": {
                    "evidence_text": "Contains Pashto in the title.",
                    "evidence_url": "https://example.org/live",
                    "markers": ["Pashto"],
                },
                "tags": ["pashto", "candidate", "dataset"],
            }
        ],
    }


def _removal_log() -> dict:
    return {
        "updated_on": "2026-03-20",
        "entries": [
            {
                "removed_on": "2026-03-19T00:00:00Z",
                "id": "candidate-kaggle-dead",
                "title": "Dead Dataset",
                "url": "https://example.org/dead",
                "reasons": ["URL returned hard-missing HTTP status 404."],
                "evidence": {
                    "status_code": 404,
                    "final_url": "https://example.org/dead",
                    "metadata_pashto": True,
                    "direct_pashto": True,
                    "page_pashto": False,
                    "signal_origin": "direct",
                },
            }
        ],
    }


def _search_payload() -> dict:
    return {
        "generated_on": "2026-03-20T00:00:00Z",
        "count": 1,
        "resources": [
            {
                "id": "dataset-live",
                "title": "Pashto Live Dataset",
                "url": "https://example.org/live",
                "category": "dataset",
                "source": "huggingface",
                "status": "verified",
                "review_state": "verified",
                "summary": "Verified Pashto dataset for contract testing.",
                "primary_use": "Testing",
                "tasks": ["asr"],
                "tags": ["pashto", "dataset"],
                "evidence_text": "Contains Pashto in the title.",
                "evidence_url": "https://example.org/live",
                "markers": ["Pashto"],
                "signal_origin": "direct",
                "direct_pashto_signal": True,
                "quality_flags": [],
            }
        ],
    }


def test_validate_repo_contracts_passes_for_valid_payloads(tmp_path) -> None:
    pytest.importorskip("jsonschema")
    pending_path = tmp_path / "pending.json"
    removal_path = tmp_path / "removal.json"
    search_path = tmp_path / "search.json"
    papers_path = tmp_path / "papers.json"
    pending_path.write_text(json.dumps(_pending_payload(), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    removal_path.write_text(json.dumps(_removal_log(), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    search_path.write_text(json.dumps(_search_payload(), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    papers_path.write_text(json.dumps(_search_payload(), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    errors = validate_repo_contracts(
        pending_path=pending_path,
        pending_schema=_schema_path("pending_candidates.schema.json"),
        removal_log_path=removal_path,
        removal_log_schema=_schema_path("removal_log.schema.json"),
        technical_search_path=search_path,
        papers_search_path=papers_path,
        search_schema=_schema_path("search_payload.schema.json"),
        benchmark_schema=Path(__file__).resolve().parents[1] / "benchmarks" / "schema" / "benchmark_result.schema.json",
        benchmark_results_root=tmp_path / "benchmark-results",
        require_jsonschema=True,
    )

    assert errors == []


def test_validate_repo_contracts_catches_search_count_mismatch(tmp_path) -> None:
    pytest.importorskip("jsonschema")
    pending_path = tmp_path / "pending.json"
    removal_path = tmp_path / "removal.json"
    search_path = tmp_path / "search.json"
    papers_path = tmp_path / "papers.json"
    payload = _search_payload()
    payload["count"] = 2
    pending_path.write_text(json.dumps(_pending_payload(), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    removal_path.write_text(json.dumps(_removal_log(), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    search_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    papers_path.write_text(json.dumps(_search_payload(), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    errors = validate_repo_contracts(
        pending_path=pending_path,
        pending_schema=_schema_path("pending_candidates.schema.json"),
        removal_log_path=removal_path,
        removal_log_schema=_schema_path("removal_log.schema.json"),
        technical_search_path=search_path,
        papers_search_path=papers_path,
        search_schema=_schema_path("search_payload.schema.json"),
        benchmark_schema=Path(__file__).resolve().parents[1] / "benchmarks" / "schema" / "benchmark_result.schema.json",
        benchmark_results_root=tmp_path / "benchmark-results",
        require_jsonschema=True,
    )

    assert any("payload.count=2 does not match resources length=1" in error for error in errors)
