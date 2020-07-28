"""
Test module for the doi paywall module
"""
import unittest
import pandas as pd
import os 
import sys

PACKAGE_PARENT = '../..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from Strategies.UnpaywallCheck.doiPaywall import extract_doi_from_url, add_doi_object, add_pdf_information_of_doi, get_unpaywall_api_data



publication_doi_url = "https://doi.org/10.1016/j.yebeh.2018.09.011"

class TestDoiPaywall(unittest.TestCase):

    def test_add_doi_object(self):
        
        doi_obj = Doi("https://doi.org/10.1016/j.yebeh.2018.09.011",True,False,"No pdf")
        self.assertTrue(csv_file, str)
        self.assertEqual(type(add_doi_object(publication_doi)), type(doi_obj))

    def test_extract_doi_from_url(self):
        self.assertRegex(publication_doi,'^https:\/\/doi.org\/([a-zA-Z0-9_.\/])*$')
        self.assertRegex(extract_doi_from_url(publication_doi),'^([a-zA-Z0-9_.\/])*$')
        

    #def test_add_pdf_information_of_doi(self):
        

    def test_get_unpaywall_api_data(self):

        doi = extract_doi_from_url(publication_doi_url)
        self.assertRegex(doi,'^([a-zA-Z0-9_.\/])*$')
        self.assertEqual(type(get_unpaywall_api_data(doi)), str)



if __name__ == '__main__':
    unittest.main()