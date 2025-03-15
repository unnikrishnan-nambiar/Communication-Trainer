import pyttsx3

class TextToSpeech:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty("rate", 150)  # Adjust speaking speed
        self.engine.setProperty("volume", 1.0)  # Adjust volume (0.0 to 1.0)

    def synthesize(self, text, output_file="output.wav"):
        """Generate speech from text and save it as an audio file."""
        self.engine.save_to_file(text, output_file)
        self.engine.runAndWait()

    def speak(self, text):
        """Speak the text in real-time."""
        self.engine.say(text)
        self.engine.runAndWait()

tts = TextToSpeech()
