# The quantum internet and quantum computers: how will they change the world?

- The quantum internet is now in a similar stage as the classical internet in the 1960's. In half a decade
the internet gained a huge role in our daily life.

- A quantum internet enables us to send qubits from one node to another. This allows us to create entanglement between any two points.

- Entanglement is inherently private.

## Qubit

A qubit is an essential element in quantum computing and quantum internet. It is a unit of quantum information,
and the quantum counterpart of the classical bit.

It is not possible to copy qubits.

## Superposition

Every quantum state can be seen as a linear combination, a sum of other distinct quantum states.

- Quantum computers are good at solving search tasks.

## Entanglement

- Quantum entanglement is a special connection between two qubits. When entangled, they can be moved
arbitrarily far apart from each other and remain entangled.

- When measured, entangled qubits will always yield zero or one perfectly at random, but they will
always yield the same outcome.

### Properties

1. Inherently private
2. Maximal coordination

## Teleportation

- Quantum teleportation is a method to send qubits using entanglement.

- Quantum teleportation can transmit a qubit without really using a physical carrier.

- It does not allow for faster than light communication.

## Quantum computer requirements

1. A quantum computer must be scalable.
2. It must be possible to initialise the qubits.
3. Good qubits are needed, the quantum state cannot be lost.
4. We need to have a universal set of quantum gates.
5. We need to be able to measure all qubits.

A billion qubits alone does not make a quantum computer. In order to do something practial with these qubits, we need to be able to control and read them, and all these qubits need to work in harmony according to your input.

## Quantum internet

- Composed of end nodes, switches, repeaters and control traffic.
- An entangled state between two qubits is the essence of the power of a quantum internet.
- Maximum coordination - qubits can be entangled at a very long distance, but when we make the same measurement on both qubits, they will give the same outcome.
- Inherently private - when two qubits are maximally entangled, it is impossible for any other qubit to have a share of this entanglement.
- More than two qubits can be entangled, but two qubits that are maximally entangled can not be entangled with other qubits. (?)

## Securing your data

### Factoring

- There is a great asymmetry in multiplying and factoring: multiplying is easy, factoring is complicated.
- This asymmetry is used in cryptography.
- Shor's quantum factoring algorithm: an algorithm which makes factoring possible in reasonable time, something that is not possible on a classical computer.

### Secure communication

- One of the applications of a quantum internet is secure communication. Specifically, a quantum internet allows us to realize quantum key distribution. 
- Practical cryptographic systems that are used in the real world nowadays use keys that are much shorter than the message. So they don't offer the ultimate guarantees of security. 
- Qubits cannot be copied, and this is at the heart of quantum key distribution, which always allows us to make more key to secure communication.

## Quantum chemistry

- Like factoring, Hamiltonian simulation can be performed on a quantum computer in polynomial, rather than exponential, time.
- These simulations are currently performed using very large supercomputers.
- Hamiltonian simulation will probably be the first application of a quantum computer. 
- Hamiltonian simulation can be used, for instance, to create a new medication, materials that don't have electrical resistance and chemical compounds.

## Blind quantum computing

- A great application of a quantum internet is that it enables secure access to quantum computers in the cloud.
- This is known as secure delegated quantum computing or blind quantum computing.
- Neither the input data, nor the algorithm used need to be revealed in order to obtain the result.
- You only need a small quantum terminal at home to use the big mainframe far away. 

## Quantum computer applications
### Linear equations

- Linear equations are applied virtually everywhere in our daily life.
- Linear equations are very useful because many complicated problems can be well approximated by systems of linear equations.
- A quantum computer, when making use of the HHL algorithm, can solve linear systems more efficiently, and much faster than classical computers. But it has a lot of caveats:
  - The solution vector is not yielded.
  - Entries of the matrix need to be sparse.
  - Robust invertibility.
  - Preparation of the input vector is complicated.


### Machine learning

- Machine learning is the discipline of producing mathematical functions that replicate patterns from large amounts of data.
- Many machine learning techniques rely on more basic tasks such as linear system solving for their functioning. These linear equations can be efficiently solved using the HHL algorithm.
- The same caveats on linear equations solving apply here, especially the input data problem.

### Other applications

- Searching (Grover's algorithm)
- Quantum approximate optimisation
- Semidefinite programming
- Matrix powers
- Quantum annealing


- Grover’s algorithm is a quantum algorithm to perform a search on an unstructured database.
- There are many more possible applications for example optimization.

## Applications of quantum internet

### Distributed systems

- A challenge in computing is to coordinate between different computers and different processors; a distributed system.
- Distributed systems are already known in classical computer science, where people have created protocols that can coordinate between different processors, even when these processors are behaving randomly. 
- The key to solving an agreement problem, which is basically a series of messages that the processors will exchange with each other, in order to solve this problem. This is commonly known as Byzantine agreement problem.
- Quantum protocols can solve such tasks with a constant number of qubit rounds of communication, so a number of rounds that does not depend on how many processors there are within the network.

### Other applications

- Quantum communication has also shown to be very useful to solve cryptographic problems, e.g. secure identification and position verification.
- Quantum communication is used to build up correlations in a network. Classical communication is still necessary to process the result and thus solve useful tasks.
- All of these effects are due to two properties of entanglement, namely maximum coordination and inherent privacy.
