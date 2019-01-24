from base import Base
from metsvalidator.mets_validator_impl import validate

# In this class we test first the correct mets descriptive metadata element and then different error samples. 
# If validation error was detected - validation result should be False.
class MetsDescriptiveMetadataTestCase(Base):
    """ Tests for METS descriptive metadata element """

    def test_load_rules(self):
        validationResult, report = validate(self.rules, self.SOURCES_PATH+"mets_descriptive_metadata_element_ok.xml")
        self.assertTrue(validationResult==True)

    def test_csip37_check_administrative_metadata_element(self):
        validationResult, report = validate(self.rules, self.SOURCES_PATH+"mets_administrative_metadata_element_not_exists.xml")
        self.assertTrue(validationResult==True)

