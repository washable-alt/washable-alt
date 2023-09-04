# Day 32

Automated Birthday Wisher

This automated birthday wisher helps you to send email and wish the recipient a happy birthday. 

## How to use

1. Run `main.py` to launch the sending of happy birthday email
2. The program will use the my_email variable and my password variable. 
3. To prevent the password from being leaked, it should use the dotenv library so that when the code is shared, the password will not be seen. 
4. use `python -m pip install virtualenv`
5. use `python -m pip install python-dotenv`
6. use `.\.venv\Scripts\Activate.ps1`
7. SMTP information - `gmail` - `smtp.gmail.com`, `hotmail` - `smtp.live.com`, `yahoo` - `smtp.mail.yahoo.com`
8. Create a connection using smtplib.SMTP(SMTP information)
9. connection.starttls() - transport layer security
10. connection.login(user= username, password= app_password)
11. connection.sendmail(from_addr=my_email, to_addrs=receiver_email, 
    msg="Subject: Hello\n\nThis is the body of my email. ")
12. connection.close()

## How to store sensitive data
1. Use configuration files
   config = configparser.ConfigParser() [Did not test this, can encrypt this using Fernet for secure usage]
2. create a dot_env file to store environment variables 


## Credits to The PyCoach (How to Send Emails with Python)
## Picture is taken from https://tenor.com/view/birthday-cake-birthday-birthday-party-happy-birthday-birthdays-gif-10164098181755864449

## Use case: Sending emails to friends so that they can feel appreciated that the user remembers their birthday (One way is to use task scheduler for Windows; try to make it work)

## Backlog - birthday-wisher-normal-start

