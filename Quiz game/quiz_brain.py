class QuizBrain:
    def __init__(self, questions):
        self.question_num = 0
        self.score = 0
        self.questions = questions
        self.currentque = None
    def still_more(self):
        return (self.question_num < len(self.questions))
    def go_to_next(self):
        self.currentque = self.questions[self.question_num]
        self.question_num+=1
        q_text = self.currentque.question_text
        return f"Q.{self.question_num}: {q_text}"
    def check_answer(self, u_answer):
        correct = self.currentque.correct_answer
        if u_answer.lower() == correct.lower:
            self.score +=1
            return True
        else : return False
    def get_score(self):
        wrong = self.question_num - self.score
        score_percent = int(self.score / self.question_num * 100)
        return (self.score, wrong, score_percent)