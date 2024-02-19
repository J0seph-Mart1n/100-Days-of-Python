from question_model import Question
from data import question_data_computer,question_data_gk,question_data_anime,question_data_film
from quiz_brain import QuizBrain
import random
import sys

question_bank = []
choice = input("Choose the category for the quiz: (anime,computer,gk,film)")
if choice == 'anime':
    for question in question_data_anime:
        question_bank.append(Question(question['question'],question['correct_answer']))
elif choice == 'computer':
    for question in question_data_computer:
        question_bank.append(Question(question['question'],question['correct_answer']))
elif choice == 'gk':
    for question in question_data_gk:
        question_bank.append(Question(question['question'],question['correct_answer']))
elif choice == 'film':
    for question in question_data_film:
        question_bank.append(Question(question['question'],question['correct_answer']))
else:
    print("Invalid Choice")
    sys.exit()

random.shuffle(question_bank)

quizBrain = QuizBrain(question_bank)
while quizBrain.still_has_questions():
    quizBrain.next_question()

print("You've Completed the quiz")
print(f"Your final score: {quizBrain.score}/{quizBrain.question_number}")