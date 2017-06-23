#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(
    name="chrReplace",
    version='0.0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'chrReplace = chr_replace:main',
        ],
    },
    install_requires=[
        'pandas',
    ],
    license="GPL"
)
