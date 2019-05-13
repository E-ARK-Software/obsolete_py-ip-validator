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

from argparse import ArgumentParser

import validation
import specification
from specification import specification_details 
from specification import specification 
import validation_utils

validation_api = None


### Validation API
class ValidationApi:

    version = "0.1"
    specifications = []
    specifications_details = []

    ### Support for multiple validators
    # Do we want to support multiple specification and validators, e.g. AIP, SIP, or
    #multiple versions from a single endpoint?
    #This means supporting concepts such as specification details
    #e.g name, URL, version, etc. but we'll need those for reporting.

    ### Specification methods

    # returns a list of supported specifications Set<Specification>
    def get_supported_specifications(self):
        return self.specifications

    # Specification format
    def set_supported_specifications(self, specification):
	self.specifications.append(specification)

    # returns a list of specification summaries Set<SpecificationDetails> 
    def get_supported_specification_summaries(self):
        return self.specifications_details

    # SpecificationDetails format 
    def set_supported_specification_summaries(self, specification_detail):
	self.specifications_details.append(specification_detail)

    # return specification of type Specification by String values
    def get_specification(self, spec_name, spec_version):
        for spec in self.specifications:
            if spec.is_supported(spec_name, spec_version):
                return spec
        return None

    # check specification of type Specification by String values. Returns a boolean result
    # True if specification is supported
    def is_supported(self, spec_name, spec_version):
        for spec in self.specifications:
            res = spec.is_supported(spec_name, spec_version)
            if res == True:
                return True
        return False

    ### Validation Methods

    # Method to validate packages in archive format. Retuns result in format ValidationResult
    #def validate(SpecificationDetails spec, InputStream packageStream):
    #    pass

    # Method to validate packages in a directory. Retuns result in format ValidationResult using 
    # SpecificationDetails and package root as a Sting
    def validate(self, spec, package_root, validation_rule_path):
        return validation_utils.validate(spec, package_root, validation_rule_path)

    ### Help methods
    def get_version(self):
        return self.version

    def create_specification(self, specification_location):
        res = None
        if specification_location is not None:
            print ("create specification details...")
            specification_detail = specification_details.SpecificationDetails()
            specification_name = validation_utils.extract_specification_name(specification_location)
            specification_detail.set_details(specification_name, '1.0', specification_location, specification_name + ' specification for testing validation API')
            validation_api.set_supported_specification_summaries(specification_detail)

            print ("create specification ...")
            specification_obj = specification.Specification()
            specification_obj.add_detail(specification_detail)
            validation_api.set_supported_specifications(specification_obj)
            res = specification_obj
        return res


def init():

    global validation_api
    validation_api = ValidationApi()
    cur_version = validation_api.get_version()
    print("started validator in version", cur_version)

    print ("read specifications ...")


def main():

    parser = ArgumentParser(description="Example usage: python validation_api.py -t all -a path1 -s path2 -r path3")
    parser.add_argument("-t", "--type", dest="type",
                    help="type of the query e.g. all, getspec, getspecs, getspecsummaries, issupported, getversion, validate")
    parser.add_argument("-a", "--archive", dest="archive",
                    help="path to the archive package in XML format")
    parser.add_argument("-s", "--spec", dest="spec",
                    help="path to the specification file in XML format")
    parser.add_argument("-r", "--rule", dest="rule",
                    help="path to the rules file in XML format")
    parser.add_argument("-n", "--name", dest="name",
                    help="name of the specification")
    parser.add_argument("-v", "--version", dest="version",
                    help="version of the specification")

    args = parser.parse_args()

    print ("args",args)

    api_type = args.type
    package_root = args.archive
    specification_location = args.spec
    validation_rule_path = args.rule
    specification_name = args.name
    specification_version = args.version

    init()
    global validation_api

    if api_type == 'all':
        specification_obj = validation_api.create_specification(specification_location)

        print ("create validation rules and add it to specification ...")
        validation_rules = validation_utils.read_rules(validation_rule_path)
        specification_obj.add_rule(validation_rules)
   
        supported_specifications = validation_api.get_supported_specifications()
        for spec in supported_specifications:
	    spec.describe()
   
        for summary in validation_api.get_supported_specification_summaries():
	    summary.describe()

        check_spec = validation_api.get_specification(supported_specifications[0].get_details()[0].name, supported_specifications[0].get_details()[0].version)
        print 'got specification: '
        print check_spec.describe()

        supported = validation_api.is_supported(supported_specifications[0].get_details()[0].name, supported_specifications[0].get_details()[0].version)
        print ("specification is supported", supported)

        print ("validate package ...")
        validation_result = validation_api.validate(supported_specifications[0].get_details()[0], package_root, validation_rule_path)
        validation_result.describe()
    elif api_type == 'getspec':
        check_spec = validation_api.get_specification(specification.name, specification.version)
        print ("got specification", check_spec.name)
    elif api_type == 'getspecs':
        supported_specifications = validation_api.get_supported_specifications()
        for spec in supported_specifications:
	    print ("supported specification", spec.describe())
    elif api_type == 'getspecsummaries':
        supported_specification_summaries = validation_api.get_supported_specification_summaries()
        for summary in validation_api.supported_specification_summaries:
	    print ("supported specification summary", summary.describe())
    elif api_type == 'issupported':
        supported = validation_api.is_supported(specification.name, specification.version)
        print ("specification is supported", supported)
    elif api_type == 'getversion':
        print '%s %10s' %("validation API version", validation_api.get_version())
    elif api_type == 'validate':
        print ("validate package ...")
        validation_result = validation_api.validate(specification, package_root)
        validation_result.describe()

# this means that if this script is executed, then 
# main() will be executed
if __name__ == '__main__':
    main()


