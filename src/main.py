from utils import banner
from weather_service import get_weather

def main():
    banner()
    while True:
        city = input("\nEnter a city (or 'exit' to quit): ").strip()
        if city.lower() == "exit":
            print("Goodbye!")
            break
        get_weather(city)

if __name__ == "__main__":
    main()
