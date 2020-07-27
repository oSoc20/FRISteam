# import necessary packages
import sys
import os

#3 lines of code to get the import form other files working
PACKAGE_PARENT = '../..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

import pandas as pd
import numpy as np
import re
import string
import spacy
from spacy.lang.en.stop_words import STOP_WORDS as en_STOP_WORDS
from spacy.lang.nl.stop_words import STOP_WORDS as nl_STOP_WORDS
import en_core_web_sm
import nl_core_news_sm
import collections
from Utils.fris_entities import Keyword
from Utils.csv_reader import read_with_lang
from Strategies.NetworkRelation.keyword_dictionary import get_keyword_dict_en, get_keyword_dict_nl

ensp = en_core_web_sm.load()
nlsp = nl_core_news_sm.load()
ensp_singlewords = en_core_web_sm.load(disable=['parser', 'ner']) # just keep tagger for lemmatization for English
nlsp_singlewords = nl_core_news_sm.load(disable=['parser', 'ner']) # just keep tagger for lemmatization for Dutch

en_stopwords = ensp.Defaults.stop_words
nl_stopwords = nlsp.Defaults.stop_words

def preprocess_abstract(text, langTag):
    """function preprocess_abstract : preprocesses a string (e.g. an abstract) with lowercasing, lemmatizing, stopword removal

   Args:
       text (string): a string
       langTag (string): the language of the words in text (e.g. 'en' for English and 'nl' for Dutch)

   Returns:
       list [of strings]: list of strings with the keyword candidates
   """
    if langTag == "en":
        abstract = ensp(text.translate(str.maketrans('', '', string.punctuation)))
        tokens = [word.lemma_ for word in abstract if not word.lemma_ in en_stopwords and len(word) > 1]
    elif langTag == "nl":
        abstract = nlsp(text.translate(str.maketrans('', '', string.punctuation)))
        tokens = [word.lemma_ for word in abstract if not word.lemma_ in nl_stopwords and len(word) > 1]       
    return tokens

def calculate_term_frequency(tokens):
    """function term_frequency : calculates the frequencies of terms from a list of words

   Args:
       tokens ([list of strings]): a list of strings (e.g. single words from an abstract)

   Returns:
       dict: {dictionary of possible keywords with their frequency relative to the total amount of words}
   """
    counter = collections.Counter()
    tf_dict = counter.copy()
    for word in tokens:
        counter[word] += 1
    for word in counter:
        tf_dict[word] = counter.get(word)/len(tokens)
    return tf_dict


def calculate_relations(abstract, langTag):
    print("CALCULATE_RELATIONS STARTED")
    tf_dict = calculate_term_frequency(preprocess_abstract(abstract, langTag))
    idf_dict = dict()
    if langTag == 'nl':
        idf_dict = get_keyword_dict_nl()
    elif langTag == 'en':
        idf_dict = get_keyword_dict_en()

    if tf_dict == {}:
        return {}
    print("TFIDF PART")
    for keyword in tf_dict:
        if keyword in idf_dict:
            tf_dict[keyword] = tf_dict[keyword]+(idf_dict[keyword]/len(idf_dict))
    print("CALCULATE_RELATIONS ENDED")
    return tf_dict