# AutoGluon Image Zero-Shot (CLIP) — not executed

- Intended task: run the CLIP zero-shot tutorial on a small set of images to demonstrate label-free classification.
- Status: Not executed in the current `.venv` to avoid instability from large model downloads on CPU-only Mac. Prior heavy-model attempts (timeseries) have crashed the kernel.
- How to run later (suggested): create a tiny folder of 2–4 images and a label set, then use `MultiModalPredictor` with `problem_type='zero_shot_image_classification'` as in the official tutorial; keep `time_limit` small.
