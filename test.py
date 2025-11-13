import app
import requests
import json
url="http://127.0.0.1:8000/predict"
test_sample =[
    {
        "tenure": 1,
        "TechSupport": "No",
        "MonthlyCharges": 400.35,
        "InternetService": "Fiber optic",
        "Contract": "Month-to-month",
        "PaymentMethod": "Electronic check"
    }]

predictions=requests.post(url,json=test_sample)
print(predictions.status_code)
print(predictions.text)
print(predictions.json())