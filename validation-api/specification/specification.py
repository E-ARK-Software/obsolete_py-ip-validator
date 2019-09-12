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

# The full specification, including rules.

import validation

class Specification:

    # The spec details in format SpecificationDetails
    details = []

    # The set of validation rules associated with the specification in format Set<ValidationRule>
    rules = []

    def get_details(self):
        return self.details

    # parameter in String format
    def is_supported(self, name, version):
        for detail in self.details:
            #print (detail.describe())
	        if detail.name == name and detail.version == version:
                    return True
        return False


    def get_rules():
        return self.rules

    # in SpecificationDetails format
    def add_detail(self, specification_detail):
        self.details.append(specification_detail)
        #self.details = self.details + specification_detail

    # in ValidationRule format
    def add_rule(self, rule):
        #self.rules.append(rule)
        self.rules = self.rules + rule

    def describe(self):
        print('Specification - details name: %s, details number: %d, rules number: %d' % self.details[0].name, len(self.details), len(self.rules))


def main():

    # test code
    pass

# this means that if this script is executed, then
# main() will be executed
if __name__ == '__main__':
    main()
