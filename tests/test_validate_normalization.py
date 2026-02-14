from pathlib import Path

from scripts.validate_normalization import validate_file


def _write(path: Path, content: str) -> Path:
    path.write_text(content, encoding="utf-8")
    return path


def test_validate_file_passes_with_valid_tsv(tmp_path: Path) -> None:
    file_path = _write(
        tmp_path / "valid.tsv",
        "id\traw_text\tnormalized_text\tnote\n"
        "n001\tfoo\tfoo\tok\n",
    )
    assert validate_file(file_path) == []


def test_validate_file_fails_on_duplicate_id(tmp_path: Path) -> None:
    file_path = _write(
        tmp_path / "dup.tsv",
        "id\traw_text\tnormalized_text\tnote\n"
        "n001\tfoo\tfoo\tok\n"
        "n001\tbar\tbar\tdup\n",
    )
    errors = validate_file(file_path)
    assert any("duplicate id" in error for error in errors)


def test_validate_file_fails_on_missing_columns(tmp_path: Path) -> None:
    file_path = _write(
        tmp_path / "missing.tsv",
        "id\traw_text\tnote\n"
        "n001\tfoo\tmissing normalized\n",
    )
    errors = validate_file(file_path)
    assert errors
    assert "Missing required columns: normalized_text" in errors[0]
