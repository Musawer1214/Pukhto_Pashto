"""Validate the machine-readable Pashto resource catalog.

Usage:
    python scripts/validate_resource_catalog.py
    python scripts/validate_resource_catalog.py --catalog resources/catalog/resources.json
"""

from __future__ import annotations

import argparse
import json
import re
from datetime import date
from pathlib import Path
from typing import Any
from urllib.parse import urlparse


ALLOWED_CATEGORIES = {"dataset", "model", "benchmark", "tool", "paper"}
ALLOWED_SOURCES = {"huggingface", "mozilla", "kaggle", "github", "arxiv", "meta", "other"}
ALLOWED_STATUS = {"verified", "candidate"}
RESOURCE_ID_RE = re.compile(r"^[a-z0-9][a-z0-9._-]*$")


def _load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _is_valid_http_url(value: str) -> bool:
    parsed = urlparse(value)
    return parsed.scheme in {"http", "https"} and bool(parsed.netloc)


def _validate_iso_date(value: str) -> bool:
    try:
        date.fromisoformat(value)
    except ValueError:
        return False
    return True


def validate_resource(resource: dict[str, Any], index: int) -> list[str]:
    errors: list[str] = []
    prefix = f"resource[{index}]"

    required_fields = {
        "id",
        "title",
        "url",
        "category",
        "source",
        "status",
        "summary",
        "primary_use",
        "pashto_evidence",
        "tags",
    }
    missing = sorted(required_fields - resource.keys())
    if missing:
        errors.append(f"{prefix} missing required fields: {', '.join(missing)}")
        return errors

    rid = resource["id"]
    if not isinstance(rid, str) or not RESOURCE_ID_RE.fullmatch(rid):
        errors.append(f"{prefix}.id must match {RESOURCE_ID_RE.pattern}")

    title = resource["title"]
    if not isinstance(title, str) or len(title.strip()) < 3:
        errors.append(f"{prefix}.title must be a non-empty string")

    url = resource["url"]
    if not isinstance(url, str) or not _is_valid_http_url(url):
        errors.append(f"{prefix}.url must be a valid http/https URL")

    category = resource["category"]
    if category not in ALLOWED_CATEGORIES:
        errors.append(f"{prefix}.category must be one of {sorted(ALLOWED_CATEGORIES)}")

    source = resource["source"]
    if source not in ALLOWED_SOURCES:
        errors.append(f"{prefix}.source must be one of {sorted(ALLOWED_SOURCES)}")

    status = resource["status"]
    if status not in ALLOWED_STATUS:
        errors.append(f"{prefix}.status must be one of {sorted(ALLOWED_STATUS)}")

    summary = resource["summary"]
    if not isinstance(summary, str) or len(summary.strip()) < 10:
        errors.append(f"{prefix}.summary must be at least 10 characters")

    primary_use = resource["primary_use"]
    if not isinstance(primary_use, str) or len(primary_use.strip()) < 3:
        errors.append(f"{prefix}.primary_use must be a non-empty string")

    if "tasks" in resource and not (
        isinstance(resource["tasks"], list)
        and all(isinstance(item, str) and item.strip() for item in resource["tasks"])
    ):
        errors.append(f"{prefix}.tasks must be a list of strings")

    tags = resource["tags"]
    if not (isinstance(tags, list) and tags and all(isinstance(tag, str) and tag.strip() for tag in tags)):
        errors.append(f"{prefix}.tags must be a non-empty list of strings")

    evidence = resource["pashto_evidence"]
    if not isinstance(evidence, dict):
        errors.append(f"{prefix}.pashto_evidence must be an object")
        return errors

    for key in ("evidence_text", "evidence_url", "markers"):
        if key not in evidence:
            errors.append(f"{prefix}.pashto_evidence missing '{key}'")

    evidence_text = evidence.get("evidence_text")
    if not isinstance(evidence_text, str) or len(evidence_text.strip()) < 3:
        errors.append(f"{prefix}.pashto_evidence.evidence_text must be a string")

    evidence_url = evidence.get("evidence_url")
    if not isinstance(evidence_url, str) or not _is_valid_http_url(evidence_url):
        errors.append(f"{prefix}.pashto_evidence.evidence_url must be a valid http/https URL")

    markers = evidence.get("markers")
    if not (isinstance(markers, list) and markers and all(isinstance(marker, str) and marker.strip() for marker in markers)):
        errors.append(f"{prefix}.pashto_evidence.markers must be a non-empty list of strings")

    return errors


def validate_catalog(catalog: dict[str, Any]) -> list[str]:
    errors: list[str] = []

    for key in ("version", "updated_on", "resources"):
        if key not in catalog:
            errors.append(f"catalog missing required top-level key: {key}")

    if errors:
        return errors

    version = catalog["version"]
    if not isinstance(version, str) or not re.fullmatch(r"^\d+\.\d+\.\d+$", version):
        errors.append("catalog.version must look like '1.0.0'")

    updated_on = catalog["updated_on"]
    if not isinstance(updated_on, str) or not _validate_iso_date(updated_on):
        errors.append("catalog.updated_on must be a valid ISO date (YYYY-MM-DD)")

    resources = catalog["resources"]
    if not isinstance(resources, list):
        errors.append("catalog.resources must be a list")
        return errors

    seen_ids: set[str] = set()
    for index, resource in enumerate(resources):
        if not isinstance(resource, dict):
            errors.append(f"resource[{index}] must be an object")
            continue
        errors.extend(validate_resource(resource, index))
        resource_id = resource.get("id")
        if isinstance(resource_id, str):
            if resource_id in seen_ids:
                errors.append(f"duplicate resource id: {resource_id}")
            seen_ids.add(resource_id)

    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--catalog", default="resources/catalog/resources.json")
    parser.add_argument("--schema", default="resources/schema/resource.schema.json")
    args = parser.parse_args()

    catalog_path = Path(args.catalog)
    schema_path = Path(args.schema)

    if not catalog_path.exists():
        print(f"Missing catalog file: {catalog_path}")
        return 1
    if not schema_path.exists():
        print(f"Missing schema file: {schema_path}")
        return 1

    try:
        schema = _load_json(schema_path)
        catalog = _load_json(catalog_path)
    except json.JSONDecodeError as exc:
        print(f"Invalid JSON: {exc}")
        return 1

    # Basic schema sanity check (this script enforces the validation rules directly).
    if not isinstance(schema, dict) or "$schema" not in schema:
        print("Schema file must be a JSON object with a '$schema' key")
        return 1

    errors = validate_catalog(catalog)
    if errors:
        print("Resource catalog validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Resource catalog valid: {len(catalog['resources'])} resources")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
