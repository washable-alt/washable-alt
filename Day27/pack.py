from tkinter import *


def grab():
    my_label.config(text=my_box.get())

def main():
    global my_label
    global my_box

    root = Tk()
    root.title('')
    root.geometry("600x400")

    my_box = Entry(root, font=("Helvetica", 28))
    my_box.pack(pady=20)

    my_button = Button(root, text="Grab text from box", command=grab)
    my_button.pack(pady=20)


    #push it down by using pady
    my_label = Label(root, text="")
    my_label.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    main()