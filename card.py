import random
class Card:

    def __init__(self):
        self.card = random.randint(1,13)
        self.score = 300

    def reset_score(self):
        self.card = 300