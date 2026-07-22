import streamlit as st
from utils.ai_helper import get_gemini_route_advice

st.title("🤖 Gemini 2.0 AI Route & Fare Estimator")

api_key = st.text_input("Enter Gemini API Key:", type="password")
col1, col2 = st.columns(2)
with col1:
    orig = st.text_input("Pickup Point:", "Sargodha")
with col2:
    dest = st.text_input("Drop Point:", "Lahore")

v_class = st.selectbox("Vehicle Type:", ["Car", "Hiace", "Bike", "Bus"])

if st.button("Generate AI Optimization Report"):
    if api_key:
        advice = get_gemini_route_advice(api_key, orig, dest, v_class)
        st.write(advice)
    else:
        st.warning("Please provide Gemini API key for live AI generation. (Showing Rule-Based Fallback)")
        st.info(f"💡 *Estimated Distance ({orig} to {dest}):* ~160 km\n* *Suggested Fair Fare:* PKR 1,150 / seat\n* *Safety Status:* Clear via M-2 Motorway.")
