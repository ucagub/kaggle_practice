import requests

payload = {
    'title': 'Saving Private Ryan (1998)'
}

response = requests.post(url='http://127.0.0.1:5000/recommend', json=payload)
print(response.json())