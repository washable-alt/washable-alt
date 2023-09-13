import requests
import pandas as pd
import csv
from pprint import pprint
from pathlib import Path
import pywhatkit

BASEURL = "https://api.openweathermap.org/data/2.5/weather"


api_key = ""

# Current weather data
parameters = {
    "lat": "1.2899175",
    "lon": "103.8519072",
    #"q": "Singapore", 
    #"lat": "33.44",
    #"lon": "-94.04",
    "appid": api_key,
    "units": "metric",
        
}

try:
    response = requests.get(BASEURL, params=parameters)
    #pprint(f"1. response: {response}")
    #pprint(f"2. response.text: {response.text}")

    #pprint(f"3. response status: {response.raise_for_status()}")

    data = response.json()

    #pprint(f"4. Data: {data}")
    
    # next 12 hours of weather data
    df = pd.DataFrame(data['weather'])
    filepath = Path(".\\Day35-keys-authentication-environment-variables\\output\\output_weather_twopointfive.csv")
    filepath.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(filepath)

    with open(".\\Day35-keys-authentication-environment-variables\\output\\output_weather_twopointfive.csv", 'r') as file:
        current_weather_data = csv.reader(file, delimiter=',')
        #print(current_weather_data)
        next(current_weather_data, None)
        for row in current_weather_data:
            #print(row)
            #print(row[1])
            #print(type(row[1]))
            if int(row[1]) < 700:
                phone_number = ""
                message = "Bring an Umbrella!"
                pywhatkit.sendwhatmsg_instantly(phone_number, message, 15, True, 2)


except requests.HTTPError as error:
    pprint(response.status_code)
    if response.status_code == 401:
        pprint(f"error: {error}")
except Exception as e:
    print(e)