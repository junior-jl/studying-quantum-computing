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

