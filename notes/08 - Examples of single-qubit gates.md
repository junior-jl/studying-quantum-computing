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

