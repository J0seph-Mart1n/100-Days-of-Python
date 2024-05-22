import requests
import datetime
import os

USERNAME = "yourusername"
TOKEN = os.environ['TOKEN']
GRAPH_ID = "graph1"

#use https://pixe.la/v1/users/j0sephmart1n/graphs/graph1.html to view the heat map
#TODO:Account creation
pixela_endpoint = "https://pixe.la/v1/users"
parameters = {
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=parameters)
# print(response.text)

#TODO:Creating graph
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_parameter = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "shibafu"
}

header = {
    "X-USER-TOKEN": TOKEN
}

# response2 = requests.post(url=graph_endpoint, json=graph_parameter, headers=header)
# print(response2.text)

#TODO:Plotting pixel to the graph
pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
today = datetime.datetime.now()
DATE = today.strftime("%Y%m%d")

pixel_parameter = {
    "date": DATE,
    "quantity": "8.2",
}

# response3 = requests.post(url=pixel_endpoint,json=pixel_parameter, headers=header)
# print(response3.text)

#TODO:Updating Pixel value
update_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{DATE}"

update_parameter = {
    "date": DATE,
    "quantity": "3.3"
}

response4 = requests.put(url=update_pixel_endpoint,json=update_parameter, headers=header)
print(response4.text)

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{DATE}"

# response5 = requests.delete(url=delete_endpoint, headers=header)
# print(response5.text)