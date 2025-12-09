# Multiclass Classification (Iris)

- Data: `../data/iris.csv`, target `species` (3 classes).
- Flow: load -> `setup(..., use_gpu=False, normalize=True)` -> `compare_models` -> `tune_model` -> plots (Confusion Matrix, Class Report, Feature Importance) -> `finalize_model` -> `predict_model` -> `save_model` (`multiclass_iris_model`).
- Outputs: `Confusion Matrix.png`, `Class Report.png`, `Feature Importance.png`, and `multiclass_iris_model.pkl`.
- Visuals: ![Confusion](Confusion%20Matrix.png) ![Class Report](Class%20Report.png) ![Feature Importance](Feature%20Importance.png)
- Env/run: Python 3.11 `.venv`, `pycaret==3.3.0`; run `multiclass_classification_pycaret.ipynb` end-to-end (CPU). Compared to hand-built pipelines in other assignments, PyCaret automates encoding/model selection and surfaces feature importance where supported.
