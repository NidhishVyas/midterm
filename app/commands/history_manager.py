import os
import pandas as pd
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class HistoryManager:
    def __init__(self, rel_path):
        load_dotenv()
        # Ensure the history file path is absolute
        abs_history_file = os.path.abspath(rel_path)
        self.history_file = abs_history_file
        # Initialize or load the DataFrame
        try:
            # Attempt to read the history file
            self.history_df = pd.read_csv(self.history_file)
        except FileNotFoundError:
            # If the file does not exist, initialize DataFrame with column names
            self.history_df = pd.DataFrame(columns=["Operation", "Result"])
        except Exception as e:
            # Handle other possible exceptions
            print(f"An error occurred: {e}")
            # Initialize DataFrame with default values or handle error accordingly
            # For instance, you might want to initialize the DataFrame even if another type of error occurred
            self.history_df = pd.DataFrame(columns=["Operation", "Result"])

    def add_operation(self, num1, operation_type, num2, result):
        # Determine the symbol for the operation
        operation_symbol = {
            "add": "+",
            "subtract": "-",
            "multiply": "*",
            "divide": "/",
        }.get(operation_type, "?")

        # Format the operation string
        operation_str = f"{num1} {operation_symbol} {num2}"

        # Append the new operation to the DataFrame
        new_entry_df = pd.DataFrame({"Operation": [operation_str], "Result": [result]})
        self.history_df = pd.concat([self.history_df, new_entry_df], ignore_index=True)

        # Save to file with headers
        self.history_df.to_csv(self.history_file, index=True, header=True)
