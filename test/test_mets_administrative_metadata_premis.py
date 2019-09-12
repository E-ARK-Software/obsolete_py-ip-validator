from test.base import Base
from metsvalidator.mets_validator_impl import validate

# In this class we test first the correct mets administrative metadata element in PREMIS format and then different error samples.
# If validation error was detected - validation result should be False.
class MetsAdministrativeMetadataPremisTestCase(Base):
    """ Tests for METS administrative metadata premis element """

    def test_load_rules(self):
        result, _ = validate(self.rules, self.make_resource_path("mets_administrative_metadata_premis_element/mets_administrative_metadata_premis_element_ok.xml"))
        self.assertTrue(result)

    def test_csip31_check_administrative_metadata_premis_element(self):
        result, _ = validate(self.rules, self.make_resource_path("mets_administrative_metadata_premis_element/mets_administrative_metadata_premis_element_not_exists.xml"))
        self.assertTrue(result)

    def test_csip32_check_administrative_metadata_premis_element_digiprovmd(self):
        result, _ = validate(self.rules, self.make_resource_path("mets_administrative_metadata_premis_element/mets_administrative_metadata_premis_element_digiprovmd_validation.xml"))
        self.assertTrue(result)

    def test_csip33_check_administrative_metadata_premis_element_digiprovmd_id(self):
        result, _ = validate(self.rules, self.make_resource_path("mets_administrative_metadata_premis_element/mets_administrative_metadata_premis_element_digiprovmd_id_validation.xml"))
        self.assertTrue(result)

    def test_csip34_check_administrative_metadata_premis_element_digiprovmd_status(self):
        result, _ = validate(self.rules, self.make_resource_path("mets_administrative_metadata_premis_element/mets_administrative_metadata_premis_element_digiprovmd_status_validation.xml"))
        self.assertTrue(result)

    def test_csip35_check_administrative_metadata_premis_element_mdref(self):
        result, _ = validate(self.rules, self.make_resource_path("mets_administrative_metadata_premis_element/mets_administrative_metadata_premis_element_mdref_validation.xml"))
        self.assertTrue(result)

    def test_csip36_check_administrative_metadata_premis_element_mdref_loctype(self):
        result, _ = validate(self.rules, self.make_resource_path("mets_administrative_metadata_premis_element/mets_administrative_metadata_premis_element_mdref_loctype_validation.xml"))
        self.assertTrue(result)

    def test_csip37_check_administrative_metadata_premis_element_mdref_xlink_type(self):
        result, _ = validate(self.rules, self.make_resource_path("mets_administrative_metadata_premis_element/mets_administrative_metadata_premis_element_mdref_xlink_type_validation.xml"))
        self.assertTrue(result)

    def test_csip38_check_administrative_metadata_premis_element_mdref_xlink_href(self):
        result, _ = validate(self.rules, self.make_resource_path("mets_administrative_metadata_premis_element/mets_administrative_metadata_premis_element_mdref_xlink_href_validation.xml"))
        self.assertTrue(result)

    def test_csip39_check_administrative_metadata_premis_element_mdref_mdtype(self):
        result, _ = validate(self.rules, self.make_resource_path("mets_administrative_metadata_premis_element/mets_administrative_metadata_premis_element_mdref_mdtype_validation.xml"))
        self.assertTrue(result)

    def test_csip40_check_administrative_metadata_premis_element_mdref_mimetype(self):
        result, _ = validate(self.rules, self.make_resource_path("mets_administrative_metadata_premis_element/mets_administrative_metadata_premis_element_mdref_mimetype_validation.xml"))
        self.assertTrue(result)

    def test_csip41_check_administrative_metadata_premis_element_mdref_file_size(self):
        result, _ = validate(self.rules, self.make_resource_path("mets_administrative_metadata_premis_element/mets_administrative_metadata_premis_element_mdref_file_size_validation.xml"))
        self.assertTrue(result)

    def test_csip42_check_administrative_metadata_premis_element_mdref_file_creation_date(self):
        result, _ = validate(self.rules, self.make_resource_path("mets_administrative_metadata_premis_element/mets_administrative_metadata_premis_element_mdref_created_validation.xml"))
        self.assertTrue(result)

    def test_csip43_check_administrative_metadata_premis_element_mdref_checksum(self):
        result, _ = validate(self.rules, self.make_resource_path("mets_administrative_metadata_premis_element/mets_administrative_metadata_premis_element_mdref_checksum_validation.xml"))
        self.assertTrue(result)

    def test_csip44_check_administrative_metadata_premis_element_mdref_checksum_type(self):
        result, _ = validate(self.rules, self.make_resource_path("mets_administrative_metadata_premis_element/mets_administrative_metadata_premis_element_mdref_checksum_type_validation.xml"))
        self.assertTrue(result)

    def test_csip45_check_administrative_metadata_premis_element_rightsmd(self):
        result, _ = validate(self.rules, self.make_resource_path("mets_administrative_metadata_premis_element/mets_administrative_metadata_premis_element_rightsmd_not_exists.xml"))
        self.assertTrue(result)
