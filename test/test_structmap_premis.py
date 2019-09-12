from test.base import Base
from metsvalidator.mets_validator_impl import validate

# In this class we test first the correct mets structmap element in PREMIS format and then different error samples.
# If validation error was detected - validation result should be False.
class MetsStructMapPremisTestCase(Base):
    """ Tests for METS structmap premis element """

    def test_load_rules(self):
        validationResult, report = validate(self.rules, self.SOURCES_PATH+"mets_structmap_premis_element/mets_structmap_premis_element_ok.xml")
        self.assertTrue(validationResult==True)

    def test_csip80_check_structmap_premis_element(self):
        validationResult, report = validate(self.rules, self.SOURCES_PATH+"mets_structmap_premis_element/mets_structmap_premis_element_not_exists.xml")
        self.assertTrue(validationResult==True)

    def test_csip81_check_structmap_premis_element_type(self):
        validationResult, report = validate(self.rules, self.SOURCES_PATH+"mets_structmap_premis_element/mets_structmap_premis_element_type_not_exists.xml")
        self.assertTrue(validationResult==True)

    def test_csip82_check_structmap_premis_element_label(self):
        validationResult, report = validate(self.rules, self.SOURCES_PATH+"mets_structmap_premis_element/mets_structmap_premis_element_label_not_exists.xml")
        self.assertTrue(validationResult==True)

    def test_csip83_check_structmap_premis_element_id(self):
        validationResult, report = validate(self.rules, self.SOURCES_PATH+"mets_structmap_premis_element/mets_structmap_premis_element_id_not_exists.xml")
        self.assertTrue(validationResult==True)

    def test_csip84_check_structmap_premis_element_div(self):
        validationResult, report = validate(self.rules, self.SOURCES_PATH+"mets_structmap_premis_element/mets_structmap_premis_element_div_not_exists.xml")
        self.assertTrue(validationResult==True)

    def test_csip85_check_structmap_premis_element_div_id(self):
        validationResult, report = validate(self.rules, self.SOURCES_PATH+"mets_structmap_premis_element/mets_structmap_premis_element_div_id_not_exists.xml")
        self.assertTrue(validationResult==True)

    def test_csip86_check_structmap_premis_element_div_label(self):
        validationResult, report = validate(self.rules, self.SOURCES_PATH+"mets_structmap_premis_element/mets_structmap_premis_element_div_label_not_exists.xml")
        self.assertTrue(validationResult==True)

    def test_csip87_check_structmap_premis_element_div_label_sub(self):
        validationResult, report = validate(self.rules, self.SOURCES_PATH+"mets_structmap_premis_element/mets_structmap_premis_element_div_label_sub_not_exists.xml")
        self.assertTrue(validationResult==True)

    def test_csip88_check_structmap_premis_element_div_div(self):
        validationResult, report = validate(self.rules, self.SOURCES_PATH+"mets_structmap_premis_element/mets_structmap_premis_element_div_div_not_exists.xml")
        self.assertTrue(validationResult==True)

    def test_csip89_check_structmap_premis_element_div_div_id(self):
        validationResult, report = validate(self.rules, self.SOURCES_PATH+"mets_structmap_premis_element/mets_structmap_premis_element_div_div_id_not_exists.xml")
        self.assertTrue(validationResult==True)

    def test_csip90_check_structmap_premis_element_div_div_label(self):
        validationResult, report = validate(self.rules, self.SOURCES_PATH+"mets_structmap_premis_element/mets_structmap_premis_element_div_div_label_not_exists.xml")
        self.assertTrue(validationResult==True)

    def test_csip91_check_structmap_premis_element_div_div_admid(self):
        validationResult, report = validate(self.rules, self.SOURCES_PATH+"mets_structmap_premis_element/mets_structmap_premis_element_div_div_admid_not_exists.xml")
        self.assertTrue(validationResult==True)

    def test_csip92_check_structmap_premis_element_div_div_dmdid(self):
        validationResult, report = validate(self.rules, self.SOURCES_PATH+"mets_structmap_premis_element/mets_structmap_premis_element_div_div_dmdid_not_exists.xml")
        self.assertTrue(validationResult==True)

    def test_csip93_check_structmap_premis_element_div_div_documentation(self):
        validationResult, report = validate(self.rules, self.SOURCES_PATH+"mets_structmap_premis_element/mets_structmap_premis_element_div_div_documentation_not_exists.xml")
        self.assertTrue(validationResult==True)

    def test_csip94_check_structmap_premis_element_div_div_documentation_id(self):
        validationResult, report = validate(self.rules, self.SOURCES_PATH+"mets_structmap_premis_element/mets_structmap_premis_element_div_div_documentation_id_not_exists.xml")
        self.assertTrue(validationResult==True)

    def test_csip95_check_structmap_premis_element_div_div_documentation_label(self):
        validationResult, report = validate(self.rules, self.SOURCES_PATH+"mets_structmap_premis_element/mets_structmap_premis_element_div_div_documentation_label_not_exists.xml")
        self.assertTrue(validationResult==True)

    def test_csip96_check_structmap_premis_element_div_div_documentation_contentid(self):
        validationResult, report = validate(self.rules, self.SOURCES_PATH+"mets_structmap_premis_element/mets_structmap_premis_element_div_div_documentation_contentid_not_exists.xml")
        self.assertTrue(validationResult==True)

    def test_csip97_check_structmap_premis_element_div_div_schema(self):
        validationResult, report = validate(self.rules, self.SOURCES_PATH+"mets_structmap_premis_element/mets_structmap_premis_element_div_div_schema_not_exists.xml")
        self.assertTrue(validationResult==True)

    def test_csip98_check_structmap_premis_element_div_div_schema_id(self):
        validationResult, report = validate(self.rules, self.SOURCES_PATH+"mets_structmap_premis_element/mets_structmap_premis_element_div_div_schema_id_not_exists.xml")
        self.assertTrue(validationResult==True)

    def test_csip99_check_structmap_premis_element_div_div_schema_label(self):
        validationResult, report = validate(self.rules, self.SOURCES_PATH+"mets_structmap_premis_element/mets_structmap_premis_element_div_div_schema_label_not_exists.xml")
        self.assertTrue(validationResult==True)

    def test_csip100_check_structmap_premis_element_div_div_schema_contentid(self):
        validationResult, report = validate(self.rules, self.SOURCES_PATH+"mets_structmap_premis_element/mets_structmap_premis_element_div_div_schema_contentid_not_exists.xml")
        self.assertTrue(validationResult==True)

    def test_csip101_check_structmap_premis_element_div_div_file(self):
        validationResult, report = validate(self.rules, self.SOURCES_PATH+"mets_structmap_premis_element/mets_structmap_premis_element_div_div_file_not_exists.xml")
        self.assertTrue(validationResult==True)

    def test_csip102_check_structmap_premis_element_div_div_file_id(self):
        validationResult, report = validate(self.rules, self.SOURCES_PATH+"mets_structmap_premis_element/mets_structmap_premis_element_div_div_file_id_not_exists.xml")
        self.assertTrue(validationResult==True)

    def test_csip103_check_structmap_premis_element_div_div_file_label(self):
        validationResult, report = validate(self.rules, self.SOURCES_PATH+"mets_structmap_premis_element/mets_structmap_premis_element_div_div_file_label_not_exists.xml")
        self.assertTrue(validationResult==True)

    def test_csip104_check_structmap_premis_element_div_div_file_contentid(self):
        validationResult, report = validate(self.rules, self.SOURCES_PATH+"mets_structmap_premis_element/mets_structmap_premis_element_div_div_file_contentid_not_exists.xml")
        self.assertTrue(validationResult==True)

    def test_csip105_check_structmap_premis_element_div_div_representation(self):
        validationResult, report = validate(self.rules, self.SOURCES_PATH+"mets_structmap_premis_element/mets_structmap_premis_element_div_div_representation_not_exists.xml")
        self.assertTrue(validationResult==True)

    def test_csip106_check_structmap_premis_element_div_div_representation_id(self):
        validationResult, report = validate(self.rules, self.SOURCES_PATH+"mets_structmap_premis_element/mets_structmap_premis_element_div_div_representation_id_not_exists.xml")
        self.assertTrue(validationResult==True)

    def test_csip107_check_structmap_premis_element_div_div_representation_label(self):
        validationResult, report = validate(self.rules, self.SOURCES_PATH+"mets_structmap_premis_element/mets_structmap_premis_element_div_div_representation_label_not_exists.xml")
        self.assertTrue(validationResult==True)

    def test_csip108_check_structmap_premis_element_div_div_representation_contentid(self):
        validationResult, report = validate(self.rules, self.SOURCES_PATH+"mets_structmap_premis_element/mets_structmap_premis_element_div_div_representation_contentid_not_exists.xml")
        self.assertTrue(validationResult==True)

    def test_csip109_check_structmap_premis_element_div_div_representation_mptr(self):
        validationResult, report = validate(self.rules, self.SOURCES_PATH+"mets_structmap_premis_element/mets_structmap_premis_element_div_div_representation_mptr_not_exists.xml")
        self.assertTrue(validationResult==True)

    def test_csip110_check_structmap_premis_element_div_div_representation_mptr_href(self):
        validationResult, report = validate(self.rules, self.SOURCES_PATH+"mets_structmap_premis_element/mets_structmap_premis_element_div_div_representation_mptr_not_exists.xml")
        self.assertTrue(validationResult==True)

    def test_csip111_check_structmap_premis_element_div_div_representation_mptr_type(self):
        validationResult, report = validate(self.rules, self.SOURCES_PATH+"mets_structmap_premis_element/mets_structmap_premis_element_div_div_representation_mptr_type_not_exists.xml")
        self.assertTrue(validationResult==True)

    def test_csip112_check_structmap_premis_element_div_div_representation_mptr_loctype(self):
        validationResult, report = validate(self.rules, self.SOURCES_PATH+"mets_structmap_premis_element/mets_structmap_premis_element_div_div_representation_mptr_loctype_not_exists.xml")
        self.assertTrue(validationResult==True)
