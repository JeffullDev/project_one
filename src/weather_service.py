import requests
from colorama import Fore, Style

API_URL = "https://api.open-meteo.com/v1/forecast"

def get_weather(city):
    print(f"{Fore.CYAN}Fetching weather for {city}...{Style.RESET_ALL}")
    try:
        # Obtener coordenadas aproximadas de la ciudad
        geo = requests.get(f"https://geocoding-api.open-meteo.com/v1/search?name={city}").json()
        if not geo.get("results"):
            print(f"{Fore.RED}City not found.{Style.RESET_ALL}")
            return None

        lat = geo["results"][0]["latitude"]
        lon = geo["results"][0]["longitude"]

        params = {
            "latitude": lat,
            "longitude": lon,
            "current_weather": True
        }

        response = requests.get(API_URL, params=params).json()
        weather = response.get("current_weather")

        if weather:
            print(f"{Fore.GREEN}Temperature: {weather['temperature']}°C")
            print(f"Wind Speed: {weather['windspeed']} km/h{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}Could not retrieve weather data.{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}Error: {e}{Style.RESET_ALL}")
