# -*- coding: utf-8 -*-
"""
Created on Sun Aug  28 08:35:39 2022

@author: GabrielADKN
"""

import numpy as np
import nltk
# nltk.download('punkt')
from nltk.stem.porter import PorterStemmer
stemmer = PorterStemmer()

def tokenize(sentence):
    """
    diviser la phrase en un tableau de mots / jetons
    un jeton peut être un mot ou un caractère de ponctuation, ou un nombre
    """
    return nltk.word_tokenize(sentence)


def stem(word):
    """
    stemming = trouver la forme racine du mot
    Exemples:
    words = ["organize", "organizes", "organizing"]
    words = [stem(w) for w in words]
    -> ["organ", "organ", "organ"]
    """
    return stemmer.stem(word.lower())


def bag_of_words(tokenized_sentence, words):
    """
    retour de sac de tableau de mots:
    1 pour chaque mot connu qui existe dans la phrase, 0 sinon
    exemple:
    sentence = ["hello", "how", "are", "you"]
    words = ["hi", "hello", "I", "you", "bye", "thank", "cool"]
    bog   = [  0 ,    1 ,    0 ,   1 ,    0 ,    0 ,      0]
    """
    # stem each word
    sentence_words = [stem(word) for word in tokenized_sentence]
    # initialize bag with 0 for each word
    bag = np.zeros(len(words), dtype=np.float32)
    for idx, w in enumerate(words):
        if w in sentence_words:
            bag[idx] = 1

    return bag