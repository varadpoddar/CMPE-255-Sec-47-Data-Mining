# CMPE-255-Sec-47-Data-Mining

Course repository for data mining / applied ML assignments (CMPE-255, Section 47). Each assignment includes a CRISP-DM style walkthrough, Colab-ready notebooks, and supporting assets.

## Layout
- `Assignment 1/`: Mental health survey analysis with executed notebook, figures, and detailed README.
- `colab_starter/`: Reusable Colab-ready starter kit (template notebook + requirements) to bootstrap future assignments.

## How to use
1) Open the relevant assignment folder and follow its README for dataset-specific steps.
2) For new assignments, copy `colab_starter/notebook_template.ipynb` and its `requirements.txt`, point `DATA_PATH`/`TARGET_COL` to your dataset, run top-to-bottom, then document outputs in the assignment README.

## Notes
- Keep figures under each assignment’s `figures/` folder and reference them from the README.
- Prefer lightweight models first; expand with tuning only if compute allows.
