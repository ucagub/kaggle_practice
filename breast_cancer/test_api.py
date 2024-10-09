import requests

data = {'mean_radius': 17.99, 'mean_texture': 10.38, 'mean_perimeter': 122.8, 'mean_area': 1001.0, 'mean_smoothness': 0.1184}

response = requests.post(url='http://127.0.0.1:5000/predict', json=data)
print(response.json())
