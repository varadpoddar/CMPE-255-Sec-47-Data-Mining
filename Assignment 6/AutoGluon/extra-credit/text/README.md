# AutoGluon Text Samples (Sentiment & Matching)

- **Notebook**: `text_autogluon.ipynb` (executed).
- **Sentiment classification**: 8 synthetic sentences labeled positive/negative; `MultiModalPredictor` (classification) trained in ~30s. Test metrics: `roc_auc = 1.0` on held-out 25%.
- **Sentence similarity (matching)**: 8 short query/response pairs with binary similarity labels; `MultiModalPredictor` with `query/response/match_label` trained in ~30s. Metrics on the small set: `roc_auc = 1.0`.
- **Artifacts**: Models stored under `ag_text_models/` (git-ignored). Notebook captures logs/metrics.
