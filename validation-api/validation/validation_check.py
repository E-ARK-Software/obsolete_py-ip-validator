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

# Couples a rule with a list of results

import validation
import definition


class ValidationCheck:

    # The rule under test in ValidationRule format
    rule = None

    # Set of results for the check. In practise will normally be pre-sorted into
    # pass and fails for use in report. Format is Set<CheckResult>
    results = []

def main():

    # test code
    pass

# this means that if this script is executed, then
# main() will be executed
if __name__ == '__main__':
    main()
