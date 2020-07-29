"""
Test module for the serice manager module
"""
import unittest
import sys
import os 

PACKAGE_PARENT = '../..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
import ServiceManager.service_manager as service_manager
import Tests.test_helper as test_helper
import Utils.enricher_entities as enricher_entities

class TestServiceManager(unittest.TestCase):
    def validate_process_project(self, project_obj):
        res = service_manager.process_project(project_obj)
        if isinstance(res, enricher_entities.ProjectResult):
            return True
        return False
    
    def validate_process_publication(self, publication_obj):
        res = service_manager.process_publication(publication_obj)
        if isinstance(res, enricher_entities.PublicationResult):
            return True
        return False

    def test_process_project(self):
        self.assertTrue(self.validate_process_project(test_helper.get_test_project()))
    
    def test_process_publication(self):
        self.assertTrue(self.validate_process_publication(test_helper.get_test_publication()))

   
if __name__ == '__main__':
    unittest.main()
