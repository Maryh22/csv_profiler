from __future__ import annotations

import json
from pathlib import Path

from csv_profiler.io import read_csv_rows
from csv_profiler.profiling import profile_rows
from csv_profiler.render import render_markdown


def main() -> None:
    rows = read_csv_rows("data/sample.csv")
    report = profile_rows(rows)

    out_dir = Path("outputs")
    out_dir.mkdir(parents=True, exist_ok=True)

    # write json
    (out_dir / "report.json").write_text(
        json.dumps(report, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    # write markdown
    (out_dir / "report.md").write_text(
        render_markdown(report),
        encoding="utf-8",
    )

    print("Wrote outputs/report.json and outputs/report.md")


if __name__ == "__main__":
    main()
