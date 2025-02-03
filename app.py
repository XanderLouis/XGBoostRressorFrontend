import streamlit as st
import requests

# Ensure no trailing slash in base_url
BASE_URL = "http://localhost:8001"

st.title("💸 Insurance Charges Prediction")

with st.form("user_input_form"):
    age = st.number_input("👨 Age:", min_value=0, max_value=120, value=30)
    sex = st.radio("👫 Sex:", ["Female", "Male"], horizontal=True)
    sex = 0 if sex == "Female" else 1  # Convert to int
    bmi = st.number_input("⚖️ BMI:", min_value=0.0, max_value=100.0, value=25.0)
    children = st.slider("👶 Children:", min_value=0, max_value=10, value=0)
    smoker = st.radio("🚬 Smoker:", ["No", "Yes"], horizontal=True)
    smoker = 0 if smoker == "No" else 1  # Convert to int
    region = st.selectbox("📍 Region:", ["Northwest", "Southeast", "Southwest", "Northeast"])

    # One-hot encode region
    data = {
        "age": age,
        "sex": sex,
        "bmi": bmi,
        "children": children,
        "smoker": smoker,
        "northwest": 1 if region == "Northwest" else 0,
        "southeast": 1 if region == "Southeast" else 0,
        "southwest": 1 if region == "Southwest" else 0,
        "northeast": 1 if region == "Northeast" else 0
    }

    submitted = st.form_submit_button("Predict 🚀")

if submitted:
    st.write("🔍 Debug: API Request Payload", data)  # Debugging aid

    try:
        response = requests.post(f"{BASE_URL}/api/predict", json=data)
        response.raise_for_status()
        prediction = response.json().get("predicted_charges", "N/A")
        st.success(f"💸 Predicted Charges: **${prediction:,.2f}**")
    except requests.exceptions.RequestException as e:
        st.error(f"❌ API Error: {e}")


# Run the Streamlit App
# Streamlit run app.py