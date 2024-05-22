from data_finder import DataFinder
from form_filler import FormFiller

data_finder = DataFinder()
house_address = data_finder.house_address_finder()
house_price = data_finder.house_price_finder()
house_link = data_finder.house_link_finder()

print(len(house_address),len(house_price), len(house_link))

form_filler = FormFiller()
for i in range(44):
    form_filler.fill_form(house_address[i],house_price[i],house_link[i])