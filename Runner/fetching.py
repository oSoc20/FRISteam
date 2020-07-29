""" Python module to fetch data from the API
"""
import json

import requests # python -m pip install requests

import sys
import os

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from Cleanup.datacleaning import clean_data
from Utils.fris_entities import Project, Publication

baseURL = "https://e7575fb0f6d4.ngrok.io/"

def get_projects(amount):
    """ funtion get_projects : gets projects from API

    Args:
        amount (integer): Amount of projects to get from the API

    Returns:
        [list/json]: The projects in json
    """
    response = requests.get(baseURL + "api/projects/size/" + str(amount))
    projects = json.loads(response.text)
    return projects
    

def get_project_by_uuid(uuid): 
    """ function get_project_by_uuid : Gets 1 project from the API 

    Args:
       uuid (string): The ID of the project to get

    Returns:
        [json]: The project  in json
    """
    response = requests.get(baseURL + "/api/projects/" + uuid)
    project = json.loads(response.text)
    return project


def get_publications(amount):
    """ funtion get_publications : gets publications from API

    Args:
        amount (integer): Amount of publications to get from the API

    Returns:
        [list/json]: The publications in json
    """
    response = requests.get(baseURL + "api/publications/size/" + str(amount))
    publications = json.loads(response.text)
    return publications


def get_publication_by_uuid(uuid): 
    """ function get_publication_by_uuid : Gets 1 publication from the API 

    Args:
       uuid (string): The ID of the publication to get

    Returns:
        [json]: The publication  in json
    """
    response = requests.get(baseURL + "/api/publications/" + uuid)
    publication = json.loads(response.text)
    return publication

# print(get_projects(20))
# print(get_project_by_uuid("6fa0f7de-4502-4995-92ae-5467e49df1b3"))
# print(get_publications(200))
# print(get_publication_by_uuid("8e60ac99-8687-4425-8e68-d42a11d4362f"))

#get projects and send them to the http_server one by one  

projects = get_projects(100)
for p in projects:
    json_project = {}
    json_project["uuid"] = p["id"]
    json_project["keywordsEn"] = p["englishKeywords"]
    json_project["keywordsNl"] = p["dutchKeywords"]
    if p["abstract"]:
        json_project["abstractEn"] = p["abstract"]["englishAbstract"]
        json_project["abstractNl"] = p["abstract"]["dutchAbstract"]
    else:
        json_project["abstractEn"] = None
        json_project["abstractNl"] = None
   
    json_project["titleEn"] = p["title"]["englishTitle"]
    json_project["titleNl"] = p["title"]["dutchTitle"]
    

    headers = {'Content-Type': 'application/json'}
    response = requests.post("http://127.0.0.1:5000/api/projects/enrich", json = json_project, headers=headers)


# #get publications and send them to the http_server one by one

publications = get_publications(100)
for p in publications:
    json_publication = {}
    json_publication["uuid"] = p["id"]
    json_publication["keywordsEn"] = p["englishKeywords"]
    json_publication["keywordsNl"] = p["dutchKeywords"]
    if p["abstract"]:
        json_publication["abstractEn"] = p["abstract"]["englishAbstract"]
        json_publication["abstractNl"] = p["abstract"]["dutchAbstract"]
    else:
        json_publication["abstractEn"] = None
        json_publication["abstractNl"] = None

    json_publication["titleEn"] = p["title"]["englishTitle"]
    json_publication["titleNl"] = p["title"]["dutchTitle"]
    json_publication["doi"]=p["doi"]


    headers = {'Content-Type': 'application/json'}
    response = requests.post("http://127.0.0.1:5000/api/publications/enrich", json = json_publication, headers=headers)


