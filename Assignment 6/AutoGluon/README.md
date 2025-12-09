# Assignment 6 — AutoGluon

This assignment focuses on running and documenting AutoGluon Colab notebooks for Kaggle competitions and tabular tasks. Components will be completed one at a time per `Assignment.steps`.

## Components
- IEEE Fraud Detection (Kaggle) — AutoGluon Tabular (this component scaffolded here).
- California Housing (Kaggle) — AutoGluon Tabular (executed on SAMPLE_FRACTION=0.1, time_limit=60s; notebook saved with outputs).
- AutoGluon tabular demos: quick start, in-depth, multimodal tabular, feature engineering (later components).

## Environment
- Python 3.11 `.venv` locally; Colab GPU recommended for faster training.
- Install requirements via `pip install -r requirements.txt` (or `pip install autogluon.tabular kaggle`).
- Datasets pulled via Kaggle API; keep credentials outside the repo.

## Structure
- `ieee-fraud/`: Kaggle IEEE-CIS fraud detection notebook, README, and talk track.
- Additional component folders will be added sequentially.

## Status
- IEEE fraud scaffold ready; execute in Colab/local with Kaggle credentials to generate outputs for submission and video.
