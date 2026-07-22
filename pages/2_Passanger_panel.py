import streamlit as st
import pandas as pd
import pydeck as pdk

st.set_page_config(page_title="Passenger Live Route Tracking", page_icon="🎒", layout="wide")

st.title("🎒 Passenger Live Route & Vehicle Radar")
st.subheader("Live tracking of all active vehicles from Sahiwal to Lahore along the entire route")

# Shared session state for active vehicles and requests
if 'active_trips' not in st.session_state:
    st.session_state.active_trips = [
        {"id": "TRIP-01", "driver": "Muhammad Saleem", "vehicle": "Car 🚗", "origin": "Sahiwal", "destination": "Lahore", "progress": 35, "lat": 30.95, "lon": 73.50, "seats": 2, "fare": 1200},
        {"id": "TRIP-02", "driver": "Tariq Mahmood", "vehicle": "Hiace 🚐", "origin": "Sahiwal", "destination": "Lahore", "progress": 60, "lat": 31.20, "lon": 73.80, "seats": 4, "fare": 900},
    ]

st.markdown("### 🌐 All Active Vehicles on Sahiwal ➔ Lahore Route")

col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("#### 🚗 Select Vehicle to View Live Position")
    trip_names = [f"{t['vehicle']} — Driver: {t['driver']} ({t['origin']} to {t['destination']})" for t in st.session_state.active_trips]
    selected_trip_str = st.selectbox("Choose a live vehicle:", trip_names)
    
    selected_idx = trip_names.index(selected_trip_str)
    trip = st.session_state.active_trips[selected_idx]
    
    covered = int((trip['progress'] / 100) * 170)
    remaining = 170 - covered
    
    st.info(f"""
    * *Driver Name:* {trip['driver']}
    * *Vehicle Type:* {trip['vehicle']}
    * *Covered Distance:* {covered} km from {trip['origin']}
    * *Remaining Distance:* {remaining} km to {trip['destination']}
    * *Available Seats:* {trip['seats']} | *Fare:* PKR {trip['fare']}
    """)
    
    if st.button("🎫 Book Seat on this Vehicle", type="primary"):
        if trip['seats'] > 0:
            trip['seats'] -= 1
            st.success(f"✅ Seat booked successfully! Driver {trip['driver']} has received your pickup location.")
        else:
            st.error("❌ Vehicle is fully booked!")

with col2:
    st.markdown("#### 🗺️ Full Route Live Map")
    # PyDeck Map showing the route and active vehicle
    layer_route = pdk.Layer(
        "LineLayer",
        data=pd.DataFrame({'start_lat': [30.6682], 'start_lon': [73.1114], 'end_lat': [31.5204], 'end_lon': [74.3587]}),
        get_source_position='[start_lon, start_lat]',
        get_target_position='[end_lon, end_lat]',
        get_color='[0, 128, 255, 200]',
        get_width=5,
    )
    
    vehicle_df = pd.DataFrame({'lat': [trip['lat']], 'lon': [trip['lon']], 'name': [trip['driver']]})
    layer_marker = pdk.Layer(
        "ScatterplotLayer",
        data=vehicle_df,
        get_position='[lon, lat]',
        get_color='[255, 0, 0, 200]',
        get_radius=10000,
    )
    
    view_state = pdk.ViewState(latitude=31.10, longitude=73.70, zoom=7.5)
    r = pdk.Deck(layers=[layer_route, layer_marker], initial_view_state=view_state)
    st.pydeck_chart(r)

st.divider()
st.markdown("### 📢 Broadcast Your Request to All Route Drivers")
with st.form("passenger_request_form"):
    p_name = st.text_input("Your Name", "Ahmad Khan")
    p_loc = st.text_input("Your Location on Route", "Chichawatni / Pipli Stop")
    p_dest = st.text_input("Your Destination", "Lahore")
    if st.form_submit_button("Broadcast to Route Drivers"):
        st.success("✅ Broadcast sent to all active drivers on the Sahiwal-Lahore route!")
