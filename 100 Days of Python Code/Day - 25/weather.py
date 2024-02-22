# with open('weather_data.csv') as file:
#     weather = file.readlines()
#
# print(weather)

import csv

# with open('weather_data.csv') as file:
#     weather = csv.reader(file)
#     temperature = []
#     for info in weather:
#         temperature.append(info[1])
#     temperature.pop(0)
#     int_temperature = [int(temp) for temp in temperature]
#     print(int_temperature)

import pandas as pd
import math

data = pd.read_csv('weather_data.csv')
# print(data['temp'])
# dict_data = data.to_dict()
# print(dict_data)
# temp_list = data['temp'].to_list()
# print(sum(temp_list)/len(temp_list))
#
# print(data['temp'].mean())
# print(data['temp'].max())
#
# #Get columns of weather_data
# print(data.condition)
# print(data['condition'])

# #Get rows of weather_data
# print(data[data.temp == data.temp.max()])
#
# #Get rows and columns of weather_data
# print(data[data.temp == data.temp.max()].condition)
#
# mon_temp = data[data.day == 'Monday'].temp
# print(((mon_temp)*9/5)+32)

squirrel_data = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
fur_color_gray = (squirrel_data[squirrel_data["Primary Fur Color"] == 'Gray']["Primary Fur Color"])
fur_color_cinnamon = (squirrel_data[squirrel_data["Primary Fur Color"] == 'Cinnamon']["Primary Fur Color"])
fur_color_black = (squirrel_data[squirrel_data["Primary Fur Color"] == 'Black']["Primary Fur Color"])
print(len(fur_color_black),len(fur_color_gray),len(fur_color_cinnamon))

data_set = {
    'Fur Color':['Black','Cinnamon','Gray'],
    'Count':[len(fur_color_black),len(fur_color_cinnamon),len(fur_color_gray)]
}

squirrel_dataframe = pd.DataFrame(data_set)
squirrel_dataframe.to_csv('squirrel_count.csv')

