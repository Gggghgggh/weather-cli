# ☁️ Weather CLI Tool (Python)

A simple and fun command-line tool to check the current weather for any city using the OpenWeatherMap API. Built with Python 🐍.

---

## ✨ Demo

      $ python weather.py Nairobi
      Weather in Nairobi:
      🌤  Clear sky  
      🌡️  Temperature: 25°C  
      💨  Wind: 5.2 m/s  
      💧  Humidity: 58%
      
## 🔧 Features

•	Get current weather conditions for any city

• Uses OpenWeatherMap API for real-time data

• Easy to use, lightweight, and extensible

• Can be extended into a web API or app

## 📦 Requirements
Python 3.6+

requests library

OpenWeatherMap API key (free)

## ⚙️ Setup Instructions

1. Clone the repo:
   
       git clone https://github.com/your-username/weather-cli.git
       cd weather-cli
   
2. Create a virtual environment (optional but recommended)
   ```bash
      python -m venv venv
      # Activate it:
      source venv/bin/activate       # macOS/Linux
      venv\Scripts\activate          # Windows (CMD)
      venv\Scripts\Activate.ps1      # Windows (PowerShell)
   
3. Install dependencies
      ```bash
      pip install requests
   
 Or from requirements.txt:
 
       pip install -r requirements.txt
         
4. Add your API key:
Get a free API key from OpenWeatherMap, then open weather.py and replace:

    ```python
        API_KEY = "your_openweather_api_key"
with your actual API key (inside quotes).

🚀 Usage
To check the weather for any city:

    ``bash
      python weather.py <city name>
Examples:

    ```bash
        python weather.py Nairobi
        python weather.py Tokyo
        python weather.py "New York"

## 📁 Project Structure
    ```bash
    
        weather-cli/
        │
        ├── weather.py          # Main CLI script
        ├── requirements.txt    # Dependencies
        ├── .gitignore          # Git ignored files
        ├── README.md           # This file
        └── venv/               # (optional) virtual environment
        
## 🙌 Acknowledgements:

OpenWeatherMap for the weather data API

