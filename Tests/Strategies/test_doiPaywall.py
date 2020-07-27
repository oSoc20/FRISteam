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

from Strategies.UnpaywallCheck.doiPaywall import import_doi_data, extract_doi, get_api_information, add_doi_object, extract_doi_from_url

csv_file = "./Strategies/UnpaywallCheck/dois.csv"
directory_to_store_json = "./Strategies/UnpaywallCheck/DOIS"

dois_csv = import_doi_data(csv_file)
serie = dois_csv["doi"]

publication_doi = "https://doi.org/10.1016/j.yebeh.2018.09.011"

class TestDoiPaywall(unittest.TestCase):

    def test_add_doi_object(self):
        
        doi_obj = Doi("https://doi.org/10.1016/j.yebeh.2018.09.011",True,False,"No pdf")
        self.assertTrue(csv_file, str)
        self.assertEqual(type(add_doi_object(publication_doi)), type(doi_obj))

    def test_extract_doi_from_url(self):
        self.assertRegex(publication_doi,'^https:\/\/doi.org\/([a-zA-Z0-9_.\/])*$')
        self.assertRegex(extract_doi_from_url(publication_doi),'^([a-zA-Z0-9_.\/])*$')
        

    def test_import_doi_data(self):
        
        df = pd.DataFrame()
        self.assertTrue(csv_file, str)
        self.assertEqual(type(import_doi_data(csv_file)), type(df))

    def test_extract_doi(self):
        df = []
        self.assertEqual(type(extract_doi(serie)), type(df))

    def test_get_api_information(self):
        dois_list = extract_doi(serie)
        li = []
        self.assertEqual(type(directory_to_store_json),str)
        self.assertEqual(type(dois_list),type(li))


if __name__ == '__main__':
    unittest.main()