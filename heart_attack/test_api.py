import requests


data = {
    'age': 1,
    'sex': 1,
    'cp': 1,
    'trtbps': 1,
    'chol': 1,
    'fbs': 1,
    'restecg': 1,
    'thalachh': 1,
    'exng': 1,
    'oldpeak': 1.0,
    'slp': 1,
    'caa': 1,
    'thall': 1
}

response = requests.post(url='http://127.0.0.1:5000/predict', json=data)


print(response.json())