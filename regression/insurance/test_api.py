import requests

data = {'age': 19, 'sex': 'female', 'bmi': 27.9, 'children': 0, 'smoker': 'yes', 'region': 'southwest'}

response = requests.post(url='http://127.0.0.1:5000/predict', json=data)

print(response.json())
