# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
from tkinter import *
from password_manager import MyPass
from PIL import ImageTk, Image

FONT_NAME = "Arial"
BLANK_SPACE = " "

def main():
   
    try:
        # Create the main window
        root = Tk()
        # Load the image
        image = Image.open(f".\\Day29\\logo.png")
        
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
        website_Entry = Entry(width=47)
        website_Entry.grid(row=1, column=1, columnspan=2)
        
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

        # Create Generate Password Button
        Generate_Button = Button(text="Generate Password")
        Generate_Button.grid(row=3, column=2, padx=(0,28))

        # Create an Add Button
        Add_Button = Button(text="Add", justify="center", width=40)
        Add_Button.grid(row=4, column=1, columnspan=2)
        
        root.mainloop()


    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()