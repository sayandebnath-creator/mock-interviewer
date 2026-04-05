from llm.interviewer import Interviewer
from voice.stt import speech_to_text
from voice.tts import speak
from core.evaluator import evaluate
from core.question_manager import QuestionManager

def run_interview():
    interviewer = Interviewer()
    qm = QuestionManager()

    print("AI Interviewer Started\n")

    # STEP 1: Get question
    question_data = qm.get_question("medium")

    # STEP 2: Ask question (CONTROLLED)
    start_prompt = f"""
Ask this question to the candidate:

{question_data['question']}

Rules:
- Do NOT give solution
- Act like real interviewer
"""

    reply = interviewer.ask(start_prompt)
    print("Interviewer:", reply)
    speak(reply)

    # STEP 3: Loop
    while True:
        user_input = speech_to_text()
        print("You:", user_input)

        if user_input.lower() in ["exit", "quit"]:
            break

        if user_input.lower() == "done":
            result = evaluate(interviewer, question_data)
            print("\nEvaluation:\n", result)
            speak(result)
            break

        # STEP 4: CONTROLLED RESPONSE (IMPORTANT)
        context_prompt = f"""
Question: {question_data['question']}
Expected Approach: {question_data['expected_approach']}

Candidate answer: {user_input}

Act as interviewer:
- If correct → ask deeper questions
- If wrong → give hint ONLY
- DO NOT give full solution
"""

        reply = interviewer.ask(context_prompt)
        print("Interviewer:", reply)
        speak(reply)