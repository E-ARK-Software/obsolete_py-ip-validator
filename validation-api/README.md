* This package comprises a validation command line API.
 
Example usage: 

python validation_api.py -t <all> <-a path1> <-s path2> <-r path3>

The type of the query <-t> selects associated API method - one of the following:

all, getspec, getspecs, getspecsummaries, issupported, getversion, validate

For these method related parameter are possible if required:

-a is the path to the archive package in XML format
-s is the path to the specification file in XML format
-r is the path to the rules file in XML format
-n is the name of the specification
-v is the version of the specification



Specifications and specifications summaries are loaded automatically from the DILCIS repository
https://github.com/DILCISBoard/E-ARK-CSIP into main project directory "py-ip-validator", using command:

py-ip-validator$ git clone https://github.com/DILCISBoard/E-ARK-CSIP.git

** The xml structure is provided in examples.md files e.g. amdsec specification:

E-ARK-CSIP/specification/implementation/metadata/mets/amdsec/examples.md 


** Validation rules are loaded from the validator sources e.g. amdsec validator:

sources/mets_administrative_metadata_premis_validator.xml


** Archive package (positive and negative samples) are loaded from the validator sources e.g. amdsec positive sample:
 
sources/mets_administrative_metadata_premis_element/mets_administrative_metadata_premis_element_ok.xml


** Resulting example for the testing of validation API command line interface:

python validation_api.py -t all -a ../sources/mets_administrative_metadata_premis_element/mets_administrative_metadata_premis_element_ok.xml -s ../E-ARK-CSIP/specification/implementation/metadata/mets/amdsec/examples.md -r ../sources/mets_administrative_metadata_premis_validator.xml
