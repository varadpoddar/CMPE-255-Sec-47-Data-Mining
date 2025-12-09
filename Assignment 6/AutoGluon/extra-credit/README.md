# Extra Credit — AutoGluon

## Checklist (status)
- [x] 1.4 Multi-label tabular (tabular-multilabel) — see `multilabel/`
- [x] 1.5 Tabular with GPU preset (tabular-gpu) — see `gpu/` (CPU fallback on Mac)
- [x] 1.6 Text: sentiment + similarity (beginner_text), multilingual finetune, NER — see `text/` (synthetic sentiment + matching executed)
- [x] 1.7 Text similarity matching — covered via `semantic-matching/` (text-to-text executed)
- [x] 1.8 Image classification (synthetic sanity) — see `image-classification/` (tiny random set); CLIP zero-shot and object detection not executed due to environment constraints (documented).
- [ ] 1.9 Image segmentation / document-PDF classification — not executed; documented.
- [x] 1.10 Semantic matching: text-to-text executed; image/text variants not executed (documented).
- [x] 1.11 Multimodal use cases: text+tabular executed in `multimodal-tabular/`; image+text table & multimodal NER not executed (documented).
- [ ] 1.12 Time series: forecasting/chronos not executed; repeated kernel crashes in current `.venv` after installing `autogluon.timeseries` (documented).

Approach: executed what the current `.venv` could handle on tiny samples/time limits; remaining heavy CV/time-series items are stubbed and documented with environment limits. Model artifacts remain git-ignored to keep the repo light.

We will execute each notebook on small samples where possible, save outputs, and document learnings in sub-READMEs. Models/artifacts will be ignored to keep the repo light.
