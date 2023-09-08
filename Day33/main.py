import os
import requests
from datetime import datetime
import smtplib, ssl
from email.message import EmailMessage
from dotenv import load_dotenv
import time


MY_LAT = 1.352083
MY_LONG = 103.819839

global iss_latitude, iss_longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

# Your position is within +5 or -5 degrees of the ISS position. (so that is is margin of error)

is_five_degrees_within_ISS_position = False

def is_iss_overhead():
    global iss_latitude, iss_longitude, is_five_degrees_within_ISS_position
    if abs(iss_latitude - MY_LAT) <= 5 and abs(iss_longitude-MY_LONG)<=5:
        is_five_degrees_within_ISS_position = True
        return is_five_degrees_within_ISS_position
    else:
        return is_five_degrees_within_ISS_position
    

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    """Sends a GET request.

    :param url: URL for the new :class:`Request` object.
    :param params: (optional) Dictionary, list of tuples or bytes to send
        in the query string for the :class:`Request`.
    :param \*\*kwargs: Optional arguments that ``request`` takes.
    :return: :class:`Response <Response>` object
    :rtype: requests.Response
    """

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    print(response)
    response.raise_for_status()
    data = response.json()
    print(data)
    
    # UTC
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour
    print(time_now)

    # If the ISS is close to my current position 
    # and it is currently dark
    # then send me an email to tell me to look up.
    # Bonus: run the code every 60 seconds

    # if it is currently nighttime return true 
    if time_now >= sunset or time_now <= sunrise:
        # It's dark. 
        return True
    

def main():

    try:
        
        while is_iss_overhead() and is_night():

            response = requests.get(url="http://api.open-notify.org/iss-now.json")
            response.raise_for_status()
            data = response.json()

            iss_latitude = float(data["iss_position"]["latitude"])
            iss_longitude = float(data["iss_position"]["longitude"])

            load_dotenv()
            email_sender = os.getenv("EMAIL_SENDER")
            email_password = os.getenv("EMAIL_PASSWORD")
            email_receiver = os.getenv("EMAIL_RECEIVER")
                
            context= ssl.create_default_context()

            subject = "Notification"

            body = f"""
            Hey, look up, ISS is now overhead of you! Current latitude: {iss_latitude}, Current longtitude: {iss_longitude}.
            """
            em = EmailMessage()
            em['From'] = email_sender
            em['To'] = email_receiver
            em['Subject'] = subject
            em.set_content(body)
                
            with smtplib.SMTP_SSL("smtp.gmail.com",465,context=context) as smtp:
                smtp.login(email_sender, email_password)
                smtp.sendmail(email_sender, email_receiver, em.as_string())
            time.sleep(60)
        
        while not is_iss_overhead() and not is_night() or not is_iss_overhead() and is_night():

            response = requests.get(url="http://api.open-notify.org/iss-now.json")
            response.raise_for_status()
            
            data = response.json()
            

            iss_latitude = float(data["iss_position"]["latitude"])
            iss_longitude = float(data["iss_position"]["longitude"])
            
            load_dotenv()
            email_sender = os.getenv("EMAIL_SENDER")
            email_password = os.getenv("EMAIL_PASSWORD")
            email_receiver = os.getenv("EMAIL_RECEIVER")
                
            context= ssl.create_default_context()

            subject = "Notification"

            body = f"""
            ISS is currently not overhead of you. Current latitude: {iss_latitude}, Current longtitude: {iss_longitude}.
            """
            em = EmailMessage()
            em['From'] = email_sender
            em['To'] = email_receiver
            em['Subject'] = subject
            em.set_content(body)
                
            with smtplib.SMTP_SSL("smtp.gmail.com",465,context=context) as smtp:
                smtp.login(email_sender, email_password)
                smtp.sendmail(email_sender, email_receiver, em.as_string())
            time.sleep(60)
            
        
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()