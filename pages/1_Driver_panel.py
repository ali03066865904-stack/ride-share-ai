import streamlit as st
import pandas as pd
import pydeck as pdk

st.set_page_config(page_title="Driver Live Route GPS Map", page_icon="🚗", layout="wide")

st.title("🚗 Driver Live GPS Route & Moving Tracker")
st.subheader("Real-time route mapping from Sahiwal through mid-stops to Lahore")

# Route coordinates definition (Sahiwal -> Sargodha/Mid-Stop -> Lahore)
route_data = pd.DataFrame({
    'lat': [30.6682, 31.0530, 31.5204],
    'lon': [73.1114, 72.6711, 74.3587],
    'name': ['Starting: Sahiwal', 'Mid-Stop (Pickup Zone)', 'Destination: Lahore']
})

col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("### 🛣️ Trip Parameters & Live Status")
    driver_name = st.text_input("Driver Name", "Muhammad Saleem")
    vehicle_type = st.selectbox("Vehicle", ["Car 🚗", "Hiace 🚐", "Motorbike 🏍️"])
    
    # Live Progress Simulation Slider (Controls the moving vehicle on the blue route line)
    progress_val = st.slider("🚗 Live Vehicle Movement Tracker (% of Journey Completed):", 0, 100, 35)
    
    # Calculate dynamic coordinates along the route based on slider
    curr_lat = 30.6682 + (31.5204 - 30.6682) * (progress_val / 100)
    curr_lon = 73.1114 + (74.3587 - 73.1114) * (progress_val / 100)
    
    covered_dist = int((progress_val / 100) * 170)
    remaining_dist = 170 - covered_dist
    
    st.info(f"📍 *Current GPS Position:* {covered_dist} km covered, {remaining_dist} km remaining to Lahore.")
    
    if st.button("🟢 Broadcast Live GPS Signal", type="primary"):
        st.success("✅ GPS Broadcast Active! Passengers within 15km can track your vehicle on the map.")

with col2:
    st.markdown("### 🗺️ Live Map: Route Line & Moving Vehicle")
    
    # Current moving vehicle dataframe
    current_vehicle_df = pd.DataFrame({
        'lat': [curr_lat],
        'lon': [curr_lon],
        'status': [f"Active Vehicle ({vehicle_type})"]
    })

    # PyDeck Layer for gorgeous map with route and moving marker
    layer_route = pdk.Layer(
        "LineLayer",
        data=pd.DataFrame({
            'start_lat': [30.6682],
            'start_lon': [73.1114],
            'end_lat': [31.5204],
            'end_lon': [74.3587]
        }),
        get_source_position='[start_lon, start_lat]',
        get_target_position='[end_lon, end_lat]',
        get_color='[0, 128, 255, 200]',
        get_width=5,
    )

    layer_vehicle = pdk.Layer(
        "ScatterplotLayer",
        data=current_vehicle_df,
        get_position='[lon, lat]',
        get_color='[255, 0, 0, 200]',
        get_radius=8000,
    )

    view_state = pdk.ViewState(
        latitude=curr_lat,
        longitude=curr_lon,
        zoom=7.5,
        pitch=0,
    )

    r = pdk.Deck(
        layers=[layer_route, layer_vehicle],
        initial_view_state=view_state,
        tooltip={"text": "Live Vehicle Position\nLat: {lat}\nLon: {lon}"}
    )

    st.pydeck_chart(r)

st.divider()
st.metric("GPS Tracking Accuracy", "High (Satellite Locked)")
