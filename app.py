import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load("crop_recommendation_model.pkl")

# Streamlit app title
st.title("🌱 Crop Recommendation System")

st.write("Enter the soil and climate conditions below to get the best crop recommendation.")

# User input fields
N = st.number_input("Nitrogen (N)", min_value=0.0, step=1.0)
P = st.number_input("Phosphorus (P)", min_value=0.0, step=1.0)
K = st.number_input("Potassium (K)", min_value=0.0, step=1.0)
temperature = st.number_input("Temperature (°C)", step=0.1)
humidity = st.number_input("Humidity (%)", step=0.1)
ph = st.number_input("Soil pH", step=0.1)
rainfall = st.number_input("Rainfall (mm)", step=0.1)

# Predict button
if st.button("Recommend Crop"):
    try:
        # Prepare input data
        input_data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
        
        # Predict crop
        prediction = model.predict(input_data)
        
        # Show result
        st.success(f"🌾 Recommended Crop: **{prediction[0]}**")
    except Exception as e:
        st.error(f"⚠️ An error occurred: {e}")

