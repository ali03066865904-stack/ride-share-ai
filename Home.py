import streamlit as st

st.set_page_config(
    page_title="Smart Ride Connect — AI Dynamic Inter-City Transport",
    page_icon="🚗",
    layout="wide"
)

st.markdown("""
    <style>
    .hero-title { font-size: 2.8rem; color: #1E3A8A; font-weight: 800; text-align: center; }
    .hero-sub { font-size: 1.2rem; color: #475569; text-align: center; margin-bottom: 30px; }
    .feature-card { background: #F1F5F9; padding: 20px; border-radius: 12px; border-left: 5px solid #2563EB; }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='hero-title'>🚗 SMART RIDE CONNECT</div>", unsafe_allow_html=True)
st.markdown("<div class='hero-sub'>Next-Gen AI Inter-City Ride Sharing & Dynamic Mid-Route Pickup System</div>", unsafe_allow_html=True)

st.image("https://images.unsplash.com/photo-1449965408869-eaa3f722e40d?q=80&w=1000&auto=format&fit=crop", use_container_width=True)

st.markdown("---")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class='feature-card'>
        <h3>👨‍✈️ Driver Dashboard</h3>
        <p>Publish long-haul inter-city trips (Sahiwal ➔ Sargodha ➔ Lahore), set empty seat counts, and share dynamic GPS radius.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class='feature-card'>
        <h3>🎒 Passenger Panel</h3>
        <p>Intermediate commuters within 10–15 km can detect active vehicles, book seats mid-route, and match drop points.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class='feature-card'>
        <h3>🤖 Gemini AI Engine</h3>
        <p>Integrated with Google Gemini 2.0 Flash to calculate route fares based on vehicle category and fuel consumption.</p>
    </div>
    """, unsafe_allow_html=True)

st.info("👈 *بائیں طرف Sidebar (سائیڈ بار) سے کوئی بھی پیج سلیکٹ کر کے ایپ کا مکمل ڈیمو دیکھیں!*")
