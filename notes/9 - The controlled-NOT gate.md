Up to now, it was only discussed single-qubit systems. To understand
multi-qubits systems, we need to understand the two qubit gate called
the **controlled-not gate** (CNOT).


## CNOT - circuit notation

<p align="center">
  <img src = "https://user-images.githubusercontent.com/69206952/175844731-31a04283-d58c-4868-b0c0-d55b1afb7d1b.png"/>
</p>

There are two lines, representing two qubits.

- The upper one is called **control qubit**;
- The lower one is called **target qubit**.

## Possible states on a 2-qubit system

For two qubits, we have four computational basis states corresponding to
the four possible states of a two-bit system:

$$ \ket{00} \ \ \ \ket{01} \ \ \ \ket{10} \ \ \ \ket{11} $$

And we can also have a superposition of the states, such as

$$ \alpha\ket{00} + \beta\ket{01} + \gamma\ket{10} + \delta\ket{11}$$

The normalization condition is still valid, hence

$$ |\alpha|^2 + |\beta|^2 + |\gamma|^2 + |\delta|^2 = 1 $$

## Behaviour

If the control qubit is set to 1, it 'flips' the target qubit, otherwise
nothing happens. More precisely,

$$ \ket{00} \xrightarrow{CNOT} \ket{00} $$

$$ \ket{01} \xrightarrow{CNOT} \ket{01} $$

$$ \ket{10} \xrightarrow{CNOT} \ket{11} $$

$$ \ket{11} \xrightarrow{CNOT} \ket{10} $$

Generally,

$$ \ket{xy} \xrightarrow{CNOT} \ket{x \ y\oplus x} $$

## Matrix representation

So, the quantum state representation is a four-dimensional vector now.

$$ \ket{\psi} = \begin{bmatrix} \alpha \\
\beta \\
\gamma \\
\delta \end{bmatrix}$$

The matrix that represents the CNOT gate is, obviously, a 4x4 matrix, shown
below.

$$ \text{CNOT} = \begin{bmatrix}
  1 & 0 & 0 & 0 \\
  0 & 1 & 0 & 0 \\
  0 & 0 & 0 & 1 \\
  0 & 0 & 1 & 0
  \end{bmatrix}$$

### Three-qubits system CNOT

<p align="center">
  <img src = "https://user-images.githubusercontent.com/69206952/175846556-64116137-646f-4cda-a992-504a4dcea334.png"/>
</p>

## Example

Suppose a two-qubit system that has the initial computational state $\ket{00}$. 
If the following circuit is applied,


<p align="center">
  <img src = "https://user-images.githubusercontent.com/69206952/175847011-5011b3f9-633f-4fd0-8c6e-f350b83c695c.png"/>
</p>

the output would be

$$ \ket{00} \xrightarrow{Had} \frac{\ket{00} + \ket{10}}{\sqrt{2}}$$

$$ \frac{\ket{00} + \ket{10}}{\sqrt{2}} \xrightarrow{CNOT} \frac{\ket{00} + \ket{11}}{\sqrt{2}} $$

  
This state is a 'highly non-classical' state. It is what we call an
entangled state. These can be used to perform a lot of interesting information
processing tasks. It will be discussed in depth later.

