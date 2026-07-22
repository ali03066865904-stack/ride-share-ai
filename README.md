# 🚗 Smart Ride Connect — AI-Powered Dynamic Inter-City Ride Sharing

> *Final Project — Ship Your AI App*  
> A Real-World Solution for Mid-Route Pickups, Flexible Fleet Capacities, and Smart Fare Estimation in Pakistan.

---

## 📌 Project Overview
In Pakistan, passengers traveling short or intermediate distances between major cities (e.g., Sargodha to Lahore on a Sahiwal-Lahore route) often face high fares or lack of available transport. 

*Smart Ride Connect* bridges this gap by enabling drivers to broadcast their route with *Live GPS Tracking*. Intermediate passengers (within a 10–15 km radius) can view upcoming vehicles, select their pick & drop points, and book seats seamlessly with dual-language support (English & Urdu).

---

## ✨ Features & Functionality
1. *Dual Simulator Layout:* Dedicated panels for Driver (Trip publishing & GPS toggle) and Passenger (Seat discovery & booking).
2. *Dynamic Mid-Route Waypoint Matching:* Mid-route travelers can book remaining seats dynamically.
3. *Multi-Vehicle Fleet:* Supports Bikes, Cars, Carry Dabbas, Hiace Vans, and Buses.
4. *Bilingual UI:* Clean interface in English & Urdu for complete accessibility.
5. *AI Route & Fare Advisor:* Uses Gemini 2.0 Flash model to recommend fair per-seat pricing and route safety tips.

---

## 🤖 AI System Prompt
```text
You are a smart Pakistani Ride-Share Assistant. Calculate estimated fare (in PKR) and route advice from starting point to destination for selected vehicle category. Consider approximate distance, current fuel prices in Pakistan, highway safety tips, and comfort
