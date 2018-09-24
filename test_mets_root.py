import unittest
from metsvalidator.mets_validator_impl import load_xml, validate

# In this class we test first the correct mets root element and then different error samples. 
# If validation error was detected - validation result should be False.
class MetsRootTestCase(unittest.TestCase):
    """ Tests for METS root element """

    def test_load_rules(self):
        rules = load_xml("metsvalidator/mets_validator.xml")
        validationResult, report = validate(rules, "metsvalidator/mets_root_element_ok.xml")
        #print("is valid: " + str(validationResult))
        #print(type(report))
        #print(report)
        self.assertTrue(validationResult==True)

    def test_cif4_has_content_specification(self):
        rules = load_xml("metsvalidator/mets_validator.xml")
        validationResult, report = validate(rules, "metsvalidator/mets_root_element_csip_not_exists.xml")
        self.assertTrue(validationResult==False)

    def test_cif4_content_specification_value_error(self):
        rules = load_xml("metsvalidator/mets_validator.xml")
        validationResult, report = validate(rules, "metsvalidator/mets_root_element_csip_value_error.xml")
        self.assertTrue(validationResult==False)

if __name__ == '__main__':
    unittest.main()
