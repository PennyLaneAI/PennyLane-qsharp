.. _installation:

Installation and setup
######################


Dependencies
============

.. highlight:: bash

PennyLane Q# requires the following libraries be installed:

* `Python <http://python.org/>`_ >=3.6
* `IQ# <https://docs.microsoft.com/en-us/quantum/install-guide/index?view=qsharp-preview>`_

as well as the following Python packages:

* `PennyLane <http://pennylane.readthedocs.io/>`_
* `qsharp <https://docs.microsoft.com/en-us/quantum/install-guide/python?view=qsharp-preview>`_

If you currently do not have Python 3 installed, we recommend `Anaconda for Python 3 <https://www.anaconda.com/download/>`_, a distributed version of Python packaged for scientific computation.


Installation
============

Follow the links above to install Python 3.6 or above, as well as the IQ# .NET package.

One complete, installation of PennyLane Q#, as well as all required Python packages
mentioned above, can be installed via ``pip``:
::

   	$ python -m pip install pennylane-qsharp


Make sure you are using the Python 3 version of pip.

Alternatively, you can install PennyLane Q# from the source code by navigating to the top directory and running
::

	$ python setup.py install


Software tests
==============

To ensure that PennyLane Q# is working correctly after installation, the test suite can be run by navigating to the source code folder and running
::

	$ make test


Documentation
=============

To build the HTML documentation, go to the top-level directory and run
::

  $ make docs

The documentation can then be found in the :file:`doc/_build/html/` directory.
