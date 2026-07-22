# 🚗 Smart Ride Connect — AI-Powered Dynamic Inter-City Ride Sharing

> *Final Project — Ship Your AI App*  
> A Real-World Solution for Mid-Route Pickups, Flexible Fleet Capacities, and Smart Fare Estimation in Pakistan.

---

## 🔗 Live Deployed Application
* *Live Working URL:* https://ride-share-ai-rcufwxvbafqe4yycpam4r7.streamlit.app/
* *GitHub Repository:* https://github.com/ali03066865904-stack/ride-share-ai

* *A Next-Generation Real-Time Inter-City Transportation, Live GPS Route Tracker & Dynamic Vehicle-Passenger Matching Ecosystem*

</div>

---

## 📌 Executive Summary
In Pakistan, commuters traveling short or intermediate distances between major cities (e.g., Sargodha or Sahiwal to Lahore routes) frequently face rigid transport schedules, high fares, and a lack of real-time visibility. 

*Smart Ride Connect* bridges this gap by enabling drivers to broadcast their route with *Live GPS Tracking*. Intermediate passengers can view active vehicles on an interactive map, monitor real-time coordinates, select precise pick-and-drop points, and book seats seamlessly across multi-class transport options.

---

## 🌟 Advanced System Modules & Features

### 1. 🚗 Driver Live GPS Route & Moving Tracker (pages/1_Driver_Panel.py)
* *Live Corridor Mapping:* Visualizes the complete inter-city route on an interactive PyDeck map with dynamic blue polyline route rendering.
* *Multi-Vehicle Category Support:* Dedicated configuration profiles and live tracking for *Cars 🚗, **Hiaces 🚐, and **Motorbikes 🏍️*.
* *Real-Time Progress Synchronization:* Features an interactive journey progress slider that calculates exact covered kilometers and remaining distance to Lahore in real-time.
* *Route-Wide Passenger Radar:* Automatically captures and displays all connected commuters waiting along the route corridor.

### 2. 🎒 Passenger Live Vehicle Radar & Auto-Matching (pages/2_Passanger_panel.py)
* *Live GPS Device Integration:* Automatically fetches browser/device geolocation coordinates to detect users instantly.
* *All-Fleet Route Visibility:* Allows passengers to view every active vehicle operating anywhere along the Sahiwal-Lahore corridor.
* *Instant Seat Booking & Ping System:* Enables passengers to dispatch pickup requests directly to approaching drivers with synchronized navigation coordinates.

### 3. 🤖 Gemini AI Smart Fare & Route Estimator (pages/3_AI_Fare_Engine.py)
* *Dynamic Pricing Algorithms:* Calculates intelligent inter-city fares based on distance benchmarks, vehicle classification, and fuel estimates.
* *Robust Fallback Engine:* Guarantees 100% uptime with smart algorithmic heuristics even during API quota exhaustion.

---

## 📁 Repository & File Architecture (Enterprise Modular Design)
This repository is built using Streamlit's official *Multi-Page Application Framework*, structured across modular files:

```text
ride-share-ai/
├── .streamlit/
│   └── config.toml             # Custom UI Theme Configuration
├── pages/
│   ├── 1_Driver_Panel.py       # Driver Dashboard, Route Publisher & Live GPS Broadcaster
│   ├── 2_Passanger_panel.py    # Passenger Radar, Vehicle Selection & Seat Booking Engine
│   └── 3_AI_Fare_Engine.py     # Gemini 2.0 AI Optimization & Smart Fare Module
├── data/
│   └── sample_routes.json      # Mock Dataset for Active Pakistani Routes
├── utils/
│   ├── fare_calculator.py      # Rule-Based Fare Logic & Mileage Calculator
│   └── ai_helper.py            # Google GenAI API Integration Wrapper
├── Home.py                     # Main Landing Page & Dashboard
├── README.md                   # Comprehensive Project Report
└── requirements.txt            # Project Python Dependencies
