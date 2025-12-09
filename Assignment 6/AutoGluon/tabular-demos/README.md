# AutoGluon Tabular Demos (Component B)

Covers quick-start classification/regression, a small in-depth/tuning example, multimodal tabular (text+cat+num), and automatic feature engineering. Runs are configured for small samples/time limits to ensure quick execution; models are deleted after each section to keep the repo light. Executed notebook with outputs is checked in.

Files
- `tabular_autogluon_demos.ipynb`: executed notebook with all sections.
- `assignment.script`: 1–2 min talk track.

Notes
- Uses built-in/synthetic datasets; no Kaggle data committed.
- `SAMPLE_FRAC_CLS/REG` and `TIME_LIMIT` can be set via env vars; defaults are small (0.2 frac, 60s).
- Model directories are cleaned up after each section; only outputs remain.
