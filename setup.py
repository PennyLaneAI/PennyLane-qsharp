#!/usr/bin/env python3
import sys
import os
from setuptools import setup

with open("pennylane_qsharp/_version.py") as f:
	version = f.readlines()[-1].split()[-1].strip("\"'")


requirements = [
    "qsharp"
]


info = {
    'name': 'PennyLane-qsharp',
    'version': version,
    'maintainer': 'Xanadu Inc.',
    'maintainer_email': 'josh@xanadu.ai',
    'url': 'http://xanadu.ai',
    'license': 'Apache License 2.0',
    'packages': [
                    'pennylane_qsharp'
                ],
    'entry_points': {
        'pennylane.plugins': [
            'microsoft.QuantumSimulator = pennylane_qsharp:QuantumSimulatorDevice'
            ],
        },
    'description': 'Microsoft Quantum Development Kit backend for PennyLane',
    'long_description': open('README.rst').read(),
    'provides': ["pennylane_qsharp"],
    'install_requires': requirements
}


classifiers = [
    "Development Status :: 4 - Beta",
    "Environment :: Console",
    "Intended Audience :: Science/Research",
    "License :: OSI Approved :: Apache Software License",
    "Natural Language :: English",
    "Operating System :: POSIX",
    "Operating System :: MacOS :: MacOS X",
    "Operating System :: POSIX :: Linux",
    "Operating System :: Microsoft :: Windows",
    "Programming Language :: Python",
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3 :: Only',
    "Topic :: Scientific/Engineering :: Physics"
]


setup(classifiers=classifiers, **(info))
