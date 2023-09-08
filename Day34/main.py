from question_model import Question
from data import questions_data
from quiz_brain import QuizBrain
from ui import QuizInterface

question_bank = []

# for each question in question data
#{'response_code': 0, 'results': [{'category': 'Entertainment: Television', 'type': 'boolean', 'difficulty': 'medium', 'question': 'AMC&#039;s &quot;The Walking Dead&quot;, Rick, Carl, Daryl, Morgan, Carol and Maggie were introduced to us in Season 1.', 'correct_answer': 'False', 'incorrect_answers': ['True']}, {'category': 'Entertainment: Video Games', 'type': 'boolean', 'difficulty': 'hard', 'question': 'In &quot;The Sims&quot; series, the most members in a household you can have is 8.', 'correct_answer': 'True', 'incorrect_answers': ['False']}, {'category': 'Mythology', 'type': 'boolean', 'difficulty': 'easy', 'question': 'In Norse mythology, Thor once dressed as a woman.', 'correct_answer': 'True', 'incorrect_answers': ['False']}, {'category': 'Geography', 'type': 'boolean', 'difficulty': 'easy', 'question': 'A group of islands is called an &#039;archipelago&#039;.', 'correct_answer': 'True', 'incorrect_answers': ['False']}, {'category': 'Science: Gadgets', 'type': 'boolean', 'difficulty': 'medium', 'question': 'The Western Electric Model 500 telephone uses tone dialing to dial phone numbers.', 'correct_answer': 'False', 'incorrect_answers': ['True']}, {'category': 'Mythology', 'type': 'boolean', 'difficulty': 'hard', 'question': 'Rannamaari was a sea demon that haunted the people of the Maldives and had to be appeased monthly with the sacrifice of a virgin girl.', 'correct_answer': 'True', 'incorrect_answers': ['False']}, {'category': 'History', 'type': 'boolean', 'difficulty': 'easy', 'question': 'In World War ll, Great Britian used inflatable tanks on the ports of Great Britain to divert Hitler away from Normandy/D-day landing.', 'correct_answer': 'True', 'incorrect_answers': ['False']}, {'category': 'Entertainment: Japanese Anime & Manga', 'type': 'boolean', 'difficulty': 'hard', 'question': 'Druid is a mage class in &quot;Log Horizon&quot;.', 'correct_answer': 'False', 'incorrect_answers': ['True']}, {'category': 'Entertainment: Video Games', 'type': 'boolean', 'difficulty': 'medium', 'question': 'In &quot;League of Legends&quot;, there exists four different types of Dragon.', 'correct_answer': 'False', 'incorrect_answers': ['True']}, {'category': 'Entertainment: Japanese Anime & Manga', 'type': 'boolean', 'difficulty': 'hard', 
#'question': 'The protagonist in &quot;Humanity Has Declined&quot; has no discernable name and is simply referred to as &#039;I&#039; for most of the series.', 'correct_answer': 'True', 'incorrect_answers': ['False']}]}

for question in questions_data:
    question_text = question["question"]
    try:
        print(question_text)
    except Exception as e:
        print(e)
    question_answer = question["correct_answer"]
    # Instantiates a new Question() object
    new_question = Question(question_text, question_answer)
    #print(new_question)
    question_bank.append(new_question)
print(question_bank)


quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)