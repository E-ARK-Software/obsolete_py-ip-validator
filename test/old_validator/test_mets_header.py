from metsvalidator.mets_validator_impl import validate

from old_validator.base import Base
from utils import Utils

# In this class we test first the correct mets header element and then different error samples.
# If validation error was detected - validation result should be False.
class MetsHeaderTestCase(Base):
    """ Tests for METS header element """

    def test_file_rules(self):
        """Test for file schematron rules."""
        for file in Utils.mets_type("hdr"):
            result, _ = validate(self.rules, file)
            print(file)
            self.assertTrue(result)
