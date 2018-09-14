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


def main():
    # Example adapted from http://lxml.de/validation.html#id2

    # Schema
    f = io.StringIO('''\
    <schema xmlns="http://purl.oclc.org/dsdl/schematron" >
    <pattern id="sum_equals_100_percent">
    <title>Sum equals 100%.</title>
    <rule context="Total">
    <assert test="sum(//Percent)=100">Sum is not 100%.</assert>
    </rule>
    </pattern>
    </schema>
    ''')

    # Parse schema
    sct_doc = etree.parse(f)
    schematron = isoschematron.Schematron(sct_doc, store_report = True)

    # XML to validate - validation will fail because sum of numbers
    # not equal to 100
    notValid = io.StringIO('''\
        <Total>
        <Percent>30</Percent>
        <Percent>30</Percent>
        <Percent>50</Percent>
        </Total>
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

main()
