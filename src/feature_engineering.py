def select_features(df):
    X = df.drop(columns=["Emp_2025"])
    y = df["Emp_2025"]
    return X, y