# core.py

from .planner import Planner
from .distributor import Distributor
from .tools import CallTool

class ProtocolEngine:
    def __init__(self, Registry):
        self.Registry = Registry
        self.Planner = Planner(Registry)
        self.Distributor = Distributor(Registry)

    def Run(self, InputText):
        print("Input received:", InputText)

        PlanResult, Context = self.Planner.Call(InputText)
        print("Planner output:", PlanResult)

        TaskData = {
            "Task": PlanResult,
            "Context": Context,
            "ToolRegistry": self.Registry.Tools,
            "SpecialistRegistry": self.Registry,
        }

        ChainOutput = []
        CurrentSpecialist = self.Distributor.Route(PlanResult)

        while CurrentSpecialist:
            print(f"Calling specialist: {CurrentSpecialist['Name']}")
            Response, ResponseType, Meta = CurrentSpecialist["Executor"].Run(TaskData)
            ChainOutput.append(Response)

            for Call in Meta.get("ToolCalls", []):
                ToolOutput = CallTool(Call["Tool"], Call["Args"], self.Registry.Tools)
                ChainOutput.append(f"[Tool: {Call['Tool']}] {ToolOutput}")

            NextName = Meta.get("NextSpecialist")
            if NextName:
                CurrentSpecialist = self.Registry.GetSpecialistByName(NextName)
                TaskData["Task"] = Meta.get("NextTask", TaskData["Task"])
            else:
                CurrentSpecialist = None

        return {
            "Output": "\n".join(ChainOutput),
            "ResponseType": "MultiStep",
            "Meta": {},
            "Specialist": "MultiAgent",
        }
