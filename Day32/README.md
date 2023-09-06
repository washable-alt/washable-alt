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
8. Create context using `ssl.create_default_context()`
9. Create a connection using `smtplib.SMTP_SSL("smtp.gmail.com",465,context=context)`
10. Login using smtp`smtp.login(user=email_sender, password=email_password)`
11. email_password is app password, and it works fine for me

# In pythonanywhere
1. Upload letter templates folder, birthdays.csv, and .env 
2. Edit the file paths appropriately in the `main.py` such as `birthdays.csv`, `letter-templates\\letter_{random.choice(my_numbers)}.txt`, `birthday-cake-birthday.gif`


## How to store passwords in a separate file

1. create a dot_env file to store environment variables 
2. Use configuration files
   config = configparser.ConfigParser() 


## Credits to The PyCoach (How to Send Emails with Python)
## Picture is taken from Tenor


## Use case: Sending emails to friends so that they can feel appreciated that the user remembers their birthday 

# Able to make the code run using dotenv in pythonanywhere, can schedule only one task for a free account, the letter templates allow the recipient to receive different templates for happy birthday wishes. It checks for the condition whether the date and month are the same. If true, then the sending of email will be successful.

