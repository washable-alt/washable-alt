import requests
from dotenv import load_dotenv
import os 

load_dotenv()

TOKEN = os.getenv("TOKEN")

USERNAME = os.getenv("MY_USERNAME")


url = "https://pixe.la/v1/users"

parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

response = requests.post(url, json=parameters)

print(response.text)

graph_endpoint = f"{url}/{USERNAME}/graphs"

graph_config = {
    "id": "graph0",
    "name": "Cycling Graph", 
    "unit": "Km",
    "type": "float",
    "color": "momiji"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

graph_response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(graph_response.text)