import unittest
from metsvalidator.mets_validator_impl import load_xml, validate

# In this class we test first the correct mets root element and then different error samples. 
# If validation error was detected - validation result should be False.
class MetsRootTestCase(unittest.TestCase):
    """ Tests for METS root element """

    @classmethod
    def setUpClass(self):
        self.rules = load_xml("metsvalidator/mets_validator.xml")

    def test_load_rules(self):
        validationResult, report = validate(self.rules, "metsvalidator/mets_root_element_ok.xml")
        #print("is valid: " + str(validationResult))
        #print(type(report))
        #print(report)
        self.assertTrue(validationResult==True)

    #def test_csip1_check_root_element(self):
    #    validationResult, report = validate(self.rules, "metsvalidator/mets_root_element_not_exists.xml")
    #    self.assertTrue(validationResult==True)

    def test_csip2_has_objid_specification(self):
        validationResult, report = validate(self.rules, "metsvalidator/mets_root_element_objid_not_exists.xml")
        self.assertTrue(validationResult==False)

    def test_csip3_has_type_specification(self):
        validationResult, report = validate(self.rules, "metsvalidator/mets_root_element_type_not_exists.xml")
        self.assertTrue(validationResult==False)

    def test_csip4_has_content_specification(self):
        validationResult, report = validate(self.rules, "metsvalidator/mets_root_element_csip_not_exists.xml")
        self.assertTrue(validationResult==False)

    def test_csip4_content_specification_value_error(self):
        validationResult, report = validate(self.rules, "metsvalidator/mets_root_element_csip_value_error.xml")
        self.assertTrue(validationResult==False)

    def test_csip5_content_specification_missing_other_type_error(self):
        validationResult, report = validate(self.rules, "metsvalidator/mets_root_element_csip_other_type_not_exists.xml")
        self.assertTrue(validationResult==False)

    def test_csip6_content_specification_missing_profile_url_error(self):
        validationResult, report = validate(self.rules, "metsvalidator/mets_root_element_profile_url_not_exists.xml")
        self.assertTrue(validationResult==False)

if __name__ == '__main__':
    unittest.main()
