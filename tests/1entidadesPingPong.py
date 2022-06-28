import netsquid as ns
import pydynaa
ns.set_random_state(seed=42)

class PingEntity(pydynaa.Entity):
    ping_evtype = pydynaa.EventType("PING_EVENT", "A ping event.")
    delay = 10.

    def start(self, qubit):
        # O "jogo" começa 'marcando' o evento do primeiro ping após o delay
        self.qubit = qubit
        self._schedule_after(self.delay, PingEntity.ping_evtype)

    def wait_for_pong(self, pong_entity):
        # Esta entidade irá 'ficar atenta' a eventos pong de uma entidade PongEntity
        pong_handler = pydynaa.EventHandler(self._handle_pong_event)
        self._wait(pong_handler, entity=pong_entity, event_type=PongEntity.pong_evtype)

    def _handle_pong_event(self, event):
        # Função callback chamada pelo pong handler quando um evento pong é provocado
        m, prob = ns.qubits.measure(self.qubit, observable=ns.Z)
        labels_z = ("|0>", "|1>")
        print(f"{ns.sim_time():.1f}: Evento pong! PingEntity mediu "
              f"{labels_z[m]} com probabilidade {prob:.2f}")
        self._schedule_after(PingEntity.delay, PingEntity.ping_evtype)


class PongEntity(pydynaa.Entity):
    pong_evtype = pydynaa.EventType("PONG_EVENT", "A pong event.")
    delay = 10.
   
    def wait_for_ping(self, ping_entity):
        # Esta entidade irá 'ficar atenta' a eventos ping de uma entidade PingEntity
        ping_handler = pydynaa.EventHandler(self._handle_ping_event)
        self._wait(ping_handler, entity=ping_entity, event_type=PingEntity.ping_evtype)

    def _handle_ping_event(self, event):
        # Função callback chamada pelo ping handler quando um evento ping é provocado
        m, prob = ns.qubits.measure(event.source.qubit, observable=ns.X)
        labels_x = ("|+>", "|->")
        print(f"{ns.sim_time():.1f}: Evento ping! PongEntity mediu "
              f"{labels_x[m]} com probabilidade {prob:.2f}")
        self._schedule_after(PongEntity.delay, PongEntity.pong_evtype)

# Criando as entidades
ping = PingEntity()
pong = PongEntity()
ping.wait_for_pong(pong)
pong.wait_for_ping(ping)

# Criando um qubit e dando a instrução para que a entidade ping inicie o processo.
qubit, = ns.qubits.create_qubits(1)
ping.start(qubit)

# Rodando simulação
stats = ns.sim_run(end_time=91)

# Imprimindo resumo da simulação
print(stats)
