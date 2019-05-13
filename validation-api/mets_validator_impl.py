#!/usr/bin/python
# coding=UTF-8
#
# METS Validator
# Copyright (C) 2017
# All rights reserved.
#
# This code is distributed under the terms of the GNU General Public
# License, Version 3. See the text file "COPYING" for further details
# about the terms of this license.
#
# CSIP1: Each CS IP Information Package MUST be included in a single physical folder (i.e. the “Information Package folder”). In other words: on the highest structural level a Common Specification IP MUST consist of one and only one folder
#
#CSIP2: The Information Package folder SHOULD be named with the ID or name of the Information Package
#
#CSIP3: The Information Package folder CAN be compressed (for example by using TAR or ZIP)
#
#CSIP4: The Information Package folder MUST include a metadata file named METS.xml, which includes information about the identity and structure of the package and its components 
#
#CSIP5: The Information Package folder MUST include a folder named metadata, which MUST include at least all metadata relevant for the whole package
#
#CSIP6: If preservation metadata are available, they SHOULD be included in sub-folder preservation
#
#CSIP7: If descriptive metadata are available, they SHOULD be included in sub-folder descriptive
#
#CSIP8: If any other metadata are available, they CAN be included in separate sub-folders, for example an additional folder named other
#
#CSIP9: The Information Package folder MUST include a folder named representations
#
#CSIP10: The representations folder MUST include a sub-folder for each individual representation (i.e. the “representation folder”) named with a string uniquely identifying the representation within the scope of the package (for example the name of the representation and/or its creation date could be good examples for an representation sub-folder) 
#
#CSIP11: The representation folder MUST include a sub-folder named data which includes all data constituting the representation 
#
#CSIP12: The representation folder CAN include a metadata file named METS.xml which includes information about the identity and structure of the representation
#
#CSIP13: The representation folder CAN include a sub-folder named metadata which CAN include all metadata about the specific representation
#
#CSIP14: The Information Package folder and representation folder CAN be extended with additional sub-folders
#
#CSIP15: We recommend including XML Schemas for all metadata in XML format into the package. These schemas SHOULD be placed into the sub-folder called schemas within the Information Package folder
#
#CSIP16: We recommend including all additional (binary) documentation about the whole package or a specific representation into the package. Such documentation SHOULD be placed into the sub-folder called documentation within the Information Package folder and/or the representation folder
#
#CSIP17: Implementers CAN add any other folders either into the Information Package folder or the representation folder

import io
from lxml import isoschematron
from lxml import etree
#from StringIO import StringIO

#def load_rules(filename):
#    print ('Loading rules from XML file:')
#    validator_rules_file = open("metsvalidator/mets_validator.xml","r")
#    validator_rules = validator_rules_file.read()
#    validator_rules_file.close()
    #print ('METS validation rules: ', validator_rules)
#    return validator_rules

def load_xml(filename):
    print ('Loading XML file:', filename)
    xml_file = open(filename,"r")
    xml_content = xml_file.read()
    xml_file.close()
    return xml_content

def validate(rules, sample_file):
    #print (rules, sample_file)
    f = io.StringIO(unicode(rules))
    
    # Parse schema
    sct_doc = etree.parse(f)
    schematron = isoschematron.Schematron(sct_doc, store_report = True)

    # XML to validate
    sample = load_xml(sample_file)
    isValid = io.StringIO(unicode(sample))

    # Parse xml
    doc = etree.parse(isValid)

    # Validate against schema
    validationResult = schematron.validate(doc)

    # Validation report
    report = schematron.validation_report

    return validationResult, report

def main():

    # Schema
    f = io.StringIO('''\
    <schema xmlns="http://purl.oclc.org/dsdl/schematron" >
    <ns prefix="csip" uri="DILCIS"/>
    <ns prefix="ead" uri="urn:isbn:1-931666-22-9"/>
    <ns prefix="mets" uri="http://www.loc.gov/METS/"/>
    <pattern id="METS_root_element_validation">
    <title>Validate METS root element.</title>
    <rule id="CSIP3-TYPE-existence" context="mets:mets">
    <assert test="@TYPE">General content type attribute does not exist.</assert>
    </rule>
    <rule id="CSIP4-CONTENTTYPESPECIFICATION-existence" context="mets:mets">
    <assert test="@csip:CONTENTTYPESPECIFICATION">Content information type attribute does not exist.</assert>
    </rule>
    </pattern>
    <pattern id="METS_root_element_value_validation">
    <rule id="CSIP4-CONTENTTYPESPECIFICATION-value" context="mets:mets">
    <assert test="(contains(string(@csip:CONTENTTYPESPECIFICATION), 'SMURFERMS') or contains(string(@csip:CONTENTTYPESPECIFICATION), 'SMURFSFSB') or contains(string(@csip:CONTENTTYPESPECIFICATION), 'SIARD1') or contains(string(@csip:CONTENTTYPESPECIFICATION), 'SIARD2') or contains(string(@csip:CONTENTTYPESPECIFICATION), 'SIARDDK') or contains(string(@csip:CONTENTTYPESPECIFICATION), 'GeoVectorGML') or contains(string(@csip:CONTENTTYPESPECIFICATION), 'GeoRasterGeotiff') or contains(string(@csip:CONTENTTYPESPECIFICATION), 'MIXED') or contains(string(@csip:CONTENTTYPESPECIFICATION), 'OTHER'))">Content information type attribute value is not known. Known values are: SMURFERMS, SMURFSFSB, SIARD1, SIARD2, SIARDDK, GeoVectorGML, GeoRasterGeotiff, MIXED, OTHER.</assert>
    </rule>
    </pattern>
    </schema>
    ''')

    # Parse schema
    sct_doc = etree.parse(f)
    schematron = isoschematron.Schematron(sct_doc, store_report = True)


    # XML to validate
    notValid = io.StringIO('''\
	<mets:mets xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
	    xmlns:mets="http://www.loc.gov/METS/" 
	    xmlns:xlink="http://www.w3.org/1999/xlink"
	    xmlns:csip="DILCIS"
	    OBJID="uuid-4422c185-5407-4918-83b1-7abfa77de182" 
	    LABEL="Sample CS IP Information Package" 
	    TYPE="Database" 
	    csip:CONTENTTYPESPECIFICATION="SIARD3" 	
	    PROFILE="http://www.eark-project.com/METS/IP.xml" 
	    xsi:schemaLocation="http://www.loc.gov/METS/ http://www.loc.gov/standards/mets/mets.xsd http://www.w3.org/1999/xlink http://www.loc.gov/standards/mets/xlink.xsd">
         </mets:mets>
        ''')

    # Parse xml
    doc = etree.parse(notValid)

    # Validate against schema
    validationResult = schematron.validate(doc)

    # Validation report
    report = schematron.validation_report

    print("is valid: " + str(validationResult))
    print(type(report))
    print(report)

#main()
