# Assignment 2: VS Code + GitHub Copilot + GPT-Engineer Workflow

Use this assignment to showcase the power of AI-assisted development in VS Code with GitHub Copilot (code and chat) plus GPT-Engineer for rapid project scaffolding. Record a screencast demonstrating key use cases; add screenshots/video to this folder when ready.

## Goals
- Install and configure VS Code, GitHub Copilot, and Copilot Chat.
- Use Copilot for coding tasks (authoring functions, refactoring, unit tests, full feature stubs).
- Run GPT-Engineer to generate a small application from a prompt; explore/verify the generated code in VS Code.
- Capture a screencast demonstrating the workflow; commit generated code and your media assets to the repo.

## Prerequisites
- VS Code installed: https://code.visualstudio.com
- GitHub account with Copilot access.
- Python 3.9+ (for GPT-Engineer) and `pipx` or `pip`.
- Git installed and configured for this repo.

## Setup
1) Install VS Code.
2) Install the GitHub Copilot extension (code completion) from the Marketplace.
3) Install the GitHub Copilot Chat extension: https://marketplace.visualstudio.com/items?itemName=GitHub.copilot-chat
4) Sign in to GitHub within VS Code and enable Copilot for the workspace.
5) (Optional) Pin the Copilot Chat view: View → Appearance → Primary/Secondary Side Bar → Chat.

## GPT-Engineer (project generator)
1) Install:
```bash
pip install gpt-engineer
# or: pipx install gpt-engineer
```
2) Initialize a project:
```bash
gpt-engineer my-app
cd my-app
```
3) Write your prompt in `prompt` (text file created by GPT-Engineer) describing the app you want.
4) Run the generator:
```bash
gpt-engineer .
```
5) Open the generated project in VS Code and explore with Copilot/Copilot Chat.

## Suggested screencast flow
Record your screen (and optionally mic) while walking through these steps:
1) **Setup**: Show VS Code, Copilot enabled, Copilot Chat panel open.
2) **Writing functions**: Prompt Copilot Chat to draft a function or class; accept/modify inline suggestions.
3) **Refactoring**: Highlight code and ask Copilot Chat to refactor or simplify; apply the patch.
4) **Unit tests**: Use Copilot Chat to write unit tests for a function/module; run tests in the terminal.
5) **Full feature**: Request Copilot Chat to scaffold a small feature (e.g., API endpoint or React component).
6) **GPT-Engineer**: Run GPT-Engineer on a fresh prompt, then open the generated code in VS Code; ask Copilot Chat to summarize and suggest improvements.
7) **Wrap-up**: Mention how Copilot and GPT-Engineer accelerated development; note any manual fixes you made.

## Where to place artifacts
- Screencast video: add to `Assignment 2/` (e.g., `copilot-demo.mp4`).
- Screenshots: add to `Assignment 2/` (e.g., `copilot-chat.png`, `gpt-engineer-output.png`).
- Generated code: commit the GPT-Engineer project (inside `Assignment 2/` or separate folder) and any refactored examples you showcased.

## Submission checklist
- [x] VS Code + Copilot + Copilot Chat installed and signed in.
- [x] GPT-Engineer installed; project generated from your prompt.
- [x] Screencast recorded covering coding, refactoring, tests, full feature, and GPT-Engineer demo.
- [x] Screenshots added (optional but recommended).
- [x] Generated code and this README committed to the repo.

## Prompt tips
- Be explicit about inputs/outputs and constraints (e.g., “Return JSON with keys x,y,z; avoid global state; prefer async/await”).
- Ask Copilot Chat to explain before applying large changes.
- For tests, specify framework (e.g., `pytest`) and edge cases you care about.

## Notes
- This repo already contains `Assignment 1` (mental health survey analysis) and a reusable `colab_starter/` kit; reuse the same documentation style here.
- Keep compute modest: start with small prompts and incremental runs. Save checkpoints of GPT-Engineer outputs before regenerating.
