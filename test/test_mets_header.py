from test.base import Base
from metsvalidator.mets_validator_impl import validate

# In this class we test first the correct mets header element and then different error samples.
# If validation error was detected - validation result should be False.
class MetsHeaderTestCase(Base):
    """ Tests for METS header element """

    def test_load_rules(self):
        result, _ = validate(self.rules, self.make_resource_path("mets_header_element/mets_header_element_ok.xml"))
        self.assertTrue(result)

    def test_csip7_check_header_element(self):
        result, _ = validate(self.rules, self.make_resource_path("mets_header_element/mets_header_element_not_exists.xml"))
        self.assertTrue(result)

    def test_csip9_check_package_creation_date(self):
        result, _ = validate(self.rules, self.make_resource_path("mets_header_element/mets_header_package_creation_date_not_exists.xml"))
        self.assertTrue(result)

    def test_csip10_check_package_last_modification_date(self):
        result, _ = validate(self.rules, self.make_resource_path("mets_header_element/mets_header_package_last_modification_date_not_exists.xml"))
        self.assertTrue(result)

    def test_csip11_check_oais_package_type(self):
        result, _ = validate(self.rules, self.make_resource_path("mets_header_element/mets_header_oais_package_type_not_exists.xml"))
        self.assertTrue(result)
        result, _ = validate(self.rules, self.make_resource_path("mets_header_element/mets_header_oais_package_type_value_error.xml"))
        self.assertTrue(result)

    def test_csip12_check_header_agent_element(self):
        result, _ = validate(self.rules, self.make_resource_path("mets_header_element/mets_header_agent_element_not_exists.xml"))
        self.assertTrue(result)

    def test_csip13_check_header_agent_role_element(self):
        result, _ = validate(self.rules, self.make_resource_path("mets_header_element/mets_header_element_agent_role_not_exists.xml"))
        self.assertTrue(result)

    def test_csip15_check_header_agent_type_element(self):
        result, _ = validate(self.rules, self.make_resource_path("mets_header_element/mets_header_element_agent_type_not_exists.xml"))
        self.assertTrue(result)

    def test_csip16_check_header_agent_other_type_element(self):
        result, _ = validate(self.rules, self.make_resource_path("mets_header_element/mets_header_element_agent_othertype_not_exists.xml"))
        self.assertTrue(result)

    def test_csip17_check_header_agent_name_element(self):
        result, _ = validate(self.rules, self.make_resource_path("mets_header_element/mets_header_element_agent_name_not_exists.xml"))
        self.assertTrue(result)

    def test_csip18_check_header_agent_note_element(self):
        result, _ = validate(self.rules, self.make_resource_path("mets_header_element/mets_header_element_agent_note_not_exists.xml"))
        self.assertTrue(result)

    def test_csip19_check_header_agent_note_type_element(self):
        result, _ = validate(self.rules, self.make_resource_path("mets_header_element/mets_header_element_agent_note_type_not_exists.xml"))
        self.assertTrue(result)
