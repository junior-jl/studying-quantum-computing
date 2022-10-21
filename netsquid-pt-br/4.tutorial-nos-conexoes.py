# Tutorial Netsquid - Nós e Conexões

# A seção anterior introduziu várias classes base de componentes para melhorar a modelagem
# de uma rede quântica. Nesta seção, comporemos esses componentes juntos em NÓS e CONEXÕES,
# dois exemplos de componentes compostos.
# Ao fim desta seção, teremos uma função que criará a rede automaticamente, a qual será usada
# na próxima seção para completar o esquema do teleporte usando protocolos.

def separador(tamanho = 50):
        """Separador básico de texto para melhor visualização."""
        print('*', end='')
        for i in range(tamanho):
            print('-', end='')
        print('*')

## Nós

# Nós (Node) representam as entidades de localização de uma rede quântica, onde todas as
# operações são locais. O Node (uma subclasse de Component) é um exemplo de componente
# composto que guarda e gerencia subcomponentes por meio de seu atributo subcomponents.

# Até aqui, Alice e Bob são duas entidades genéricas de simulação (Entity). Nesta seção,
# usaremos componentes Nós, descrevendo-os puramente em termos de seu hardware de rede.
# Em uma seção posterior, iremos demonstrar como descrever o comportamento lógico restante
# utilizando entidades de protocolo virtuais.
separador()
from netsquid.nodes import Node
alice = Node("Alice")

# Pode-se pensar em um nó como uma localização para quaisquer componentes locais. Por exemplo,
# se queremos que Alice possua uma memória quântica, podemos adicionar ao seu nó:

from netsquid.components import QuantumMemory
memoriaq = QuantumMemory("MemoriaAlice", num_positions=2)
alice.add_subcomponent(memoriaq, name="memoria1")
print("Subcomponente de alice 'memoria1':")
print(alice.subcomponents["memoria1"])
separador()
# De maneira geral, qualquer componente pode ser adicionado como subcomponente de outro dessa
# forma, desde que uma hierarquia seja mantida de forma consistente. Podemos obter informações
# sobre os subcomponentes e supercomponentes de um componente como segue:

print("Subcomponentes de alice:")
print(alice.subcomponents)
separador()
print("Supercomponente de memoriaq:")
print(memoriaq.supercomponent)
separador()
print("alice não possui supercomponente?")
print(alice.supercomponent is None)
separador()

# Há um tratamento especial para a memória quântica principal (ou processador quântico) em nós:
# este pode ser especificado na inicialização, e pode ser acessado usando o atributo qmemory.
memoriaq_bob = QuantumMemory("MemoriaBob", num_positions=2)
bob = Node("Bob", qmemory=memoriaq_bob)
print(f"bob.qmemory -> {bob.qmemory}")
print(f"memoriaq_bob -> {memoriaq_bob}")
print(f"bob.subcomponents -> {bob.subcomponents}")
separador()

# Assim como qualquer componente, nós podem ter portas (Port). Não é possível conectar portas
# entre componentes com diferentes supercomponentes, por conta disso as portas de um nó servem
# como uma interface externa para todos os seus subcomponentes. Isso ajuda a impor localidade,
# algo que veremos novamente quando discutirmos protocolos. Um subcomponente de um nó pode
# se comunicar pelas portas de um nó encaminhando (forwarding) sua saída ou recebendo uma
# entrada encaminhada. 
# Checar imagem: https://docs.netsquid.org/latest-release/_images/ports_forwarding.png
alice.add_ports(['qin_charlie'])
alice.ports['qin_charlie'].forward_input(alice.qmemory.ports['qin'])

# Dessa forma, quaisquer mensagens transmitidas como entrada à porta qin_charlie de Alice será
# diretamente encaminhada como entrada para a porta qin da sua memória.
