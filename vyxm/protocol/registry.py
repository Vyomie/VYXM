from vyxm.protocol.specialists import (
    TransformersLLMExecutor,
    OllamaExecutor,
    LlamaCppExecutor,
    DiffusersImageGenExecutor,
)
# registry.py

from .tools import ToolRegistryInstance

class Registry:
    def __init__(self, AllowedTags=None):
        self.Specialists = []
        self.PlannerModel = None
        self.AllowedTags = AllowedTags or ["Code", "ImageGen", "LLM"]
        self.Tools = ToolRegistryInstance
        self._RegisterPrebuilts()

    def _RegisterPrebuilts(self):
        from .specialists import (
            TransformersLLMExecutor,
            OllamaExecutor,
            LlamaCppExecutor,
            DiffusersImageGenExecutor,
        )

        self.RegisterSpecialist("Transformers", TransformersLLMExecutor(), Tag="LLM")
        self.RegisterSpecialist("Ollama", OllamaExecutor(), Tag="LLM")
        self.RegisterSpecialist("LlamaCpp", LlamaCppExecutor(), Tag="LLM")
        self.RegisterSpecialist("Diffusers", DiffusersImageGenExecutor(), Tag="ImageGen")

    def RegisterSpecialist(self, Name, Executor, Tag="LLM"):
        if Tag not in self.AllowedTags:
            self.AllowedTags.append(Tag)
        self.Specialists.append({"Name": Name, "Executor": Executor, "Tag": Tag})

    def RegisterPlanner(self, Name, Executor):
        self.PlannerModel = {"Name": Name, "Executor": Executor}

    def GetSpecialist(self, Tag):
        return next((S for S in self.Specialists if S["Tag"].lower() == Tag.lower()), None)

    def GetSpecialistByName(self, Name):
        return next((S for S in self.Specialists if S["Name"] == Name), None)

    def GetAllTags(self):
        return self.AllowedTags

    def DecoratorSpecialist(self, Name, Tag="LLM"):
        def Wrapper(Cls):
            self.RegisterSpecialist(Name, Cls(), Tag)
            return Cls
        return Wrapper

    def DecoratorPlanner(self, Name):
        def Wrapper(Cls):
            self.RegisterPlanner(Name, Cls())
            return Cls
        return Wrapper
