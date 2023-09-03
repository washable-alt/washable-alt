from tkinter import *
import pandas as pd


BACKGROUND_COLOR = "#B1DDC6"

def previous_card():
    """Displays previous flashcard in the sequence"""
    global card_index
    # check if the previous_card() function is called, if card_index - 1 is greater than or equal to 0
    # clicking on it before the first card will not result in any changes to the flashcard being shown
    if card_index - 1 >= 0:
        card_index -= 1
        canvas.itemconfig(card_title, text="French")
        canvas.itemconfig(card_word, text=to_learn[card_index]["French"])
        canvas.itemconfig(card_image, image=card_front_img)


def flip_card():
    """Flipping the flashcard to reveal the answer or solution on the back of the card, and then flipping it back to the front."""
    # Retrieves the current flashcard from the to_learn list based on the card_index
    current_card = to_learn[card_index]
    # If the card title is equal to "French", change the title, the card word, and card_image for flipping
    if canvas.itemcget(card_title, "text") == "French":
        canvas.itemconfig(card_title, text="English")
        canvas.itemconfig(card_word, text=current_card["English"], fill="black")
        canvas.itemconfig(card_image, image=card_back_img)
    else:
        canvas.itemconfig(card_title, text="French")
        canvas.itemconfig(card_word, text=current_card["French"])
        canvas.itemconfig(card_image, image=card_front_img)


def next_card():
    global card_index
    """Displays the next flashcard in the sequence.

    Checks if there is a next flashcard available based on the current `card_index`. 
    If a next flashcard exists, it updates the canvas to display the 
    French version of the next flashcard, along with its front image. 
    If there are no more remaining flashcards, it shows a message indicating 
    that all cards have been learned and disables the navigation and flip buttons.
    """
    # Say there are 5 flashcards in the to_learn list, when the card_index is 4, the card_index + 1 would be 5.
    # If card_index < len(to_learn) is used, it would still evaluate to True because 4 < 5. 
    # However, trying to access to_learn[card_index + 1], it the index 5 does not exist in the to_learn list.
    if card_index + 1 < len(to_learn):
        card_index += 1
        #change the title to French
        canvas.itemconfig(card_title, text="French")
        #point to the next index of to_learn and access the dictionary value with key "French"
        canvas.itemconfig(card_word, text=to_learn[card_index]["French"])
        canvas.itemconfig(card_image, image=card_front_img)
    else:
        canvas.itemconfig(card_title, text="All cards learnt!")
        canvas.itemconfig(card_word, text="")
        
        canvas.delete(card_image)  # Remove the card image
        canvas.create_window(400, 263, window=restart_button)
        previous_button.config(state=DISABLED)
        flip_button.config(state=DISABLED)
        known_button.config(state=DISABLED)


def restart_cards():
    global card_index, card_back_img, card_image, card_title, card_word
    # set card index to the end of the to_learn list
    card_index = -1
    card_front_img = PhotoImage(file=".\\Day31\\images\\card_front.png")
    card_back_img = PhotoImage(file=".\\Day31\\images\\card_back.png")
    # Sets image with the card front png photo with the width and height specified
    card_image = canvas.create_image(400, 263, image=card_front_img)
    # Sets card title to italic
    card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
    card_word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
    canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
    canvas.grid(row=0, column=0, columnspan=3, padx=50, pady=50, sticky="nsew")
    next_card()
    restart_button.destroy()
    previous_button.config(state=NORMAL)
    flip_button.config(state=NORMAL)
    known_button.config(state=NORMAL)


def main():

    try:
        data = pd.read_csv(".\\Day31\\data\\french_words.csv")
        global to_learn, card_index, canvas, card_title, card_word, card_image, previous_button
        global card_front_img, card_back_img, restart_button, flip_button, known_button
        to_learn = data.to_dict(orient="records")
        
        card_index = -1
        
        root = Tk()
        root.title("Flashcards")
        root.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
        root.resizable(False, False)
        
        canvas = Canvas(width=800, height=526)
        card_front_img = PhotoImage(file=".\\Day31\\images\\card_front.png")
        card_back_img = PhotoImage(file=".\\Day31\\images\\card_back.png")
        card_image = canvas.create_image(400, 263, image=card_front_img)
        card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
        card_word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
        canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
        canvas.grid(row=0, column=0, columnspan=3, padx=50, pady=50, sticky="nsew")

        flip_button = Button(text="Flip", highlightthickness=0, command=flip_card, width=10, height=2)
        flip_button.grid(row=1, column=0, padx=(70, 0), pady=20)

        previous_button = Button(text="Previous", highlightthickness=0, command=previous_card, width=10, height=2)
        previous_button.grid(row=1, column=1, pady=20)

        known_button = Button(text="Next", highlightthickness=0, command=next_card, width=10, height=2)
        known_button.grid(row=1, column=2, padx=(10, 70), pady=20)

        restart_button = Button(text="Restart", highlightthickness=0, command=restart_cards, width=20, height=2)
        
        next_card()
        root.mainloop()

    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()