import streamlit as st
import requests

st.title("📊 Workforce Prediction")

Emp_2018 = st.number_input("Employees 2018")
Emp_2019 = st.number_input("Employees 2019")
Emp_2020 = st.number_input("Employees 2020")
Emp_2021 = st.number_input("Employees 2021")
Emp_2022 = st.number_input("Employees 2022")
Emp_2023 = st.number_input("Employees 2023")
Emp_2024 = st.number_input("Employees 2024")

if st.button("Predict"):
    try:
        response = requests.post(
            "https://workforce-prediction-api.onrender.com/predict", 
            json={
                "Emp_2018": Emp_2018,
                "Emp_2019": Emp_2019,
                "Emp_2020": Emp_2020,
                "Emp_2021": Emp_2021,
                "Emp_2022": Emp_2022,
                "Emp_2023": Emp_2023,
                "Emp_2024": Emp_2024
            }
        )

        result = response.json()

        st.write(result)

        st.success(f"Predicted Employees (2025): {result['predicted_2025']}")

    except Exception as e:
        st.error(f"Error: {e}")
