from vyxm.protocol.registry import Registry
from vyxm.protocol.specialists import DiffusersImageGenExecutor

registry = Registry()
registry.RegisterSpecialist("ImageGen", DiffusersImageGenExecutor(), Tag="ImageGen")

specialist = registry.GetSpecialistByName("ImageGen")
print(specialist["Executor"].run("A futuristic cityscape at sunset"))