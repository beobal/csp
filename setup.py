#!/usr/bin/env python

from distutils.core import setup
from os.path import abspath, join, dirname

setup(
    name='csp',
    version='1.0',
    description='Cassandra Snapshot Publisher',
    long_description=open(abspath(join(dirname(__file__), 'README'))).read(),
    author='Sam Tunnicliffe',
    author_email='sam@datastax.com',
    url='https://github.com/beobal/csp',
    packages=[],
    scripts=['csp'],
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
    ],
)
