
'''
 Entity objects
'''


class Keyword:
    def __init__(self, keyword, locale, uuid):
        self.keyword = keyword
        self.locale = locale
        self.uuid = uuid


class Project:
    def __init__(self, uuid, title_en, title_nl, keywords_en, keywords_nl, abstract_en, abstract_nl):
        self.uuid = uuid
        self.title_en = title_en
        self.title_nl = title_nl
        self.keywords_en = keywords_en
        self.keywords_nl = keywords_nl
        self.abstract_en = abstract_en
        self.abstract_nl = abstract_nl


class Publication:
    def __init__(self, uuid, title_en, title_nl, keywords_en, keywords_nl, abstract_en, abstract_nl, doi):
        self.uuid = uuid
        self.title_en = title_en
        self.title_nl = title_nl
        self.keywords_en = keywords_en
        self.keywords_nl = keywords_nl
        self.abstract_en = abstract_en
        self.abstract_nl = abstract_nl
        self.doi = doi


class KeywordResult:
    def __init__(self, score, value, language):
        self.score = score
        self.value = value
        self.language = language


class ProjectResult:
    def __init__(self, uuid, keywords):
        self.uuid = uuid
        self.keywords = keywords


class PublicationResult:
    def __init__(self, uuid, keywords, doi):
        self.uuid = uuid
        self.keywords = keywords
        self.doi = doi
