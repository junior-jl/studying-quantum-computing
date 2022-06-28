from netsquid.nodes import Node
node_ping = Node(name="Ping")
node_pong = Node(name="Pong")

from netsquid.components.models import DelayModel

class PingPongDelayModel(DelayModel):
    def __init__(self, speed_of_light_fraction=0.5, standart_deviation=0.05):
        super().__init__()

        self.properties["speed"] = speed_of_light_fraction * 3e5
        self.properties["std"] = standart_deviation
        self.required_properties = ['lenght']

    def generate_delay(self, **kwargs):
        avg_speed = self.properties["speed"]
        std = self.properties["std"]
        speed = self.properties["rng"].normal(avg_speed, avg_speed * std)
        delay = 1e9 * kwargs['lenght'] / speed
        return delay

