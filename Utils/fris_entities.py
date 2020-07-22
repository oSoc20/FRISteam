class Keyword:
    """Entity object used for the keywords.csv file.
    The csv file contains 3 columns with keyword value, language and research output's uuid.
    :param keyword the keyword's value.
    :param locale the keyword's language.
    :param uuid the research output's uuid."""
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



