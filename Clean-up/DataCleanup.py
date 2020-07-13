import pandas as pd
import re
# D:\Programma\Python\python -m pip install requests
import requests
# get request with parameters example: 
# parameters={"something": 0}
# response = requests.get("url", params=parameters)
import json

data = {}

def cleanhtml(raw_html):
    #replact &lt;p&gt; to <p> so html-tags can be removed
    raw_html = raw_html.replace('&lt;','<')
    raw_html = raw_html.replace('&gt;','>')
    cleanr = re.compile("<.*?>")
    cleantext = re.sub(cleanr, "", raw_html)
    return cleantext

def cleanASCII(raw_html):
    raw_html = raw_html.replace("&#39;","'")
    cleanr = re.compile("&#.*;")
    cleantext = re.sub(cleanr, "", raw_html)
    return cleantext

def replaceSomeCharacters(raw_html):
    raw_html = raw_html.replace('Â', '')
    raw_html = raw_html.replace('â€™', "'")
    raw_html = raw_html.replace('â€œ', "'")
    raw_html = raw_html.replace('&amp;#39;', "'")
    return raw_html

def cleandata(text):
    text = cleanhtml(text)
    text= cleanASCII(text)
    text = replaceSomeCharacters(text)
    return text


def getProjects(amount):
    response = requests.get("https://4234f99e6d2a.ngrok.io/api/projects/size/" + str(amount))
    projects = json.loads(response.text)
    for project in projects:
        print(project['abstract']['englishAbstract'])
        print()
   
    # result:
    # [{'id': '6fa0f7de-4502-4995-92ae-5467e49df1b3', 'englishKeywords': ['Ion channels', 'Positive allosteric modulators', 'Crystallography'], 'dutchKeywords': [], 'dataProvider': {'id': '54937891', 'name': 'KULeuven'}, 'doi': None, 'title': {'englishTitle': 'Structure-based discovery of positive allosteric modulators of the alpha7 nicotinic ecetylcholine receptor as cognition enhancers.', 'dutchTitle': 'Structuur-gebaseerde ontwikkeling van positieve allostere modulatoren van de alpha7 nicotine acetylcholine receptor met klinische toepassing als cognitie verbeteraars.'}, 'empty': False, 'abstract': {'id': 148096734, 'englishAbstract': '&lt;p&gt;Nicotinic acetylcholine receptors (nAChRs) areÂ\xa0relevant therapeutic targets for diseases of the brain. The most promising target for 
    # disorders associated with cognitive dysfunction is the alpha7 subtype. The scientific goal is to develop novel molecules targeting the Î±7 nicotinic acetylcholine receptor and that improve cognition in schizophrenia and Alzheimerâ€™s disease, both of which are disordersÂ\xa0for which there remains an unmet medical need. The main goal is to obtain a patent for the novel compounds and to negotiate a license with a pharmaceutical company. A 3-dimensional structure of the alpha7 subtype of nAChR is notÂ\xa0yet available, but detailed insight of protein structures at atomic level yields invaluable information about protein function and can facilitate theÂ\xa0discovery and development of new drugs. A marine snail protein (calledÂ\xa0acetylcholine binding protein) has been engineered to mimic the human alpha7 nAChR and offers a realistic template for structure-based drug design. The goal of this project is the development of novel high affinity lead compounds with activity as positive allosteric modulators for alpha7 nAChR. These compounds will have potential application as cognition enhancers in schizophrenia and Alheimer&amp;#39;sÂ\xa0disease.&lt;/p&gt;', 'dutchAbstract': '&lt;p&gt;Nicotine-acetylcholinereceptoren (nAChR&amp;#39;s)Â\xa0zijn relevante therapeutische doelen voor hersenziekten.Â\xa0Het meest veelbelovende doelwit voor aandoeningenÂ\xa0geassocieerd met cognitieve dysfunctie is het alpha7-subtype. Het wetenschappelijkeÂ\xa0doel is om nieuwe moleculen te ontwikkelen die zich richten op deÂ\xa0Î±7 nicotinische acetylcholinereceptor en die de cognitie verbeteren bijÂ\xa0schizofrenie en de ziekte van Alzheimer, die beideÂ\xa0stoornissen zijn waarvoor nog steeds een onvervulde medische behoefte bestaat. Het belangrijkste doel is om een patent te verkrijgen voor de nieuweÂ\xa0verbindingen en om een licentie te bedingen bijÂ\xa0een farmaceutisch bedrijf.Â\xa0Een driedimensionale structuur van het alpha7-subtype van nahr is nog niet beschikbaar, maar gedetailleerd inzicht van eiwitstructuren op atomair niveau levert onschatbare informatie over de eiwitfunctie op en kan deÂ\xa0ontdekking en ontwikkeling van nieuwe geneesmiddelen vergemakkelijken. Een marine slak-eiwit (acetylcholine-bindend eiwit genaamd) isÂ\xa0ontwikkeldÂ\xa0om de menselijke alfa7 nAChR na te bootsen en biedt een realistische sjabloon voor op structuur gebaseerd geneesmiddelenontwerp. Het doelÂ\xa0van ditÂ\xa0project is de ontwikkeling van nieuwe verbindingen met een hoge affiniteit met activiteit als positieve allosterische modulators voor alpha7 nAChR. Deze verbindingen zullen mogelijk worden toegepastÂ\xa0als cognitie-versterkers bij schizofrenie en de ziekte van Alzheimer.&lt;/p&gt;'}}]

def  GetProjectByUuid(uuid): 
    response = requests.get("https://4234f99e6d2a.ngrok.io/api/projects/" + uuid)
    project = response.json()
    print(project['abstract']['englishAbstract'])

    # result:
    # {'id': '6fa0f7de-4502-4995-92ae-5467e49df1b3', 'englishKeywords': ['Ion channels', 'Positive allosteric modulators', 'Crystallography'], 'dutchKeywords': [], 'dataProvider': {'id': '54937891', 'name': 'KULeuven'}, 'doi': None, 'title': {'englishTitle': 'Structure-based discovery of positive allosteric modulators of the alpha7 nicotinic ecetylcholine receptor as cognition enhancers.', 'dutchTitle': 'Structuur-gebaseerde ontwikkeling van positieve allostere modulatoren van de alpha7 nicotine acetylcholine receptor met klinische toepassing als cognitie verbeteraars.'}, 'empty': False, 'abstract': {'id': 148096734, 'englishAbstract': '&lt;p&gt;Nicotinic acetylcholine receptors (nAChRs) areÂ\xa0relevant therapeutic targets for diseases of the brain. The most promising target for disorders associated with cognitive dysfunction is the alpha7 subtype. The scientific goal is to develop novel molecules targeting the Î±7 nicotinic acetylcholine receptor and that improve cognition in schizophrenia and Alzheimerâ€™s disease, both of which are disordersÂ\xa0for which there remains an unmet medical need. The main goal is to obtain a patent for the novel compounds and to negotiate a license with a pharmaceutical company. A 3-dimensional structure of the alpha7 subtype of nAChR is notÂ\xa0yet available, but detailed insight of protein structures at atomic level yields invaluable information about protein function and can facilitate theÂ\xa0discovery and development of new drugs. A marine snail protein (calledÂ\xa0acetylcholine binding protein) has been engineered to mimic the human alpha7 nAChR and offers a realistic template for structure-based drug design. The goal of this project is the development of novel high affinity lead compounds with activity as positive allosteric modulators for alpha7 nAChR. These compounds 
    # will have potential application as cognition enhancers in schizophrenia and Alheimer&amp;#39;sÂ\xa0disease.&lt;/p&gt;', 'dutchAbstract': '&lt;p&gt;Nicotine-acetylcholinereceptoren (nAChR&amp;#39;s)Â\xa0zijn relevante therapeutische doelen voor hersenziekten.Â\xa0Het meest veelbelovende doelwit voor aandoeningenÂ\xa0geassocieerd met cognitieve dysfunctie is het alpha7-subtype. Het wetenschappelijkeÂ\xa0doel is om nieuwe moleculen te ontwikkelen die zich richten op deÂ\xa0Î±7 nicotinische acetylcholinereceptor en die de 
    # cognitie verbeteren bijÂ\xa0schizofrenie en de ziekte van Alzheimer, die beideÂ\xa0stoornissen zijn waarvoor nog steeds een onvervulde medische behoefte bestaat. Het belangrijkste doel is om een patent te verkrijgen voor de nieuweÂ\xa0verbindingen en om een licentie te bedingen bijÂ\xa0een farmaceutisch bedrijf.Â\xa0Een driedimensionale structuur van het alpha7-subtype van nahr is nog niet beschikbaar, maar gedetailleerd inzicht van eiwitstructuren op atomair niveau levert onschatbare informatie over de eiwitfunctie op en kan deÂ\xa0ontdekking en ontwikkeling van nieuwe geneesmiddelen vergemakkelijken. Een marine slak-eiwit (acetylcholine-bindend eiwit genaamd) isÂ\xa0ontwikkeldÂ\xa0om de menselijke alfa7 nAChR na te bootsen en biedt een realistische sjabloon voor op structuur gebaseerd geneesmiddelenontwerp. Het doelÂ\xa0van ditÂ\xa0project is de ontwikkeling van nieuwe verbindingen met een hoge affiniteit met activiteit als positieve allosterische modulators voor alpha7 nAChR. Deze verbindingen zullen mogelijk worden toegepastÂ\xa0als cognitie-versterkers bij schizofrenie en de ziekte van Alzheimer.&lt;/p&gt;'}}


getProjects(2)
# GetProjectByUuid("6fa0f7de-4502-4995-92ae-5467e49df1b3")