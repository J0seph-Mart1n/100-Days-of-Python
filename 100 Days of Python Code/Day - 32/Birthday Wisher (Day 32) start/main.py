import smtplib
import datetime as dt
import random

now = dt.datetime.now()

with open("quotes.txt", 'r') as file:
    quotes = file.readlines()

random_quote = random.choice(quotes)

my_email = "jmkl0987@gmail.com"
password = "izoq ufhc fooq eyvh"

if now.weekday() in range(0,5):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"Subject:Motivational Quote\n\n{random_quote}"
        )