from base import Base
from metsvalidator.mets_validator_impl import validate

# In this class we test first the correct mets administrative metadata element in PREMIS format and then different error samples. 
# If validation error was detected - validation result should be False.
class MetsAdministrativeMetadataPremisTestCase(Base):
    """ Tests for METS administrative metadata premis element """

    def test_load_rules(self):
        validationResult, report = validate(self.rules, self.SOURCES_PATH+"mets_administrative_metadata_premis_element/mets_administrative_metadata_premis_element_ok.xml")
        self.assertTrue(validationResult==True)

    def test_csip31_check_administrative_metadata_premis_element(self):
        validationResult, report = validate(self.rules, self.SOURCES_PATH+"mets_administrative_metadata_premis_element/mets_administrative_metadata_premis_element_not_exists.xml")
        self.assertTrue(validationResult==True)

    def test_csip32_check_administrative_metadata_premis_element_digiprovmd(self):
        validationResult, report = validate(self.rules, self.SOURCES_PATH+"mets_administrative_metadata_premis_element/mets_administrative_metadata_premis_element_digiprovmd_validation.xml")
        self.assertTrue(validationResult==True)

    def test_csip33_check_administrative_metadata_premis_element_digiprovmd_id(self):
        validationResult, report = validate(self.rules, self.SOURCES_PATH+"mets_administrative_metadata_premis_element/mets_administrative_metadata_premis_element_digiprovmd_id_validation.xml")
        self.assertTrue(validationResult==True)

    def test_csip34_check_administrative_metadata_premis_element_digiprovmd_status(self):
        validationResult, report = validate(self.rules, self.SOURCES_PATH+"mets_administrative_metadata_premis_element/mets_administrative_metadata_premis_element_digiprovmd_status_validation.xml")
        self.assertTrue(validationResult==True)

    def test_csip35_check_administrative_metadata_premis_element_mdref(self):
        validationResult, report = validate(self.rules, self.SOURCES_PATH+"mets_administrative_metadata_premis_element/mets_administrative_metadata_premis_element_mdref_validation.xml")
        self.assertTrue(validationResult==True)

    def test_csip36_check_administrative_metadata_premis_element_mdref_loctype(self):
        validationResult, report = validate(self.rules, self.SOURCES_PATH+"mets_administrative_metadata_premis_element/mets_administrative_metadata_premis_element_mdref_loctype_validation.xml")
        self.assertTrue(validationResult==True)

    def test_csip37_check_administrative_metadata_premis_element_mdref_xlink_type(self):
        validationResult, report = validate(self.rules, self.SOURCES_PATH+"mets_administrative_metadata_premis_element/mets_administrative_metadata_premis_element_mdref_xlink_type_validation.xml")
        self.assertTrue(validationResult==True)

    def test_csip38_check_administrative_metadata_premis_element_mdref_xlink_href(self):
        validationResult, report = validate(self.rules, self.SOURCES_PATH+"mets_administrative_metadata_premis_element/mets_administrative_metadata_premis_element_mdref_xlink_href_validation.xml")
        self.assertTrue(validationResult==True)

    def test_csip39_check_administrative_metadata_premis_element_mdref_mdtype(self):
        validationResult, report = validate(self.rules, self.SOURCES_PATH+"mets_administrative_metadata_premis_element/mets_administrative_metadata_premis_element_mdref_mdtype_validation.xml")
        self.assertTrue(validationResult==True)

    def test_csip40_check_administrative_metadata_premis_element_mdref_mimetype(self):
        validationResult, report = validate(self.rules, self.SOURCES_PATH+"mets_administrative_metadata_premis_element/mets_administrative_metadata_premis_element_mdref_mimetype_validation.xml")
        self.assertTrue(validationResult==True)

    def test_csip41_check_administrative_metadata_premis_element_mdref_file_size(self):
        validationResult, report = validate(self.rules, self.SOURCES_PATH+"mets_administrative_metadata_premis_element/mets_administrative_metadata_premis_element_mdref_file_size_validation.xml")
        self.assertTrue(validationResult==True)

    def test_csip42_check_administrative_metadata_premis_element_mdref_file_creation_date(self):
        validationResult, report = validate(self.rules, self.SOURCES_PATH+"mets_administrative_metadata_premis_element/mets_administrative_metadata_premis_element_mdref_created_validation.xml")
        self.assertTrue(validationResult==True)

    def test_csip43_check_administrative_metadata_premis_element_mdref_checksum(self):
        validationResult, report = validate(self.rules, self.SOURCES_PATH+"mets_administrative_metadata_premis_element/mets_administrative_metadata_premis_element_mdref_checksum_validation.xml")
        self.assertTrue(validationResult==True)

    def test_csip44_check_administrative_metadata_premis_element_mdref_checksum_type(self):
        validationResult, report = validate(self.rules, self.SOURCES_PATH+"mets_administrative_metadata_premis_element/mets_administrative_metadata_premis_element_mdref_checksum_type_validation.xml")
        self.assertTrue(validationResult==True)

    def test_csip45_check_administrative_metadata_premis_element_rightsmd(self):
        validationResult, report = validate(self.rules, self.SOURCES_PATH+"mets_administrative_metadata_premis_element/mets_administrative_metadata_premis_element_rightsmd_not_exists.xml")
        self.assertTrue(validationResult==True)




