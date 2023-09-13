import requests
from pprint import pprint


# Open Trivia API
"""
    Code 0: Success Returned results successfully.
    Code 1: No Results Could not return results. The API doesn't have enough questions for your query. (Ex. Asking for 50 Questions in a Category that only has 20.)
    Code 2: Invalid Parameter Contains an invalid parameter. Arguements passed in aren't valid. (Ex. Amount = Five)
    Code 3: Token Not Found Session Token does not exist.
    Code 4: Token Empty Session Token has returned all possible questions for the specified query. Resetting the Token is necessary.
"""

#parameters = {
#    "amount": 10,
#    "type": "boolean",
#    "token": session_token,
#    "category": 17,
#}

## It will never give the same question twice using a token 

# parameters = {
#    "command": "request"
#}

#response = requests.get("https://opentdb.com/api_token.php", params=parameters)
#pprint(response)
#pprint(response.raise_for_status())
#data = response.json()['token']
#pprint(data)

#response = requests.get("https://opentdb.com/api.php", params=parameters)
#pprint(response)
#response.raise_for_status()
#pprint(response)
#data = response.json()
#pprint(data)
#question_data = data["results"]

#parameters = {
#    "command": "reset",
#    "token": session_token,
#}
#
#response = requests.get("https://opentdb.com/api_token.php", params=parameters)
#
#pprint(response)
#response.raise_for_status()
#data = response.json()
#pprint(data)
#print(session_token)
#question_data = data["results"]

import requests

# Example usage
session_token = ""

"""At most 50 questions can be requested per API call"""
BASE_URL = "https://opentdb.com/api.php"
API_TOKEN_URL = "https://opentdb.com/api_token.php"

def fetch_questions(session_token):
    parameters = {
        "amount": 10,
        "type": "boolean",
        "token": session_token,
        # Science and Nature: 17, # Animals: 27
        "category": 27,
    }

    try:
        response = requests.get(BASE_URL, params=parameters)
        response.raise_for_status()
        data = response.json()
        questions_data = data["results"]
        return questions_data
    except requests.HTTPError as error:
        # Unauthorized error code
        if response.status_code == 401:  
            refresh_token = reset_token()
            # Retry fetch_questions with the new token
            print("Resetting token...")
            print(refresh_token)
            return fetch_questions(refresh_token)
        else:
            raise error

def reset_token():
    parameters = {
        "command": "request"
    }

    response = requests.get(API_TOKEN_URL, params=parameters)
    # Raise HTTP error if one occurred
    response.raise_for_status()
    data = response.json()
    token = data["token"]
    return token



try:
    if session_token == "":
        token = reset_token()
        session_token = token
    questions_data = fetch_questions(session_token)
    pprint(f"Able to fetch questions_data: {questions_data}")
    for question in questions_data:
        pprint(question['correct_answer'])
    
except requests.HTTPError as error:
    print(f"Failed to fetch questions: {error}")