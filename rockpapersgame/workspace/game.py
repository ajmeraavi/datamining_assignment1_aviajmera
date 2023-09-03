from player import Player
from computer_player import ComputerPlayer

class Game:
    def __init__(self):
        self.player = Player()
        self.computer = ComputerPlayer()
        self.player_score = 0
        self.computer_score = 0

    def start_game(self):
        self.player_score = 0
        self.computer_score = 0

    def play_round(self, player_choice):
        self.player.make_choice(player_choice)
        self.computer.make_choice()
        result = self.get_round_result()
        if result == "win":
            self.player_score += 1
        elif result == "lose":
            self.computer_score += 1
        return result

    def get_round_result(self):
        player_choice = self.player.choice
        computer_choice = self.computer.choice
        if player_choice == computer_choice:
            return "tie"
        elif (
            (player_choice == "rock" and computer_choice == "scissors")
            or (player_choice == "paper" and computer_choice == "rock")
            or (player_choice == "scissors" and computer_choice == "paper")
        ):
            return "win"
        else:
            return "lose"

    def reset_game(self):
        self.player.reset_choice()
        self.computer.reset_choice()
        self.player_score = 0
        self.computer_score = 0
