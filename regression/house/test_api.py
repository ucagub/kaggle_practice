import requests

data = {'date': '20141013T000000', 'bedrooms': 3, 'bathrooms': 1.0, 'sqft_living': 1180, 'sqft_lot': 5650, 'floors': 1.0, 'waterfront': 0, 'view': 0, 'condition': 3, 'grade': 7, 'sqft_above': 1180, 'sqft_basement': 0, 'yr_built': 1955, 'yr_renovated': 0, 'zipcode': 98178, 'lat': 47.5112, 'long': -122.257, 'sqft_living15': 1340, 'sqft_lot15': 5650}

response = requests.post(url='http://127.0.0.1:5000/predict', json=data)

print(response.json())