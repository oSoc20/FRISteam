'''Object that will be used to show the enricher's results for projects and publications.
The schema below follows the FRIS' suggested schema:
{
    "ProjectResult": {
        "uuid": "9168910c-f8af-4842-b6d7-04cbb1f79abf",
                "keywords": {
                        "KeywordResult": {
                                "Score": "1.0005",
                                "Value": "A.I.",
                                "Language": "nl"
                        },
                        "KeywordResult": {
                                "Score": "2.0505",
                                "Value": "Machine Learning",
                                "Language": "nl"
                        }
        }
    }
}
'''
class Keyword:
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
    :param keywords must be a list of KeywordResult
    :param alerts must be a list of string """
    def __init__(self, uuid, keywords=None, alerts=None):
        if keywords is None:
            keywords = []
        if alerts is None:
            alerts = []
        self.uuid = uuid
        self.keywords = keywords
        self.alerts = alerts


class PublicationResult:
    """Publication result object that will show enricher's results.
        :param uuid refers to the project that has been enriched.
        :param keywords must be a list of KeywordResult.
        :param doi is the reference to the doi for the publication.
        :param alerts must be a list of string"""
    def __init__(self, uuid, doi, keywords=None, alerts=None):
        if keywords is None:
            keywords = []
        if alerts is None:
            alerts = []
        self.uuid = uuid
        self.keywords = keywords
        self.doi = doi 
        self.alerts = alerts


class Doi:
    """Doi object that will be used in a PublicationResult Object.
        :param doi is the reference to the doi for the publication.
        :param data_received refers if the Unpaywall API can reach the doi or not.
        :param no_paywall declare if there is a paywall or not in the doi link.
        :param pdf_url refers to a pdf url if there isn't a paywall.
    """
    def __init__(self, doi, data_received, no_paywall, pdf_url):
        self.doi = doi
        self.data_received = data_received
        self.no_paywall = no_paywall
        self.pdf_url = pdf_url




