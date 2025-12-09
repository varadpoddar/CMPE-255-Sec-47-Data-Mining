# CMPE-255-Sec-47-Data-Mining

Course repository for data mining / applied ML assignments (CMPE-255, Section 47). Each assignment includes a CRISP-DM style walkthrough, Colab-ready notebooks, and supporting assets.

## Layout
- `Assignment 1/`: Mental health survey analysis with executed notebook, figures, and detailed README.
- `Assignment 2 (Extra Credit)/`: VS Code + Copilot demo assets (instructions, video placeholders).
- `Apache beam data engineering exercise - Assignment 3/`: Beam pipelines with I/O, windowing, partitioning, and sklearn RunInference.
- `Assignment 4/CRISP-DM/`: House Prices regression case study following CRISP-DM (notebook, figures, script).
- `Assignment 4/SEMMA/`: Adult Income classification case study following SEMMA (notebook, figures, script).
- `Assignment 4/KDD/`: Wine Quality regression case study following KDD (notebook, figures, script).
- `Assignment 5/PyCaret/`: PyCaret 2.3.5 local (GPU where possible) tutorials for classification, regression, clustering, anomaly, association rules, time series, and Gradio demos.
- `Assignment 6/AutoGluon/`: AutoGluon Tabular runs (IEEE fraud, California housing) plus extra credit multimodal/time-series/text/image tasks; executed notebooks with outputs and component-level READMEs.
- `Assignment 7/Unsloth/`: Fine-tuning LLMs with Unsloth (full finetune, checkpoint resume, mental-health chatbot, Ollama export). Local notebooks + notes on Colab credit limits and expected runtime steps.
- `Assignment 8/Clustering/`: Colab-first clustering suite—k-means from scratch, hierarchical, GMM, DBSCAN (PyCaret), PyOD anomaly, time-series (tslearn, TS2Vec), document embeddings, and image/audio embedding templates. Executed locals noted in status; remaining to run in Colab/GPU.
- `colab_starter/`: Reusable Colab-ready starter kit (template notebook + requirements) to bootstrap future assignments.

## How to use
1) Open the relevant assignment folder and follow its README for dataset-specific steps.
2) For new assignments, copy `colab_starter/notebook_template.ipynb` and its `requirements.txt`, point `DATA_PATH`/`TARGET_COL` to your dataset, run top-to-bottom, then document outputs in the assignment README.

## Notes
- Keep figures under each assignment’s `figures/` folder and reference them from the README.
- Prefer lightweight models first; expand with tuning only if compute allows.
