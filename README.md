cat <<EOF > README.md
![VYXM Logo](logo.png)

**VYXM** is an extensible AI tool designed for intelligent orchestration of tasks such as natural language processing, code generation, and image synthesis. Built around modularity, it allows users to plug in and route between different AI capabilities using a clean, protocol-driven interface.

At its core, `vyxm` provides a high-level API to define, register, plan, and execute AI-powered tools — with the `vyxm.protocol` module serving as a lightweight internal protocol for defining tool behaviors.

---

## ✨ Features

- 🔌 **Tool Registry**: Register and organize multiple AI tools using simple decorators.
- 🧠 **Intent Planning**: Lightweight, extensible planning engine for routing inputs.
- 🔀 **Dynamic Distribution**: Route prompts to the appropriate tool with zero glue code.
- 🧩 **Composable Design**: Easily combine tools like LLMs, image models, custom logic, etc.
- 🧱 **Protocol Subset**: Direct access to low-level planning, distribution, and registry.

---

## 📦 Installation

```bash
pip install vyxm
```

---

## 🧠 Quick Example: Build a Multi-Modal AI Agent

We'll register a **code generation** and an **image generation** tool, then let vyxm automatically choose which one to run based on the input.

### 1. Register Tools

```python
from vyxm.protocol import registry, distributor

@registry.register("code_gen")
def code_gen(data):
    prompt = data["prompt"]
    return f"# Python Code\\ndef hello():\\n    print('Prompt was: {prompt}')"

@registry.register("image_gen")
def image_gen(data):
    description = data["description"]
    return f"[Image: '{description}']"
```

### 2. Call via Distributor

```python
print(distributor.run("Generate Python code that reverses a string"))
print(distributor.run("Create an image of a serene beach at sunset with floating lanterns"))
```

## 📂 Protocol Module Overview

`vyxm.protocol` provides the foundational components that power `vyxm`:

- **registry**: Tool registration system
- **planner**: Intent classification (can be extended with LLM-based planning)
- **distributor**: Dispatches prompts to tools based on plan

You can use `vyxm.protocol` directly for advanced workflows or contribute your own planning logic.

---

## 🛠️ Extending vyxm

You can extend `vyxm` by adding tools like:

- Language model wrappers (e.g., OpenAI, Claude, local LLMs)
- Text-to-image models (e.g., Stability, DALL·E)
- Custom domain-specific functions (e.g., search, summarization)

Just register your tool and let the system handle the routing.

---

## 📚 License

MIT © 2025 Vyomie

EOF
