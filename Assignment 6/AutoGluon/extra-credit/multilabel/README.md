# Multi-label Tabular — AutoGluon (Extra Credit 1.4)

Notebook: `multilabel_autogluon.ipynb`

- **Dataset**: 30% sample of the Adult Income CSV (`train_multi.csv`) with two binary label columns (`class_>50K`, `class_<=50K`) saved locally in `data/`.
- **Workaround**: `MultiLabelPredictor` is unavailable for Python 3.11, so two `TabularPredictor` binary models are trained one-vs-rest to mimic multi-label behavior. Models are persisted under `ag_multilabel_models/` (ignored in git).
- **Config**: `presets="medium_quality_faster_train"`, `time_limit=30s` per label, train/validation split of 80/20 with stratification on the original `class` column.
- **Results**: Both labels achieved perfect validation metrics (f1/accuracy/ROC AUC/precision/recall/mcc = 1.0) on the held-out 20% split. LightGBM/ExtraTrees dominated the ensembles; FastAI models were skipped because the optional extra dependency was not installed.
- **Outputs**: The notebook shows training logs, the first few combined predictions with probabilities for each label, and the metrics dictionary summarizing performance.
