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
import json

ensp = en_core_web_sm.load()
nlsp = nl_core_news_sm.load()
ensp_singlewords = en_core_web_sm.load(disable=['parser', 'ner']) # just keep tagger for lemmatization for English
nlsp_singlewords = nl_core_news_sm.load(disable=['parser', 'ner']) # just keep tagger for lemmatization for Dutch

en_stopwords = ensp.Defaults.stop_words
nl_stopwords = nlsp.Defaults.stop_words

keyword_dict_nl = collections.Counter()
keyword_dict_en = collections.Counter()

def compose_keyword_dictionary():
    keywords_list_en =  read_with_lang("Utils/researchoutput_uuid_keywords.csv", 'en')
    keywords_list_nl =  read_with_lang("Utils/researchoutput_uuid_keywords.csv", 'nl')
    idf_dict_en = collections.Counter()
    for keyword in keywords_list_en:
        keyword.keyword = " ".join([token.lemma_.lower() for token in ensp_singlewords(keyword.keyword)])
        idf_dict_en[keyword.keyword] += 1

    idf_dict_nl = collections.Counter()
    for keyword in keywords_list_nl:
        keyword.keyword = " ".join([token.lemma_.lower() for token in nlsp_singlewords(keyword.keyword)])
        idf_dict_nl[keyword.keyword] += 1
    
    json_en = json.dumps(idf_dict_en)
    f_en = open("Strategies/NetworkRelation/keyword_dict_en.json", "w")
    f_en.write(json_en)
    f_en.close

    json_nl = json.dumps(idf_dict_nl)
    f_nl = open("Strategies/NetworkRelation/keyword_dict_nl.json", "w")
    f_nl.write(json_nl)
    f_nl.close

def read_dictionaries_from_file():
    global keyword_dict_en
    with open("Strategies/NetworkRelation/keyword_dict_en.json", 'r') as f_en:
        keyword_dict_en = json.load(f_en)
    global keyword_dict_nl
    with open("Strategies/NetworkRelation/keyword_dict_nl.json", 'r') as f_nl:
        keyword_dict_nl = json.load(f_nl)

def get_keyword_dict_nl():
    if not keyword_dict_nl:
        print("Load dutch keyword dictionary in memory")
        read_dictionaries_from_file()
    return keyword_dict_nl

def get_keyword_dict_en():
    if not keyword_dict_en:
        print("Load english keyword dictionary in memory")
        read_dictionaries_from_file()
    return keyword_dict_en

