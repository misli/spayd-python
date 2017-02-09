#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from setuptools import setup, find_packages

setup(
    name            = 'spayd',
    version         = '0.1.0',
    description     = 'Python implementation of the SPAYD format',
    author          = 'Jakub Dorňák',
    author_email    = 'jakub.dornak@misli.cz',
    license         = 'BSD',
    url             = 'https://github.com/misli/spayd-python',
    packages        = find_packages(),
    install_requires=[
    ],
    classifiers     = [
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
