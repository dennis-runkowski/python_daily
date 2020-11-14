"""
Extract features from text. Two different approaches
    1. TFIDF
    2. Spacy -> noun chunks
"""
from collections import defaultdict
import logging
import re

from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import spacy

import seaborn as sns
from matplotlib import pyplot as plt
from bs4 import BeautifulSoup
import pandas as pd

logging.basicConfig(level=logging.DEBUG)
log = logging
STEMMER = WordNetLemmatizer()
NLP = spacy.load('en_core_web_lg')


class FeatureExtraction(object):
    def __init__(self, documents, min_df=2, max_df=0.5, n_grams=2,
                 max_features=100):
        """
        Args for the FeatureExtraction class

        Args:
            documents (list): List of documents (text)
            min_df (int): ignore terms that appear in less than x documents
            max_df (int): ignore terms that appear in more than x% of the
            documents
            n_grams (int): Number of n-grams you want to use, default is 2 (
            bi-grams)
        """
        self.docs = documents
        self.tfidf = TfidfVectorizer(
            min_df=min_df,
            max_df=max_df,
            max_features=max_features,
            ngram_range=(1, n_grams),
            stop_words=stopwords.words('english')
        )

    def clean_data(self):
        """
        Clean the documents.
            -> remove single char
            -> remove starting single char
            -> remove multi spaces
            -> remove html
            -> make lowercase
            -> lemmatize tokens i.e cars = car
        """
        clean_documents = []
        for doc in self.docs:
            # remove all single characters
            document = re.sub(r'\s+[a-zA-Z]\s+', ' ', doc)

            # Remove single characters from the start
            document = re.sub(r'\^[a-zA-Z]\s+', ' ', document)

            # Substituting multiple spaces with single space
            document = re.sub(r'\s+', ' ', document, flags=re.I)

            # Remove HTML
            document = BeautifulSoup(document, features="lxml")

            document = document.text

            document = document.lower()
            _temp = []
            for wrd in document.split(" "):

                if not wrd.isdigit():
                    # Remove all the special characters
                    wrd = re.sub(r'\W', '', wrd)
                    _temp.append(STEMMER.lemmatize(wrd))

            clean_documents.append(" ".join(_temp))

        self.docs = clean_documents


    def get_features(self):
        """
        Extracts features from the corpus of docs

        Returns:
            list of features
        """
        self.features = self.tfidf.fit_transform(self.docs)
        return self.tfidf.get_feature_names()

    def get_features_spacy(self):
        """
        Get features using spacy for a corpus of documents

        Returns:
            sorted list of tuples containing features and their frequency
        """

        feature_dict = defaultdict(lambda: 0)
        for doc in self.docs:
            nlp_doc = NLP(doc)
            for chunk in nlp_doc.noun_chunks:
                feature_dict[chunk.text] += 1

        sorted_features = sorted(
            dict(feature_dict).items(), key=lambda x: x[1])
        return sorted_features


    def plot_heatmap(self, doc_end, doc_start=0):
        """
        Plot a heatmap of the features by the document TFIDF score
        Args:
            doc_end (int): last document to include in the heatmap
            doc_start (int): starting document for the heatmap
        Returns:
            sns heatmap figure
        """
        df = pd.DataFrame(
            self.features.todense(),
            columns=self.tfidf.get_feature_names()
        )
        transformed_df = df[doc_start:doc_end].loc[
                         :, (df[doc_start:doc_end] != 0).any(axis=0)]

        plt.figure(figsize=(15, 12))
        fig = sns.heatmap(
            transformed_df,
            cmap='coolwarm',
            linecolor='black',
            linewidths=1,
            annot=True
        )
        fig.set(xlabel='Features', ylabel='Documents', title='Feature Heatmap')
        plt.show()

    def feature_rank(self):
        """
        Rank all the features by their frequency
        Returns:

        """
        mapping_matrix = self.features.todense()
        feature_count = defaultdict(lambda: 0)
        feature_names = self.tfidf.get_feature_names()
        for idx, name in enumerate(feature_names):
            for score in mapping_matrix:
                if score[0, idx] > 0.00:
                    feature_count[name] += 1

        sorted_features = sorted(
            dict(feature_count).items(),key=lambda x: x[1] )
        return sorted_features


