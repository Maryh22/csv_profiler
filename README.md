## Setup
~~~
uv venv -p 3.112
uv pip install -r requirements.txt
~~~
## Run CLI
~~~
If you have a src/ folder:
Mac/Linux: export PYTHONPATH=src
Windows: $env:PYTHONPATH="src"
uv run python -m csv_profiler.cli profile data/sample.csv --out-dir outputs
~~~

## Run GUI
~~~
If you have a src/ folder:12
Mac/Linux: export PYTHONPATH=src13
Windows: $env:PYTHONPATH="src"14
uv run streamlit run app.py
~~~~