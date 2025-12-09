# AutoGluon Image Classification (synthetic sanity check)

- **Notebook**: `image_cls_autogluon.ipynb` (runs on tiny synthetic dataset).
- **Dataset**: 8 random 64×64 RGB images split into two classes (`cat`, `dog`) under `data/train/`.
- **Setup**: `MultiModalPredictor` (image classification) with `time_limit=30s`, small sample to validate pipeline.
- **Results**: On the tiny hold-out set, `roc_auc=0.5` (essentially random on 2 samples) — expected given the random images and tiny split; demonstrates pipeline runs end-to-end on this env.
- **Artifacts**: Models saved to `ag_image_models/` (git-ignored); dataset under `data/` (git-ignored).
