import json
from flask import Flask, Response
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
 Encoding function to encode an object to JSON
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
    return {'hello': 'world'}


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
    keywords_en = req['keywordsEn']
    keywords_nl = req['keywordsNl']
    abstract_en = req['abstractEn']
    abstract_nl = req['abstractNl']
    doi = req['doi']
    publication = Publication(uuid, title_en, title_nl, keywords_en, keywords_nl, abstract_en, abstract_nl, doi)

    # TODO:
    enrich_res = service_manager.process_publication(publication)

    response = Response(enrich_res)
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Content-Type'] = 'application/json'

    return response


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
    keywords_en = req['keywordsEn']
    keywords_nl = req['keywordsNl']
    abstract_en = req['abstractEn']
    abstract_nl = req['abstractNl']
    project = Project(uuid, title_en, title_nl, keywords_en, keywords_nl, abstract_en, abstract_nl)

    # TODO:
    enrich_res = service_manager.process_project(project)
    response = Response(enrich_res)
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Content-Type'] = 'application/json'

    return response


@app.errorhandler(500)
def internal_error(error):
    return f"500 error: {error}"


@app.errorhandler(404)
def not_found(error):
    return f"404 error: {error}"


def run(debug=False, threaded=True):
    app.run(debug=debug, threaded=threaded)


if __name__ == '__main__':
    '''Launch the http server'''
    run(True)
