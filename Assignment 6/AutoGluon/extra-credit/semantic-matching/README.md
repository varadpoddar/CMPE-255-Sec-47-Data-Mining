# AutoGluon Semantic Matching (text-to-text)

- **Notebook**: `semantic_matching_autogluon.ipynb` (executed).
- **Dataset**: 4 tiny query/response pairs with binary similarity labels.
- **Setup**: `MultiModalPredictor` with `label/query/response/match_label` on CPU, `eval_metric='accuracy'`, `time_limit=30s`.
- **Result**: Accuracy on the tiny set = 0.75 (as seen in the notebook output). Models saved under `ag_semantic_models/` (git-ignored).
