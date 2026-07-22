import streamlit as st
import pandas as pd
import pydeck as pdk

st.set_page_config(page_title="Driver Route & Passenger Sync", page_icon="🚗", layout="wide")

st.title("🚗 Driver Live Route & Passenger Tracker")
st.subheader("Manage your Sahiwal-Lahore trip and view all connected passengers along the route")

if 'active_trips' not in st.session_state:
    st.session_state.active_trips = [
        {"id": "TRIP-01", "driver": "Muhammad Saleem", "vehicle": "Car 🚗", "origin": "Sahiwal", "destination": "Lahore", "progress": 35, "lat": 30.95, "lon": 73.50, "seats": 2, "fare": 1200}
    ]

col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("### 🛣️ Update Your Trip Progress")
    d_name = st.text_input("Driver Name", "Muhammad Saleem")
    d_veh = st.selectbox("Vehicle Type", ["Car 🚗", "Hiace 🚐", "Motorbike 🏍️"])
    
    progress = st.slider("Trip Progress (% completed from Sahiwal to Lahore):", 0, 100, 35)
    
    # Calculate live coordinates
    curr_lat = 30.6682 + (31.5204 - 30.6682) * (progress / 100)
    curr_lon = 73.1114 + (74.3587 - 73.1114) * (progress / 100)
    
    covered = int((progress / 100) * 170)
    remaining = 170 - covered
    
    st.info(f"📍 *Position Status:* {covered} km completed, {remaining} km remaining to Lahore.")
    
    if st.button("🚀 Sync Live Position with Route", type="primary"):
        st.success("✅ Live position broadcasted across the entire route!")

with col2:
    st.markdown("### 🗺️ Full Route Map & Moving Vehicle")
    layer_route = pdk.Layer(
        "LineLayer",
        data=pd.DataFrame({'start_lat': [30.6682], 'start_lon': [73.1114], 'end_lat': [31.5204], 'end_lon': [74.3587]}),
        get_source_position='[lon, lat]' if False else '[73.1114, 30.6682]',
        get_target_position='[74.3587, 31.5204]',
        get_color='[0, 128, 255, 200]',
        get_width=5,
    )
    
    current_df = pd.DataFrame({'lat': [curr_lat], 'lon': [curr_lon]})
    layer_car = pdk.Layer(
        "ScatterplotLayer",
        data=current_df,
        get_position='[lon, lat]',
        get_color='[0, 255, 0, 200]',
        get_radius=10000,
    )
    
    view_state = pdk.ViewState(latitude=31.10, longitude=73.70, zoom=7.5)
    r = pdk.Deck(layers=[layer_route, layer_car], initial_view_state=view_state)
    st.pydeck_chart(r)

st.divider()
st.markdown("### 👥 Connected Passengers Waiting Along This Route")
st.warning("👤 *Passenger:* Ahmad Khan \n* *Pickup Location:* Chichawatni (Route Stop) \n* *Destination:* Lahore \n* *Status:* Looking for vehicle matching this route")

if st.button("✅ Accept & Pick Up Passenger"):
    st.success("🎉 Passenger accepted! Route synchronized with passenger's phone.")
