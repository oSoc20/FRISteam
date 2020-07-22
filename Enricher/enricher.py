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

#Strategies
import Strategies.TextRank.textrank as strategy_textrank
import Strategies.Synonyms.synonyms as strategy_synonyms
import Strategies.UnpaywallCheck.doiPaywall as strategy_doi_paywall






def enrich_publication(publication_object):
    """
    if isinstance(publication_object, Publication):
        textrank_en = strategy_textrank.textrank_keywords(publication_object.abstract_en, 'en')
        textrank_nl = strategy_textrank.textrank_keywords(publication_object.abstract_nl, 'nl')
        synonyms_en = strategy_synonyms.get_synonym_by_word_list(publication_object.keywords_en, 'eng', 10)
        synonyms_nl = strategy_synonyms.get_synonym_by_word_list(publication_object.keywords_nl, 'nld', 10)
        print(textrank_en)
        print(textrank_nl)
        print(synonyms_en)
        print(synonyms_nl)
        print("Enricher: publication enriched")
    else:
        print("Enricher: invalid publication object")
    """
    if isinstance(publication_object, Publication):
        doi_object = strategy_doi_paywall.add_doi_information(publication_object.doi)
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
    

def enrich_project(project_object):
    """
    if isinstance(project_object, Project):
        textrank_en = strategy_textrank.textrank_keywords(str(project_object.abstract_en), 'en')
        textrank_nl = strategy_textrank.textrank_keywords(str(project_object.abstract_nl), 'nl')
        synonyms_en = strategy_synonyms.get_synonym_by_word_list(str(project_object.keywords_en), 'eng', 10)
        synonyms_nl = strategy_synonyms.get_synonym_by_word_list(str(project_object.keywords_nl), 'nld', 10)
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