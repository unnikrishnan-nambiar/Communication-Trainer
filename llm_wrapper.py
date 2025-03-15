import ollama

class LLMWrapper:
    def __init__(self, model_name="mistral"):
        """Initialize LLM with Ollama for local inference."""
        self.model_name = model_name

    def generate_response(self, prompt):
        """Generate AI response based on user input."""
        try:
            response = ollama.chat(
                model=self.model_name, 
                messages=[{"role": "user", "content": prompt}]
            )
            return response["message"]["content"]
        except Exception as e:
            return f"Error generating response: {str(e)}"

# ✅ Only support DeepSeek-R1 and Mistral
available_models = {
    "mistral": LLMWrapper("mistral"),
    "deepseek": LLMWrapper("deepseek-r1")
}

def get_llm(model_name="mistral"):
    """Return the selected LLM instance, default to Mistral."""
    return available_models.get(model_name, available_models["mistral"])
