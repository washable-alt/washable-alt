import os
import smtplib
from dotenv import load_dotenv
from email.message import EmailMessage
import ssl

def main():

    try:
        load_dotenv()
        email_sender = os.getenv("EMAIL_SENDER")
        email_password = os.getenv("EMAIL_PASSWORD")
        email_receiver = os.getenv("EMAIL_RECEIVER")

        subject = "Wishing you a Happy Birthday"

        body = """
        Happy Birthday!  
                                                                                                                                                                                     
        """

        em = EmailMessage()
        em['From'] = email_sender
        em['To'] = email_receiver

        em['Subject'] = subject

        em.set_content(body)

        # Split the email_receiver string into a list of email addresses
        email_receiver_list = email_receiver.split(',')

         # Attach files to the email
        # Replace `attachment_file_path` with the actual path of the file to attach
        attachment_file_path = '.\\Day32-send-email\\birthday-cake-birthday.gif'
        with open(attachment_file_path, 'rb') as attachment_file:
            attachment_data = attachment_file.read()
        em.add_attachment(attachment_data, maintype='application', subtype='octet-stream', filename=os.path.basename(attachment_file_path))

        context = ssl.create_default_context()
    
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            #Login
            smtp.login(email_sender, email_password)
            ## for just one email address
            #smtp.sendmail(email_sender, email_receiver, em.as_string())
            ## for multiple email addresses
            # Send the email to each email address in the list
            for receiver_email in email_receiver_list:
                em.replace_header('To', receiver_email)
                smtp.send_message(em)
        print("Successful")
        
    except Exception as e:
        print(e)
        

if __name__ == "__main__":
    main()