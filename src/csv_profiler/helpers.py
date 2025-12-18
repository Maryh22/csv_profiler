from __future__ import annotations


def is_missing(value: str | None) -> bool:
    """Return True if value is considered missing."""
    if value is None:
        return True
    return value.strip() == ""


def try_float(value: str) -> float | None:
    """Try converting a string to float. Return None if it fails."""
    try:
        return float(value)
    except ValueError:
        return None


def infer_type(values: list[str]) -> str:
    """
    Infer column type based on its values.
    Returns: 'int', 'float', or 'str'
    """
    numeric_count = 0

    for v in values:
        if is_missing(v):
            continue
        if try_float(v) is not None:
            numeric_count += 1

    if numeric_count == 0:
        return "str"
    if numeric_count == len(values):
        return "float"
    return "str"
