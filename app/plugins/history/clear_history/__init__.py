import os
import pandas as pd


def clear_history(history_file, history_manager):
    """Clears all entries from the history."""
    # Clear history DataFrame
    history_manager.history_df = pd.DataFrame(columns=["Operation", "Result"])

    # Save the cleared DataFrame back to the file
    history_manager.history_df.to_csv(history_manager.history_file, index=False)

    print("History has been cleared.")
