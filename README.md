Weather CLI App

A simple and functional Python command-line application that shows the current weather for any city in the world using the Open-Meteo API.
It demonstrates the use of virtual environments, modules, dependencies, and version control with Git.

Project Overview

This project was created as part of the Python Virtual Environments and Fundamentals activity.
The main goal is to build a clean, modular, and reproducible Python application that uses external dependencies within an isolated environment.

It uses:

requests → to make HTTP requests to the Open-Meteo API

colorama → to display colored text and a friendly terminal experience

Project Structure

PROJECT_ONE/
│
├── src/
│ ├── main.py
│ ├── utils.py
│ └── weather_service.py
│
├── tests/
│ └── test_weather.py
│
├── requirements.txt
├── .gitignore
├── xi.yml
└── README.md

Setup Instructions

Create and activate a virtual environment

Windows (PowerShell):
python -m venv .venv
.venv\Scripts\Activate.ps1

macOS / Linux:
python3 -m venv venv
source venv/bin/activate

Install dependencies
Once your virtual environment is active, install all required packages:

pip install -r requirements.txt

Your requirements.txt should contain:
requests
colorama

Run the application
Launch the app directly from the root directory:

python src/main.py

Example output:

==============================
🌤 WEATHER CLI APP

Enter a city: Bogotá
Fetching weather for Bogotá...
Temperature: 18°C
Wind Speed: 3 km/h

How It Works

The user enters a city name.

The program sends a request to the Open-Meteo Geocoding API to find coordinates.

Using those coordinates, it fetches real-time weather data.

The information is displayed in a clean and colored format in the terminal.

No API key is required, since Open-Meteo provides a free and open public endpoint.

Git Workflow

The repository follows a simple GitFlow-inspired structure:

main
└── develop
  ├── feature/setup-venv
  ├── feature/weather-service
  ├── feature/utils-banner
  ├── feature/main-cli
  ├── feature/tests
  ├── feature/docs-readme
  └── release/v1.0.0

Each feature branch focuses on one functionality and is merged into develop after testing.
When everything is stable, develop is merged into main for the official release.

Good Practices Followed

✔ Virtual environment properly configured (venv/)
✔ Dependencies listed and frozen in requirements.txt
✔ Organized modular code under src/
✔ Clean, descriptive commit messages
✔ Public repository on GitHub with reproducible instructions
✔ Clear and human-friendly documentation

Author

Developed independently by Jeffry López, as part of the Python Fundamentals module.
Aiming for simplicity, clarity, and maintainability — proof that even small scripts can follow professional software practices.

License

This project is open-source and available for educational purposes.
Feel free to fork, test, and extend it with new features.