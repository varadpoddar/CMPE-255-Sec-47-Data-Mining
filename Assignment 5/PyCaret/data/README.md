# Data placement for Assignment 5 (PyCaret)

Create this `data/` directory and place the downloaded Kaggle CSVs here. Default notebook paths use `../data/<filename>`; adjust paths in notebooks if you store files elsewhere.

Required files:
- `adult.csv` (Adult Census Income)
- `iris.csv` (Iris)
- `kc_house_data.csv` (King County House Sales)
- `winequalityN.csv` (Wine Quality; drop `quality` for clustering)
- `creditcard.csv` (Credit Card Fraud)
- `Groceries_dataset.csv` (Groceries basket; used for association rules via mlxtend)
- `AirPassengers.csv` (Airline Passengers)
- `DailyDelhiClimateTrain.csv` (Daily Delhi Climate)

All notebooks expect these exact filenames under `Assignment 5/PyCaret/data/`. Keeping paths consistent ensures executed notebooks and the Gradio app load data/models without edits.
