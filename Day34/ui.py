from tkinter import *
from quiz_brain import QuizBrain
import requests

THEME_COLOR = "#375362"


class QuizInterface:
    
    
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
    
        ## Create the canvas first 
        self.root = Tk()
        self.root.title("Quizzler")
        self.root.geometry("700x700")
        self.root.resizable(False, False)

        self.root['bg'] = THEME_COLOR

        self.score_Label = Label(text="Score: 0", font=("Courier", '12', 'bold'), bg=THEME_COLOR, highlightthickness=0, fg="white")
        self.score_Label.grid(row=0, column=2)

        self.canvas = Canvas(self.root, bg="white", height=450, width=450, highlightthickness=0)
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Welcome to Quiz",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(row=1, column=1, padx=100, pady=50, columnspan=2)

        true_image = PhotoImage(file=".\\Day34\\images\\true.png")
        self.true_Button = Button(image=true_image, highlightthickness=0, command=self.true_pressed)
        self.true_Button.grid(row=2, column=1)

        false_image = PhotoImage(file=".\\Day34\\images\\false.png")
        self.false_Button = Button(image=false_image,highlightthickness=0, command=self.false_pressed)
        self.false_Button.grid(row=2, column=2)
        
        self.get_next_question()

        self.root.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_Label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text=f"You've reached the end of the quiz. \nFinal Score: {self.quiz.score} / {self.quiz.question_number}\n")
            self.true_Button.config(state="disabled")
            self.false_Button.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.root.after(1000, self.get_next_question)

        self.root.mainloop()
