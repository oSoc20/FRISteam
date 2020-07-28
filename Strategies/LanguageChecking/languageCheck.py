import spacy
#python -m pip install spacy-langdetect
from spacy_langdetect import LanguageDetector

nlp = spacy.load('en_core_web_sm')
nlp.add_pipe(LanguageDetector(), name='language_detector', last=True)

def check_if_english(text):
    """ function check_if_english: checks if the input text is in english

    Args:
        text (string): The text which is checked if it is in english

    Returns:
        boolean : returns true if english
    """
    doc = nlp(text)
    if doc._.language["language"] == "en":
       return True
    return False

def check_if_dutch(text):
    """ function check_if_dutch : checks if the input text is in dutch

    Args:
        text (string): The text which is checked if it is in dutch

    Returns:
        boolean : returns true if dutch
    """
    doc = nlp(text)
    if doc._.language["language"] == "nl":
       return True
    return False