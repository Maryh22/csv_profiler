# CSV Profiler

A simple CSV profiling tool with:
- Command Line Interface (CLI)
- Streamlit Web GUI

---

## Setup

Create a virtual environment and install dependencies:

```
uv venv -p 3.11
uv pip install -r requirements.txt
```
$env:PYTHONPATH="src"
uv run python -m csv_profiler.cli data/sample.csv --out-dir outputs
