import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Driver Live GPS Dashboard", page_icon="🚗", layout="wide")

st.title("🚗 Driver Live GPS Navigation & Radar")
st.subheader("Automatic GPS Route Broadcast & Nearby Passenger Detection")

st.markdown("### 📡 Broadcast Your Live Driving Location")

driver_geo_script = """
<div id="driver_status">Click below to share your real-time vehicle GPS position:</div>
<button onclick="getDriverLocation()" style="background-color:#16A34A; color:white; padding:10px 20px; border:none; border-radius:5px; cursor:pointer; font-weight:bold;">🛰️ Start Live Vehicle GPS Broadcast</button>

<script>
var statusDiv = document.getElementById("driver_status");
function getDriverLocation() {
  if (navigator.geolocation) {
    navigator.geolocation.watchPosition(showDriverPosition);
  } else {
    statusDiv.innerHTML = "Geolocation not supported.";
  }
}

function showDriverPosition(position) {
  statusDiv.innerHTML = "<b>Live Vehicle Lat:</b> " + position.coords.latitude.toFixed(4) + 
                        " | <b>Lon:</b> " + position.coords.longitude.toFixed(4) + 
                        " <span style='color:green; font-weight:bold;'>🟢 GPS Broadcasting Live!</span>";
}
</script>
"""
components.html(driver_geo_script, height=120)

st.divider()

st.markdown("### 🔔 Live Passengers Waiting on Your Route (Auto-Detected by GPS)")
st.warning("👤 *Passenger Detected:* Ahmad Khan \n* *Distance:* 4.1 km ahead on your route \n* *Destination:* Lahore \n* *GPS Match:* Within your 15km pickup radius!")

if st.button("✅ Accept Passenger GPS Ping & Navigate"):
    st.success("🎉 Passenger request accepted! Turn-by-turn GPS navigation synchronized.")

st.divider()
st.metric("Live GPS Satellite Link", "Connected (High Accuracy)")
st.metric("Active Radius Scanning", "15 km")
