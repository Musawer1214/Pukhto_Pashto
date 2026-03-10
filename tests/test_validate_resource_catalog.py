import json
from pathlib import Path

import pytest

from scripts.validate_resource_catalog import validate_catalog, validate_catalog_against_schema


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


def _schema() -> dict:
    path = Path(__file__).resolve().parents[1] / "resources" / "schema" / "resource.schema.json"
    return json.loads(path.read_text(encoding="utf-8"))


def test_validate_catalog_passes_for_minimal_valid_catalog() -> None:
    errors = validate_catalog(_minimal_catalog())
    assert errors == []


def test_validate_catalog_against_schema_passes_for_minimal_valid_catalog() -> None:
    pytest.importorskip("jsonschema")
    errors = validate_catalog_against_schema(_schema(), _minimal_catalog())
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


def test_validate_catalog_fails_for_unexpected_top_level_field() -> None:
    catalog = _minimal_catalog()
    catalog["unexpected"] = True
    errors = validate_catalog(catalog)
    assert any("unexpected top-level fields" in error for error in errors)


def test_validate_catalog_fails_for_unexpected_resource_field() -> None:
    catalog = _minimal_catalog()
    catalog["resources"][0]["unexpected"] = "value"
    errors = validate_catalog(catalog)
    assert any("unexpected fields" in error for error in errors)

    pytest.importorskip("jsonschema")
    schema_errors = validate_catalog_against_schema(_schema(), catalog)
    assert any("Additional properties are not allowed" in error for error in schema_errors)


def test_validate_catalog_fails_for_unexpected_evidence_field() -> None:
    catalog = _minimal_catalog()
    catalog["resources"][0]["pashto_evidence"]["unexpected"] = "value"
    errors = validate_catalog(catalog)
    assert any("pashto_evidence has unexpected fields" in error for error in errors)


def test_validate_catalog_fails_for_non_pashto_centric_model() -> None:
    catalog = _minimal_catalog()
    catalog["resources"][0]["category"] = "model"
    catalog["resources"][0]["title"] = "Generic Multilingual Model"
    catalog["resources"][0]["url"] = "https://example.org/model"
    catalog["resources"][0]["pashto_evidence"]["evidence_text"] = "Language support listed in docs."
    catalog["resources"][0]["pashto_evidence"]["evidence_url"] = "https://example.org/model-docs"
    catalog["resources"][0]["pashto_evidence"]["markers"] = ["multilingual"]
    errors = validate_catalog(catalog)
    assert any("must be Pashto-centric" in error for error in errors)


def test_validate_catalog_allows_pashto_centric_model() -> None:
    catalog = _minimal_catalog()
    catalog["resources"][0]["category"] = "model"
    catalog["resources"][0]["title"] = "Pashto ASR Model"
    catalog["resources"][0]["url"] = "https://example.org/pashto-model"
    errors = validate_catalog(catalog)
    assert errors == []


def test_validate_catalog_allows_multilingual_model_with_pashto_evidence() -> None:
    catalog = _minimal_catalog()
    catalog["resources"][0]["category"] = "model"
    catalog["resources"][0]["title"] = "Generic Multilingual Model"
    catalog["resources"][0]["url"] = "https://example.org/model"
    catalog["resources"][0]["pashto_evidence"]["evidence_text"] = "Language table explicitly includes Pashto."
    catalog["resources"][0]["pashto_evidence"]["evidence_url"] = "https://example.org/model/languages"
    catalog["resources"][0]["pashto_evidence"]["markers"] = ["Pashto", "ps"]
    errors = validate_catalog(catalog)
    assert errors == []
