import os
import requests

class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self):
        self.TEQUILA_API_KEY = os.environ['TEQUILLA_API_KEY']
        self.TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com/locations/query"
        self.tequila_header = {
            "apikey": self.TEQUILA_API_KEY
        }

    #Gets the IATA Code for cities in sheet
    def iata_code(self,city):
        tequila_parameter = {
            "term": city
        }
        response3 = requests.get(url=self.TEQUILA_ENDPOINT, params=tequila_parameter, headers=self.tequila_header)
        response3.raise_for_status()
        data2 = response3.json()
        code = (data2["locations"][0]["code"])

        parameter = {
            "price": {
                "iataCode": code
            }
        }
        return parameter