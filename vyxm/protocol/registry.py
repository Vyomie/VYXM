class Registry:
    def __init__(self, allowed_tags=None):
        self.specialists = []
        self.planner_model = None
        self.allowed_tags = allowed_tags or ["Code", "ImageGen", "LLM"]

    def register_specialist(self, name, executor, tag="LLM"):
        if tag not in self.allowed_tags:
            self.allowed_tags.append(tag)
        self.specialists.append({"name": name, "executor": executor, "tag": tag})

    def register_planner(self, name, executor):
        self.planner_model = {"name": name, "executor": executor}

    def get_specialist(self, tag):
        return next((s for s in self.specialists if s["tag"].lower() == tag.lower()), None)

    def get_specialist_by_name(self, name):
        return next((s for s in self.specialists if s["name"] == name), None)

    def get_all_tags(self):
        return self.allowed_tags
