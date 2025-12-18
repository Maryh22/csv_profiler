from __future__ import annotations

import json
from pathlib import Path
import typer

from csv_profiler.io import read_csv_rows
from csv_profiler.profiling import profile_rows
from csv_profiler.render import render_markdown

app = typer.Typer()


@app.command()
def profile(
    input_path: Path = typer.Argument(..., help="Path to input CSV file"),
    out_dir: Path = typer.Option("outputs", "--out-dir", help="Output directory"),
    report_name: str = typer.Option("report", "--report-name", help="Base report name"),
) -> None:
    rows = read_csv_rows(input_path)
    report = profile_rows(rows)

    out_dir.mkdir(parents=True, exist_ok=True)

    (out_dir / f"{report_name}.json").write_text(
        json.dumps(report, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    (out_dir / f"{report_name}.md").write_text(
        render_markdown(report),
        encoding="utf-8",
    )

    typer.echo(f"Wrote {out_dir}/{report_name}.json and {out_dir}/{report_name}.md")


if __name__ == "__main__":
    app()
