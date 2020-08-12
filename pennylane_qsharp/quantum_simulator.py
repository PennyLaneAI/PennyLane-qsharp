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
QuantumSimulator Device
=======================

**Module name:** :mod:`pennylane_qsharp.quantum_simulator`

.. currentmodule:: pennylane_qsharp.quantum_simulator

This module contains the :class:`~.QuantumSimulatorDevice` class, a PennyLane device that allows
evaluation and differentiation of Microsoft's full state simulator using PennyLane.

Classes
-------

.. autosummary::
   QuantumSimulatorDevice

Code details
~~~~~~~~~~~~
"""
import numpy as np

from .device import QSharpDevice
from ._version import __version__


class QuantumSimulatorDevice(QSharpDevice):
    r"""Microsoft Q# full state simulator for PennyLane.


    Args:
        shots (int): number of circuit evaluations/random samples used
            to estimate expectation values of observables.
        noisy (bool): set to ``True`` to add noise models to your QVM.
    """
    name = 'Microsoft Q# full state simulator device'
    short_name = 'microsoft.QuantumSimulator'

    def pre_measure(self):
        """Run the simulator"""
        # pylint: disable=attribute-defined-outside-init
        for i in range(self.shots):
            self.results.append([1-2*int(i) for i in self.qs.simulate()])

    def expval(self, observable, wires, par):
        # translate the user wire labels to device wire labels
        device_wires = self.map_wires(wires)
        return np.mean(np.array(self.results).T[device_wires.labels[0]])

    def var(self, observable, wires, par):
        # translate the user wire labels to device wire labels
        device_wires = self.map_wires(wires)
        return np.var(np.array(self.results).T[device_wires.labels[0]])
