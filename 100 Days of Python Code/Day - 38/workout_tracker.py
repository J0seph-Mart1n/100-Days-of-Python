import requests
from datetime import datetime
import os

#Declaring Constants
APP_ID = os.environ["APP_ID"]
APP_KEY = os.environ["APP_KEY"]
SHETTY_TOKEN = os.environ["SHETTY_TOKEN"]
SHETTY_ENDPOINT = os.environ["SHETTY_ENDPOINT"]

HEADERS = {
    'Content-Type': 'application/json',
    'x-app-id': APP_ID,
    'x-app-key': APP_KEY
}

#Constructing Parameter and asking user input
nutrix_parameter = {
    "query": input("Enter your workout: "),
    "gender": "male",
    "weight_kg": 75,
    "height_cm": 188,
    "age": 20
}

host_domain = "https://trackapi.nutritionix.com"
nutrix_endpoint = f"{host_domain}/v2/natural/exercise"

#Posting user's input and generating response
response = requests.post(url=nutrix_endpoint, json=nutrix_parameter, headers=HEADERS)
data = response.json()

today = datetime.now()
date = today.strftime("%d/%m/%Y")
time = today.strftime("%H:%M:%S")

#Getting Exercise name, duration, calories burned, from the JSON Data File
for i in range(len(data["exercises"])):
    exercise = data["exercises"][i]["name"]
    duration = data["exercises"][i]["duration_min"]
    calories = data["exercises"][i]["nf_calories"]
    print(exercise)
    print(duration)
    print(calories)

    header = {
        "Authorization": SHETTY_TOKEN
    }

    parameter = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise.title(),
            "duration": duration,
            "calories": calories
        }
    }

    #Posting the data to google sheets with current time
    response2 = requests.post(url=SHETTY_ENDPOINT, json=parameter, headers=header)
    print(response2.text)