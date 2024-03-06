##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import datetime as dt
import smtplib
import pandas as pd

my_email = "jmkl0987@gmail.com"
password = "izoq ufhc fooq eyvh"

#Reading birthdays.csv file
birthdays = pd.read_csv("birthdays.csv")
dict_birthdays = birthdays.to_dict()

#taking today's time and creating an empty list to store birthday's of today
now = dt.datetime.now()
today_birthday = []

#checking for birthdays
for i in range(len(dict_birthdays['name'])):
    if now.day == dict_birthdays['day'][i] and now.month == dict_birthdays['month'][i]:
        today_birthday.append([dict_birthdays['name'][i],dict_birthdays['email'][i]])

#opening letter_2.txt
with open('letter_templates/letter_2.txt', 'r') as file:
    content = file.readlines()
letter = ''.join(content)

#generating birthday letters
for j in range(len(today_birthday)):
    new_letter = letter.replace("[NAME]", today_birthday[j][0])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=today_birthday[j][1],
            msg=f"Subject:Happy Birthday {today_birthday[j][0]}\n\n{new_letter}"
        )