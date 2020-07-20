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
        {'word': 1.0041177897330824,
 'corpus': 0.7177726760478924,
 'text': 0.6407500605156563,
 'frequencies': 0.5410010023268136,
 'reference': 0.45590115909699,
 'quality': 0.42779885773982623,
 'phrase': 0.42779885773982623,
 'test': 0.3809348095177171,
 'language': 0.370344367877619,
 'Keyness': 0.35791269463258,
 'context': 0.35791269463258,
 'words': 0.3177550301394162})
    
    def test_extract_dutch_keywords(self):
        self.assertEqual(textrank_keywords("Het Nederlands is een West-Germaanse taal en de moedertaal van de meeste inwoners van Nederland, België en Suriname. In de Europese Unie spreken ongeveer 25 miljoen mensen Nederlands als eerste taal, en een bijkomende acht miljoen als tweede taal. Verder is het Nederlands ook een officiële taal van de Caraïbische (ei)landen Aruba, Curaçao en Sint-Maarten, terwijl de Franse Westhoek en de regio rondom de Duitse stad Kleef van oudsher Nederlandstalige gebieden zijn, waar Nederlandse dialecten mogelijk nog gesproken worden door de oudste generaties. Ook in de voormalige kolonie Indonesië kunnen in sommige gebieden de oudste generaties nog Nederlands spreken. Het aantal sprekers van het Nederlands in de Verenigde Staten, Canada en Australië wordt geschat op ruim een half miljoen. De Kaap-Hollandse dialecten van Zuid-Afrika en Namibië werden gestandaardiseerd tot Afrikaans, een dochtertaal van het Nederlands.", "nl"), 
        {'taal': 1.0759753547121376,
 'dialecten': 0.6542022237511517,
 'gebieden': 0.5353777024908467,
 'inwoners': 0.4758099846794649,
 'Afrika': 0.4715546551756896,
 'Verenigde': 0.45438212460620947,
 'Staten': 0.45438212460620947,
 'Nederland': 0.38571399058840944,
 'Kleef': 0.3820306746502307,
 'Namibië': 0.37555667140492377,
 'Curaçao': 0.37433924684205844,
 'moedertaal': 0.3606752464926687}
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
 'West': 0.2809109769979336,
 'Nederland': 0.2809109769979336})

    def test_extract_empty_english_abstract(self):
        self.assertEqual(textrank_keywords("", "en"), 
        {})

    def test_extract_empty_dutch_abstract(self):
        self.assertEqual(textrank_keywords("", "nl"), 
        {})

if __name__ == '__main__':
    unittest.main()