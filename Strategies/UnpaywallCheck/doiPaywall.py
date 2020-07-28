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

from Utils.enricher_entities import Doi

"""
If you handle a publication json with a doi    

"""


def add_doi_object(publication_doi_url):
    """
    Return a doi object to the Enricher containing for the doi different information like : 
        doi, data_received_from_Unpaywall_api, no_paywall, pdf_url

    Args:
        publication_doi (str): doi of a publication 

    Returns:
        Doi object: Doi object with the fields : doi, data_received_from_Unpaywall_api, no_paywall, pdf_url
    """
    doi = extract_doi_from_url(publication_doi_url)
    data_received_from_Unpaywall_api, no_paywall, pdf_url = add_pdf_information_of_doi(doi)
    doi_obj = Doi(publication_doi, data_received_from_Unpaywall_api, no_paywall, pdf_url)

    return doi_obj


def extract_doi_from_url(doi_url):
    """
    Extract doi from a doi url

    Args:
        doi url (str): doi url

    Returns:
        doi: doi from the doi url
    """
    slashparts = doi_url.split('https://doi.org/')

    if len(slashparts) < 2:
        return ""

    return slashparts[1]

def add_pdf_information_of_doi(doi):

    """
    add the different information to the doi object because of its json file

    Args:
        dois (str): doi 
    
    Returns:
        bool, bool, str : data_received_from_Unpaywall_api, no_paywall, pdf_url
    """

    if doi == "":
        return False, False, ""

    data_received_from_Unpaywall_api = True

    file = get_unpaywall_api_data(doi)
    try:
        jsonfile = json.loads(file)
    except:
        data_received_from_Unpaywall_api = False

    no_paywall = jsonfile["is_oa"]
    
    if jsonfile["best_oa_location"] is not None:
        pdf_url = jsonfile["best_oa_location"]["url_for_pdf"]
    else:
        pdf_url = "No pdf"
    
    return data_received_from_Unpaywall_api, no_paywall, pdf_url



def get_unpaywall_api_data(doi):
    """
    Get the json of the doi from the Unpaywall API and store it in the file "file_to_save_to"

    Args:
        doi (string): doi 

    Returns:
        JSON string: Json string containing all the data from the Unpaywall API
    """
    url = f'http://api.unpaywall.org/v2/{doi}?email=baudlemartino@hotmail.com'

    file_to_save_to = ""
    with requests.get(url, stream=True) as r:
        if r.status_code == 200:
            #for chunk in r.iter_content(chunk_size=1024*1024):
                #file_to_save_to.write(chunk)
                file_to_save_to = file_to_save_to + r.text
                
    return file_to_save_to


