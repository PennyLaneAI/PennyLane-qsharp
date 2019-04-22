import os

if 'dotnet' not in os.environ['PATH']:
    os.environ['PATH'] += ":/home/josh/.dotnet/tools"

import pennylane as qml

dev = qml.device('microsoft.QuantumSimulator', wires=2)

@qml.qnode(dev)
def circuit(x, y):
    qml.RX(x, wires=0)
    qml.RY(y, wires=0)
    return qml.expval.PauliZ(0)

print(circuit(0.5, 0.1))


dev2 = qml.device('default.qubit', wires=2)

@qml.qnode(dev2)
def circuit(x, y):
    qml.RX(x, wires=0)
    qml.RY(y, wires=0)
    return qml.expval.PauliZ(0)

print(circuit(0.5, 0.1))