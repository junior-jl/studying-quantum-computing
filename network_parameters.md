# Nós

- Boolean: end_node
- Boolean: quantico
- Boolean: memoria
- id
- taxa_minima
- ruido_operacoes
- decoerencia
- geracao
- destilaçao
- lat (?)
- long (?)

```py
class No(object):
    def __init__(self, id = '', taxa_minima=0, ruido_operacoes=0, decoerencia=0, geracao=1, lat=0, long=0, end_node=False,
                 quantico=True, memoria=False):
        self.id = id

    def distanciaEntreNos(self, alvo):
        # import geopy.distance
        coords_1 = (self.lat, self.long)
        coords_2 = (alvo.lat, alvo.long)

        print(geopy.distance.geodesic(coords_1, coords_2).km)
```

# Canais

- Boolean: quantico
- id
- comprimento
- [unidade]
- delay (ms)
- ocupado
- registro_swap

## Netsquid

- Modelo de delay (Q e C)
- Modelo de ruído (Q e C)
- Modelo de perdas (Q e C)
```py
class Canal(object):
  def __init__(self, id, comprimento, quantico = True, unidade = 'km', ocupado = False, registro_swap = []):
    self.id = id
    self.comprimento = comprimento
    self.delay = 3e8/self.comprimento
```

  
