from ques_model import Question
from quiz_data import q_data
from quiz_brain import QuizBrain
from quiz_ui import Quiz_Ui
from random import shuffle
import html
ques_bank =[]
for question in q_data:
    choices = []
    question_text = html.unescape(question["question"])
    correct_answer =html.unescape(question["correct_answer"])
    wrong_answers = question["incorrect_answers"]
    for answer in wrong_answers:
        choices.append(html.unescape('answer'))
    choices.append(correct_answer)
    shuffle(choices)
    newques = Question(question_text, correct_answer, choices)
    ques_bank.append(newques)
    quiz = QuizBrain(ques_bank)
    quiz_ui = Quiz_Ui(quiz)
    print("Quiz Done")
    print(f"Total Score: {quiz.score}/{quiz.question_num}")