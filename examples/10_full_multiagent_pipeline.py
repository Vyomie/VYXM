from vyxm.protocol.registry import Registry
from vyxm.protocol.core import ProtocolEngine
from vyxm.protocol.agent_specialists import RestaurantFinder, EmailSender

registry = Registry()
registry.RegisterSpecialist("RestaurantFinder", RestaurantFinder(), Tag="Utility")
registry.RegisterSpecialist("EmailSender", EmailSender(), Tag="Utility")

engine = ProtocolEngine(registry)
result = engine.Run("Find sushi in NYC and email it to me")
print(result)