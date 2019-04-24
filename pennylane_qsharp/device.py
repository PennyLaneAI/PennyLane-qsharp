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

This module contains a base class for constructing Q# devices for PennyLane.

This class provides all the boilerplate for supporting Q# devices on PennyLane.

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
operation Program () : Bool[] {{
    mutable resultArray = new Result[{wires}];
    using (q = Qubit[{wires}]) {{
        // operations
        {operations}
        // measurements
        {measurements}
    }}
    return BoolArrFromResultArr(resultArray);
}}
"""

# mapping operations supported by PennyLane to the
# corresponding Q# operation
qsharp_operation_map = {
    "PauliX": 'X(q[{wires[0]}]);\n',
    "PauliY": 'Y(q[{wires[0]}]);\n',
    "PauliZ": 'Z(q[{wires[0]}]);\n',
    "Hadamard": 'H(q[{wires[0]}]);\n',
    'CNOT': 'CNOT(q[{wires[0]}], q[{wires[1]}]);\n',
    'SWAP': 'SWAP(q[{wires[0]}], q[{wires[1]}]);\n',
    'CZ': 'CZ(q[{wires[0]}], q[{wires[1]}]);\n',
    'PhaseShift': 'R1({p[0]}, q[{wires[0]}]);\n',
    'RX': 'Ry({p[0]}, q[{wires[0]}]);\n',
    'RY': 'Rx({p[0]}, q[{wires[0]}]);\n',
    'RZ': 'Rz({p[0]}, q[{wires[0]}]);\n',
    'Rot': 'Rz({p[0]}, q[{wires[0]}]);\nRy({p[1]}, q[{wires[0]}]);\nRz({p[2]}, q[{wires[0]}]);\n',
    # the following gates are provided by the PL-Q# plugin
    'S': 'S(q[{wires[0]}]);\n',
    'T': 'T(q[{wires[0]}]);\n',
    'CCNOT': 'CNOT(q[{wires[0]}], q[{wires[1]}], q[{wires[2]}]);\n',
}


qsharp_expectation_map = {
    "PauliX": 'MResetX(q[{wires[0]}]);\n',
    "PauliY": 'MResetY(q[{wires[0]}]);\n',
    "PauliZ": 'MResetZ(q[{wires[0]}]);\n',
    "Hadamard": 'Ry(-pi/4, q[{wires[0]}]);\nMResetZ(q[{wires[0]}]);\n',
    'Identity': 'MeasureIdentity(q[{wires[0]}]});\nReset(q[{wires[0]}]);\n'
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
        return self._source_code

    def apply(self, operation, wires, par):
        # pylint: disable=attribute-defined-outside-init
        self.prog += self._operation_map[operation].format(p=par, wires=wires)
        self.prog += "            "

    def post_apply(self): #pragma no cover
        """Compile the Q# program"""
        for e in self.expval_queue:
            self.measure += "set resultArray[{wires[0]}] = ".format(wires=e.wires)
            self.measure += self._expectation_map[e.name].format(p=e.parameters, wires=e.wires)
            self.measure += "            "

        self._source_code = PROGRAM.format(wires=self.num_wires, operations=self.prog, measurements=self.measure)
        self.qs = qsharp.compile(self._source_code)

    @abc.abstractmethod
    def pre_expval(self): #pragma no cover
        """Run the simulation"""
        raise NotImplementedError

    def reset(self):
        self.prog = ""
        self.measure = ""
        self._source_code = ""
        self.qs = None
        self.results = []

    @property
    def operations(self):
        return set(self._operation_map.keys())

    @property
    def operations(self):
        """Get the supported set of operations.

        Returns:
            set[str]: the set of PennyLane operation names the device supports
        """
        return set(self._operation_map.keys())

    @property
    def expectations(self):
        """Get the supported set of expectations.

        Returns:
            set[str]: the set of PennyLane expectation names the device supports
        """
        return set(self._expectation_map.keys())
