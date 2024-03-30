import logging
import pandas as pd


def load_history(history_file, history_manager):
    """Loads and prints the history from the specified CSV file."""
    try:
        # Load history from the CSV file
        history_df = pd.read_csv(history_file)
        # Check if history is empty
        if not history_df.empty:
            print("History Entries:")
            print(history_df.to_string(index=True))
            logging.info("History was accessed.")
        else:
            logging.info("History is empty.")
            print("History is empty.")
    except FileNotFoundError:
        logging.info("History file not found.")
        print("History file not found.")
