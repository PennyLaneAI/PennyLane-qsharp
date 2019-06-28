PennyLane Q# Plugin
###################

.. image:: https://img.shields.io/readthedocs/pennylane-qsharp.svg?style=for-the-badge
  :target: https://pennylane-qsharp.readthedocs.io
  :alt: Documentation

Contains the PennyLane Q# plugin. This plugin allows the full state simulator from the Microsoft Quantum Development Toolkit
devices to work with PennyLane.

`The Microsoft Quantum Development Kit <https://www.microsoft.com/en-us/quantum/development-kit>`_ is an open-source
library for quantum programming using the .NET Q# quantum programming language. Resulting quantum programs
can be executed using built in local simulators, or via the cloud-based Azure quantum simulator.

`PennyLane <https://pennylane.readthedocs.io>`_ is a machine learning library for optimization and
automatic differentiation of hybrid quantum-classical computations.


Features
========

* Provides a Microsoft QDK device to be used with PennyLane: ``microsoft.QuantumSimulator``.
  This provides access to the local full state simulator.


* All provided devices support all core qubit PennyLane operations and observables.


* Provides custom PennyLane operations to cover additional Q# operations, including
  ``T``, ``S``, ``ISWAP``, ``CCNOT``, ``PSWAP``, and many more. Every custom operation
  supports analytic differentiation.


* Combine Microsoft Azure quantum simulators with PennyLane's automatic differentiation and optimization.


Installation
============

PennyLane-qsharp requires both PennyLane and the Microsoft Quantum Development Kit. To install the
Microsoft QDK and IQ#, `see the intruction details <https://docs.microsoft.com/en-us/quantum/install-guide/index?view=qsharp-preview>`_
provided by Microsoft.

Once the QDK is installed, you can install PennyLane-qsharp via ``pip``:

.. code-block:: bash

    $ python -m pip install pennylane-qsharp


Getting started
===============

Once the PennyLane Q# plugin is installed, the provided QDK devices can be accessed straight away in PennyLane.

You can instantiate provided devices for PennyLane as follows:

.. code-block:: python

    import pennylane as qml
    dev = qml.device('microsoft.QuantumSimulator', wires=2, shots=1000)

These devices can then be used just like other devices for the definition and evaluation of QNodes within PennyLane.
For more details, refer to the PennyLane documentation.


Contributing
============

We welcome contributions - simply fork the PennyLane-qsharp repository, and then make a
`pull request <https://help.github.com/articles/about-pull-requests/>`_ containing your contribution.

All contributers to PennyLane-qsharp will be listed as authors on the releases.

We also encourage bug reports, suggestions for new features and enhancements, and even links to cool projects or
applications built on PennyLane and the Microsoft QDK.


Authors
=======

`Josh Izaac <https://github.com/josh146>`_


Support
=======

- **Source Code:** https://github.com/XanaduAI/pennylane-qsharp
- **Issue Tracker:** https://github.com/XanaduAI/pennylane-qsharp/issues

If you are having issues, please let us know by posting the issue on our Github issue tracker.


License
=======

PennyLane-qsharp is **free** and **open source**, released under the Apache License, Version 2.0.
