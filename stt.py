import whisper

class SpeechToText:
    def __init__(self):
        self.model = whisper.load_model("base")  # Lightweight model for efficiency

    def transcribe(self, audio_path):
        """Convert speech to text."""
        result = self.model.transcribe(audio_path)
        return result["text"]

stt = SpeechToText()
