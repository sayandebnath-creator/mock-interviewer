# AI Mock Interviewer (Google-Style DSA)

An AI-powered technical interviewer that simulates real-world coding interviews (Google/MNC level) using open-source LLMs, speech recognition, and voice feedback.
![Demo GIF of Mock Interviewer](videos/demo1.gif)

---

## 🚀 Overview

This project is a **voice-enabled AI interviewer** designed to help you practice Data Structures & Algorithms (DSA) interviews.

Unlike basic chatbots, this system:

* Asks **structured, curated interview questions**
* Interacts like a **real interviewer**
* Provides **guided hints (not direct answers)**
* Evaluates your performance at the end

---

## 🧠 Features

### ✅ Core Interview Engine

* Google-style DSA questions
* Controlled interviewer behavior (no random answers)
* Context-aware follow-up questions

### 🎙️ Voice Interaction

* Speak your answers
* AI responds with voice

### 📊 Evaluation System

* Scores you on:

  * Correctness
  * Approach
  * Communication
* Gives final verdict (Hire / No Hire)

### 📚 Question Bank

* Predefined structured problems
* Tagged by difficulty & topic
* Expected approach included for evaluation

---

## 🏗️ Project Structure

```
ai-interviewer/
│
├── main.py                  # Entry point
│
├── config/
│   └── settings.py         # Configurations (model names, paths)
│
├── llm/
│   └── interviewer.py      # LLM logic + prompt control
│
├── core/
│   ├── interview_loop.py   # Main interview flow
│   ├── evaluator.py        # Candidate evaluation
│   └── question_manager.py # Question selection logic
│
├── data/
│   ├── questions.json      # Question bank
│   └── loader.py           # Loads questions
│
├── voice/
│   ├── stt.py              # Speech-to-text (Whisper)
│   └── tts.py              # Text-to-speech (pyttsx3)
│
├── utils/
│   └── audio.py            # Audio recording helper
```

---

## ⚙️ Tech Stack

* **LLM Runtime:** Ollama
* **Model:** Mixtral 8x7B / LLaMA 3
* **Speech-to-Text:** Whisper
* **Text-to-Speech:** pyttsx3
* **Language:** Python

---

## 🔧 Installation

### 1. Clone the repo

```bash
git clone https://github.com/sayandebnath-creator/mock-interviewer.git
cd mock-interviewer
```

---

### 2. Create virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Install dependencies

```bash
pip install ollama faster-whisper sounddevice scipy pyttsx3
```

---

### 4. Install Ollama

Download from: https://ollama.com

Pull model:

```bash
ollama pull mixtral
```

(Use `llama3` if system is low-end)

---

## ▶️ Run the Project

```bash
python main.py
```

---

## 🎯 How It Works

```
🎤 You speak
   ↓
📝 Whisper converts speech → text
   ↓
🧠 LLM acts as interviewer
   ↓
🔊 pyttsx3 converts response → voice
```

---

## 🧪 Example Flow

1. AI: "Find two numbers that sum to target."
2. You: (speak your approach)
3. AI: Gives hints / asks follow-ups
4. You: Say `"done"`
5. AI: Gives evaluation + verdict

---

## 📈 Evaluation Criteria

* Correctness
* Problem-solving approach
* Time & space complexity
* Communication clarity

---

## ⚠️ Known Limitations

* Voice output is slightly robotic (pyttsx3)
* No real-time interruption support
* Limited question dataset (can be expanded)

---

## 🔮 Future Improvements

* Adaptive difficulty system
* Topic-based weak area tracking
* Web UI (React + mic button)
* Real-time coding interface
* System Design + Behavioral rounds

---

## 💡 Why This Project Matters

Most “AI interview” tools are just chatbots.

This system:

* Uses **structured questions**
* Enforces **interviewer behavior**
* Provides **real evaluation**

👉 Closer to real MNC interview simulation

---

## 📌 Author

Built for serious interview preparation and system design practice.

---

## ⭐ Next Step

Implement:

* Adaptive interviewer (difficulty scaling)
* Personalized feedback system

---
