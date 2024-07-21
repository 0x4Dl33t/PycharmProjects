class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0
        self.count = 0

    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        elif self.question_number == len(self.question_list):
            print(f"\n\n*************************** \nYou've completed the quiz! "
                  f"\nYour final score is {self.score}/{self.count}. \n*************************** \n")
            return False

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"\nQ.{self.question_number}: {current_question.text} True or False? ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        self.count += 1
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print(f"\nYou got it right! 🙂\nThe correct answer is {correct_answer}. "
                  f"\nYour current score is {self.score}/{self.count}. ")
        else:
            print(f"\nYou got it wrong! 😔\nThe correct answer is {correct_answer}. "
                  f"\nYour current score is {self.score}/{self.count}. ")
