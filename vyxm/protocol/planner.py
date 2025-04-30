class Planner:
    def __init__(self, registry):
        self.registry = registry

    def Call(self, input_text):
        if not self.registry.PlannerModel:
            return input_text, {}

        planner_exec = self.registry.PlannerModel["executor"]
        return planner_exec(input_text)
