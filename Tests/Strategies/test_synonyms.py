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
from collections import Counter

class TestSynonyms(unittest.TestCase):

    def test_get_synonym_by_word_eng(self):
        self.assertEqual(get_synonym_by_word("Bad", 'eng'), Counter({'badly': 2, 'badness': 1, 'big': 1, 'tough': 1, 'spoiled': 1, 'spoilt': 1, 'regretful': 1, 'sorry': 1, 'uncollectible': 1, 'risky': 1, 'high-risk': 1, 'speculative': 1, 'unfit': 1, 'unsound': 1, 'forged': 1, 'defective': 1}))

    def test_get_synonym_by_word_nld(self):
        self.assertEqual(get_synonym_by_word("Wetenschap", 'nld'), Counter({'kennis': 2, 'weten': 2, 'medeweten': 1, 'perceptie': 1, 'cognitie': 1, 'bagage': 1, 'ervaring': 1}))

    def test_get_synonym_by_word_list_eng(self):
        self.assertEqual(get_synonym_by_word_list(["Bad", "Science", "Life"], 'eng', 2), Counter({'badness': 0.030303030303030304, 'big': 0.030303030303030304}))

    def test_get_synonym_by_word_list_nld(self):
        self.assertEqual(get_synonym_by_word_list(["Slecht", "Leven", "Onderzoek"], 'nld', 2), Counter({'boos': 0.015625, 'kwaad': 0.015625}))


if __name__ == '__main__':
    unittest.main()
