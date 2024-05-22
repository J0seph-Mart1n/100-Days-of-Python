from bs4 import BeautifulSoup
import requests
from form_filler import FormFiller

class DataFinder:

    def __init__(self) -> None:
        self.house_link_list = []
        self.house_price_list = []
        self.house_address_list = []
        response = requests.get(url="https://appbrewery.github.io/Zillow-Clone/?")
        zillow_website = response.text
        self.soup = BeautifulSoup(zillow_website, "html.parser")

    def house_link_finder(self):
        apartment = self.soup.find_all(name='a', class_='StyledPropertyCardDataArea-anchor')
        for house_link in apartment:
            link = (house_link['href'])
            self.house_link_list.append(link)
        return self.house_link_list 

    def house_price_finder(self):
        price = self.soup.find_all(name='span', class_='PropertyCardWrapper__StyledPriceLine')
        for house_price in price:
            price_value = house_price.text
            price_value = price_value[0:6]
            price_value = price_value.replace('+','')
            self.house_price_list.append(price_value)
        return self.house_price_list

    def house_address_finder(self):
        address = self.soup.find_all(name='address')
        for home_address in address:
            home_address = home_address.text
            home_address = home_address.strip()
            home_address = home_address.replace('|','')
            self.house_address_list.append(home_address)
        return self.house_address_list