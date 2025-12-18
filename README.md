## Setup
uv venv -p 3.11
uv pip install -r requirements.txt

## Run CLI
# If you have a src/ folder:
# Windows PowerShell:
$env:PYTHONPATH="src"
uv run python -m csv_profiler.cli profile data/sample.csv --out-dir outputs

## Run GUI
# If you have a src/ folder:
$env:PYTHONPATH="src"
uv run streamlit run app.py

## Output Files
- outputs/report.json
- outputs/report.md
