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
    <ns prefix="csip" uri="DILCIS"/>
    <ns prefix="ead" uri="urn:isbn:1-931666-22-9"/>
    <ns prefix="mets" uri="http://www.loc.gov/METS/"/>
    <pattern id="CONTENTTYPESPECIFICATION_attribute_does_not_exist">
    <title>Validate CONTENTTYPESPECIFICATION attribute.</title>
    <rule context="mets:mets">
    <assert test="@csip:CONTENTTYPESPECIFICATION">Attribute does not exist.</assert>
    </rule>
    </pattern>
    </schema>
    ''')

#    f = io.StringIO('''\
#    <sch:schema xmlns:sch="http://purl.oclc.org/dsdl/schematron" >
#    <sch:ns prefix="ead" uri="urn:isbn:1-931666-22-9"/>
#    <sch:ns prefix="mets" uri="http://www.loc.gov/METS/"/>
#    <sch:pattern id="CONTENTTYPESPECIFICATION_attribute_does_not_exist">
#    <sch:title>Validate CONTENTTYPESPECIFICATION attribute.</sch:title>
#    <sch:rule context="mets:mets">
#    <sch:assert test="@csip:CONTENTTYPESPECIFICATION">Attribute does not exist.</sch:assert>
#    </sch:rule>
#    </sch:pattern>
#    </sch:schema>
#    ''')

    # Parse schema
    sct_doc = etree.parse(f)
    schematron = isoschematron.Schematron(sct_doc, store_report = True)

    # XML to validate - validation will fail because sum of numbers
    # not equal to 100
    notValid = io.StringIO('''\
	<mets:mets xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
	    xmlns:mets="http://www.loc.gov/METS/" 
	    xmlns:csip="DILCIS"
	    OBJID="uuid-4422c185-5407-4918-83b1-7abfa77de182" 
	    LABEL="Sample CS IP Information Package" 
	    TYPE="Database" 
	    csip:CONTENTTYPESPECIFICATION="SIARD2" 	
	    xsi:schemaLocation="http://www.loc.gov/METS/ http://www.loc.gov/standards/mets/mets.xsd http://www.w3.org/1999/xlink http://www.loc.gov/standards/mets/xlink.xsd">
         </mets:mets>
        ''')
#    notValid = io.StringIO('''\
#	<mets:mets xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
#	    xmlns:mets="http://www.loc.gov/METS/" 
#	    xmlns:csip="DILCIS"
#	    OBJID="uuid-4422c185-5407-4918-83b1-7abfa77de182" 
#	    LABEL="Sample CS IP Information Package" 
#	    TYPE="Database" 
#	    CONTENTTYPESPECIFICATION="SIARD2" 	
 #       </mets:mets>
 #      ''')
#    notValid = io.StringIO('''\
#	<!--?oxygen SCHSchema="mets_general_rules-ISO.sch"?-->
#	<mets:mets xmlns:xsi="http://www.w3.org/2001/XMLSchema#-instance" 
#	    xmlns:mets="http://www.loc.gov/METS/" 
#	    xmlns:xlink="http://www.w3.org/1999/xlink"
#	    xmlns:csip="DILCIS"
#	    OBJID="uuid-4422c185-5407-4918-83b1-7abfa77de182" 
#	    LABEL="Sample CS IP Information Package" 
#	    TYPE="Database" 
#	    csip:CONTENTTYPESPECIFICATION="SIARD2" 
#	    PROFILE="http://www.eark-project.com/METS/IP.xml" 
#	    xsi:schemaLocation="http://www.loc.gov/METS/ http://www.loc.gov/standards/mets/mets.xsd http://www.w3.org/1999/xlink http://www.loc.gov/standards/mets/xlink.xsd">
#	</mets:mets>
 #      ''')
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
