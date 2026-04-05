import ollama
from config.settings import MODEL_NAME

SYSTEM_PROMPT = """
You are a Google DSA interviewer.

- Speak directly to the user
- No third-person ("candidate")
- Be concise and natural
- Ask questions step-by-step
- Give hints only if needed
"""

class Interviewer:
    def __init__(self):
        self.messages = [
            {"role": "system", "content": SYSTEM_PROMPT}
        ]

    def ask(self, user_input):
        self.messages.append({"role": "user", "content": user_input})

        response = ollama.chat(
            model=MODEL_NAME,
            messages=self.messages
        )

        reply = response["message"]["content"]
        self.messages.append({"role": "assistant", "content": reply})

        return reply