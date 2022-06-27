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
