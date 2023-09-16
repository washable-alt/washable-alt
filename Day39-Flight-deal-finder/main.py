import requests
from dotenv import load_dotenv
import os
import json
from pprint import pprint
from datetime import datetime, timedelta
from twilio.rest import Client

load_dotenv()

SHEETY_ENDPOINT = os.getenv("SHEETY_ENDPOINT")

SHEETY_USERNAME = os.getenv("SHEETY_USERNAME")

SHEETY_TOKEN = os.getenv("SHEETY_TOKEN")

GOOGLE_SHEET_NAME = "prices"

TEQUILA_ENDPOINT = os.getenv("TEQUILA_LOCATION_ENDPOINT")

TEQUILA_API_KEY = os.getenv("TEQUILA_API_KEY")

TEQUILA_SEARCH_ENDPOINT = os.getenv("TEQUILA_SEARCH_ENDPOINT")

auth_headers = {
    "Authorization": f"Bearer {SHEETY_TOKEN}" 
}

def send_sms(message):
    
    ACCOUNT_SID = os.getenv("ACCOUNT_SID")
    AUTH_TOKEN = os.getenv("AUTH_TOKEN")
    PHONE_NUMBER = os.getenv("PHONE_NUMBER")
    MY_PHONE_NUMBER = os.getenv("MY_PHONE_NUMBER")
    client = Client(ACCOUNT_SID, AUTH_TOKEN)

    message = client.messages.create(
        from_=PHONE_NUMBER,
        to=MY_PHONE_NUMBER,
        body=f"{message}"
    )

    print(message.sid)

def get_response_for_sheety_endpoint():
    sheet_inputs = {
    GOOGLE_SHEET_NAME: {
        "city": "",
        "iataCode": "",
        "lowestPrice": ""
        }
    }

    get_response = requests.get(SHEETY_ENDPOINT, params=sheet_inputs, headers=auth_headers)
    #print(get_response.text)
    return get_response.text

def change_iataCode_to_testing():
    changed_sheet_inputs = {
        "price": {
            "iataCode": "TESTING",
        }
    }
    for i in range(2,11):
        response = requests.put(f"{SHEETY_ENDPOINT}/{i}",json=changed_sheet_inputs,headers=auth_headers)
        print(response.text)

    return response.text



country_list= ["Paris","Berlin","Tokyo","Sydney","Istanbul","Kuala Lumpur","New York","San Francisco","Cape Town"]

headers = {
    "apikey":TEQUILA_API_KEY
}

def get_response_for_one_country():
    try: 
        tequila_response = requests.get(TEQUILA_ENDPOINT, params=parameters, headers=headers)
        pprint(tequila_response.json()['locations'][0]['code'])
    except Exception as e:
        pprint(e)

    parameters = {
               "term": "Paris"
           }

def put_request_for_tequila_and_sheety():
    try:
        # zip function allows me to iterate in parallel over two or more iterables
        for i, country in zip(range(2, 11), country_list):
            parameters = {
                "term": country
            }
            tequila_response = requests.get(TEQUILA_ENDPOINT, params=parameters, headers=headers)
            
            changed_sheet_inputs = {
                "price": {
                    "iataCode": tequila_response.json()['locations'][0]['code']
                }
            }
            response = requests.put(f"{SHEETY_ENDPOINT}/{i}", json=changed_sheet_inputs, headers=auth_headers)
            print(response.text)
        
    except Exception as e:
        print(e)

def prices_for_cities_tequila_compare_in_sheety_and_send_sms(data):
    # Set the parameters
    fly_from = "LON"
    # search flights one day from today
    date_from = (datetime.utcnow().now() + timedelta(days=1)).strftime(r"%d/%m/%Y")
    # 6 months from now
    date_to = (datetime.utcnow().now() + timedelta(days=180)).strftime(r"%d/%m/%Y")  
    # 7 days from now
    return_from = (datetime.utcnow().now() + timedelta(days=7)).strftime(r"%d/%m/%Y")
    # 28 days from now  
    return_to = (datetime.utcnow().now() + timedelta(days=28)).strftime(r"%d/%m/%Y")  
    currency = "GBP"
    for x,y in zip(range(2,11),range(len(country_list))):
        parameters = {
            "fly_from": fly_from,
            "fly_to": data['prices'][y]['iataCode'],
            "date_from": date_from,
            "date_to": date_to,
            "return_from": return_from,
            "return_to": return_to,
            "nights_in_dst_from": 7,
            "nights_in_dst_to":28,
            "flight_type": "round",
            "one_for_city": 1,
            "curr": currency,
            "limit": 3
        }
        try:
            response = requests.get(TEQUILA_SEARCH_ENDPOINT, params=parameters, headers=headers)
            #pprint(response.json()['data'][0])
            real_time_price = response.json()['data'][0]['price']
            #pprint(f"Routes: {response.json()['data'][0]['route']}")
            #pprint(f"Route0: {response.json()['data'][0]['route'][0]['local_departure'].split('T')[0]}")
            #pprint(f"Route1: {response.json()['data'][0]['route'][1]['local_departure'].split('T')[0]}")
            #pprint(f"Route2: {response.json()['data'][0]['route'][2]['local_departure'].split('T')[0]}")

            #pprint(f"{country}: £ {real_time_price}")
            #pprint(f"Departure city name: {response.json()['data'][0]['route'][0]['cityFrom']}")
            #pprint(f"Departure Airport IATA Code: {response.json()['data'][0]['route'][0]['flyFrom']}")
            #pprint(f"Arrival City Name: {response.json()['data'][0]['route'][0]['cityTo']}")
            #pprint(f"Arrival Airport IATA Code: {response.json()['data'][0]['route'][0]['cityCodeTo']}")
            #pprint(f"Local departure date: {response.json()['data'][0]['route'][0]['local_departure'].split('T')[0]}")
            #pprint(f"Return date: {response.json()['data'][0]['route'][1]['local_departure'].split('T')[0]}")

            departure_city_name = response.json()['data'][0]['route'][0]['cityFrom']
            departure_airport_iata_code = response.json()['data'][0]['route'][0]['flyFrom']
            arrival_city_name = response.json()['data'][0]['route'][0]['cityTo']
            arrival_airport_iata_code = response.json()['data'][0]['route'][0]['flyTo']
            local_departure_date =  response.json()['data'][0]['route'][0]['local_departure'].split('T')[0]
            return_date = response.json()['data'][0]['route'][1]['local_departure'].split('T')[0]
            
            
            #pprint(response.json()['data'][0]['price'])
            changed_sheet_inputs = {
                "price": {
                    "lowestPrice": ""
                }
            }
            response = requests.get(f"{SHEETY_ENDPOINT}/{x}", json=changed_sheet_inputs, headers=auth_headers)
            #print(response.text)
            updated_data = response.json()
            print(updated_data)
            if int(real_time_price) < int(updated_data['price']['lowestPrice']) and (local_departure_date == return_date):
                return_date = response.json()['data'][0]['route'][2]['local_departure'].split('T')[0]
                if local_departure_date == return_date:
                    print(f"One-way ticket found! Only £{real_time_price} to fly from {departure_city_name}-{departure_airport_iata_code} to {arrival_city_name}-{arrival_airport_iata_code} on {local_departure_date}.")
                    message = f"One-way ticket found! Only £{real_time_price} to fly from {departure_city_name}-{departure_airport_iata_code} to {arrival_city_name}-{arrival_airport_iata_code} on {local_departure_date}."
                    send_sms(message=message)
            elif int(real_time_price) < int(updated_data['price']['lowestPrice']):
                print(f"Low price alert! Only £{real_time_price} to fly from {departure_city_name}-{departure_airport_iata_code} to {arrival_city_name}-{arrival_airport_iata_code}, from {local_departure_date} to {return_date}")
                message = f"Low price alert! Only £{real_time_price} to fly from {departure_city_name}-{departure_airport_iata_code} to {arrival_city_name}-{arrival_airport_iata_code}, from {local_departure_date} to {return_date}"
                send_sms(message=message)

        except IndexError:
            print(f"No flights found for {data['prices'][y]['iataCode']}")
            continue
        

if __name__ =="__main__":
    get_response = get_response_for_sheety_endpoint()
    data = json.loads(get_response)
    country_list= ["Paris","Berlin","Tokyo","Sydney","Istanbul","Kuala Lumpur","New York","San Francisco","Cape Town"]
    for i in range(len(country_list)):
        if (data['prices'][i]['iataCode']) == "TESTING" or (data['prices'][i]['iataCode']) == "":
            put_request_for_tequila_and_sheety()
    prices_for_cities_tequila_compare_in_sheety_and_send_sms(data)
    