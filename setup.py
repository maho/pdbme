#!/usr/bin/python3

import os
from distutils.core import setup
from io import open


here = os.path.abspath(os.path.dirname(__file__))
try:
    README = open(os.path.join(here, 'README.md'), encoding='utf8').read()
    CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()
except IOError:
    README = CHANGES = ''


setup(
    name="pdbme",
    version="0.0.1",
    description="remote pdb which connects to developer",
    long_description=README + "\n\n" + CHANGES,
    author="Łukasz Mach",
    author_email="maho@pagema.net",
    url="http://github.com/mahomahomaho/pdbme",
    packages=["pdbme", "pdbme.arpdb"],
    classifiers=[
        "Development Status :: A - Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: ISC License (ISCL)",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 2.5",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.0",
        "Programming Language :: Python :: 3.1",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.7",
        "Topic :: Software Development :: Debuggers",
    ],
    requires=['click'],
    scripts=['scripts/pdbme-cli']
)
