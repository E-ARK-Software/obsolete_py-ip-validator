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

# The result of checking a rule against a package

import location
import path

class CheckResult:

    # True if the check passed, false otherwise
    is_passed = True

    # Location needs design. It should be the best way of reporting the source
    # of the failure to the user, e.g. the path, line number and xpath for a METS
    # file location. I figured you might be best figuring our what actually works
    # here... Format is Location
    location = ''

    # A list of relative package paths to items related to test failure,
    # e.g. a missing package file, a file that fails hash integrity checking, etc.
    # Format is List<Path>
    related_items = []

    def describe(self):
        print("Check result:", "is passed", is_passed, "location", location)

def main():

    # test code
    pass

# this means that if this script is executed, then
# main() will be executed
if __name__ == '__main__':
    main()
