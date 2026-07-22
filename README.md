# 🚀 Smart Ride Connect — AI-Powered Inter-City Dynamic Ride-Sharing & Live GPS Radar

<div align="center">

[![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Production%20Ready%20🔥-success.svg)]()

*A Next-Generation Real-Time Inter-City Transportation, Live GPS Route Tracker & Dynamic Vehicle-Passenger Matching Ecosystem*

</div>

---

## 📌 Executive Summary
In Pakistan, commuters traveling along major inter-city corridors (such as the Sahiwal $\rightarrow$ Sargodha $\rightarrow$ Lahore route) frequently encounter rigid transport schedules, high fares, and a lack of real-time visibility. *Smart Ride Connect* solves this by establishing a decentralized, two-sided marketplace. It integrates live browser geolocation sensors, PyDeck interactive mapping, multi-class vehicle profiling, and an advanced Gemini AI Fare Optimization Engine to connect drivers and mid-route passengers instantly.

---

## 🌟 Advanced System Modules & Features

### 1. 🚗 Driver Live GPS Route & Moving Tracker (pages/1_Driver_Panel.py)
* *Live Corridor Mapping:* Visualizes the complete inter-city route on an interactive PyDeck map with dynamic blue polyline route rendering.
* *Multi-Vehicle Category Support:* Dedicated configuration profiles for *Cars 🚗, **Hiaces 🚐, and **Motorbikes 🏍️*.
* *Real-Time Progress Synchronization:* Features an interactive journey progress slider that calculates exact covered kilometers and remaining distance to the destination in real-time.
* *Route-Wide Passenger Radar:* Automatically captures and displays all connected commuters waiting along the corridor without arbitrary distance caps.

### 2. 🎒 Passenger Live Vehicle Radar & Auto-Matching (pages/2_Passanger_panel.py)
* *Live GPS Device Integration:* Automatically fetches browser/device geolocation coordinates to detect users instantly.
* *All-Fleet Route Visibility:* Allows passengers to view every active vehicle (Bikes, Cars, Vans) operating anywhere along the route.
* *Instant Seat Booking & Ping System:* Enables passengers to dispatch pickup requests directly to approaching drivers with synchronized navigation coordinates.

### 3. 🤖 Gemini AI Smart Fare & Route Estimator (pages/3_AI_Fare_Engine.py)
* *Dynamic Pricing Algorithms:* Calculates intelligent inter-city fares based on distance benchmarks, vehicle classification, and fuel estimates.
* *Robust Fallback Engine:* Guarantees 100% uptime with smart algorithmic heuristics even during API quota exhaustion.

---

## 📂 Enterprise Repository & File Architecture

```text
ride-share-ai/
│
├── .streamlit/
│   └── config.toml               # Enterprise Custom UI Theme & Configuration
│
├── pages/
│   ├── 1_Driver_Panel.py         # Driver Dashboard, Route Publisher & Live GPS Broadcaster
│   ├── 2_Passanger_Panel.py      # Passenger Radar, Vehicle Selection & Seat Booking Engine
│   └── 3_AI_Fare_Engine.py       # Gemini 2.0 AI Optimization & Smart Fare Module
│
├── utils/
│   └── ai_helper.py              # Core AI Integration & Fallback Heuristics
│
├── data/
│   └── sample_routes.json        # Corridor Metadata & Intermediate Stop Coordinates
│
├── Home.py                       # Main System Landing Portal & Navigation Hub
├── requirements.txt              # Production Dependencies & Python Libraries
└── README.md                     # Professional System Documentation
