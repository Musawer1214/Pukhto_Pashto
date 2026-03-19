"""Report non-destructive quality signals across the resource pipeline."""

from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

try:
    from scripts.resource_quality import (
        normalized_title,
        resource_has_direct_pashto_signal,
        resource_has_metadata_pashto_signal,
        resource_is_candidate_like,
        resource_signal_origin,
    )
except ModuleNotFoundError:
    from resource_quality import (
        normalized_title,
        resource_has_direct_pashto_signal,
        resource_has_metadata_pashto_signal,
        resource_is_candidate_like,
        resource_signal_origin,
    )


def _load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def _repeat_url_groups(removal_log: dict[str, Any]) -> list[dict[str, Any]]:
    entries = removal_log.get("entries", [])
    counter: Counter[str] = Counter()
    for entry in entries:
        if isinstance(entry, dict):
            url = str(entry.get("url", "")).rstrip("/")
            if url:
                counter[url] += 1
    return [
        {"url": url, "count": count}
        for url, count in sorted(counter.items(), key=lambda item: (-item[1], item[0]))
        if count > 1
    ]


def _pending_previously_removed(
    pending_payload: dict[str, Any],
    removal_log: dict[str, Any],
) -> list[dict[str, Any]]:
    previous_urls = {
        str(entry.get("url", "")).rstrip("/")
        for entry in removal_log.get("entries", [])
        if isinstance(entry, dict)
    }
    results: list[dict[str, Any]] = []
    for candidate in pending_payload.get("candidates", []):
        if not isinstance(candidate, dict):
            continue
        url = str(candidate.get("url", "")).rstrip("/")
        if url and url in previous_urls:
            results.append(
                {
                    "id": candidate.get("id", ""),
                    "title": candidate.get("title", ""),
                    "url": candidate.get("url", ""),
                }
            )
    return results


def _candidate_like_verified(catalog: dict[str, Any]) -> list[dict[str, Any]]:
    results: list[dict[str, Any]] = []
    for resource in catalog.get("resources", []):
        if not isinstance(resource, dict):
            continue
        if str(resource.get("status")) == "verified" and resource_is_candidate_like(resource):
            results.append(
                {
                    "id": resource.get("id", ""),
                    "title": resource.get("title", ""),
                    "url": resource.get("url", ""),
                    "signal_origin": resource_signal_origin(resource),
                }
            )
    return results


def _metadata_only_verified(catalog: dict[str, Any]) -> list[dict[str, Any]]:
    results: list[dict[str, Any]] = []
    for resource in catalog.get("resources", []):
        if not isinstance(resource, dict):
            continue
        if resource_has_metadata_pashto_signal(resource) and not resource_has_direct_pashto_signal(resource):
            results.append(
                {
                    "id": resource.get("id", ""),
                    "title": resource.get("title", ""),
                    "category": resource.get("category", ""),
                    "source": resource.get("source", ""),
                }
            )
    return results


def _duplicate_title_groups(catalog: dict[str, Any]) -> list[dict[str, Any]]:
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for resource in catalog.get("resources", []):
        if not isinstance(resource, dict):
            continue
        title_key = normalized_title(str(resource.get("title", "")))
        if title_key:
            grouped[title_key].append(resource)

    results: list[dict[str, Any]] = []
    for title_key, items in grouped.items():
        if len(items) < 2:
            continue
        results.append(
            {
                "title_key": title_key,
                "entries": [
                    {
                        "id": item.get("id", ""),
                        "title": item.get("title", ""),
                        "category": item.get("category", ""),
                        "source": item.get("source", ""),
                        "url": item.get("url", ""),
                    }
                    for item in items
                ],
            }
        )
    return sorted(results, key=lambda item: item["title_key"])


def _datacite_project_collisions(catalog: dict[str, Any]) -> list[dict[str, Any]]:
    papers: dict[str, list[dict[str, Any]]] = defaultdict(list)
    projects: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for resource in catalog.get("resources", []):
        if not isinstance(resource, dict):
            continue
        source = str(resource.get("source", "")).strip()
        title_key = normalized_title(str(resource.get("title", "")))
        if not title_key:
            continue
        if source == "datacite" and resource.get("category") == "paper":
            papers[title_key].append(resource)
        if source == "datacite" and resource.get("category") == "project":
            projects[title_key].append(resource)

    results: list[dict[str, Any]] = []
    for title_key, project_items in projects.items():
        paper_items = papers.get(title_key)
        if not paper_items:
            continue
        results.append(
            {
                "title_key": title_key,
                "paper_ids": [item.get("id", "") for item in paper_items],
                "project_ids": [item.get("id", "") for item in project_items],
            }
        )
    return sorted(results, key=lambda item: item["title_key"])


def audit_resource_pipeline(
    *,
    catalog: dict[str, Any],
    pending_payload: dict[str, Any],
    removal_log: dict[str, Any],
) -> dict[str, Any]:
    return {
        "catalog_count": len(catalog.get("resources", [])) if isinstance(catalog.get("resources"), list) else 0,
        "pending_count": len(pending_payload.get("candidates", []))
        if isinstance(pending_payload.get("candidates"), list)
        else 0,
        "repeated_removal_urls": _repeat_url_groups(removal_log),
        "pending_previously_removed": _pending_previously_removed(pending_payload, removal_log),
        "candidate_like_verified": _candidate_like_verified(catalog),
        "metadata_only_verified": _metadata_only_verified(catalog),
        "duplicate_title_groups": _duplicate_title_groups(catalog),
        "datacite_project_collisions": _datacite_project_collisions(catalog),
    }


def _print_summary(report: dict[str, Any]) -> None:
    print("Resource pipeline audit summary:")
    print(f"- catalog_count={report['catalog_count']}")
    print(f"- pending_count={report['pending_count']}")
    print(f"- repeated_removal_urls={len(report['repeated_removal_urls'])}")
    print(f"- pending_previously_removed={len(report['pending_previously_removed'])}")
    print(f"- candidate_like_verified={len(report['candidate_like_verified'])}")
    print(f"- metadata_only_verified={len(report['metadata_only_verified'])}")
    print(f"- duplicate_title_groups={len(report['duplicate_title_groups'])}")
    print(f"- datacite_project_collisions={len(report['datacite_project_collisions'])}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--catalog", default="resources/catalog/resources.json")
    parser.add_argument("--pending", default="resources/catalog/pending_candidates.json")
    parser.add_argument("--removal-log", default="resources/catalog/removal_log.json")
    parser.add_argument("--output", default="")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    report = audit_resource_pipeline(
        catalog=_load_json(Path(args.catalog)),
        pending_payload=_load_json(Path(args.pending)),
        removal_log=_load_json(Path(args.removal_log)),
    )

    if args.output:
        Path(args.output).write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        _print_summary(report)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
