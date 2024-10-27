import requests

data = {'message': 'What is AQI air quality'}

response = requests.post(url='http://127.0.0.1:5000/', json=data)

print(response.json())