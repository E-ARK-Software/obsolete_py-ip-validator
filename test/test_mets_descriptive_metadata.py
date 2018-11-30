from base import Base
from metsvalidator.mets_validator_impl import validate

# In this class we test first the correct mets descriptive metadata element and then different error samples. 
# If validation error was detected - validation result should be False.
class MetsDescriptiveMetadataTestCase(Base):
    """ Tests for METS descriptive metadata element """

    def test_load_rules(self):
        validationResult, report = validate(self.rules, self.SOURCES_PATH+"mets_descriptive_metadata_element_ok.xml")
        self.assertTrue(validationResult==True)

    def test_csip20_check_descriptive_metadata_element(self):
        validationResult, report = validate(self.rules, self.SOURCES_PATH+"mets_descriptive_metadata_element_not_exists.xml")
        self.assertTrue(validationResult==True)

    def test_csip21_check_descriptive_metadata_id(self):
        validationResult, report = validate(self.rules, self.SOURCES_PATH+"mets_descriptive_metadata_element_id_not_exists.xml")
        self.assertTrue(validationResult==True)

    def test_csip22_check_descriptive_metadata_admid(self):
        validationResult, report = validate(self.rules, self.SOURCES_PATH+"mets_descriptive_metadata_element_admid_not_exists.xml")
        self.assertTrue(validationResult==True)

    def test_csip23_check_descriptive_metadata_creation_date(self):
        validationResult, report = validate(self.rules, self.SOURCES_PATH+"mets_descriptive_metadata_element_creation_date_not_exists.xml")
        self.assertTrue(validationResult==True)

    def test_csip24_check_descriptive_metadata_status(self):
        validationResult, report = validate(self.rules, self.SOURCES_PATH+"mets_descriptive_metadata_element_status_not_exists.xml")
        self.assertTrue(validationResult==True)

    def test_csip25_check_descriptive_metadata_reference(self):
        validationResult, report = validate(self.rules, self.SOURCES_PATH+"mets_descriptive_metadata_element_reference_not_exists.xml")
        self.assertTrue(validationResult==True)

