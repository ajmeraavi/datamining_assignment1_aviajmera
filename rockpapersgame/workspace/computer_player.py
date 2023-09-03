import random
from player import Player

class ComputerPlayer(Player):
    def make_choice(self):
        choices = ["rock", "paper", "scissors"]
        self.choice = random.choice(choices)
