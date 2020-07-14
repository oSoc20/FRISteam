"""
Test module for the synonyms module
"""
import unittest
import sys
from Strategies.Synonyms.synonyms import get_synonym_by_word , get_synonym_by_word_list

class TestSynonyms(unittest.TestCase):

    def test_get_synonym_by_word_eng(self):
        self.assertEqual(get_synonym_by_word("Bad", 'eng', 2), [['badly', 2], ['badness', 1]])

    def test_get_synonym_by_word_nld(self):
        self.assertEqual(get_synonym_by_word("Wetenschap", 'nld', 2), [['kennis', 2], ['weten', 2]])

    def test_get_synonym_by_word_list_eng(self):
        self.assertEqual(get_synonym_by_word_list(["Bad", "Science", "Life"], 'eng', 2), [['Bad', 'Science', 'Life'], [[['badly', 2], ['badness', 1]], [['scientific_discipline', 1], ['skill', 1]], [['living', 2], ['animation', 1]]]])

    def test_get_synonym_by_word_list_nld(self):
        self.assertEqual(get_synonym_by_word_list(["Slecht", "Leven", "Onderzoek"], 'nld', 2), [['Slecht', 'Leven', 'Onderzoek'], [[['boos', 1], ['kwaad', 1]], [['voortbestaan', 3], ['overleven', 2]], [['inspectie', 2], ['navraag', 2]]]])


if __name__ == '__main__':
    unittest.main()
