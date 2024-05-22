import requests
from flight_data import FlightData
import datetime as dt



class FlightSearch(FlightData):
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        super().__init__()
        self.date_from = dt.datetime.now()
        self.date_to = self.date_from + dt.timedelta(days=6 * 30)
        self.date_from = self.date_from.strftime("%d/%m/%Y")
        self.date_to = self.date_to.strftime("%d/%m/%Y")

    #Checks the price of flights
    def price_check(self,city):
        search_parameter = {
            "fly_from": "PNQ",
            "fly_to": city,
            "date_from": self.date_from,
            "date_to": self.date_to,
            "curr": "INR",
            "max_stopovers":0
        }
        response = requests.get(url="https://api.tequila.kiwi.com/v2/search", params=search_parameter, headers=self.tequila_header)

        try:
            data = response.json()["data"][0]
        except IndexError:
            search_parameter["max_stopovers"] = 2
            response = requests.get(url="https://api.tequila.kiwi.com/v2/search", params=search_parameter, headers=self.tequila_header)
            data = response.json()["data"][0]
            price = [data["price"], data["route"][0]["cityTo"]]
            return price

        price = [data["price"]]
        return price