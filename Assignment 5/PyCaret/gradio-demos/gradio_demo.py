import gradio as gr
import pandas as pd
from pathlib import Path
from pycaret.classification import load_model as load_classifier, predict_model as predict_cls
from pycaret.regression import load_model as load_regressor, predict_model as predict_reg
from pycaret.time_series import load_model as load_ts, predict_model as predict_ts

# Resolve model paths relative to this file
BASE = Path(__file__).resolve().parent.parent
CLASSIFIER_PATH = str(BASE / "classification-binary" / "binary_income_model")
REGRESSOR_PATH = str(BASE / "regression" / "regression_kc_house_model")
TS_UNI_PATH = str(BASE / "timeseries" / "ts_airpassengers_model")

clf = load_classifier(CLASSIFIER_PATH)
reg = load_regressor(REGRESSOR_PATH)
ts_uni = load_ts(TS_UNI_PATH)


def predict_income(age, hours_per_week, education_num, capital_gain, capital_loss):
    data = pd.DataFrame(
        [
            {
                "age": age,
                "hours.per.week": hours_per_week,
                "education.num": education_num,
                "capital.gain": capital_gain,
                "capital.loss": capital_loss,
            }
        ]
    )
    preds = predict_cls(clf, data=data)
    return preds["Label"].iloc[0], float(preds["Score"].iloc[0])


def predict_house_price(bedrooms, bathrooms, sqft_living, sqft_lot, floors, waterfront):
    data = pd.DataFrame(
        [
            {
                "bedrooms": bedrooms,
                "bathrooms": bathrooms,
                "sqft_living": sqft_living,
                "sqft_lot": sqft_lot,
                "floors": floors,
                "waterfront": waterfront,
            }
        ]
    )
    preds = predict_reg(reg, data=data)
    return float(preds["prediction_label"].iloc[0])


def forecast_passengers(steps):
    fh = list(range(1, int(steps) + 1))
    forecast_df = predict_ts(ts_uni, fh=fh)
    return forecast_df.to_markdown(index=False)


cls_demo = gr.Interface(
    fn=predict_income,
    inputs=[
        gr.Number(label="Age", value=35),
        gr.Number(label="Hours per week", value=40),
        gr.Number(label="Education num", value=10),
        gr.Number(label="Capital gain", value=0),
        gr.Number(label="Capital loss", value=0),
    ],
    outputs=[gr.Textbox(label="Predicted income"), gr.Number(label="Score")],
    title="Income Classifier Demo",
    description="Uses the saved PyCaret binary classifier.",
)

reg_demo = gr.Interface(
    fn=predict_house_price,
    inputs=[
        gr.Number(label="Bedrooms", value=3),
        gr.Number(label="Bathrooms", value=2),
        gr.Number(label="Sqft living", value=1800),
        gr.Number(label="Sqft lot", value=5000),
        gr.Number(label="Floors", value=1),
        gr.Radio(label="Waterfront", choices=[0, 1], value=0),
    ],
    outputs=gr.Number(label="Predicted price"),
    title="House Price Regressor Demo",
    description="Uses the saved PyCaret regression model.",
)

ts_demo = gr.Interface(
    fn=forecast_passengers,
    inputs=[gr.Number(label="Forecast horizon (months)", value=12)],
    outputs=gr.Textbox(label="Forecast table"),
    title="AirPassengers Forecast Demo",
    description="Uses the saved PyCaret time-series model (univariate).",
)

demo = gr.TabbedInterface(
    [cls_demo, reg_demo, ts_demo],
    tab_names=["Income Classifier", "House Price Regressor", "AirPassengers Forecast"],
)

if __name__ == "__main__":
    demo.launch()
