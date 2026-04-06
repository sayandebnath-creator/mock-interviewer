import random
from data.loader import load_questions

class QuestionManager:
    def __init__(self):
        self.questions = load_questions()

    def get_question(self, difficulty=None):
        if difficulty:
            filtered = [q for q in self.questions if q["difficulty"] == difficulty] # Filter questions by difficulty
        else:
            filtered = self.questions

        return random.choice(filtered)