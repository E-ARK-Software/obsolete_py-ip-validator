# py-ip-validator
py-ip-validator

Python IP Validator Prototype
==============================
A prototype for the METS data validation. This prototype implements the structure validation defined by the following rules (CSIP1 to CSIP17):
 
https://github.com/DILCISBoard/E-ARK-CSIP/blob/master/implementation/index.md#41folder-structure-of-the-cs-ip

The implementation requirements of the CS IP Information Package structure are:

CSIP1: Each CS IP Information Package MUST be included in a single physical folder (i.e. the “Information Package folder”). In other words: on the highest structural level a Common Specification IP MUST consist of one and only one folder

CSIP2: The Information Package folder SHOULD be named with the ID or name of the Information Package

CSIP3: The Information Package folder CAN be compressed (for example by using TAR or ZIP)

CSIP4: The Information Package folder MUST include a metadata file named METS.xml, which includes information about the identity and structure of the package and its components 

CSIP5: The Information Package folder MUST include a folder named metadata, which MUST include at least all metadata relevant for the whole package

CSIP6: If preservation metadata are available, they SHOULD be included in sub-folder preservation

CSIP7: If descriptive metadata are available, they SHOULD be included in sub-folder descriptive

CSIP8: If any other metadata are available, they CAN be included in separate sub-folders, for example an additional folder named other

CSIP9: The Information Package folder MUST include a folder named representations

CSIP10: The representations folder MUST include a sub-folder for each individual representation (i.e. the “representation folder”) named with a string uniquely identifying the representation within the scope of the package (for example the name of the representation and/or its creation date could be good examples for an representation sub-folder) 

CSIP11: The representation folder MUST include a sub-folder named data which includes all data constituting the representation 

CSIP12: The representation folder CAN include a metadata file named METS.xml which includes information about the identity and structure of the representation

CSIP13: The representation folder CAN include a sub-folder named metadata which CAN include all metadata about the specific representation

CSIP14: The Information Package folder and representation folder CAN be extended with additional sub-folders

CSIP15: We recommend including XML Schemas for all metadata in XML format into the package. These schemas SHOULD be placed into the sub-folder called schemas within the Information Package folder

CSIP16: We recommend including all additional (binary) documentation about the whole package or a specific representation into the package. Such documentation SHOULD be placed into the sub-folder called documentation within the Information Package folder and/or the representation folder

CSIP17: Implementers CAN add any other folders either into the Information Package folder or the representation folder

Test cases which should be used for running the tests:
 
https://github.com/DILCISBoard/eark-ip-test-corpus/tree/master/corpus/structure/root

Pre-requisites
--------------
 - Git or a copy of the latest source code
 - MacOS or Linux. Sorry Windows isn't currently supported.
 - Python 3. Python 2 isn't supported.
 - [Python pip](https://pip.pypa.io/en/stable/) for installing Python modules.

Using virtual environments for Python will save a lot of pain and allow you to
run Python 3 and Python 2 applications in harmony. If that sounds good then read [this primer](http://docs.python-guide.org/en/latest/dev/virtualenvs/).

Quick Start
-----------
The portal is a Flask web application written in Python. It's currently easy to install as long as you have a Python 3 environment. Be aware that this is currently a local development installation, it's not ready for deployment as a reliable application to a server. We're working on that. That said there's a few stages to getting going:
1. Getting the code.
2. Setting up a Python 3 virtualenv (optional but recommended).
3. Installing the validator prototype and its dependencies.
4. Running the validator on test samples provided in https://github.com/DILCISBoard/eark-ip-test-corpus/tree/master/corpus/structure/root.

Let's take a look in a little more detail. We've provided some helper scripts for virtualenv setup, deployment and running which we'll also point you to.

### Getting the code
There's no helper script for this. Clone this repository and move into the project root directory:
````bash
$ git clone https://github.com/DILCISBoard/py-ip-validator.git
$ cd py-ip-validator
````
Alternatively download and unpack the source archive from this git repository.
````bash
$ wget https://github.com/DILCISBoard/py-ip-validator/archive/master.zip
$ unzip master.zip
$ rm master.zip
$ cd py-ip-validator-master
````
Once you've done this you can create the virtualenv for installation, or skip the next step if you have a Python 3 environment you're happy to use.

### Setting up a Python 3 virtualenv (optional)
We need to create a Python virtualenv in the project root folder in a `venv` subdirectory and activate it thus:
````bash
$ virtualenv -p python3 venv
$ source ./venv/bin/activate
````
There's a helper script in the root directory you can run instead:
`$ ./venv.sh`. If this has worked your terminal prompt should be adorned with a venv marker, e.g. `(venv) $`.

You only need to create the virtualenv once, although you can remove it by simply deleting the `venv` subdirectory. You'll need to activate the virtualenv `source ./venv/bin/activate` every time you start a new terminal session.

### Installing the application and dependencies
Installing the application is straightforward using `pip`:
````bash
(venv) $ source ./venv/bin/activate
(venv) $ pip install -e .
````
Where the `-e` switch tells pip to monitor the directory and recompile changes. This is useful for development but should be omitted for stable deployments.

Again there's a helper script for this: `(venv) $ ./setup.sh`.


### Running the application
Finally run the validator application:

````bash
(venv) $ python mets-validator/MetsValidator.py
````
There's a script that you can use for this in the project root, `run.sh`. 
Or to run unit tests `runMetsValidatorTests.sh`

For testing adjust XML samples stored in files if necessary.

This code is released under the GPLv3 license. 
