from art import Art
from data import question_data
from quiz_brain import QuizBrain
from question_model import Question

art = Art()


def main():
    # print logo - art 
    art.print_logo()
    
    # First thing is to initialize the question bank to be an empty list, 
    # format the question data and create own quiz bank
    question_bank = []

    # Manipulating a list of dictionaries
    for question in question_data:
        question_text = question["question"]
        question_answer = question["correct_answer"]
        new_question = Question(question_text, question_answer)
        question_bank.append(new_question)

    #print(question_bank)
    
    # Creates an instance of QuizBrain object named quiz
    # question_list is the question bank
    # score and question_number = 0 

    quiz = QuizBrain(question_bank)

    while quiz.still_has_questions():
        quiz.next_question()

    print("You've completed the quiz. ")
    print(f"Your final score was: {quiz.score}/{quiz.question_number}. ")



if __name__ == "__main__":
    main()