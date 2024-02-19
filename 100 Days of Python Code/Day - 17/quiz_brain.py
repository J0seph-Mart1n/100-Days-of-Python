class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number<10

    def check_answer(self,user_answer,correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You have got the right answer")
            self.score+=1
        else:
            print("You answer is wrong")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your score: {self.score}/{self.question_number}")

    def next_question(self):
        question = self.question_list[self.question_number]
        user_answer = input(f"Q.{self.question_number+1}: {question.text} (True/False)?: ")
        self.question_number+=1
        self.check_answer(user_answer, question.answer)


