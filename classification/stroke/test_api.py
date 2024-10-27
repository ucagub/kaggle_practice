import requests

data = {
    'id': 1,
    'gender':'Male',
    'age': 1.0,
    'hypertension': 1,
    'heart_disease': 1,
    'ever_married': 'Yes', 
    'work_type': 'Private',
    'Residence_type': 'Urban',
    'avg_glucose_level': 1.0,
    'bmi': 1.0,
    'smoking_status': 'smoked'
}
res = requests.post('http://127.0.0.1:5000/predict', json=data)
print(res.json())
