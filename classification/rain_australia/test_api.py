import requests

data = {
    'Date': 20230101,  # Example date as an integer (YYYYMMDD)
    'Location': 'Sydney',  # Example location as a string
    'MinTemp': 15.5,  # Minimum temperature in degrees Celsius
    'MaxTemp': 28.0,  # Maximum temperature in degrees Celsius
    'Rainfall': 0.0,  # Rainfall amount in millimeters
    'Evaporation': 3.2,  # Evaporation amount in millimeters
    'Sunshine': 10.5,  # Sunshine hours
    'WindGustDir': 'NE',  # Wind gust direction as a string
    'WindGustSpeed': 35.0,  # Wind gust speed in km/h
    'WindDir9am': 'E',  # Wind direction at 9 AM
    'WindDir3pm': 'NW',  # Wind direction at 3 PM
    'WindSpeed9am': 10.0,  # Wind speed at 9 AM
    'WindSpeed3pm': 15.0,  # Wind speed at 3 PM
    'Humidity9am': 75.0,  # Humidity percentage at 9 AM
    'Humidity3pm': 60.0,  # Humidity percentage at 3 PM
    'Pressure9am': 1012.5,  # Atmospheric pressure at 9 AM
    'Pressure3pm': 1010.0,  # Atmospheric pressure at 3 PM
    'Cloud9am': 4.0,  # Cloud cover at 9 AM (e.g., on a scale from 0 to 8)
    'Cloud3pm': 3.0,  # Cloud cover at 3 PM
    'Temp9am': 18.0,  # Temperature at 9 AM
    'Temp3pm': 26.0,  # Temperature at 3 PM
    'RainToday': 'Yes'  # Indicates if it rained today (Yes/No)
}
res = requests.post(url='http://127.0.0.1:5000/predict', json=data)
print(res.json())