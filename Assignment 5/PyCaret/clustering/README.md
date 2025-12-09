# Clustering (Wine Quality features)

- Data: `../data/winequalityN.csv`, drop `quality` column to cluster on physicochemical features.
- Flow: load -> `setup(..., use_gpu=False, normalize=True)` -> `create_model('kmeans')` -> plots (Elbow, Silhouette, t-SNE) -> `assign_model` -> `save_model` (`clustering_wine_model`).
- Outputs (already generated): `Elbow Plot.png`, `Silhouette Plot.png`, `Cluster t-SNE (3d).png`, and `clustering_wine_model.pkl`.
- Visuals: ![Elbow](Elbow%20Plot.png) ![Silhouette](Silhouette%20Plot.png) ![Cluster t-SNE](Cluster%20t-SNE%20(3d).png)
- Env/run: Python 3.11 `.venv`, `pycaret==3.3.0`; run `clustering_pycaret.ipynb` top-to-bottom. Low-code approach vs manual feature scaling/cluster selection in other methodologies.
