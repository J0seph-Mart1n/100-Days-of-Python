import requests
from twilio.rest import Client

API_KEY = "c0757689522bd1f5eba9dd0376635aa9"
MY_LAT = 29.916654
MY_LONG = -90.038116
account_sid = 'AC29a37838a2de0a59bb084fdebc596136'
auth_token = '23919516fe5117c5d86a8b27f4d64669'

parameters = {
    "lat":MY_LAT,
    "lon":MY_LONG,
    "appid":API_KEY,
    "cnt":5
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
data = response.json()
will_rain = False
for i in range(len(data["list"])):
    weather_id = data["list"][i]["weather"][0]["id"]
    if int(weather_id) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="It is going to rain today. Do bring your Umbrella",
        from_='+16562184044',
        to='+919172232178'
    )
    print(message.status)