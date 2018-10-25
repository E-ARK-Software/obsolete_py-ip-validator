import unittest
from metsvalidator.mets_validator_impl import load_xml, validate

# In this class we test first the correct mets header element and then different error samples. 
# If validation error was detected - validation result should be False.
class MetsHeaderTestCase(unittest.TestCase):
    """ Tests for METS header element """

    @classmethod
    def setUpClass(self):
        self.rules = load_xml("metsvalidator/mets_header_validator.xml")

    def test_load_rules(self):
        validationResult, report = validate(self.rules, "metsvalidator/mets_header_element_ok.xml")
        self.assertTrue(validationResult==True)

    def test_csip7_check_header_element(self):
        validationResult, report = validate(self.rules, "metsvalidator/mets_header_element_not_exists.xml")
        self.assertTrue(validationResult==True)

    #def test_csip7_has_objid_specification(self):
    #    validationResult, report = validate(self.rules, "metsvalidator/mets_root_element_objid_not_exists.xml")
    #    self.assertTrue(validationResult==False)

if __name__ == '__main__':
    unittest.main()
