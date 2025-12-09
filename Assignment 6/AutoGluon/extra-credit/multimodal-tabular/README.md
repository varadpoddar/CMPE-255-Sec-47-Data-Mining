# AutoGluon Multimodal (text + tabular) — synthetic

- **Notebook**: `multimodal_tabular_autogluon.ipynb` (executed).
- **Dataset**: 8 synthetic phone reviews with a text field (`review`), numeric `price` and `rating`, and binary `label` (good vs bad).
- **Setup**: `MultiModalPredictor` with `problem_type='binary'`, `eval_metric='accuracy'`, `time_limit=30s`; 75/25 train/val split.
- **Result**: `accuracy = 1.0` on the small validation split (tiny dataset, so near-perfect fit is expected).
- **Artifacts**: Models under `ag_multimodal_models/` (git-ignored).
