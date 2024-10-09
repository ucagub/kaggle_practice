import requests

data = {
    'ph': 1.0,
    'Hardness': 1.0,
    'Solids': 1.0,
    'Chloramines': 1.0,
    'Sulfate': 1.0,
    'Conductivity': 1.0,
    'Organic_carbon': 1.0,
    'Trihalomethanes': 1.0,
    'Turbidity': 1.0
}

response = requests.post(url='http://127.0.0.1:5000/predict', json=data)
print(response.json())