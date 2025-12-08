# Colab Notebook Starter (Reusable)

Use this starter to bootstrap future assignments with a Colab-ready workflow. It mirrors the pattern used in `Assignment 1` and is designed for lightweight EDA, preprocessing, modeling, and visuals on a tabular dataset.

## What’s inside
- `notebook_template.ipynb`: runnable template with placeholders for dataset path, target column, EDA plots, preprocessing, models, and metrics.
- `requirements.txt`: core Python deps for local or Colab use.

## Quick start (Colab)
1) Upload your dataset CSV to Colab and set `DATA_PATH` and `TARGET_COL` in the first config cell.
2) Run the install cell (optional on Colab if you need pinned versions): `pip install -r requirements.txt`.
3) Execute cells top-to-bottom. Replace any TODO placeholders with your dataset-specific logic (e.g., column names, model list, or target type).
4) Download the executed notebook to keep results/versioned outputs alongside your assignment.

## Quick start (local)
```bash
pip install -r requirements.txt
python -m ipykernel install --user --name python3 || true  # if kernel missing
```
Then open `notebook_template.ipynb` in Jupyter/VS Code and set `DATA_PATH` and `TARGET_COL`.

## Tips when adapting
- Prefer small subsamples if data is large; the template keeps compute light.
- Keep figures in `figures/` and reference them from your README.
- Update metrics/insights back into your assignment README after execution.
