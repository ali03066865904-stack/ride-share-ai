# 🚗 Smart Ride Connect — AI-Powered Dynamic Inter-City Ride Sharing

> *Final Project — Ship Your AI App*  
> A Real-World Solution for Mid-Route Pickups, Flexible Fleet Capacities, and Smart Fare Estimation in Pakistan.

---

## 🔗 Live Deployed Application
* *Live Working URL:* [YOUR_STREAMLIT_URL_HERE]
* *GitHub Repository:* https://github.com/ali03066865904-stack/ride-share-ai

---

## 📌 Project Overview
In Pakistan, passengers traveling short or intermediate distances between major cities (e.g., Sargodha to Lahore on a Sahiwal-Lahore route) often face high fares or lack of available transport. 

*Smart Ride Connect* bridges this gap by enabling drivers to broadcast their route with *Live GPS Tracking*. Intermediate passengers (within a 10–15 km radius) can view upcoming vehicles, select their pick & drop points, and book seats seamlessly with dual-language support (English & Urdu).

---

## 📁 Repository & File Architecture (Enterprise Modular Design)
This repository is built using Streamlit's official *Multi-Page Application Framework*, structured across 10 modular files:

```text
ride-share-ai/
├── .streamlit/
│   └── config.toml             # Custom UI Theme Configuration
├── pages/
│   ├── 1_👨‍✈️_Driver_Panel.py    # Driver Dashboard & Route Publisher
│   ├── 2_🎒_Passenger_Panel.py # Dynamic Mid-Route Seat Booking
│   └── 3_🤖_AI_Fare_Engine.py   # Gemini 2.0 AI Advisor Module
├── data/
│   └── sample_routes.json      # Mock Dataset for Active Pakistani Routes
├── utils/
│   ├── fare_calculator.py      # Rule-Based Fare Logic & Mileage Calculator
│   └── ai_helper.py            # Google GenAI API Integration Wrapper
├── Home.py                     # Main Landing Page & Dashboard
├── README.md                   # Comprehensive Project Report
└── requirements.txt            # Project Python Dependencies
