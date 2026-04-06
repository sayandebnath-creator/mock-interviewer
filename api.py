from fastapi import FastAPI
from pydantic import BaseModel
from llm.interviewer import Interviewer
from core.question_manager import QuestionManager
from cors.middleware import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

interviewer = Interviewer()
qm = QuestionManager()

# store current question globally (simple version)
current_question = qm.get_question("medium")


class UserInput(BaseModel):
    text: str

@app.get("/")
def read_root():
    return {"message": "Welcome to the Mock Interviewer API."}

@app.get("/start")
def start_interview():
    prompt = f"""
Ask this question:

{current_question['question']}

Do NOT give solution.
"""
    reply = interviewer.ask(prompt)
    return {"reply": reply}


@app.post("/respond")
def respond(user_input: UserInput):
    context_prompt = f"""
Question: {current_question['question']}
Expected: {current_question['expected_approach']}

Candidate: {user_input.text}

Act like interviewer:
- If correct → go deeper
- If wrong → hint only
"""

    reply = interviewer.ask(context_prompt)
    return {"reply": reply}


@app.get("/evaluate")
def evaluate():
    prompt = f"""
Question: {current_question['question']}
Expected: {current_question['expected_approach']}

Evaluate candidate:
- Correctness (0–10)
- Approach (0–10)
- Communication (0–10)
- Verdict
"""
    reply = interviewer.ask(prompt)
    return {"reply": reply}