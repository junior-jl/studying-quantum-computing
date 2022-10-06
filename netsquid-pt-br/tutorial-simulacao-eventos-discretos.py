# Tutorial Netsquid - Simulação de eventos discretos
# A ideia dessa seção é estender a simulação do teleporte 
# com um modelo temporal usando a engine pydynaa para
# simulação de eventos discretos

def separador(tamanho = 50):
    """Separador básico de texto para melhor visualização."""
    print('*', end='')
    for i in range(tamanho):
        print('-', end='')
    print('*')

# O pacote pyDynAA define classes que representam alguns conceitos essenciais:
#   - entidades (Entity)
#   - eventos (Event)
#   - tipo específico de evento (EventType)
#   - expressões de evento usadas para descrever combinações lógicas (EventExpression)
#   - manipuladores (?) de eventos que respondem a eventos (EventHandler e ExpressionHandler)
#   - mecanismo de simulação que lida com a marcação de eventos e registros (SimulationEngine)

# As entidades são qualquer coisa no mundo da simulação que possam gerar resposta a eventos.
# A classe base Entity fornece métodos para marcar eventos e esperar por estes.
# Eventos marcados ocorrerão em dados momentos na linha do tempo da simulação.
# O mecanismo de simulação roda 'saltando' sequencialmente de evento a evento discretamente.
# Uma entidade responde a eventos registrando um objeto manipulador de evento com uma função
# callback para esperar por eventos de um tipo específico (ou não), fonte, e id serem provocados.
# Checar imagem: https://docs.netsquid.org/latest-release/_images/pydynaa.png

# Funções do mecanismo de simulação:
#   - sim_run()
#   - sim_reset()
#   - sim_time()
#   Ver mais no módulo simtools

# Vamos considerar um exemplo de um jogo de ping pong jogado com um qubit, similar 
# ao tutorial de 10 minutos do Netsquid. 

# Importamos os pacotes Netsquid e pyDynAA
import netsquid as ns
import pydynaa

# Para que os resultados sejam os mesmos, vamos fixar a seed para o gerador de números aleatórios
ns.set_random_state(seed=42)

# Criaremos duas entidades de simulação PingEntity e PongEntity, ambas subclasses da classe Entity
# Nossas entidades tomarão turnos para reagir aos eventos ping ou pong da outra e medir um qubit
# compartilhado na base padrão ou de Hadamard, respectivamente.

class EntidadePing(pydynaa.Entity):
                 #pydynaa.EventType(nome, descrição)
    tipo_ev_ping = pydynaa.EventType("EVENTO_PING", "Um evento ping.")
    atraso = 10.

    def inicia(self, qubit):
        # Começa o jogo marcando o primeiro evento ping depois do delay
        self.qubit = qubit
        # Basicamente marca um evento do tipo event_type após um dado intervalo)
        #    _schedule_after(intervalo, event_type)
        self._schedule_after(self.atraso, EntidadePing.tipo_ev_ping)

    def espera_por_pong(self, entidade_pong):
        # Configura essa entidade para 'escutar' eventos pong de uma EntidadePong
        #                  pydynaa.EventHandler(função callback)
        manipulador_pong = pydynaa.EventHandler(self._lida_com_evento_pong)
        #Entity._wait(manipulador, [entidade], [tipo de evento], [evento], ...)
        self._wait(manipulador_pong, entity=entidade_pong,
                   event_type=EntidadePong.tipo_ev_pong)

    def _lida_com_evento_pong(self, evento):
        # Função callback chamada pelo manipualor pong quando um evento pong é provocado
        m, prob = ns.qubits.measure(self.qubit, observable=ns.Z)
        labels_z = ("|0>", "|1>")
        # netsquid.util.simtools.sim_time([magnitude] padrão = nanossegundos)
        # retorna o tempo atual de simulação
        print(f"{ns.sim_time():.1f}: Evento pong! EntidadePing mediu "
              f"{labels_z[m]} com probabilidade {prob:.2f}")
        # Após a medição do qubit enviado pela EntidadePong, é marcado um novo evento
        # do tipo tipo_ev_ping
        self._schedule_after(EntidadePing.atraso, EntidadePing.tipo_ev_ping)

class EntidadePong(pydynaa.Entity):
    tipo_ev_pong = pydynaa.EventType("EVENTO_PONG", "Um evento pong.")
    atraso = 10.

    def espera_por_ping(self, entidade_ping):
        # Configura essa entidade para 'escutar' eventos ping de uma EntidadePing
        manipulador_ping = pydynaa.EventHandler(self._lida_com_evento_ping)
        self._wait(manipulador_ping, entity=entidade_ping,
                   event_type=EntidadePing.tipo_ev_ping)
        # Esse método faz a EntidadePong esperar continuamente por eventos correspondentes
        # Caso quiséssemos esperar e lidar somente com o primeiro evento do tipo podíamos
        # usar o método _wait_once()

    def _lida_com_evento_ping(self, evento):
        # Função callback chamada pelo manipulador ping quando um evento ping é provocado
        # Event.source -> a entidade fonte que iniciou o evento
        m, prob = ns.qubits.measure(evento.source.qubit, observable=ns.X)
        # A fonte do evento (EntidadePing) é usada para que a EntidadePong possa acessar
        # o qubit compartilhado
        labels_x = ("|+>", "|->")
        print(f"{ns.sim_time():.1f}: Evento ping! EntidadePong mediu "
              f"{labels_x[m]} com probabilidade {prob:.2f}")
        self._schedule_after(EntidadePong.atraso, EntidadePong.tipo_ev_pong)

# Criar entidades e registra-las em relação a outra
ping = EntidadePing()
pong = EntidadePong()
ping.espera_por_pong(pong)
pong.espera_por_ping(ping)

# Criar um qubit e instruir a entidade ping a iniciar o processo
q1, = ns.qubits.create_qubits(1)

# TODO: entender isso q1, ??????

# O jogo é iniciado, mas a simulação ainda não está rodando...
ping.inicia(q1)
# A entidade ping foi configurada para 'escutar' e reagir a eventos pong, a única diferença
# é que esta medirá o qubit na base padrão. Esse jogo de ping pong quântico continuará
# indefinidamente, já que novos eventos são gerados dinamicamente depois de cada ping e pong

# netquid.util.simtools.sim_run([tempo_final], [duração], [magnitude])
# Roda a simulação... caso tempo_final ou duração não sejam setados, então a simulação irá
# rodar até que não hajam mais eventos marcados na linha do tempo.
estatisticas = ns.sim_run(end_time=91)
# A função run retorna um objeto SimStats que guarda estatísticas interessantes da simulação.
print(estatisticas)
# Podemos ver que a simulação realmente durou 91 nanossegundos e que exatamente 9 eventos foram
# marcados e lidados. Houveram 9 operações quânticas, as medições, e o máximo tamanho de estado
# quântico operado foi 1 qubit, como esperado.

#### Exemplo simples de teleporte quântico

# Primeiro, resetamos a linha do tempo da simulação, limpando qualquer evento e setando o 
# tempo de simulação de volta a zero

ns.sim_reset()

# Agora definimos três entidades de simulação: Alice, Bob, e Charlie. Charlie será responsável
# por gerar continuamente u mpar de qubits emaranhados (o estado de Bell |B00>), sendo um qubit
# para Alice e o outro para Bob. Alice espera o seu qubit emaranhado chegar, ao chegar, ela 
# emaranha seu próprio qubit com o que acabou de receber, mede ambos e envia as correções
# clássicas para Bob. Bob irá simultaneamente esperar pelo qubit emaranhado de Charlie e as
# correções clássicas de Alice. Para isso iremos usar expressões de evento (EventExpression)
# Ver imagem: https://docs.netsquid.org/latest-release/_images/aafig-68b936f1a385af8661132617442f6cf318b973f5.svg

class Charlie(pydynaa.Entity):
    tipo_ev_pronto = pydynaa.EventType("QUBITS_PRONTOS", "Qubits emaranhados estão prontos.")
    _tipo_ev_gerar = pydynaa.EventType("GERAR", "Gerar qubits emaranhados.")
    periodo = 50.
    atraso = 10.

    def __init__(self):
        # Inicializa Charlie emaranhando qubits após cada geração de evento
        self.qubits_emaranhados = None
        self._manipulador_geracao = pydynaa.EventHandler(self._emaranha_qubits)
        self._wait(self._manipulador_geracao, entity=self,
                   event_type=Charlie._tipo_ev_gerar)

    def _emaranha_qubits(self, event):
        # Função callback que emaranha qubits e marca um evento PRONTO
        qb1, qb2 = ns.qubits.create_qubits(2)
        # Gerar o estado de Bell a partir de uma porta Hadamard e uma CNOT
        #         operate(qubits, operador)
        ns.qubits.operate(qb1, ns.H)
        ns.qubits.operate([qb1, qb2], ns.CNOT)
        self.qubits_emaranhados = [qb1, qb2]
        # Após a geração, marcar evento do tipo PRONTO após atraso
        self._schedule_after(Charlie.atraso, Charlie.tipo_ev_pronto)
        print(f"{ns.sim_time():.1f}: Charlie terminou de gerar emaranhamento!")
        # Após anunciar que o par está pronto, marcar evento do tipo GERAR novamente
        # para ocorrer depois de um certo período (aqui, 50 ns)
        self._schedule_after(Charlie.periodo, Charlie._tipo_ev_gerar)
        
    def inicia(self):
        # Começa a geração de emaranhamento
        print(f"{ns.sim_time():.1f} Charlie iniciou a geração de emaranhamento.")
        self._schedule_now(Charlie._tipo_ev_gerar)

# Aqui foram definidos dois tipos de eventos: um privado usado para simular uma frequência
# na geração de emaranhamento e um público usado para sinalizar a geração bem sucedida para
# Alice e Bob. A função callback de _manipulador_geracao() marca um evento do tipo PRONTO
# depois de um atraso e marca o próximo evento de geração

# A classe entidade Alice define o evento público tipo_ev_pronto e privado _tipo_ev_teleporte
# O primeiro comunica a Bob que suas correções estão prontas, o último é usado para simular
# um atraso na operação de teleporte local de Alice.

class Alice(pydynaa.Entity):
    tipo_ev_pronto = pydynaa.EventType("CORRECOES_PRONTAS", "As correções estão prontas.")
    _tipo_ev_teleporte = pydynaa.EventType("TELEPORTE", "Teleporta o qubit.")
    atraso = 20.

    def __init__(self, estado_teleporte):
        # Inicializa Alice setando o estado de teleporte e esperando o teleporte
        self.estado_teleporte = estado_teleporte
        self.qb0 = None
        self.qb1 = None
        self.corrections = None
        self._manipulador_teleporte = pydynaa.EventHandler(self._lide_com_teleporte)
        self._wait(self._manipulador_teleporte, entity=self,
                   event_type=Alice._tipo_ev_teleporte)

    def espera_por_charlie(self, charlie):
        # Configura Alice para esperar por um qubit emaranhado de Charlie
        self._manipulador_qubit = pydynaa.EventHandler(self._lide_com_qubit)
        self._wait(self._manipulador_qubit, entity=charlie,
                   event_type=Charlie.tipo_ev_pronto)

    def _lide_com_qubit(self, evento):
        # Função callback que lida com a chegada de qubits emaranhados e marca teleporte
        # Qubit 0 de Alice é o que deve ser teleportado para Bob
        self.qb0, = ns.qubits.create_qubits(1, no_state = True)
        # Qubit 1 de Alice é o primeiro do par de qubits emaranhados de Charlie
        self.qb1 = evento.source.qubits_emaranhados[0]
        #         assign_qstate(qubit, qrepr, [formalismo])
        ns.qubits.assign_qstate([self.qb0], self.estado_teleporte)
        self._schedule_after(Alice.atraso, Alice._tipo_ev_teleporte)
        print(f"{ns.sim_time():.1f}: Alice recebeu o qubit emaranhado!")

    def _lide_com_teleporte(self, evento):
        # Função callback que faz o teleporte e marca um evento de correções prontas
        # Alice emaranha seus qubits
        ns.qubits.operate([self.qb0, self.qb1], ns.CNOT)
        ns.qubits.operate(self.qb0, ns.H)
        m0, __ = ns.qubits.measure(self.qb0)
        m1, __ = ns.qubits.measure(self.qb1)
        self.correcoes = [m0, m1]
        self._schedule_now(Alice.tipo_ev_pronto)
        print(f"{ns.sim_time():.1f}: Alice mediu qubits e está enviando correções.")


# Bob deve esperar tanto pelo qubit emaranhado de Charlie e as correções de Alice, finalizando
# a tarefa do teleporte aplicando as possíveis correções ao seu qubit local.

class Bob(pydynaa.Entity):

    def espera_por_teleporte(self, alice, charlie):
        # Configura Bob para esperar pelo seu qubit emaranhado e as correções de Alice
        # pydynaa.core.EventExpression([source], [event_type], [event_id])
        expressao_ev_charlie_pronto = pydynaa.EventExpression(
                source=charlie, event_type=Charlie.tipo_ev_pronto)
        expressao_ev_alice_pronto = pydynaa.EventExpression(
                source=alice, event_type=Alice.tipo_ev_pronto)
        expressao_ev_ambos_prontos = expressao_ev_charlie_pronto & expressao_ev_alice_pronto
        self._manipulador_teleporte = pydynaa.ExpressionHandler(self._lida_com_teleporte)
        self._wait(self._manipulador_teleporte, expression=expressao_ev_ambos_prontos)

    def _lida_com_teleporte(self, expressao_evento):
        # Função callback que lida com mensagens de Alice e Charlie
        # first_term = primeiro termo da expressão de evento
        # atomic_source = a entidade fonte da expressão atômica
        # Expressões podem ser atômicas ou compostas
        # Uma expressão atômica descreve futuros eventos similarmente a um _wait():
        # usando a fonte, tipo e id dos eventos, opcionalmente.
        # Uma expressão composta combina duas expressões atômicas ou compostas com um
        # AND ou OR lógico

        # Pegando o segundo qubit de Charlie (first_term.atomic_source)
        qubit = expressao_evento.first_term.atomic_source.qubits_emaranhados[1]
        alice = expressao_evento.second_term.atomic_source
        self._aplica_correcoes(qubit, alice.correcoes)

    def _aplica_correcoes(self, qubit, correcoes):
        # Aplica correções de teleporte e checa fidelidade
        m0, m1 = correcoes
        # Se [m0 m1]:
        #   00: não faz nada
        #   01: aplica porta X
        #   10: aplica porta Z
        #   11: aplica XZ
        if m1:
            ns.qubits.operate(qubit, ns.X)
        if m0:
            ns.qubits.operate(qubit, ns.Z)
        #                      fidelity(qubits, estado_referencia, [squared(quadrado)])
        fidelidade = ns.qubits.fidelity(qubit, alice.estado_teleporte, squared=True)
        print(f"{ns.sim_time():.1f}: Bob recebeu o qubit emaranhado e correções!"
                f" Fidelidade = {fidelidade:.3f}")

# Vamos configurar a rede
# Alice deve enviar o estado quântico |-> para Bob

def configura_rede(alice, bob, charlie):
    alice.espera_por_charlie(charlie)
    bob.espera_por_teleporte(alice, charlie)
    charlie.inicia()

alice = Alice(estado_teleporte=ns.h1)
bob = Bob()
charlie = Charlie()

configura_rede(alice, bob, charlie)
estatisticas2 = ns.sim_run(end_time=100)
print(estatisticas2)

# Podemos ver que o máximo tamanho de estado quântico foi 3, ocorrendo quando Alice 
# emaranha seu qubit com o qubit já emaranhado recebido de Charlie

# Finalizando, vamos adicinoar ruído dependente do tempo ao qubit de Bob
# Calcularemos a diferença de tempo entre a chegada do qubit de Bob e o tempo atual
# de simulação e passaremos para a função delay_depolarize()

class BobRuidoso(Bob):
    taxa_depolar = 1e7 # taxa de depolarização dos qubits que esperam [Hz]

    def _lide_com_teleporte(self, expressao_evento):
        # Função callback que primeiro aplica ruído ao qubit antes das correções
        expr_alice = expressao_evento.second_term
        expr_charlie = expressão_evento.first_term
        # Computa o tempo que o qubit recebido de Charlie esperou
        atraso = ns.sim_time() - expr_charlie.triggered_time
        # Aplice ruído quântico dependente de tempo ao qubit de Bob
        qubit = expr_charlie.atomic_source.qubits_emaranhados[1]
        ns.qubits.delay_depolarize(qubit, BobRuidoso.taxa_depolar, atraso)
        # Aplica correções clássicas (como antes)
        self._aplica_correcoes(qubit, expr_alice.atomic_source.correcoes)

# Para visualizar imediatamente o efeito na fidelidade, trocaremos o formalismo para
# matriz densidade
# Resetando a simulação...
ns.sim_reset()
ns.set_qstate_formalism(ns.QFormalism.DM)

alice = Alice(estado_teleporte=ns.h1)
bob = BobRuidoso()
charlie = Charlie()
configura_rede(alice, bob, charlie)
estatisticas3 = ns.sim_run(end_time=50)
print(estatisticas3)
