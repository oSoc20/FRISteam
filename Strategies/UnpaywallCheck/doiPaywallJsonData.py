# -*- coding: utf-8 -*-
"""
Author Baudouin Martelee
FRISteam

"""
#Import packages
import os
import pandas as pd
import json
import glob
import requests
import sys

#3 lines of code tot get the import form other files working
PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from Enricher.enricher import get_publications_with_doi, get_publications_list

baseURL = "https://c2d3eecf4542.ngrok.io"



def get_json_with_doi():
    publi_list = get_publications_list(amount_publication)
    json_obj_list = get_publications_with_doi(publi_list)
    print(type(json_obj_list))
    print(json_obj_list)




if __name__ == "__main__":

    get_json_with_doi()