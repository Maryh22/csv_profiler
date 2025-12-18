from __future__ import annotations


def render_markdown(report: dict) -> str:
    lines: list[str] = []

    # Title
    lines.append("# CSV Profiling Report\n")

    # Summary
    lines.append("## Summary\n")
    lines.append(f"- Rows: **{report['n_rows']}**")
    lines.append(f"- Columns: **{report['n_cols']}**\n")

    # Columns table
    lines.append("## Columns\n")
    lines.append("| Name | Type | Missing | Unique |")
    lines.append("|------|------|---------|--------|")

    for col in report["columns"]:
        lines.append(
            f"| {col['name']} | {col['type']} | {col['missing']} | {col['unique']} |"
        )

    return "\n".join(lines) + "\n"
