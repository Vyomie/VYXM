# Vyxm Protocol

**Modular multi-agent protocol system with planner, distributor, and executor support.**

```python
from vyxm.protocol import Protocall

engine = Protocall()
engine.register_model("code_bot", "gpt2", "transformers", tag="Code")

response = engine.run("Write a Python class for a linked list")
print(response.output_text)
```