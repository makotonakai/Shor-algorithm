from qiskit import IBMQ, QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit import execute, Aer
from qiskit.qasm import pi
from qiskit.tools.visualization import plot_histogram, circuit_drawer
import numpy as np

APItoken = "Replace me"
url = "Replace me"
IBMQ.enable_account(APItoken, url)

IBMQ.backends()

def swap(qci,s1,s2):
	qci.cx(s1,s2)
	qci.cx(s2,s1)
	qci.cx(s1,s2)

def iqft(qci,q,n):
	for i in range(n):
		for j in range(i):
			qci.cu1(-np.pi/float(2**(i-j)),q[i],q[j])
		qci.h(q[i])

nx = 3
ny = 4
nc = 4
q1 = QuantumRegister(nx)
q2 = QuantumRegister(ny)
c = ClassicalRegister(nc)
qc1 = QuantumCircuit(q1, c)
qc2 = QuantumCircuit(q2, c)
qc = qc1+qc2

for i in range(nx):
	qc.h(q1[i])
qc.x(q2[3])
qc.cx(q1[0],q2[0])
qc.cx(q1[1],q2[0])
qc.cx(q1[1],q2[2])
qc.cx(q1[2],q2[1])
qc.ccx(q1[0],q1[2],q2[0])
qc.ccx(q1[0],q1[2],q2[1])
qc.ccx(q1[0],q1[2],q2[2])
qc.ccx(q1[1],q1[2],q2[2])
iqft(qc,q1,nx)
swap(qc,q1[0],q1[2])

for j in range(ny):
	qc.measure(q2[ny-j-1],c[j])
	
backends = ['ibmq_20_tokyo', 'qasm_simulator']
#Use this for the actual machine
#backend_sim = IBMQ.get_backend(backends[0])
#Use this for the simulation
backend_sim = Aer.get_backend(backends[1])
result = execute(qc, backend_sim, shots=4096).result()
#{'1011': 1017, '1001': 521, '1101': 502, '0011': 1048, '0001': 496, '0101': 512}
#circuit_drawer(qc).show()

print(result.get_counts(qc))
plot_histogram(result.get_counts(qc))
