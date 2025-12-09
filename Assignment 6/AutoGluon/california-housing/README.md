# California Housing — AutoGluon (Component 2)

Goal
- Run AutoGluon Tabular on the California housing price dataset (Kaggle mirror). Produce executed notebook with outputs for grading and 1–2 minute walkthrough.

Environment
- Python 3.11 `.venv` or Colab GPU. Install deps: `pip install -r ../requirements.txt`.
- Data: download Kaggle California Housing (or use sklearn fetch_california_housing as fallback). Keep raw data out of git; place under `data/` (ignored).

Run steps (Colab/local)
1) Install deps: `pip install autogluon.tabular kaggle`.
2) Obtain data: `!kaggle datasets download -d camnugent/california-housing-prices -p data/` and unzip, or use sklearn fetch in notebook (fallback is built-in).
3) Set `SAMPLE_FRACTION` env var (e.g., 0.1 used in the executed run) to keep runtime small; default time_limit=60s in the notebook.
4) Run all cells in `california_housing_autogluon.ipynb`; leaderboard, feature importance, and metrics are produced. Executed notebook with outputs is saved in-place.
5) Record a 1–2 minute walkthrough showing your execution.

Outputs to check in
- Executed notebook with outputs (no raw data committed).
- README/script updated after run; figures can be embedded if saved (none generated in the sample run).
- Sample run (SAMPLE_FRACTION=0.1, time_limit=60s): best model WeightedEnsemble_L3 with RMSE ≈ 0.61 on holdout; feature importance computed on 124-row test split.

Notes vs earlier assignments
- Low-code AutoGluon replaces manual feature engineering; focus on leaderboard and fit/predict for regression. This contrasts with CRISP/KDD pipelines in prior assignments.
