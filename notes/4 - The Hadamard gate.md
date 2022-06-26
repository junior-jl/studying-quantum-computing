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

