# VyxM Protocol

**Multi-agent orchestration system for executing tasks via specialists, tools, and planners.**

## Features
- Modular specialist registration
- Planner + distributor separation
- Tool registry with decorators
- Easy zero-shot routing
- Visualization of agent-tool graph

## Installation
```
pip install vyxm-protocol
```

## Usage Examples

### 1. Run a ProtocolEngine flow:
```python
from vyxm.protocol.registry import Registry
from vyxm.protocol.core import ProtocolEngine

registry = Registry()
engine = ProtocolEngine(registry)

result = engine.Run("Generate a cat image and email it to me")
print(result)
```

### 2. Register custom specialist:
```python
from vyxm.protocol.registry import Registry

class HelloSpecialist:
    def Run(self, InputData):
        return ("Hello!", "Text", {"ToolCalls": [], "NextSpecialist": None})

registry = Registry()
registry.RegisterSpecialist("Greeter", HelloSpecialist(), Tag="LLM")
```

### 3. Use tools directly:
```python
from vyxm.protocol.prebuilt_tools import GoogleMaps
print(GoogleMaps("coffee shops in SF"))
```

## Development Setup

Build and test the package:
```bash
pip install -e .[dev]
```

## License
MIT License