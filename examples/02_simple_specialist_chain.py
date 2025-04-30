from vyxm.protocol.registry import Registry
from vyxm.protocol.agent_specialists import RestaurantFinder, EmailSender

registry = Registry()
registry.RegisterSpecialist("RestaurantFinder", RestaurantFinder(), Tag="Utility")
registry.RegisterSpecialist("EmailSender", EmailSender(), Tag="Utility")

restaurant = RestaurantFinder().Run({
    "Task": "Find sushi in NYC",
    "ToolRegistry": registry.Tools
})

print(restaurant)