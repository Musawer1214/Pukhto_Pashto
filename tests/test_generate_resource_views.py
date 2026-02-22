from scripts.generate_resource_views import _build_search_payload, _partition_search_resources


def _resource(*, rid: str, category: str, status: str = "verified") -> dict:
    return {
        "id": rid,
        "title": f"{rid} title",
        "url": f"https://example.org/{rid}",
        "category": category,
        "source": "other",
        "status": status,
        "summary": "Pashto-focused resource summary for search payload tests.",
        "primary_use": "Testing payload generation",
        "tasks": ["nlp"],
        "pashto_evidence": {
            "evidence_text": "Contains explicit Pashto marker in title.",
            "evidence_url": f"https://example.org/{rid}",
            "markers": ["pashto"],
        },
        "tags": ["pashto", category],
    }


def test_partition_search_resources_routes_papers_to_papers_payload() -> None:
    resources = [
        _resource(rid="dataset-a", category="dataset"),
        _resource(rid="paper-a", category="paper"),
        _resource(rid="project-a", category="project"),
        _resource(rid="paper-b", category="paper"),
    ]

    technical, papers = _partition_search_resources(resources)

    assert [item["id"] for item in technical] == ["dataset-a", "project-a"]
    assert [item["id"] for item in papers] == ["paper-a", "paper-b"]


def test_partition_search_resources_keeps_non_paper_categories_in_technical_payload() -> None:
    resources = [
        _resource(rid="code-a", category="code"),
        _resource(rid="tool-a", category="tool"),
    ]

    technical, papers = _partition_search_resources(resources)

    assert len(technical) == 2
    assert papers == []


def test_build_search_payload_includes_expected_fields() -> None:
    payload = _build_search_payload([_resource(rid="paper-a", category="paper")], "2026-02-22")

    assert payload["generated_on"] == "2026-02-22T00:00:00Z"
    assert payload["count"] == 1
    item = payload["resources"][0]
    assert item["id"] == "paper-a"
    assert item["category"] == "paper"
    assert item["markers"] == ["pashto"]
