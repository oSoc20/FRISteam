# -*- coding: utf-8 -*-

import sys
import os

#3 lines of code tot get the import form other files working
PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))




def enrich_publication(publication_object):

def enrich_project(project_object):



if __name__ == "__main__":
    #print("ok")
    #json_file = get_publication_with_uid("8e60ac99-8687-4425-8e68-d42a11d4362f")
    #print("cool")
    publi_list = get_publications_list(500)

    publi_doi_list = get_publications_with_doi(publi_list)

    print(publi_doi_list)

