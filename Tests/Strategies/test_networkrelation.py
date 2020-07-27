"""
Test module for the networkrelation module
"""
import unittest
import sys
import os

PACKAGE_PARENT = '../..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
from Strategies.NetworkRelation.networkrelation import preprocess_abstract, calculate_term_frequency, calculate_relations

class TestNetworkRelation(unittest.TestCase):

    def test_compare_english(self):
        self.assertEqual(calculate_relations("An abstract is a brief summary of a research article, thesis, review, conference proceeding, or any in-depth analysis of a particular subject and is often used to help the reader quickly ascertain the paper's purpose.[1] When used, an abstract always appears at the beginning of a manuscript or typescript, acting as the point-of-entry for any given academic paper or patent application. Abstracting and indexing services for various academic disciplines are aimed at compiling a body of literature for that particular subject. The terms précis or synopsis are used in some publications to refer to the same thing that other publications might call an abstract. In management reports, an executive summary usually contains more information (and often more sensitive information) than the abstract does.", "en"), {'abstract': 0.06462797959989969, 'use': 0.04856605768242016, 'information': 0.032917982865214655, 'publication': 0.032358730027006496, 'subject': 0.032313989799949844, 'paper': 0.03228043462965736, 'academic': 0.03228043462965736, 'summary': 0.03225806451612903, 'particular': 0.03225806451612903, 'management': 0.026195583345811284, 'research': 0.01777323560239649, 'review': 0.017538349410349062, 'literature': 0.01683369083420679, 'conference': 0.01664354486921602, 'patent': 0.016464583960989407, 'service': 0.016431028790696918, 'analysis': 0.01640865867716859, 'article': 0.016341548336583613, 'report': 0.01631917822305529, 'act': 0.016307993166291126, 'application': 0.016240882825706147, 'thesis': 0.01621851271217782, 'body': 0.016207327655413658, 'discipline': 0.01617377248512117, 'indexing': 0.016162587428357005, 'term': 0.016162587428357005, 'proceeding': 0.01614021731482868, 'refer': 0.01614021731482868, 'thing': 0.01614021731482868, 'brief': 0.016129032258064516, 'indepth': 0.016129032258064516, 'help': 0.016129032258064516, 'reader': 0.016129032258064516, 'quickly': 0.016129032258064516, 'ascertain': 0.016129032258064516, 'purpose1': 0.016129032258064516, 'appear': 0.016129032258064516, 'beginning': 0.016129032258064516, 'manuscript': 0.016129032258064516, 'typescript': 0.016129032258064516, 'pointofentry': 0.016129032258064516, 'abstracting': 0.016129032258064516, 'aim': 0.016129032258064516, 'compile': 0.016129032258064516, 'précis': 0.016129032258064516, 'synopsis': 0.016129032258064516, 'executive': 0.016129032258064516, 'usually': 0.016129032258064516, 'contain': 0.016129032258064516, 'sensitive': 0.016129032258064516})

    def test_compare_dutch(self):
        self.assertEqual(calculate_relations("Een alinea is het tekstgedeelte tussen twee inspringingen of tussen twee regels wit, de kleinste eenheid van een tekst die nog uit meerdere zinnen bestaat. De alinea is volgens schrijfadviseur Jan Renkema de belangrijkste bouwsteen van een tekst.[1] Incidenteel kan een alinea ook uit een enkele zin of zelfs uit een woord bestaan, maar alleen ter afwisseling met langere alinea's, bijvoorbeeld om het aanzien van een tekst gevarieerder te maken.", "nl"), {'alinea': 0.12903225806451613, 'twee': 0.06451612903225806, 'tekst': 0.06451612903225806, 'zin': 0.06451612903225806, 'bestaan': 0.06451612903225806, 'tekstgedeelte': 0.03225806451612903, 'inspringing': 0.03225806451612903, 'regel': 0.03225806451612903, 'wit': 0.03225806451612903, 'klein': 0.03225806451612903, 'eenheid': 0.03225806451612903, 'meerdere': 0.03225806451612903, 'schrijfadviseur': 0.03225806451612903, 'jan': 0.03225806451612903, 'renkema': 0.03225806451612903, 'belangrijk': 0.03225806451612903, 'bouwsteen': 0.03225806451612903, 'tekst1': 0.03225806451612903, 'incidenteel': 0.03225806451612903, 'woord': 0.03225806451612903, 'afwisseling': 0.03225806451612903, 'aanzien': 0.03225806451612903, 'gevarieerd': 0.03225806451612903, 'maken': 0.03225806451612903})

    def test_compare_empty_abstract_en(self):
        self.assertEqual(calculate_relations("", "en"), {})

    def test_compare_empty_abstract_nl(self):
        self.assertEqual(calculate_relations("", "nl"), {})
    
if __name__ == '__main__':
    unittest.main()