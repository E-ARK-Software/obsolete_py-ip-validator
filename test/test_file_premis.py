from base import Base
from metsvalidator.mets_validator_impl import validate

# In this class we test first the correct mets administrative metadata element in PREMIS format and then different error samples. 
# If validation error was detected - validation result should be False.
class MetsAdministrativeMetadataPremisTestCase(Base):
    """ Tests for METS administrative metadata premis element """

    def test_load_rules(self):
        validationResult, report = validate(self.rules, self.SOURCES_PATH+"mets_file_premis_element/mets_file_premis_element_ok.xml")
        self.assertTrue(validationResult==True)

    def test_csip58_check_file_premis_element(self):
        validationResult, report = validate(self.rules, self.SOURCES_PATH+"mets_file_premis_element/mets_file_premis_element_not_exists.xml")
        self.assertTrue(validationResult==True)

    def test_csip59_check_file_premis_element_id(self):
        validationResult, report = validate(self.rules, self.SOURCES_PATH+"mets_file_premis_element/mets_file_premis_element_id_not_exists.xml")
        self.assertTrue(validationResult==True)

    def test_csip60_check_file_premis_element_filegrp(self):
        validationResult, report = validate(self.rules, self.SOURCES_PATH+"mets_file_premis_element/mets_file_premis_element_filegrp_not_exists.xml")
        self.assertTrue(validationResult==True)

    def test_csip61_check_file_premis_element_admid(self):
        validationResult, report = validate(self.rules, self.SOURCES_PATH+"mets_file_premis_element/mets_file_premis_element_admid_not_exists.xml")
        self.assertTrue(validationResult==True)



