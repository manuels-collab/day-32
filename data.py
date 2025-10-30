import requests


paramters = {
    'amount': 10,
    'category': 21,
    'type': 'boolean'
}
response = requests.get("https://opentdb.com/api.php", params=paramters)

data = response.json()
#print(response.json()['results'][0])

question_data = []
for item in data['results']:
    question_data.append(item)