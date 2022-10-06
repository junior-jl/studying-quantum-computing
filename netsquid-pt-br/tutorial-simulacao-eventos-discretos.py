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

    def _lida_com_evento_ping(self, event):
        # Função callback chamada pelo manipulador ping quando um evento ping é provocado
        # Event.source -> a entidade fonte que iniciou o evento
        m, prob = ns.qubits.measure(event.source.qubit, observable=ns.X)
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
