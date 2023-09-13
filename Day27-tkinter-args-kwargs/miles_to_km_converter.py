from tkinter import *

def main():
# create window

    root = Tk()
    root.geometry('500x300')
    root.resizable(False, False)
    root.title("Miles to Kilometers converter")
    

    miles_label = Label(root, text="Enter distance in miles:")
    miles_label.pack()

    km_label = Label(root, text="Distance in kilometers:")
    km_label.pack()

    miles_entry = Entry(root)
    miles_entry.pack()

    def convert(*args):

        miles = float(miles_entry.get())
        
        kilometers = miles * 1.60934

        #Changing the text of km label
        km_label.config(text=f"Distance in kilometers: {kilometers:.2f}")

    convert_button = Button(root, text="Convert", command=convert)
    convert_button.pack()

    root.mainloop()




if __name__ == "__main__":
    main()