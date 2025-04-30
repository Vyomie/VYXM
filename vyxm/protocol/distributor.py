from transformers import pipeline

class Distributor:
    def __init__(self, registry):
        self.registry = registry
        self.classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

    def Route(self, input_text):
        candidate_labels = self.registry.GetAllTags()
        result = self.classifier(input_text, candidate_labels)
        best_label = result["labels"][0]
        return self.registry.GetSpecialist(best_label)
