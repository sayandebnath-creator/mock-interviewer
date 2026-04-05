import json

def load_questions():
    with open("data/questions.json", "r") as f:
        return json.load(f)