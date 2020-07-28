import sys
import os
#3 lines of code tot get the import form other files working
PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from Cleanup.datacleaning import clean_data
import Enricher.enricher as enricher

def process_project(project_obj):
    """This function sends a project object through data cleaning and passes the cleaned object to the enricher

    Args:
        project_obj (Utils.fris_entities.Project): Instance of Project class 

    Returns:
        Utils.enricher_entities.ProjectResult: Instance of ProjectResult containing enriched data
    """
    cleaned_project = clean_data(project_obj)
    print("Service Manager: successful process_project")
    enriched_proj = enricher.enrich_project(cleaned_project)
    return enriched_proj


def process_publication(publication_obj):
    """This function sends a publication object through data cleaning and passes the cleaned object to the enricher

    Args:
        publication_obj (Utils.fris_entities.Publication): Instance of Publication class 

    Returns:
        Utils.enricher_entities.PublicationResult: Instance of PublicationResult containing enriched data
    """
    cleaned_pub = clean_data(publication_obj)
    print("Service Manager: successful process_publication")
    enriched_pub = enricher.enrich_publication(cleaned_pub)
    return enriched_pub

