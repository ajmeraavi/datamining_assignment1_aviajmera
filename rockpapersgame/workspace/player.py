class Player:
    def __init__(self):
        self.choice = None

    def make_choice(self, choice):
        self.choice = choice

    def reset_choice(self):
        self.choice = None
