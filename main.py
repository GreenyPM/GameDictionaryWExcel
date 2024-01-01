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
        self.display_welcome_message()

    def display_welcome_message(self):
        print("\n=== Welcome to the GAME COLLECTOR! ===")
        print("A fine application to track your games")

    def display_menu(self):
        print("\nPlease choose one of the options below:")
        print("- add (game)\n- view (collection)\n- import\n- clear\n- export\n- exit")

    def get_user_choice(self):
        return input("Your choice: ").lower()

    def add_game(self):
        platform_entry = input("Enter Name of Platform: ")
        game_entry = input("Enter Name of Game: ")
        self.collection_handler.add_game_entry(platform_entry, game_entry)

    def view_collection(self):
        self.collection_handler.display_collection()

    def import_collection(self):
        filename = input(f"Enter the filename to import (default: {self.default_filename}): ") or self.default_filename
        self.collection_handler.import_collection(filename)

    def clear_collection(self):
        self.collection_handler.clear_collection()

    def export_collection(self):
        filename = input(f"Enter the filename to export (default: {self.default_filename}): ") or self.default_filename
        self.collection_handler.export_collection(filename)

    def exit_program(self):
        logger.info("Exiting.")
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

    def handle_invalid_choice(self):
        logger.warning("Invalid Selection. Please Try Again.")

    def run(self):
        while self.keep_going:
            self.display_menu()
            user_choice = self.get_user_choice()
            self.process_user_choice(user_choice)

if __name__ == "__main__":
    interface = Interface()
    interface.run()
