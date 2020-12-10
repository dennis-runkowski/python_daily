"""Question game"""

from question_model import Question
from quiz_brain import QuizBrain
from data import question_data


def main():
    """Main function to run"""
    question_bank = []
    for question in question_data:
        text = question['question']
        answer = question['correct_answer']
        new_question = Question(text, answer)
        question_bank.append(new_question)

    brain = QuizBrain(question_bank)

    while brain.still_has_questions():
        brain.next_question()

    print(f'You completed the quiz')
    print(f'Your final score was: {brain.score}/{brain.question_number}')


if __name__ == "__main__":
    main()
