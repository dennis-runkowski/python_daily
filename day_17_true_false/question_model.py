"""Question Model"""


class Question:
    """Model for Questions

    Args:
        text (str): text for the question
        answer (str): question answer
    """
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

