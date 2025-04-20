# weather.py
import requests
import sys
import os

API_KEY = "c8cb3b93e5d3ed1c629e924cfd2ab655"  # Replace with your actual key
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city_name):
    params = {
        "q": city_name,
        "appid": API_KEY,
        "units": "metric"
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if response.status_code != 200:
        print(f"Error: {data.get('message', 'Something went wrong')}")
        return

    weather = data["weather"][0]["description"].capitalize()
    temp = data["main"]["temp"]
    wind = data["wind"]["speed"]
    humidity = data["main"]["humidity"]

    print(f"Weather in {city_name}:")
    print(f"🌤  {weather}")
    print(f"🌡️  Temperature: {temp}°C")
    print(f"💨  Wind: {wind} m/s")
    print(f"💧  Humidity: {humidity}%")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python weather.py <city>")
    else:
        city = " ".join(sys.argv[1:])
        get_weather(city)
