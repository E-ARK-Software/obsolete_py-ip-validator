from metsvalidator.mets_validator_impl import validate

from utils import Utils
from old_validator.base import Base

# In this class we test first the correct mets administrative metadata element in PREMIS format and then different error samples.
# If validation error was detected - validation result should be False.
class MetsAdministrativeMetadataPremisTestCase(Base):
    """ Tests for METS administrative metadata premis element """

    def test_file_rules(self):
        """Test for file schematron rules."""
        for file in Utils.mets_type("amd"):
            result, _ = validate(self.rules, file)
            print(file)
            self.assertTrue(result)
