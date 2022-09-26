PennyLane Q# Plugin
###################

:Release: |release|

.. image:: _static/puzzle_qsharp.png
    :align: center
    :width: 70%
    :target: javascript:void(0);

|

.. include:: ../README.rst
  :start-after:	header-start-inclusion-marker-do-not-remove
  :end-before: header-end-inclusion-marker-do-not-remove

Once PennyLane-Q# is installed, the provided Q# devices can be accessed straight
away in PennyLane, without the need to import any additional packages.


Devices
~~~~~~~

Currently, PennyLane-Q# provides one Q# device for PennyLane:

.. title-card::
    :name: 'microsoft.QuantumSimulator'
    :description: Q#'s simulator backend.
    :link: devices/quantum_simulator.html

.. raw:: html

        <div style='clear:both'></div>
        </br>

Tutorials
~~~~~~~~~

To see the PennyLane-Q# plugin in action, you can use any of the qubit based `demos
from the PennyLane documentation <https://pennylane.ai/qml/demonstrations.html>`_, for example
the tutorial on `qubit rotation <https://pennylane.ai/qml/demos/tutorial_qubit_rotation.html>`_,
and simply replace ``'default.qubit'`` with any of the available ProjectQ devices, such as
``'microsoft.QuantumSimulator'``:

.. code-block:: python

    dev = qml.device('microsoft.QuantumSimulator', wires=XXX)


.. toctree::
   :maxdepth: 2
   :titlesonly:
   :hidden:

   installation
   support

.. toctree::
   :maxdepth: 2
   :caption: Usage
   :hidden:

   devices/quantum_simulator

.. toctree::
   :maxdepth: 1
   :caption: API
   :hidden:

   code
