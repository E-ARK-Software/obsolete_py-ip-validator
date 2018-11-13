import unittest
from metsvalidator.mets_validator_impl import load_xml, validate

# In this class we test first the correct mets root element and then different error samples. 
# If validation error was detected - validation result should be False.
class Base(unittest.TestCase):
    """ Base class for tests of METS elements. This class defines a common 'setUp' method that initializes rules which are used in the various tests. """

    #SOURCES_PATH = "sources/"

    @classmethod
    def setUpClass(self):
        self.SOURCES_PATH = "sources/"
        self.rules = load_xml(self.SOURCES_PATH+"mets_validator.xml")

if __name__ == '__main__':
    unittest.main()
