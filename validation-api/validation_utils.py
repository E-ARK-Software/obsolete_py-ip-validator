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

from xml.dom import minidom
import specification
import validation
from validation import validation_rule, validation_result

# XML field names
RULE = 'rule'
ID = 'id'
ASSERT = 'assert'
TEST = 'test'
MESSAGE = 'message'

# this method parses xml file. Path parameter is in String format
def parse_xml(path):
    return minidom.parse(path)

# this method parses rule xml file. Path parameter is in String format
def read_rules(path):
    rules = []

    xml_validation_rule = parse_xml(path)
    itemlist = xml_validation_rule.getElementsByTagName(RULE)
    print "%s: %10d" %("rules",len(itemlist))
    for item in itemlist:
        print '%s: %20s' % (ID, item.attributes[ID].value)
        print '%s: %20s' % (TEST, item.getElementsByTagName(ASSERT)[0].attributes[TEST].value)
        print '%s: %20s' % (MESSAGE, list(item.getElementsByTagName(ASSERT))[0].firstChild.data)

        validation_rule_obj = validation_rule.ValidationRule()
        validation_rule_obj.id = item.attributes[ID].value
        validation_rule_obj.level = "INFO"
        validation_rule_obj.message = list(item.getElementsByTagName(ASSERT))[0].firstChild.data
        validation_rule_obj.description = item.getElementsByTagName(ASSERT)[0].attributes[TEST].value
        rules.append(validation_rule_obj)
    return rules
    
# this method parses archive package xml file. Path parameter is in String format
def read_archive(path):

    print ("validation: read archive package")
    xml_archive = parse_xml(path)
    itemlist = xml_archive.getElementsByTagName("mets:digiprovMD")
    print "%s: %10d" %("archive items",len(itemlist))
    for item in itemlist:
        print '%s: %20s' % (ID, item.attributes["ID"].value)
        print '%s: %20s' % ("CREATED", item.attributes["CREATED"].value)
        print '%s: %20s' % ("LOCTYPE", item.getElementsByTagName("mets:mdRef")[0].attributes["LOCTYPE"].value)
        print '%s: %20s' % ("type", item.getElementsByTagName("mets:mdRef")[0].attributes["type"].value)
        print '%s: %20s' % ("href", item.getElementsByTagName("mets:mdRef")[0].attributes["href"].value)
        print '%s: %20s' % ("MDTYPE", item.getElementsByTagName("mets:mdRef")[0].attributes["MDTYPE"].value)
        print '%s: %20s' % ("MDTYPEVERSION", item.getElementsByTagName("mets:mdRef")[0].attributes["MDTYPEVERSION"].value)
        print '%s: %20s' % ("MIMETYPE", item.getElementsByTagName("mets:mdRef")[0].attributes["MIMETYPE"].value)
        print '%s: %20s' % ("SIZE", item.getElementsByTagName("mets:mdRef")[0].attributes["SIZE"].value)
        print '%s: %20s' % ("CREATED", item.getElementsByTagName("mets:mdRef")[0].attributes["CREATED"].value)
        print '%s: %20s' % ("CHECKSUM", item.getElementsByTagName("mets:mdRef")[0].attributes["CHECKSUM"].value)
        print '%s: %20s' % ("CHECKSUMTYPE", item.getElementsByTagName("mets:mdRef")[0].attributes["CHECKSUMTYPE"].value)
        print '%s: %20s' % ("LABEL", item.getElementsByTagName("mets:mdRef")[0].attributes["LABEL"].value)
    
# this method parses specification package xml file. Path parameter is in String format
def read_specification(path):

    print ("validation: read specification")
    xml_archive = parse_xml(path)
    itemlist = xml_archive.getElementsByTagName("mets:digiprovMD")
    print "%s: %10d" %("specificaton items",len(itemlist))
    for item in itemlist:
        print '%s: %20s' % (ID, item.attributes["ID"].value)
        print '%s: %20s' % ("CREATED", item.attributes["CREATED"].value)
        print '%s: %20s' % ("LOCTYPE", item.getElementsByTagName("mets:mdRef")[0].attributes["LOCTYPE"].value)
        print '%s: %20s' % ("type", item.getElementsByTagName("mets:mdRef")[0].attributes["type"].value)
        print '%s: %20s' % ("href", item.getElementsByTagName("mets:mdRef")[0].attributes["href"].value)
        print '%s: %20s' % ("MDTYPE", item.getElementsByTagName("mets:mdRef")[0].attributes["MDTYPE"].value)
        print '%s: %20s' % ("MDTYPEVERSION", item.getElementsByTagName("mets:mdRef")[0].attributes["MDTYPEVERSION"].value)
        print '%s: %20s' % ("MIMETYPE", item.getElementsByTagName("mets:mdRef")[0].attributes["MIMETYPE"].value)
        print '%s: %20s' % ("SIZE", item.getElementsByTagName("mets:mdRef")[0].attributes["SIZE"].value)
        print '%s: %20s' % ("CREATED", item.getElementsByTagName("mets:mdRef")[0].attributes["CREATED"].value)
        print '%s: %20s' % ("CHECKSUM", item.getElementsByTagName("mets:mdRef")[0].attributes["CHECKSUM"].value)
        print '%s: %20s' % ("CHECKSUMTYPE", item.getElementsByTagName("mets:mdRef")[0].attributes["CHECKSUMTYPE"].value)
        print '%s: %20s' % ("LABEL", item.getElementsByTagName("mets:mdRef")[0].attributes["LABEL"].value)

def extract_specification_name(specification_location):
   
    location_folders = specification_location.split('/')
    return location_folders[-2]


# this mathod validates archive package according to the provided specification 
# and returns ValidationResult. 
# Specification parameter is given in SpecificationDetails format. Path parameter is a String
def validate(spec, path, validation_rule_path):
    
    read_archive(path)
    #read_specification(spec.location)
    
    print 'validation rule path: %s' % (validation_rule_path)
    # call validation package
    #from base import Base
#    import sys
#    sys.path.append('../metsvalidator')
    from mets_validator_impl import validate, load_xml
    # we test a sample in PREMIS format. if validation error was detected - validation result should be False.
    rules = load_xml("../sources/mets_validator.xml") # test validation rules path
    #rules = load_xml(validation_rule_path)
    print ("read rules file for validation method", rules, path)
    res, report = validate(rules.decode('utf-8'), path)
    print (str(res), str(report))

    # report validation results
    validation_res = validation_result.ValidationResult()
    validation_res.level = "INFO" #levels[2]
    validation_res.status = "VALID"
    validation_res.passed_checks = 5
    validation_res.error_total = 0
    validation_res.warning_total = 1
    validation_res.info_total = 4
    return validation_res

def main():

    # test code
    pass

# this means that if this script is executed, then 
# main() will be executed
if __name__ == '__main__':
    main()
