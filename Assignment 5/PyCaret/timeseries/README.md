# Time Series (AirPassengers + Delhi Climate Exogenous)

- Data: `../data/AirPassengers.csv` (monthly passengers), `../data/DailyDelhiClimateTrain.csv` (daily weather).
- Flow:
  - Univariate: setup with `Passengers`, fh=24, seasonal_period=12, `use_gpu=False` -> `compare_models`/`tune_model` -> forecast -> save model (`ts_airpassengers_model`).
  - Exogenous: setup with `meantemp` target + remaining covariates, fh=30, seasonal_period=7, `use_gpu=False`, `enforce_exogenous=True` -> `compare_models`/`tune_model` -> forecast/diagnostics -> provide recent exogenous values for prediction (`X=future_exog`) -> save model (`ts_delhi_climate_model`).
- Outputs: models saved (`ts_airpassengers_model.pkl`, `ts_delhi_climate_model.pkl`) and forecast/diagnostic plots saved in the notebook directory.
- Run: execute `timeseries_pycaret.ipynb` end-to-end; dash comm warnings during plotting can be ignored. GPU is disabled for local compatibility. PyCaret TS provides rapid model comparison vs the custom ARIMA/Prophet work in earlier assignments, with minimal manual feature crafting.
