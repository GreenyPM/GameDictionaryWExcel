from tabulate import tabulate
from loggerConfig import logger
from gameDict import GameDict
import pandas as pd

class Interface:
    def __init__(self):
        self.game_collection = {}
        self.collection_handler = GameDict(self.game_collection)
        self.default_filename = "output.xlsx"
        self.keep_going = True

    def display_menu(self):
        print("\n=== Welcome to the GAME COLLECTOR! ===")
        print("A fine application to track your games")
        print("Please choose one of the options below:")
        print("- add (game)\n- view (collection)\n- import\n- clear\n- export\n- exit")

    def get_user_choice(self):
        return input("Your choice: ").lower()

    def add_game(self):
        platform_entry = input("Enter Name of Platform: ")
        game_entry = input("Enter Name of Game: ")
        result = self.collection_handler.add_game_entry(platform_entry, game_entry)
        logger.info(result)
        print(f"\n{result}\n")

    def view_collection(self):
        self.collection_handler.display_collection()

    def import_collection(self):
        filename = input(f"Enter the filename to import (default: {self.default_filename}): ") or self.default_filename
        result = self.collection_handler.import_collection(filename)
        logger.info(result)
        print(f"\n{result}\n")

    def clear_collection(self):
        result = self.collection_handler.clear_collection()
        logger.info(result)
        print(f"\n{result}\n")

    def export_collection(self):
        filename = input(f"Enter the filename to export (default: {self.default_filename}): ") or self.default_filename
        result = self.collection_handler.export_collection(filename)
        logger.info(result)
        print(f"\n{result}\n")

    def exit_program(self):
        logger.info("Exiting the program.")
        self.keep_going = False

    def process_user_choice(self, user_choice):
        options = {
            "add": self.add_game,
            "add game": self.add_game,
            "view": self.view_collection,
            "view collection": self.view_collection,
            "import": self.import_collection,
            "clear": self.clear_collection,
            "export": self.export_collection,
            "exit": self.exit_program,
            "quit": self.exit_program,
        }

        try:
            options.get(user_choice, self.handle_invalid_choice)()
        except KeyboardInterrupt:
            logger.warning("KeyboardInterrupt detected.")
            print("\nYou're gonna have to try better than that.\n")

    def handle_invalid_choice(self):
        logger.warning("Invalid Selection.")
        print("Invalid Selection. Please Try Again.")

    def run(self):
        while self.keep_going:
            self.display_menu()
            user_choice = self.get_user_choice()
            self.process_user_choice(user_choice)

if __name__ == "__main__":
    interface = Interface()
    interface.run()
