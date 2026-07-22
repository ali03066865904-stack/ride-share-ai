import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Live GPS Passenger Panel", page_icon="🎒", layout="wide")

st.title("🎒 Passenger Live GPS Radar & Auto-Matching")
st.subheader("Automatic GPS Detection — Find nearby drivers within your 15km radius instantly.")

# JavaScript component to fetch real device/browser GPS coordinates automatically
st.markdown("### 📍 Your Live GPS Coordinates (Auto-Detected)")

geo_script = """
<div id="demo">Click the button below to fetch your live GPS location:</div>
<button onclick="getLocation()" style="background-color:#2563EB; color:white; padding:10px 20px; border:none; border-radius:5px; cursor:pointer; font-weight:bold;">🛰️ Fetch My Live GPS Location</button>

<script>
var x = document.getElementById("demo");
function getLocation() {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(showPosition, showError);
  } else {
    x.innerHTML = "Geolocation is not supported by this browser.";
  }
}

function showPosition(position) {
  x.innerHTML = "<b>Latitude:</b> " + position.coords.latitude + 
                "<br><b>Longitude:</b> " + position.coords.longitude + 
                " <span style='color:green; font-weight:bold;'>✔️ GPS Active & Locked!</span>";
}

function showError(error) {
  switch(error.code) {
    case error.PERMISSION_DENIED:
      x.innerHTML = "User denied the request for Geolocation.";
      break;
    case error.POSITION_UNAVAILABLE:
      x.innerHTML = "Location information is unavailable.";
      break;
    case error.TIMEOUT:
      x.innerHTML = "The request to get user location timed out.";
      break;
    case error.UNKNOWN_ERROR:
      x.innerHTML = "An unknown error occurred.";
      break;
  }
}
</script>
"""
components.html(geo_script, height=120)

st.divider()

st.markdown("### 🚗 Nearby Drivers Live Radar (Auto-Matched)")
st.info("📡 GPS Radar Active: Scanning Sahiwal ➔ Sargodha ➔ Lahore Route...")

# Simulated auto-detected live matching vehicles
col1, col2 = st.columns(2)
with col1:
    st.success("🚗 *Car (Muhammad Saleem)\n *Distance from you:* 3.2 km away\n* *Speed:* 65 km/h (Approaching)\n* *Status:* Available (2 Seats Left)")
    if st.button("Connect & Request Pickup"):
        st.balloons()
        st.success("✅ GPS Ping Sent to Driver! Driver's navigation updated with your live coordinates.")

with col2:
    st.info("🏍️ *Motorbike (Ali Raza)\n *Distance from you:* 8.5 km away\n* *Speed:* 45 km/h\n* *Status:* Available (1 Seat Left)")
    if st.button("Connect & Request Bike Ride"):
        st.success("✅ GPS Ping Sent to Biker!")
