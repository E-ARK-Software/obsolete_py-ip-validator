"""
    Base class for unit tests.
"""
import os
import unittest
from metsvalidator.mets_validator_impl import load_xml

TEST_DIR = os.path.dirname(os.path.realpath(__file__))

# In this class we test first the correct mets root element and then different error samples.
# If validation error was detected - validation result should be False.
class Base(unittest.TestCase):
    """ Base class for tests of METS elements. This class defines a common
    'setUp' method that initializes rules which are used in the various tests. """

    #SOURCES_PATH = "sources/"

    @classmethod
    def setUpClass(cls):
        cls.rules = load_xml(cls.make_schematron_path("mets_validator.xml"))

    @classmethod
    def get_test_resources_dir(cls):
        """Return the resources directory path"""
        return os.path.join(TEST_DIR, "../resources")

    @classmethod
    def get_schematron_dir(cls):
        """Return the scematron directory path"""
        return os.path.join(TEST_DIR, "../..", "schematron")

    @classmethod
    def make_schematron_path(cls, name):
        """Concatencates the passed name to a schematron directory path"""
        return os.path.join(cls.get_schematron_dir(), name)

    @classmethod
    def make_resource_path(cls, name):
        """Concatencates the passed name to a test resource directory path"""
        return os.path.join(cls.get_test_resources_dir(), name)

if __name__ == '__main__':
    unittest.main()
