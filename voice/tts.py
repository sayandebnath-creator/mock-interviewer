import pyttsx3

engine = pyttsx3.init()

# Optional: make it sound better
engine.setProperty('rate', 170)   # speed
engine.setProperty('volume', 1.0)

def speak(text):
    clean = clean_text_for_tts(text)
    engine.say(clean)
    engine.runAndWait()