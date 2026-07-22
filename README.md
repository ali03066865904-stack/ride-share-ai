# 🚀 Smart Ride Connect — AI-Powered Inter-City Dynamic Ride-Sharing & Live GPS Radar

<div align="center">

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://ride-share-ai-rcufwxybafqe4yycpam4rf.streamlit.app/)
[![GitHub Repository](https://img.shields.io/badge/GitHub-Repository-blue.svg)](https://github.com/ali03066865904-stack/ride-share-ai)
[![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Status](https://img.shields.io/badge/Status-Production%20Ready%20🔥-success.svg)]()

*A Next-Generation Real-Time Inter-City Transportation, Live GPS Route Tracker & Dynamic Vehicle-Passenger Matching Ecosystem*

</div>

---

## 📌 1. Project Overview & Real-World Problem Solved
* *App Name:* Smart Ride Connect
* *What it does:* It is a decentralized, two-sided real-time inter-city transportation platform that connects drivers broadcasting active routes with intermediate passengers looking for flexible transport options.
* *The Problem It Solves:* In Pakistan, commuters traveling along major inter-city corridors (such as the *Sahiwal $\rightarrow$ Sargodha $\rightarrow$ Lahore* route) frequently encounter rigid transport schedules, exorbitant fares, and a total lack of real-time visibility for intermediate pickups. 
* *Target Audience:* Daily commuters, inter-city travelers, and local vehicle owners (Car, Hiace, and Motorbike drivers) looking to optimize shared travel costs.

---

## 🔗 2. Live Deployed Application & Repository
* *Live Working URL (Clickable):* https://ride-share-ai-rcufwxvbafqe4yycpam4r7.streamlit.app/
* *GitHub Repository:* [View GitHub Source Code](https://github.com/ali03066865904-stack/ride-share-ai)

---

## 🌟 3. Comprehensive Features List
The application is structured using Streamlit's official Multi-Page Framework and features:
1. *Driver Live GPS Route & Moving Tracker (pages/1_Driver_Panel.py):*
   * Visualizes the complete inter-city route on an interactive PyDeck map with dynamic blue polyline route rendering.
   * Multi-class vehicle configuration profiles (*Cars 🚗, **Hiaces 🚐, and **Motorbikes 🏍️*).
   * Real-time progress synchronization via an interactive journey progress slider calculating exact covered kilometers and remaining distance to Lahore.
   * Route-wide passenger radar capturing commuters waiting along the corridor.
2. *Passenger Live Vehicle Radar & Auto-Matching (pages/2_Passanger_panel.py):*
   * Live browser/device geolocation sensor integration for instant coordinate detection.
   * Full-fleet route visibility allowing passengers to track all active vehicles operating across the Sahiwal-Lahore corridor.
   * Instant seat booking and ping dispatch system for approaching drivers.
3. *Gemini AI Smart Fare & Route Estimator (pages/3_AI_Fare_Engine.py):*
   * Intelligent dynamic pricing calculations based on distance benchmarks, vehicle classification, and fuel estimates.
   * Robust algorithmic fallback engine guaranteeing 100% uptime even during API rate limits.

---

## 🤖 4. AI Feature & System Prompt
* *What the AI Does:* The *AI Smart Fare Engine* analyzes live route dynamics, inter-city traffic congestion, current fuel benchmarks, and passenger pooling capacity to generate optimal fare estimates and safety recommendations.
* *Underlying AI System Prompt & Instructions:*
  ```text
  Role: You are an expert AI Inter-City Transportation & Logistics Advisor in Pakistan.
  Task: Analyze the given pickup point, drop-off destination, and vehicle class (Car, Hiace, or Motorbike). Compute the optimal dynamic fare in PKR, estimate travel time, calculate fuel resource consumption, and provide a structured route optimization insight report for the passenger and driver.
  Constraints: Ensure robust fallback calculations if API quotas are exceeded, maintaining high reliability and precision.
