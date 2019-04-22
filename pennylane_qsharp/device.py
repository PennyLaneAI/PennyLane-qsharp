# Copyright 2019 Xanadu Quantum Technologies Inc.

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
Base Q# device class
====================

**Module name:** :mod:`pennylane_qsharp.device`

.. currentmodule:: pennylane_qsharp.device

This module contains a base class for constructing Q# devices for PennyLane,
as well as some auxillary functions for converting PennyLane supported operations
(such as ``BasisState``, ``Rot``) to the equivalent Q# operations.

This class provides all the boilerplate for supporting Q# devices on PennyLane.

Auxiliary functions
-------------------

.. autosummary::
    basis_state
    rotation
    controlled_phase

Classes
-------

.. autosummary::
   QSharpDevice

Code details
~~~~~~~~~~~~
"""
import abc

import numpy as np

import qsharp

from pennylane import Device

from ._version import __version__


PROGRAM = """\
namespace PennyLane.Program
{
    open Microsoft.Quantum.Canon;
    open Microsoft.Quantum.Primitive;

    operation HelloQ () : Unit {
        mutable resultArray = new Result[n];
        using (qubits = Qubit[{wires}]) {
            // operations
            {operations}

            // measurements
            {measurements}

        }
        return BoolArrFromResultArr(resultArray);
    }
}
"""


# mapping operations supported by PennyLane to the
# corresponding Q# operation
qsharp_operation_map = {
    "PauliX": 'X({wires[0]});\n',
    "PauliY": 'Y({wires[0]});\n',
    "PauliZ": 'Z({wires[0]});\n',
    "Hadamard": 'H({wires[0]});\n',
    'CNOT': 'CNOT({wires[0]}, {wires[1]});\n',
    'SWAP': 'SWAP({wires[0]}, {wires[1]});\n',
    'CZ': 'CZ({wires[0]}, {wires[1]});\n',
    'PhaseShift': 'R1({p[0]}, {wires[0]});\n',
    'RX': 'Ry({p[0]}, {wires[0]});\n',
    'RY': 'Rx({p[0]}, {wires[0]});\n',
    'RZ': 'Rz({p[0]}, {wires[0]});\n',
    'Rot': 'Rz({p[0]}, {wires[0]});\nRy({p[1]}, {wires[0]});\nRz({p[2]}, {wires[0]});\n',
    # the following gates are provided by the PL-Q# plugin
    'S': 'S({wires[0]});\n',
    'T': 'T({wires[0]});\n',
    'CCNOT': 'CNOT({wires[0]}, {wires[1]}, {wires[2]});\n',
}


qsharp_expectation_map = {
    "PauliX": 'MResetX({wires[0]});\n',
    "PauliY": 'MResetY({wires[0]});\n',
    "PauliZ": 'MResetZ({wires[0]});\n',
    "Hadamard": 'Ry(-pi/4, {wires[0]});\nMResetZ({wires[0]});\n',
    'Identity': 'MeasureIdentity({wires[0]}});\nReset({wires[0]});\n'
}


class QSharpDevice(Device):
    r"""Abstract Q# device for PennyLane.

    Args:
        wires (int): the number of modes to initialize the device in
        shots (int): Number of circuit evaluations/random samples used
            to estimate expectation values of expectations.
            For simulator devices, 0 means the exact EV is returned.
    """
    pennylane_requires = '>=0.2'
    version = __version__
    author = 'Josh Izaac'

    _operation_map = qsharp_operation_map
    _expectation_map = qsharp_expectation_map

    def __init__(self, wires, shots=1024, **kwargs):
        if shots <= 0:
            raise ValueError("Number of shots must be a positive integer.")

        super().__init__(wires, shots)
        self.reset()

    @property
    def source(self):
        """View the last evaluated Q# program"""
        return self.source

    def apply(self, operation, wires, par):
        # pylint: disable=attribute-defined-outside-init
        self.prog += self._operation_map[operation].format(*par, *wires)

    def post_apply(self): #pragma no cover
        """Compile the Q# program"""
        for e in self.expval_queue:
            self.measure += self._operation_map[operation].format(*e.parameters, *e.wires)

        self.source = PROGRAM.format(wires=self.num_wires, operations=self.prog, measurements=self.measure)
        self.qs = qsharp.compile(self.source)

    @abc.abstractmethod
    def pre_expval(self): #pragma no cover
        """Run the simulation"""
        raise NotImplementedError

    def reset(self):
        self.prog = []
        self.measure = []
        self.source = ""
        self.qs = None
        self.results = []

    @property
    def operations(self):
        return set(self._operation_map.keys())
