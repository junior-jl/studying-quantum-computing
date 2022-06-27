## Quantum logic gate

It is a way of manipulating the quantum state of qubits. They are the basic
building blocks of quantum computing.

## Quantum NOT gate

It is a generalization of the classical NOT gate.

### Behaviour

The action of the NOT gate on the  $\ket{0} $ and  $\ket{1} $ states:

$$ \ket{0} \xrightarrow{NOT} \ket{1}$$

$$ \ket{1} \xrightarrow{NOT} \ket{0}$$

The action on a superposition state:

$$ \alpha \ket{0} + \beta \ket{1} \xrightarrow{NOT}
\alpha \ket{1} + \beta \ket{0} $$

### Circuit notation

For historical reasons, the NOT quantum gate (Pauli-X) is represented by an **X** on a box.

<p align="center">
  <img src="https://user-images.githubusercontent.com/69206952/175829099-23cdc4b0-febc-47fc-8449-a634d3157770.png"/>
</p>

The line on the sides of the gate is called **quantum wire**.

### Matrix representation

The matrix representation of the action of a quantum NOT gate is:

$$ X = \begin{bmatrix}
0 & 1 \\
1 & 0 \end{bmatrix}$$

So, the action of the NOT gate can be seen as the multiplication of $X\ket{\psi}$

$$ X \ket{0} = \begin{bmatrix}
0 & 1 \\
1 & 0 \end{bmatrix} \begin{bmatrix}
1 \\
0 \end{bmatrix} = \begin{bmatrix}
0 \\
1 \end{bmatrix} = \ket{1} $$

$$ X \ket{1} = \begin{bmatrix}
0 & 1 \\
1 & 0 \end{bmatrix} \begin{bmatrix}
0 \\
1 \end{bmatrix} = \begin{bmatrix}
1 \\
0 \end{bmatrix} = \ket{0} $$

### Quantum wire

The simplest quantum circuit (computation) is a simple wire. We can interpret
as a single qubit being preserved (or passed).

<p align="center">
  <img src="https://user-images.githubusercontent.com/69206952/175829348-4b8451e7-e54f-46ca-b350-bfabc4c8ce5f.png"/>
</p>

Although very simple to understand, a quantum wire is, in many systems, the
hardest system of all to implement, because quantum states tend to be very
fragiles, since they are implemented, generally, in single atoms, single
photons, being very easily perturbed by the environment.

### Two quantum NOT gates

It is very straighforward to note that using two NOT gates in a row on a
qubit state is the equivalent of a quantum wire. Mathematically, the multiplication
of the X matrix by itself will result on an identity matrix.

$$ XX = \begin{bmatrix}
0 & 1 \\
1 & 0 \end{bmatrix}
\begin{bmatrix}
0 & 1 \\
1 & 0 \end{bmatrix} = 
\begin{bmatrix}
1 & 0 \\
0 & 1 \end{bmatrix} $$

