#!/usr/bin/python
# coding=UTF-8
#
# METS Validator Portal
# Copyright (C) 2017
# All rights reserved.
#
# This code is distributed under the terms of the GNU General Public
# License, Version 3. See the text file "COPYING" for further details
# about the terms of this license.

# The main details of a specification that can be used for conformance checking.

class SpecificationDetails:

    # Name and Version can be combined to make a unique key for multi specification
    # A unique name for the specification, e.g. E-ARK CSIP in String format
    name = ""

    # The version of the specification. In time, We may want a more sophisticated
    # structure behind version, e.g. int major, int minor, int patchNo, String qualifier
    # so we can easily make comparisons. Version is in String format
    version = ""

    # A URL for the specification site or location in a String format
    location = ""

    # A more detailed textual description of the specification in a String format
    description = ""

    # parameters are in String format
    def set_details(self, name, version, location, description):
        self.name = name
        self.version = version
        self.location = location
        self.description = description

    def describe(self):
        print 'Specification details - name: %s, version: %s, location: %s, description: %s' % (self.name, self.version, self.location, self.description)

def main():

    # test code
    pass

# this means that if this script is executed, then 
# main() will be executed
if __name__ == '__main__':
    main()
