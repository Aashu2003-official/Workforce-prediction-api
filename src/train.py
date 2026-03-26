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

    X, y = select_features(df)

    model = RandomForestRegressor()
    model.fit(X, y)

    model_dir = os.path.join(BASE_DIR, "models")
    os.makedirs(model_dir, exist_ok=True)

    model_path = os.path.join(model_dir, "model.pkl")
    joblib.dump(model, model_path)

    print("Model trained and saved!")

if __name__ == "__main__":
    train()