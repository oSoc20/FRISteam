""" Test module for the datacleaing module

"""

import unittest
import os 
import sys

PACKAGE_PARENT = '../..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from Cleanup.datacleaning import clean_data
from Tests.test_helper import get_test_project

class TestCleanup(unittest.TestCase):
    def validate_clean_data(self, tag):
        cleaned_proj = clean_data(get_test_project())
        return (tag in cleaned_proj.title_en) and (tag in cleaned_proj.title_nl) and (tag in cleaned_proj.abstract_en) and (tag in cleaned_proj.abstract_nl)

    def test_get_projects_nohtmltag(self):
        self.assertFalse(self.validate_clean_data("<p>"))

    def test_get_projects_no_nbsp(self):
        self.assertFalse(self.validate_clean_data("\xa0"))

if __name__ == '__main__':
    unittest.main()