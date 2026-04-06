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

# DIFFERENCE BETWEEN PIPER AND PYTTSX3

| Aspect         | Before (Piper)           | Now (pyttsx3) |
| -------------- | ------------------------ | ------------- |
| Setup          | Heavy                    | Minimal       |
| Dependencies   | External binary + models | Pure Python   |
| OS issues      | Yes                      | No            |
| Audio playback | Manual (`afplay`)        | Automatic     |
| Stability      | Fragile                  | Stable        |
| Voice quality  | Good                     | Basic         |
| Dev speed      | Slow                     | Fast          |

# State driven Ui
idle → listening → speaking

# UI FLOW
Click "Start"
 → /start
 → AI speaks

User clicks mic
 → speaks
 → /respond
 → AI replies

User says "done"
 → /evaluate
 → final result

# Important engineering notes
⚠️ State issue (important)

Right now:
current_question = ...

This is global (bad for multi-users)

But fine for:
✔ your local project
✔ MVP

# What build for now:-
✔ API-driven system
✔ UI + backend separation
✔ Voice interaction
✔ Real interview loop