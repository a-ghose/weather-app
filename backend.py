from flask import Flask, request, jsonify, send_from_directory
import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")

if not API_KEY:
    raise RuntimeError("OPENWEATHER_API_KEY not found in environment variables")

app = Flask(__name__)

@app.route("/")
def index():
    return send_from_directory(".", "index.html")  # "." = current directory

@app.route("/weather")
def weather():
    city = request.args.get("city")
    if not city:
        return jsonify({"error": "City not provided"}), 400

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&appid={API_KEY}"
    
    try:
        response = requests.get(url)
        data = response.json()

        if data.get("cod") == "404":
            return jsonify({"cod": "404", "message": "City not found"}), 404

        return jsonify(data)
    except Exception as e:
        print("Error contacting OpenWeather API:", e)
        return jsonify({"error": "Failed to fetch weather data"}), 500

if __name__ == "__main__":
    app.run(debug=True)
