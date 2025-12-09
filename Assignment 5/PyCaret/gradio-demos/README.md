# Gradio Demos

- Models used: `classification-binary/binary_income_model.pkl`, `regression/regression_kc_house_model.pkl`, `timeseries/ts_airpassengers_model.pkl` (created by their notebooks).
- How to run: activate `.venv` then `python Assignment 5/PyCaret/gradio-demos/gradio_demo.py`. Gradio will print a local URL; keep the process running to use the UI.
- Tabs: Income Classifier (binary Adult model), House Price Regressor (KC house model), AirPassengers Forecast (univariate TS model).
- Requirements: `gradio`, `pycaret==3.3.0` (from root `requirements.txt`). Paths are resolved relative to the repo root via `pathlib`, so no manual path edits are needed if the repo structure stays intact.
- Notes: restart after regenerating models to pick up new weights. This low-code serving mirrors the PyCaret training simplicity and avoids custom FastAPI/Streamlit wiring used in other assignments.
