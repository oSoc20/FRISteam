""" Test module for the datacleaing module

"""

import unittest
from Cleanup.datacleaning import get_projects_and_clean, get_project_by_uuid_and_clean
from Runner.fetching import get_project_by_uuid

class TestCleanup(unittest.TestCase):

    def test_get_projects_nohtmltag(self):
        self.assertFalse("<p>" in cleandata(get_project_by_uuid("6fa0f7de-4502-4995-92ae-5467e49df1b3")))

    def test_get_projects_no_nbsp(self):
        self.assertFalse("\xa0" in cleandata(get_project_by_uuid("6fa0f7de-4502-4995-92ae-5467e49df1b3")))

if __name__ == '__main__':
    unittest.main()