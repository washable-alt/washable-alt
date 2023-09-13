Day 34

# Use Open Trivia API to Create a quizlet GUI game.

How to use: 
`data.py`file - 
1. Create a token for the Opentrivia API - requests.get(url, params=parameters)
2. `url` is https://opentdb.com/api_token.php
3. `parameters` is a dictionary of key-value pairs
4. `key` - command
5. `value` - request
6. `response for token` - response.json()['token'] (session tokens are only valid for 6 hours)
7. To call the main API - request.get(url, params=parameters)
8. parameters are amount, type, token and category
9. data = response.json()
Note: set session token as "", and it can help to reset for the first time 


`quiz_brain.py` file - 
1. `__init__`: Takes in the questions_data, initialises itself with attributes question_number = 0, score = 0, question_list as q_list and sets current question as a None object
2. `still_has_questions`: return true if question number is less than the length of the question_list
3. `next_question`: Outputs the question from the question data in a f-string "Q.{self.question_number}: {q_text}"
4. `check_answer`: takes in the variable user_answer, and compare it with the correct answer, if the answers match, self.score increments by one and return True, else return False

`question_model.py` file:
1. Initialises a class that takes in text and answer
2. Question().text = q_text
3. Question().answer = q_answer

`ui.py` file:
Initialise a quiz interface that takes in the parameter quiz_brain and a type hint of class QuizBrain
1. Create a root window using Tkinter library
2. Set the width and height as 700x700 using Tk().geometry
3. Create Label for score
4. Create Canvas with height and width of 450
5. Use Canvas.create_text to create the Welcome to Quiz
6. Get next question
7. true_pressed - if true is pressed, give feedback(check user answer and quiz answer whether it is true)
8. false_pressed - if false is pressed, set is_right to `False`, check answer via the give feedback() function
9. give_feedback(is_right) - if is_right is `True`: set the bg of canvas as green, else set it to red

`main.py` file:
1. Initializes an empty question_bank, i.e., question_bank = []
2. Because this is a list of dictionaries, to access the questions from question_data, a `for` loop is needed 
3. append new question into question_bank
4. Initializes the quiz object with QuizBrain(question_bank) and quiz_ui with QuizInterface(quiz), it will get next question after initialising the user interface

Using `pprint` to print JSON dictionaries in a more organized way