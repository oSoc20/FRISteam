""" Test module for the datacleaing module

"""

import unittest
from Cleanup.datacleaning import get_projects_and_clean, get_project_by_uuid_and_clean

class TestCleanup(unittest.TestCase):

    def test_get_projects_length(self):
        self.assertEqual(len(get_projects_and_clean(2)), 2)

    def test_get_projects_nohtmltag(self):
        self.assertFalse("<p>" in get_projects_and_clean(1))

    def test_get_projects_no_nbsp(self):
        self.assertFalse("\xa0" in get_projects_and_clean(1))

    def test_get_project_by_uuid_id(self):
        self.assertEqual(get_project_by_uuid_and_clean("6fa0f7de-4502-4995-92ae-5467e49df1b3")['id'],"6fa0f7de-4502-4995-92ae-5467e49df1b3")

if __name__ == '__main__':
    unittest.main()