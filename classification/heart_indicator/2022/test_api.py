import requests

sample_data = {
    "State": "Alabama",
    "Sex": "Female",
    "GeneralHealth": "Very good",
    "PhysicalHealthDays": 0.0,
    "MentalHealthDays": 0.0,
    "LastCheckupTime": "Within past year (anytime less than 12 months ago)",
    "PhysicalActivities": "No",
    "SleepHours": 8.0,
    "RemovedTeeth": None,  # NaN equivalent in Python
    "HadHeartAttack": "No",
    "HadAngina": "No",
    "HadStroke": "No",
    "HadAsthma": "No",
    "HadSkinCancer": "No",
    "HadCOPD": "No",
    "HadDepressiveDisorder": "No",
    "HadKidneyDisease": "No",
    "HadArthritis": "No",
    "HadDiabetes": "Yes",
    "DeafOrHardOfHearing": "No",
    "BlindOrVisionDifficulty": "No",
    "DifficultyConcentrating": "No",
    "DifficultyWalking": "No",
    "DifficultyDressingBathing": "No",
    "DifficultyErrands": "No",
    "SmokerStatus": "Never smoked",
    "ECigaretteUsage": "Not at all (right now)",
    "ChestScan": "No",
    "RaceEthnicityCategory": "White only, Non-Hispanic",
    "AgeCategory": "Age 80 or older",
    "HeightInMeters": None,  # NaN equivalent in Python
    "WeightInKilograms": None,  # NaN equivalent in Python
    "BMI": None,  # NaN equivalent in Python
    "AlcoholDrinkers": "No",
    "HIVTesting": "No",
    "FluVaxLast12": "Yes",
    "PneumoVaxEver": "No",
    "TetanusLast10Tdap": 'Yes, received tetanus shot but not sure what type',
    "HighRiskLastYear": "No"
}

response = requests.post(url='http://127.0.0.1:5000/predict', json=sample_data)
print(response.json())