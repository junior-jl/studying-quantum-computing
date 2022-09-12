# Tutorial Netsquid - Qubits e computação quântica

import netsquid as ns


def separador(tamanho = 50):
    """Separador básico de texto para melhor visualização."""
    print('*', end='')
    for i in range(tamanho):
        print('-', end='')
    print('*')

# Qubits e seu estado quântico

# Criando dois qubits
q1, q2 = ns.qubits.create_qubits(2)
# Imprimindo o estado dos dois qubits, por padrão devem ser |0>
print('Estado q1 -> ' + str(q1.qstate.qrepr))
print('Estado q2 -> ' + str(q2.qstate.qrepr))
separador()
# Checando se os estados dos qubits são iguais (deve ser falso)
print('Os estados q1 e q2 são iguais? ', end='')
print(q1.qstate == q2.qstate)
# Combinando os qubits
print('Qubits 1 e 2 combinados...')
ns.qubits.combine_qubits([q1, q2])
# Agora o estado de q1 e q2 é o mesmo... |00> (logo... True)
print('Os estados q1 e q2 são iguais? ', end='')
print(q1.qstate == q2.qstate)
# Esse método mostra o número de qubits que possuem o mesmo 'qstate' que q1
print('Quantos qubits possuem o estado quântico combinado com q1? ', end='')
print(q1.qstate.num_qubits)
print('Estado combinado q1-q2 -> ', end='')
# QState([Qubit('QS#0-0'), Qubit('QS#0-1')])
print(q1.qstate.qrepr)
separador()
# A função reduce_dm() é o método recomendado para inspecionar o estado de um qubit
# Estudar reduced density matrix!!!!
print('Matriz densidade reduzida de q1 e q2:')
print(ns.qubits.reduced_dm([q1, q2]))
print('Matriz densidade reduzida de q2 sozinho:')
print(ns.qubits.reduced_dm(q2))

# Medição de qubits

print('O número de qubits que possui o estado q1.qstate é igual ao número de qubits que possui o estado q2.qstate? ',
      end='')
print(q1.qstate.num_qubits == q2.qstate.num_qubits)
print('q1.qstate = ' + str(q1.qstate))
print('q2.qstate = ' + str(q2.qstate))

# É feita uma medição em q1
print('Medição feita em q1... (Resultado, probabilidade) -> ', end='')
print(ns.qubits.measure(q1))
print('Após a medição, o estado conjunto é separado.')
print('Número de qubits no estado q1.qstate é igual ao número de qubits no estado q2.qstate? Quantos? ', end='')
print(q1.qstate.num_qubits == q2.qstate.num_qubits, end=' ')
print(q1.qstate.num_qubits)
print('Matriz densidade reduzida de q1 sozinho:')
print(ns.qubits.reduced_dm(q1))

separador()
print('Combinando os estados novamente...')
ns.qubits.combine_qubits([q1, q2])
print('Número de qubits no estado q1.qstate é igual ao número de qubits no estado q2.qstate? Quantos? ', end='')

print(q1.qstate.num_qubits == q2.qstate.num_qubits, end=' ')
print(q1.qstate.num_qubits)
print('Resultado da medição de q2 (com descarte)')
print(ns.qubits.measure(q2, discard=True))
print('Estado quântico de q2 é vazio (None)? ', end='')
print(q2.qstate is None)

# Formalismo de estados quânticos

# A classe QState define um estado quântico compartilhado que é representado por um QRepr, o qual pode ser:
# - KetRepr (padrão)
# - DenseDMRepr
# - SparseDMRepr
# - StabRepr
# - GSLCRepr
# Estes são os QFormalism's
# Para mudar o formalismo utilizado na simulação, usar set_qstate_formalism().

separador()
from netsquid.qubits.qformalism import QFormalism
print('Formalismo utilizado até agora... (padrão): ', end='')
print(ns.get_qstate_formalism())
# Change to stabilizer formalism:
ns.set_qstate_formalism(QFormalism.STAB)
print('Após o uso de ''set_qstate_formalism(QFormalism.STAB)'': ', end='')
print(ns.get_qstate_formalism())

# É possível atribuir um estado a qubits manualmente. Por exemplo, atribuindo o estado |+-> a dois novos qubits:

separador()
# Criando dois qubits sem estado
q1, q2 = ns.qubits.create_qubits(2, no_state=True)
print('Atribuindo o estado h01 (h0 = |+>, h1 = |->) aos qubits q1 e q2')
ns.qubits.assign_qstate([q1, q2], ns.h01)
print('Matriz densidade reduzida (MDR) de q1:')
print(ns.qubits.reduced_dm(q1))
print('MDR de q2:')
print(ns.qubits.reduced_dm(q2))

separador()
print('Checando o formalismo utilizado...')
print(type(q1.qstate.qrepr))
print('q1.qstate.qrepr.check_matrix: a matriz que representa os geradores do estado q1:')
print(q1.qstate.qrepr.check_matrix)
print('q1.qstate.qrepr.phases: o vetor que representa as fases associadas aos geradores do estado q1:')
print(q1.qstate.qrepr.phases)

# Operações quânticas

separador()
# Mudando o formalismo para matriz densidade
ns.set_qstate_formalism(QFormalism.DM)
# Criando 3 qubits (como no exemplo do teleporte, dois com Alice e um com Bob)
a1, a2, b1 = ns.qubits.create_qubits(3)

# Vamos teleportar o estado |0_y> = \frac{|0> + j|1>}{\sqrt{2}} de Alice (a1) para Bob...
# Esse estado pode ser preparado a partir do estado |0> aplicando os operadores H e S.
# O estado emaranhado entre a2 e b1 será |B_{00}>
print('a1 após criação:')
print(ns.qubits.reduced_dm([a1]))
# Realizando as operações mencionadas em a1
ns.qubits.operate(a1, ns.H) # a1 = |0> (padrão) ... H|0> = |=>
separador(20)
print('a1 após porta Hadamard:')
print(ns.qubits.reduced_dm([a1]))
ns.qubits.operate(a1, ns.S) # a1 = |+> ... S|+> = |0_y>
separador(20)
print('a1 após porta S:')
print(ns.qubits.reduced_dm([a1]))
# Transformar a2 e b1 no estado de Bell |B_{00}> = \frac{|00> + |11>}{\sqrt{2}}
ns.qubits.operate(a2, ns.H)  # Aplicando Hadamard em a2
ns.qubits.operate([a2, b1], ns.CNOT)  # Aplicando CNOT em a2, b1: a2 = controle, b1 = alvo
separador(20)
print('Estado emaranhado a2, b1:')
print(ns.qubits.reduced_dm([a2, b1]))

# Criando operadores
separador()
import numpy as np
# Construir um novo operador usando preexistentes:
newOp = ns.CNOT * ((ns.X + ns.Z) / np.sqrt(2) ^ ns.I)
print(newOp.name)  # Nota: CNOT == CX
# Construir um novo operador usando uma matriz:
newOp2 = ns.qubits.Operator("newOp2", np.array([[1, 1j], [-1j, -1]])/np.sqrt(2))
print(newOp2.name)
print('Novo operador é unitário? Novo operador é hermitiano?')
print(newOp2.is_unitary == True)
print(newOp2.is_hermitian == True)
# Construir novo operador usando funções auxiliares:
R = ns.create_rotation_op(angle=np.pi/4, rotation_axis=(1, 0, 0))
print(R.name)
# Construir um operador controlado:
CR = R.ctrl
print(CR.name)

# O protocolo continua com Alice fazendo uma medição do estado de Bell nos seus dois qubits
# Então, ela envia seus dois bits clássicos correspondentes às medidas para que Bob
# realize as possíveis correções

# A função measure realiza uma medição projetiva. Por padrão, a base é Z (|0> , |1>)

separador()
# Garante o mesmo resultado dos testes
ns.set_random_state(seed=42)
print('Número de qubits com estado compartilhado a2 antes do emaranhamento entre a2 e a1: ', end='')
print(a2.qstate.num_qubits)
print('Estado inicial de a1 (estado a ser teleportado):')
estado_teleporte = ns.qubits.reduced_dm([a1])
print(ns.qubits.reduced_dm([a1]))
# Emaranhamento entre os qubits de Alice
ns.qubits.operate([a1, a2], ns.CNOT)  # CNOT: a1 = controle, a2 = alvo
ns.qubits.operate(a1, ns.H)
print('Número de qubits com estado compartilhado a2 após o emaranhamento entre a2 e a1: ', end='')
print(a2.qstate.num_qubits)

# Medição de a1 na base padrão:
m1, prob = ns.qubits.measure(a1)
# Linha necessária para usar o ket no print, no lugar de 0 e 1 normal
labels_z = ("|0>", "|1>")
separador(25)
print('Medições nos qubits de Alice:')

print(f"Medido {labels_z[m1]} com probabilidade {prob:.2f}")
# Medição de a2 na base padrão:
m2, prob = ns.qubits.measure(a2)
print(f"Medido {labels_z[m2]} com probabilidade {prob:.2f}")

# Confirmando que após a medição, o emaranhamento é perdido
print('Número de qubits com estado compartilhado a2 após as medições em a1 e a2: ', end='')
print(a2.qstate.num_qubits)

if m2 == 1:
    ns.qubits.operate(b1, ns.X)
if m1 == 1:
    ns.qubits.operate(b1, ns.Z)
print('Matriz densidade reduzida do qubit de Bob após correções:')
print(ns.qubits.reduced_dm([b1]))
print('Matriz densidade reduzida do estado inicial do qubit de Alice:')
print(estado_teleporte)

# A verificação é melhor por meio da fidelidade
# O estado inicial de a1 era |0_y>

fidelidade = ns.qubits.fidelity(b1, ns.y0, squared=True)
print(f"A fidelidade é {fidelidade:.3f}")

separador()
# Também é possível especificar a base de medição...
# Base Hadamard (observável X):
q3, = ns.qubits.create_qubits(1)
m3, prob = ns.qubits.measure(q3, observable=ns.X, discard=True)
labels_x = ("+", "-")
print(f"Medido |{labels_x[m3]}> com probabilidade {prob:.2f}")

# Além disso, pode-se utilizar o exemplo do ping-pong entre dois observáveis diferentes...
separador()
q4, = ns.qubits.create_qubits(1)
for i in range(6):
    print('Iteração ' + str(i) + ': ', end='')
    # Se i for ímpar, mede na base padrão, se i for par, mede na base X
    observable, labels = (ns.Z, ("0", "1")) if i % 2 else (ns.X, ("+", "-"))
    m, prob = ns.qubits.measure(q4, observable=observable)
    print(f"Medido |{labels[m]}> com probabilidade {prob:.2f}")

# Medições gerais (tópico avançado)

# Os formalismos KET e DM também suportam medições gerais em múltiplos qubits usando uma lista de operadores
# Por exemplo, a medição no estado de Bell acima pode ser descrita como uma única medição em dois qubits
# Neste caso, o operador deve ser feito manualmente. E, diferente da função measure(), essa medição não divide
# o estado compartilhado

separador()
operadores_bell = []
p0, p1 = ns.Z.projectors
operadores_bell.append(ns.CNOT * (ns.H ^ ns.I) * (p0 ^ p0) * (ns.H ^ ns.I) * ns.CNOT)
operadores_bell.append(ns.CNOT * (ns.H ^ ns.I) * (p0 ^ p1) * (ns.H ^ ns.I) * ns.CNOT)
operadores_bell.append(ns.CNOT * (ns.H ^ ns.I) * (p1 ^ p0) * (ns.H ^ ns.I) * ns.CNOT)
operadores_bell.append(ns.CNOT * (ns.H ^ ns.I) * (p1 ^ p1) * (ns.H ^ ns.I) * ns.CNOT)

q5, q6 = ns.qubits.create_qubits(2)
ns.qubits.operate(q5, ns.H)
meas, prob = ns.qubits.gmeasure([q5, q6], meas_operators=operadores_bell)
labels_bell = ("|00>", "|01>", "|10>", "|11>")
print(f"Medido {labels_bell[meas]} com probabilidade {prob:.2f}")
print('Número de qubits com o mesmo estado q5: ', end='')
print(q5.qstate.num_qubits)

# Aplicando ruído (tópico avançado)

# Finalizando a questão do teleporte...
# Qubits perdem coerência com o tempo
# Pode-se supor que b1 depolarizou durante a medição de Bell em a1 e a2, o que causaria a perda de fidelidade...

ns.qubits.delay_depolarize(b1, depolar_rate=1e7, delay=20)
fid = ns.qubits.fidelity([b1], reference_state=ns.y0, squared=True)

separador()
print('Voltando ao teleporte...')
print('Fidelidade com taxa de depolarização no tempo:')
print(f"A fidelidade é {fid:.3f}")

# Além disso, o módulo qubitapi define algumas funções para aplicar ruído ou operações estocáticas em qubits
separador()
q1, q2, q3, q4 = ns.qubits.create_qubits(4)
ns.qubits.stochastic_operate(q1, [ns.X, ns.Y, ns.Z], p_weights=(1/2, 1/4, 1/4))
print(ns.qubits.reduced_dm([q1]))
ns.qubits.apply_pauli_noise(q2, p_weights=(1/4, 1/4, 1/4, 1/4))  # (I, X, Y, Z)
print(ns.qubits.reduced_dm([q2]))
ns.qubits.depolarize(q3, prob=0.8)
print(ns.qubits.reduced_dm([q3]))
ns.qubits.operate(q4, ns.X)  # -> |1>
ns.qubits.amplitude_dampen(q4, gamma=0.1, prob=1)
print(ns.qubits.reduced_dm([q4]))

