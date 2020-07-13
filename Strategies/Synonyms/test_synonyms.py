import unittest
import sys
from synonyms import get_synonym_by_word , get_synonym_by_word_list

class TestSynonyms(unittest.TestCase):

    def test_get_synonym_by_word_eng(self):
        self.assertEqual(get_synonym_by_word("Bad", 'eng', 2), ['badness', 'big'])

    def test_get_synonym_by_word_nld(self):
        self.assertEqual(get_synonym_by_word("Wetenschap", 'nld', 2), ['medeweten', 'perceptie'])

    def test_get_synonym_by_word_list_eng(self):
        self.assertEqual(get_synonym_by_word_list(["Bad", "Science", "Life"], 'eng', 2), [['Bad', 'Science', 'Life'], [['badness', 'big'], ['scientific_discipline', 'skill'], ['living', 'animation']]])

    def test_get_synonym_by_word_list_nld(self):
        self.assertEqual(get_synonym_by_word_list(["Slecht", "Leven", "Onderzoek"], 'nld', 2), [['Slecht', 'Leven', 'Onderzoek'], [['boos', 'kwaad'], ['levensduur', 'levenslang'], ['inspectie', 'monstering']]])


if __name__ == '__main__':
    unittest.main()
