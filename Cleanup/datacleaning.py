""" Python module to clean data.

The characters that are not supposed to be there
    like '<p>', are removed.
The data is being placed into the right encoding.
"""

import json
import re

import ftfy # python -m pip install ftfy


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

def actual_cleaning(text):
    """ function actual_cleaning: Do the actual cleaning of the data.

    Args:
        text (string): the original text
    Returns:
        string: the cleaned text
    """
    text = ftfy.fix_text(text)
    text = clean_html(text)
    text = remove_nbsp(text)
    return text.encode('utf8')

def clean_data(project):
    """ function clean_data: gets the project 

    Args:
        project (string): the original project data

    Returns:
        string: the fully cleaned project data
    """
    
    # for attribute, value in project.items():
    #     print(attribute, "-----", value) 
    #     # if (attribute == "abstract"):
    #     #         print(att, " &&&&& ", val)
    #     print()

    # strings = [project["title"]["englishTitle"], project["title"]["dutchTitle"], project["abstract"]["englishAbstract"], project["abstract"]["dutchAbstract"]]
    # for string in strings:
    #    string = actual_cleaning(string)
    project["title"]["englishTitle"]= actual_cleaning(project["title"]["englishTitle"])
    project["title"]["dutchTitle"] = actual_cleaning(project["title"]["dutchTitle"])
    project["abstract"]["englishAbstract"] = actual_cleaning(project["abstract"]["englishAbstract"])
    project["abstract"]["dutchAbstract"] = actual_cleaning(project["abstract"]["dutchAbstract"])
    print(project)
    return project
    
