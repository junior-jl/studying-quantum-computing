# Nós

- Boolean: end_node
- Boolean: quantico
- Boolean: memoria
- id
- taxa_minima
- ruido_operacoes
- decoerencia
- geracao
- lat (?)
- long (?)

```py
class No(object):
  def __init__(self, id, taxa_minima = 0, ruido_operacoes = 0, decoerencia = 0, geracao = 1, lat = 0, long = 0, end_node = False, quantico = True, memoria = False):
    self.id = id
```

# Canais

- Boolean: quantico
- id
- comprimento
- [unidade]
- delay (ms)
- ocupado
- registro_swap

```py
class Canal(object):
  def __init__(self, id, comprimento, quantico = True, unidade = 'm', ocupado = False, registro_swap = []):
    self.id = id
    self.comprimento = comprimento
    self.delay = 3e8/self.comprimento
```
