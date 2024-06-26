"""
Module imports
os: for interacting with the system
random: for generating random choices (rock, paper, scissors)
time: for introducing delays
"""
import os
import random
import time


class GameLogic:
    """
    Handles the game logic for Rock, Paper, Scissors game.
    """

    def __init__(self):
        """
        Initializes the GameLogic class with available choices.
        """
        self.our_choices = ["rock", "paper",
                            "scissors"]  # Define available choice for the game

    def valid_answer(self, answer):
        """
            checks if the player's answer is valid
            :param answer: (string) Player's answer
            :return:
                bool: True if the answer is valid, False otherwise
            """
        return answer in self.our_choices
        # Check if the player's answer
        # is in the available choices

    @staticmethod
    def winning_answer(answer1, answer2):
        """
            Checks if 'answer1' beats 'answer2'
            :param answer1: (str) Player 1's answer
            :param answer2: (str) Player 2's answer
            :return:
                bool: 'True' if 'answer1' beats 'answer2', False otherwise
            """
        return (answer1 == "rock" and answer2 == "scissors"
                or answer1 == "paper" and answer2 == "rock"
                or answer1 == "scissors" and answer2 == "paper")

    @staticmethod
    def equal_answer(answer1, answer2):
        """
        Checks if 'answer1' and 'answer2' are equal.
        :param answer1: (str) Player 1's answer
        :param answer2: (str) Player 2's answer
        :return:
            bool: 'True' if answers are equal, False otherwise
    """
        return answer1 == answer2


class GameInit:
    """
    Initializes the Rock, Paper, Scissors game and manages the game interface.
    """

    def __init__(self):
        """
        Initializes the GameInit class with color codes for the console.
        """
        self.green = "\033[0;32m"

    @staticmethod
    def clear_console():
        """
        Clears the console screen.
        :return:
        """
        os.system("cls" if os.name ==
                  "nt" else "clear")  # Clear the console screen

    def display_choice(self, choice):
        """
        Display ASCII art for the player's or computer's choice.
        :param choice: (str) The choice made by player or computer
        """
        if choice == "rock":
            print("    _______")
            print("---'   ____)")
            print("      (_____)")
            print("      (_____)")
            print("      (____)")
            print("---.__(___)")
        elif choice == "paper":
            print("    _______")
            print("---'   ____)____")
            print("          ______)")
            print("          _______)")
            print("         _______)")
            print("---.__________)")
        else:
            print("    _______")
            print("---'   ____)____")
            print("          ______)")
            print("       __________)")
            print("      (____)")
            print("---.__(___)")

    def start_game(self):
        """
        Starts the Rock, Paper, Scissors game.

        """

        running = True
        while running:  # Start the game loop
            print(self.green)  # Print output in green color
            print("### Rock Paper Scissors Game ###")
            # Ask the player for their name
            player_name = input("Enter your name: ")
            print(f"\nWelcome, {player_name}!\n")  # Greet the player by name
            logic = GameLogic()  # Create an instance of the GameLogic class

            print("Type your choice:")
            answer_player = input()
            # Validate player's input
            while not logic.valid_answer(answer_player):
                print("Not a valid option. Expecting:", logic.our_choices)
                answer_player = input()  # Prompt player to enter a valid answer

            self.clear_console()  # Clear the console screen

            print("You chose:", answer_player)
            # Display the player's choice in ASCII art
            self.display_choice(answer_player)
            time.sleep(0.5)
            print("Computer is thinking...")
            time.sleep(1)
            pc_answer = random.choice(logic.our_choices)
            # Computer randomly chooses
            # from the options
            print("Computer chose:", pc_answer)
            self.display_choice(pc_answer)
            time.sleep(1)

            if logic.equal_answer(answer_player, pc_answer):
                print("IT'S A TIE!!!")
            elif logic.winning_answer(answer_player, pc_answer):
                print(f"{answer_player} beats {pc_answer}")
                print(f"\n {player_name} YOU WIN!!! \n")
                print("        ___________")
                print("       '._==_==_=_.'")
                print("       .-\\: ECOLE /-.")
                print("      | (|:.  IT |) |")
                print("       '-|:.     |-'")
                print("         \\::.    /")
                print("          '::. .'")
                print("            ) (")
                print("          _.' '._")
                print("         `\"\"\"\"\"\"\"`")
            else:
                print(f"{pc_answer} beats {answer_player}")
                print(f"\n {player_name} YOU LOSE! \n")


if __name__ == "__main__":  # Check if the current script is the main script
    game_ui = GameInit()  # Create an instance of the GameInit class
    game_ui.clear_console()  # Clear the console screen
    game_ui.start_game()  # Start the game
