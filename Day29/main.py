from tkinter import *
from tkinter import messagebox
from password_manager import MyPass
from PIL import ImageTk, Image
from password_manager import MyPass
import json

FONT_NAME = "Arial"
BLANK_SPACE = " "

mypass=MyPass()


def main():
   
    try:
        # Create the main window
        root = Tk()
        # Load the image
        image = Image.open(".\\Day29\\logo.png")
        
        root.title("Password Manager")
        
        root.geometry("700x700")
        root.resizable(False, False)
        # Resize the image if necessary
        image = image.resize((200, 200))

        root.config(padx=50, pady=50)

        # Convert the Image Object into a Tkinter-compatible photo image
        photo = ImageTk.PhotoImage(image)

        # Create a label to display the image
        logo_Label = Label(root, image=photo)
        logo_Label.grid(row=0, column=1)

        # Create the website label
        website_Label = Label(root, text="Website: ", font=(FONT_NAME, 12, "bold"))
        website_Label.grid(row=1, column=0, padx=(10,0))

        # Create the entry with column span
        website_Entry = Entry(width=21)
        website_Entry.grid(row=1, column=1,padx=(0,16))

        # Create the search button

        def on_enter(e):
            search_Button.config(bg="blue", fg="white")

        def on_leave(e):
            search_Button.config(bg="SystemButtonFace", fg="black")
        
        def find_password():
            website = website_Entry.get()
            with open(".\\Day29\\data.json") as data_file:
                data = json.load(data_file)
                if website in data:
                    email = data[website]['email']
                    password = data[website]['password'] 
                    messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
                else:
                    messagebox.showinfo(title="Error", message=f"No details for {website} exists.")

        search_Button = Button(root, text="Search", bg="SystemButtonFace", fg="black", command=find_password)
        search_Button.grid(row=1, column=2, padx=(0,28))

        # Bind events to change the button color
        search_Button.bind("<Enter>", on_enter)
        search_Button.bind("<Leave>", on_leave)
        
        email_Label = Label(root, text="Email/Username: ", font=(FONT_NAME, 12, "bold"))
        email_Label.grid(row=2, column=0, padx=(10,0))
        
        # Create the email entry with column span
        email_Entry = Entry(width=47)
        email_Entry.grid(row=2, column=1, columnspan=2)
        

        password_Label = Label(root, text="Password: ", font=(FONT_NAME, 12, "bold"))
        password_Label.grid(row=3, column=0, padx=(10,0))

         # Create the email entry with column span
        password_Entry = Entry(width=21)
        password_Entry.grid(row=3, column=1,padx=(0,16))

        def generate_password_action():
            new_password = mypass.generate_password()
            password_Entry.delete(0, END)  # Clear any existing text
            password_Entry.insert(0, new_password)

        # Create Generate Password Button
        Generate_Button = Button(text="Generate Password", command=generate_password_action)
        Generate_Button.grid(row=3, column=2, padx=(0,28))

        def add_entry_action():
            website = website_Entry.get()
            email = email_Entry.get()
            password = password_Entry.get()
            new_data = {
                website: {
                    "email": email,
                    "password": password,
                }
            }

            if len(website) == 0 or len(password) == 0:
                messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
            # Validate email format
            elif not email.endswith("@gmail.com"):
                messagebox.showwarning("Invalid Email", "Please enter a valid Gmail address.")
                email_Entry.delete(0, END)  # Clear the invalid input
                return
            else:
                #is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
                #                               f"\nPassword: {password} \nIs it ok to save?")
                #if is_ok:
                    # Create a MyPass instance and add entry to file
                    #password_entry = MyPass()
                    #password_entry.set_website(website)
                    #password_entry.set_email(email)
                    #password_entry.set_password(password)
                    #password_entry.add_entry_to_file()
                    # Write json, read json and update json
                    # json.dump(), json.load() and json.update() respectively
                # write file
                #with open(".\\Day29\\data.json", 'w') as data_file:
                #    json.dump(new_data, data_file, indent=4)
#
                #    website_Entry.delete(0, END)
                #    password_Entry.delete(0, END)
                # read file
                try:    
                    with open(".\\Day29\\data.json", 'r') as data_file:
                        # Reading old data
                        data = json.load(data_file)
                        # Updating old data with new data
                except FileNotFoundError:
                    with open(".\\Day29\\data.json", 'w') as data_file:
                        json.dump(new_data, data_file, indent=4)
                    print(type(data))
                    data.update(new_data)
                else: 
                    #Updating old data with new data
                    data.update(new_data)

                    with open(".\\Day29\\data.json", 'w') as data_file:
                        # Saving updated data
                        json.dump(data, data_file, indent=4)
                finally:
                    website_Entry.delete(0, END)
                    password_Entry.delete(0, END)

        # Create an Add Button
        Add_Button = Button(text="Add", justify="center", width=40, command=add_entry_action)
        Add_Button.grid(row=4, column=1, columnspan=2)
        
        root.mainloop()


    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()