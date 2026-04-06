import json

def load_questions():
    with open("data/questions.json", "r") as f: # Load questions from JSON file
        return json.load(f)