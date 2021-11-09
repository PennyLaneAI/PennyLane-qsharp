PennyLane Q# Plugin
###################

.. image:: https://img.shields.io/readthedocs/pennylane-qiskit.svg?logo=read-the-docs&style=popout-square
    :alt: Read the Docs
    :target: https://pennylaneqsharp.readthedocs.io

.. header-start-inclusion-marker-do-not-remove

The PennyLane Q# plugin integrates the Q# quantum computing framework with PennyLane's
quantum machine learning capabilities.

`The Microsoft Quantum Development Kit <https://www.microsoft.com/en-us/quantum/development-kit>`_ is an open-source
library for quantum programming using the .NET Q# quantum programming language. Resulting quantum programs
can be executed using built in local simulators, or via the cloud-based Azure quantum simulator.

`PennyLane <https://pennylane.readthedocs.io>`__ is a cross-platform Python library for quantum machine
learning, automatic differentiation, and optimization of hybrid quantum-classical computations.

.. header-end-inclusion-marker-do-not-remove

The documentation can be found `here <https://pennylane-qsharp.readthedocs.io>`_.

Features
========

* Provides a Microsoft QDK device to be used with PennyLane: ``microsoft.QuantumSimulator``.
  This provides access to the local full state simulator.


* All provided devices support all core qubit PennyLane operations and observables.


* Provides custom PennyLane operations to cover additional Q# operations, including
  ``T``, ``S``, ``ISWAP``, ``CCNOT``, ``PSWAP``, and many more. Every custom operation
  supports analytic differentiation.


* Combine Microsoft Azure quantum simulators with PennyLane's automatic differentiation and optimization.

.. installation-start-inclusion-marker-do-not-remove

Installation
============

 Installation of this plugin, as well as all dependencies, can be done using ``pip``:

   	$ python -m pip install pennylane-qsharp


Make sure you are using the Python 3 version of pip.

Alternatively, you can install PennyLane Q# from the source code by navigating to the top directory and running
::

	$ python setup.py install

Dependencies
~~~~~~~~~~~~

PennyLane Q# requires the following libraries be installed:

* `Python <http://python.org/>`_ >= 3.6
* `IQ# <https://docs.microsoft.com/en-us/quantum/install-guide/index?view=qsharp-preview>`_

as well as the following Python packages:

* `PennyLane <http://pennylane.readthedocs.io/>`__ >= 0.11.0
* `Q# <https://docs.microsoft.com/en-us/quantum/install-guide/python?view=qsharp-preview>`_

If you currently do not have Python 3 installed, we recommend
`Anaconda for Python 3 <https://www.anaconda.com/download/>`_, a distributed version of
Python packaged for scientific computation.


Software tests
~~~~~~~~~~~~~~

To ensure that PennyLane Q# is working correctly after installation,
the test suite can be run by navigating to the source code folder and running
::

	$ make test


Documentation
~~~~~~~~~~~~~

To build the HTML documentation, go to the top-level directory and run
::

  $ make docs

The documentation can then be found in the ``doc/_build/html/`` directory.

.. installation-end-inclusion-marker-do-not-remove


Contributing
============

We welcome contributions - simply fork the PennyLane-Q# repository, and then make a
`pull request <https://help.github.com/articles/about-pull-requests/>`_ containing your contribution.

All contributers to PennyLane-Q# will be listed as authors on the releases.

We also encourage bug reports, suggestions for new features and enhancements, and even links to cool projects or
applications built on PennyLane and the Microsoft QDK.


Authors
=======

PennyLane-Q# is the work of `many contributors <https://github.com/XanaduAI/PennyLane-qsharp/graphs/contributors>`_.

If you are doing research using PennyLane and PennyLane-Q#, please cite `our paper <https://arxiv.org/abs/1811.04968>`_:

    Ville Bergholm, Josh Izaac, Maria Schuld, Christian Gogolin, M. Sohaib Alam, Shahnawaz Ahmed,
    Juan Miguel Arrazola, Carsten Blank, Alain Delgado, Soran Jahangiri, Keri McKiernan, Johannes Jakob Meyer,
    Zeyue Niu, Antal Száva, and Nathan Killoran.
    *PennyLane: Automatic differentiation of hybrid quantum-classical computations.* 2018. arXiv:1811.04968

.. support-start-inclusion-marker-do-not-remove

Support
=======

- **Source Code:** https://github.com/XanaduAI/pennylane-qsharp
- **Issue Tracker:** https://github.com/XanaduAI/pennylane-qsharp/issues
- **PennyLane Forum:** https://discuss.pennylane.ai

If you are having issues, please let us know by posting the issue on our Github issue tracker, or
by asking a question in the forum.

.. support-end-inclusion-marker-do-not-remove

License
=======

PennyLane-Q# is **free** and **open source**, released under the Apache License, Version 2.0.
