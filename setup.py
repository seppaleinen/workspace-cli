#!/usr/local/bin/python3

import os
from setuptools import setup


# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name = "workspace-cli",
    version = "0.0.1",
    author = "David Eriksson",
    author_email = "davidbaeriksson@gmail.com",
    description = ("A way to maintain git workspace"),
    license = "BSD",
    keywords = "git workspace maintain",
    url = "https://github.com/seppaleinen/workspace-cli",
    packages=[],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 1 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
    install_requires=['click', 'gitpython'],
    scripts=['cli.py'],
    entry_points={
        'console_scripts': [
            'cli = cli:cli',
        ],
    },
)
