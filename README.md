# 🌦️ Weather CLI

A simple Python CLI tool that fetches real-time weather data for any city using the OpenWeatherMap API.

---

## 🔧 Features

- Get current weather by city name
- Outputs temperature, humidity, wind, and weather conditions
- Lightweight and easy to use

---

## 🛠️ Requirements

- Python 3.7+
- `requests` library

---

## 🚀 Setup Instructions

1. **Clone the repo**
   ```bash
   git clone https://github.com/your-username/weather-cli.git
   cd weather-cli
Create and activate a virtual environment

bash
Copy
Edit
python -m venv venv
source venv/bin/activate     # On Windows: venv\Scripts\activate
Install dependencies

bash
Copy
Edit
pip install requests
Add your API key

Open weather.py and replace:

python
Copy
Edit
API_KEY = "your_openweather_api_key"
with your actual API key from OpenWeatherMap.

📦 Usage
bash
Copy
Edit
python weather.py Nairobi
Example output:

yaml
Copy
Edit
Weather in Nairobi:
🌤  Clear sky
🌡️  Temperature: 26°C
💨  Wind: 4.7 m/s
💧  Humidity: 60%
🧪 Sample Cities to Try
Nairobi

New York

London

Tokyo

Mumbai
