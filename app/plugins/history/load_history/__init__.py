# Assuming history is stored in the same global list named 'history_entries'
# This variable should be defined in a shared location accessible by all modules.
import pandas as pd


history_entries = []


def load_history(history_file):
    """
    Loads and prints the history from the specified CSV file.
    """
    try:
        # Load history from the CSV file
        history_df = pd.read_csv(history_file)
        # Check if history is empty
        if not history_df.empty:
            print("History Entries:")
            print(history_df.to_string(index=True))
        else:
            print("History is empty.")
    except FileNotFoundError:
        print("History file not found.")
    except Exception as e:
        print(f"An error occurred while loading history: {e}")
