class Keyword:
    def __init__(self, keyword, locale, uuid):
        self.keyword = keyword
        self.locale = locale
        self.uuid = uuid


'''
 Entity objects build after the parameters of the body of a http request.
'''


class Project:
    """Object containing all the project's data.
    :param uuid the project's uuid.
    :param title_en the project's english title.
    :param title_nl the project's dutch title .
    :param keywords_en the project's english keywords.
    :param keywords_nl the project's dutch keywords.
    :param abstract_en the project's english abstract.
    :param abstract_nl the project's dutch abstract."""
    def __init__(self, uuid, title_en, title_nl, keywords_en, keywords_nl, abstract_en, abstract_nl):
        self.uuid = uuid
        self.title_en = title_en
        self.title_nl = title_nl
        self.keywords_en = keywords_en
        self.keywords_nl = keywords_nl
        self.abstract_en = abstract_en
        self.abstract_nl = abstract_nl


class Publication:
    """Object containing all the publication's data.
        :param uuid the publication's uuid.
        :param title_en the publication's english title.
        :param title_nl the publication's dutch title .
        :param keywords_en the publication's english keywords.
        :param keywords_nl the publication's dutch keywords.
        :param abstract_en the publication's english abstract.
        :param abstract_nl the publication's dutch abstract.
        :param doi publication's doi link."""
    def __init__(self, uuid, title_en, title_nl, keywords_en, keywords_nl, abstract_en, abstract_nl, doi):
        self.uuid = uuid
        self.title_en = title_en
        self.title_nl = title_nl
        self.keywords_en = keywords_en
        self.keywords_nl = keywords_nl
        self.abstract_en = abstract_en
        self.abstract_nl = abstract_nl
        self.doi = doi


'''Object that will be used to show the enricher's results.
They follow the general schema:
{
    "Enriching Algorithm": {
        "uuid": "9168910c-f8af-4842-b6d7-04cbb1f79abf",
                "KeywordsList": {
                        "Keyword": {
                                "Score": "1.0005",
                                "Value": "A.I.",
                                "Language": "nl"
        }
    }
}
'''
class KeywordResult:
    """Keyword result object that will show the enricher's results.
    :param score is the score assigned by the enricher to the newly extracted keyword.
    :param value is the newly extracted keyword.
    :param language is the language of the new keyword extracted by the enricher."""
    def __init__(self, score, value, language):
        self.score = score
        self.value = value
        self.language = language


class ProjectResult:
    """Project result object that will show enricher's results.
    :param uuid refers to the project that has been enriched
    :param keywords must be a list of KeywordResult """
    def __init__(self, uuid, keywords=None):
        if keywords is None:
            keywords = []
        self.uuid = uuid
        self.keywords = keywords


class PublicationResult:
    """Publication result object that will show enricher's results.
        :param uuid refers to the project that has been enriched.
        :param keywords must be a list of KeywordResult.
        :param doi is the reference to the doi for the publication."""
    def __init__(self, uuid, keywords=None, doi=None):
        if keywords is None:
            keywords = []
        if doi is None:
            doi = "not available"
        self.uuid = uuid
        self.keywords = keywords
        self.doi = doi
