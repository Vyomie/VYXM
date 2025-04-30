from transformers import pipeline
import subprocess

# Transformers LLM Executor
class TransformersLLMExecutor:
    def __init__(self, model_name="gpt2"):
        self.generator = pipeline("text-generation", model=model_name)

    def Run(self, input_data):
        query = input_data["Task"] if isinstance(input_data, dict) else input_data
        result = self.generator(query, max_length=100, do_sample=True)
        return result[0]["generated_text"], "Text", {"ToolCalls": [], "NextSpecialist": None}


# Ollama Executor
class OllamaExecutor:
    def __init__(self, model_name="llama2"):
        self.model_name = model_name

    def Run(self, input_data):
        query = input_data["Task"] if isinstance(input_data, dict) else input_data
        result = subprocess.run(
            ["ollama", "run", self.model_name, query],
            capture_output=True,
            text=True
        )
        return result.stdout.strip(), "Text", {"ToolCalls": [], "NextSpecialist": None}


# Llama.cpp Executor
class LlamaCppExecutor:
    def __init__(self, model_path="models/llama.bin"):
        self.model_path = model_path

    def Run(self, input_data):
        query = input_data["Task"] if isinstance(input_data, dict) else input_data
        result = subprocess.run(
            ["llama", "-m", self.model_path, "-p", query],
            capture_output=True,
            text=True
        )
        return result.stdout.strip(), "Text", {"ToolCalls": [], "NextSpecialist": None}


# Diffusers Image Generation Executor
class DiffusersImageGenExecutor:
    def __init__(self, model_id="CompVis/stable-diffusion-v1-4"):
        from diffusers import StableDiffusionPipeline
        import torch

        self.pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
        self.pipe.to("cuda" if torch.cuda.is_available() else "cpu")

    def Run(self, input_data):
        prompt = input_data["Task"] if isinstance(input_data, dict) else input_data
        image = self.pipe(prompt).images[0]
        image.save("output.png")
        return "Image saved as output.png", "Image", {"ToolCalls": [], "NextSpecialist": None}
