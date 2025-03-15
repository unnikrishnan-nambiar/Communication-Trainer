import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig

class MultiLLM:
    def __init__(self, model_name="mistralai/Mistral-7B"):
        """Load the selected LLM with quantization for efficiency."""
        self.model_name = model_name

        # ✅ Enable 4-bit Quantization
        quant_config = BitsAndBytesConfig(
            load_in_4bit=True,  # Use 4-bit precision
            bnb_4bit_compute_dtype=torch.float16,  # Use float16 for computation
            bnb_4bit_quant_type="nf4",  # Normalized 4-bit quantization
            llm_int8_skip_modules=["lm_head"]  # Speed up inference
        )

        # ✅ Load Tokenizer & Model with Quantization
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(
            model_name, 
            quantization_config=quant_config,
            device_map="auto"  # Automatically use GPU if available
        )

    def generate_response(self, prompt):
        """Generate AI response based on user input."""
        inputs = self.tokenizer(prompt, return_tensors="pt").to(self.model.device)
        output = self.model.generate(**inputs, max_length=200)
        return self.tokenizer.decode(output[0], skip_special_tokens=True)

# ✅ Support for multiple LLMs
available_models = {
    "mistral": MultiLLM("mistralai/Mistral-7B"),
    "llama2": MultiLLM("meta-llama/Llama-2-7b"),
    "falcon": MultiLLM("tiiuae/falcon-7b"),
}

def get_llm(model_name):
    """Return the LLM instance based on model selection."""
    return available_models.get(model_name, available_models["mistral"])
