import requests
import pandas as pd
import csv
from pprint import pprint
from pathlib import Path
import json
import pywhatkit
from datetime import datetime, timedelta

BASEURL = "https://api.openweathermap.org/data/3.0/onecall"
#http://api.openweathermap.org/geo/1.0/direct
#https://api.openweathermap.org/data/2.5/weather

api_key = ""

WILL_RAIN = False

parameters = {
    "lat": "1.2899175",
    "lon": "103.8519072",
    #"q": "Singapore", 
    #"lat": "33.44",
    #"lon": "-94.04",
    "appid": api_key,
    "units": "metric",
    #data can be currently, minutely, hourly and daily; we want to access hourly data
    "exclude": "current, minutely, daily"
}

try:
    response = requests.get(BASEURL, params=parameters)
    #pprint(f"1. response: {response}")
    #pprint(f"2. response.text: {response.text}")

    #pprint(f"3. response status: {response.raise_for_status()}")

    data = response.json()

    #pprint(f"4. Data: {data}")
    
    # next 12 hours of weather data
    df = pd.DataFrame(data['hourly'][:12])
    filepath = Path(".\\Day35\\output\\output_onecall_threepointzero.csv")
    filepath.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(filepath)

    with open(".\\Day35\\output\\output.csv", 'r') as file:
        hourly_weather_rows = csv.reader(file, delimiter=',')
        next(hourly_weather_rows, None)
        
        for row in hourly_weather_rows:
            print(row)
            weather = row[13]
            # remove the square brackets
            weather = weather[1:-1]
            #print(weather)

            # Access the dictionary in the list

            # valid json needs to have "" instead of '', double quotes instead of single quotes
            weather = weather.replace("\'", "\"")
            weather_condition = json.loads(weather)
            #print(weather_condition)
            #print(weather_condition['id'])
            #print(type(weather_condition['id']))

            if weather_condition['id'] < 700:
                WILL_RAIN = True

        if WILL_RAIN:
            phone_number = ""
            message = "Bring an Umbrella!"
            pywhatkit.sendwhatmsg_instantly(phone_number, message, 15, True, 2)
            

except requests.HTTPError as error:
    pprint(response.status_code)
    if response.status_code == 401:
        pprint(f"error: {error}")
except Exception as e:
    print(e)