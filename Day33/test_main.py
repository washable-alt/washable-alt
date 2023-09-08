import requests
import urllib3
import json

try:
    # http://api.open-notify.org/iss-now.json/ -> endpoint
    response = requests.get("http://api.open-notify.org/iss-now.json/", verify=False)
    print(response)
    response = urllib3.request("GET", "http://api.open-notify.org/iss-now.json/")
    
    #bytes type
    print(type(response.data))
    print(response.data)
    
    # decode using utf-8 or use the codecs module
    obj = json.loads(response.data.decode('utf-8'))
    # print the dictionary of the API response from the API request called to the URI 
    print(obj)
    # print the unix timestamp; a way to track time as a running total of seconds
    print(obj['timestamp'])
    # printing the longitude and lattitude
    print(obj['iss_position'])
    # printing the longitude 
    print(obj['iss_position']['longitude'])
    # printing the message
    print(obj['message'])
    
except Exception as e:
    print(e)