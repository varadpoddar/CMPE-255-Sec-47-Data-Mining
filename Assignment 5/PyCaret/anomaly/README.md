# Anomaly Detection (Credit Card Transactions)

- Data: `../data/creditcard.csv`; label `Class` kept only for reference. Notebook defaults to a 25% sample to keep runtime manageable.
- Env: Python 3.11 with `pycaret==3.3.0` (see root requirements). GPU disabled (`use_gpu=False`).
- Flow: load -> drop `Class` for training -> optional sampling via `SAMPLE_FRAC` -> `setup(..., normalize=True)` -> `create_model('iforest')` -> `assign_model` to attach `Anomaly` and `Anomaly_Score` -> `save_model` (`anomaly_creditcard_iforest`). Heavy t-SNE/UMAP plotting is skipped (one prior t-SNE image present from earlier run).
- Outputs: saved model, anomaly labels/scores in the notebook output, and an existing `t-SNE (3d) Dimension Plot.png`.
- Visuals: ![t-SNE](t-SNE%20(3d)%20Dimension%20Plot.png)
- Run: execute `anomaly_pycaret.ipynb` end-to-end; tweak `SAMPLE_FRAC` for speed/fidelity.
