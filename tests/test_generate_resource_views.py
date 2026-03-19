import json

from scripts.generate_resource_views import _write_text_file, main


def _catalog() -> dict:
    return {
        "version": "1.0.0",
        "updated_on": "2026-03-10",
        "resources": [
            {
                "id": "dataset-verified",
                "title": "Pashto Verified Dataset",
                "url": "https://example.org/pashto-dataset",
                "category": "dataset",
                "source": "other",
                "status": "verified",
                "summary": "Verified Pashto dataset for generator coverage.",
                "primary_use": "Testing",
                "tasks": ["asr"],
                "pashto_evidence": {
                    "evidence_text": "Explicit Pashto support is listed.",
                    "evidence_url": "https://example.org/pashto-dataset",
                    "markers": ["Pashto"],
                },
                "tags": ["pashto", "dataset"],
            },
            {
                "id": "dataset-candidate",
                "title": "Pashto Candidate Dataset",
                "url": "https://example.org/pashto-candidate",
                "category": "dataset",
                "source": "other",
                "status": "candidate",
                "summary": "Candidate Pashto dataset that should stay out of public search.",
                "primary_use": "Testing",
                "tasks": ["asr"],
                "pashto_evidence": {
                    "evidence_text": "Explicit Pashto support is listed.",
                    "evidence_url": "https://example.org/pashto-candidate",
                    "markers": ["Pashto"],
                },
                "tags": ["pashto", "dataset"],
            },
            {
                "id": "paper-verified",
                "title": "Pashto Verified Paper",
                "url": "https://example.org/pashto-paper",
                "category": "paper",
                "source": "other",
                "status": "verified",
                "summary": "Verified Pashto paper for search payload partition coverage.",
                "primary_use": "Testing",
                "tasks": ["nlp"],
                "pashto_evidence": {
                    "evidence_text": "Paper title contains Pashto.",
                    "evidence_url": "https://example.org/pashto-paper",
                    "markers": ["Pashto"],
                },
                "tags": ["pashto", "paper"],
            },
            {
                "id": "paper-candidate",
                "title": "Pashto Candidate Paper",
                "url": "https://example.org/pashto-paper-candidate",
                "category": "paper",
                "source": "other",
                "status": "candidate",
                "summary": "Candidate Pashto paper that should stay out of public search.",
                "primary_use": "Testing",
                "tasks": ["nlp"],
                "pashto_evidence": {
                    "evidence_text": "Paper title contains Pashto.",
                    "evidence_url": "https://example.org/pashto-paper-candidate",
                    "markers": ["Pashto"],
                },
                "tags": ["pashto", "paper"],
            },
        ],
    }


def test_generate_resource_views_uses_verified_resources_and_lf_line_endings(
    monkeypatch,
    tmp_path,
) -> None:
    catalog_path = tmp_path / "resources" / "catalog" / "resources.json"
    catalog_path.parent.mkdir(parents=True)
    catalog_path.write_text(json.dumps(_catalog(), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    monkeypatch.chdir(tmp_path)

    assert main() == 0

    technical_payload = json.loads((tmp_path / "docs" / "search" / "resources.json").read_text(encoding="utf-8"))
    papers_payload = json.loads((tmp_path / "docs" / "papers" / "resources.json").read_text(encoding="utf-8"))

    assert technical_payload["count"] == 1
    assert [item["id"] for item in technical_payload["resources"]] == ["dataset-verified"]
    assert technical_payload["resources"][0]["review_state"] == "verified"
    assert technical_payload["resources"][0]["signal_origin"] == "direct"
    assert technical_payload["resources"][0]["direct_pashto_signal"] is True
    assert technical_payload["resources"][0]["quality_flags"] == []
    assert papers_payload["count"] == 1
    assert [item["id"] for item in papers_payload["resources"]] == ["paper-verified"]

    assert b"\r\n" not in (tmp_path / "resources" / "README.md").read_bytes()
    assert b"\r\n" not in (tmp_path / "resources" / "papers" / "README.md").read_bytes()


def test_write_text_file_skips_unchanged_content(tmp_path) -> None:
    path = tmp_path / "sample.txt"
    assert _write_text_file(path, "same\n") is True
    assert _write_text_file(path, "same\n") is False
