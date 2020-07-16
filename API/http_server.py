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
    uuid = request.form['uuid']
    title_en = request.form['titleEn']
    title_nl = request.form['titleNl']
    keywords_en = request.form['keywordsEn']
    keywords_nl = request.form['keywordsNl']
    abstract_en = request.form['abstractEn']
    abstract_nl = request.form['abstractNl']
    doi = request.form['doi']
    publication = Publication(uuid, title_en, title_nl, keywords_en, keywords_nl, abstract_en, abstract_nl, doi)

    # TODO:
    #enrich_res = services_manager.enrich(publication)

    response = Response(MyEncoder().encode(publication))
    response.headers['Access-Controll-Allow-Origin'] = '*'
    response.headers['Content-Type'] = 'application/json'

    return response

'''
 POST route to enrich project data.
 It will build a Project object from Form-Data sent via the POST request, enrich it and return enriched data as JSON
'''
@app.route("/api/projects/enrich", methods=["POST"])
def enrich_proj_data():
    uuid = request.form['uuid']
    title_en = request.form['titleEn']
    title_nl = request.form['titleNl']
    keywords_en = request.form['keywordsEn']
    keywords_nl = request.form['keywordsNl']
    abstract_en = request.form['abstractEn']
    abstract_nl = request.form['abstractNl']
    project = Project(uuid, title_en, title_nl, keywords_en, keywords_nl, abstract_en, abstract_nl)

    # TODO:
    #enrich_res = services_manager.enrich(project)

    response = Response(MyEncoder().encode(project))
    response.headers['Access-Controll-Allow-Origin'] = '*'
    response.headers['Content-Type'] = 'application/json'

    return response


'''
 It will run the server in localhost:5000
'''
if __name__ == '__main__':
    app.run(debug=True)
