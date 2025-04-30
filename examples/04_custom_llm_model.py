from vyxm.protocol.registry import Registry
from vyxm.protocol.specialists import TransformersLLMExecutor

registry = Registry()
registry.RegisterSpecialist("GPT2Writer", TransformersLLMExecutor("gpt2"), Tag="LLM")

spec = registry.GetSpecialistByName("GPT2Writer")
print(spec["Executor"].run("Once upon a time in a galaxy far, far away..."))