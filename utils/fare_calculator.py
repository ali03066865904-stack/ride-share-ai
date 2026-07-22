# Fare Engine Module
RATES_PER_KM = {
    "Bike / موٹر سائیکل": 8,
    "Car / کار": 16,
    "Carry Dabba / کیری ڈبہ": 12,
    "Hiace / ہائی ایس": 10,
    "Shalimar Bus / شالیمار بس": 7
}

def calculate_estimated_fare(vehicle_type: str, distance_km: float, seats: int = 1) -> float:
    """Calculates fair fare per seat based on distance and vehicle class."""
    base_rate = RATES_PER_KM.get(vehicle_type, 15)
    total_cost = distance_km * base_rate
    fare_per_seat = round(total_cost / max(seats, 1))
    return fare_per_seat
