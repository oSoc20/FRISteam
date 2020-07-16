""" Test module for the datacleaing module

"""

import unittest
import os 
import sys

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from Cleanup.datacleaning import clean_data
from Runner.fetching import get_project_by_uuid

class TestCleanup(unittest.TestCase):

    def test_get_projects_nohtmltag(self):
        self.assertFalse("<p>" in clean_data(get_project_by_uuid("6fa0f7de-4502-4995-92ae-5467e49df1b3")))

    def test_get_projects_no_nbsp(self):
        self.assertFalse("\xa0" in clean_data(get_project_by_uuid("6fa0f7de-4502-4995-92ae-5467e49df1b3")))

if __name__ == '__main__':
    unittest.main()