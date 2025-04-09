class Planner:
    def __init__(self, registry):
        self.registry = registry

    def call(self, input_text):
        if not self.registry.planner_model:
            return input_text, {}

        planner_exec = self.registry.planner_model["executor"]
        return planner_exec(input_text)
