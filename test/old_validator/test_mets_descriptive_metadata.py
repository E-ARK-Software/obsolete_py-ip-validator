from test.old_validator.base import Base
from test.utils import Utils

from metsvalidator.mets_validator_impl import validate

# In this class we test first the correct mets descriptive metadata element and then different error samples.
# If validation error was detected - validation result should be False.
class MetsDescriptiveMetadataTestCase(Base):
    """ Tests for METS descriptive metadata element """

    def test_file_rules(self):
        """Test for file schematron rules."""
        for file in Utils.mets_type("dmd"):
            result, _ = validate(self.rules, file)
            print(file)
            self.assertTrue(result)
