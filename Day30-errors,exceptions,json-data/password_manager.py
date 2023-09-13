import random 
import string

class MyPass:
    def __init__(self):
        self.website = ""
        self.email = ""
        self.password = ""

    def set_website(self, website):
        self.website = website

    def set_email(self, email):
        self.email = email

    def set_password(self, password):
        self.password = password

    @staticmethod
    def generate_password():
        # Implementation of password generation algorithm
        length = 16  # Password length
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        return password

    def add_entry_to_file(self):
        entry = f"{self.website} | {self.email} | {self.password}\n"
        with open(".\\Day30-errors,exceptions,json-data\\passwords.txt", "a") as file:
            file.write(entry)