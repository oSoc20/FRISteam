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
from Strategies.UnpaywallCheck.doiPaywall import import_doi_data, extract_doi, get_api_information

csv_file = "../Strategies/UnpaywallCheck/dois.csv"
directory_to_store_json = "../Strategies/UnpaywallCheck/DOIS"

dois_csv = import_doi_data(csv_file)
serie = dois_csv["doi"]

class TestDoiPaywall(unittest.TestCase):

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