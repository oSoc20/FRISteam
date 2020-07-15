""" Python module to clean data.

The data is being requested on the SOAP API.
After that the characters that are not supposed to be there
    like '<p>', are removed.
The data is being placed into the right encoding.
"""

import json
import re

import ftfy # python -m pip install ftfy
import requests # python -m pip install requests

baseURL = "https://c2d3eecf4542.ngrok.io"


def clean_html(raw_html):
    """function clean_html: get the HTML-tags out of the data.

    Args:
        raw_html (string): original string with HTML-tags in it.

    Returns:
        string: clean string without HTML-tags
    """
    cleanr = re.compile("<.*?>")
    cleantext = re.sub(cleanr, "", raw_html)
    return cleantext

def remove_nbsp(text):
    """function remove_nbsp: Remove non breaking spaces from data.

    Args:
        text (string): original text

    Returns:
        string: cleaned text without the nbsp
    """
    cleantext = text.replace('\xa0', ' ')
    return cleantext

def clean_data(text):
    """ function clean_data: call other functions for cleaning the data.
        This function has been made to prevent having to call all the methds on the data.

    Args:
        text (string): the original data

    Returns:
        string: the fully cleaned data
    """
    text = ftfy.fix_text(text)
    text = clean_html(text)
    text = remove_nbsp(text)
    return text

def get_projects_and_clean(amount):
    """ funtion get_projects_and_clean : gets projects from API and cleans data

    Args:
        amount (integer): Amount of projects to get from the API
    """
    response = requests.get(baseURL + "/api/projects/size/" + str(amount))
    projects = json.loads(response.text)
    for project in projects:
        project['abstract']['dutchAbstract'] = clean_data(project['abstract']['dutchAbstract'])
        project['abstract']['englishAbstract'] = clean_data(project['abstract']['englishAbstract'])
        print(project)

def get_project_by_uuid(uuid): 
    """ function get_project_by_uuid : Gets 1 project from the API

    Args:
        uuid (string): The Uuid to get the project for
    """
    response = requests.get(baseURL + "/api/projects/" + uuid)
    # project = response.json()
    project = json.loads(response.text)
    project['abstract']['dutchAbstract'] = clean_data(project['abstract']['dutchAbstract'])
    project['abstract']['englishAbstract'] = clean_data(project['abstract']['englishAbstract'])
    print(project)


get_projects_and_clean(2)
# get_project_by_uuid("6fa0f7de-4502-4995-92ae-5467e49df1b3")