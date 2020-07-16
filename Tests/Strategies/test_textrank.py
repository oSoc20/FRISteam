"""
Test module for the textrank module
"""
import unittest
import sys
# this still needs to be adapted so we land in the right folder to import the module
from Strategies.TextRank.textrank import TextRank4Keyword, textrank_keywords

class TestTextRank(unittest.TestCase):

    def test_extract_english_keywords(self):
        self.assertEqual(textrank_keywords("In corpus linguistics a key word is a word which occurs in a text more often than we would expect to occur by chance alone. Key words are calculated by carrying out a statistical test (e.g., loglinear or chi-squared) which compares the word frequencies in a text against their expected frequencies derived in a much larger corpus, which acts as a reference for general language use. Keyness is then the quality a word or phrase has of being key in its context.", "en"), 
        {'word': '2.3383907106070563',
 'text': '1.5506211237124696',
 'corpus': '1.5189385170118341',
 'frequencies': '1.138652640806487',
 'reference': '0.9609977742165241',
 'quality': '0.9019527654503615',
 'phrase': '0.9019527654503615',
 'test': '0.7891491685842646',
 'language': '0.7779064725783476',
 'Keyness': '0.7504102975016437',
 'context': '0.7504102975016437',
 'chance': '0.665982412886259'})
    
    def test_extract_dutch_keywords(self):
        self.assertEqual(textrank_keywords("Het Nederlands is een West-Germaanse taal en de moedertaal van de meeste inwoners van Nederland, België en Suriname. In de Europese Unie spreken ongeveer 25 miljoen mensen Nederlands als eerste taal, en een bijkomende acht miljoen als tweede taal. Verder is het Nederlands ook een officiële taal van de Caraïbische (ei)landen Aruba, Curaçao en Sint-Maarten, terwijl de Franse Westhoek en de regio rondom de Duitse stad Kleef van oudsher Nederlandstalige gebieden zijn, waar Nederlandse dialecten mogelijk nog gesproken worden door de oudste generaties. Ook in de voormalige kolonie Indonesië kunnen in sommige gebieden de oudste generaties nog Nederlands spreken. Het aantal sprekers van het Nederlands in de Verenigde Staten, Canada en Australië wordt geschat op ruim een half miljoen. De Kaap-Hollandse dialecten van Zuid-Afrika en Namibië werden gestandaardiseerd tot Afrikaans, een dochtertaal van het Nederlands.", "nl"), 
        {'taal': '2.141210468319559',
 'dialecten': '1.4958114087301588',
 'gebieden': '1.313985615079365',
 'inwoners': '1.222834837006428',
 'Afrika': '1.2163233134920635',
 'Verenigde': '1.1900458333333335',
 'Staten': '1.1900458333333335',
 'Nederland': '1.0849695592286501',
 'Kleef': '1.0793333333333333',
 'Namibië': '1.0694267857142856',
 'Curaçao': '1.067563877410468',
 'moedertaal': '1.0466551652892564'}
 )

    def test_extract_short_english_abstract(self):
        self.assertEqual(textrank_keywords("In corpus linguistics a key word is a word which occurs often.", "en"), 
        {'word': '1.2443749999999998', 
        'corpus': '0.7556249999999999'}
)

    def test_extract_short_dutch_abstract(self):
        self.assertEqual(textrank_keywords("Het Nederlands is een West-Germaanse taal en de moedertaal van de meeste    inwoners van Nederland.", "nl"), 
        {'taal': '1.0814583333333332',
 'moedertaal': '1.0814583333333332',
 'inwoners': '1.0814583333333332',
 'West': '0.8778125',
 'Nederland': '0.8778125'})

    def test_extract_empty_english_abstract(self):
        self.assertEqual(textrank_keywords("", "en"), [{}])

    def test_extract_empty_dutch_abstract(self):
        self.assertEqual(textrank_keywords("", "nl"), [{}])

if __name__ == '__main__':
    unittest.main()