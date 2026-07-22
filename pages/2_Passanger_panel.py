import streamlit as st
import json

st.title("🎒 Passenger Mid-Route Seat Booking")
st.caption("Scan live vehicles passing through your area (e.g. Sargodha on Sahiwal-Lahore route)")

try:
    with open("data/sample_routes.json", "r") as f:
        routes = json.load(f)
        
    for r in routes:
        with st.expander(f"🚗 {r['vehicle']} — Driver: {r['driver']} (Route: {r['from_city']} ➔ {r['via_stop']} ➔ {r['to_city']})"):
            st.write(f"📞 *Phone:* {r['phone']}")
            st.write(f"💺 *Seats Left:* {r['seats_available']}")
            st.write(f"💰 *Fare:* PKR {r['fare_pkr']}")
            if st.button(f"Book Pickup at {r['via_stop']} ({r['id']})"):
                st.balloons()
                st.success("🎉 Seat Booked Successfully! Pickup synchronized with driver.")
except Exception as e:
    st.error("No active route data found.")
