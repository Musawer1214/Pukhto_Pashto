from scripts.validate_resource_catalog import validate_catalog


def _minimal_catalog() -> dict:
    return {
        "version": "1.0.0",
        "updated_on": "2026-02-15",
        "resources": [
            {
                "id": "dataset-example",
                "title": "Example Dataset",
                "url": "https://example.org/dataset",
                "category": "dataset",
                "source": "other",
                "status": "verified",
                "summary": "Useful Pashto example dataset for testing the validator.",
                "primary_use": "Testing",
                "pashto_evidence": {
                    "evidence_text": "Mentions Pashto in title.",
                    "evidence_url": "https://example.org/dataset",
                    "markers": ["Pashto"],
                },
                "tags": ["pashto", "test"],
            }
        ],
    }


def test_validate_catalog_passes_for_minimal_valid_catalog() -> None:
    errors = validate_catalog(_minimal_catalog())
    assert errors == []


def test_validate_catalog_fails_for_duplicate_ids() -> None:
    catalog = _minimal_catalog()
    catalog["resources"].append(dict(catalog["resources"][0]))
    errors = validate_catalog(catalog)
    assert any("duplicate resource id" in error for error in errors)


def test_validate_catalog_fails_for_invalid_evidence_url() -> None:
    catalog = _minimal_catalog()
    catalog["resources"][0]["pashto_evidence"]["evidence_url"] = "not-a-url"
    errors = validate_catalog(catalog)
    assert any("evidence_url" in error for error in errors)
