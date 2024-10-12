import requests

data = {'id': 0, 
        'cap-diameter': 8.8, 
        'cap-shape': 'f', 
        'cap-surface': 's', 
        'cap-color': 'u', 
        'does-bruise-or-bleed': 'f', 
        'gill-attachment': 'a', 
        'gill-spacing': 'c', 
        'gill-color': 'w', 
        'stem-height': 4.51, 
        'stem-width': 15.39, 
        'stem-root': None, 
        'stem-surface': None, 
        'stem-color': 'w', 
        'veil-type': None, 
        'veil-color': None, 
        'has-ring': 'f', 
        'ring-type': 'f', 
        'spore-print-color': None, 
        'habitat': 'd', 
        'season': 'a'
        }

response = requests.post(url='http://127.0.0.1:5000/predict', json=data)

print(response.json())
