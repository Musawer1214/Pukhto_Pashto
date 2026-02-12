"""Validate normalization seed data for the Pashto project.

Usage:
    python scripts/validate_normalization.py data/processed/normalization_seed_v0.1.tsv
"""

from __future__ import annotations

import csv
import sys
from pathlib import Path


REQUIRED_COLUMNS = ("id", "raw_text", "normalized_text", "note")


def detect_delimiter(first_line: str) -> str | None:
    if "\t" in first_line:
        return "\t"
    if "," in first_line:
        return ","
    return None


def validate_file(path: Path) -> list[str]:
    errors: list[str] = []
    seen_ids: dict[str, int] = {}

    if not path.exists():
        return [f"File not found: {path}"]

    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        first_line = handle.readline()
        if not first_line:
            return [f"Empty file: {path}"]

        delimiter = detect_delimiter(first_line)
        if delimiter is None:
            return [
                "Could not detect delimiter. Use TSV (preferred) or CSV with headers: "
                + ", ".join(REQUIRED_COLUMNS)
            ]

        handle.seek(0)
        reader = csv.DictReader(handle, delimiter=delimiter)

        if reader.fieldnames is None:
            return [f"Missing header row in: {path}"]

        missing = [col for col in REQUIRED_COLUMNS if col not in reader.fieldnames]
        if missing:
            errors.append(f"Missing required columns: {', '.join(missing)}")
            return errors

        row_count = 0
        for line_number, row in enumerate(reader, start=2):
            row_count += 1

            row_id = (row.get("id") or "").strip()
            raw_text = (row.get("raw_text") or "").strip()
            normalized_text = (row.get("normalized_text") or "").strip()

            if not row_id:
                errors.append(f"Line {line_number}: empty 'id'")
            elif row_id in seen_ids:
                errors.append(
                    f"Line {line_number}: duplicate id '{row_id}' "
                    f"(first seen at line {seen_ids[row_id]})"
                )
            else:
                seen_ids[row_id] = line_number

            if not raw_text:
                errors.append(f"Line {line_number}: empty 'raw_text'")
            if not normalized_text:
                errors.append(f"Line {line_number}: empty 'normalized_text'")

        if row_count == 0:
            errors.append("No data rows found.")

    return errors


def main() -> int:
    if len(sys.argv) != 2:
        print(
            "Usage: python scripts/validate_normalization.py "
            "data/processed/normalization_seed_v0.1.tsv"
        )
        return 2

    input_path = Path(sys.argv[1])
    errors = validate_file(input_path)

    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Validation passed: {input_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
