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

# Tips for working with qubits

## Notations

The linear combination 

$$ \alpha \ket{0} + \beta \ket{1} $$

can be represented as the column vector

$$ \begin{bmatrix}
\alpha \\
\beta
\end{bmatrix} = \begin{bmatrix}
\text{amplitude of} \ \ket{0} \\
\text{amplitude of} \ \ket{1}
\end{bmatrix} $$

It is also convenient to represent the state of a quantum bit as

$$ \ket{\psi} $$



## Kets are vectors

**Remember:** _Kets_ are **vectors**!

Hence, all the usual rules for vectors are valid for kets. For example,

$$ 2 (\alpha \ket{0} + \beta \ket{1}) = 2\alpha \ket{0} + 2\beta \ket{1} $$

because

$$ 2 \begin{bmatrix}
\alpha \\
\beta
\end{bmatrix} = \begin{bmatrix}
2\alpha \\
2\beta
\end{bmatrix} $$

Also,

$$ 1 \ket{0} = \begin{bmatrix}
1 \\
0
\end{bmatrix} = \ket{0} = \ket{0} + 0 \ket{1} $$

# Our first quantum gate: the quantum NOT

## Notations

The linear combination 

$$ \alpha \ket{0} + \beta \ket{1} $$

can be represented as the column vector

$$ \begin{bmatrix}
\alpha \\
\beta
\end{bmatrix} = \begin{bmatrix}
\text{amplitude of} \ \ket{0} \\
\text{amplitude of} \ \ket{1}
\end{bmatrix} $$

It is also convenient to represent the state of a quantum bit as

$$ \ket{\psi} $$



## Kets are vectors

**Remember:** _Kets_ are **vectors**!

Hence, all the usual rules for vectors are valid for kets. For example,

$$ 2 (\alpha \ket{0} + \beta \ket{1}) = 2\alpha \ket{0} + 2\beta \ket{1} $$

because

$$ 2 \begin{bmatrix}
\alpha \\
\beta
\end{bmatrix} = \begin{bmatrix}
2\alpha \\
2\beta
\end{bmatrix} $$

Also,

$$ 1 \ket{0} = \begin{bmatrix}
1 \\
0
\end{bmatrix} = \ket{0} = \ket{0} + 0 \ket{1} $$

# The Hadamard gate

The quantum NOT gate didn't do much beyond what is possible with the classical
NOT gate. Here, we are going to see the first 'real' quantum gate: the
**Hadamard** gate.

## The Hadamard gate

The operation of the Hadamard gate on the  $\ket{0} $  and  $\ket{1} $  states is the following:

$$ \ket{0} \xrightarrow{Had} \frac{\ket{0} + \ket{1}}{\sqrt{2}}$$

$$ \ket{1} \xrightarrow{Had} \frac{\ket{0} - \ket{1}}{\sqrt{2}}$$

The Hadamard action on a superposition state is linear:

$$ \alpha\ket{0} + \beta\ket{1} \xrightarrow{Had} 
\alpha\frac{\ket{0} + \ket{1}}{\sqrt{2}} + \beta\frac{\ket{0} - \ket{1}}{\sqrt{2}}$$

$$ \alpha\ket{0} + \beta\ket{1} \xrightarrow{Had}
\frac{\alpha + \beta}{\sqrt{2}} \ket{0} + \frac{\alpha - \beta}{\sqrt{2}} \ket{1} $$

### Circuit notation

<p align="center">
  <img src="https://user-images.githubusercontent.com/69206952/175829988-41507001-ec51-441b-89bc-d1997251c700.png"/>
</p>

### Matrix representation

$$ H = \frac{1}{\sqrt{2}}
\begin{bmatrix} 1 & 1 \\
1 & -1 \end{bmatrix}$$

$$ H \ket{0} = H \begin{bmatrix} 1 \\ 
0 \end{bmatrix} = \frac{1}{\sqrt{2}} \begin{bmatrix} 1 \\
1 \end{bmatrix} = \frac{\ket{0} + \ket{1}}{\sqrt{2}}$$

$$ H \ket{1} = H \begin{bmatrix} 0 \\ 
1 \end{bmatrix} = \frac{1}{\sqrt{2}} \begin{bmatrix} 1 \\
-1 \end{bmatrix} = \frac{\ket{0} - \ket{1}}{\sqrt{2}}$$

## Hadamard gate importance

Why to use it?
- **Short answer**: it will be treated in depth later, but... The Hadamard gate 
expands the range of states that are possible to a computer to be. By doing
that, it creates the possibility to take shortcuts. 'It makes possible to
move in a way that is not possible in a classical computer'.

### Two Hadamard gates in series

It is important to note what happens when using two Hadamard gates in series:

$$ HH = \frac{1}{\sqrt{2}}
\begin{bmatrix} 1 & 1 \\
1 & -1 \end{bmatrix} \frac{1}{\sqrt{2}}
\begin{bmatrix} 1 & 1 \\
1 & -1 \end{bmatrix} = \frac{1}{2}
\begin{bmatrix} 2 & 0 \\
0 & 2 \end{bmatrix} = 
\begin{bmatrix} 1 & 0 \\
0 & 1 \end{bmatrix}$$

So, it results on the identity matrix again, even though it's very different
from the NOT gate.

In other words, two Hadamard gates in series are equivalent to a quantum wire.

# Measuring a qubit

Imagine a qubit in a general state 

$$ \ket{\psi} = \alpha \ket{0} + \beta \ket{1} $$

If you're asked if you are able to determine  $\alpha $  and  $\beta $,
the answer would be **NO!** 

**The quantum state of any system is not directly observable!**

The above is a fundamental constraint of quantum mechanics and quantum information.
The best we could do is get partial information about the amplitudes.

## Measurement in the computational basis

Suppose you are given a qubit in the state $\ket{\psi}$ and you perform the
measurement in the computational basis. What it does is it gives you a classical
bit and a probability:

- 0, with probability $|\alpha|^2$
- 1, with probability $|\beta|^2$

The measurement **disturbs** the qubit. After the measurement, if you get the
computational basis state  $\ket{0} $, for example, the posterior state of the
qubit will be the computation basis state  $\ket{0} $. The amplitudes are 'gone'.
There is no more information you can extract about the amplitudes.

Also... there are other types of measurements that can be done in quantum computing.
But this one is fundamental, because, we'll see that combining these measurements
and quantum gates we can effectively simulate an arbitrary quantum measurement.

### Example

If you have the state

$$ \frac{\ket{0} + \ket{1}}{\sqrt{2}} $$

and you measure it, you can get

- 0, with probability $1/2$
- 1, with probability $1/2$

because de amplitudes are $\frac{1}{\sqrt{2}}$.

### Example 2

Note: Typically, once a quantum bit is measured, it is **discarded**.

<p align="center">
  <img src="https://user-images.githubusercontent.com/69206952/175832270-c6f2ccb3-e0a0-4a78-a0a0-847d69e84072.png"/>
</p>

The double wire is used to represent the transportation of a classical bit.
The 'm' box will represent a measurement.

## Normalization

In a quantum state as
$$ \ket{\psi} = \alpha \ket{0} + \beta \ket{1} $$

we have

$$ p(0) + p(1) = 1 $$

$$ |\alpha|^2 + |\beta^2| = 1 $$

where **p** is the probability.

Here we understand why the quantum states should have length 1.

# General single-qubit gates

A general single-qubit gate is described as any **unitary** matrix (U) acting
on an input state.

## Unitary matrix

A unitary matrix is a complex matrix $U$ that satisfies the condition:

$$ U^{\dagger}U = UU^{\dagger} = I$$

where $U^{\dagger}$ represents the conjugate transpose matrix of U. In math terms:

$$ U^{\dagger} = (U^{T})^*$$

For example,

$$ \begin{bmatrix} a & b \\
c & d \end{bmatrix} ^{\dagger} = 
\begin{bmatrix} a^* & c^* \\
b^* & d^* \end{bmatrix}
$$

### Meaning of unitary matrix

"Unitary matrices preserve length."

This means that if we take any states and apply a unitary matrix to it,
the length (norm) is always equal to the length of the original vector.

This is important in a quantum gate because the input is going to be 
a normalized vector and the output state also needs to satisfy that
condition.

To check the proof, see https://www.youtube.com/watch?v=SWKuH9emuag&list=PL1826E60FD05B44E4&index=6

# Why unitaries are the only matrices that can become gates?

**Result**: 

$$ || M \ket{\psi} || = || \ket{\psi} || $$

for all $\ket{\psi}$ if, and only if, M is unitary.

**Background**:

$$ \ket{\psi} = \begin{bmatrix}
a \\
b \\
\vdots \\
z
\end{bmatrix} \rightarrow \bra{\psi} = \begin{bmatrix} a^* b^* \cdots z^*
\end{bmatrix}$$

where $\bra{\psi}$ is called the **bra notation**, complementing the **ket notation**.

**Note**: the full notation is called **bra-ket** notation, or **Dirac** notation.

## Bra-ket notation

$$ \ket{\psi}^{\dagger} = \bra{\psi} $$

$$ ||\ket{\psi}||^2 = \bra{\psi}\ket{\psi} $$

This is usually written as

$$ \braket{\psi|\psi} $$

### Unit vector

$\ket{e_j}$ is the j'th unit vector

$$ \begin{bmatrix}
1 \\
0 \\
\vdots \\
0
\end{bmatrix} \, \ 
\begin{bmatrix}
0 \\
1 \\
\vdots \\
0
\end{bmatrix} \ , \ \cdots
$$

Hence,

- $ M \ket{e_k}$ is the k'th column of M;
- $\bra{e_j}M\ket{e_k} \text{ is the element } M_{jk}$.


To check proof why unitaries are the only matrices which preserves length: https://www.youtube.com/watch?v=foNuXVzOtW0&list=PL1826E60FD05B44E4&index=7

# Examples of single-qubit gates

## Phase-shift gate

$$ \begin{bmatrix}
e^{i\theta} & 0 \\
0 & e^{i\phi} \end{bmatrix}
$$

where  $\theta $ and  $\phi $ are real numbers.

$$ \ket{0} \xrightarrow{PS} e^{i\theta}\ket{0} $$

$$ \ket{1} \xrightarrow{PS} e^{i\phi}\ket{1} $$

If you have a state $\ket{\psi}$ in superposition, this gate will not 
affect the measurement in a computational basis, because the exponential
factor doesn't alter the probability of either state.

Suppose  $\theta = 0 $  and  $ \phi = \pi $, the gate becomes

$$ \begin{bmatrix}
1 & 0 \\
0 & -1 \end{bmatrix}
$$

$$ \frac{\ket{0} + \ket{1}}{\sqrt{2}} 
\xrightarrow{PS} \frac{\ket{0} - \ket{1}}{\sqrt{2}}$$

How to tell these two states apart? If a measurement is done, the probability
on both states is 0.5, but if we use the following circuit, we can distinguish
them.

<p align="center">
  <img src="https://user-images.githubusercontent.com/69206952/175837352-3cc63bcf-6633-496e-ac1b-b894fb54905f.png"/>
</p>

In the circuit, a Hadamard gate is applied to the previous state.
Now, if a measurement is done:

- If the result is 0, we know, for sure, that the previous state was
$$ \frac{\ket{0} + \ket{1}}{\sqrt{2}}$$
- If the result is 1, we know, for sure, that the previous state was
$$ \frac{\ket{0} - \ket{1}}{\sqrt{2}}$$

## Rotation

This is one familiar rotation matrix.

$$ \begin{bmatrix}
\cos \theta & -\sin \theta \\
\sin \theta & \cos \theta \end{bmatrix}
$$

The already presented **X (NOT)** gate is

$$ X = \begin{bmatrix}
0 & 1 \\
1 & 0 \end{bmatrix}
$$

And the **X** gate has two 'partners': **Y** and **Z** gates.

$$ Y = \begin{bmatrix}
0 & -i \\
i & 0 \end{bmatrix}
$$

$$ Z = \begin{bmatrix}
1 & 0 \\
0 & -1 \end{bmatrix}
$$

They are, sometimes, called the Pauli sigma matrices, for historical reasons.
They come up when you try and analyze properties like electron spin.

# The controlled-NOT gate

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

# Universal quantum computation

## Classical computation

Using the AND and NOT gates you can compute any function.

The OR, XOR, addition, subtraction, multiplication can be built up
out of these basic elementary operations. Hence, we call the AND and
NOT gates are **universal** for classical computation.

## Quantum computation

Similarly, the CNOT and the single-qubit gates presented thus far are
sufficient to build up **any** unitary operation on **n** qubits. Thus,
**CNOT** and **single-qubit gates** are **universal** for quantum computing.

**Note:** it is not the only possible universal set of operations, but
it is a very convenient one and widely used.

So, in order to create a quantum computer, it is enough to be able to 
create qubits that are long-lasting and also the CNOT and single qubit
gates, plus measurement tools.

## Example of a quantum computation


<p align="center">
  <img src = "https://user-images.githubusercontent.com/69206952/175850133-fb4f6d76-bbd9-42d5-9652-042434e637a3.png"/>
</p>

The gates were not named, but one can suppose Hadamard gates, rotation, etc.

The  $\ket{0} $'s are just shorthand for the computation basis state  $\ket{000 \cdots 0} $.

### Steps

1. Start in a computation basis state, here $\ket{000 \cdots 0} $;
2. Apply a sequence of CNOTS and single-qubit gates;
3. Measure in the computational basis.

In the measurement, we would have

$$ p(\ket{000 \cdots 0}) = |\text{amplitude}|^2 $$

The typical classical idea of computation is that we have some input
that, for example, contains two numbers and you want to compute some function
of these numbers, maybe, an addition. But... what does this have to do
with quantum computing model?

Classically,

$$ x \rightarrow f(x) $$

In the quantum computing, one can assume that the value of **x** is
stored in the first **n** qubits and then there's some more qubits, all
in the 0 state, being  $\ket{x,0} $  the starting state of the computation. 
And you apply a sequence of gates, achieving:

$$ \ket{x, 0} \rightarrow \ket{x, f(x)}$$

Later, we will show that there is always a equivalent quantum circuit
to any classical circuit, roughly of the same size, to achieve the same
computation. But remember, sometimes a quantum circuit can find
'shortcuts'.

In particular, factoring is an operation that can be done vastly more
quickly in quantum than in classical computing.
# Superdense coding

<p align="center">
  <img src="https://user-images.githubusercontent.com/69206952/175996660-61342406-b2d0-4d93-934c-f6db47bda092.png" />
</p>

See again: https://www.youtube.com/watch?v=w5rCn593Dig&list=PL1826E60FD05B44E4&index=11&t=1s


# Preparing the Bell state

In the superdense coding algorithm, the first procedure was creating a
**Bell state** between the two qubits using a Hadamard and CNOT gates.

<p align="center">
   <img src="https://user-images.githubusercontent.com/69206952/175999331-fedc553b-eaf7-470d-a53c-06bdfce84047.png" />
</p>

**Theorem**: For any normalized states  $\ket{\psi} $  and  $\ket{\phi} $, 
there always exists a unitary **U** such that

$$ U\ket{\psi} = \ket{\phi} $$

To see the proof of this theorem: https://www.youtube.com/watch?v=O2pYwsLMXo4&list=PL1826E60FD05B44E4&index=12

# What's so special about entangled states?

# What's so special about entangled states anyway?

In classical computing, in a string of bits such as '011010...' it is 
elementary that each individual bit has its own value defined. In
quantum computing, it is not always possible to describe the state of
each individual qubit. It doesn't have a definite state on its own.

## The Bell states

The following state is one of the called **Bell states**:

$$ \ket{B_{00}} = \frac{\ket{00} + \ket{11}}{\sqrt{2}}$$

There are four specific two-qubit states called on the **Bell basis**.
The above is also represented as $\ket{\phi^+}$. The other three are:

- $\ket{\phi^-}$  or $\ket{B_{10}}$:
  
$$ \frac{\ket{00} - \ket{11}}{\sqrt{2}} $$

- $\ket{\psi^+}$  or $\ket{B_{01}}$:

$$ \frac{\ket{01} + \ket{10}}{\sqrt{2}} $$

- $\ket{\psi^-}$  or $\ket{B_{11}}$:

$$ \frac{\ket{01} - \ket{10}}{\sqrt{2}} $$

One thing to note is that it is **not possible** to write a Bell state as

$$ \frac{\ket{00} + \ket{11}}{\sqrt{2}} \neq (\alpha \ket{0} + \beta
\ket{1})(\gamma\ket{0} + \delta\ket{1})$$

The expansion of the right-hand side on above equation is exactly what
one would expect, thus

$$ (\alpha \ket{0} + \beta
\ket{1})(\gamma\ket{0} + \delta\ket{1}) = \alpha\gamma \ket{00} +
\alpha\delta\ket{01} + \beta\gamma\ket{10} + \beta\delta\ket{11}$$

Looking at this result, we can see that this state cannot possibly be
equal to the Bell state, because it implies that

$$ \alpha\delta = 0 \rightarrow \alpha = 0 \ \ \text{or} \ \ \delta = 0 $$

$$ \beta\gamma = 0 \rightarrow \beta = 0 \ \ \text{or} \ \ \gamma = 0 $$

## Entangled states
Hence, these states that cannot be ddecomposed into parts **entangled
quantum states**. These states are essencial in quantum computation.

### Complexity difference between classical and quantum

Imagine a general quantum state $\ket{\psi}$

$$ \ket{\psi} = \psi_{00\cdots0}\ket{00\cdots0} + \psi_{00\cdots1}\ket{00\cdots1} + \cdots + \psi_{11\cdots1}\ket{11\cdots1}$$

One can note that there are $2^n$ amplitudes to be stored and this is 
far more than the **n** bits needed to represent a classical general
state.

Because we can't observe these amplitudes directly, we can say that
there is a lot of hidden information. But we can make use of quantum
gates to rapidly manipulate that exponential amount of hidden information.

As commented, these can be reflected in the final measurement results.

# Distinguishing quantum states

If you have orthonormal quantum states, they can always be distinguished.

This is another essential attribute of the Bell states, they are orthonormal
to one another.


## Measurement in an orthonormal basis

In computational basis, if we had

$$ \ket{\psi} = \sum_j = \alpha_j \ket{j} $$

we would get the result of the measure as: j, with prob. $|\alpha|^2$,
and the posterior state would be $\ket{j}$.

In an arbitrary orthonormal $\ket{\psi_j}$ basis

$$ \ket{\psi} = \sum_j \alpha_j \ket{\psi_j} $$

the output would be: j, with prob. $|\alpha|^2$, but the posterior state
would be $\ket{\psi_j}$.

# Superdense coding redux: putting it all together

The superdense coding algorithm studied before can be summarized as:

1. Eve prepares the Bell state $\ket{B_{00}}$;
2. Eve sends one qubit to Alice and one qubit to Bob;
3. Alice applies I, X, Z or XZ to her qubit depending on which two bits
she wants to communicate to Bob -> Bell state;
4. Alice sends her qubit to Bob;
5. Bob distinguish which of the four states.

# Partial measurements

Up to now, everytime we talked about measurement we meant to measure the
whole set of qubits, but now we'll see what happens when we measure just
some of those qubits in our quantum system.

## Example

Suppose a system with 2 qubits and a measurement is made on just one of 
them (the first in this example).

The quantum state before the measurement is

$$ \alpha\ket{00} + \beta\ket{01} + \gamma\ket{10} + \delta\ket{11} $$

The questions are:
- What is the probability of 0 (p(0))?
- What is the probability of 1 (p(1))?
- What are the posterior states?

### Independence

One might guess that

$$ p(0) = p(00) + p(01) = |\alpha|^2 + |\beta|^2 $$

And this is right. The outcome of the first bit cannot depend on what we
do with other parts of the system. Hence,

$$ p(1) = p(10) + p(11) = |\gamma|^2 + |\delta|^2 $$

## General rule

$$ p(m) = \sum_. |\alpha_{.m.}|^2$$

The dots represent a sum over all other possibilites.

## Posterior state

Coming back to the example above... The input state is 

$$ \alpha\ket{00} + \beta\ket{01} + \gamma\ket{10} + \delta\ket{11} $$

We can write this as

$$ \ket{0}(\alpha\ket{0} + \beta\ket{1}) + \ket{1}(\gamma\ket{0} + \delta\ket{1})$$

If the result of the measure on the first qubit is:

- 0:
  - the posterior state of the first qubit is, with no surprises, $\ket{0}$;
  - the posterior state of the second qubit is $\frac{\alpha\ket{0} + \beta\ket{1}}{\sqrt{|\alpha|^2 + |\beta|^2}} $,
  where the denominator is necessary for the normalization.
- 1:
  - the posterior state of the first qubit is, with no surprises, $\ket{1}$;
  - the posterior state of the second qubit is $\frac{\gamma\ket{0} + \delta\ket{1}}{\sqrt{|\gamma|^2 + |\delta|^2}} $,
  where the denominator is necessary for the normalization.
  
This result can be generalized for a multi-qubit system in the same way
showed for the probability.

# Partial measurements in an arbitrary basis

The representation of the state 

$$ \alpha\ket{00} + \beta\ket{01} + \gamma\ket{10} + \delta\ket{11}$$

in an orthonormal arbitrary basis $\ket{e_0}, \ket{e_1}$ where

$$ \ket{e_0} = \frac{\ket{0} + \ket{1}}{\sqrt{2}}$$

$$ \ket{e_1} = \frac{\ket{0} - \ket{1}}{\sqrt{2}}$$

would be 

$$ \alpha'\ket{e_00} + \beta'\ket{e_01} + \gamma'\ket{e_10} + \delta'\ket{e_11}$$

Now the probability of measuring 0 on the first bit would be

$$ p(0) = |\alpha'|^2 + |\beta'|^2 $$

and the posterior state would be

$$ \ket{e_0} \left(\frac{\alpha'\ket{0} + \beta'\ket{1}}{\sqrt{|\alpha'|^2 + |\beta'|^2}} \right)$$

And the probability of measuring 1 on the first bit would be

$$ p(1) = |\gamma'|^2 + |\delta'|^2 $$

and the posterior state would be

$$ \ket{e_1} \left(\frac{\gamma'\ket{0} + \delta'\ket{1}}{\sqrt{|\gamma'|^2 + |\delta'|^2}} \right)$$

**Note**: the second bit here is still represented in the computational
basis.

## Example (proof)

Using the orthonormal set presented above, we can see that

$$ \ket{0} = \frac{\ket{e_0} + \ket{e_1}}{\sqrt{2}} $$

$$ \ket{1} = \frac{\ket{e_0} - \ket{e_1}}{\sqrt{2}}$$

So...

$$ \ket{\psi} = \alpha\ket{00} + \beta\ket{01} + \gamma\ket{10} + \delta\ket{11} $$

is equal to

$$ \frac{\alpha + \gamma}{\sqrt{2}}\ket{e_0 0} + \frac{\beta + \delta}{\sqrt{2}}\ket{e_0 1} +  \frac{\alpha - \gamma}{\sqrt{2}}\ket{e_1 0} + \frac{\beta - \delta}{\sqrt{2}}\ket{e_1 1} $$

So... the probability of measuring $\ket{e_0}$

$$ p(0) = \frac{|\alpha + \gamma|^2 + |\beta + \delta|^2}{2}$$

and the posterior state is going to be

$$ \ket{e_0} \left( \frac{(\alpha + \gamma)\ket{0} + (\beta + \gamma)\ket{1}}{\text{norm constant}} \right)$$

The equivalent for the $\ket{e_1}$ state can be easily done the same way.

# Quantum teleportation
It envolves two parties, Alice and Bob.

## Steps

1. They start with two qubits entangled in Bell state (prepared
by a third party (Charlie)) $\ket{B_{00}}$;
2. Alice has another qubit in the state

$$ \ket{\psi} = \alpha\ket{0} + \beta\ket{1}$$

3. Alice does a Bell basis measurement on her two qubits;
4. Alice sends to Bob the measurement result (on a classical information channel);
5. Bob recover the original of state of $\ket{\psi}$ by applying an adequate operation.

<p align="center">
  <img src="https://user-images.githubusercontent.com/69206952/176030270-6de4d7df-b9e6-4711-845e-40162ef47c79.png" />
</p>

The probability of any of the four possible states is 0.25. Depending on the
outcome, Bob should apply the appropriate operation to recover the original state
as shown in the following table

| Outcome | Equivalent | Operation | 
|:--:|:--:|:--:|
|$\alpha \ket{0} + \beta\ket{1}$|$\ket{\psi}$| I |
|$\alpha \ket{1} + \beta\ket{0}$|X$\ket{\psi}$| X |
|$\alpha \ket{0} - \beta\ket{1}$|Z$\ket{\psi}$| Z |
|-$\alpha \ket{1} + \beta\ket{0}$|ZX$\ket{\psi}$| ZX |

# Quantum teleportation

In the quantum teleportation protocol, note that:

- Alice didn't know anything about the initial state of her qubit.
- Curiously, the Bell basis measurement doesn't say a thing about the initial state of the quantum bit.
- Because of the measurement, we know that we are not creating a copy of the initial state of Alice's qubit
on Bob's qubit, we are destroying the initial state and recovering it in Bob's qubit.

The quantum teleportation must be interpreted as a basic primitive operation
that can be used to do all sorts of other things, like quantum error correction,
quantum computation, architectures, etc.


