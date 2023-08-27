import tkinter as tk



def main():
# create window

    window = tk.Tk()
    window.geometry('500x300')
    window.resizable(False, False)
    window.configure(background='black')
    window.title("Miles to Kilometers converter")
    window.mainloop()




if __name__ == "__main__":
    main()