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
from setuptools import setup

setup(
    name='mets-validator',
    packages=['metsvalidator'],
    include_package_data=True,
    install_requires=[
        'lxml==3.7.3'
    ],
)
