Based on the requirements, here are the core classes, functions, and methods that will be necessary for the Rock, Paper, Scissors game:

1. Game:
   - `start_game()`: Starts the game and initializes the GUI.
   - `play_round(player_choice)`: Handles the logic for playing a round of Rock, Paper, Scissors.
   - `reset_game()`: Resets the game state.

2. Player:
   - `make_choice(choice)`: Sets the player's choice (rock, paper, or scissors).

3. ComputerPlayer (inherits from Player):
   - `make_choice()`: Generates a random choice for the computer player.

4. GUI:
   - `create_widgets()`: Creates the GUI widgets.
   - `update_score()`: Updates the score display.
   - `show_result(result)`: Displays the result of a round.
   - `disable_buttons()`: Disables the choice buttons.
   - `enable_buttons()`: Enables the choice buttons.
   - `reset_game()`: Resets the game state.

Now let's proceed with the file structure and code implementation.

1. main.py

