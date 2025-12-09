# Assignment 5 — PyCaret (Local, Python 3.11)

What was achieved
- Executed, PyCaret-driven notebooks for binary & multiclass classification, regression, clustering, anomaly detection, association rules (via mlxtend), and time series (univariate + exogenous), all running in the shared Python 3.11 `.venv` with `pycaret==3.3.0`.
- Saved plots and models per task, linked from each sub-README; Gradio app wired to the saved classifier, regressor, and time-series models.
- Compared to prior methodology-heavy assignments (CRISP/SEMMA/KDD), this one uses PyCaret’s low-code pipeline (`setup` → `compare_models` → `tune_model` → `finalize_model`) to automate preprocessing, model selection, and evaluation, with light bespoke changes (sampling for anomaly, mlxtend for rules).

Environment and constraints
- Python 3.11 `.venv` (see `requirements.txt`). GPU is disabled (`use_gpu=False`) to avoid local LightGBM GPU build issues; all runs are CPU.
- Data lives in `Assignment 5/PyCaret/data/`; notebooks assume `../data/<file>.csv`.

## Structure
- `classification-binary/`
- `classification-multiclass/`
- `regression/`
- `clustering/`
- `anomaly/`
- `association-rules/`
- `timeseries/` (univariate, with/without exogenous)
- `gradio-demos/`
- Figures live beside their notebooks in each folder.

Shared deps: `requirements.txt` (PyCaret 3.3.0, scikit-learn 1.4.2, mlxtend, Gradio, etc.).

## Dataset choices (Kaggle/local CSVs)
- Binary classification: Adult Census Income — https://www.kaggle.com/datasets/uciml/adult-census-income (target `income`).
- Multiclass classification: Iris — https://www.kaggle.com/datasets/uciml/iris (target `Species`).
- Regression: King County House Sales — https://www.kaggle.com/datasets/harlfoxem/housesalesprediction (target `price`).
- Clustering: Wine Quality — https://www.kaggle.com/datasets/rajyellow46/wine-quality (use features, drop `quality`; file `winequalityN.csv`).
- Anomaly detection: Credit Card Fraud — https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud (use `Class` as label for scoring/inspection).
- Association rules: Groceries basket — https://www.kaggle.com/datasets/heeraldedhia/groceries-dataset (market basket CSV).
- Time series (univariate): Airline Passengers — https://www.kaggle.com/datasets/rakannimer/air-passengers (monthly passengers).
- Time series (with exogenous): Daily Delhi Climate — https://www.kaggle.com/datasets/sumanthvrao/daily-climate-time-series-data (use `meantemp` target + covariates; add synthetic DOW/holiday if desired).
- Gradio demos: reuse tuned binary classifier and regression model above; serve via Gradio UI.

### Expected local files (place under `Assignment 5/PyCaret/data/`)
- `adult.csv` (Adult Census Income)
- `iris.csv` (Iris)
- `kc_house_data.csv` (King County House Sales)
- `winequalityN.csv` (Wine Quality)
- `creditcard.csv` (Credit Card Fraud)
- `groceries.csv` (Groceries basket)
- `AirPassengers.csv` (Airline Passengers)
- `DailyDelhiClimateTrain.csv` (Daily Delhi Climate)

Create the `data/` folder and drop these CSVs there before running the notebooks. Each notebook’s `csv_path` points to `../data/<filename>` by default—adjust if you store them elsewhere.

## Per-task notebook flow (low-code vs methodology-heavy work)
- Common: load data, split (or time-series split), `setup(..., use_gpu=False)`, `compare_models`, `tune_model`, `plot_model` (classification ROC/PR/confusion; regression residuals/feature/error; clustering elbow/silhouette/tsne; time-series forecast/diagnostics), `finalize_model`, `predict_model`, `save_model`.
- Classification: imbalance fix (binary), leaderboards, tuned winners, confusion/PR/AUC plots.
- Regression: baselines vs tuned, residuals/error/feature-importance plots.
- Clustering: k-means with elbow/silhouette/t-SNE visuals and saved model.
- Anomaly: isolation forest on sampled credit-card data; heavy plots skipped to avoid >30 min runs.
- Association rules: mlxtend Apriori + association_rules (PyCaret 3.x lacks `arules`); saves frequent itemsets, rules CSVs, and scatter plot.
- Time series: univariate AirPassengers and exogenous Delhi Climate; saved models and forecast outputs.
- Gradio: three tabs (income classifier, house-price regressor, AirPassengers forecast) loading saved models.

## Outputs & documentation
- Each task has: executed notebook, figures, task README with embedded graphics, and `assignment.script` (talk track).
- Gradio demo: run `python Assignment 5/PyCaret/gradio-demos/gradio_demo.py` inside `.venv` after notebooks save models.
