# IEEE Fraud Detection — AutoGluon (Component 1)

Goals
- Run AutoGluon Tabular on the Kaggle IEEE-CIS fraud detection dataset.
- Produce an executed notebook with outputs (leaderboard, feature importance, predictions) for grading and 1–2 minute video walkthrough.

Environment
- Python 3.11 `.venv` or Colab GPU. Install deps: `pip install -r ../requirements.txt`.
- Requires Kaggle API credentials (`kaggle.json`) placed outside the repo; set `KAGGLE_USERNAME`/`KAGGLE_KEY` env vars or upload via Colab.

Run steps (Colab/local)
1) Install deps: `pip install autogluon.tabular kaggle`.
2) Download data: `!kaggle competitions download -c ieee-fraud-detection` then unzip to `data/`.
3) (Optional) Set `SAMPLE_FRACTION` to a smaller value (e.g., 0.1) for faster runs.
4) Run all cells in `ieee_fraud_autogluon.ipynb`; ensure leaderboard/feature importance/predictions render. Save the executed notebook with outputs to git.
5) Record a 1–2 minute walkthrough showing the notebook running (your execution).

Outputs to check in
- Executed notebook with outputs.
- No raw Kaggle data in the repo (keep in `data/` ignored by .gitignore).
- Updated README/script after run; screenshots optional.

Notes vs. earlier methodology assignments
- Low-code pipeline via `TabularPredictor` replaces manual preprocessing/EDA; focuses on AutoML leaderboard/tuning rather than CRISP/SEMMA phases.
- Kaggle API integration required; ensure credentials are provided at runtime, not committed.
