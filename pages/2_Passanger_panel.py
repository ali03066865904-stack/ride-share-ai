import streamlit as st
import pandas as pd

st.set_page_config(page_title="Passenger & Mid-Route Matching", page_icon="🎒", layout="wide")

st.title("🎒 Passenger Booking & Ride Matching Engine")
st.subheader("Search running vehicles or broadcast your pickup request along the route")

# Session state initialization for requests
if 'passenger_requests' not in st.session_state:
    st.session_state.passenger_requests = [
        {"name": "Ali Raza", "pickup": "Sahiwal Bypass", "destination": "Lahore", "seats": 1, "status": "Looking for Ride 🟡"}
    ]

if 'rides' not in st.session_state:
    st.session_state.rides = [
        {"id": "RIDE-101", "driver": "Muhammad Saleem", "phone": "0300-1234567", "vehicle": "Car 🚗", "origin": "Sahiwal", "destination": "Lahore", "seats": 2, "fare": 1200}
    ]

tab1, tab2 = st.tabs(["🔍 Search Active Vehicles", "📢 Broadcast My Pickup Request (Passenger to Driver)"])

with tab1:
    st.markdown("### Active Inter-City & Mid-Route Vehicles")
    for r in st.session_state.rides:
        st.info(f"🚗 *{r['vehicle']}* | Driver: {r['driver']} ({r['phone']}) | Route: {r['origin']} ➔ {r['destination']} | Seats Left: {r['seats']} | Fare: PKR {r['fare']}")
        if st.button(f"Book Seat ({r['id']})", key=r['id']):
            if r['seats'] > 0:
                r['seats'] -= 1
                st.success(f"✅ Seat booked successfully on {r['vehicle']}!")
            else:
                st.error("❌ No seats available!")

with tab2:
    st.markdown("### 📢 Passenger Ride Request Broadcast")
    st.write("Are you waiting mid-route (e.g., 10-15km away)? Broadcast your pickup request so passing drivers can accept you!")
    
    with st.form("passenger_broadcast_form"):
        p_name = st.text_input("Your Full Name", "Ahmad Khan")
        p_phone = st.text_input("Your Phone Number", "0301-9876543")
        p_pickup = st.text_input("Your Current Location / Pickup Point", "Chichawatni Interchange (15km from Sahiwal)")
        p_dest = st.selectbox("Your Destination City", ["Lahore", "Multan", "Faisalabad", "Rawalpindi"])
        p_seats = st.slider("Required Seats", 1, 4, 1)
        
        submitted = st.form_submit_button("🚀 Broadcast Request to Nearby Drivers")
        if submitted:
            new_req = {"name": p_name, "pickup": p_pickup, "destination": p_dest, "seats": p_seats, "status": "Pending Driver Acceptance 🟡"}
            st.session_state.passenger_requests.append(new_req)
            st.success("✅ Broadcast Sent! Nearby drivers on this route will now see your request on their dashboard.")

st.divider()
st.markdown("### 📋 Live Requests Board")
df_reqs = pd.DataFrame(st.session_state.passenger_requests)
st.dataframe(df_reqs, use_container_width=True)
