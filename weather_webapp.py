import streamlit as st
import requests
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = st.secrets.get("OPENWEATHER_API_KEY", os.getenv("OPENWEATHER_API_KEY"))

st.title("Weather App")

with st.form(key="weather_form"):
    city = st.text_input("Enter City", placeholder="e.g. New York")
    submitted = st.form_submit_button("Get Weather")

if submitted and city:
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID={API_KEY}"
    response = requests.get(url).json()

    if str(response.get("cod")) == "404":
        st.error("Invalid City")
    else:
        weather = response["weather"][0]["main"]
        temperature = round(response["main"]["temp"])
        st.success(f"The weather in {city} is: {weather}")
        st.info(f"The temperature is: {temperature} °F")
