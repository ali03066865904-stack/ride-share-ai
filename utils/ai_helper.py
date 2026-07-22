from google import genai

def get_gemini_route_advice(api_key: str, origin: str, destination: str, vehicle: str):
    """Fetches AI route advice and fare optimization from Gemini 2.0 API."""
    if not api_key:
        return None
    try:
        client = genai.Client(api_key=api_key)
        prompt = (
            f"You are an expert Pakistani Ride-Share Transport Advisor. "
            f"Calculate exact distance, estimated fuel cost, fair fare per seat in PKR, "
            f"and safety route advice for traveling from {origin} to {destination} via {vehicle}."
        )
        response = client.models.generate_content(model='gemini-2.0-flash', contents=prompt)
        return response.text
    except Exception as e:
        return f"API Error: {str(e)}"
