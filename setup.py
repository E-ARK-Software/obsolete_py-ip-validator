#!/usr/bin/python
# coding=UTF-8
#
# BitCurator Access Webtools (Disk Image Access for the Web)
# Copyright (C) 2014 - 2016
# All rights reserved.
#
# This code is distributed under the terms of the GNU General Public
# License, Version 3. See the text file "COPYING" for further details
# about the terms of this license.
#
"""Setup for METS validator app."""
from setuptools import setup, find_packages

TEST_DEPS = [
    'pre-commit',
    'pytest',
    'pylint',
    'pytest-coverage'
]
EXTRAS = {
    'testing': TEST_DEPS,
}

setup(
    name='E-ARK Information Package Validator',
    packages=find_packages(),
    version='0.1-dev',
    long_description=open('README.md').read(),
    include_package_data=True,
    install_requires=[
        'lxml==3.7.3'
    ],
    tests_requires=TEST_DEPS,
    extras_require=EXTRAS,
)
