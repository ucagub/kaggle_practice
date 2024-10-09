import requests

data = {'Age': 23, 'Sex': 'F', 'BP': 'HIGH', 'Cholesterol': 'HIGH', 'Na_to_K': 25.355}

response = requests.post(url='http://127.0.0.1:5000/predict', json=data)

print(response.json())