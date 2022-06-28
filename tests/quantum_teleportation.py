import netsquid as ns
import pydynaa

class Eduardo(pydynaa.Entity):
        #     pydynaa.EventType(name, description)
    tipo_ok = pydynaa.EventType("QUBITS_OK", "Qubits emaranhados estao prontos.")
	# O underscore indica que o método é privado à entidade.
    _tipo_gerar = pydynaa.EventType("GERAR", "Gerar qubits emaranhados.")
    period = 50.
    delay = 10.

	# Inicializa Eduardo emaranhando qubits depois de cada evento gerador
    def __init__(self):
        self.qubits_emaranhados = None
	# O manipulador lida com um evento para uma Entidade usando uma função callback
	#			  pydynaa.EventHandler(callback_function, [id], [safe_guards])
        self._gerar_manipulador = pydynaa.EventHandler(self._emaranhar_qubits)
	#    _wait(handler, [entity], [event_type], [event], [event_id], [once], [expression])
	# Espera de si próprio um evento do tipo '_tipo_gerar'
        self._wait(self._gerar_manipulador, entity=self,
                   event_type=Eduardo._tipo_gerar)
	
	# Função callback que emaranha qubits e marca um evento para 'avisar' que o emaranhamento
	# está completo (tipo_ok)
    def _emaranhar_qubits(self, event):
	# Gera dois qubits
        q1, q2 = ns.qubits.create_qubits(2)
	# Aplicando Hadamard + CNOT -> estado de Bell
        ns.qubits.operate(q1, ns.H)
        ns.qubits.operate([q1, q2], ns.CNOT)
        self.qubits_emaranhados = [q1, q2]
	#    _schedule_after(interval(float), event_type)
	# Depois do delay, marca um evento do tipo 'tipo_ok'
        self._schedule_after(Eduardo.delay, Eduardo.tipo_ok)
        print(f"{ns.sim_time():.1f}: Eduardo gerou um par de qubits emaranhados!")
	# Depois do período, marca um evento do tipo '_tipo_gerar'
	# Continua gerando um par de qubits emaranhados a cada período
        self._schedule_after(Eduardo.period, Eduardo._tipo_gerar)

    def start(self):
        # Começa a gerar o emaranhamento
        print(f"{ns.sim_time():.1f}: Eduardo iniciou o processo de gerar o emaranhamento.")
	#    _schedule_now(event_type)
        self._schedule_now(Eduardo._tipo_gerar)


class Adauto(pydynaa.Entity):
    tipo_ok = pydynaa.EventType("CORRECAO_PRONTA", "Correcoes estao prontas")
    _tipo_teleporte = pydynaa.EventType("TELEPORTE", "Teleporte o qubit.")
    delay = 20.

    def __init__(self, estado_inicial):
	# Inicializa Adauto setando o estado inicial e esperando o teleporte
        self.estado_inicial = estado_inicial
        self.q0 = None
        self.q1 = None
        self.correcoes = None
        self._manipulador_teleporte = pydynaa.EventHandler(self._lide_com_teleporte)
        self._wait(self._manipulador_teleporte, entity=self,
                   event_type=Adauto._tipo_teleporte)

    def wait_for_Eduardo(self, Eduardo):
        # Setup Adauto to wait for an entanglement qubit from Eduardo
        self._qubit_handler = pydynaa.EventHandler(self._handle_qubit)
        self._wait(self._qubit_handler, entity=Eduardo,
                   event_type=Eduardo.tipo_ok)

    def _handle_qubit(self, event):
        # Callback function that handles arrival of entangled qubit
        # and schedules teleportation
        self.q0, = ns.qubits.create_qubits(1, no_state=True)
        self.q1 = event.source.qubits_emaranhados[0]
        ns.qubits.assign_qstate([self.q0], self.estado_inicial)
        self._schedule_after(Adauto.delay, Adauto._tipo_teleporte)
        print(f"{ns.sim_time():.1f}: Adauto received entangled qubit")

    def _lide_com_teleporte(self, event):
        # Callback function that does teleportation and schedules
        # a correcoes ready event
        ns.qubits.operate([self.q0, self.q1], ns.CNOT)
        ns.qubits.operate(self.q0, ns.H)
        m0, __ = ns.qubits.measure(self.q0)
        m1, __ = ns.qubits.measure(self.q1)
        self.correcoes = [m0, m1]
        self._schedule_now(Adauto.tipo_ok)
        print(f"{ns.sim_time():.1f}: Adauto measured qubits & sending correcoes")

class Junior(pydynaa.Entity):

    def wait_for_teleport(self, Adauto, Eduardo):
        # Setup Junior to wait for his entangled qubit and Adauto's correcoes
        Eduardo_ready_evexpr = pydynaa.EventExpression(
            source=Eduardo, event_type=Eduardo.tipo_ok)
        Adauto_ready_evexpr = pydynaa.EventExpression(
            source=Adauto, event_type=Adauto.tipo_ok)
        both_ready_evexpr = Eduardo_ready_evexpr & Adauto_ready_evexpr
        self._manipulador_teleporte = pydynaa.ExpressionHandler(self._lide_com_teleporte)
        self._wait(self._manipulador_teleporte, expression=both_ready_evexpr)

    def _lide_com_teleporte(self, event_expression):
        # Callback function that handles messages from both Adauto and Eduardo
        qubit = event_expression.first_term.atomic_source.qubits_emaranhados[1]
        Adauto = event_expression.second_term.atomic_source
        self._apply_correcoes(qubit, Adauto.correcoes)

    def _apply_correcoes(self, qubit, correcoes):
        # Apply teleportation correcoes and check fidelity
        m0, m1 = correcoes
        if m1:
            ns.qubits.operate(qubit, ns.X)
        if m0:
            ns.qubits.operate(qubit, ns.Z)
        fidelity = ns.qubits.fidelity(qubit, Adauto.estado_inicial, squared=True)
        print(f"{ns.sim_time():.1f}: Junior received entangled qubit and correcoes!"
              f" Fidelity = {fidelity:.3f}")

def setup_network(Adauto, Junior, Eduardo):
    Adauto.wait_for_Eduardo(Eduardo)
    Junior.wait_for_teleport(Adauto, Eduardo)
    Eduardo.start()

Adauto = Adauto(estado_inicial=ns.h1)
Junior = Junior()
Eduardo = Eduardo()

setup_network(Adauto, Junior, Eduardo)
stats = ns.sim_run(end_time=100)
print(stats)
