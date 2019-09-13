"""
  Unit tests for XML Schema validation.
"""
import unittest

from lxml import etree

from earkips.xml.xsd import MetsValidator
from earkips.xml.schematron import SchmematronValidator, IpSchematronValidator, _schematron_file

from .utils import Utils

class XMLSchemaTests(unittest.TestCase):
    """ Unit tests for schema validation. """
    validator = MetsValidator()

    def test_invalid_mets(self):
        """ Test validation of valid file."""
        for invalid_mets in Utils.invalid_mets():
            is_valid, _ = XMLSchemaTests.validator.is_valid(invalid_mets)
            self.assertFalse(is_valid)

    def test_valid_mets(self):
        """ Test validation of valid file."""
        for valid_mets in Utils.valid_mets():
            is_valid, _ = XMLSchemaTests.validator.is_valid(valid_mets)
            self.assertTrue(is_valid)

    def test_no_file(self):
        """ Test validation of no file."""
        with self.assertRaises(OSError) as os_error:
            XMLSchemaTests.validator.is_valid(Utils.to_resource_dir('no.xml'))
        self.assertTrue('Error reading file' in str(os_error.exception))

    def test_directory(self):
        """ Test validation of directory."""
        with self.assertRaises(etree.XMLSyntaxError) as syntax_error:
            XMLSchemaTests.validator.is_valid(".")
        self.assertTrue('Document is empty' in str(syntax_error.exception))

    def test_root(self):
        """Test mets root validation."""
        self._test_schema_validator("root")

    def test_hdr(self):
        """Test mets hdr validation."""
        self._test_schema_validator("hdr")

    def test_dmd(self):
        """Test mets dmd validation."""
        self._test_schema_validator("dmd")

    def test_amd(self):
        """Test mets amd validation."""
        self._test_schema_validator("amd")

    def test_file(self):
        """Test mets file validation."""
        self._test_schema_validator("file")

    def test_structmap(self):
        """Test mets file validation."""
        self._test_schema_validator("structmap")

    def _test_schema_validator(self, name):
        for file in Utils.mets_type(name):
            print(file)
            result, message = self.validator.is_valid(file)
            if ".invalid" in file:
                self.assertFalse(result, file)
            else:
                self.assertTrue(result, file + ":\n" + str(message))

class XMLSchematronTests(unittest.TestCase):
    """Test cases for low level schematron validator"""
    def test_root(self):
        """Test mets root validation."""
        self._test_schematron_validator("root")

    def test_hdr(self):
        """Test mets hdr validation."""
        self._test_schematron_validator("hdr")

    def test_dmd(self):
        """Test mets dmd validation."""
        self._test_schematron_validator("dmd")

    def test_amd(self):
        """Test mets amd validation."""
        self._test_schematron_validator("amd")

    def test_file(self):
        """Test mets file validation."""
        self._test_schematron_validator("file")

    def test_structmap(self):
        """Test mets file validation."""
        self._test_schematron_validator("structmap")

    def _test_schematron_validator(self, name):
        validator = SchmematronValidator(_schematron_file(name))
        for file in Utils.mets_type(name):
            print(file)
            result, report = validator.is_valid(file)
            if ".sidelined" in str(file):
                pass
            elif ".valid" in str(file):
                self.assertTrue(result, file + ":\n" + str(report))
            else:
                self.assertFalse(result, file + ":\n" + str(report))

class IpSchematronValidatorTests(unittest.TestCase):
    """Test cases for schematron validator"""
    def test_root(self):
        """Test mets root validation."""
        self._test_ip_schematron_validator("root")

    def test_hdr(self):
        """Test mets hdr validation."""
        self._test_ip_schematron_validator("hdr")

    def test_dmd(self):
        """Test mets dmd validation."""
        self._test_ip_schematron_validator("dmd")

    def test_amd(self):
        """Test mets amd validation."""
        self._test_ip_schematron_validator("amd")

    def test_file(self):
        """Test mets file validation."""
        self._test_ip_schematron_validator("file")

    def test_structmap(self):
        """Test mets file validation."""
        self._test_ip_schematron_validator("structmap")


    def _test_ip_schematron_validator(self, name):
        validator = IpSchematronValidator()
        for file in Utils.mets_type(name):
            print(file)
            try:
                result, reports = validator.validate(file)
                if not result:
                    for report in reports:
                        print(report)
                        print(str(reports[report]))
                if ".sidelined" in str(file):
                    pass
                elif ".valid" in str(file):
                    self.assertTrue(result, file + ":\n" + str(reports))
                else:
                    self.assertFalse(result, file)
            except etree.XSLTApplyError as excep:
                print(str(excep))
                self.fail()

if __name__ == '__main__':
    unittest.main()
