from qiskit import QuantumCircuit, execute, Aer
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

def get_measurement_circuit():
    # output of a quantum circuit
    qc_measure = QuantumCircuit(4,2)

    # extract outputs
    qc_measure.measure(2,0) # extract XOR value
    qc_measure.measure(3,1) # extract AND value

    # return this circuit
    return qc_measure

def get_starting_qubits(a,b):
    qc_ha = QuantumCircuit(4)
    # encode inputs in qubits 0 and 1
    if a==1:
        qc_ha.x(0) # For a=0, remove the this line. For a=1, leave it.
    if b==1:
        qc_ha.x(1) # For b=0, remove the this line. For b=1, leave it.
    qc_ha.barrier()
    return qc_ha

def get_half_adder():
    qc_ha = QuantumCircuit(4)
    # use cnots to write the XOR of the inputs on qubit 2
    qc_ha.cx(0,2)
    qc_ha.cx(1,2)
    # use ccx to write the AND of the inputs on qubit 3
    qc_ha.ccx(0,1,3)
    qc_ha.barrier()
    return qc_ha

# Create the half-adder adding all three stages
qc = get_starting_qubits(1,1) + get_half_adder() + get_measurement_circuit()

# this is how the circuit looks like now
qc.draw()
# this is to draw with matplotlib
# qc.draw(output='mpl',justify='none')

# now, execute the circuit
job = execute(qc, Aer.get_backend('qasm_simulator'))
counts = job.result().get_counts()
plot_histogram(counts)
plt.show()