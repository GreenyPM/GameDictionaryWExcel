from tabulate import tabulate
from loggerConfig import logger
import pandas as pd

class GameDict:
    def __init__(self, dictionary=None, pk=0):
        self.dictionary = dictionary or {}
        self.pk = pk

    def add_game_entry(self, platform, game):
        self.dictionary[self.pk] = [platform, game]
        self.pk += 1
        logger.info(f"Added {game} on {platform} to Dictionary")
        return

    def display_collection(self):
        if not self.dictionary:
            logger.info("There are currently no games in this collection")
            return

        headers = ["Platform", "Game"]
        table_data = [list(entry) for entry in self.dictionary.values()]

        logger.info("Viewing collection: ")
        print(tabulate(table_data, headers, tablefmt="fancy_grid"))
        return

    def import_collection(self, filename="output.xlsx"):
        try:
            imported_df = pd.read_excel(filename, index_col=0)  # Set index_col=0 to exclude the index column
            self.dictionary = {idx: list(row) for idx, row in imported_df.iterrows()}
            logger.info(f"Imported collection from {filename}.")
        except FileNotFoundError:
            logger.warning(f"File {filename} not found.")
        return

    def export_collection(self, filename="output.xlsx"):
        game_df = pd.DataFrame(self.dictionary.values(), columns=['Platform', 'Videogames'])
        with pd.ExcelWriter(filename) as writer:
            game_df.to_excel(writer)
        logger.info(f"Exported collection to {filename}")
        return

    def clear_collection(self):
        self.dictionary.clear()
        logger.info("Dictionary Cleared")
        return