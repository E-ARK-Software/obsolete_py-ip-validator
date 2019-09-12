from test.base import Base

from metsvalidator.mets_validator_impl import validate

# In this class we test first the correct mets root element and then different error samples.
# If validation error was detected - validation result should be False.
class MetsRootTestCase(Base):
    """ Tests for METS root element """

    def test_load_rules(self):
        result, _ = validate(self.rules, self.make_resource_path("mets_root_element/mets_root_element_ok.xml"))
        #print("is valid: " + str(result))
        #print(type(report))
        #print(report)
        self.assertTrue(result)

    def test_csip2_has_objid_specification(self):
        result, _ = validate(self.rules, self.make_resource_path("mets_root_element/mets_root_element_objid_not_exists.xml"))
        self.assertFalse(result)

    def test_csip3_has_type_specification(self):
        result, _ = validate(self.rules, self.make_resource_path("mets_root_element/mets_root_element_type_not_exists.xml"))
        self.assertFalse(result)

    def test_csip4_has_content_specification(self):
        result, _ = validate(self.rules, self.make_resource_path("mets_root_element/mets_root_element_csip_not_exists.xml"))
        self.assertFalse(result)

    def test_csip4_content_specification_value_error(self):
        result, _ = validate(self.rules, self.make_resource_path("mets_root_element/mets_root_element_csip_value_error.xml"))
        self.assertFalse(result)

    def test_csip5_content_specification_missing_other_type_error(self):
        result, _ = validate(self.rules, self.make_resource_path("mets_root_element/mets_root_element_csip_other_type_not_exists.xml"))
        self.assertFalse(result)

    def test_csip6_content_specification_missing_profile_url_error(self):
        result, _ = validate(self.rules, self.make_resource_path("mets_root_element/mets_root_element_profile_url_not_exists.xml"))
        self.assertFalse(result)
