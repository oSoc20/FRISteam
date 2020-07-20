# -*- coding: utf-8 -*-

import sys
import os

#3 lines of code to get the import form other files working
PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
import Strategies.TextRank.textrank
import Strategies.Synonyms.synonyms


def enrich_publication(publication_object):
    print("Enricher: publication enriched")
    return publication_object


def enrich_project(project_object):
    print("Enricher: project enriched")
    return project_object
