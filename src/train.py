from src.data_preprocessing import load_data, preprocess_data
from src.feature_engineering import select_features
from sklearn.ensemble import RandomForestRegressor
import joblib
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

file_path = os.path.join(BASE_DIR, "data", "companies data.csv")


def train():
    df = load_data(file_path)
    df = preprocess_data(df)
    
    x, y = select_features(df)

    model = RandomForestRegressor()
    model.fit(x, y)

    joblib.dump(model, "models/model.pkl")

if __name__ == "__main__":
    train()