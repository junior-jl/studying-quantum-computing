# Basic model of quantum computation
  - applied linear algebra;
  - vector, matrices, Hermitian matrices, unitary matrices;
  - circuits - AND, OR, NOT.

## Information

The fundamental unit in classical (traditional) information is the bit, 
that assumes the value of 0 or 1.
In the physical world, we might represent a bit in terms of a voltage 
inside a computer, or a magnetic domain in a hard disk, etc.

The qubit is the equivalent system in quantum computing.
We are going to work with a mathematical abstraction of the qubit, 
as we do with the bit.

So, the **qubit** is gonna be treated as the simplest quantum system.
Physically, it can be treated as atoms, photons, eletrons, etc.

It is the fundamental unit of quantum information. 

The computations are going to be made by manipulating the qubits and their states.

## Qubit - quantum bit

Similar to the bit, the qubit has two 'special' states: $\ket{0} \text{ and } \ket{1}$
equivalent to the 0 and 1 states in the bit.

This notation with 'funny' brackets is called **ket notation**.

### Quantum state

The **quantum state of a qubit** is a vector in a 2-dimensional complex vector space.
So, a general quantum state can be written as a linear combination of $\ket{0} \text{ and } \ket{1}$.
Hence, we can write any quantum state as:

$$ \alpha \ket{0} + \beta \ket{1} $$

