import pyttsx3
import speech_recognition as sr

class SpeechAssistant:
    def __init__(self):
        # Initialize text-to-speech engine
        self.engine = pyttsx3.init()
        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', self.voices[0].id)

    def speak(self, text):
        """
        Converts the provided text to speech.
        """
        self.engine.say(text)
        self.engine.runAndWait()

    def listen(self):
        """
        Listens for speech and converts it to text.
        Returns the recognized text or an error message.
        """
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.pause_threshold = 1
            audio = recognizer.listen(source)

        try:
            print("Recognizing...")
            query = recognizer.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
        except Exception as e:
            print("Sorry, I didn't catch that. Could you please repeat?")
            return "None"
        return query

# Example usage:
if __name__ == "__main__":
    assistant = SpeechAssistant()
    
    # Example: Assistant says a greeting
    assistant.speak("Hello, how can I assist you today?")
    
    # Example: Assistant listens for a command
    command = assistant.listen()
    if command != "None":
        assistant.speak(f"You said: {command}")
