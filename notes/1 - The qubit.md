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

## Quantum state

The **quantum state of a qubit** is a vector in a 2-dimensional complex vector space.

<p align="center">
    <img src="https://user-images.githubusercontent.com/69206952/175797308-54e2be33-4aad-4f7e-8515-0ce5e6933938.png" />

</p>
So, a general quantum state can be written as a linear combination of $\ket{0} \text{ and } \ket{1}$.
Hence, we can write any quantum state as:

$$ \alpha \ket{0} + \beta \ket{1} $$

## Superposition

'Superposition is just a fancy word for linear combination'. Thus, the equation above can be interpreted as a superposition of the states $\ket{0} \text{ and } \ket{1}$.

## Amplitude

The  $\alpha $ and  $\beta $ coefficients in the above equation are called amplitudes for the  $\ket{0} $ state and $\ket{1}$ state.

### Normalization costraint

We have the following constraint on the values of the amplitudes.

$$ |\alpha|^2 + |\beta|^2 = 1$$

Note: The  $\ket{0} $ is not the null vector, or zero vector.

Note$^2$: The superposition doesn't mean that the a qubit is in the state  $\ket{0} $ and  $\ket{1} $ simultaneously.
