import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load("crop_recommendation_model.pkl")

# Title
st.set_page_config(page_title="🌱 Crop Recommendation System", layout="centered")
st.title("🌱 Crop Recommendation System")
st.write("Enter soil and climate conditions to get the best crop recommendation.")

# Sidebar inputs
st.sidebar.header("Soil & Climate Inputs")
N = st.sidebar.slider("Nitrogen (N)", 0, 200, 50)
P = st.sidebar.slider("Phosphorus (P)", 0, 200, 40)
K = st.sidebar.slider("Potassium (K)", 0, 200, 40)
temperature = st.sidebar.slider("Temperature (°C)", 0, 50, 25)
humidity = st.sidebar.slider("Humidity (%)", 0, 100, 50)
ph = st.sidebar.slider("Soil pH", 0.0, 14.0, 6.5)
rainfall = st.sidebar.slider("Rainfall (mm)", 0.0, 300.0, 100.0)

# Crop images dictionary
crop_images = {
    "rice": "https://upload.wikimedia.org/wikipedia/commons/6/65/Rice_plants.jpg",
    "wheat": "https://upload.wikimedia.org/wikipedia/commons/4/41/Wheat_close-up.jpg",
    "maize": "https://upload.wikimedia.org/wikipedia/commons/2/21/Maize_cob.jpg",
    "sugarcane": "https://upload.wikimedia.org/wikipedia/commons/3/36/Sugarcane.jpg",
    # Add more crops here
}

# Predict crop instantly
try:
    input_data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
    prediction = model.predict(input_data)
    crop = prediction[0]

    st.success(f"🌾 Recommended Crop: **{crop}**")

    # Display crop image if available
    if crop.lower() in crop_images:
        st.image(crop_images[crop.lower()], caption=crop, use_column_width=True)
except Exception as e:
    st.error(f"⚠️ An error occurred: {e}")

