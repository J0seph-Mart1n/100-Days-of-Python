import requests
from twilio.rest import Client

API_KEY = "api_key"
MY_LAT = "latitude"
MY_LONG = "longitude"
account_sid = 'account_sid'
auth_token = 'auth_token'

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
        to='your_num'
    )
    print(message.status)
