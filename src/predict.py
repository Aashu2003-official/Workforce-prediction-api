import os
import joblib
import pandas as pd
from src.train import train

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "models", "model.pkl")

model = None

def load_model():
    global model

    if model is None:
        if not os.path.exists(MODEL_PATH):
            print("Model not found. Training...")
            train()

        model = joblib.load(MODEL_PATH)

    return model


def predict_workforce(features):
    model = load_model()

    import pandas as pd

    df = pd.DataFrame([{
        "Emp_2018": features[0],
        "Emp_2019": features[1],
        "Emp_2020": features[2],
        "Emp_2021": features[3],
        "Emp_2022": features[4],
        "Emp_2023": features[5],
        "Emp_2024": features[6],
    }])

    prediction = model.predict(df)

    return float(prediction[0])