from llm_wrapper import llm  # Ensure LLM is imported
from stt import stt  # Import speech-to-text

class PresentationAssessment:
    def analyze_text(self, text):
        prompt = f"Analyze this speech for clarity, pacing, and persuasiveness:\n{text}"
        return llm.generate_response(prompt)  # Use LLM

    def analyze_audio(self, audio_path):
        text = stt.transcribe(audio_path)  # Convert speech to text
        return self.analyze_text(text)  # Analyze converted text

assessment = PresentationAssessment()
