import requests

# Example usage
data= {
    "Unnamed: 0": 1,
    "id": 101,
    "Gender": "Male",
    "Customer Type": "Loyal Customer",
    "Age": 30,
    "Type of Travel": "Business travel",
    "Class": "Business",
    "Flight Distance": 1500,
    "Inflight wifi service": 1,
    "Departure/Arrival time convenient": 1,
    "Ease of Online booking": 1,
    "Gate location": 1,
    "Food and drink": 1,
    "Online boarding": 1,
    "Seat comfort": 1,
    "Inflight entertainment": 1,
    "On-board service": 1,
    "Leg room service": 1,
    "Baggage handling": 1,
    "Checkin service": 1,
    "Inflight service": 1,
    "Cleanliness": 1,
    "Departure Delay in Minutes": 5,
    "Arrival Delay in Minutes": None,
    "satisfaction": "satisfied"
}
response = requests.post(url='http://127.0.0.1:5000/predict', json=data)
print(response.json())
