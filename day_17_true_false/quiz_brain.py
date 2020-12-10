"""Class to manage the  quiz"""


class QuizBrain:
    """Quiz class

    Args:
        question_list (list): List of questions
    """
    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list

    def next_question(self):
        """Fetch the next question"""
        current_question = self.question_list[self.question_number]
        current_text = current_question.text
        self.question_number += 1
        user_answer = input(
            f'Q.{self.question_number}:' \
            f' {current_text} (True/False)?: '
        )
        self.check_answer(user_answer, current_question.answer)

    def still_has_questions(self):
        """Check if there are still quesitons

        Returns:
            bool
        """
        return len(self.question_list) > self.question_number

    def check_answer(self, user_answer, current_question):
        """Check a users answer

        Args:
            user_answer (str): User answer
            current_question (str): Answer for the current question
        """
        if user_answer.lower() == current_question.lower():
            self.score += 1
            print('You got it right!')
        else:
            print('That is wrong')

        print(f'The correct answer was :{current_question}')
        print(f'Your current score is {self.score}/{self.question_number}')
        print('')



