import yaml
import random
from stt import stt  # Speech-to-Text
from tts import tts  # Text-to-Speech
from database import progress_db  # Import database
from llm_wrapper import get_llm  # ✅ Use llm_wrapper (Ollama)

class ChatTrainer:
    def __init__(self, config_path="config.yaml"):
        """Load predefined scenarios from YAML."""
        with open(config_path, "r") as file:
            self.config = yaml.safe_load(file)

    def get_random_scenario(self, category):
        """Retrieve a pre-generated scenario from YAML."""
        scenarios = self.config["training_modules"].get(category, [])
        return random.choice(scenarios) if scenarios else "Invalid category."

    def evaluate_response(self, user_audio, username, category, model_name="mistral"):
        """Evaluate the user's spoken response using LLM-based feedback and structured scoring."""
        user_text = stt.transcribe(user_audio)  # Convert speech to text
        scenario = self.get_random_scenario(category)

        if not user_text.strip():
            feedback = "I couldn't understand your response. Please try again with clearer speech."
            score = 0
        else:
            llm = get_llm(model_name)  # ✅ Use llm_wrapper (Ollama)
            prompt = f"""
            Evaluate the following response based on:
            - Clarity (0-10)
            - Engagement (0-10)
            - Structure (0-10)

            Response: "{user_text}"

            Provide structured feedback and a final score out of 100.
            """
            feedback = llm.generate_response(prompt)  # ✅ Use Ollama API

            # Extract structured scores (fallback if LLM fails)
            try:
                clarity_score = 10 if len(user_text.split()) > 15 else 5
                engagement_score = 10 if "story" in user_text.lower() else 5
                structure_score = 10 if "." in user_text else 5
                score = (clarity_score + engagement_score + structure_score) * 3  # Scale to 100
            except:
                score = 50  # Default fallback score

        # ✅ Save user progress
        progress_db.save_progress(username, category, scenario, user_text, feedback, score)

        return feedback, score

chat_trainer = ChatTrainer()
