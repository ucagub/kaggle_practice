import requests

data = {'Education': 'Bachelors', 'JoiningYear': 2017, 'City': 'Bangalore', 'PaymentTier': 3, 'Age': 34, 'Gender': 'Male', 'EverBenched': 'No', 'ExperienceInCurrentDomain': 0}

response = requests.post(url='http://127.0.0.1:5000/predict', json=data)

print(response.json())