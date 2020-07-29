import json
from flask import Flask, Response, render_template

from flask_restful import request
from flask_cors import CORS
import sys
import os
#3 lines of code tot get the import form other files working
PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

'''
 template folder needed to serve the documentation's html file. 
'''
template_dir = os.path.join(SCRIPT_DIR, '..')
template_dir = os.path.join(template_dir, 'docs')
template_dir = os.path.join(template_dir, '_build')
template_dir = os.path.join(template_dir, 'html')

print("Starting Server (This can take a few minutes)")

from Utils.fris_entities import Project, Publication
import ServiceManager.service_manager as service_manager
# import service_manager

'''
 Encoding class to encode an object to JSON
'''
class MyEncoder(json.JSONEncoder):
    def default(self, o): # pylint: disable=E0202
        return o.__dict__


# initialization for the API
app = Flask(__name__, template_folder=template_dir)
CORS(app)


"""
 /
 Will show a welcome message to the api.
"""
@app.route("/")
def send_root():
    return "Welcome to FRIS-Enricher API."


"""
 /documentation
 It will render the html page with all the documentation for the backend
"""
@app.route("/documentation")
def serve_doc_html():
    return render_template("index.html")

"""
 /ping
 GET route to check whether the server is alive
"""
@app.route("/ping", methods=["GET"])
def send_ping():
    return Response(None, 200)


"""
 /api/publications/enrich
 POST route to enrich publication data.
 It will build a Publication object from Form-Data sent via the POST request, enrich it and return enriched data as JSON
"""
@app.route("/api/publications/enrich", methods=["POST"])
def enrich_pub_data():
    req = request.get_json(force=True)
    try:
        publication = extract_publication_from_request(req)
        enrich_res = service_manager.process_publication(publication)

        response = Response(MyEncoder().encode(enrich_res), 200)
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Content-Type'] = 'application/json'

        return response
    except Exception as e:
        return Response(f"Invalid data or missing values. {e.args}", 400)


def extract_publication_from_request(req):
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
    publication = Publication(uuid, title_en, title_nl, keywords_en, keywords_nl, abstract_en, abstract_nl, doi)
    return publication


"""
 /api/projects/enrich
 POST route to enrich project data.
 It will build a Project object from Form-Data sent via the POST request, enrich it and return enriched data as JSON
"""
@app.route("/api/projects/enrich", methods=["POST"])
def enrich_proj_data():
    req = request.get_json(force=True)
    try:
        project = extract_project_from_request(req)
        enrich_res = service_manager.process_project(project)

        response = Response(MyEncoder().encode(enrich_res), 200)
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Content-Type'] = 'application/json'

        return response
    except Exception as e:
        return Response(f"Invalid data or missing values. {e.args}", 400)


def extract_project_from_request(req):
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
    project = Project(uuid, title_en, title_nl, keywords_en, keywords_nl, abstract_en, abstract_nl)
    return project


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
    run(False, True)
