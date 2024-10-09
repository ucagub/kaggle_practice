import requests
data = {'gender': 'Female', 'age': 80.0, 'hypertension': 0, 'heart_disease': 1, 'smoking_history': 'never', 'bmi': 25.19, 'HbA1c_level': 6.6, 'blood_glucose_level': 140}

response = requests.post(url='http://127.0.0.1:5000/predict', json=data)
print(response.json())