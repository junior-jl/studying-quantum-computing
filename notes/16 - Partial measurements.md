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
