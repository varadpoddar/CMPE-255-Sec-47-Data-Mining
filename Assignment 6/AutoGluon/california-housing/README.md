# California Housing — AutoGluon (Component 2)

What was run
- Dataset: California Housing (sklearn fallback), sampled at 10% for speed (495 train rows, 124 test rows).
- Training: `TabularPredictor(label='median_house_value', presets='best_quality', time_limit=60s)` with AutoGluon 1.1.1 on Python 3.11.
- Models: Stacked/ensembled LightGBM/CatBoost/RandomForest; fastai/torch models were skipped (missing deps) as expected.

Key results (from executed notebook)
- Best model: `WeightedEnsemble_L3` with RMSE ≈ 0.61 on the holdout. LightGBM/RandomForest/CatBoost variants clustered around ~0.62–0.64 RMSE.
- Feature importance (permutation on test split, top 4): MedInc ≫ AveOccup ≈ Latitude ≈ Longitude. Rooms/house age mattered less in this sampled run.
- Evaluation summary: RMSE ≈ 0.61, MAE ≈ 0.43, R2 ≈ 0.70; sample predictions printed for first 5 rows.

Files
- `california_housing_autogluon.ipynb`: executed with outputs (leaderboards, training logs, feature importance, metrics).
- `assignment.script`: talk track for the 1–2 minute demo video.

Notes
- Data are kept out of git (`data/` ignored); model artifacts can be large and are ignored (`ag_california_models/`).
- This component focuses on AutoGluon’s low-code AutoML rather than CRISP/KDD-style feature engineering.
