import netsquid as ns
from netsquid.qubits.qformalism import QFormalism

ns.set_qstate_formalism(QFormalism.DM)
a1, a2, b1 = ns.qubits.create_qubits(3)

### o estado de a1 é teleportado para b1 usando um estado emaranhado entre b1 e a2.
### o estado escolhido para a1 é |0_y> = \frac{|0> + i|1>}{\sqrt{2}} ---- 0 +i1 / raiz(2)
### o estado inicial padrão dos qubits é |0>
### caminhos dos qubits
### |a1> = |0> deve passar por um operador de Hadamard (H) e um operador de fase (S);
### |a2> = |0> deve passar por um operador de Hadamard (H) e ser emaranhado com b1;
### |b1> = |0> deve ser emaranhado com a2.

### o estado emaranhado entre a2 e b1 é |B_{00}> = \frac{|00> + |11>}{\sqrt{2}} ---- 00 + 11 / raiz(2)

ns.qubits.operate(a1, ns.H) # aplicando a porta Hadamard a a1: |0> -> |+>
ns.qubits.operate(a1, ns.S) # aplicando a porta S a a1: |+> -> |0_y>
print("Matriz de densidades reduzida (bit 1 - Alice)")
print(ns.qubits.reduced_dm([a1]))

ns.qubits.operate(a2, ns.H) # aplicando a porta Hadamard a a2: |0> -> |+>
print("Antes da combinação de a2 com b1:")
print(f"Estado de a2: {a2.qstate}, Estado de b1: {b1.qstate}")
ns.qubits.operate([a2, b1], ns.CNOT) # CNOT: a2 = controle, b1 = alvo
print("Após a combinação de a2 com b1:")
print(ns.qubits.reduced_dm([a2, b1]))
print(f"Estado de a2: {a2.qstate}, Estado de b1: {b1.qstate}")

ns.set_random_state(seed=42)
ns.qubits.operate([a1, a2], ns.CNOT) # CNOT: a1 = controle, a2 = alvo
ns.qubits.operate(a1, ns.H)

m1, prob = ns.qubits.measure(a1)
labels_z = ("|0>", "|1>")
print("Bit 1 - Alice é medido")
print(f"Medido {labels_z[m1]} com probabilidade {prob:.2f}")
m2, prob = ns.qubits.measure(a2)
print("Bit 2 - Alice é medido")
print(f"Medido {labels_z[m2]} com probabilidade {prob:.2f}")

print("Antes da correção - Bit 1 - Bob")
print(ns.qubits.reduced_dm([b1]))
# Operações necessárias no qubit de Bob dependendo da medição obtida nos bits de Alice
if m2 == 1:
    ns.qubits.operate(b1, ns.X)
if m1 == 1:
    ns.qubits.operate(b1, ns.Z)
print("Matriz de densidades reduzida (bit - Bob)")
print(ns.qubits.reduced_dm([b1]))

