# https://www.youtube.com/watch?v=0RPFWZj7Jm0
from qiskit import *
import matplotlib.pyplot as plt
import numpy as np

"""
We are going to flip the sign of the input if it is the winner.
In this case, to encode the winner as qubits, we are going to encode it
as the state 11
"""

# define the oracle circuit
oracle = QuantumCircuit(2,name='oracle')
# the Controlled-Z (CZ) gate flips the sign of the state if control=1
# cz(control, target).
oracle.cz(0,1)
oracle.to_gate()
oracle.draw()

# Now, we move to the Belle's basis with the Haddamard gate to perform
# quantum computations:
# h(qubit)
# qubit = index of qubit to prepare with Hadamard. In this case, [0,1]
# means a (different) Hadamard will be added to qubit0 and qubit1
backend = Aer.get_backend("statevector_simulator")
grover_circ = QuantumCircuit(2,2)
grover_circ.h([0,1])
# and qubits [0,1] will be added as an input to oracle
grover_circ.append(oracle, [0,1])
grover_circ.draw()

# execute this circuit
job = execute(grover_circ, backend)
result = job.result()
# and get back the state vector
sv = result.get_statevector()
np.around(sv, 2)
# At thsi pont, sv is:
# array([ 0.5+0.j,  0.5+0.j,  0.5+0.j, -0.5+0.j])
# Which can be checked just by doing Oracle*H_1*H_2*|00>

# add an amplification operator to "amplify" the probability
# of the winning state |11> because, at this point, the -1
# coefficient added in the CZ state is not measurable
reflection = QuantumCircuit(2, name='reflection')
# apply Hadamard to all qubts to bring them back to 00
reflection.h([0,1])
# apply a negative phase only to the 00 state 
reflection.z([0,1])
reflection.cz(0,1)
# transform it back to the Bell basis
reflection.h([0,1])
reflection.to_gate()
reflection.draw()

# put everything together
backend = Aer.get_backend('qasm_simulator')
grover_circ = QuantumCircuit(2,2)
# prepare in the Bell basis
grover_circ.h([0,1])
# add an oracle, which if we write the input state |s> in the 
# basis spanned by the orthogonal states |w> and |s'>, the oracle
# operator is just reflecting the state accross the |s'> "axis":
# |s> = a|w> + b|s'>
# to:
# |s> = -a|w> + b|s'> = |s1>
# NOTE: see minute 12:40 of video
grover_circ.append(oracle, [0,1])
# now, the reflection operator is doing something similar, but it is
# now just reflecting accross the |s> state, which moves it closer to
# the |w> state:
# Reflection|s1> = ( |s><s| - 1)|s1> = c|s> - |s1>
# NOTE: look at the geometric interpretation considering s,s1 as vectors 
grover_circ.append(reflection, [0,1])
# now, when we measure, as we are closer to the winning state, its
# probability is increasing, so we are most likely getting that state
# as the output
grover_circ.measure([0,1],[0,1])
# we want to get back the 11 state
job = execute(grover_circ, backend, shots=1)
result=job.result()
print(result.get_counts())