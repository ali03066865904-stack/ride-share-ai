import streamlit as st
from google import genai

st.set_page_config(page_title="RoutePool AI - Smart Ride Sharing", page_icon="🚗", layout="wide")

st.title("🚗 RoutePool AI — Smart Ride Sharing & Fare Assistant")
st.caption("Post rides, search available seats, and get AI-powered fair fare estimates!")

# Setup API Key securely
api_key = st.sidebar.text_input("Enter Gemini API Key:", type="password")

if "rides" not in st.session_state:
    st.session_state.rides = [
        {"driver": "Ali", "from": "Sargodha", "to": "Sahiwal", "vehicle": "Car", "seats": 3, "fare": 800},
        {"driver": "Usman", "from": "Lahore", "to": "Islamabad", "vehicle": "Bike", "seats": 1, "fare": 1200}
    ]

tab1, tab2, tab3 = st.tabs(["📌 Post a Ride", "🔍 Find Rides", "🤖 AI Fare & Route Assistant"])

with tab1:
    st.header("Driver: Offer a Ride")
    with st.form("ride_form"):
        driver_name = st.text_input("Your Name")
        start_loc = st.text_input("Starting Location (e.g. Sargodha)")
        end_loc = st.text_input("Destination Location (e.g. Sahiwal)")
        vehicle_type = st.selectbox("Vehicle Type", ["Bike", "Car", "Van/Hiace"])
        available_seats = st.number_input("Available Seats", min_value=1, max_value=15, value=2)
        fare_per_seat = st.number_input("Fare per Seat (PKR)", min_value=0, value=500)
        
        submitted = st.form_submit_button("Post Ride")
        if submitted:
            if driver_name and start_loc and end_loc:
                st.session_state.rides.append({
                    "driver": driver_name,
                    "from": start_loc,
                    "to": end_loc,
                    "vehicle": vehicle_type,
                    "seats": available_seats,
                    "fare": fare_per_seat
                })
                st.success("Ride posted successfully!")
            else:
                st.error("Please fill in all details.")

with tab2:
    st.header("Passenger: Find Available Rides")
    if not st.session_state.rides:
        st.info("No rides posted yet.")
    else:
        for idx, ride in enumerate(st.session_state.rides):
            with st.expander(f"🚗 {ride['from']} ➔ {ride['to']} ({ride['vehicle']}) — By {ride['driver']}"):
                st.write(f"*Available Seats:* {ride['seats']}")
                st.write(f"*Fare per seat:* PKR {ride['fare']}")
                if st.button(f"Book Seat #{idx+1}"):
                    if ride['seats'] > 0:
                        ride['seats'] -= 1
                        st.success("Seat booked successfully!")
                        st.rerun()
                    else:
                        st.error("Sorry, no seats available!")

with tab3:
    st.header("🤖 AI Route & Fare Advisor")
    st.write("Get AI recommendations for fair pricing and fuel estimation.")
    ai_from = st.text_input("From Location:", "Sargodha")
    ai_to = st.text_input("To Location:", "Sahiwal")
    ai_vehicle = st.selectbox("Vehicle Category:", ["Bike", "Car", "Van"])

    if st.button("Calculate Smart Fare & Route Info"):
        if not api_key:
            st.warning("Please enter your Gemini API Key in the sidebar first!")
        else:
            try:
                client = genai.Client(api_key=api_key)
                prompt = f"""
                You are a smart Pakistani Ride-Share & Fare Assistant. 
                Calculate an estimated realistic per-seat fare (in PKR) and distance advice for travelling from {ai_from} to {ai_to} using a {ai_vehicle}.
                Consider approximate distance, current fuel prices in Pakistan, and comfort. 
                Provide:
                1. Estimated Distance (km)
                2. Recommended Fair Fare per seat (PKR)
                3. Route & Safety Advice for passengers/drivers.
                Keep the response concise and clear.
                """
                response = client.models.generate_content(
                    model='gemini-2.0-flash',
                    contents=prompt
                )
                st.markdown("### 📊 AI Estimation Results")
                st.write(response.text)
            except Exception as e:
                st.error(f"Error: {e}")
