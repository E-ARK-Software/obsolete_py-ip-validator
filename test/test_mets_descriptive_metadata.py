from test.base import Base
from metsvalidator.mets_validator_impl import validate

# In this class we test first the correct mets descriptive metadata element and then different error samples.
# If validation error was detected - validation result should be False.
class MetsDescriptiveMetadataTestCase(Base):
    """ Tests for METS descriptive metadata element """

    def test_load_rules(self):
        result, _ = validate(self.rules, self.make_resource_path("mets_descriptive_metadata_element/mets_descriptive_metadata_element_ok.xml"))
        self.assertTrue(result)

    def test_csip20_check_descriptive_metadata_element(self):
        result, _ = validate(self.rules, self.make_resource_path("mets_descriptive_metadata_element/mets_descriptive_metadata_element_not_exists.xml"))
        self.assertTrue(result)

    def test_csip21_check_descriptive_metadata_id(self):
        result, _ = validate(self.rules, self.make_resource_path("mets_descriptive_metadata_element/mets_descriptive_metadata_element_id_not_exists.xml"))
        self.assertTrue(result)

    def test_csip22_check_descriptive_metadata_admid(self):
        result, _ = validate(self.rules, self.make_resource_path("mets_descriptive_metadata_element/mets_descriptive_metadata_element_admid_not_exists.xml"))
        self.assertTrue(result)

    def test_csip23_check_descriptive_metadata_creation_date(self):
        result, _ = validate(self.rules, self.make_resource_path("mets_descriptive_metadata_element/mets_descriptive_metadata_element_creation_date_not_exists.xml"))
        self.assertTrue(result)

    def test_csip24_check_descriptive_metadata_status(self):
        result, _ = validate(self.rules, self.make_resource_path("mets_descriptive_metadata_element/mets_descriptive_metadata_element_status_not_exists.xml"))
        self.assertTrue(result)

    def test_csip25_check_descriptive_metadata_reference(self):
        result, _ = validate(self.rules, self.make_resource_path("mets_descriptive_metadata_element/mets_descriptive_metadata_element_reference_not_exists.xml"))
        self.assertTrue(result)

    # location group

    def test_csip26_check_descriptive_metadata_location_type(self):
        result, _ = validate(self.rules, self.make_resource_path("mets_descriptive_metadata_element/mets_descriptive_metadata_location_location_type_not_exists.xml"))
        self.assertTrue(result)

    def test_csip27_check_descriptive_metadata_location_type_value_url(self):
        result, _ = validate(self.rules, self.make_resource_path("mets_descriptive_metadata_element/mets_descriptive_metadata_location_location_type_value_not_url.xml"))
        self.assertTrue(result)

    def test_csip28_check_descriptive_metadata_location_xlink_type(self):
        result, _ = validate(self.rules, self.make_resource_path("mets_descriptive_metadata_element/mets_descriptive_metadata_location_xlink_type_not_exists.xml"))
        self.assertTrue(result)

    def test_csip29_check_descriptive_metadata_location_xlink_type_value(self):
        result, _ = validate(self.rules, self.make_resource_path("mets_descriptive_metadata_element/mets_descriptive_metadata_location_xlink_type_value_not_simple.xml"))
        self.assertTrue(result)

    def test_csip30_check_descriptive_metadata_location_xlink_href_validation(self):
        result, _ = validate(self.rules, self.make_resource_path("mets_descriptive_metadata_element/mets_descriptive_metadata_location_xlink_href_validation.xml"))
        self.assertTrue(result)

    def test_csip31_check_descriptive_metadata_mdtype_validation(self):
        result, _ = validate(self.rules, self.make_resource_path("mets_descriptive_metadata_element/mets_descriptive_metadata_mdtype_validation.xml"))
        self.assertTrue(result)

    def test_csip32_check_descriptive_metadata_core_mimetype_validation(self):
        result, _ = validate(self.rules, self.make_resource_path("mets_descriptive_metadata_element/mets_descriptive_metadata_core_mimetype_validation.xml"))
        self.assertTrue(result)

    def test_csip33_check_descriptive_metadata_core_size_validation(self):
        result, _ = validate(self.rules, self.make_resource_path("mets_descriptive_metadata_element/mets_descriptive_metadata_core_size_validation.xml"))
        self.assertTrue(result)

    def test_csip34_check_descriptive_metadata_core_created_validation(self):
        result, _ = validate(self.rules, self.make_resource_path("mets_descriptive_metadata_element/mets_descriptive_metadata_core_created_validation.xml"))
        self.assertTrue(result)

    def test_csip35_check_descriptive_metadata_core_checksum_validation(self):
        result, _ = validate(self.rules, self.make_resource_path("mets_descriptive_metadata_element/mets_descriptive_metadata_core_checksum_validation.xml"))
        self.assertTrue(result)

    def test_csip36_check_descriptive_metadata_core_checksumtype_validation(self):
        result, _ = validate(self.rules, self.make_resource_path("mets_descriptive_metadata_element/mets_descriptive_metadata_core_checksumtype_validation.xml"))
        self.assertTrue(result)
