PennyLane Q# Plugin
###################

:Release: |release|
:Date: |today|



This plugin allows two Microsoft Quantum Development Toolkit
devices to work with PennyLane - the `QuantumSimulator` full state simulator, and the `ToffoliSimulator`.

`The Microsoft Quantum Development Kit <https://www.microsoft.com/en-us/quantum/development-kit>`_ is an open-source
library for quantum programming using the .NET Q# quantum programming language. Resulting quantum programs
can be executed using built in local simulators, or via the cloud-based Azure quantum simulator.

`PennyLane <https://pennylane.readthedocs.io>`_ is a machine learning library for optimization and
automatic differentiation of hybrid quantum-classical computations.



Features
========

* Provides two devices to be used with PennyLane: ``microsoft.QuantumSimulator`` and
  ``microsoft.ToffoliSimulator``. These provide access to the local full state simulator and restricted
  Toffoli simulator respectively.


* All provided devices support all core qubit PennyLane operations and expectation values.


* Provides custom PennyLane operations to cover additional Q# operations, including
  ``T``, ``S``, ``ISWAP``, ``CCNOT``, ``PSWAP``, and many more. Every custom operation
  supports analytic differentiation.


* Combine Microsoft Azure quantum simulators with PennyLane's automatic differentiation and optimization.



To get started with the PennyLane Q# plugin, follow the :ref:`installation steps <installation>`, then see the :ref:`usage <usage>` page.

Authors
=======

`Josh Izaac <https://github.com/josh146>`_

Contents
========

.. rst-class:: contents local topic

.. toctree::
   :maxdepth: 2
   :caption: Getting started

   installing
   usage

.. rst-class:: contents local topic

.. toctree::
   :maxdepth: 1
   :caption: Code details

   code/ops
   code/device
   code/quantum_simulator
   code/toffoli_simulator
