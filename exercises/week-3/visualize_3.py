# problem 10
problem_set = \
    [[['0', '2'], ['1', '0'], ['1', '2'], ['1', '3'], ['2', '0'], ['3', '3']],
    [['0', '0'], ['0', '1'], ['1', '2'], ['2', '2'], ['3', '0'], ['3', '3']],
    [['0', '0'], ['1', '1'], ['1', '3'], ['2', '0'], ['3', '2'], ['3', '3']],
    [['0', '0'], ['0', '1'], ['1', '1'], ['1', '3'], ['3', '2'], ['3', '3']],
    [['0', '2'], ['1', '0'], ['1', '3'], ['2', '0'], ['3', '2'], ['3', '3']],
    [['1', '1'], ['1', '2'], ['2', '0'], ['2', '1'], ['3', '1'], ['3', '3']],
    [['0', '2'], ['0', '3'], ['1', '2'], ['2', '0'], ['2', '1'], ['3', '3']],
    [['0', '0'], ['0', '3'], ['1', '2'], ['2', '2'], ['2', '3'], ['3', '0']],
    [['0', '3'], ['1', '1'], ['1', '2'], ['2', '0'], ['2', '1'], ['3', '3']],
    [['0', '0'], ['0', '1'], ['1', '3'], ['2', '1'], ['2', '3'], ['3', '0']],
    
    [['0', '1'], ['0', '3'], ['1', '2'], ['1', '3'], ['2', '0'], ['3', '2']],

    [['0', '0'], ['1', '3'], ['2', '0'], ['2', '1'], ['2', '3'], ['3', '1']],
    [['0', '1'], ['0', '2'], ['1', '0'], ['1', '2'], ['2', '2'], ['2', '3']],
    [['0', '3'], ['1', '0'], ['1', '3'], ['2', '1'], ['2', '2'], ['3', '0']],
    [['0', '2'], ['0', '3'], ['1', '2'], ['2', '3'], ['3', '0'], ['3', '1']],
    [['0', '1'], ['1', '0'], ['1', '2'], ['2', '2'], ['3', '0'], ['3', '1']]]
    
def visualize(problem_set):
    for n,problem in enumerate(problem_set):
        # print the matrix
        print(f"PROBLEM {n}:")
        print("-----------")
        for i in range(0,4):
            print("| ", end="")
            for j in range(0,4):
                if [ str(i), str(j) ] in problem:
                    print("X", end=" ")
                else:
                    print(".", end=" ")
            print("|")
        print("-----------\n")

def calculate_determinants(problem_set):
    import numpy as np
    for n,problem in enumerate(problem_set):
        # print the matrix
        matrix = np.zeros(shape=(4,4))
        for x,y in problem:
            matrix[int(x)][int(y)] = 1
        print(f"PROBLEM {n}: {np.linalg.det(matrix)}")

def calculate_combinations_of_3_operations():
    import itertools
    return list(itertools.combinations(['r0','r1','r2','r3','c0','c1','c2','c3'], 3))

def get_empty_tiles_from_operations(c):
    # check which tiles must be empty
    empty = []
    for op in c:
        tiles = set()
        if 'r0' in op:
            tiles = tiles | {0,1,2,3}
        if 'r1' in op:
            tiles = tiles | {4,5,6,7}
        if 'r2' in op:
            tiles = tiles | {8,9,10,11}
        if 'r3' in op:
            tiles = tiles | {12,13,14,15}
        if 'c0' in op:
            tiles = tiles | {0,4,8,12}
        if 'c1' in op:
            tiles = tiles | {1,5,9,13}
        if 'c2' in op:
            tiles = tiles | {2,6,10,14}
        if 'c3' in op:
            tiles = tiles | {3,7,11,15}
        # empty tiles
        empty.append( list({0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15} - tiles) )
    return empty


def calculate_cost(bits,debug=False):
    cost = 0
    for i,b in enumerate(bits[1:]):
        d = hamming(b, bits[i])
        if debug:
            print(d)
        cost += d
    return cost

def estimate_cost(circuit):
    # transpile
    from qiskit.transpiler import PassManager
    from qiskit.transpiler.passes import Unroller
    pass_ = Unroller(['u3', 'cx'])
    pm = PassManager(pass_)
    new_circuit = pm.run(circuit) 
    new_circuit.draw()
    # get operations
    ops = new_circuit.count_ops()
    # estimate cost
    return ops.get('u3',0) + 10*ops.get('cx',0)

def transpile(circuit, level=0):
    from qiskit import IBMQ, Aer, execute
    from qiskit import QuantumCircuit
    from qiskit.compiler import transpile
    from qiskit.transpiler import PassManager
    from qiskit.transpiler.passes import Unroller
    # # unroll
    # pass_ = Unroller(['u3', 'cx'])
    # pm = PassManager(pass_)
    # new_circuit = pm.run(circuit) 
    # transpile
    backend = Aer.get_backend('qasm_simulator')
    optimized_0 = transpile(circuit, basis_gates = ['u3','cx'], backend=backend, seed_transpiler=11, optimization_level=level)
    return optimized_0

def gray(width):

    def binaryString(n,w=0):
        from collections import deque
        bits = deque()
        while n > 0:
            bits.appendleft(('0','1')[n&1])
            n >>= 1
        while len(bits) < w:
            bits.appendleft('0')
        return ''.join(bits)
    return [binaryString(n ^ (n>>1),width) for n in range(2**width)]
