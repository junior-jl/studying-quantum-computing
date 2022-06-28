import netsquid as ns
import pydynaa

class Charlie(pydynaa.Entity):
    ready_evtype = pydynaa.EventType("QUBITS_READY", "Entangled qubits are ready.")
    _generate_evtype = pydynaa.EventType("GENERATE", "Generate entangled qubits.")
    period = 50.
    delay = 10.

    def __init__(self):
        # Initialise Charlie by entangling qubits after every generation event
        self.entangled_qubits = None
        self._generate_handler = pydynaa.EventHandler(self._entangle_qubits)
        self._wait(self._generate_handler, entity=self,
                   event_type=Charlie._generate_evtype)

    def _entangle_qubits(self, event):
        # Callback function that entangles qubits and schedules an
        # entanglement ready event
        q1, q2 = ns.qubits.create_qubits(2)
        ns.qubits.operate(q1, ns.H)
        ns.qubits.operate([q1, q2], ns.CNOT)
        self.entangled_qubits = [q1, q2]
        self._schedule_after(Charlie.delay, Charlie.ready_evtype)
        print(f"{ns.sim_time():.1f}: Charlie finished generating entanglement")
        self._schedule_after(Charlie.period, Charlie._generate_evtype)

    def start(self):
        # Begin generating entanglement
        print(f"{ns.sim_time():.1f}: Charlie start generating entanglement")
        self._schedule_now(Charlie._generate_evtype)


class Alice(pydynaa.Entity):
    ready_evtype = pydynaa.EventType("CORRECTION_READY", "Corrections are ready.")
    _teleport_evtype = pydynaa.EventType("TELEPORT", "Teleport the qubit.")
    delay = 20.

    def __init__(self, teleport_state):
        # Initialise Alice by setting the teleport state and waiting to teleport
        self.teleport_state = teleport_state
        self.q0 = None
        self.q1 = None
        self.corrections = None
        self._teleport_handler = pydynaa.EventHandler(self._handle_teleport)
        self._wait(self._teleport_handler, entity=self,
                   event_type=Alice._teleport_evtype)

    def wait_for_charlie(self, charlie):
        # Setup Alice to wait for an entanglement qubit from Charlie
        self._qubit_handler = pydynaa.EventHandler(self._handle_qubit)
        self._wait(self._qubit_handler, entity=charlie,
                   event_type=Charlie.ready_evtype)

    def _handle_qubit(self, event):
        # Callback function that handles arrival of entangled qubit
        # and schedules teleportation
        self.q0, = ns.qubits.create_qubits(1, no_state=True)
        self.q1 = event.source.entangled_qubits[0]
        ns.qubits.assign_qstate([self.q0], self.teleport_state)
        self._schedule_after(Alice.delay, Alice._teleport_evtype)
        print(f"{ns.sim_time():.1f}: Alice received entangled qubit")

    def _handle_teleport(self, event):
        # Callback function that does teleportation and schedules
        # a corrections ready event
        ns.qubits.operate([self.q0, self.q1], ns.CNOT)
        ns.qubits.operate(self.q0, ns.H)
        m0, __ = ns.qubits.measure(self.q0)
        m1, __ = ns.qubits.measure(self.q1)
        self.corrections = [m0, m1]
        self._schedule_now(Alice.ready_evtype)
        print(f"{ns.sim_time():.1f}: Alice measured qubits & sending corrections")

class Bob(pydynaa.Entity):

    def wait_for_teleport(self, alice, charlie):
        # Setup Bob to wait for his entangled qubit and Alice's corrections
        charlie_ready_evexpr = pydynaa.EventExpression(
            source=charlie, event_type=Charlie.ready_evtype)
        alice_ready_evexpr = pydynaa.EventExpression(
            source=alice, event_type=Alice.ready_evtype)
        both_ready_evexpr = charlie_ready_evexpr & alice_ready_evexpr
        self._teleport_handler = pydynaa.ExpressionHandler(self._handle_teleport)
        self._wait(self._teleport_handler, expression=both_ready_evexpr)

    def _handle_teleport(self, event_expression):
        # Callback function that handles messages from both Alice and Charlie
        qubit = event_expression.first_term.atomic_source.entangled_qubits[1]
        alice = event_expression.second_term.atomic_source
        self._apply_corrections(qubit, alice.corrections)

    def _apply_corrections(self, qubit, corrections):
        # Apply teleportation corrections and check fidelity
        m0, m1 = corrections
        if m1:
            ns.qubits.operate(qubit, ns.X)
        if m0:
            ns.qubits.operate(qubit, ns.Z)
        fidelity = ns.qubits.fidelity(qubit, alice.teleport_state, squared=True)
        print(f"{ns.sim_time():.1f}: Bob received entangled qubit and corrections!"
              f" Fidelity = {fidelity:.3f}")

def setup_network(alice, bob, charlie):
    alice.wait_for_charlie(charlie)
    bob.wait_for_teleport(alice, charlie)
    charlie.start()

alice = Alice(teleport_state=ns.h1)
bob = Bob()
charlie = Charlie()

setup_network(alice, bob, charlie)
stats = ns.sim_run(end_time=100)
print(stats)
