# AutoGluon Tabular with GPU (Extra Credit 1.5)

- **Dataset**: Adult Income (`train.csv`) downloaded to `data/`, sampled 20% for a quick run; 80/20 train/test split stratified on `class`.
- **Environment**: CUDA not available on this Mac (arm64), so the tutorial runs on CPU while still using the GPU-friendly presets (`num_gpus="auto"`).
- **Training setup**: `TabularPredictor` with `presets="medium_quality_faster_train"`, `time_limit=60s`, `eval_metric=roc_auc`. Models saved under `ag_gpu_models/` (ignored in git).
- **Leaderboard (top)**: WeightedEnsemble_L2 (CatBoost + XGBoost + ExtraTrees + k-NN + Torch) reached `roc_auc=0.916` on the test split; CatBoost alone at `0.914`, XGBoost at `0.911`, LightGBM at `0.910`.
- **Metrics (test split)**: roc_auc=0.916, accuracy=0.861, balanced_accuracy=0.766, f1=0.663, precision=0.755, recall=0.590.
- **Artifacts**: Executed notebook with outputs: `gpu_autogluon.ipynb` includes CUDA check, training logs, leaderboard, and metric dictionary.
