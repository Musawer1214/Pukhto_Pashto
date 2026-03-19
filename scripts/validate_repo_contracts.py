"""Validate catalog-adjacent repository JSON contracts."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

try:
    from jsonschema import Draft202012Validator, FormatChecker
except ModuleNotFoundError:
    Draft202012Validator = None
    FormatChecker = None


def _load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def _format_path(path: list[Any]) -> str:
    rendered = "payload"
    for item in path:
        if isinstance(item, int):
            rendered += f"[{item}]"
        else:
            rendered += f".{item}"
    return rendered


def validate_json_against_schema(
    payload: Any,
    schema: dict[str, Any],
    *,
    require_jsonschema: bool = False,
) -> list[str]:
    if Draft202012Validator is None or FormatChecker is None:
        if require_jsonschema:
            return ["jsonschema dependency is required; install with `pip install -e \".[dev]\"`"]
        return []

    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    errors = sorted(
        validator.iter_errors(payload),
        key=lambda error: (list(error.absolute_path), error.message),
    )
    return [f"{_format_path(list(error.absolute_path))}: {error.message}" for error in errors]


def _validate_search_payload_counts(name: str, payload: dict[str, Any]) -> list[str]:
    count = payload.get("count")
    resources = payload.get("resources")
    if not isinstance(count, int):
        return [f"{name}: payload.count must be an integer"]
    if not isinstance(resources, list):
        return [f"{name}: payload.resources must be a list"]
    if count != len(resources):
        return [f"{name}: payload.count={count} does not match resources length={len(resources)}"]
    return []


def _validate_single_contract(
    name: str,
    payload_path: Path,
    schema_path: Path,
    *,
    require_jsonschema: bool = False,
) -> list[str]:
    if not payload_path.exists():
        return [f"{name}: missing payload file {payload_path}"]
    if not schema_path.exists():
        return [f"{name}: missing schema file {schema_path}"]

    try:
        payload = _load_json(payload_path)
        schema = _load_json(schema_path)
    except json.JSONDecodeError as exc:
        return [f"{name}: invalid JSON: {exc}"]

    errors = validate_json_against_schema(payload, schema, require_jsonschema=require_jsonschema)
    if name in {"technical-search", "papers-search"} and isinstance(payload, dict):
        errors.extend(_validate_search_payload_counts(name, payload))
    return [f"{name}: {error}" for error in errors]


def validate_repo_contracts(
    *,
    pending_path: Path,
    pending_schema: Path,
    removal_log_path: Path,
    removal_log_schema: Path,
    technical_search_path: Path,
    papers_search_path: Path,
    search_schema: Path,
    benchmark_schema: Path,
    benchmark_results_root: Path,
    require_jsonschema: bool = False,
) -> list[str]:
    errors: list[str] = []
    errors.extend(
        _validate_single_contract(
            "pending-candidates",
            pending_path,
            pending_schema,
            require_jsonschema=require_jsonschema,
        )
    )
    errors.extend(
        _validate_single_contract(
            "removal-log",
            removal_log_path,
            removal_log_schema,
            require_jsonschema=require_jsonschema,
        )
    )
    errors.extend(
        _validate_single_contract(
            "technical-search",
            technical_search_path,
            search_schema,
            require_jsonschema=require_jsonschema,
        )
    )
    errors.extend(
        _validate_single_contract(
            "papers-search",
            papers_search_path,
            search_schema,
            require_jsonschema=require_jsonschema,
        )
    )

    benchmark_files = sorted(
        path
        for path in benchmark_results_root.rglob("*.json")
        if "templates" not in path.parts
    )
    if benchmark_files:
        if not benchmark_schema.exists():
            errors.append(f"benchmark-results: missing schema file {benchmark_schema}")
        else:
            schema = _load_json(benchmark_schema)
            for path in benchmark_files:
                try:
                    payload = _load_json(path)
                except json.JSONDecodeError as exc:
                    errors.append(f"benchmark-results: {path}: invalid JSON: {exc}")
                    continue
                schema_errors = validate_json_against_schema(
                    payload,
                    schema,
                    require_jsonschema=require_jsonschema,
                )
                errors.extend(f"benchmark-results: {path}: {error}" for error in schema_errors)

    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--pending", default="resources/catalog/pending_candidates.json")
    parser.add_argument("--pending-schema", default="resources/schema/pending_candidates.schema.json")
    parser.add_argument("--removal-log", default="resources/catalog/removal_log.json")
    parser.add_argument("--removal-log-schema", default="resources/schema/removal_log.schema.json")
    parser.add_argument("--technical-search", default="docs/search/resources.json")
    parser.add_argument("--papers-search", default="docs/papers/resources.json")
    parser.add_argument("--search-schema", default="resources/schema/search_payload.schema.json")
    parser.add_argument("--benchmark-schema", default="benchmarks/schema/benchmark_result.schema.json")
    parser.add_argument("--benchmark-results-root", default="benchmarks/results")
    parser.add_argument("--require-jsonschema", action="store_true")
    args = parser.parse_args()

    errors = validate_repo_contracts(
        pending_path=Path(args.pending),
        pending_schema=Path(args.pending_schema),
        removal_log_path=Path(args.removal_log),
        removal_log_schema=Path(args.removal_log_schema),
        technical_search_path=Path(args.technical_search),
        papers_search_path=Path(args.papers_search),
        search_schema=Path(args.search_schema),
        benchmark_schema=Path(args.benchmark_schema),
        benchmark_results_root=Path(args.benchmark_results_root),
        require_jsonschema=args.require_jsonschema,
    )
    if errors:
        print("Repository contract validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Repository contracts valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
