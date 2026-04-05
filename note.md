# VOICE ARCHITECTURE
Mic → STT → LLM (your interviewer) → TTS → Speaker

# Voice architecture now
Voice → Whisper → LLM → pyttsx3 → Speaker


# PRESENT FLOW
main.py
  ↓
interview_loop.py  ← EVERYTHING CONNECTS HERE
  ↓
QuestionManager → gets question
  ↓
Interviewer (LLM)
  ↓
STT (your voice → text)
  ↓
TTS (AI → voice)
  ↓
Evaluator (final scoring)

# What each library does :-
Ollama
→ connects your Python code to local LLM (Mixtral / LLaMA)

faster-whisper
→ speech → text

sounddevice
→ captures mic input

SciPy
→ saves audio file (.wav)

pyttsx3
→ text → voice