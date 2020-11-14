"""
Class to get the similarity between two strings. This is only meant for english
text.

Usage:
    install spacy --> pip install spacy
    download -->  python -m spacy download en_core_web_lg
"""
import logging
import re
import spacy
from spacy.lang.en import STOP_WORDS

logging.basicConfig(level=logging.DEBUG)
log = logging
nlp = spacy.load('en_core_web_lg')
stop_words = STOP_WORDS


class TextSimilarity(object):

    def __init__(self, text_1, text_2):
        """
        Init the class with two strings that will be compared.
        Args:
            text_1 (str): String of text
            text_2 (str): String of text
        """
        if not isinstance(text_1, str):
            log.error("Please only pass in type str")
            raise TypeError

        if not isinstance(text_2, str):
            log.error("Please only pass in type str")
            raise TypeError

        self.data = [text_1, text_2]

    def remove_stop_words(self):
        """
        Clean the text by removing stop words
        """
        _new_data = []
        for text in self.data:
            tokens = text.split(' ')
            cleaned = [i for i in tokens if i not in stop_words]
            new_text = ' '.join(cleaned)
            _new_data.append(new_text)

        self.data = _new_data

    def remove_punctuation(self):
        """
        Remove punctuation from the text
        """
        _new_data = []
        for text in self.data:
            new_text = re.sub(r'[^\w\s]', '', text)
            _new_data.append(new_text)

        self.data = _new_data

    def lowercase(self):
        """
        Make the text lower case
        """
        _new_data = [text.lower() for text in self.data]
        self.data = _new_data

    def text_similarity(self):
        """
        Returns:
            similarity score between two strings.
        """
        text_1 = nlp(self.data[0])
        text_2 = nlp(self.data[1])
        score = text_1.similarity(text_2)
        return score

    def __repr__(self):
        """
        clean way to view the current state of self.data
        """

        return 'Text_1: {i}, Text_2: {x}'.format(i=self.data[0], x=self.data[1])
