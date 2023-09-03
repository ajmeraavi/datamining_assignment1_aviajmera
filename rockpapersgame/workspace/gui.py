import tkinter as tk
from tkinter import messagebox

class GUI:
    def __init__(self, root, game):
        self.root = root
        self.game = game
        self.choice_buttons = []
        self.score_label = None

    def create_widgets(self):
        self.root.title("Rock, Paper, Scissors")

        # Score label
        self.score_label = tk.Label(self.root, text="Player: 0  Computer: 0")
        self.score_label.pack()

        # Choice buttons
        choices = ["rock", "paper", "scissors"]
        for choice in choices:
            button = tk.Button(
                self.root,
                text=choice,
                command=lambda choice=choice: self.play_round(choice),
            )
            button.pack()
            self.choice_buttons.append(button)

        # Reset button
        reset_button = tk.Button(
            self.root, text="Reset", command=self.reset_game
        )
        reset_button.pack()

    def play_round(self, player_choice):
        result = self.game.play_round(player_choice)
        self.update_score()
        self.show_result(result)

    def update_score(self):
        player_score = self.game.player_score
        computer_score = self.game.computer_score
        self.score_label.config(text=f"Player: {player_score}  Computer: {computer_score}")

    def show_result(self, result):
        if result == "win":
            messagebox.showinfo("Result", "You win!")
        elif result == "lose":
            messagebox.showinfo("Result", "You lose!")
        else:
            messagebox.showinfo("Result", "It's a tie!")

    def reset_game(self):
        self.game.reset_game()
        self.update_score()
