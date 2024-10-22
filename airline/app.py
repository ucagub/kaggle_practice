from typing import Optional
from flask import Flask, jsonify, request
from pydantic import BaseModel, ValidationError, Field
import pickle
import pandas as pd

class Flight(BaseModel):
    id: int
    gender: object = Field(..., alias='Gender')
    customer_type: object = Field(..., alias='Customer Type')
    age: int = Field(..., alias='Age')
    type_of_travel: object = Field(..., alias='Type of Travel')
    flight_class: object = Field(..., alias='Class')
    flight_distance: int = Field(..., alias='Flight Distance')
    inflight_wifi_service: int = Field(..., alias='Inflight wifi service')
    departure_arrival_time_convenient: int = Field(..., alias='Departure/Arrival time convenient')
    ease_of_online_booking: int = Field(..., alias='Ease of Online booking')
    gate_location: int = Field(..., alias='Gate location')
    food_and_drink: int = Field(..., alias='Food and drink')
    online_boarding: int = Field(..., alias='Online boarding')
    seat_comfort: int = Field(..., alias='Seat comfort')
    inflight_entertainment: int = Field(..., alias='Inflight entertainment')
    onboard_service: int = Field(..., alias='On-board service')
    leg_room_service: int = Field(..., alias='Leg room service')
    baggage_handling: int = Field(..., alias='Baggage handling')
    checkin_service: int = Field(..., alias='Checkin service')
    inflight_service: int = Field(..., alias='Inflight service')
    cleanliness: int = Field(..., alias='Cleanliness')
    departure_delay_in_minutes: int = Field(..., alias='Departure Delay in Minutes')
    arrival_delay_in_minutes: object = Field(None, alias='Arrival Delay in Minutes')

with open('pipeline.pkl', 'rb') as file:
    loaded_pipeline = pickle.load(file)

with open('label_encoder.pkl', 'rb') as file:
    loaded_le = pickle.load(file)

# print(sample_row)
# flight = Flight(**sample_row)
# inputs = pd.DataFrame([flight.model_dump(by_alias=True)])
# pred = loaded_pipeline.predict(inputs)
# actual_pred = loaded_le.inverse_transform(pred)[0]
# actual_pred
app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        flight = Flight(**request.json)
        inputs = pd.DataFrame([flight.model_dump(by_alias=True)])
        pred = loaded_pipeline.predict(inputs)
        actual_pred = loaded_le.inverse_transform(pred)[0]
        response = {
            'prediction': actual_pred
        }
        return jsonify(response), 200
    except ValidationError as e:
        return jsonify(e.errors()), 400


if __name__ == '__main__':
    app.run()

