#!/usr/bin/env python

from distutils.core import setup

long_desc = open('README.rst').read()

setup(name='mockdoc',
    version='0.0.1',
    description='library for asserting type correctness based on doc blocks',
    long_description=long_desc,
    packages=('mockdoc',),
    license='GPLv2',
    author='Michael Hrivnak',
    author_email='mhrivnak@hrivnak.org',
    url='https://github.com/mhrivnak/mockdoc',
    classifiers=(
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries',
    )
)
