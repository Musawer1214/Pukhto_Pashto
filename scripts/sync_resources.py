"""Discover new Pashto-related resource candidates from public endpoints.

This script does not auto-merge into the main catalog. It writes candidates to
`resources/catalog/pending_candidates.json` for maintainer review.

Usage:
    python scripts/sync_resources.py
    python scripts/sync_resources.py --limit 20 --output resources/catalog/pending_candidates.json
"""

from __future__ import annotations

import argparse
import json
import re
import socket
import ssl
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from http.client import IncompleteRead
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError


USER_AGENT = "pashto-resource-sync/1.0"
MAX_FETCH_RETRIES = 4
RETRYABLE_HTTP_CODES = {429, 500, 502, 503, 504}


def _slug(value: str) -> str:
    value = value.lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    value = re.sub(r"-+", "-", value).strip("-")
    return value[:80] if value else "resource"


def _parse_retry_after_seconds(retry_after: str | None) -> float | None:
    if not retry_after:
        return None

    retry_after = retry_after.strip()
    if not retry_after:
        return None

    if retry_after.isdigit():
        return float(retry_after)

    try:
        retry_at = parsedate_to_datetime(retry_after)
    except (TypeError, ValueError):
        return None

    now = datetime.now(timezone.utc)
    if retry_at.tzinfo is None:
        retry_at = retry_at.replace(tzinfo=timezone.utc)
    return max(0.0, (retry_at - now).total_seconds())


def _is_ssl_cert_error(exc: BaseException) -> bool:
    if isinstance(exc, ssl.SSLCertVerificationError):
        return True
    if isinstance(exc, URLError):
        reason = exc.reason
        if isinstance(reason, ssl.SSLCertVerificationError):
            return True
    return "CERTIFICATE_VERIFY_FAILED" in str(exc)


def _retryable_network_error(exc: BaseException) -> bool:
    if _is_ssl_cert_error(exc):
        return False
    if isinstance(exc, (TimeoutError, socket.timeout, IncompleteRead, ConnectionResetError)):
        return True
    if isinstance(exc, URLError):
        reason = exc.reason
        if isinstance(reason, (TimeoutError, socket.timeout, IncompleteRead, ConnectionResetError)):
            return True
        return True
    return False


def _retry_delay(attempt: int, retry_after: str | None = None) -> float:
    parsed = _parse_retry_after_seconds(retry_after)
    if parsed is not None:
        return min(max(parsed, 0.0), 60.0)
    return min(2 ** (attempt - 1), 30.0)


def _fetch_bytes(
    url: str,
    *,
    timeout: float = 20.0,
    ssl_context: ssl.SSLContext | None = None,
    source_name: str = "remote",
) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    last_exc: BaseException | None = None

    for attempt in range(1, MAX_FETCH_RETRIES + 1):
        try:
            with urllib.request.urlopen(req, timeout=timeout, context=ssl_context) as response:
                return response.read()
        except HTTPError as exc:
            last_exc = exc
            if exc.code in RETRYABLE_HTTP_CODES and attempt < MAX_FETCH_RETRIES:
                delay = _retry_delay(attempt, exc.headers.get("Retry-After"))
                print(
                    f"[retry] {source_name} HTTP {exc.code} from {url}; "
                    f"retrying in {delay:.1f}s ({attempt}/{MAX_FETCH_RETRIES})"
                )
                time.sleep(delay)
                continue
            raise
        except Exception as exc:  # noqa: BLE001
            last_exc = exc
            if _retryable_network_error(exc) and attempt < MAX_FETCH_RETRIES:
                delay = _retry_delay(attempt)
                print(
                    f"[retry] {source_name} network error from {url}: {exc}; "
                    f"retrying in {delay:.1f}s ({attempt}/{MAX_FETCH_RETRIES})"
                )
                time.sleep(delay)
                continue
            raise

    if last_exc is not None:
        raise RuntimeError(f"{source_name} fetch failed after retries: {last_exc}") from last_exc
    raise RuntimeError(f"{source_name} fetch failed unexpectedly for {url}")


def _fetch_json(
    url: str,
    *,
    timeout: float = 20.0,
    ssl_context: ssl.SSLContext | None = None,
    source_name: str = "remote",
) -> Any:
    payload = _fetch_bytes(
        url,
        timeout=timeout,
        ssl_context=ssl_context,
        source_name=source_name,
    )
    return json.loads(payload.decode("utf-8"))


def _fetch_text(
    url: str,
    *,
    timeout: float = 20.0,
    ssl_context: ssl.SSLContext | None = None,
    source_name: str = "remote",
) -> str:
    payload = _fetch_bytes(
        url,
        timeout=timeout,
        ssl_context=ssl_context,
        source_name=source_name,
    )
    return payload.decode("utf-8", errors="replace")


def _candidate(
    *,
    rid: str,
    title: str,
    url: str,
    category: str,
    source: str,
    summary: str,
    evidence_text: str,
    evidence_url: str,
    markers: list[str],
    tags: list[str],
) -> dict[str, Any]:
    return {
        "id": rid,
        "title": title.strip(),
        "url": url.strip(),
        "category": category,
        "source": source,
        "status": "candidate",
        "summary": summary.strip(),
        "primary_use": "Needs maintainer review before promotion to verified catalog.",
        "tasks": [],
        "pashto_evidence": {
            "evidence_text": evidence_text.strip(),
            "evidence_url": evidence_url.strip(),
            "markers": markers,
        },
        "tags": tags,
    }


def fetch_huggingface(kind: str, limit: int) -> list[dict[str, Any]]:
    if kind not in {"datasets", "models"}:
        return []

    query = urllib.parse.urlencode({"search": "pashto", "limit": str(limit)})
    url = f"https://huggingface.co/api/{kind}?{query}"
    payload = _fetch_json(url, source_name=f"huggingface-{kind}")

    category = "dataset" if kind == "datasets" else "model"
    out: list[dict[str, Any]] = []
    for item in payload:
        repo_id = item.get("id") or item.get("modelId")
        if not repo_id:
            continue
        repo_url = f"https://huggingface.co/{'datasets/' if kind == 'datasets' else ''}{repo_id}"
        rid = f"candidate-hf-{kind[:-1]}-{_slug(repo_id)}"
        out.append(
            _candidate(
                rid=rid,
                title=repo_id,
                url=repo_url,
                category=category,
                source="huggingface",
                summary=f"Candidate {category} returned from Hugging Face search for Pashto.",
                evidence_text="Matched by Pashto keyword in Hugging Face search results.",
                evidence_url=repo_url,
                markers=["pashto"],
                tags=["pashto", "candidate", category],
            )
        )
    return out


def fetch_huggingface_spaces(limit: int) -> list[dict[str, Any]]:
    query = urllib.parse.urlencode({"search": "pashto", "limit": str(limit)})
    url = f"https://huggingface.co/api/spaces?{query}"
    payload = _fetch_json(url, source_name="huggingface-spaces")

    out: list[dict[str, Any]] = []
    for item in payload:
        space_id = item.get("id")
        if not space_id:
            continue
        space_url = f"https://huggingface.co/spaces/{space_id}"
        rid = f"candidate-hf-project-{_slug(space_id)}"
        summary = "Candidate project app returned from Hugging Face Spaces Pashto search."
        out.append(
            _candidate(
                rid=rid,
                title=space_id,
                url=space_url,
                category="project",
                source="huggingface",
                summary=summary,
                evidence_text="Matched by Pashto keyword in Hugging Face Spaces search.",
                evidence_url=space_url,
                markers=["pashto"],
                tags=["pashto", "candidate", "project", "space"],
            )
        )
    return out


def fetch_kaggle_datasets(limit: int) -> list[dict[str, Any]]:
    # Public Kaggle dataset listing endpoint (no auth needed for list responses).
    query = urllib.parse.urlencode({"search": "pashto", "page": "1"})
    url = f"https://www.kaggle.com/api/v1/datasets/list?{query}"
    payload = _fetch_json(url, source_name="kaggle-datasets")

    out: list[dict[str, Any]] = []
    for item in payload:
        title = (item.get("titleNullable") or "").strip()
        dataset_url = (item.get("urlNullable") or "").strip()
        owner = (item.get("ownerRefNullable") or "").strip()
        subtitle = (item.get("subtitleNullable") or "").strip()
        if not title or not dataset_url:
            continue

        blob = f"{title} {subtitle}".lower()
        if "pashto" not in blob and "pukhto" not in blob:
            continue

        owner_prefix = f"{owner}/" if owner else ""
        rid = f"candidate-kaggle-dataset-{_slug(owner_prefix + title)}"
        out.append(
            _candidate(
                rid=rid,
                title=title,
                url=dataset_url,
                category="dataset",
                source="kaggle",
                summary=(subtitle or "Candidate Kaggle dataset returned from Pashto search.")[:240],
                evidence_text="Kaggle dataset title/subtitle includes Pashto keyword.",
                evidence_url=dataset_url,
                markers=["Pashto"],
                tags=["pashto", "candidate", "dataset", "kaggle"],
            )
        )
        if len(out) >= limit:
            break
    return out


def fetch_github_pashto_repos(limit: int) -> list[dict[str, Any]]:
    # Query by topic first for high precision, then by keyword for recall.
    query_variants = [
        "topic:pashto",
        "pashto in:name,description,readme",
    ]

    combined: dict[str, dict[str, Any]] = {}
    for query_text in query_variants:
        query = urllib.parse.urlencode(
            {"q": query_text, "sort": "stars", "order": "desc", "per_page": str(limit)}
        )
        url = f"https://api.github.com/search/repositories?{query}"
        payload = _fetch_json(
            url,
            timeout=30.0,
            source_name="github-repositories",
        )
        for item in payload.get("items", []):
            full_name = item.get("full_name")
            html_url = item.get("html_url")
            if not full_name or not html_url:
                continue
            combined[full_name] = item

    out: list[dict[str, Any]] = []
    for full_name, item in sorted(combined.items(), key=lambda kv: kv[1].get("stargazers_count", 0), reverse=True):
        name_blob = " ".join(
            [
                full_name or "",
                item.get("name") or "",
                item.get("description") or "",
                " ".join(item.get("topics") or []),
            ]
        ).lower()
        if "pashto" not in name_blob and "pukhto" not in name_blob:
            continue

        html_url = item["html_url"]
        category = "project"
        topics = item.get("topics") or []
        if any(token in name_blob for token in ("toolkit", "library", "nlp", "asr", "tts", "ocr", "api", "code")):
            category = "code"

        rid = f"candidate-gh-{category}-{_slug(full_name)}"
        description = (item.get("description") or "").strip()
        summary = description or "Candidate Pashto-related GitHub repository."
        out.append(
            _candidate(
                rid=rid,
                title=full_name,
                url=html_url,
                category=category,
                source="github",
                summary=summary[:240] if summary else "Candidate Pashto-related GitHub repository.",
                evidence_text="Repository metadata (name/description/topics) includes Pashto markers.",
                evidence_url=html_url,
                markers=["pashto"],
                tags=["pashto", "candidate", category, "github", *(topics[:3])],
            )
        )
        if len(out) >= limit:
            break
    return out


def fetch_arxiv(limit: int) -> list[dict[str, Any]]:
    query = urllib.parse.urlencode(
        {"search_query": "all:pashto", "start": "0", "max_results": str(limit)}
    )
    url = f"https://export.arxiv.org/api/query?{query}"
    try:
        xml_text = _fetch_text(url, timeout=30.0, source_name="arxiv")
    except Exception as exc:  # noqa: BLE001
        if not _is_ssl_cert_error(exc):
            raise
        # arXiv occasionally fails cert chain validation in some runner images.
        insecure_context = ssl._create_unverified_context()
        print("[warn] arxiv SSL verification failed; retrying with unverified TLS context")
        xml_text = _fetch_text(
            url,
            timeout=30.0,
            ssl_context=insecure_context,
            source_name="arxiv",
        )
    root = ET.fromstring(xml_text)
    ns = {"atom": "http://www.w3.org/2005/Atom"}

    out: list[dict[str, Any]] = []
    for entry in root.findall("atom:entry", ns):
        title = (entry.findtext("atom:title", default="", namespaces=ns) or "").strip()
        link = (entry.findtext("atom:id", default="", namespaces=ns) or "").strip()
        summary = (entry.findtext("atom:summary", default="", namespaces=ns) or "").strip()
        if not title or not link:
            continue

        rid = f"candidate-arxiv-{_slug(title)}"
        out.append(
            _candidate(
                rid=rid,
                title=title,
                url=link,
                category="paper",
                source="arxiv",
                summary=summary[:240] if summary else "Candidate paper returned from arXiv query for Pashto.",
                evidence_text="Matched by arXiv query: all:pashto.",
                evidence_url=link,
                markers=["pashto"],
                tags=["pashto", "candidate", "paper"],
            )
        )
    return out


def fetch_semantic_scholar(limit: int) -> list[dict[str, Any]]:
    fields = "title,url,abstract,year,externalIds"
    query = urllib.parse.urlencode(
        {"query": "pashto", "limit": str(limit), "fields": fields}
    )
    url = f"https://api.semanticscholar.org/graph/v1/paper/search?{query}"
    payload = _fetch_json(
        url,
        timeout=30.0,
        source_name="semantic-scholar",
    )

    out: list[dict[str, Any]] = []
    for item in payload.get("data", []):
        title = (item.get("title") or "").strip()
        if not title:
            continue
        paper_url = (item.get("url") or "").strip()
        if not paper_url:
            ext = item.get("externalIds") or {}
            arxiv_id = ext.get("ArXiv")
            if arxiv_id:
                paper_url = f"https://arxiv.org/abs/{arxiv_id}"
        if not paper_url:
            continue

        summary = (item.get("abstract") or "").strip()
        rid = f"candidate-s2-{_slug(title)}"
        out.append(
            _candidate(
                rid=rid,
                title=title,
                url=paper_url,
                category="paper",
                source="other",
                summary=summary[:240] if summary else "Candidate paper returned from Semantic Scholar search for Pashto.",
                evidence_text="Matched by Semantic Scholar query: pashto.",
                evidence_url=paper_url,
                markers=["pashto"],
                tags=["pashto", "candidate", "paper"],
            )
        )
    return out


def _dedupe_candidates(
    candidates: list[dict[str, Any]],
    existing_ids: set[str],
    existing_urls: set[str],
) -> list[dict[str, Any]]:
    unique: list[dict[str, Any]] = []
    seen_ids = set(existing_ids)
    seen_urls = set(existing_urls)

    for item in candidates:
        rid = item["id"]
        url = item["url"].rstrip("/")
        if rid in seen_ids or url in seen_urls:
            continue
        seen_ids.add(rid)
        seen_urls.add(url)
        unique.append(item)
    return unique


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--catalog", default="resources/catalog/resources.json")
    parser.add_argument("--output", default="resources/catalog/pending_candidates.json")
    parser.add_argument("--limit", type=int, default=15)
    args = parser.parse_args()

    catalog_path = Path(args.catalog)
    output_path = Path(args.output)

    catalog = json.loads(catalog_path.read_text(encoding="utf-8"))
    resources = catalog.get("resources", [])
    existing_ids = {resource.get("id", "") for resource in resources if isinstance(resource, dict)}
    existing_urls = {
        resource.get("url", "").rstrip("/")
        for resource in resources
        if isinstance(resource, dict) and isinstance(resource.get("url"), str)
    }

    all_candidates: list[dict[str, Any]] = []
    source_errors: list[str] = []
    sources_used: list[str] = []

    fetch_steps = [
        ("kaggle-datasets", lambda: fetch_kaggle_datasets(args.limit)),
        ("huggingface-datasets", lambda: fetch_huggingface("datasets", args.limit)),
        ("huggingface-models", lambda: fetch_huggingface("models", args.limit)),
        ("huggingface-spaces", lambda: fetch_huggingface_spaces(args.limit)),
        ("github-repositories", lambda: fetch_github_pashto_repos(args.limit)),
        ("arxiv", lambda: fetch_arxiv(args.limit)),
        ("semantic-scholar", lambda: fetch_semantic_scholar(args.limit)),
    ]

    for source_name, step in fetch_steps:
        try:
            results = step()
            all_candidates.extend(results)
            sources_used.append(source_name)
        except Exception as exc:  # noqa: BLE001
            source_errors.append(f"{source_name}: {exc}")

    unique_candidates = _dedupe_candidates(all_candidates, existing_ids, existing_urls)
    unique_candidates = sorted(unique_candidates, key=lambda item: item["title"].lower())

    payload: dict[str, Any] = {
        "generated_on": datetime.now(timezone.utc).isoformat(),
        "sources": sources_used,
        "candidate_count": len(unique_candidates),
        "candidates": unique_candidates,
    }
    if source_errors:
        payload["errors"] = source_errors

    output_path.parent.mkdir(parents=True, exist_ok=True)
    if output_path.exists():
        try:
            old_payload = json.loads(output_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            old_payload = None
        if isinstance(old_payload, dict):
            old_compare = {key: value for key, value in old_payload.items() if key != "generated_on"}
            new_compare = {key: value for key, value in payload.items() if key != "generated_on"}
            if old_compare == new_compare:
                print(
                    f"Candidate sync complete: {len(unique_candidates)} new candidates, "
                    f"{len(source_errors)} source errors, no file changes"
                )
                return 0

    output_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(
        f"Candidate sync complete: {len(unique_candidates)} new candidates, "
        f"{len(source_errors)} source errors"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
