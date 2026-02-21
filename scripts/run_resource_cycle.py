"""Run the Pashto resource update cycle in a repeatable way.

This script is a command wrapper around existing resource scripts so maintainers
do not need to remember the full sequence.

Usage:
    python scripts/run_resource_cycle.py
    python scripts/run_resource_cycle.py --limit 30
    python scripts/run_resource_cycle.py --skip-pytest
    python scripts/run_resource_cycle.py --discover-only
    python scripts/run_resource_cycle.py --max-promotions 10
    python scripts/run_resource_cycle.py --skip-existing-review
    python scripts/run_resource_cycle.py --skip-pashto-relevance-check
"""

from __future__ import annotations

import argparse
import shlex
import subprocess
import sys
from pathlib import Path


def _run(command: list[str], cwd: Path) -> int:
    print(f"[run] {shlex.join(command)}")
    completed = subprocess.run(command, cwd=str(cwd), check=False)
    return completed.returncode


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=25, help="Candidate fetch limit per source")
    parser.add_argument("--skip-pytest", action="store_true", help="Skip pytest step")
    parser.add_argument("--discover-only", action="store_true", help="Only sync candidates and stop")
    parser.add_argument(
        "--max-promotions",
        type=int,
        default=None,
        help="Optional cap for auto-promotion count from pending candidates",
    )
    parser.add_argument(
        "--skip-existing-review",
        action="store_true",
        help="Skip review/removal of stale existing resources before syncing candidates.",
    )
    parser.add_argument(
        "--resource-timeout",
        type=float,
        default=12.0,
        help="Timeout in seconds for existing-resource URL probes.",
    )
    parser.add_argument(
        "--skip-pashto-relevance-check",
        action="store_true",
        help="Disable Pashto relevance filtering in existing-resource review.",
    )
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parents[1]
    steps: list[list[str]] = []
    if not args.skip_existing_review:
        review_step = [
            "python",
            "scripts/review_existing_resources.py",
            "--timeout",
            str(args.resource_timeout),
        ]
        if not args.skip_pashto_relevance_check:
            review_step.append("--enforce-pashto-relevance")
        steps.append(review_step)

    steps.append(["python", "scripts/sync_resources.py", "--limit", str(args.limit)])

    if not args.discover_only:
        promote_step = ["python", "scripts/promote_candidates.py"]
        if args.max_promotions is not None:
            promote_step.extend(["--max-promotions", str(args.max_promotions)])
        steps.extend(
            [
                promote_step,
                ["python", "scripts/validate_resource_catalog.py"],
                ["python", "scripts/generate_resource_views.py"],
                ["python", "scripts/check_links.py"],
            ]
        )
        if not args.skip_pytest:
            steps.append(["python", "-m", "pytest", "-q"])

    for command in steps:
        code = _run(command, repo_root)
        if code != 0:
            print(f"[fail] Step failed with exit code {code}")
            return code

    print("[ok] Resource cycle completed")
    if args.discover_only:
        print(
            "Next: review resources/catalog/pending_candidates.json and promote approved "
            "entries into resources/catalog/resources.json."
        )
    else:
        print("Next: commit updated catalog/generated files and push.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
