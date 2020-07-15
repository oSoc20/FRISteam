import json
import re
# D:\Programma\Python\python -m pip install requests
import requests
# D:\Programma\Python\python -m pip install ftfy
import ftfy

baseURL = "https://c2d3eecf4542.ngrok.io"

def cleanhtml(raw_html):
    cleanr = re.compile("<.*?>")
    cleantext = re.sub(cleanr, "", raw_html)
    return cleantext

def removeNbsp(text):
    cleantext = text.replace('\xa0', ' ')
    return cleantext

def cleandata(text):
    text = ftfy.fix_text(text)
    text = cleanhtml(text)
    text = removeNbsp(text)
    return text

def getProjectsJSON(amount):
    response = requests.get(baseURL + "/api/projects/size/" + str(amount))
    projects = json.loads(response.text)
    for project in projects:
        project['abstract']['dutchAbstract'] = cleandata(project['abstract']['dutchAbstract'])
        project['abstract']['englishAbstract'] = cleandata(project['abstract']['englishAbstract'])
        print(project)
        print()

def getProjectJSONByUuid(uuid): 
    response = requests.get(baseURL + "/api/projects/" + uuid)
    # project = response.json()
    project = json.loads(response.text)
    project['abstract']['dutchAbstract'] = cleandata(project['abstract']['dutchAbstract'])
    project['abstract']['englishAbstract'] = cleandata(project['abstract']['englishAbstract'])
    print(project)


# getProjectsJSON(15)
getProjectJSONByUuid("6fa0f7de-4502-4995-92ae-5467e49df1b3")