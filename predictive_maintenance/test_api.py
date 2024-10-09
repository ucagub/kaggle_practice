import requests

data = {'UDI': 1, 'Product_ID': 'M14860', 'Type': 'M', 'Air_temperature_K': 298.1, 'Process_temperature_K': 308.6, 'Rotational_speed_rpm': 1551, 'Torque_Nm': 42.8, 'Tool_wear_min': 0, 'Target': 0}
response = requests.post(url="http://127.0.0.1:5000/predict", json=data)

print(response.json())