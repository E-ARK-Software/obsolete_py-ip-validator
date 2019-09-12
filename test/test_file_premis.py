"""
    Unit tests for PREMIS elements.
"""
from test.base import Base
from metsvalidator.mets_validator_impl import validate

# In this class we test first the correct mets file metadata element in
# PREMIS format and then different error samples.
# If validation error was detected - validation result should be False.
class MetsFileMetadataPremisTestCase(Base):
    """ Tests for METS file metadata premis element """

    def test_load_rules(self):
        result, _ = validate(self.rules, self.make_resource_path("mets_file_premis_element/mets_file_premis_element_ok.xml"))
        self.assertTrue(result)

    def test_csip58_check_file_premis_element(self):
        result, _ = validate(self.rules, self.make_resource_path("mets_file_premis_element/mets_file_premis_element_not_exists.xml"))
        self.assertTrue(result)

    def test_csip59_check_file_premis_element_id(self):
        result, _ = validate(self.rules, self.make_resource_path("mets_file_premis_element/mets_file_premis_element_id_not_exists.xml"))
        self.assertTrue(result)

    def test_csip60_check_file_premis_element_filegrp(self):
        result, _ = validate(self.rules, self.make_resource_path("mets_file_premis_element/mets_file_premis_element_filegrp_not_exists.xml"))
        self.assertTrue(result)

    def test_csip61_check_file_premis_element_admid(self):
        result, _ = validate(self.rules, self.make_resource_path("mets_file_premis_element/mets_file_premis_element_admid_not_exists.xml"))
        self.assertTrue(result)

    def test_csip62_check_file_premis_element_contentinformationtype(self):
        result, _ = validate(self.rules, self.make_resource_path("mets_file_premis_element/mets_file_premis_element_contentinformationtype_not_exists.xml"))
        self.assertTrue(result)

    def test_csip63_check_file_premis_element_othercontentinformationtype(self):
        result, _ = validate(self.rules, self.make_resource_path("mets_file_premis_element/mets_file_premis_element_othercontentinformationtype_not_exists.xml"))
        self.assertTrue(result)

    def test_csip64_check_file_premis_element_use(self):
        result, _ = validate(self.rules, self.make_resource_path("mets_file_premis_element/mets_file_premis_element_use_not_exists.xml"))
        self.assertTrue(result)

    def test_csip65_check_file_premis_element_grp_id(self):
        result, _ = validate(self.rules, self.make_resource_path("mets_file_premis_element/mets_file_premis_element_grp_id_not_exists.xml"))
        self.assertTrue(result)

    def test_csip66_check_file_premis_element_grp_file(self):
        result, _ = validate(self.rules, self.make_resource_path("mets_file_premis_element/mets_file_premis_element_grp_file_not_exists.xml"))
        self.assertTrue(result)

    def test_csip67_check_file_premis_element_grp_file_id(self):
        result, _ = validate(self.rules, self.make_resource_path("mets_file_premis_element/mets_file_premis_element_grp_file_id_not_exists.xml"))
        self.assertTrue(result)

    def test_csip68_check_file_premis_element_grp_file_mimetype(self):
        result, _ = validate(self.rules, self.make_resource_path("mets_file_premis_element/mets_file_premis_element_grp_file_mimetype_not_exists.xml"))
        self.assertTrue(result)

    def test_csip69_check_file_premis_element_grp_file_size(self):
        result, _ = validate(self.rules, self.make_resource_path("mets_file_premis_element/mets_file_premis_element_grp_file_size_not_exists.xml"))
        self.assertTrue(result)

    def test_csip70_check_file_premis_element_grp_file_created(self):
        result, _ = validate(self.rules, self.make_resource_path("mets_file_premis_element/mets_file_premis_element_grp_file_created_not_exists.xml"))
        self.assertTrue(result)

    def test_csip71_check_file_premis_element_grp_file_checksum(self):
        result, _ = validate(self.rules, self.make_resource_path("mets_file_premis_element/mets_file_premis_element_grp_file_checksum_not_exists.xml"))
        self.assertTrue(result)

    def test_csip72_check_file_premis_element_grp_file_checksum_type(self):
        result, _ = validate(self.rules, self.make_resource_path("mets_file_premis_element/mets_file_premis_element_grp_file_checksum_type_not_exists.xml"))
        self.assertTrue(result)

    def test_csip73_check_file_premis_element_grp_file_owner_id(self):
        result, _ = validate(self.rules, self.make_resource_path("mets_file_premis_element/mets_file_premis_element_grp_file_owner_id_not_exists.xml"))
        self.assertTrue(result)

    def test_csip74_check_file_premis_element_grp_file_adm_id(self):
        result, _ = validate(self.rules, self.make_resource_path("mets_file_premis_element/mets_file_premis_element_grp_file_adm_id_not_exists.xml"))
        self.assertTrue(result)

    def test_csip75_check_file_premis_element_grp_file_dmd_id(self):
        result, _ = validate(self.rules, self.make_resource_path("mets_file_premis_element/mets_file_premis_element_grp_file_dmd_id_not_exists.xml"))
        self.assertTrue(result)

    def test_csip76_check_file_premis_element_grp_file_flocat(self):
        result, _ = validate(self.rules, self.make_resource_path("mets_file_premis_element/mets_file_premis_element_grp_file_flocat_not_exists.xml"))
        self.assertTrue(result)

    def test_csip77_check_file_premis_element_grp_file_flocat_loctype(self):
        result, _ = validate(self.rules, self.make_resource_path("mets_file_premis_element/mets_file_premis_element_grp_file_flocat_loctype_not_exists.xml"))
        self.assertTrue(result)

    def test_csip78_check_file_premis_element_grp_file_flocat_type(self):
        result, _ = validate(self.rules, self.make_resource_path("mets_file_premis_element/mets_file_premis_element_grp_file_flocat_xlink_type_not_exists.xml"))
        self.assertTrue(result)

    def test_csip79_check_file_premis_element_grp_file_flocat_loctype(self):
        result, _ = validate(self.rules, self.make_resource_path("mets_file_premis_element/mets_file_premis_element_grp_file_flocat_xlink_href_not_exists.xml"))
        self.assertTrue(result)
