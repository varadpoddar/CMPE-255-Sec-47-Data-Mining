# Apache Beam Data Engineering Exercise

This assignment demonstrates Apache Beam in Colab with core transforms and patterns: composite transforms, pipeline I/O, `ParDo`, windowing, `Map`, `Filter`, `Partition`, and Beam ML (sklearn RunInference). You will run the provided notebook, capture a code walk-through video, and add screenshots/video artifacts to this folder. The video is required—explain inputs, transforms, outputs, and the ML inference step.

## What you need
- Google Colab account.
- Python 3.10+ (Colab default) and internet to install `apache-beam`.
- Source references (explore as needed):
  - Beam interactive Colab: https://colab.research.google.com/github/apache/beam/blob/master/examples/notebooks/interactive-overview/getting-started.ipynb
  - Beam Playground: https://beam.apache.org/get-started/try-beam-playground
  - Interactive overview: https://beam.apache.org/get-started/an-interactive-overview-of-beam/
  - Beam ML: https://beam.apache.org/documentation/ml/about-ml/
  - RunInference (sklearn): https://beam.apache.org/documentation/transforms/python/elementwise/runinference-sklearn/

## Files in this folder
- `beam_exercise.ipynb`: Colab-ready notebook covering Beam setup, `Map`/`Filter`, `ParDo`, composite transform, partitioning, windowing, I/O, and a working Beam ML RunInference (sklearn) example.
- `README.md`: (this file) instructions and checklist.
- _(Add your own)_ screencast video (`beam-demo.mp4`) and screenshots after recording.

## Executed run (latest)
- Beam version: 2.56.0 (running in `.venv` Python 3.11).
- Temp output directory: `/var/folders/86/nr8r5c99659ggl44tw4xs62h0000gn/T/tmpgz80gbnv`.
- Partition demo produced files like `beam_output-00000-of-00001`.
- Windowed counts emitted `PCollection` objects per 60s windows (see notebook output).
- Text sink sample content:
  - `{'user': 'alice', 'score': 5, 'ts': 0, 'tag': 'fail'}`
  - `{'user': 'bob', 'score': 7, 'ts': 10, 'tag': 'pass'}`
  - `{'user': 'dave', 'score': 9, 'ts': 80, 'tag': 'pass'}`
  - `{'user': 'eve', 'score': 4, 'ts': 95, 'tag': 'fail'}`
- Sklearn RunInference predictions (tiny `LogisticRegression`): `0.0`, `1.0`, `1.0`.

## Workflow
1) Open `beam_exercise.ipynb` in Colab. If prompted, run the first cell to install dependencies.
2) Execute cells top-to-bottom:
   - Quick data intro and Beam setup.
   - `Map`, `Filter`, `ParDo` basics.
   - Composite transform (class-based transform combining multiple steps).
   - Partitioning example (even/odd split).
   - Windowing with `FixedWindows` and aggregation.
   - Pipeline I/O using `WriteToText` to a temp path.
   - Beam ML `RunInference` with a tiny sklearn model (LogisticRegression) to show end-to-end inference.
3) Capture a short walk-through video explaining inputs, transforms, outputs, windowing/partition behavior, file outputs, and the ML inference step.
4) Add video/screenshots to this folder and commit them.

## Submission checklist
- [x] `beam_exercise.ipynb` executed (outputs visible in `beam_exercise_executed.ipynb`).
- [ ] Video walkthrough added (e.g., `beam-demo.mp4`) covering transforms and the sklearn RunInference step.
- [ ] Screenshots added (optional).
- [x] Key outputs (sample text output, console logs) verified.

## Tips
- Keep window sizes small (e.g., 60s) and data volumes tiny to fit Colab quotas.
- For Beam ML `RunInference`, start with a tiny scikit-learn model (e.g., `LogisticRegression`) to avoid heavy downloads.
- If you need live examples, the Beam Playground has many runnable snippets for reference.

## Video walkthrough script (draft)
1) **Intro & goal (30s)**  
   - State that the exercise demonstrates core Apache Beam transforms plus a small sklearn RunInference example in Colab/local `.venv`.
2) **Environment (30s)**  
   - Mention Beam 2.56.0, Python 3.11 `.venv`, notebook structure, and that dependencies are prelisted in `requirements.txt`.
3) **Basics: Map/Filter/ParDo (1 min)**  
   - Show the first transforms that square numbers, filter evens, and use `ParDo` for custom logic. Call out the printed results.
4) **Composite transform & partition (1 min)**  
   - Explain the class-based composite transform that tags evens/odds and writes to temporary files. Point to the `beam_output-00000-of-00001` file and show its contents.
5) **Windowing demo (1 min)**  
   - Describe the 60s `FixedWindows` over toy events and the aggregated counts; mention the `PCollection` output and how windowing groups by event time.
6) **Pipeline I/O (30s)**  
   - Highlight writing JSON lines to a temp directory; display the sample records (alice, bob, dave, eve) from the executed run.
7) **Beam ML RunInference (1 min)**  
   - Walk through the tiny `LogisticRegression` model saved with joblib, the `SklearnModelHandlerNumpy`, and the predictions `0.0, 1.0, 1.0`.
8) **Wrap-up (30s)**  
   - Summarize what was covered, remind to add the video file and screenshots to this folder, and note any warnings (e.g., interactive viz dependency notice).
