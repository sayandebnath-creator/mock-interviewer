from faster_whisper import WhisperModel
from utils.audio import record_audio
from config.settings import AUDIO_FILE, WHISPER_MODEL

model = WhisperModel(WHISPER_MODEL)

def speech_to_text():
    record_audio(AUDIO_FILE)

    segments, _ = model.transcribe(AUDIO_FILE)
    text = " ".join([seg.text for seg in segments])

    return text.strip()