import streamlit as st
import requests

st.title("📊 Workforce Prediction")

emp_2018 = st.number_input("Employees 2018")
emp_2019 = st.number_input("Employees 2019")
emp_2020 = st.number_input("Employees 2020")
emp_2021 = st.number_input("Employees 2021")
emp_2022 = st.number_input("Employees 2022")
emp_2023 = st.number_input("Employees 2023")
emp_2024 = st.number_input("Employees 2024")

if st.button("Predict"):
    response = requests.post(
        "https://ai-workforce-prediction.onrender.com/predict",
        json={
            "Emp_2018": emp_2018,
            "Emp_2019": emp_2019,
            "Emp_2020": emp_2020,
            "Emp_2021": emp_2021,
            "Emp_2022": emp_2022,
            "Emp_2023": emp_2023,
            "Emp_2024": emp_2024
        }
    )

    result = response.json()
    st.success(f"Predicted Employees (2025): {result['predicted_2025']}")