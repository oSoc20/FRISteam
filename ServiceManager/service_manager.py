import sys
import os
#3 lines of code tot get the import form other files working
PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

import Enricher.enricher as enricher

def process_project(project_obj):
    enriched_proj = enricher.enrich_project(project_obj)
    return enriched_proj


def process_publication(publication_obj):
    enriched_pub = enricher.enrich_publication(publication_obj)
    return enriched_pub
