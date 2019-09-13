from test.old_validator.base import Base
from test.utils import Utils

from metsvalidator.mets_validator_impl import validate

# In this class we test first the correct mets structmap element in PREMIS format and then different error samples.
# If validation error was detected - validation result should be False.
class MetsStructMapPremisTestCase(Base):
    """ Tests for METS structmap premis element """

    def test_file_rules(self):
        """Test for file schematron rules."""
        for file in Utils.mets_type("structmap"):
            result, _ = validate(self.rules, file)
            print(file)
            self.assertTrue(result)
