from test.utils import Utils
from test.old_validator.base import Base

from metsvalidator.mets_validator_impl import validate

# In this class we test first the correct mets root element and then different error samples.
# If validation error was detected - validation result should be False.
class MetsRootTestCase(Base):
    """ Tests for METS root element """

    def test_file_rules(self):
        """Test for file schematron rules."""
        for file in Utils.mets_type("root"):
            result, report = validate(self.rules, file)
            print(file)
            print(report)
            if "ok" in file:
                self.assertTrue(result)
            elif "sidelined" in file:
                pass
            else:
                self.assertFalse(result)
