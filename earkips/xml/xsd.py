"""
  Module to handle XML Schema validation.
"""
#!/usr/bin/python
# coding=UTF-8
#
# E-ARK Information Package Validation
# Copyright (C) 2017
# All rights reserved.
#
# This code is distributed under the terms of the GNU General Public
# License, Version 3. See the text file "COPYING" for further details
# about the terms of this license.
#
import os

from lxml import etree

THIS_DIR = os.path.dirname(os.path.realpath(__file__))

def _load_mets_schema():
    schema_doc = etree.parse(_to_schema_dir('xmllint-pack.xsd'))
    return etree.XMLSchema(schema_doc)

def _to_schema_dir(file_name):
    return os.path.join(THIS_DIR, "schema", file_name)

class MetsValidator():
    """Performs METS schema validation."""
    def __init__(self):
        self._schema = _load_mets_schema()

    @property
    def schema(self):
        """Return the validator type."""
        return self._schema

    def is_valid(self, mets_file_like):
        """ Validate a METS file like object against the schema. """
        doc = etree.parse(mets_file_like)
        try:
            self.schema.assertValid(doc)
        except etree.DocumentInvalid as valid_excep:
            return False, str(valid_excep)
        return True, "valid"
