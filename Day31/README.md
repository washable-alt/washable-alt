# Day 31 

Flashcards Application

This flashcards application helps you learn new words or concepts by displaying flashcards with question and answer content. It allows you to flip the flashcard to reveal the answer and navigate through the flashcards using previous and next buttons.

In this case, it is french words.

## How to Use

1. Run `main.py` to launch the flashcards application.
2. The application displays a flashcard with a question or prompt on the front.
3. Click the "Flip" button to reveal the answer or solution on the back of the flashcard.
4. To navigate through the flashcards:
    - Click the "Next" button to move to the next flashcard.
    - Click the "Previous" button to go back to the previous flashcard.
5. The application continues to cycle through the flashcards until all of them have been viewed.
6. If you want to restart the flashcards and go through them again:
    - Click the "Restart" button.

## Functions

The application uses the following functions:

- `flip_card()`: This function is called when the "Flip" button is clicked. It changes the display from the front of the flashcard to the back, revealing the answer or solution.
- `next_card()`: This function is called when the "Next" button is clicked. It moves to the next flashcard in the sequence.
- `previous_card()`: This function is called when the "Previous" button is clicked. It goes back to the previous flashcard.
- `restart_cards()`: This function is called when the "Restart" button is clicked. It resets the flashcards, allowing you to go through them again from the beginning.

Note that the itemconfig() method can only be used on a canvas object or widget that represents a canvas, while the config() method can be used on any tkinter widget.

Feel free to modify the provided flashcards in the `data/french_words.csv` file to suit your learning needs. Add your own question and answer pairs to expand the flashcards collection.

