import csv
import json
from io import StringIO
from pathlib import Path

import streamlit as st

from csv_profiler.profiling import profile_rows
from csv_profiler.render import render_markdown



# Task 1

st.set_page_config(page_title="CSV Profiler", layout="wide")
st.title("CSV Profiler")
st.caption("Upload CSV → profile → export JSON + Markdown")

st.sidebar.header("Inputs")

rows = None
report = st.session_state.get("report")



# Task 2 

uploaded = st.file_uploader("Upload a CSV", type=["csv"])
show_preview = st.sidebar.checkbox("Show preview", value=True)

if uploaded is not None:
    text = uploaded.getvalue().decode("utf-8-sig")
    rows = list(csv.DictReader(StringIO(text)))

    # Task 6 
    
    if len(rows) == 0:
        st.error("CSV has no data. Upload a CSV with at least 1 row.")
        st.stop()

    if len(rows[0]) == 0:
        st.warning("CSV has no headers (no columns detected).")

    st.write("Filename:", uploaded.name)
    st.write("Rows loaded:", len(rows))

    if show_preview:
        st.subheader("Preview")
        st.write(rows[:5])

else:
    st.info("Upload a CSV to begin.")



# Task 3 

if rows is not None and len(rows) > 0:
    if st.button("Generate report"):
        st.session_state["report"] = profile_rows(rows)

    report = st.session_state.get("report")

    if report is not None:
        cols = st.columns(2)
        cols[0].metric("Rows", report.get("n_rows", 0))
        cols[1].metric("Columns", report.get("n_cols", 0))


# Task 4

if report is not None:
    st.subheader("Columns")
    st.write(report.get("columns", {}))

    with st.expander("Markdown preview", expanded=False):
        st.markdown(render_markdown(report))

    with st.expander("Raw JSON (debug)", expanded=False):
        st.json(report)



if report is not None:
    report_name = st.sidebar.text_input("Report name", value="report").strip() or "report"

    json_file = f"{report_name}.json"
    md_file = f"{report_name}.md"

    json_text = json.dumps(report, indent=2, ensure_ascii=False)
    md_text = render_markdown(report)

    c1, c2 = st.columns(2)
    c1.download_button("Download JSON", data=json_text, file_name=json_file)
    c2.download_button("Download Markdown", data=md_text, file_name=md_file)

    if st.button("Save to outputs/"):
        out_dir = Path("outputs")
        out_dir.mkdir(parents=True, exist_ok=True)

        (out_dir / json_file).write_text(json_text, encoding="utf-8")
        (out_dir / md_file).write_text(md_text, encoding="utf-8")

        st.success(f"Saved outputs/{json_file} and outputs/{md_file}")
