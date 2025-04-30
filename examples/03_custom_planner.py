from vyxm.protocol.registry import Registry
from vyxm.protocol.core import ProtocolEngine

class SimplePlanner:
    def __call__(self, input_text):
        return "Find ramen", {}

registry = Registry()
registry.RegisterPlanner("SimplePlanner", SimplePlanner())

engine = ProtocolEngine(registry)
result = engine.Run("Find me good ramen in Tokyo")
print(result)