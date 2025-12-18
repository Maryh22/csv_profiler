from __future__ import annotations


def is_missing(value: str | None) -> bool:
    if value is None:
        return True
    v = value.strip().lower()
    return v == "" or v in {"na", "n/a", "null", "none", "nan"}


def try_float(value: str) -> float | None:
    try:
        return float(value)
    except ValueError:
        return None


def infer_type(values: list[str]) -> str:
    non_missing = [v for v in values if not is_missing(v)]
    if not non_missing:
        return "text"

    for v in non_missing:
        if try_float(v) is None:
            return "text"
    return "number"


def profile_rows(rows: list[dict[str, str]]) -> dict:
    n_rows = len(rows)
    columns = list(rows[0].keys()) if rows else []
    n_cols = len(columns)

    cols_report = []

    for col in columns:
        values = [row.get(col, "") for row in rows]
        missing = sum(1 for v in values if is_missing(v))
        unique = len(set(v for v in values if not is_missing(v)))
        col_type = infer_type(values)

        cols_report.append(
            {
                "name": col,
                "type": col_type,
                "missing": missing,
                "unique": unique,
            }
        )

    return {
        "n_rows": n_rows,
        "n_cols": n_cols,
        "columns": cols_report,
    }
