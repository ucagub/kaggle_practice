import requests

data = {
    'enrollee_id': 1,
    'city':'city_103',
    'city_development_index': 1.0,
    'gender': 'Male',
    'relevent_experience': 'Has relevant experience',
    'enrolled_university':'no_enrollment',
    'education_level': 'Graduate',
    'major_discipline': 'STEM',
    'experience': 15,
    'company_size': '50-99',
    'company_type': 'Pvt Ltd', 
    'last_new_job': 'never', 
    'training_hours': 1
}

response = requests.post(url='http://127.0.0.1:5000/predict', json=data)
print(response.json())