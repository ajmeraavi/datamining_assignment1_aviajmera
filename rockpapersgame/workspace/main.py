import tkinter as tk
from game import Game
from gui import GUI
from player import Player

def main():
    root = tk.Tk()
    game = Game()
    gui = GUI(root, game)
    gui.create_widgets()
    root.mainloop()

if __name__ == "__main__":
    main()
