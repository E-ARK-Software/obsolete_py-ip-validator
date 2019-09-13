"""
    Library functions for handling Schematron checking.
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
from lxml import isoschematron
from lxml import etree

THIS_DIR = os.path.dirname(os.path.realpath(__file__))

def _load_schematron_doc(file_like):
    schematron_doc = etree.parse(file_like)
    return isoschematron.Schematron(schematron_doc, store_report=True)

def _to_schema_dir(file_name):
    return os.path.join(THIS_DIR, "schema", file_name)

def _schematron_dir():
    return os.path.join(THIS_DIR, "../../schematron")

def _schematron_file(name):
    return os.path.join(_schematron_dir(), "mets_" + name + "_rules.xml")

class SchmematronValidator():
    """Performs schematron validation."""
    def __init__(self, schematron):
        self._schematron = _load_schematron_doc(schematron)

    def is_valid(self, file_like):
        """ Validate a file like object against the schematron rules. """
        doc = etree.parse(file_like)
        is_valid = self.schematron.validate(doc)
        return is_valid, self.schematron.validation_report

    @property
    def schematron(self):
        """Return the schematron document used by validator"""
        return self._schematron

class IpSchematronValidator():
    """Class that loads different schematron validators."""
    rule_names = ['amd', 'dmd', 'file', 'hdr', 'root', 'structmap']
    def __init__(self):
        self._ruleset = _rules_dict(self.rule_names)

    @property
    def ruleset(self):
        """Return the ruleset for debugging."""
        return self._ruleset

    def validate(self, to_validate):
        """Validate a file against the schematron validators."""
        reports = {}
        valid = True
        for _rule in self._ruleset:
            is_valid, report = self._ruleset[_rule].is_valid(to_validate)
            if not is_valid:
                reports[_rule] = report
                valid = False
        return valid, reports

    @classmethod
    def schematron_paths(cls):
        """Generator that yields the paths of the schematron files."""
        for name in cls.rule_names:
            yield _schematron_file(name)

def _rules_dict(names):
    _ruleset = {}
    for name in names:
        _ruleset[name] = SchmematronValidator(_schematron_file(name))
    return _ruleset
