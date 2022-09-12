```
Estado q1 -> KetRepr(num_qubits=1,
ket=
[[1.+0.j]
 [0.+0.j]])
Estado q2 -> KetRepr(num_qubits=1,
ket=
[[1.+0.j]
 [0.+0.j]])
*--------------------------------------------------*
Os estados q1 e q2 são iguais? False
Qubits 1 e 2 combinados...
Os estados q1 e q2 são iguais? True
Quantos qubits possuem o estado quântico combinado com q1? 2
Estado combinado q1-q2 -> KetRepr(num_qubits=2,
ket=
[[1.+0.j]
 [0.+0.j]
 [0.+0.j]
 [0.+0.j]])
*--------------------------------------------------*
Matriz densidade reduzida de q1 e q2:
[[1.+0.j 0.+0.j 0.+0.j 0.+0.j]
 [0.+0.j 0.+0.j 0.+0.j 0.+0.j]
 [0.+0.j 0.+0.j 0.+0.j 0.+0.j]
 [0.+0.j 0.+0.j 0.+0.j 0.+0.j]]
Matriz densidade reduzida de q2 sozinho:
[[1.+0.j 0.+0.j]
 [0.+0.j 0.+0.j]]
O número de qubits que possui o estado q1.qstate é igual ao número de qubits que possui o estado q2.qstate? True
q1.qstate = QState([Qubit('QS#0-0'), Qubit('QS#0-1')])
q2.qstate = QState([Qubit('QS#0-0'), Qubit('QS#0-1')])
Medição feita em q1... (Resultado, probabilidade) -> (0, 1.0)
Após a medição, o estado conjunto é separado.
Número de qubits no estado q1.qstate é igual ao número de qubits no estado q2.qstate? Quantos? True 1
Matriz densidade reduzida de q1 sozinho:
[[1.+0.j 0.+0.j]
 [0.+0.j 0.+0.j]]
*--------------------------------------------------*
Combinando os estados novamente...
Número de qubits no estado q1.qstate é igual ao número de qubits no estado q2.qstate? Quantos? True 2
Resultado da medição de q2 (com descarte)
(0, 1.0)
Estado quântico de q2 é vazio (None)? True
*--------------------------------------------------*
Formalismo utilizado até agora... (padrão): <class 'netsquid.qubits.kettools.KetRepr'>
Após o uso de set_qstate_formalism(QFormalism.STAB): <class 'netsquid.qubits.stabtools.StabRepr'>
*--------------------------------------------------*
Atribuindo o estado h01 (h0 = |+>, h1 = |->) aos qubits q1 e q2
Matriz densidade reduzida (MDR) de q1:
[[0.5+0.j 0.5+0.j]
 [0.5+0.j 0.5+0.j]]
MDR de q2:
[[ 0.5+0.j -0.5+0.j]
 [-0.5+0.j  0.5+0.j]]
*--------------------------------------------------*
Checando o formalismo utilizado...
<class 'netsquid.qubits.stabtools.StabRepr'>
q1.qstate.qrepr.check_matrix: a matriz que representa os geradores do estado q1:
[[1 0 0 0]
 [0 1 0 0]]
q1.qstate.qrepr.phases: o vetor que representa as fases associadas aos geradores do estado q1:
[ 1 -1]
*--------------------------------------------------*
a1 após criação:
[[1.+0.j 0.+0.j]
 [0.+0.j 0.+0.j]]
*--------------------*
a1 após porta Hadamard:
[[0.5+0.j 0.5+0.j]
 [0.5+0.j 0.5+0.j]]
*--------------------*
a1 após porta S:
[[0.5+0.j  0. -0.5j]
 [0. +0.5j 0.5+0.j ]]
*--------------------*
Estado emaranhado a2, b1:
[[0.5+0.j 0. +0.j 0. +0.j 0.5+0.j]
 [0. +0.j 0. +0.j 0. +0.j 0. +0.j]
 [0. +0.j 0. +0.j 0. +0.j 0. +0.j]
 [0.5+0.j 0. +0.j 0. +0.j 0.5+0.j]]
*--------------------------------------------------*
(CX*(((X+Z)/(1.41))^I))
newOp2
Novo operador é unitário? Novo operador é hermitiano?
True
True
R_x[0.79]
CR_x[0.79]
*--------------------------------------------------*
Número de qubits com estado compartilhado a2 antes do emaranhamento entre a2 e a1: 2
Estado inicial de a1 (estado a ser teleportado):
[[0.5+0.j  0. -0.5j]
 [0. +0.5j 0.5+0.j ]]
Número de qubits com estado compartilhado a2 após o emaranhamento entre a2 e a1: 3
*-------------------------*
Medições nos qubits de Alice:
Medido |0> com probabilidade 0.50
Medido |1> com probabilidade 0.50
Número de qubits com estado compartilhado a2 após as medições em a1 e a2: 1
Matriz densidade reduzida do qubit de Bob após correções:
[[0.5+0.j  0. -0.5j]
 [0. +0.5j 0.5+0.j ]]
Matriz densidade reduzida do estado inicial do qubit de Alice:
[[0.5+0.j  0. -0.5j]
 [0. +0.5j 0.5+0.j ]]
A fidelidade é 1.000
*--------------------------------------------------*
Medido |-> com probabilidade 0.50
*--------------------------------------------------*
Iteração 0: Medido |-> com probabilidade 0.50
Iteração 1: Medido |0> com probabilidade 0.50
Iteração 2: Medido |+> com probabilidade 0.50
Iteração 3: Medido |0> com probabilidade 0.50
Iteração 4: Medido |-> com probabilidade 0.50
Iteração 5: Medido |1> com probabilidade 0.50
*--------------------------------------------------*
Medido |10> com probabilidade 0.25
Número de qubits com o mesmo estado q5: 2
*--------------------------------------------------*
Voltando ao teleporte...
Fidelidade com taxa de depolarização no tempo:
A fidelidade é 0.909
*--------------------------------------------------*
[[0.25+0.j 0.  +0.j]
 [0.  +0.j 0.75+0.j]]
[[0.5+0.j 0. +0.j]
 [0. +0.j 0.5+0.j]]
[[0.6+0.j 0. +0.j]
 [0. +0.j 0.4+0.j]]
[[0.1+0.j 0. +0.j]
 [0. +0.j 0.9+0.j]]

Process finished with exit code 0
```
