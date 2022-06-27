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
