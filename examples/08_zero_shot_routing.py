from vyxm.protocol.registry import Registry
from vyxm.protocol.core import ProtocolEngine

registry = Registry()
engine = ProtocolEngine(registry)

# This will invoke the zero-shot classifier to route the task
result = engine.Run("Generate a picture of a cat in space")
print(result)