import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/predict"
st.title("Insurance Premium Category Prediction")
st.markdown("Enter you detail below....")

age = st.number_input("Age", value = 30, min_value = 1, max_value = 120)
weight = st.number_input("Weight", value = 50.00, max_value = 300.0, min_value = 1.0)
height = st.number_input("Height", value = 1.45, min_value = 1.0, max_value = 2.5)
income_lpa = st.number_input("Income_LPA", value = 3.50, min_value = 0.00)
smoker = st.selectbox("Smoker", [True, False])
city = st.text_input("City", value = "Mumbai")
occupation = st.selectbox("Occupation", ["Manager", "Engineer", "Doctor", "Teacher", "Businessman", "Accountant", "Lawyer", "Scientist", "Designer", "Developer"])

if st.button("Predict premium category"):
    input_data = {
        "age" : age,
        "weight" : weight,
        "height" : height,
        "income_lpa" : income_lpa,
        "smoker" : smoker,
        "city" : city,
        "occupation" : occupation
    }
    try:
        response = requests.post(API_URL, json = input_data)
        if response.status_code == 200:
            result = response.json()
            st.success(f"Predicted Insurance Category : **{result["response"]}**")
        else:
            st.error(f"API Error : {response.status_code} - {response.text}")
            
    except requests.exceptions.ConnectionError:
        st.error("Could not connect to fastapi server. Make sure its run on the port 8000")