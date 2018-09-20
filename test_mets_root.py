import unittest
from metsvalidator.mets_validator_impl import load_rules

class MetsRootTestCase(unittest.TestCase):
    """ Tests for METS root element """

    def test_load_rules(self):
        load_rules()
        self.assertTrue(1==1)

    def test_has_cif4(self):
        self.assertTrue(2==1)

if __name__ == '__main__':
    unittest.main()
