# -*- coding: utf-8 -*-

import sys
import os

#3 lines of code to get the import form other files working
PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

#Utils
from Utils.fris_entities import Publication, Project
from Utils.enricher_entities import PublicationResult, ProjectResult, Keyword, Doi
from Utils.csv_reader import read

#Strategies
import Strategies.TextRank.textrank as strategy_textrank
import Strategies.Synonyms.synonyms as strategy_synonyms
import Strategies.NetworkRelation.networkrelation as strategy_network
import Strategies.UnpaywallCheck.doiPaywall as strategy_doi_paywall
from Strategies.NetworkRelation.keyword_dictionary import get_keyword_dict_en, get_keyword_dict_nl

#Collections
from collections import Counter

#Load network relation in memory
get_keyword_dict_en()
get_keyword_dict_nl()

def enrich_publication(publication_object):
    
    if isinstance(publication_object, Publication):
        keywords = get_keywords(publication_object.abstract_en, publication_object.keywords_en, publication_object.abstract_nl, publication_object.keywords_nl)
        doi_object = strategy_doi_paywall.add_doi_object(publication_object.doi)
        publication_result = PublicationResult(publication_object.uuid, doi_object,keywords)
        print("Enricher: publication enriched")
    else:
        publication_result = PublicationResult(publication_object.uuid, None, None)
        print("Enricher: invalid publication object")
   
    return publication_result

def enrich_project(project_object):
    if isinstance(project_object, Project):
        keywords = get_keywords(project_object.abstract_en, project_object.keywords_en, project_object.abstract_nl, project_object.keywords_nl)
        project_result = ProjectResult(project_object.uuid, keywords)
        print("Enricher: project enriched")
    else:
        project_result = ProjectResult(project_object.uuid, None)
        print("Enricher: invalid project object")
    return project_result



def get_best_keywords_en(abstract_en, keywords_en, max_number):
    
    synonyms_en = Counter()
    if keywords_en:
        synonyms_en = strategy_synonyms.get_synonym_by_word_list(keywords_en, 'eng')

    textrank_en = Counter()
    network_en = Counter()
    if abstract_en:
        textrank_en = strategy_textrank.textrank_keywords(abstract_en, 'en')
        network_en = strategy_network.calculate_relations(abstract_en, 'en')

    #English keyword combination
    tr_network_combi_dict_en = textrank_en + network_en
    intersection_en = Counter()
    for keyword, score in tr_network_combi_dict_en.items():
        if keyword in textrank_en:
            intersection_en[keyword] = score
    best_keywords_en = (intersection_en + synonyms_en).most_common(max_number)

    return best_keywords_en    


def get_best_keywords_nl(abstract_nl, keywords_nl, max_number):
    
    synonyms_nl = Counter()
    if keywords_nl:
        synonyms_nl = strategy_synonyms.get_synonym_by_word_list(keywords_nl, 'nld')

    textrank_nl = Counter()
    network_nl = Counter()
    if abstract_nl:
        textrank_nl = strategy_textrank.textrank_keywords(abstract_nl, 'nl')
        network_nl = strategy_network.calculate_relations(abstract_nl, 'nl')

    #Dutch keyword combination
    tr_network_combi_dict_nl = textrank_nl + network_nl
    intersection_nl = Counter()
    for keyword, score in tr_network_combi_dict_nl.items():
        if keyword in textrank_nl:
            intersection_nl[keyword] = score
    best_keywords_nl = (intersection_nl + synonyms_nl).most_common(max_number)
    
    return best_keywords_nl   

def get_keywords(abstract_en, keywords_en, abstract_nl, keywords_nl):
    best_keywords_en = get_best_keywords_en(abstract_en, keywords_en, 10)
    best_keywords_nl = get_best_keywords_nl(abstract_nl, keywords_nl, 10)
    keyword_list = []
    for keyword_score in best_keywords_en:
        keyword_list.append(Keyword(keyword_score[1], keyword_score[0], 'en'))
    
    for keyword_score in best_keywords_nl:
        keyword_list.append(Keyword(keyword_score[1], keyword_score[0], 'nl'))

    return keyword_list