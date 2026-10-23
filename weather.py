import requests

WEATHER_CODES = {
    0: "Clear sky",
    1: "Mainly clear",
    2: "Partly cloudy",
    3: "Overcast",
    45: "Fog",
    48: "Depositing rime fog",
    51: "Light drizzle",
    61: "Slight rain",
    63: "Moderate rain",
    65: "Heavy rain",
    71: "Slight snow",
    80: "Rain showers",
    95: "Thunderstorm"
}

def fetch_weather(city):
    
    loc_cords = requests.get(
        "https://geocoding-api.open-meteo.com/v1/search",

        params={"name": city, "count": 1, "language": "en", "format": "json"},

        timeout=10
    ) 
    loc_cords.raise_for_status()
    locations = loc_cords.json().get("results", [])

    if not locations:
        raise ValueError(f"location not found {city}")

    location = locations[0]

    response = requests.get(
        "https://api.open-meteo.com/v1/forecast",
        
        params={
            "latitude" : location["latitude"],
            "longitude": location["longitude"],
      
            "current": (
            "temperature_2m,"
            "relative_humidity_2m,"
            "apparent_temperature,"
            "is_day,"
            "precipitation,"
            "rain,"
            "showers,"
            "weather_code,"
            "pressure_msl,"
            "cloud_cover,"
            "wind_speed_10m,"
            "wind_direction_10m,"
            "wind_gusts_10m"
        ),
           "timezone"  : "auto"},

            timeout= 10
    )

    response.raise_for_status()
    data = response.json()["current"]

    data["condition"] = WEATHER_CODES.get(
        data["weather_code"],
        "Unknown Conditions"
    )

    data["city"] = location["name"]
    data["country"] = location.get("country", "unknown")

    return data
