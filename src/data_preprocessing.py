import pandas as pd

def load_data(file_path):
    try:
        data = pd.read_csv(file_path)
        print(f"Data loaded successfully from {file_path}")
        return data
    except Exception as e:
        print(f"An error occurred while loading data: {e}")
        return None
def preprocess_data(data):
    try:
        if "Company" in data.columns:
            data = data.drop(columns=["Company"])
        data = data.ffill()
        
        print("Data preprocessing completed successfully.")
        return data
    except Exception as e:
        print(f"An error occurred during data preprocessing: {e}")
        return None