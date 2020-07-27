# -*- coding: utf-8 -*-

import sys
import os

#3 lines of code to get the import form other files working
PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

#Utils
from Utils.fris_entities import Publication, Project
from Utils.enricher_entities import PublicationResult
from Utils.csv_reader import read

#Strategies
import Strategies.TextRank.textrank as strategy_textrank
import Strategies.Synonyms.synonyms as strategy_synonyms
import Strategies.NetworkRelation.networkrelation as strategy_network
import Strategies.UnpaywallCheck.doiPaywall as strategy_doi_paywall

#Collections
from collections import Counter

def enrich_publication(publication_object):
    
    if isinstance(publication_object, Publication):
<<<<<<< HEAD
        textrank_en = strategy_textrank.textrank_keywords(publication_object.abstract_en, 'en')
        textrank_nl = strategy_textrank.textrank_keywords(publication_object.abstract_nl, 'nl')
        synonyms_en = strategy_synonyms.get_synonym_by_word_list(publication_object.keywords_en, 'eng')
        synonyms_nl = strategy_synonyms.get_synonym_by_word_list(publication_object.keywords_nl, 'nld')
        network_en = strategy_network.calculate_relations(publication_object.abstract_en, read("researchoutput_uuid_keywords.csv"), 'en')
        network_nl = strategy_network.calculate_relations(publication_object.abstract_nl, read("researchoutput_uuid_keywords.csv"), 'nl')
=======
        textrank_en = Counter()
        print("Abstract EN: ", publication_object.abstract_en)
        if publication_object.abstract_en:
            textrank_en = strategy_textrank.textrank_keywords(str(publication_object.abstract_en), 'en')
        textrank_nl = Counter()
        print("Abstract NL: ", publication_object.abstract_nl)
        if publication_object.abstract_nl:
            textrank_nl = strategy_textrank.textrank_keywords(publication_object.abstract_nl, 'nl')
        
        print("KEYWORDS EN: ", publication_object.keywords_en)
        synonyms_en = strategy_synonyms.get_synonym_by_word_list(publication_object.keywords_en, 'eng')
        print("KEYWORDS NL: ", publication_object.keywords_nl)
        synonyms_nl = strategy_synonyms.get_synonym_by_word_list(publication_object.keywords_nl, 'nld')
        network_en = Counter()
        if publication_object.abstract_en:
            network_en = strategy_network.calculate_relations(publication_object.abstract_en, 'en')
        network_nl = Counter()
        if publication_object.abstract_nl:
            network_nl = strategy_network.calculate_relations(publication_object.abstract_nl, 'nl')
>>>>>>> 796193fc71ab1fa2c4fbd7d96ad3bd02aa59c821
        #print(textrank_en)
        #print(textrank_nl)
        #print(synonyms_en)
        #print(synonyms_nl)
        #print(network_en)
        #print(network_nl)

        # this only works if all textrank_, synonyms_ and network_ outputs are Counter dictionaries (initialize by Counter(dict)), 
        # it returns the 10 highest scoring keywords as a list of tuples [(keyword, score), ...]
<<<<<<< HEAD
        # best_keywords_en = (textrank_en + synonyms_en + network_en).most_common(10)
        # best_keywords_nl = (textrank_nl + synonyms_nl + network_nl).most_common(10)
=======
        best_keywords_en = (textrank_en + synonyms_en + network_en).most_common(10)
        best_keywords_nl = (textrank_nl + synonyms_nl + network_nl).most_common(10)
        print("BEST KEYWORDS EN: ", best_keywords_en)
        print("BEST KEYWORDS NL: ", best_keywords_nl)
>>>>>>> 796193fc71ab1fa2c4fbd7d96ad3bd02aa59c821
        print("Enricher: publication enriched")
    else:
        print("Enricher: invalid publication object")
    """
    if isinstance(publication_object, Publication):
        doi_object = strategy_doi_paywall.add_doi_object(publication_object.doi)
        print(doi_object.doi)
        print(doi_object.data_received)
        print(doi_object.no_paywall)
        print(doi_object.pdf_url)

        publication_obj_result = PublicationResult(publication_object.uuid, doi_object)
        print(publication_obj_result)
        print(publication_obj_result.uuid)
        print(publication_obj_result.doi)
        
        print("Enricher: publication enriched")
    else:
        print("Enricher: invalid publication object")

    return publication_object
    """

def enrich_project(project_object):
    """
    if isinstance(project_object, Project):
        textrank_en = strategy_textrank.textrank_keywords(str(project_object.abstract_en), 'en')
        textrank_nl = strategy_textrank.textrank_keywords(str(project_object.abstract_nl), 'nl')
        synonyms_en = strategy_synonyms.get_synonym_by_word_list(str(project_object.keywords_en), 'eng', 10)
        synonyms_nl = strategy_synonyms.get_synonym_by_word_list(str(project_object.keywords_nl), 'nld', 10)
        network_en = strategy_network.calculate_relations(publication_object.abstract_en, read("researchoutput_uuid_keywords.csv"), 'en')
        network_nl = strategy_network.calculate_relations(publication_object.abstract_nl, read("researchoutput_uuid_keywords.csv"), 'nl')
        print(textrank_en)
        print(textrank_nl)
        print(synonyms_en)
        print(synonyms_nl)
        print("Enricher: project enriched")
    else:
        print("Enricher: invalid project object")
    """
    return project_object



#TESTING