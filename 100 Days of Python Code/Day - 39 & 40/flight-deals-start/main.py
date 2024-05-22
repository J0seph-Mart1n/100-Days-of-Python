#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from flight_data import FlightData
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

#Declaring classes
flightData = FlightData()
dataManager = DataManager()
flightSearch = FlightSearch()
data = dataManager.sheet_data()
notificationManager = NotificationManager()

#Asking new users to join the club
# print("Welcome to the Ultimate Flight Club!")
# print("We find you the best flight deals and mail you")
# print("What is your first name?")
# user_fname = input()
# print("What is your last name?")
# user_lname = input()
# while True:
#     print("What is your email?")
#     user_gmail = input()
#     print("Enter your email again")
#     confirm_email = input()
#     if user_gmail == confirm_email:
#         print("You are in the club")
#         dataManager.put_details(user_fname,user_lname,user_gmail)
#         break
#     else:
#         print("Enter the same email.")

user_data = dataManager.get_email()
print(user_data)
print(data)
#Sending SMS or Gmail to user if prices are low
for city in data["prices"]:
    # parameter = flightData.iata_code(city["city"])
    # text = dataManager.sheet_iata(parameter,city['id'])
    # print(text)
    price = flightSearch.price_check(city["iataCode"])
    if len(price) == 2:
        sms_text = f"Low price alert! Only Rs {price[0]} to fly from Pune-PNQ to {city['city']}-{city['iataCode']}, from {flightSearch.date_from} to {flightSearch.date_to}.\nFlight has 1 stop over, via {price[1]}."
    else:
        sms_text = f"Low price alert! Only Rs {price[0]} to fly from Pune-PNQ to {city['city']}-{city['iataCode']}, from {flightSearch.date_from} to {flightSearch.date_to}."
    if int(price[0]) < int(city["lowestPrice"]):
        # notificationManager.send_sms(
        #     message=sms_text
        # )
        print(f"{city['city']}: Rs {price[0]}")
        for email in user_data["users"]:
            sender_email = email["email"]
            notificationManager.send_email(sms_text,sender_email)



