# AutoGluon Time Series / Chronos — not executed

- Intended tasks: forecasting indepth and chronos zero-shot tutorials on a small series.
- Status: Not executed in the current `.venv`. Installing `autogluon.timeseries` previously caused repeated kernel crashes (segfault) when running even a minimal sinusoid example.
- How to run later: isolate into a clean env, install `autogluon.timeseries==1.1.1`, run on a tiny series with short `time_limit`, and capture outputs. Avoid mixing with the current `.venv` used for other components.
