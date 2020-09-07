"""
  Unit test utilities
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

class Utils:
    """Unit test utils."""
    TEST_ROOT = os.path.dirname(os.path.realpath(__file__))

    @classmethod
    def get_resource_path(cls):
        """Return the path of the resources directory."""
        return os.path.join(cls.TEST_ROOT, "resources")

    @classmethod
    def to_resource_dir(cls, file_name):
        """Concat the resource dir to a given file name and return the full path."""
        return os.path.join(cls.get_resource_path(), file_name)

    @classmethod
    def list_resource_files(cls):
        """ Generator that lists all resource files."""
        return _list_files_in_dir(cls.get_resource_path())

    @classmethod
    def valid_mets(cls):
        """ Generator that iterates valid METS files."""
        return cls.mets_type('.valid')

    @classmethod
    def invalid_mets(cls):
        """ Generator that iterates invalid METS files."""
        return cls.mets_type('.invalid')

    @classmethod
    def mets_type(cls, mets_type):
        """ Generator that iterates a type of METS file."""
        return _list_files_in_dir(os.path.join(cls.get_resource_path(), 'mets', mets_type))

    @classmethod
    def discrete(cls):
        """ Generator that iterates a type of METS file."""
        return _list_files_in_dir(os.path.join(cls.get_resource_path(), "mets", 'discrete'))

def _list_files_in_dir(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            yield os.path.join(root, file)

def _print_reports(reports):
    for report in reports:
        print(report)
        print(reports[report])
