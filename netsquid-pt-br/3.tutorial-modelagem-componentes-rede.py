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
import pydynaa
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

# Portas
#   Para simular o jogo de ping pong quântico do tutorial passado, queremos que o qubit seja
#   fisicamente transportado entre os dois jogadores usando canais, e que o qubit seja
#   automaticamente transportado do canal para a memória quântica quando chegar.
#   O canal e a memória quântica são componentes e todos os componentes compartilham a mesma
#   interface de comunicação, as portas (Port).
#   Checar imagem: https://docs.netsquid.org/latest-release/_images/ports_connect.png
#   Os métodos send() e receive() usados anteriormente da classe Canal são métodos
#   convenientes que usam as portas send e recv de um canal, respectivamente. Logo, ao invés
#   de usar esses métodos, poderíamos fazer:
separador()
canal = Channel("CanalTutorial", delay=3)
canal.ports['send'].tx_input("hello")
ns.sim_run()
x = canal.ports['recv'].rx_output()
print(x)

# Portas transmitem (TX) e recebem (RX) objetos mensagem (Message). Uma mensagem é composta
# de uma lista de itens e um dicionário opcional de campos de metadados.
# Além disso, portas sempre são atreladas a um componente, logo, há uma distinção entre:
#   - tx_input() -> transmitir uma mensagem para dentro de um componente
#   - tx_output() -> transmitir uma mensagem para fora de um componente
#   - rx_output() -> receber uma mensagem saída de um componente
#   - rx_input() -> receber uma mensagem entrada de um componente
# A conexão entre duas portas pode ser feita pelo método connect(), o qual irá passar a 
# saída transmitida de uma porta para a entrada recebida de outra, e vice-versa.
# No jogo de PingPong, usamos put() para armazenar um qubit. Uma alternativa para isso
# é enviar uma mensagem contendo uma lista de qubits para a porta qin da memória, ou uma
# mensagem com um único qubit para uma porta específica qinX, onde X é o índice de uma posição
# de memória específica. Quando essa porta for conectada à porta de recepção do canal, o qubit
# que chegar será automaticamente armazenado.
separador()
print("Armazenando o qubit enviado pelo canal na memória por meio de portas...")
canal.ports['recv'].connect(memq.ports['qin0'])
qubit, = create_qubits(1)
print(f"Qubit criado: {qubit}")
canal.send(qubit)
ns.sim_run()
print(f"Posição de memória 0 da memória conectada ao canal pela porta qin0: {memq.peek(0)}")

# Usando componentes e portas, vamos reescrever as entidades Ping e Pong, no entanto, agora
# elas terão uma memória quântica cuja porta de saída está conectada à entrada de um canal
# quântico. Assim, ao invés de esperarem por um evento ping ou pong, irão esperar a chegada
# de um qubit na porta de entrada qin0 da memória quântica.

from netsquid.components.component import Port
from netsquid.qubits.qformalism import QFormalism
class EntidadePing(pydynaa.Entity):
    comprimento = 2e-3  # comprimento do canal [km]

    def __init__(self):
        # Cria uma memória e um canal quântico
        self.memoriaq = QuantumMemory("MemoriaPing", num_positions=1)
        self.canalq = QuantumChannel("CanalPing", length=self.comprimento,
                                     models={"delay_model": FibreDelayModel()})
        # Conectar a saída da memória à entrada do canal ping
        self.memoriaq.ports["qout"].connect(self.canalq.ports["send"])
        # Configura função callback para lidar com a entrada na porta qin0 da memória
        # A transmissão de uma mensagem de entrada tx_input() marca um evento do tipo 
        # evtype_input
        self._wait(pydynaa.EventHandler(self._lida_com_qubit_entrada),
                     entity=self.memoriaq.ports["qin0"], event_type=Port.evtype_input)
        # notify_all_input = True -> sempre marca um evento de entrada quando essa porta
        # é conectada, encaminhada ou vinculada
        self.memoriaq.ports["qin0"].notify_all_input = True

    def inicia(self, qubit):
        # Começa o jogo fazendo do jogador ping enviar o primeiro qubit (ping)
        self.canalq.send(qubit)

    def espera_por_pong(self, outra_entidade):
        # Configura essa entidade para colocar qubits que chegarem na memória quântica
        # Conecta a porta de recepção (ponto de chegada) do canal da outra entidade a
        # porta da sua posição zero da memória quântica
        self.memoriaq.ports["qin0"].connect(outra_entidade.canalq.ports["recv"])

    def _lida_com_qubit_entrada(self, evento):
        # Função callback chamada pelo manipulador de pong quando um evento pong é provocado
        [m], [prob] = self.memoriaq.measure(positions=[0], observable=ns.Z)
        labels_z = ("|0>", "|1>")
        print(f"{ns.sim_time():.1f}: Evento Pong! A EntidadePing mediu "
                                      f"{labels_z[m]} com probabilidade {prob:.2f}")
        self.memoriaq.pop(positions=[0])

class EntidadePong(pydynaa.Entity):
    comprimento = 2e-3  # comprimento do canal [km]

    def __init__(self):
        # Cria uma memória e um canal quântico
        self.memoriaq = QuantumMemory("MemoriaPong", num_positions=1)
        self.canalq = QuantumChannel("CanalPong", length=self.comprimento,
                                     models={"delay_model": FibreDelayModel()})
        # Conectar a saída da memória para a entrada do canal pong
        self.memoriaq.ports["qout"].connect(self.canalq.ports["send"])
        # Configura a função callback para ldiar com a entrada na memória quântica
        self._wait(pydynaa.EventHandler(self._lida_com_qubit_entrada),
                     entity=self.memoriaq.ports["qin0"], event_type=Port.evtype_input)
        self.memoriaq.ports["qin0"].notify_all_input = True

    def espera_por_ping(self, outra_entidade):
        # Configura essa entidade para passar qubits recebidos para a memória quântica
        self.memoriaq.ports["qin0"].connect(outra_entidade.canalq.ports["recv"])

    def _lida_com_qubit_entrada(self, evento):
        # Função callback chamada pelo manipulador de ping quando um evento ping é provocado
        [m], [prob] = self.memoriaq.measure(positions=[0], observable=ns.X)
        labels_x = ("|+>", "|->")
        print(f"{ns.sim_time():.1f}: Evento ping! EntidadePong mediu "
              f"{labels_x[m]} com probabilidade {prob:.2f}")
        self.memoriaq.pop(positions=[0])

# Podemos notar que as entidades são muito parecidas, e poderíamos ter escrito apenas uma classe
# Mas, por motivos de clareza, foram definidas duas classes separadas.
# A simulação fica:
separador()
print("Nova simulação do jogo de Ping Pong quântico")
ns.sim_reset()
ping = EntidadePing()
pong = EntidadePong()
ping.espera_por_pong(pong)
pong.espera_por_ping(ping)
# Cria um qubit e instrui a entidade ping a iniciar o processo
qubit, = ns.qubits.create_qubits(1)
ping.inicia(qubit)
ns.set_random_state(seed=42)
estatisticas = ns.sim_run(91)
print(estatisticas)

# Teleporte quântico utilizando componentes
# Resetando a simulação e trocando o formalismo para matriz densidade para demonstrar os efeitos do
# ruído na fidelidade final sem a necessidade de amostragem...
ns.set_qstate_formalism(ns.QFormalism.DM)
ns.sim_reset()

# Alice e Bob agora possuem uma memória para armazenar e manipular seus qubits. Além disso, serão
# inicializados com as portas send e receive do canal clássico que usam para trocar a informação
# clássica sobre correções. 

class Alice(pydynaa.Entity):
    def __init__(self, estado_teleporte, canalc_porta_send):
        self.estado_teleporte = estado_teleporte
        self.canalc_porta_send = canalc_porta_send
        self.memoriaq = QuantumMemory("MemoriaAlice", num_positions=2)
        self._wait(pydynaa.EventHandler(self._lida_com_qubit_entrada),
                   entity=self.memoriaq.ports["qin1"], event_type=Port.evtype_input)
        self.memoriaq.ports["qin1"].notify_all_input = True

    def _lida_com_qubit_entrada(self, evento):
        # Função callback que faz o teleporte e marca um evento de correções prontas
        q0, = ns.qubits.create_qubits(1, no_state=True)
        # q0 -> Qubit de Alice com o estado a ser teleportado
        ns.qubits.assign_qstate([q0], self.estado_teleporte)
        self.memoriaq.put([q0], positions=[0])
        separador()
        print("Estado a ser teleportado")
        print(self.memoriaq.peek(positions=[0])[0].qstate.qrepr)
        # Emaranha os qubits nas posições 0 e 1 da memória
        self.memoriaq.operate(ns.CNOT, positions=[0, 1])
        self.memoriaq.operate(ns.H, positions=[0])
        # Realiza a medição dos qubits, pega o retorno[0] -> lista de medições
        # retorno[1] seria a lista de probabilidades
        m0, m1 = self.memoriaq.measure(positions=[0, 1], observable=ns.Z,
                                       discard=True)[0]
        # Coloca na entrada da porta de transmissão as medições feitas nos qubits
        # emaranhados q0 e q1
        self.canalc_porta_send.tx_input([m0, m1])
        separador()
        print(f"{ns.sim_time():.1f}: Alice recebeu o qubit emaranhado, "
              f"mediu os qubits e está enviando as correções!")
        print(f"Correções enviadas -> {[m0, m1]}")
        separador()


class Bob(pydynaa.Entity):
    taxa_depolar = 1e7  # taxa de despolarização dos qubits inativos [Hz]

    def __init__(self, canalc_porta_recv):
        modelo_ruido = DepolarNoiseModel(depolar_rate=self.taxa_depolar)
        self.memoriaq = QuantumMemory("MemoriaBob", num_positions=1,
                                      memory_noise_models=[modelo_ruido])
        # Ligamos o manipulador de mensagens à porta de recepção do canal
        # clássico ligado a Bob
        canalc_porta_recv.bind_output_handler(self._lida_com_correcoes)

    def _lida_com_correcoes(self, mensagem):
        # Função callback que lida com mensagens de Alice e Charlie
        m0, m1 = mensagem.items
        if m1:
            self.memoriaq.operate(ns.X, positions=[0])
            separador()
            print("Foi aplicada uma porta X na posição zero da memória de Bob!")
        if m0:
            self.memoriaq.operate(ns.Z, positions=[0])
            separador()
            print("Foi aplicada uma porta Z na posição zero da memória de Bob!")
        qubit = self.memoriaq.pop(positions=[0])
        fidelidade = ns.qubits.fidelity(qubit, ns.y0, squared=True)
        separador()
        print(f"{ns.sim_time():.1f}: Bob recebeu o qubit emaranhado e as correções!"
              f" Fidelidade = {fidelidade:.3f}")
        print(f"Qubit de Bob após aplicação das correções: "
              f"{qubit[0].qstate.qrepr}")

# Na simulação anterior, havia uma entidade Charlie que gerava o emaranhamento e enviava
# os qubits a Alice e Bob, agora um novo componente irá substituir essa entidade: uma fonte
# quântica (QSource), que será conectada a Alice e Bob por meio de canais quânticos.
# Uma fonte quântica gera um ou mais qubits em estados específicos ou aleatoriamente amostrados,
# neste último caso, é possível usar um objeto amostrador de estados (StateSampler).
# Este objeto é inicializado com uma lista de estados e probabilidades. Um estado aleatório desta
# lista pode ser amostrado pelo método sample(). Neste exemplo, sempre queremos o estado |B00>...
from netsquid.qubits.state_sampler import StateSampler
import netsquid.qubits.ketstates as ks
amostrador_estados = StateSampler([ks.b00], [1.0])

from netsquid.components.qsource import QSource, SourceStatus
# Queremos enviar os dois qubits gerados para duas direções diferentes, logo, especificamos duas
# portas dde saída no construtor da fonte com os nomes padrão qout0 e qout1
fonte_charlie = QSource("Charlie", amostrador_estados, frequency=100, num_ports=2,
                        timing_model=FixedDelayModel(delay=50),
                        status=SourceStatus.INTERNAL)

# A fonte quântica pode estar em um dos três modos especificados por SourceStatus:
#   - OFF (padrão)
#   - INTERNAL
#   - EXTERNAL
# No modo interno, a fonte opera usando seu componente clock interno (Clock), que pode ser
# inicializado usando os parâmetros frequency ou timing_model.
# No modo externo, a fonte espera ser externamente provocada recebendo alguma mensagem na sua porta
# gatilho (trigger). Também é possível chamar trigger() manualmente para emular uma mensagem
# chegando na porta. No exemplo acima, escolhemos usar o clock interno com um delay de 50ns
# (frequência de 20 GHz).
# Para configurar a rede, conectamos as portas de saída da fonte a dois canais quânticos
# unilaterais, os quais serão conectados às entradas das memórias quânticas de Alice e Bob.

def configura_rede(alice, bob, fonteq, comprimento=4e-3):
    canalq_c_para_a = QuantumChannel("Charlie->Alice", length=comprimento / 2,
                                     models={"delay_model": FibreDelayModel()})
    canalq_c_para_b = QuantumChannel("Charlie->Bob", length=comprimento / 2,
                                     models={"delay_model": FibreDelayModel()})
    fonteq.ports["qout0"].connect(canalq_c_para_a.ports["send"])
    fonteq.ports["qout1"].connect(canalq_c_para_b.ports["send"])
    alice.memoriaq.ports["qin1"].connect(canalq_c_para_a.ports["recv"])
    bob.memoriaq.ports["qin0"].connect(canalq_c_para_b.ports["recv"])

# Agora podemos criar as entidades Alice e Bob juntas com um canal clássico entre elas, e chamar
# o configurador de rede
separador()
print("Simulação do teleporte com componentes e portas")
separador()
from netsquid.components import ClassicalChannel
canalc = ClassicalChannel("CanalC", length=4e-3,
                          models={"delay_model": FibreDelayModel()})
alice = Alice(estado_teleporte=ns.y0, canalc_porta_send=canalc.ports["send"])
bob = Bob(canalc_porta_recv=canalc.ports["recv"])
separador()
print("Posição zero da memória de Bob antes da simulação")
print(bob.memoriaq.peek(positions=[0]))
separador()
configura_rede(alice, bob, fonte_charlie)
estatisticas = ns.sim_run(end_time=100)

# Por fim, podemos notar uma importante diferença em relação ao tutorial passado: o ruído
# é aplicado automaticamente pelas memórias quânticas

