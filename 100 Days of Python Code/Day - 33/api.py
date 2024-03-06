import requests
import datetime as dt
import smtplib
import time

my_email = "jmkl0987@gmail.com"
password = "izoq ufhc fooq eyvh"
MY_LAT = 18.563919
MY_LONG = 73.909525


def iss_above():
    #getting iss position using API
    response1 = requests.get(url="http://api.open-notify.org/iss-now.json")
    response1.raise_for_status()
    data_iss = response1.json()
    long = float(data_iss["iss_position"]["longitude"])
    lat = float(data_iss["iss_position"]["latitude"])
    print(long, lat)

    #checking when is the sunrise and the sunset in my location
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
        "tzid": "Asia/Kolkata"
    }
    response2 = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response2.raise_for_status()

    data_sun = response2.json()
    sunrise = int(data_sun["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data_sun["results"]["sunset"].split("T")[1].split(":")[0])
    now = dt.datetime.now()
    current_hour = now.hour

    #Sending an email to myself if ISS is above me during night time
    if 15<long<21 and 70<lat<77:
        if current_hour<sunrise or current_hour>sunset:
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=my_email, password=password)
                connection.sendmail(
                    from_addr=my_email,
                    to_addrs=my_email,
                    msg=f"Subject:ISS Alert\n\nLook into the sky ISS is right above you"
                )

    time.sleep(60)
    iss_above()

iss_above()