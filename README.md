# 🚗 RoutePool AI — Smart Ride Sharing & Fare Assistant

*RoutePool AI* is an end-to-end web application designed to solve daily commuting and intercity travel challenges in Pakistan. It enables drivers with available vehicle capacity (bikes, cars, vans) to offer shared rides, while empowering passengers to easily discover affordable local commutes. Integrated with Google Gemini 2.5 AI, the app automatically calculates recommended per-seat fair fares based on route distance, vehicle type, and fuel market conditions.

---

## 🔗 Live Application & Links
* *Live Deployed App:* https://ride-share-ai-xm3psr5n4doxtqsazjb6ig.streamlit.app
* *GitHub Repository:* https://github.com/ali03066865904-stack/ride-share-ai

---

## 🌟 Key Features

1. *Driver Ride Publishing:*
   * Drivers can offer rides by entering starting location, destination, vehicle category (Bike/Car/Van), total seats available, and custom base fare.
   
2. *Interactive Seat Booking:*
   * Passengers can browse through active rides and reserve seats in real time with dynamic seat count tracking.

3. *🤖 AI-Powered Fare & Route Advisor:*
   * Calculates realistic per-seat pricing dynamically using current fuel trends and distance estimation.
   * Generates actionable safety advice and route convenience guidance for riders and commuters.

---

## 🧠 The AI Feature & System Prompt

The application utilizes Google's *Gemini 2.5 Flash* model to function as an expert Pakistani mobility assistant.

### System Prompt / Instructions:
```text
You are a smart Pakistani Ride-Share & Fare Assistant. 
Calculate an estimated realistic per-seat fare (in PKR) and distance advice for travelling from {ai_from} to {ai_to} using a {ai_vehicle}.
Consider approximate distance, current fuel prices in Pakistan, and comfort. 

Provide:
1. Estimated Distance (km)
2. Recommended Fair Fare per seat (PKR)
3. Route & Safety Advice for passengers/drivers.
Keep the response concise and clear.
