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
