import requests
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")

API_KEY = 'e69fe9a03a69cd4bfb4b41486a78858f'

user_input = input("Enter City: ")


weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={API_KEY}")

if weather_data.json()['cod'] == '404':
    print("Invalid City")
else:
    weather = weather_data.json()['weather'][0]['main']
    temperature = round(weather_data.json()['main']['temp'])

    print(f"The weather in {user_input} is: {weather}")
    print(f"The temperature in {user_input} is: {temperature} degrees")

