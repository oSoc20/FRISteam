import pandas as pd
import re
# D:\Programma\Python\python -m pip install requests
import requests

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


def getRequestData():
    # parameters={"something": 0}
    # response = requests.get("https://0c13cea8df9b.ngrok.io/api/projects/1", params=parameters)
    response = requests.get("https://0c13cea8df9b.ngrok.io/api/projects/1")
    data = response.json()
    print(data)


def getJSONData():
    df = pd.read_json("soapdata.json",orient='str')
    # print(df['abstract']["englishAbstract"])


# getJSONData()
getRequestData()