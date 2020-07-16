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
from ServiceManager.service_manager import process_project

baseURL = "https://c1ad24caa1f6.ngrok.io"

def get_projects(amount):
    """ funtion get_projects : gets projects from API

    Args:
        amount (integer): Amount of projects to get from the API

    Returns:
        [list/json]: The projects in json
    """
    response = requests.get(baseURL + "/api/projects/size/" + str(amount))
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
    response = requests.get(baseURL + "/api/publications/size/" + str(amount))
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
# print(get_publication_by_uuid("85dbe745-772d-472e-b5fa-3e6d36f966d4"))

class MyEncoder(json.JSONEncoder):
    def default(self, o):
        return o.__dict__
        
projects = get_projects(1)
for p in projects:
    project = Project(p["id"],p["title"]["englishTitle"],p["title"]["dutchTitle"],p["englishKeywords"],p["dutchKeywords"],p["abstract"]["englishAbstract"],p["abstract"]["dutchAbstract"])
    # response = requests.post("http://localhost:5000/api/projects/enrich", MyEncoder().encode(project))
    process_project(project)

# publications = get_publications(500)
# for publication in publications:
#     if publication['doi'] :
#         print(publication)