from base import Base
from metsvalidator.mets_validator_impl import validate

# In this class we test first the correct mets file metadata element in PREMIS format and then different error samples. 
# If validation error was detected - validation result should be False.
class MetsFileMetadataPremisTestCase(Base):
    """ Tests for METS file metadata premis element """

    def test_load_rules(self):
        validationResult, report = validate(self.rules, self.SOURCES_PATH+"mets_file_premis_element/mets_file_premis_element_ok.xml")
        self.assertTrue(validationResult==True)

    def test_csip58_check_file_premis_element(self):
        validationResult, report = validate(self.rules, self.SOURCES_PATH+"mets_file_premis_element/mets_file_premis_element_not_exists.xml")
        self.assertTrue(validationResult==True)

    def test_csip59_check_file_premis_element_id(self):
        validationResult, report = validate(self.rules, self.SOURCES_PATH+"mets_file_premis_element/mets_file_premis_element_id_not_exists.xml")
        self.assertTrue(validationResult==True)

    def test_csip60_check_file_premis_element_filegrp(self):
        validationResult, report = validate(self.rules, self.SOURCES_PATH+"mets_file_premis_element/mets_file_premis_element_filegrp_not_exists.xml")
        self.assertTrue(validationResult==True)

    def test_csip61_check_file_premis_element_admid(self):
        validationResult, report = validate(self.rules, self.SOURCES_PATH+"mets_file_premis_element/mets_file_premis_element_admid_not_exists.xml")
        self.assertTrue(validationResult==True)

    def test_csip62_check_file_premis_element_contentinformationtype(self):
        validationResult, report = validate(self.rules, self.SOURCES_PATH+"mets_file_premis_element/mets_file_premis_element_contentinformationtype_not_exists.xml")
        self.assertTrue(validationResult==True)

    def test_csip63_check_file_premis_element_othercontentinformationtype(self):
        validationResult, report = validate(self.rules, self.SOURCES_PATH+"mets_file_premis_element/mets_file_premis_element_othercontentinformationtype_not_exists.xml")
        self.assertTrue(validationResult==True)

    def test_csip64_check_file_premis_element_use(self):
        validationResult, report = validate(self.rules, self.SOURCES_PATH+"mets_file_premis_element/mets_file_premis_element_use_not_exists.xml")
        self.assertTrue(validationResult==True)

    def test_csip65_check_file_premis_element_grp_id(self):
        validationResult, report = validate(self.rules, self.SOURCES_PATH+"mets_file_premis_element/mets_file_premis_element_grp_id_not_exists.xml")
        self.assertTrue(validationResult==True)

    def test_csip66_check_file_premis_element_grp_file(self):
        validationResult, report = validate(self.rules, self.SOURCES_PATH+"mets_file_premis_element/mets_file_premis_element_grp_file_not_exists.xml")
        self.assertTrue(validationResult==True)

    def test_csip67_check_file_premis_element_grp_file_id(self):
        validationResult, report = validate(self.rules, self.SOURCES_PATH+"mets_file_premis_element/mets_file_premis_element_grp_file_id_not_exists.xml")
        self.assertTrue(validationResult==True)

    def test_csip68_check_file_premis_element_grp_file_mimetype(self):
        validationResult, report = validate(self.rules, self.SOURCES_PATH+"mets_file_premis_element/mets_file_premis_element_grp_file_mimetype_not_exists.xml")
        self.assertTrue(validationResult==True)

    def test_csip69_check_file_premis_element_grp_file_size(self):
        validationResult, report = validate(self.rules, self.SOURCES_PATH+"mets_file_premis_element/mets_file_premis_element_grp_file_size_not_exists.xml")
        self.assertTrue(validationResult==True)

    def test_csip70_check_file_premis_element_grp_file_created(self):
        validationResult, report = validate(self.rules, self.SOURCES_PATH+"mets_file_premis_element/mets_file_premis_element_grp_file_created_not_exists.xml")
        self.assertTrue(validationResult==True)

    def test_csip71_check_file_premis_element_grp_file_checksum(self):
        validationResult, report = validate(self.rules, self.SOURCES_PATH+"mets_file_premis_element/mets_file_premis_element_grp_file_checksum_not_exists.xml")
        self.assertTrue(validationResult==True)

    def test_csip72_check_file_premis_element_grp_file_checksum_type(self):
        validationResult, report = validate(self.rules, self.SOURCES_PATH+"mets_file_premis_element/mets_file_premis_element_grp_file_checksum_type_not_exists.xml")
        self.assertTrue(validationResult==True)

    def test_csip73_check_file_premis_element_grp_file_owner_id(self):
        validationResult, report = validate(self.rules, self.SOURCES_PATH+"mets_file_premis_element/mets_file_premis_element_grp_file_owner_id_not_exists.xml")
        self.assertTrue(validationResult==True)

    def test_csip74_check_file_premis_element_grp_file_adm_id(self):
        validationResult, report = validate(self.rules, self.SOURCES_PATH+"mets_file_premis_element/mets_file_premis_element_grp_file_adm_id_not_exists.xml")
        self.assertTrue(validationResult==True)

    def test_csip75_check_file_premis_element_grp_file_dmd_id(self):
        validationResult, report = validate(self.rules, self.SOURCES_PATH+"mets_file_premis_element/mets_file_premis_element_grp_file_dmd_id_not_exists.xml")
        self.assertTrue(validationResult==True)

    def test_csip76_check_file_premis_element_grp_file_flocat(self):
        validationResult, report = validate(self.rules, self.SOURCES_PATH+"mets_file_premis_element/mets_file_premis_element_grp_file_flocat_not_exists.xml")
        self.assertTrue(validationResult==True)

    def test_csip77_check_file_premis_element_grp_file_flocat_loctype(self):
        validationResult, report = validate(self.rules, self.SOURCES_PATH+"mets_file_premis_element/mets_file_premis_element_grp_file_flocat_loctype_not_exists.xml")
        self.assertTrue(validationResult==True)

    def test_csip78_check_file_premis_element_grp_file_flocat_type(self):
        validationResult, report = validate(self.rules, self.SOURCES_PATH+"mets_file_premis_element/mets_file_premis_element_grp_file_flocat_xlink_type_not_exists.xml")
        self.assertTrue(validationResult==True)

    def test_csip79_check_file_premis_element_grp_file_flocat_loctype(self):
        validationResult, report = validate(self.rules, self.SOURCES_PATH+"mets_file_premis_element/mets_file_premis_element_grp_file_flocat_xlink_href_not_exists.xml")
        self.assertTrue(validationResult==True)



