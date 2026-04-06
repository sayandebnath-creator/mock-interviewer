import re

def clean_text_for_tts(text):
    text = re.sub(r"\*\*(.*?)\*\*", r"\1", text)  # remove **
    text = re.sub(r"\*", "", text)               # remove leftover *
    return text