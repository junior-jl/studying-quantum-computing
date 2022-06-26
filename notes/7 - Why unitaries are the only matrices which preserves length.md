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
