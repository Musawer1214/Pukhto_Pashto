from scripts.audit_resource_pipeline import audit_resource_pipeline


def test_audit_resource_pipeline_reports_expected_quality_signals() -> None:
    catalog = {
        "resources": [
            {
                "id": "candidate-hf-dataset-pashto-live",
                "title": "Pashto Live Dataset",
                "url": "https://example.org/live",
                "category": "dataset",
                "source": "huggingface",
                "status": "verified",
                "summary": "Verified Pashto dataset.",
                "primary_use": "Automated discovery entry for Pashto resource tracking.",
                "tasks": [],
                "pashto_evidence": {
                    "evidence_text": "Contains Pashto in the title.",
                    "evidence_url": "https://example.org/live",
                    "markers": ["Pashto"],
                },
                "tags": ["pashto", "candidate", "dataset"],
            },
            {
                "id": "paper-a",
                "title": "Duplicate Title",
                "url": "https://example.org/paper-a",
                "category": "paper",
                "source": "datacite",
                "status": "verified",
                "summary": "Pashto paper example for duplicate audit.",
                "primary_use": "Testing",
                "tasks": ["nlp"],
                "pashto_evidence": {
                    "evidence_text": "Contains Pashto in the title.",
                    "evidence_url": "https://example.org/paper-a",
                    "markers": ["Pashto"],
                },
                "tags": ["pashto", "paper"],
            },
            {
                "id": "project-a",
                "title": "Duplicate Title",
                "url": "https://example.org/project-a",
                "category": "project",
                "source": "datacite",
                "status": "verified",
                "summary": "Pashto project example for collision audit.",
                "primary_use": "Testing",
                "tasks": [],
                "pashto_evidence": {
                    "evidence_text": "Metadata mentions Pashto support.",
                    "evidence_url": "https://example.org/project-a",
                    "markers": ["metadata"],
                },
                "tags": ["pashto", "project"],
            },
        ]
    }
    pending = {
        "candidates": [
            {
                "id": "candidate-dead",
                "title": "Dead candidate",
                "url": "https://example.org/dead",
            }
        ]
    }
    removal_log = {
        "entries": [
            {"url": "https://example.org/dead"},
            {"url": "https://example.org/dead"},
        ]
    }

    report = audit_resource_pipeline(catalog=catalog, pending_payload=pending, removal_log=removal_log)

    assert len(report["pending_previously_removed"]) == 1
    assert len(report["candidate_like_verified"]) == 1
    assert len(report["metadata_only_verified"]) == 1
    assert len(report["duplicate_title_groups"]) == 1
    assert len(report["datacite_project_collisions"]) == 1
    assert report["repeated_removal_urls"][0]["count"] == 2
