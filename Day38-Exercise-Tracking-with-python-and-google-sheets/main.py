import requests
from datetime import datetime
import os
from dotenv import load_dotenv


load_dotenv()
# My personal data. Used by Nutritionix to calculate calories. 
GENDER = os.getenv("GENDER")
WEIGHT_KG = os.getenv("WEIGHT_KG")
HEIGHT_CM = os.getenv("HEIGHT_CM")
AGE = os.getenv("AGE")

# Nutritionix APP ID and API Key. Actual values are stroed as environment variables.
APP_ID = os.getenv("NUTRITIONIX_APP_ID")
API_KEY = os.getenv("NUTRITIONIX_API_KEY")

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercises you did: ")


# Nutritionix API Call
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(f"Nutritionix API call: \n {result} \n")

# Adding date and time
# Change this datetime object to a string
today_date = datetime.utcnow().now().strftime(r"%d/%m/%Y")
print(today_date)
print(type(today_date))
now_time = datetime.utcnow().now().strftime(r"%X")
print(now_time)
print(type(now_time))

# Sheety Project API: Check Google Sheet name and Sheety endpoint
GOOGLE_SHEET_NAME = "sheet1"
SHEETY_ENDPOINT = os.getenv("SHEETY_ENDPOINT")

print(result["exercises"])

for exercise in result["exercises"]:
    # make the first letter to be capitalized
    #print(exercise["name"].title())
    sheet_inputs = {
        GOOGLE_SHEET_NAME: {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    
# Sheety Authentication Option 1: No Auth
"""
sheet_response = requests.post(SHEETY_ENDPOINT, json=sheet_inputs)
"""
#try:
#    sheet_response = requests.post(SHEETY_ENDPOINT, json=sheet_inputs)
#
#    print(f"Sheety Response: \n {sheet_response.text}")
#
#except Exception as e:
#    print(e)
#
## Sheety Authentication Option 2: Basic Auth
#SHEETY_USERNAME = os.getenv("SHEETY_USERNAME")
#SHEETY_PASSWORD = os.getenv("SHEETY_PASSWORD")
#try:
#    basic_auth = os.getenv("SHEETY_BASIC_AUTH")
#    auth_headers = {
#        "Authorization": f"Basic {basic_auth}" 
#    }
#    sheet_response = requests.post(
#        SHEETY_ENDPOINT,
#        json=sheet_inputs,
#        headers=auth_headers
#        )
#    print(f"Sheety Response: \n {sheet_response.text}")
#    
#except Exception as e:
#    print(e)
#
try:
    token = os.getenv("SHEETY_TOKEN")
    bearer_headers = {
        "Authorization": f"Bearer {token}"
    }
    sheet_response = requests.post(
        SHEETY_ENDPOINT,
        json=sheet_inputs,
        headers=bearer_headers
    )
    print(f"Sheety Response: \n {sheet_response.text}")
except Exception as e:
    print(e)

## delete an row of id 2 (row 2)
#try: 
#    token = os.getenv("SHEETY_TOKEN")
#    bearer_headers = {
#        "Authorization": f"Bearer {token}"
#    }
#    sheet_response = requests.delete(
#        f"{SHEETY_ENDPOINT}/2",
#        json=sheet_inputs,
#        headers=bearer_headers
#    )
#    print(f"Sheety Response: \n {sheet_response.text}")
#except Exception as e:
#    print(e)

# Filtering Rows - Filter activity called Swimming
#try:
#    token = os.getenv("SHEETY_TOKEN")
#    bearer_headers = {
#        "Authorization": f"Bearer {token}"
#    }
#    filter_endpoint = "?filter[exercise]=Swimming"
#    sheet_response = requests.get(
#        f"{SHEETY_ENDPOINT}{filter_endpoint}", 
#        json=sheet_inputs,
#        headers=bearer_headers
#    )
#    print(f"Sheety Response: \n {sheet_response.text}")
#except Exception as e:
#    print(e)