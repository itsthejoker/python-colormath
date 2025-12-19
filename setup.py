#!/usr/bin/env python
# -*- coding: utf-8 -*-
import colormath

from setuptools import setup

LONG_DESCRIPTION = open("README.rst").read()

CLASSIFIERS = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: BSD License",
    "Natural Language :: English",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Topic :: Scientific/Engineering :: Mathematics",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Programming Language :: Python :: 3.12",
    "Programming Language :: Python :: 3.13",
    "Programming Language :: Python :: 3.14",
]

KEYWORDS = "color math conversions"

setup(
    name="colormath",
    version=colormath.VERSION,
    description="Color math and conversion library.",
    long_description=LONG_DESCRIPTION,
    author="Joe Kaufeld",
    author_email="opensource@joekaufeld.com",
    url="https://github.com/itsthejoker/python-colormath",
    download_url="http://pypi.python.org/pypi/colormath/",
    packages=["colormath"],
    platforms=["Platform Independent"],
    license="BSD",
    classifiers=CLASSIFIERS,
    keywords=KEYWORDS,
    install_requires=["numpy", "networkx>=2.0"],
    extras_require={"development": ["black", "flake8", "nose", "pre-commit", "sphinx"]},
)
