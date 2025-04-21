# 🌦️ Weather Checker

A modern and responsive web application built with **FastAPI** and **Jinja2** that fetches real-time weather data using the **OpenWeatherMap API**. Designed with a clean and mobile-friendly UI and deployed on **Vercel**.

## 🔗 Live Demo
Check it out live here: [Weather Checker App](https://weather-web-api-git-main-christophers-projects-9ac7965f.vercel.app/)

## ✨ Features

- 🔍 Search weather by city
- 📡 Real-time data from OpenWeatherMap
- 💻 Clean and responsive UI
- 🧭 Weather condition icons
- ☁️ FastAPI backend with HTML templating (Jinja2)
- 🚀 Deployed on Vercel

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- FastAPI
- Uvicorn
- Jinja2
- requests

### Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/weather-checker.git
cd weather-checker

2. **Install dependencies:**

```bash
pip install -r requirements.txt
Create a .env file or replace the API_KEY in index.py with your OpenWeatherMap API key.

### Run locally

```bash
uvicorn api.index:app --reload
Visit http://localhost:8000 to view the app.


4. **📦 Directory Structure**

```bash
weather-checker/
│
├── api/
│   ├── index.py
│   ├── templates/
│   │   └── form.html
│   └── static/ (optional, for icons)
├── vercel.json
├── README.md
└── requirements.txt
