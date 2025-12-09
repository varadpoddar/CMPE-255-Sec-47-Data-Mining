# Assignment 8 — Clustering (Colab-first)

One Colab per component. Run each in Colab (GPU/TPU if needed), capture outputs, and record a short walkthrough video. Links below are for reference only; do not commit datasets/checkpoints.

## Components (to be delivered)
1) K-Means clustering **from scratch** — `colabs/kmeans_from_scratch.ipynb` (fetched from reference notebook; requires `sample_data/income.csv` to run in Colab)
2) Hierarchical clustering (library) — `colabs/hierarchical_clustering.ipynb` (executed locally after patching empty-cluster handling)
3) Gaussian mixture models (GMM) — `colabs/gmm_clustering.ipynb`
4) DBSCAN via PyCaret — `colabs/dbscan_pycaret.ipynb`
5) Anomaly detection with PyOD — `colabs/pyod_anomaly.ipynb`
6) Time-series clustering (tslearn) — `colabs/timeseries_clustering.ipynb`
7) Document clustering with LLM embeddings — `colabs/document_clustering_embeddings.ipynb`
8) Image clustering with ImageBind embeddings — `colabs/image_clustering_imagebind.ipynb`
9) Audio clustering with ImageBind embeddings — `colabs/audio_clustering_imagebind.ipynb`

## How to use the Colabs
- Open the notebook in Colab, select GPU runtime if needed.
- Install requirements inside the notebook (pinned where provided).
- Run all cells; ensure charts/tables render. Add screenshots/links to your walkthrough video in the notebook.
- Export executed notebook (with outputs) back to this folder.

## Status
- K-Means: not executed locally (needs `sample_data/income.csv` in Colab).
- Hierarchical: executed locally with patched `find_permutation` to handle empty clusters; outputs saved.
- Remaining: templates added; run in Colab/GPU as needed and save outputs + video links. ImageBind notebooks expect GPU and internet to fetch sample media.
