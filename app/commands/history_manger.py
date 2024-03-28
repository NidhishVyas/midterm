# history_manager.py
import pandas as pd
import logging
import os
from dotenv import load_dotenv


class HistoryManager:
    def __init__(self, rel_path):
        load_dotenv()       
        abs_history_file = os.path.join(rel_path)
        self.history_file = abs_history_file
        self.history = self.load_history()

    def load_history(self):
        try:
            history = pd.read_csv(self.history_file)
            logging.info("History loaded successfully")
            return history
        except FileNotFoundError:
            logging.warning("History file not found, starting with empty history")
            return pd.DataFrame(columns=["Expression", "Result"])

    def save_history(self):
        self.history.to_csv(self.history_file, index=False)
        logging.info("History saved successfully")

    def clear_history(self):
        self.history = pd.DataFrame(columns=["Expression", "Result"])
        self.save_history()
        logging.info("History cleared")

    def delete_record(self, index):
        self.history.drop(index, inplace=True)
        self.save_history()
        logging.info("Record deleted successfully")

    def add_operation(self, expression, result):
        """Add a new operation to the history."""
        new_row = pd.DataFrame({"Expression": [expression], "Result": [result]})
        self.history = pd.concat([self.history, new_row], ignore_index=True)
        self.save_history()
        logging.info("Operation added to history successfully")
