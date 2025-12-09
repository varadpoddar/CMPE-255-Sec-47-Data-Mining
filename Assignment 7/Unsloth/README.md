# Assignment 7 — Modern AI with Unsloth.ai

This assignment captures Colab notebooks and documentation for Unsloth finetuning tasks. Run the notebooks in Google Colab with GPU. Record a YouTube walkthrough for each use case (code, inputs, outputs) and link it from the README once uploaded.

## Components (Colab1)
1) **Full finetuning (smolLM2 135M)** — `full_finetune_smollm2.ipynb` (full_finetuning=True)
2) **Continued finetuning from custom checkpoint** — `continued_finetune_checkpoint.ipynb`
3) **Mental health chatbot finetune (phi3/similar)** — `mental_health_chatbot.ipynb`
4) **Finetune & export to Ollama** — `finetune_export_ollama.ipynb`

## How to run (Colab)
- Open the notebook in Colab, select GPU runtime.
- Install deps inside Colab (`pip install -q unsloth` plus tutorial-specific extras).
- Provide/point to your dataset and (for continued training) your checkpoint path.
- Execute all cells; verify training logs, evaluation, and inference samples render.
- Export artifacts as instructed (e.g., Ollama export).
- Record a 1–2 minute video per notebook showing code, data prep, training, and inference/output.

## Local attempt & limitation
- Attempted `pip install unsloth` in local `.venv` (Mac/ARM, CPU-only). Installation failed building `xformers` (`clang++: unsupported option -fopenmp`) and would be impractical without GPU.
- Colab credits are currently exhausted, so runs must be done when GPU credits are available (Colab Pro/Kaggle GPU/other GPU).
- Proceed by running the provided notebooks in Colab (or any GPU environment) and capturing outputs/videos there.

## Deliverables
- Executed notebooks with outputs saved to the repo.
- Video links (YouTube) per use case (add to each notebook/README).
- No raw datasets or checkpoints committed; keep paths external or mounted in Colab.
