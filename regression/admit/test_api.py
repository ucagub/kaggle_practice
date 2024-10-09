import requests

data = {'Serial No.': 1.0, 'GRE Score': 337.0, 'TOEFL Score': 118.0, 'University Rating': 4.0, 'SOP': 4.5, 'LOR ': 4.5, 'CGPA': 9.65, 'Research': 1.0}

response = requests.post(url='http://127.0.0.1:5000/predict', json=data)

print(response.json())