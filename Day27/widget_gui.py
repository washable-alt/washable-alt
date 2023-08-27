import tkinter as tk

window = tk.Tk()
window.title("Widget Examples")
window.minsize(width=1000, height=1000)

# Label

my_label = tk.Label(text="This is old text", font=("Arial", 24, "bold"))

# Label config can be used to configure old text and new text
my_label.config(text="This is new text")

my_label.place(x=450, y=100)

# place label in the gui window
#my_label.pack()

#Buttons
def action():
    print("Hello, World")

#calls action() when pressed
button = tk.Button(text="Click Me", command=action)

# set the x and y coordinates
button.place(x=500, y=150)

# place button at gui window
#button.pack()

#Entries
entry = tk.Entry(width=30)
#Add some text to begin with
entry.insert(tk.END, string="Type..." )
#Gets text in entry
#print(entry.get())
entry.place(x=450, y= 200)
#entry.pack()

#Text
text = tk.Text(height=5, width=30)
#Puts cursor in textbox.
text.focus()
#Adds some text to begin with.
text.insert(tk.END, "Example of multi-line text entry.")
#Get's current value in textbox at line 1, character 0
#print(text.get("1.0", tk.END))
text.place(x=450, y=250)
#text.pack()

#Spinbox
def spinbox_used():
    #gets the current value in spinbox.
    print(spinbox.get())
spinbox = tk.Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.place(x=450, y = 350)
# spinbox.pack()

#Scale
#Called with current scale value.
def scale_used(value):
    print(value)
scale = tk.Scale(from_=0, to=100, command=scale_used)
scale.place(x=450, y=400)
#scale.pack()

#Checkbutton
def checkbutton_used():
    #Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())
#variable to hold on to checked state, 0 is off, 1 is on.
checked_state = tk.IntVar()
checkbutton = tk.Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.place(x=550, y=450)
#checkbutton.pack()

#Radiobutton
def radio_used():
    print(radio_state.get())
#Variable to hold on to which radio button value is checked.
radio_state = tk.IntVar()
radiobutton1 = tk.Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = tk.Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)

radiobutton1.place(x=450, y=550)
radiobutton2.place(x=450, y=600)
#radiobutton1.pack()
#radiobutton2.pack()


#Listbox
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))

listbox = tk.Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.place(x=500, y=650)

#listbox.pack()


window.mainloop()