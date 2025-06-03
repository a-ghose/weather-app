# 🌦 Weather App — CLI, Flask Web, and Streamlit

This project is a simple weather app that fetches current weather data using the [OpenWeather API](https://openweathermap.org/api). It's implemented in three different interfaces:

- ✅ **Command-Line Interface (CLI)** — `app.py`
- ✅ **Web App with Flask** — `backend.py + index.html`
- ✅ **Interactive Web App with Streamlit** — `weather_webapp.py`

The project is meant practice building and interacting with REST APIs using Python across multiple platforms.

---

## 🚀 Features

- Fetches real-time weather based on user-entered city
- Displays main weather condition and temperature
- Uses environment variables to keep API keys secure
- Demonstrates frontend-backend separation (Flask)
- Streamlit version includes an instant UI

---

## 🛠 Project Structure

```
weather-app/
├── app.py                # CLI version
├── backend.py            # Flask backend for index.html
├── index.html            # HTML frontend served by Flask
├── weather_webapp.py     # Streamlit interface
├── .env                  # (Not committed) stores API key
├── requirements.txt      # Project dependencies
└── README.md             # You're reading it!
```

---

## 🔐 API Setup

1. Get a free API key from [OpenWeather](https://openweathermap.org/api).
2. Create a `.env` file in the project root:

```
OPENWEATHER_API_KEY=your_actual_api_key_here
```

This file is **ignored in version control** via `.gitignore`.

---

## 📦 Installation

1. Clone the repository:

```
git clone https://github.com/a-ghose/weather-app.git
cd weather-app
```

2. Install the dependencies:

```
pip install -r requirements.txt
```

---

## 🧑‍💻 How to Run

### ▶️ CLI Version (`app.py`)

```
python app.py
```

It will prompt you to enter a city and display the weather in your terminal.

---

### 🌐 Flask Web App (`backend.py + index.html`)

1. Start the backend:

```
python backend.py
```

2. Visit the app in your browser:

```
http://127.0.0.1:5000
```

Type a city and press "Get Weather" — your browser will display the results.

---

### 📊 Streamlit App (`weather_webapp.py`)

```
streamlit run weather_webapp.py
```

You'll get a live dashboard UI in your browser where you can enter a city name and view the results.

---

## 🧹 .gitignore (important)

Be sure to include this in your `.gitignore` to prevent secrets and clutter from being committed:

```
.env
__pycache__/
*.pyc
*.pyo
```

---

## 📝 Notes

- API calls are made via the backend (in `backend.py`) to keep your key secure.
- If you open `index.html` directly from the filesystem, the browser may block it. Always serve it via Flask.
- If you deploy, use environment variables on the platform (Render, Fly.io, etc).

---

## 👤 Author

Built by [Animesh Ghose](https://github.com/a-ghose) to explore multi-interface Python applications and API consumption.
