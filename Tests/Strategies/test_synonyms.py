"""
Test module for the synonyms module
"""
import unittest
import sys
import os 

PACKAGE_PARENT = '../..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
from Strategies.Synonyms.synonyms import get_synonym_by_word , get_synonym_by_word_list

class TestSynonyms(unittest.TestCase):

    def test_get_synonym_by_word_eng(self):
        self.assertEqual(get_synonym_by_word("Bad", 'eng', 2), [['badly', 0.058823529411764705], ['badness', 0.029411764705882353]])

    def test_get_synonym_by_word_nld(self):
        self.assertEqual(get_synonym_by_word("Wetenschap", 'nld', 2), [['kennis', 0.18181818181818182], ['weten', 0.18181818181818182]])

    def test_get_synonym_by_word_list_eng(self):
        self.assertEqual(get_synonym_by_word_list(["Bad", "Science", "Life"], 'eng', 2), [['Bad', 'Science', 'Life'], [[['badly', 0.058823529411764705], ['badness', 0.029411764705882353]], [['scientific_discipline', 0.25], ['skill', 0.25]], [['living', 0.07142857142857142], ['animation', 0.03571428571428571]]]])

    def test_get_synonym_by_word_list_nld(self):
        self.assertEqual(get_synonym_by_word_list(["Slecht", "Leven", "Onderzoek"], 'nld', 2), [['Slecht', 'Leven', 'Onderzoek'], [[['boos', 0.25], ['kwaad', 0.25]], [['voortbestaan', 0.07142857142857142], ['overleven', 0.047619047619047616]], [['inspectie', 0.058823529411764705], ['navraag', 0.058823529411764705]]]])


if __name__ == '__main__':
    unittest.main()
