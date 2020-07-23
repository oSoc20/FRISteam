import json
from flask import Flask, Response
from Utils.enricher_entities import ProjectResult, PublicationResult, Doi, Keyword
from flask_restful import request
import sys
import os
#3 lines of code tot get the import form other files working
PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
from Utils.fris_entities import Project, Publication
import ServiceManager.service_manager as service_manager
# import service_manager

'''
 Encoding class to encode an object to JSON
'''
class MyEncoder(json.JSONEncoder):
    def default(self, o):
        return o.__dict__


# initialization for the API
app = Flask(__name__)


'''
 test route to check whether the server is alive
'''
@app.route("/")
def hello():
    return {'hello': 'world'}, 200


'''
 POST route to enrich publication data.
 It will build a Publication object from Form-Data sent via the POST request, enrich it and return enriched data as JSON
'''
@app.route("/api/publications/enrich", methods=["POST"])
def enrich_pub_data():
    req = request.get_json(force=True)
    uuid = req['uuid']
    title_en = req['titleEn']
    title_nl = req['titleNl']
    
    keywords_en = []
    for keyword in req['keywordsEn']:
        keywords_en.append(keyword)
    keywords_nl = []
    for keyword in req['keywordsNl']:
        keywords_nl.append(keyword)

    abstract_en = req['abstractEn']
    abstract_nl = req['abstractNl']
    doi = req['doi']

    # TODO:
    publication = Publication(uuid, title_en, title_nl, keywords_en, keywords_nl, abstract_en, abstract_nl, doi)
    #enrich_res = service_manager.process_publication(publication)

    test_res = PublicationResult("1234-5678-9000", Doi("thedoi.com", True, True, "thepdf.com"),
                             [Keyword(1.265, "new Key 1", "en"), Keyword(0.98245, "new Key 2", "en")])

    response = Response(MyEncoder().encode(test_res))
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Content-Type'] = 'application/json'

    return response, 200


'''
 POST route to enrich project data.
 It will build a Project object from Form-Data sent via the POST request, enrich it and return enriched data as JSON
'''
@app.route("/api/projects/enrich", methods=["POST"])
def enrich_proj_data():
    req = request.get_json(force=True)
    uuid = req['uuid']
    title_en = req['titleEn']
    title_nl = req['titleNl']

    keywords_en = []
    for keyword in req['keywordsEn']:
        keywords_en.append(keyword)
    keywords_nl = []
    for keyword in req['keywordsNl']:
        keywords_nl.append(keyword)

    abstract_en = req['abstractEn']
    abstract_nl = req['abstractNl']

    # TODO:
    project = Project(uuid, title_en, title_nl, keywords_en, keywords_nl, abstract_en, abstract_nl)
    #enrich_res = service_manager.process_project(project)

    test_res = ProjectResult("1234-5678-9000", [Keyword(1.265, "new Key 1", "en"), Keyword(0.98245, "new Key 2", "en")])

    response = Response(MyEncoder().encode(test_res))
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Content-Type'] = 'application/json'

    return response, 200


@app.errorhandler(500)
def internal_error(error):
    return f"500 error: {repr(error)}", 500


@app.errorhandler(404)
def not_found(error):
    return f"404 error: {repr(error)}", 404


def run(debug=False, threaded=True):
    app.run(debug=debug, threaded=threaded)


if __name__ == '__main__':
    '''Launch the http server'''
    run(True, False)
