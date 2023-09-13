import os
from dotenv import load_dotenv
from email.message import EmailMessage
import ssl
import smtplib

load_dotenv()

email_sender = os.getenv("EMAIL_SENDER")
email_password = os.getenv("EMAIL_PASSWORD")
email_receiver = os.getenv("EMAIL_RECEIVER")

subject = "Job searching is such fun."

body = """
Give me a job! Enslave me! Yes! I love it! 
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject

em.set_content(body)

context = ssl.create_default_context()

try:    
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        #Login
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())

except Exception as e:
    print(e)