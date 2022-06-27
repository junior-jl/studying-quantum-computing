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

