##################### Normal Starting Project ######################

# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes. e.g.
#name,email,year,month,day
#YourName,your_own@email.com,today_year,today_month,today_day

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Create a tuple from today's month and day using datetime. e.g.
# today = (today_month, today_day)
from datetime import datetime
import pandas as pd
import random
import smtplib
#from configparser import ConfigParser
from email.message import EmailMessage
import ssl
import os
from dotenv import load_dotenv

def main():
    # HINT 2: Use pandas to read the birthdays.csv
    birthdays = pd.read_csv(f".\\Day32\\birthday-wisher-normal-start\\birthdays.csv")
    #print(birthdays)
    #for (index, data_row) in birthdays.iterrows():
        #print(index)
        #print(data_row)
        #print(data_row['month'])
        #print(data_row['day'])

    today = datetime.now()
    today_tuple = (today.month, today.day)
    #print(today_tuple)

    # HINT 3: Use dictionary comprehension to create a dictionary from birthday.csv that is formated like this:
    # birthdays_dict = {
    #     (birthday_month, birthday_day): data_row
    # } 
    birthdays_dict = {
        (data_row['month'], data_row['day']): data_row for (_,data_row) in birthdays.iterrows()
    }
    print(birthdays_dict)
    try:
        if today_tuple in birthdays_dict:
            birthday_person = birthdays_dict[today_tuple]
            
            my_numbers = ['one', 'two', 'three']
            file_path = f".\Day32\\birthday-wisher-normal-start\\letter-templates\\letter_{random.choice(my_numbers)}.txt"
            with open(file_path) as letter_file:
                contents = letter_file.read()
                #print(birthday_person["name"])
                contents = contents.replace("[NAME]", birthday_person["name"])
            print(contents)

            load_dotenv()
            email_sender = os.getenv("EMAIL_SENDER")
            email_password = os.getenv("EMAIL_PASSWORD")
            email_receiver = os.getenv("EMAIL_RECEIVER")


            #config_file_path = f".\\Day32\\birthday-wisher-normal-start\\config.ini"
            #config = ConfigParser()
            #config.read(config_file_path)
            
            em = EmailMessage()
            em['From'] = email_sender
            em['To'] = email_receiver

            subject = "Wishing you a Happy Birthday!"

            em['Subject'] = subject

            em.set_content(contents)

            # Split the email_receiver string into a list of email addresses
            email_receiver_list = email_receiver.split(',')
            print(email_receiver_list)

            # Attach files to the email
            # Replace `attachment_file_path` with the actual path of the file to attach
            attachment_file_path = '.\\Day32\\birthday-cake-birthday.gif'
            with open(attachment_file_path, 'rb') as attachment_file:
                attachment_data = attachment_file.read()
            em.add_attachment(attachment_data, maintype='application', subtype='octet-stream', filename=os.path.basename(attachment_file_path))

            context = ssl.create_default_context()

            with smtplib.SMTP_SSL("smtp.gmail.com",465,context=context) as smtp:
                
                smtp.login(user=email_sender, password=email_password)
                for receiver_email in email_receiver_list:
                    em.replace_header('To', receiver_email)
                    smtp.send_message(em)

            print("Successful")

    except Exception as e:
        print(e)
        

if __name__ == "__main__":
    main()