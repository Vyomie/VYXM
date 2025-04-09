from .planner import Planner
from .distributor import Distributor

class ProtocolEngine:
    def __init__(self, registry):
        self.registry = registry
        self.planner = Planner(registry)
        self.distributor = Distributor(registry)

    def run(self, input_text):
        print("Input received:", input_text)

        plan_result, context = self.planner.call(input_text)
        print("Planner output:", plan_result)

        specialist = self.distributor.route(plan_result)
        if not specialist:
            return {"output": "No suitable specialist found.", "specialist": None}

        response, response_type, meta = specialist["executor"](plan_result)
        return {
            "output": response,
            "response_type": response_type,
            "meta": meta,
            "specialist": specialist["name"]
        }
