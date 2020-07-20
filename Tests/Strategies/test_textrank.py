"""
Test module for the textrank module
"""
import unittest
import sys
import os
# this still needs to be adapted so we land in the right folder to import the module
PACKAGE_PARENT = '../..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
from Strategies.TextRank.textrank import TextRank4Keyword, textrank_keywords

class TestTextRank(unittest.TestCase):

    def test_extract_english_keywords(self):
        self.assertEqual(textrank_keywords("In corpus linguistics a key word is a word which occurs in a text more often than we would expect to occur by chance alone. Key words are calculated by carrying out a statistical test (e.g., loglinear or chi-squared) which compares the word frequencies in a text against their expected frequencies derived in a much larger corpus, which acts as a reference for general language use. Keyness is then the quality a word or phrase has of being key in its context.", "en"), 
        {'word': 1.0436556785898956, 
        'corpus': 0.6600867392869518, 
        'text': 0.6092570533806281, 
        'chi': 0.5067072852808676, 
        'frequencies': 0.5011478297946753, 
        'loglinear': 0.4432616308403234, 
        'reference': 0.41598315561146876, 
        'quality': 0.3946067380660485, 
        'phrase': 0.3946067380660485, 
        'test': 0.3669232598178098, 
        'language': 0.33884610225150225, 
        'Keyness': 0.32491778901378054})
    
    def test_extract_dutch_keywords(self):
        self.assertEqual(textrank_keywords("Het Nederlands is een West-Germaanse taal en de moedertaal van de meeste inwoners van Nederland, België en Suriname. In de Europese Unie spreken ongeveer 25 miljoen mensen Nederlands als eerste taal, en een bijkomende acht miljoen als tweede taal. Verder is het Nederlands ook een officiële taal van de Caraïbische (ei)landen Aruba, Curaçao en Sint-Maarten, terwijl de Franse Westhoek en de regio rondom de Duitse stad Kleef van oudsher Nederlandstalige gebieden zijn, waar Nederlandse dialecten mogelijk nog gesproken worden door de oudste generaties. Ook in de voormalige kolonie Indonesië kunnen in sommige gebieden de oudste generaties nog Nederlands spreken. Het aantal sprekers van het Nederlands in de Verenigde Staten, Canada en Australië wordt geschat op ruim een half miljoen. De Kaap-Hollandse dialecten van Zuid-Afrika en Namibië werden gestandaardiseerd tot Afrikaans, een dochtertaal van het Nederlands.", "nl"), 
        {'Nederlands': 1.0969950551821996, 
        'taal': 0.612849107835524, 
        'miljoen': 0.5569733172729824, 
        'Westhoek': 0.44584171507941844, 
        'inwoners': 0.4330848565473977, 
        'Sint-Maarten': 0.42949325332576466, 
        'Staten': 0.4080326822818925, 
        'Curaçao': 0.40779504454844684, 
        'Verenigde': 0.40673074628493633, 
        'gebieden': 0.4022837328462512, 
        'generaties': 0.4022837328462512, 
        'regio': 0.3976367559489353}
        )
 )

    def test_extract_short_english_abstract(self):
        self.assertEqual(textrank_keywords("In corpus linguistics a key word is a word which occurs often.", "en"), 
        {'word': 0.6414213562373094, 'corpus': 0.35857864376269055}
        )

    def test_extract_short_dutch_abstract(self):
        self.assertEqual(textrank_keywords("Het Nederlands is een West-Germaanse taal en de moedertaal van de meeste inwoners van Nederland.", "nl"), 
        {'taal': 0.6460593486680444, 
        'moedertaal': 0.6460593486680444, 
        'inwoners': 0.6460593486680444, 
        'Nederlands': 0.2809109769979336, 
        'Nederland': 0.2809109769979336}
        )

    def test_extract_empty_english_abstract(self):
        self.assertEqual(textrank_keywords("", "en"), 
        {})

    def test_extract_empty_dutch_abstract(self):
        self.assertEqual(textrank_keywords("", "nl"), 
        {})

if __name__ == '__main__':
    unittest.main()