import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open("crop_recommendation_model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("🌱 Crop Recommendation System")

st.write("Enter soil and climate details below to get the best crop suggestion.")

# Input fields
N = st.number_input("Nitrogen (N)", min_value=0, max_value=200, value=50)
P = st.number_input("Phosphorus (P)", min_value=0, max_value=200, value=50)
K = st.number_input("Potassium (K)", min_value=0, max_value=200, value=50)
temperature = st.number_input("Temperature (°C)", min_value=0.0, max_value=50.0, value=25.0)
humidity = st.number_input("Humidity (%)", min_value=0.0, max_value=100.0, value=60.0)
ph = st.number_input("pH Value", min_value=0.0, max_value=14.0, value=6.5)
rainfall = st.number_input("Rainfall (mm)", min_value=0.0, max_value=300.0, value=100.0)

# Predict button
if st.button("Recommend Crop"):
    input_data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
    prediction = model.predict(input_data)
    st.success(f"✅ Recommended Crop: **{prediction[0]}**")
import streamlit as st

st.title("🌱 Crop Recommendation System")
st.write("This is a demo Streamlit app. Soon we’ll add ML model predictions here!")

# Example input form
nitrogen = st.number_input("Nitrogen (N)", min_value=0, max_value=200, value=50)
phosphorus = st.number_input("Phosphorus (P)", min_value=0, max_value=200, value=50)
potassium = st.number_input("Potassium (K)", min_value=0, max_value=200, value=50)
temperature = st.number_input("Temperature (°C)", value=25.0)
humidity = st.number_input("Humidity (%)", value=60.0)
ph = st.number_input("pH value", min_value=0.0, max_value=14.0, value=6.5)
rainfall = st.number_input("Rainfall (mm)", value=100.0)

if st.button("Recommend Crop"):
    st.success("🚜 Recommended Crop: Wheat (placeholder)")

