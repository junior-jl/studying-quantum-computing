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

