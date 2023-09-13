from tkinter import *

CONSTANT_MILES_TO_KM = 1.60934


def convert(*args):
    miles = float(entry.get())

    kilometers = miles * CONSTANT_MILES_TO_KM 

    km_label.config(text=f"{kilometers:.2f}")

def click(event):
    entry.configure(state=NORMAL, justify="center")
    entry.delete(0,END)
    entry.unbind('<Button-1>', clicked)

def main():
    global entry
    global km_label
    global clicked

    root = Tk()
    root.geometry('1000x500')
    root.resizable(False,False)
    root.title("Miles to Kilometers converter")

    entry = Entry(root, font = ("Helvetica",28), fg="black", width=20)
    entry.insert(0, string="Input a value..." )
    entry.place(x=250, y=0)
    #Bind the Entry widget with Mouse Button to clear the content
    clicked = entry.bind('<Button-1>', click)
    

    text = Label(root, text="miles", font = ("Helvetica", 28), fg="black")
    text.place(x=600, y=0)

    is_equal_to_label = Label(root, text="is equal to", font=("Helvetica", 28), fg="black")
    is_equal_to_label.place(x=200,y=200)

    km_label = Label(root, text="", font = ("Helvetica", 28), fg="black")
    km_label.place(x=420, y=200)

    text_km = Label(root, text='km', font=("Helvetica", 28), fg="black")
    text_km.place(x=600, y= 200)


    convert_button = Button(root, text="Convert", command=convert, font=("Helvetica", 28))
    convert_button.place(x=400, y= 300)
    
    root.mainloop()

if __name__=="__main__":
    main()