from __future__ import annotations

from csv_profiler.helpers import is_missing, infer_type

from csv_profiler.helpers import is_missing, try_float

def column_values(rows: list[dict[str, str]], col: str) -> list[str]:
    return [row.get(col, "") for row in rows]


def basic_profile(rows: list[dict[str, str]]) -> dict:
    columns = list(rows[0].keys()) if rows else []

    report: dict = {
        "summary": {
            "rows": len(rows),
            "columns": len(columns),
            "column_names": columns,
        },
        "columns": {},
    }

    for col in columns:
        values = column_values(rows, col)
        col_type_raw = infer_type(values)

        if col_type_raw in ("int", "float"):
            col_type = "number"
            stats = numeric_stats(values)
        else:
            col_type = "text"
            stats = text_stats(values)

        report["columns"][col] = {
            "type": col_type,
            "missing": stats.get("missing", 0),
            "stats": stats,
        }

    return report

def numeric_stats(values: list[str]) -> dict:
    """Compute stats for numeric column values (strings)."""
    usable = [v for v in values if not is_missing(v)]
    missing = len(values) - len(usable)

    nums: list[float] = []
    for v in usable:
        x = try_float(v)
        if x is None:
            raise ValueError(f"Non-numeric value found: {v!r}")
        nums.append(x)

    count = len(nums)
    unique = len(set(nums))
    min_v = min(nums) if nums else None
    max_v = max(nums) if nums else None
    mean_v = (sum(nums) / count) if count else None

    return {
        "count": count,
        "missing": missing,
        "unique": unique,
        "min": min_v,
        "max": max_v,
        "mean": mean_v,
    }

def text_stats(values: list[str]) -> dict:
    """Compute stats for text column values."""
    usable = [v for v in values if not is_missing(v)]
    missing = len(values) - len(usable)

    count = len(usable)
    unique = len(set(usable))

    if usable:
        top = max(set(usable), key=usable.count)
        freq = usable.count(top)
    else:
        top = None
        freq = None

    return {
        "count": count,
        "missing": missing,
        "unique": unique,
        "top": top,
        "freq": freq,
    }