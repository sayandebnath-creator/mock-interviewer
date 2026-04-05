def evaluate(interviewer, question_data):
    prompt = f"""
Question: {question_data['question']}
Expected Approach: {question_data['expected_approach']}

Evaluate candidate:

- Correctness (0–10)
- Approach (0–10)
- Communication (0–10)
- Verdict (Hire / No Hire)
"""

    return interviewer.ask(prompt)