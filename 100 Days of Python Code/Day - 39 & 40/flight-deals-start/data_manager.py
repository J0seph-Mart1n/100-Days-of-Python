import os
import requests

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        #Initialization of constants
        self.SHETTY_TOKEN = os.environ["SHETTY_TOKEN"]
        self.SHETTY_ENDPOINT_FLIGHT = "https://api.sheety.co/a70e2c349fde2e4a56c7fc50701f63fd/lowFlightDeals/prices"
        self.SHETTY_ENDPOINT_CLUB = "https://api.sheety.co/a70e2c349fde2e4a56c7fc50701f63fd/lowFlightDeals/users"
        self.header = {
            "Authorization": self.SHETTY_TOKEN
        }

    #Gets data from Low Flight Deals in Google sheets
    def sheet_data(self):
        response = requests.get(url=self.SHETTY_ENDPOINT_FLIGHT, headers=self.header)
        data = response.json()
        return data

    #Puts in IATA Code in the sheet
    def sheet_iata(self,parameter,row_id):
        response2 = requests.put(url=f"{self.SHETTY_ENDPOINT_FLIGHT}/{row_id}", json=parameter)
        return response2.text

    #Gets all the data of users in sheet
    def get_email(self):
        response = requests.get(url=self.SHETTY_ENDPOINT_CLUB, headers=self.header)
        data = response.json()
        return data

    #Inserts new user details in google sheet
    def put_details(self,fname,lname,email):
        parameters = {
            "user":{
                "firstName":fname,
                "lastName":lname,
                "email":email
            }
        }
        response = requests.post(url=f"{self.SHETTY_ENDPOINT_CLUB}", json=parameters, headers=self.header)
        print(response.text)