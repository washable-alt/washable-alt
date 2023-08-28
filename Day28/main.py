from tkinter import *
from PIL import Image, ImageTk
import math
import winsound

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
timer = None
reps = 0

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    """Resets the timer by configuring the canvas to 00:00, check_marks to no check_marks"""

    root.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_Label.config(text="Timer", fg=GREEN)
    check_marks.config(text="")
    
# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    """start the timer and increment the reps by one whenever the button Start is clicked"""

    # global variable used to keep track of the number of repetitions or cycles of work 
    # and break intervals 
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    #if repetitions divisible by 8, means more than 8 cycles of work and break intervals
    if reps % 8 == 0:
        count_down(long_break_sec)
        title_Label.config(text="Break", fg=RED)
    # if repetitions divisible by 2, commence short break
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_Label.config(text="Break", fg=PINK)
    else:
    # for other repetitions not divisible by 2 or 8, keep counting down the timer
        count_down(work_sec)
        title_Label.config(text="Work", fg=GREEN)
        
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    """Count down the timer"""

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = root.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        check_marks.config(text=marks)
        winsound.PlaySound(f".\\Day28\\guitar.wav", winsound.SND_LOOP)

# ---------------------------- UI SETUP ------------------------------- #
def main():
    global root
    global canvas
    global check_marks
    global title_Label
    global timer_text

    try:
        root = Tk()
        root.title("Pomorodo Timer")
        root.geometry("1000x600")
        root.config(padx=50, pady=50, bg=YELLOW)
        root.resizable(False, False)
        canvas = Canvas(root, width=700, height=300, bg=YELLOW, highlightthickness=0)

        # Creating a Label Widget
        title_Label = Label(root, text="Timer", font=(FONT_NAME, 30, "bold"), fg=GREEN, bg=YELLOW, highlightthickness=0)
        title_Label.grid(row=0, column=1, sticky=NW,pady=30, padx = 270)


        # Load the image
        img = ImageTk.PhotoImage(file=".\\Day28\\tomato.png")
        # Add the image in the canvas
        canvas.create_image(430, 200, image=img, anchor="se")
        timer_text = canvas.create_text(400,125, text="00:00", fill="white",font=(FONT_NAME, 30, "bold"), anchor="se")
        canvas.grid(row=1, column=1)

        button_one = Button(text="Start", highlightthickness=0, font=(FONT_NAME, 20, "bold"), command=start_timer)
        button_two = Button(text="Reset", highlightthickness=0, font=(FONT_NAME, 20, "bold"), command=reset_timer)
        button_one.grid(row=2, column=0, sticky="SE")
        button_two.grid(row=2, column=2, sticky="SE")

        check_marks = Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
        check_marks.grid(row=3, column=1)

        root.mainloop()
    
    except ValueError as e:
        print(e)

if __name__=="__main__":
    main()