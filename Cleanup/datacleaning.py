""" Python module to clean data.

The characters that are not supposed to be there
    like '<p>', are removed.
The data is being placed into the right encoding.
"""

import json
import re
import sys
import os

import ftfy # python -m pip install ftfy

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
from Utils.fris_entities import Project, Publication

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

def clean_data(obj):
    """ function clean_data: gets the project 

    Args:
        project (string): the original project data

    Returns:
        string: the fully cleaned project data
    """
    if type(obj) == Project:
        obj.abstract_en = actual_cleaning(obj.abstract_en)
        obj.abstract_nl = actual_cleaning(obj.abstract_nl)
        obj.title_en = actual_cleaning(obj.title_en)
        obj.title_nl = actual_cleaning(obj.title_nl)
    return obj
    
