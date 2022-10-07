# Tutorial Netsquid - Modelagem de componentes de rede

# Na seção anterior, mostramos como usar o simulador de eventos discretos
# para teleportar um qubit. Esse processo envolvia instruções manuais para
# as entidades envolvidas marcarem eventos no tempo
# Nesta seção, iremos mostrar como esse exemplo de simulação pode ser simplificado
# introduzindo componentes de rede, que são entidades de simulação que modelam
# o hardware de uma rede quântica.

# Componentes
#   São representados pela classe base Component, a qual é subclasse de Entity.
#   Subclasses de Component: canais quânticos e clássicos, fontes quânticas e 
#   processadores quânticos...
#   Atributos de componentes:
#       - propriedades (properties) - definem as características físicas do componente
#       - modelos (models) - descrevem o comportamento funcional do componente
#       - ports (portas) - para comunicação de entrada e saída
#       - subcomponentes (subcomponents) - peças que constroem (possivelmente) o componente

# Canais
#   O envio de uma mensagem com atraso pode ser modelado por um canal (Channel), que é 
#   uma subclasse de Component

def separador(tamanho = 50):
    """Separador básico de texto para melhor visualização."""
    print('*', end='')
    for i in range(tamanho):
        print('-', end='')
    print('*')

import netsquid as ns
from netsquid.components import Channel, QuantumChannel
# Channel(nome, [delay], [comprimento], [modelos], 
# [transmitir_itens_vazios], [propriedades], **kwargs)
canal = Channel(name="MeuCanal")
print(f"O canal {canal} foi criado.")
#     send(itens, [append], [header], **kwargs)
canal.send("hello world!")
print(f"A mensagem "'hello world!'" deve ser enviada pelo canal...")
ns.sim_run()

# Canais são uma subclasse de Entity e marcam eventos para transmitir a mensagem. Assim,
# precisamos rodar o simulador para a mensagem chegar. Para receber mensagens, podemos 
# usar receive(). Esse método retorna a mensagem na saída, assim como o tempo que as
# mensagens trafegaram pelo canal. Como nenhum delay foi especificado, o padrão é não
# haver atraso, logo, a mensagem é recebida no mesmo instante que foi enviada
itens, atraso = canal.receive()
print(f"A mensagem {itens} foi enviada com atraso de {atraso} ns.")

# Há várias formas de adicionar delay a um canal, uma delas é inicializando um canal com 
# um delay fixo
Channel(name="CanalDelay", delay=10)

# Outra forma é especificar um modelo de delay (DelayModel), uma subclasse de Model usada
# para gerar atrasos. Por exemplo, podemos usar o modelo de atraso fixo, no qual apenas
# o delay é especificado
from netsquid.components.models.delaymodels import FixedDelayModel
modelo_atraso_fixo = FixedDelayModel(delay=10)

# Os modelos de um componente são armazenados no seu atributo models e indexado com a chave
# apropriada. É possível entregar um dicionário com modelos na inicialização.
separador()
canal.models['delay_model'] = modelo_atraso_fixo
canal.send("hello world!")
print(f"A mensagem "'hello world!'" deve ser enviada pelo canal...")
ns.sim_run()
itens, atraso = canal.receive()
print(f"A mensagem {itens} foi enviada com atraso de {atraso} ns.")

# Um exemplo de modelo que amostra aleatoriamente seu atraso é o modelo de delay gaussiano,
# amostrando de uma distribuição normal

from netsquid.components.models.delaymodels import GaussianDelayModel
#                         GaussianDelayModel(delay_mean, delay_std, [rng], **kwargs)
# delay_mean -> média do atraso; delay_std -> desvio padrão do atraso; rng -> gerador de
# números aleatórios
modelo_atraso_gaussiano = GaussianDelayModel(delay_mean=5, delay_std=0.1)
# O FibreDelayModel modela o atraso presente em canais de fibra óptica. Dependendo da
# velocidade da luz na fibra e do comprimento do canal
# O comprimento do canal é uma propriedade que pode ser definida na inicialização do objeto
Channel("CanalTutorial", length=10)
# ou modificado após a inicialização
canal.properties['length'] = 10
separador()
# As propriedades necessárias para uso de um modelo são definidas no atributo required_properties
from netsquid.components.models.delaymodels import FibreDelayModel
modelo_atraso = FibreDelayModel()
print(f"A velocidade da luz na fibra: {modelo_atraso.properties['c']:.1f} [km/s]")
print("Propriedades obrigatórias no modelo de delay FibreDelayModel")
print(modelo_atraso.required_properties)

# Naturalmente, além de usar canais para enviar mensagens clássicas, queremos transmitir
# qubits (Qubit). Para isso, é necessário que o canal modele não só o atraso, mas qualquer
# ruído ou perda (atenuação) quântica que os qubits experimentam por conta das características
# físicas do canal. Para esse propósito, há o canal quântico (QuantumChannel), usado apenas
# para transmissão de qubits. Assim, o canal quântico deve especificar dois tipos de modelos:
#   - modelo de ruído quântico (quantum_noise_model)
#   - modelo de perda quãntica (quantum_loss_model)
# Ambos devem ser do tipo QuantumErrorModel (modelo de erro quântico), uma classe genérica
# capaz de modelar ruído e perdas. A diferença técnica entre esses dois fenômenos é:
# a perda é aplicada à mensagem antes da transmissão, o ruído é aplicado imediatamente
# antes da sua recepção.
# Um exemplo de modelo de perda é o FibreLossModel
from netsquid.components.models.qerrormodels import FibreLossModel
from netsquid.components.qchannel import QuantumChannel
#              FibreLossModel([p_loss_init, [p_loss_length], [rng])
# p_loss_init -> probabilidade inicial de perder um fóton assim que entrar n ocanal por conta
# da conversão de frequência
# p_loss_length -> probabilidade de sobrevivência do fóton por comprimento do canal [dB/km]
modelo_perda = FibreLossModel(p_loss_init=0.83, p_loss_length=0.2)
canalq = QuantumChannel("MeuCanalQ", length=20, models={'quantum_loss_model': modelo_perda})

# A título de informação, também existe a classe base de canal clássico (ClassicalChannel)
# para transmitir informação clássica, na qual também é possível aplicar modelos de ruído
# e perdas

# Memória quântica
#   O componente projetado para lidar com armazenamento de qubits (QuantumMemory) levando em 
#   conta os efeitos de decoerência.
from netsquid.components import QuantumMemory
memoriaq = QuantumMemory(name="MinhaMemoria", num_positions=1)
# Esta possui posições de memória (MemoryPosition) para guardar os qubits. Podemos adicionar 
# modelos de erro para as posições de memória que aplicarão ruído aos qubits (opcionalmente) 
# proporcionalmente ao tempo inativo. Por exemplo, vamos considerar o modelo de ruído de 
# despolarização (DepolarNoiseModel).
# A velocidade com que a despolarização ocorre é chamada taxa de despolarização (depolar_rate)
# , a qual, para um valor de 1MHz (por exemplo) significa que após um microssegundo, há uma 
# probabilidade de 63% de despolarização.
from netsquid.components.models.qerrormodels import DepolarNoiseModel
ruido_depolar = DepolarNoiseModel(depolar_rate=1e6) # a taxa é em Hz
# Uma memória quântica pode possuir múltiplas posições de memória, às quais podem ser 
# atribuídos modelos únicos de erro, podendo especificar na inicialização:
memq = QuantumMemory("MemoriaDepolar", num_positions=2,
                     memory_noise_models=[ruido_depolar, ruido_depolar])
# Ou ainda, pode-se atribuir o modelo às posições de memória da seguinte forma:
for pos_mem in memq.mem_positions:
    pos_mem.models['noise_model'] = ruido_depolar

# put() - insere um qubit na memória
# pop() - retira um qubit da memória
# peek() - verifica se o qubit está na memória (ótimo para debug)
separador()
from netsquid.qubits.qubitapi import create_qubits
print("Memória antes da inserção de qubits")
def imprime_memoria():
    for i in range(len(memq.mem_positions)):
        print(f"Posição {i} : {memq.peek(i)}")
imprime_memoria()
qubits = create_qubits(1)
separador()
print(f"Qubit criado: {qubits}")
memq.put(qubits)
separador()
print(f"Memória após a inserção do qubit")
imprime_memoria()
print(f"memq.peek(0) -> retorna o elemento 0 da memória -> {memq.peek(0)}")
memq.pop(positions=0)
separador(80)
print(f"Memória após o comando memq.pop(positions=0)")
imprime_memoria()
print(f"memq.peek(0) -> {memq.peek(0)}")

# A memória quântica também pode ser usada para realizar operações instantâneas nos qubits.
# Isto é diferente de aplicar portas quânticas aos qubits, o que será explicado na seção
# de processadores quânticos. Para operar, selecionamos um qubit, e escolhemos uma operação
# para aplicar. Por exemplo, uma porta X:
import netsquid.qubits.operators as ops 
separador()
print(f"O qubit {qubits} é colocado de volta na memória usando memq.put(qubits).")
memq.put(qubits)
imprime_memoria()
separador()
print("Estado do qubit:")
print(qubits[0].qstate.qrepr)
separador()
memq.operate(ops.X, positions=0) # no tutorial oficial é usado [0]
# o atributo positions pode ser uma lista de posições ou uma posição da memória
print("Memória após a aplicação da porta X na posição zero:")
imprime_memoria()
separador()
print("Estado do qubit após operação:")
print(qubits[0].qstate.qrepr)
separador()

# Por fim, a memória também pode realizar medições nos qubits. O resultado da medição
# contém duas listas de informação: 
#       1. o resultado da medição para cada qubit
#       2. a probabilidade de cada resultado
print(f"Medição na posição 0 da memória (memq.measure(positions=0)):\n"\
      f" {memq.measure(positions=0)}")
# Também é possível mudar a base de medição:
print(f"Medição na posição 0 na base X (memq.measure(positions=0, observable=ops.X)):\n"\
      f" {memq.measure(positions=0, observable=ops.X)}")
