import requests
from datetime import datetime

pixela_endpoint = 'https://pixe.la/v1/users'
USERNAME = "manuels"
TOKEN = "#############"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}


#response = requests.post(url=pixela_endpoint, json=user_params)
#print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    'id': 'graph1',
    "name": 'Cycling Graph',
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

#response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
#print(response.text)

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_config['id']}"

today = datetime(year=2025, month=8, day=31)

pixel_params = {
    'date': today.strftime("%Y%m%d"),
    'quantity': '15'
}

#response = requests.post(url=pixel_endpoint, json=pixel_params, headers=headers)
#print(response.text)


updated_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_config['id']}/{pixel_params['date']}"

updated_params = {
    'quantity': '4'
}

#response = requests.put(url=updated_endpoint, json=updated_params, headers=headers)
#print(response.text)


deleted_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_config['id']}/{pixel_params['date']}"

response = requests.delete(url=deleted_endpoint, headers=headers)
print(response.text)
