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

