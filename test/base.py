"""
    Base class for unit tests.
"""
import unittest
from metsvalidator.mets_validator_impl import load_xml

# In this class we test first the correct mets root element and then different error samples.
# If validation error was detected - validation result should be False.
class Base(unittest.TestCase):
    """ Base class for tests of METS elements. This class defines a common
    'setUp' method that initializes rules which are used in the various tests. """

    #SOURCES_PATH = "sources/"

    @classmethod
    def setUpClass(cls):
        cls.SOURCES_PATH = "sources/"
        cls.rules = load_xml(cls.SOURCES_PATH+"mets_validator.xml")

if __name__ == '__main__':
    unittest.main()
