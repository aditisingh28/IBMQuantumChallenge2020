from qiskit import QuantumCircuit, execute, Aer
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# n qubits as the input q, n bits as the output b
n = 8
n_q = n
n_b = n
# output of a quantum circuit
qc_output = QuantumCircuit(n_q,n_b)

# add a measurement to qubit j and write the output to bit j
# question: do we always need to write outputs in bits? can't they be in qubits as well?
# NOTE: this DOESNT execute the measurement. It just connects the measurement gates
for j in range(n):
    qc_output.measure(j,j)

# this is how the circuit looks like now
qc_output.draw()

# now, execute the circuit. The signature to execute is:
#     execute(experiments, backend)
# where:
# experiments - a single circuit or a list of circuits
# backend: the backend to use (can be a simulator or a real QM)
# it returns a job as the execution is done async
job = execute(qc_output, Aer.get_backend('qasm_simulator'))
counts = job.result().get_counts()
plot_histogram(counts)
plt.show()