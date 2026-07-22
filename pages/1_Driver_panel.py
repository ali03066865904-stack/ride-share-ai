import streamlit as st
from utils.fare_calculator import calculate_estimated_fare

st.title("👨‍✈️ Driver Dashboard & Route Publisher")

with st.form("driver_form"):
    driver_name = st.text_input("Driver Full Name:", "Muhammad Saleem")
    phone = st.text_input("Contact Number:", "0300-1234567")
    vehicle = st.selectbox("Vehicle Category:", ["Car / کار", "Bike / موٹر سائیکل", "Carry Dabba / کیری ڈبہ", "Hiace / ہائی ایس", "Shalimar Bus / شالیمار بس"])
    
    col1, col2, col3 = st.columns(3)
    with col1:
        origin = st.text_input("Starting City:", "Sahiwal")
    with col2:
        mid_stop = st.text_input("Mid Route Stop (10-15km Pickup):", "Sargodha")
    with col3:
        destination = st.text_input("Final City:", "Lahore")
        
    seats = st.slider("Available Seats:", 1, 40, 3)
    submitted = st.form_submit_button("🚀 Broadcast Live Route GPS")

if submitted:
    est_fare = calculate_estimated_fare(vehicle, 160, seats)
    st.success(f"✅ Route Live! Dynamic Fare Calculated: PKR {est_fare} per seat.")
