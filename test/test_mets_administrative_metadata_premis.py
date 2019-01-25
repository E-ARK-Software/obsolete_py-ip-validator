from base import Base
from metsvalidator.mets_validator_impl import validate

# In this class we test first the correct mets administrative metadata element in PREMIS format and then different error samples. 
# If validation error was detected - validation result should be False.
class MetsAdministrativeMetadataPremisTestCase(Base):
    """ Tests for METS administrative metadata premis element """

    def test_load_rules(self):
        validationResult, report = validate(self.rules, self.SOURCES_PATH+"mets_administrative_metadata_premis_element_ok.xml")
        self.assertTrue(validationResult==True)

    def test_csip31_check_administrative_metadata_premis_element(self):
        validationResult, report = validate(self.rules, self.SOURCES_PATH+"mets_administrative_metadata_premis_element_not_exists.xml")
        self.assertTrue(validationResult==True)

    def test_csip32_check_administrative_metadata_premis_element_digiprovmd(self):
        validationResult, report = validate(self.rules, self.SOURCES_PATH+"mets_administrative_metadata_premis_element_digiprovmd_validation.xml")
        self.assertTrue(validationResult==True)

    def test_csip33_check_administrative_metadata_premis_element_digiprovmd_id(self):
        validationResult, report = validate(self.rules, self.SOURCES_PATH+"mets_administrative_metadata_premis_element_digiprovmd_id_validation.xml")
        self.assertTrue(validationResult==True)

    def test_csip34_check_administrative_metadata_premis_element_digiprovmd_status(self):
        validationResult, report = validate(self.rules, self.SOURCES_PATH+"mets_administrative_metadata_premis_element_digiprovmd_status_validation.xml")
        self.assertTrue(validationResult==True)




